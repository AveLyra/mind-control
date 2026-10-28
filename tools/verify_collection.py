"""Check public collection navigation and immutable published-record digests."""
from pathlib import Path
from urllib.parse import unquote
from collections import Counter
from audit_source_links import canonical_url, source_urls
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'sources/manifest.json').read_text())
errors = []
ids = set()
for record in manifest['records']:
    if record['id'] in ids:
        errors.append('Duplicate ID: ' + record['id'])
    ids.add(record['id'])
    path = root / record['path']
    if not path.is_file():
        errors.append('Missing record: ' + record['path'])
    elif hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']:
        errors.append('Digest mismatch: ' + record['path'])

receipts = manifest.get('supplementary_recovery', {}).get('original_truncations_recovered', [])
if len(receipts) != 6 or len({r['message_id'] for r in receipts}) != 6:
    errors.append('Expected recovery receipts for six distinct original truncated messages')
for receipt in receipts:
    record = next((r for r in manifest['records'] if r['id'] == receipt['record_id']), None)
    if record is None or 'TRUNCATED' in record['status']:
        errors.append('Missing or still-truncated recovery: ' + receipt['record_id'])
    if not receipt.get('cutoff_tail_matched') or receipt.get('normalized_characters_beyond_cutoff', 0) <= 0:
        errors.append('No recorded continuation beyond old cutoff: ' + receipt['record_id'])
    if receipt.get('shared_opening_normalized_characters', 0) < 3500:
        errors.append('Insufficient recorded opening comparison: ' + receipt['record_id'])

checked = 0
for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    text = path.read_text()
    for target in re.findall(r'\]\(([^\n]+?)\)', text):
        target = target.strip().strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
            continue
        target = unquote(target.split('#', 1)[0])
        checked += 1
        if not (path.parent / target).exists():
            errors.append(f'{path.relative_to(root)}: missing link {target}')
    if re.search(r'https?://drive\.google\.com/', text):
        errors.append(f'{path.relative_to(root)}: private backup URL in public Markdown')
    if re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY', text):
        errors.append(f'{path.relative_to(root)}: possible credential')
    if re.search(r'\[citation marker unresolved in (?:reader|recovered chat)\]|\[unresolved source \d+\]|:chatgpt-content-reference\{', text):
        errors.append(f'{path.relative_to(root)}: unexplained citation placeholder')
    if re.search(r'/Users/admin/|\]\(sandbox:', text):
        errors.append(f'{path.relative_to(root)}: private workspace reference')

record_by_id = {record['id']: record for record in manifest['records']}
citation_report_path = root / 'sources/citation-recovery.json'
citation_report = json.loads(citation_report_path.read_text())
if hashlib.sha256(citation_report_path.read_bytes()).hexdigest() != manifest['citation_audit']['ledger_sha256']:
    errors.append('Citation-ledger digest disagrees with manifest')
markers = citation_report['markers']
if len(markers) != 471 or len({(r['record_id'], r['source_index']) for r in markers}) != 471:
    errors.append('Expected 471 distinct original citation-marker dispositions')
if dict(Counter(r['status'] for r in markers)) != citation_report['summary']:
    errors.append('Citation disposition summary disagrees with marker ledger')
if citation_report['summary'] != manifest['citation_audit']['dispositions']:
    errors.append('Manifest and citation ledger disagree')
unavailable = sum(r['status'] == 'editorial_cross_reference_original_attachment_unavailable' for r in markers)
if unavailable != 50 or unavailable != manifest['citation_audit']['original_uploaded_file_references_unrecovered']:
    errors.append('Unavailable original upload references are not consistently disclosed')
repairs = {(r['record_id'], r['old_url']): r.get('new_url', r['old_url']) for r in citation_report['link_repairs']}
for marker in markers:
    record = record_by_id.get(marker['record_id'])
    if record is None:
        errors.append('Citation refers to unknown record: ' + marker['record_id'])
        continue
    text = (root / record['path']).read_text()
    urls = {canonical_url(u) for u in re.findall(r'https?://[^\s<>\]`"|]+', text)}
    for target in marker.get('urls', []):
        target = repairs.get((record['id'], target), target)
        if canonical_url(target) not in urls:
            errors.append(f"Citation target absent from {record['id']}: {target}")
    for target in marker.get('targets', []):
        if not (root / target).is_file():
            errors.append('Missing citation target: ' + target)

new_ids = manifest['deep_research_discovery']['new_record_ids']
if len(new_ids) != 16 or len(set(new_ids)) != 16 or any(i not in record_by_id for i in new_ids):
    errors.append('Deep-research discovery must identify 16 distinct included records')

link_report = json.loads((root / 'sources/link-audit.json').read_text())
for path_key, digest_key in [('report', 'report_sha256'), ('registry_report', 'registry_report_sha256')]:
    path = root / manifest['source_link_audit'][path_key]
    if hashlib.sha256(path.read_bytes()).hexdigest() != manifest['source_link_audit'][digest_key]:
        errors.append('Audit-report digest disagrees with manifest: ' + str(path.relative_to(root)))
current_urls = source_urls()
audited_urls = {r['url']: r for r in link_report['links']}
if set(current_urls) != set(audited_urls):
    errors.append(f'Link-audit coverage mismatch: {len(set(current_urls)-set(audited_urls))} missing; {len(set(audited_urls)-set(current_urls))} stale')
for url, paths in current_urls.items():
    if url in audited_urls and set(audited_urls[url]['record_paths']) != paths:
        errors.append('Link-audit context paths are stale: ' + url)
if dict(Counter(r['status'] for r in link_report['links'])) != link_report['summary']:
    errors.append('Link-audit status summary disagrees with URL records')
if link_report['summary'] != manifest['source_link_audit']['http_summary'] or len(current_urls) != manifest['source_link_audit']['unique_source_urls']:
    errors.append('Manifest and source-link report disagree')

trials = json.loads((root / 'sources/trial-identity-checks.json').read_text())['studies']
trial_urls = {r['source_url'] for r in trials}
if trial_urls != {u for u in current_urls if u.startswith('https://clinicaltrials.gov/study/')}:
    errors.append('Trial identity checks do not cover all cited NCT URLs')

tracked_research = {record['path'] for record in manifest['records']}
for path in (root / 'research').rglob('*'):
    if path.is_file() and str(path.relative_to(root)) not in tracked_research:
        errors.append('Uncatalogued research file: ' + str(path.relative_to(root)))
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f"PASS: {len(ids)} records; SHA-256 digests match; {checked} local links resolve; six recovery receipts; 471 citation dispositions; {len(current_urls)} audited source URLs; six registry identities; no uncatalogued research or matched private URLs/credentials.")
