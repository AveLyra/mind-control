"""Audit published source URLs; HTTP access is distinct from claim verification."""
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode, unquote, quote
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter, defaultdict
from html import unescape
import argparse
import json
import re
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
AUDITOR_VERSION = 3
AUDIT_DATE = datetime.now(ZoneInfo('America/New_York')).date().isoformat()
HEADERS = {'User-Agent': 'MindControlResearchWiki-LinkAudit/1.0 (source-link verification)', 'Accept': 'text/html,application/pdf,application/json;q=0.9,*/*;q=0.8'}

def canonical_url(url):
    url = unescape(url).rstrip('.,;:')
    while url.endswith(')') and url.count(')') > url.count('('):
        url = url[:-1]
    p = urlsplit(url)
    if p.scheme not in ['http', 'https'] or not p.hostname:
        return None
    if p.hostname in ['chatgpt.com', 'drive.google.com', 'docs.google.com']:
        return None
    # Literal ellipses in example wikitext are illustrative, not source links.
    if '...' in p.path or '\u2026' in p.path:
        return None
    query = [(k, v) for k, v in parse_qsl(p.query) if not k.startswith('utm_')]
    return urlunsplit((p.scheme, p.netloc, p.path, urlencode(query), p.fragment))

def source_urls():
    sources = defaultdict(set)
    for folder in ['research', 'wiki']:
        for path in (ROOT / folder).rglob('*.md'):
            for match in re.finditer(r'https?://[^\s<>\]`"|]+', path.read_text()):
                url = canonical_url(match.group())
                if url:
                    sources[url].add(str(path.relative_to(ROOT)))
    return sources

def fetch(url, timeout=18, cap=131072):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as response:
        data = response.read(cap)
        content_type = response.headers.get('Content-Type', '')
        text = data.decode('utf-8', errors='replace') if 'pdf' not in content_type else ''
        title_match = re.search(r'<title[^>]*>(.*?)</title>', text, re.I | re.S)
        title = unescape(re.sub(r'<[^>]+>', '', title_match.group(1))).strip() if title_match else None
        lower = (title or '').lower() + ' ' + text[:20000].lower()
        challenge = any(term in lower for term in ['checking your browser', 'just a moment...', 'verify you are human', 'enable javascript and cookies to continue', 'request unsuccessful. incapsula', 'access denied', 'captcha challenge', 'client challenge', 'enable javascript to proceed'])
        status = 'access_challenge' if challenge else 'redirect_landing' if (title or '').lower() == 'redirecting' else 'reachable'
        return {'http_status': response.status, 'final_url': response.url, 'content_type': content_type, 'title': title, 'bytes_sampled': len(data), 'status': status, 'pdf_signature': data.startswith(b'%PDF') if 'pdf' in content_type else None}

def read_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as response:
        return json.load(response)

def doi_metadata(doi):
    """Non-biomedical articles and datasets need registration-agency metadata."""
    endpoint = 'https://api.crossref.org/works/' + quote(doi, safe='')
    try:
        r = read_json(endpoint)['message']
        return {'doi': r.get('DOI'), 'title': '; '.join(r.get('title', [])), 'authorString': '; '.join(' '.join([a.get('given', ''), a.get('family', '')]).strip() for a in r.get('author', [])), 'publication_date': r.get('published', {}).get('date-parts'), 'journalTitle': '; '.join(r.get('container-title', [])), 'type': r.get('type'), 'metadata_provider': 'Crossref', 'metadata_url': endpoint}
    except Exception:
        pass
    endpoint = 'https://api.datacite.org/dois/' + quote(doi, safe='')
    try:
        r = read_json(endpoint)['data']['attributes']
        return {'doi': r.get('doi'), 'title': '; '.join(t['title'] for t in r.get('titles', [])), 'pubYear': r.get('publicationYear'), 'type': r.get('types', {}).get('resourceTypeGeneral'), 'metadata_provider': 'DataCite', 'metadata_url': endpoint}
    except Exception:
        return None

def metadata_fallback(url):
    pmid = re.match(r'https?://pubmed.ncbi.nlm.nih.gov/(\d+)', url)
    pmc = re.match(r'https?://(?:pmc.ncbi.nlm.nih.gov/articles/|www.ncbi.nlm.nih.gov/pmc/articles/)(PMC\d+)', url)
    doi = re.match(r'https?://(?:dx\.)?doi.org/(.+)', url)
    query = None
    if pmid:
        query = 'EXT_ID:' + pmid.group(1) + ' AND SRC:MED'
    elif pmc:
        query = 'PMCID:' + pmc.group(1)
    elif doi:
        query = 'DOI:"' + unquote(doi.group(1)).strip() + '"'
    if query is None:
        return None
    endpoint = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urlencode({'query': query, 'format': 'json', 'pageSize': 1})
    try:
        doc = read_json(endpoint)
        results = doc.get('resultList', {}).get('result', [])
        if results:
            r = results[0]
            return {key: r.get(key) for key in ['id', 'source', 'pmcid', 'doi', 'title', 'authorString', 'pubYear', 'journalTitle']} | {'metadata_provider': 'Europe PMC', 'metadata_url': endpoint}
        if doi:
            registered = doi_metadata(unquote(doi.group(1)).strip())
            if registered:
                return registered
        return {'status': 'no_matching_record', 'metadata_url': endpoint}
    except Exception as exc:
        if doi:
            registered = doi_metadata(unquote(doi.group(1)).strip())
            if registered:
                return registered
        return {'status': 'metadata_unavailable', 'error': type(exc).__name__}

def audit_one(url, paths, locks):
    host = urlsplit(url).netloc
    result = {'url': url, 'record_paths': sorted(paths), 'checked_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'auditor_version': AUDITOR_VERSION}
    with locks[host]:
        try:
            result.update(fetch(url))
        except urllib.error.HTTPError as exc:
            result.update(http_status=exc.code, final_url=exc.url, status='access_restricted' if exc.code in [401, 403, 429] else 'http_error')
        except Exception as exc:
            result.update(status='request_failed', error=type(exc).__name__, error_detail=str(exc)[:200])
        # Bibliographic resolution is useful even when the target returns a challenge.
        if re.search(r'pubmed\.ncbi|pmc\.ncbi|doi\.org/', url):
            meta = metadata_fallback(url)
            if meta:
                result['bibliographic_metadata'] = meta
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=str(ROOT / 'sources/link-audit.json'))
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--refresh', action='store_true')
    args = parser.parse_args()
    urls = source_urls()
    output = Path(args.output)
    previous = {}
    if output.exists() and not args.refresh:
        prior_report = json.loads(output.read_text())
        if prior_report.get('audit_date') == AUDIT_DATE:
            previous = {r['url']: r for r in prior_report.get('links', [])}
    results = []
    todo = []
    for url, paths in urls.items():
        if url in previous:
            r = previous[url]; r['record_paths'] = sorted(paths)
            if (r.get('title') or '').lower() == 'redirecting' and r['status'] == 'reachable':
                r['status'] = 'redirect_landing'
            results.append(r)
        else:
            todo.append((url, paths))
    locks = defaultdict(lambda: threading.Semaphore(2))
    # Materialize locks before concurrent access.
    for url in urls:
        _ = locks[urlsplit(url).netloc]
    print(f'Auditing {len(todo)} URLs; reusing {len(results)} prior results.', flush=True)
    def save():
        report = {'audit_date': AUDIT_DATE, 'auditor_version': AUDITOR_VERSION, 'scope': 'All source HTTP(S) URLs in research and wiki Markdown, excluding account/Drive URLs and literal-ellipsis examples; no claim-level certification', 'summary': dict(Counter(r['status'] for r in results)), 'links': sorted(results, key=lambda r: r['url'])}
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(audit_one, url, paths, locks): url for url, paths in todo}
        for future in as_completed(futures):
            results.append(future.result())
            if len(results) % 25 == 0:
                save(); print(f'Checked {len(results)}/{len(urls)}: {dict(Counter(r["status"] for r in results))}', flush=True)
    save()
    print(f'Completed {len(results)} URL checks: {dict(Counter(r["status"] for r in results))}', flush=True)

if __name__ == '__main__':
    main()
