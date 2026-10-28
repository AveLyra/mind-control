"""Rebuild the catalog and URL index from the published research manifest."""
from pathlib import Path
from audit_source_links import canonical_url
import json
import re
import hashlib

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'sources/manifest.json').read_text())
records = manifest['records']
catalog = '''# Source catalog

[Wiki home](../README.md) · [Coverage and gaps](coverage.md) · [Citation audit](citation-audit.md) · [Link audit](link-audit.md) · [Recovery report](recovery.md)

These are research records, not independent replications. IDs preserve provenance without publishing private backup URLs. The six original reader truncations are recovered. Unavailable uploaded references, editorial supplements, and source-answer boundaries are recorded in the citation audit. Exact published derivatives are hashed in [manifest.json](manifest.json).

| ID / recovered research | Origin | Status |
|---|---|---|
'''
refs = {}
for r in records:
    catalog += f"| [{r['title']}](../{r['path']}) | {r['origin']} | {r['status']} |\n"
    text = (root / r['path']).read_text()
    for match in re.finditer(r'https?://[^\s<>\]`"|]+', text):
        url = canonical_url(match.group())
        if url is None:
            continue
        refs.setdefault(url,[]).append(r['path'])
(root / 'sources/catalog.md').write_text(catalog)
old = (root / 'sources/bibliography.md').read_text()
intro = old.split('## Recovered links')[0]
body = '## Recovered links\n\n'
for url, paths in sorted(refs.items()):
    body += f'- [{url}]({url}) — [recovered context](../{paths[0]})\n'
(root / 'sources/bibliography.md').write_text(intro + body)
# Audit files are generated evidence. Keep their manifest mirrors synchronized
# after an intentional refresh, without rehashing historical research records.
audit_path = root / 'sources/link-audit.json'
registry_path = root / 'sources/trial-identity-checks.json'
if audit_path.is_file() and registry_path.is_file():
    audit = json.loads(audit_path.read_text())
    manifest['source_link_audit'] = {
        'date': audit['audit_date'],
        'unique_source_urls': len(audit['links']),
        'http_summary': audit['summary'],
        'metadata_summary': audit.get('metadata_summary', {}),
        'report': 'sources/link-audit.json',
        'report_sha256': hashlib.sha256(audit_path.read_bytes()).hexdigest(),
        'registry_report': 'sources/trial-identity-checks.json',
        'registry_report_sha256': hashlib.sha256(registry_path.read_bytes()).hexdigest(),
    }
    (root / 'sources/manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
print(f'Reindexed {len(records)} records and {len(refs)} public source leads.')
