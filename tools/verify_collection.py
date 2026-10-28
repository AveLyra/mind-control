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
ancestry_status = 'retained_upload_excerpt_ancestry_identified_original_file_unavailable'
unidentified_status = 'editorial_cross_reference_original_attachment_unavailable'
unavailable = sum(r['status'] in {ancestry_status, unidentified_status} for r in markers)
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

# Shared text ancestry is narrower than recovering the original upload. Check
# the retained excerpts against the unchanged complete source, and preserve
# the unresolved reference and the original-file boundary explicitly.
upload_path = root / manifest['upload_ancestry_recovery']['report']
upload = json.loads(upload_path.read_text())
if hashlib.sha256(upload_path.read_bytes()).hexdigest() != manifest['upload_ancestry_recovery']['report_sha256']:
    errors.append('Upload-ancestry report digest disagrees with manifest')
expected_upload_summary = {
    'references_reviewed': 50,
    'high_confidence_text_ancestry_identified': 49,
    'source_identity_unresolved': 1,
    'original_file_bytes_unavailable_references': 50,
    'original_uploaded_files_fully_restored': 0,
    'answers_with_matching_retained_excerpts': 5,
    'distinct_matching_excerpts': 3,
}
if (upload['summary'] != expected_upload_summary
        or upload['summary'] != manifest['upload_ancestry_recovery']['summary']
        or upload['summary'] != citation_report['upload_ancestry_recovery']['summary']):
    errors.append('Upload recovery limits or summary are inconsistent')
if (manifest['citation_audit']['upload_text_ancestry_identified'] != 49
        or manifest['citation_audit']['file_style_source_identity_unresolved'] != 1):
    errors.append('Manifest does not distinguish upload ancestry from unidentified source')
source = upload['ancestral_source']
source_record = record_by_id[source['record_id']]
source_text = (root / source_record['path']).read_text()
if source['path'] != source_record['path'] or source['published_sha256'] != source_record['sha256']:
    errors.append('Ancestral source identity or digest mismatch')
source_plain = re.sub(r'\[source \d+\]\([^\n)]+\)', '', source_text)
source_plain = re.sub(r'\[([^\]]+)\]\([^\n)]+\)', r'\1', source_plain)
normalize = lambda text: re.sub(r'\W+', '', text).lower()
source_normalized = normalize(source_plain)
excerpts = {excerpt['id']: excerpt for excerpt in upload['excerpts']}
if len(excerpts) != 3 or len(upload['excerpts']) != 3:
    errors.append('Expected three distinct retained upload excerpts')
upload_prose = (root / 'sources/upload-recovery.md').read_text()
for excerpt in excerpts.values():
    quote = excerpt['plain_text']
    normalized = normalize(quote)
    offset = source_normalized.find(normalized)
    if (len(normalized) < 300 or len(normalized) != excerpt['normalized_characters']
            or offset < 0 or offset != excerpt['normalized_offset_in_published_source']
            or hashlib.sha256(quote.encode()).hexdigest() != excerpt['plain_text_sha256']):
        errors.append('Retained excerpt does not match ancestral source: ' + excerpt['id'])
    if normalized not in normalize(upload_prose):
        errors.append('Retained excerpt absent from human-readable recovery report: ' + excerpt['id'])
    for index in excerpt['retained_original_citation_indices']:
        if not re.search(r'\[source ' + re.escape(index) + r'\]\(', source_text):
            errors.append('Retained citation index absent from ancestral source: ' + index)
expected_counts = {
    '8349b528-8aa3-4ce7-928b-a6bfe15f92bc': 8,
    '710556a1-7594-4b91-b9b4-03d2dca491d5': 9,
    '1a6c75ff-4601-4f88-b959-4cdec13997eb': 19,
    '92060796-96e7-421a-a090-bc6e03558358': 8,
    '5a68e43a-789c-474b-8761-83e97c4fcf5a': 5,
}
seen_upload_keys = set()
if len(upload['answers']) != 5 or {a['message_id'] for a in upload['answers']} != set(expected_counts):
    errors.append('Upload receipts do not identify the five original affected answers')
for answer in upload['answers']:
    record_id, message_id = answer['record_id'], answer['message_id']
    source_indices = answer['citation_indices']
    if (len(source_indices) != expected_counts.get(message_id)
            or len(set(source_indices)) != len(source_indices)
            or answer['excerpt_id'] not in excerpts
            or answer['original_file_bytes_recovered'] is not False
            or answer['files_listed_in_answer_source_panel'] != 1
            or answer['displayed_file_name'] != 'Pasted text.txt'):
        errors.append('Invalid answer-level upload receipt: ' + message_id)
    controls = answer['original_citation_controls']
    snapshot = record_by_id[record_id]['citation_audit']['source_snapshot']
    if (controls['indices'] != source_indices or controls['count'] != len(source_indices)
            or controls['all_preview_labels'] != 'Open preview of Pasted text.txt'
            or controls['private_source_text_sha256'] != snapshot['rendered_text_sha256']
            or controls['private_source_html_sha256'] != snapshot['rendered_html_sha256']):
        errors.append('Original citation controls disagree with source snapshot: ' + message_id)
    answer_text = (root / record_by_id[record_id]['path']).read_text()
    for index in source_indices:
        key = record_id, index
        seen_upload_keys.add(key)
        marker = next((m for m in markers if (m['record_id'], m['source_index']) == key), None)
        if (marker is None or marker['status'] != ancestry_status
                or marker.get('original_file_bytes_recovered') is not False
                or marker.get('original_citation_recovered') is not False
                or marker.get('source_text_ancestry_identified') is not True
                or marker.get('ancestral_record_id') != source['record_id']
                or marker.get('ancestry_receipt_message_id') != message_id
                or source['path'] not in marker.get('targets', [])):
            errors.append('Upload ancestry disposition lacks a matching receipt: ' + str(key))
        expected_link = f'[upload ancestry {index}](../../sources/upload-recovery.md#receipt-{message_id})'
        if expected_link not in answer_text:
            errors.append('Upload ancestry receipt absent from cited answer: ' + str(key))
if seen_upload_keys != {(m['record_id'], m['source_index']) for m in markers if m['status'] == ancestry_status}:
    errors.append('Upload receipt coverage disagrees with citation ledger')
unidentified = upload['unidentified_reference']
unidentified_keys = {(m['record_id'], m['source_index']) for m in markers if m['status'] == unidentified_status}
if (unidentified_keys != {(unidentified['record_id'], unidentified['ledger_source_index'])}
        or unidentified['raw_reference'] != 'turn3file2'
        or unidentified['rendered_reference_text'] != ''
        or unidentified['mapping_to_specific_source_observed'] is not False):
    errors.append('The separate unidentified source gap is not preserved')
if (upload['backup_checks']['indexed_attachment_originals_read'] != 36
        or upload['backup_checks']['attachment_digests_matching_inventory'] != 36
        or upload['backup_checks']['lossless_multipart_archive_downloaded'] is not False
        or upload['original_upload_access']['file_id_or_original_bytes_recovered'] is not False):
    errors.append('Upload or backup recovery limits changed without new evidence')

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
print(f"PASS: {len(ids)} records; SHA-256 digests match; {checked} local links resolve; six recovery receipts; 471 citation dispositions; 49 upload-ancestry mappings / three matched excerpts / one unidentified source; {len(current_urls)} audited source URLs; six registry identities; no uncatalogued research or matched private URLs/credentials.")
