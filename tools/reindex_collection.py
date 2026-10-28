"""Rebuild the catalog and URL index from the published research manifest."""
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
import json
import re

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'sources/manifest.json').read_text())
records = manifest['records']
catalog = '''# Source catalog

[Wiki home](../README.md) · [Coverage and gaps](coverage.md) · [Citation corrections](corrections.md) · [Recovery report](recovery.md)

These are research records, not independent replications. IDs preserve provenance without publishing private backup URLs. The six original truncated answers have been recovered. Other records can still contain unresolved citations or readable-backup section boundaries. Exact published derivatives are hashed in [manifest.json](manifest.json).

| ID / recovered research | Origin | Status |
|---|---|---|
'''
refs = {}
for r in records:
    catalog += f"| [{r['title']}](../{r['path']}) | {r['origin']} | {r['status']} |\n"
    text = (root / r['path']).read_text()
    for match in re.finditer(r'https?://[^\s<>\]`"|]+', text):
        url = match.group().rstrip('.,;:')
        while url.endswith(')') and url.count(')') > url.count('('):
            url = url[:-1]
        p = urlsplit(url)
        if not p.netloc or p.hostname in ['drive.google.com', 'chatgpt.com']:
            continue
        if p.hostname not in ['pubmed.ncbi.nlm.nih.gov', 'pmc.ncbi.nlm.nih.gov', 'doi.org', 'www.nature.com', 'www.science.org', 'www.intelligence.senate.gov', 'www.cia.gov', 'clinicaltrials.gov', 'physionet.org', 'www.jmir.org', 'www.frontiersin.org', 'journals.plos.org', 'www.publichealth.va.gov', 'jamanetwork.com', 'journals.sagepub.com', 'www.psych.upenn.edu', 'dxe.pubpub.org', 'www.uscourts.gov', 'docs.justia.com']:
            continue
        q = [(k,v) for k,v in parse_qsl(p.query) if not k.startswith('utm_')]
        url = urlunsplit((p.scheme,p.netloc,p.path,urlencode(q),p.fragment))
        refs.setdefault(url,[]).append(r['path'])
(root / 'sources/catalog.md').write_text(catalog)
old = (root / 'sources/bibliography.md').read_text()
intro = old.split('## Recovered links')[0]
body = '## Recovered links\n\n'
for url, paths in sorted(refs.items()):
    body += f'- [{url}]({url}) — [recovered context](../{paths[0]})\n'
(root / 'sources/bibliography.md').write_text(intro + body)
print(f'Reindexed {len(records)} records and {len(refs)} public source leads.')
