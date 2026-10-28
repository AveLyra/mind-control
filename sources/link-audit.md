# Source-link and publication-identity audit

[Home](../README.md) · [Citation recovery](citation-audit.md) · [Bibliography](bibliography.md) · [Machine results](link-audit.json)

Checked October 27, 2026, America/New_York. All **746 distinct source URLs** in `research/` and `wiki/` were included. URL variants can identify the same publication; this is not a study count. Private account/Drive links and literal-ellipsis examples are excluded. The generated bibliography indexes research-record URLs; the audit additionally covers wiki-only sources.

## Direct access results

| Result | URLs | Meaning |
|---|---:|---|
| Reachable | 339 | HTTP success with no recognized challenge in the sampled response; not full-text certification. |
| Access challenge | 230 | A browser/human-verification response, sometimes returned with HTTP 200. |
| Access restricted | 120 | HTTP 401, 403, or 429. |
| Redirect landing | 48 | An intermediary page rather than verified article content. |
| Request failed | 7 | TLS validation or another request error; verification was not disabled. |
| Other HTTP error | 2 | Two official guidance URLs returned 404 directly despite content retrieval through another channel. |

The [JSON report](link-audit.json) records the URL, contexts, observed status, redirect destination, available title, and metadata. HTTP 200 is not evidence that a scientific claim is true. Blocking is not evidence that an identifier is fictitious.

## Independent identity checks

- **467 URL identities** resolved through Europe PMC, Crossref, or DataCite metadata services. These are URL identities, not distinct studies or full-text reviews.
- **Three index misses** were independently matched through primary institutional or official records: Bauer’s cookie-banner study, van den Hout’s checking meta-analysis, and the generalizable speech-neuroprosthesis preprint. The failed API matches remain in the raw results alongside the successful checks.
- **All six NCT identifiers** were retrieved from ClinicalTrials.gov. The [registry receipt](trial-identity-checks.json) records titles, statuses, and source update dates. Other registry fields were not comprehensively reviewed; registration does not establish efficacy.
- Crossref identifies the `.sa2` eLife DOI as an **Assessment**. It is retained for the peer-review qualification, separately from the experimental article.

These checks support identification. Only selected claims received fresh substantive checks; historical estimates and conclusions remain subject to their original limitations.

## Repairs and access discrepancies

The [repair ledger](citation-recovery.json) preserves original targets and reasons. Changes include an encoded trailing space in a DOI, malformed Apple navigation, an outdated FTC page, a failed Folia mirror replaced by its publication DOI, and a removed Wikipedia draft-policy route replaced by current guidance. An Evans paper also received a separately verified PubMed access alternative, with the original mirror retained.

Apple’s Focus guidance and the FTC privacy guide were retrieved as official page content by the web source tool, while direct requests returned HTTP 404. Both observations are recorded; neither route is represented as uniformly accessible. The failed Folia mirror and old Wikipedia draft URL are historical failures in the repair ledger, not current source targets.

Seven legacy endpoints still failed direct TLS validation:

- [https://sleepdata.org/about](https://sleepdata.org/about)
- [https://sleepdata.org/datasets](https://sleepdata.org/datasets)
- [https://www.psych.upenn.edu/history/orne/evansetal1969jnmd467476.html](https://www.psych.upenn.edu/history/orne/evansetal1969jnmd467476.html)
- [https://www.psych.upenn.edu/history/orne/evansetal1970jnmd171187.html](https://www.psych.upenn.edu/history/orne/evansetal1970jnmd171187.html)
- [https://www.psych.upenn.edu/history/orne/orneetal1968jpsp189196.html](https://www.psych.upenn.edu/history/orne/orneetal1968jpsp189196.html)
- [https://www.psych.upenn.edu/history/orne/orneholland1968ijp282293.html](https://www.psych.upenn.edu/history/orne/orneholland1968ijp282293.html)
- [https://www.psych.upenn.edu/history/orne/sheehanetal1968jnmd209220.html](https://www.psych.upenn.edu/history/orne/sheehanetal1968jnmd209220.html)

Some Penn text was retrievable through indexed primary-source results, but live direct access remains unverified. A failed mirror does not remove the underlying historical study; it limits the available retrieval route.

## Reproduce

Run `python3 tools/audit_source_links.py --output sources/link-audit.json --refresh` for fresh HTTP/metadata checks, `python3 tools/reindex_collection.py` to refresh indexes and audit-report digests, then `python3 tools/verify_collection.py` for corpus coverage and integrity. Without `--refresh`, the auditor reuses same-day results and checks new URLs. It verifies TLS, limits response samples to 128 KiB, and uses bounded concurrency. Manual web and connector identity checks are separately dated and require repeating those retrievals; a CLI refresh alone does not reproduce them.

A full scientific audit would additionally inspect corrected publications, methods, outcome definitions, numerical claims, replication, and contrary findings. This report does not claim that work has been completed for every source.
