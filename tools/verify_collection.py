"""Check public collection navigation and immutable published-record digests."""
from pathlib import Path
from urllib.parse import unquote
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

tracked_research = {record['path'] for record in manifest['records']}
for path in (root / 'research').rglob('*'):
    if path.is_file() and str(path.relative_to(root)) not in tracked_research:
        errors.append('Uncatalogued research file: ' + str(path.relative_to(root)))
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f"PASS: {len(ids)} records; SHA-256 digests match; {checked} local links resolve; no uncatalogued research or matched private URLs/credentials.")
