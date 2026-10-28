# Source-link and publication-identity audit

[Home](../README.md) · [Citation recovery](citation-audit.md) · [Bibliography](bibliography.md) · [Machine results](link-audit.json) · [New literature intake](awareness-update-intake.md)

Checked October 28, 2026, America/New_York. All **896 distinct source URLs** in `research/` and `wiki/` have direct-access and metadata attempts recorded for that date. The [combined-technique review](../research/updates/2026-10-28-combined-techniques.md) checked 20 newly cited URLs while preserving the 876 earlier same-day results and updating their context paths. This includes the supplied awareness-review artifacts, initial network checks, and topic-page links. URL variants can identify the same work; this is not a study count. Private account/Drive links and literal-ellipsis examples are excluded.

## Direct access results

| Result | URLs | Meaning |
|---|---:|---|
| Reachable | 405 | HTTP success without a recognized challenge in the sample; not full-text certification. |
| Access challenge | 281 | A browser or human-verification response, sometimes returned with HTTP 200. |
| Access restricted | 145 | HTTP 401, 403, or 429. |
| Redirect landing | 55 | An intermediary page rather than verified article content. |
| Request failed | 7 | TLS validation or another request error; verification was not disabled. |
| Other HTTP error | 3 | Two official guidance URLs returned 404; a supplied author-PDF route returned 503. |

The JSON report records each URL, research/wiki context paths, attempt time, status, redirect destination, sampled title, and available metadata. HTTP success does not establish scientific support for a claim; blocking does not establish an invalid identifier.

## Publication identities and separately dated checks

- **578 URL identities** resolved through Europe PMC, Crossref, or DataCite metadata in the same-day audits, including 13 new URL identities in the combination review. These are URL identities, not independent studies or complete full-text reviews.
- **1 remaining API index miss** retains a separately dated independent identity check from October 27. Earlier independent checks remain recorded even where a fresh API lookup now resolves the identity.
- **All 53 numbered references in the supplied continuation bibliography** passed title and DOI/PMID relationship checks. All 58 DOI-resolver URLs in those new records resolved bibliographic metadata. The version-3 eLife DOI and PubMed's base DOI identify one study; their alias is explicit in the [intake receipt](awareness-update-intake.json).
- The supplied update received selected primary-text checks, not a complete independent rereading of every paper or numerical table entry. Its FT/PFT/A labels describe the supplied reviewer. New independent checks are enumerated in the [intake report](awareness-update-intake.md).
- The initial research network checked 24 selected citation/abstract identities through the PubMed connector, retrieved two complete PMC bodies, and inspected selected relevant sections. Its three added URLs met direct-browser challenges despite successful metadata and connector retrievals. The [source-check record](../research/updates/2026-10-28-horizon-source-checks.md) preserves the full-text scope and failed Raz retrieval.
- The combination follow-up selected 16 publications, retrieved 13 complete PubMed abstracts and three complete PMC bodies, and inspected selected primary PDF/HTML sections. Of its 20 new URLs, 19 were directly reachable and one DOI route was restricted despite resolved Crossref identity. Publisher-PDF 403, institutional-PDF 429, connector failures, successful alternate primary routes, and preprint/final-version distinctions are explicit in the [new source record](../research/updates/2026-10-28-combined-techniques.md). These checks are not 16 independent full-text reviews or experiments.
- The **six ClinicalTrials.gov identity receipts remain dated October 27**. Their direct source URLs were included in this refresh, but the earlier connector retrievals and trial fields were not rerun. See the [registry receipt](trial-identity-checks.json).
- Earlier independent web-content checks for Apple Focus guidance and the FTC privacy guide retain their October 27 dates. Their direct requests still returned 404; these are separately dated observations from different access routes.

## Repairs and remaining access limits

The [repair ledger](citation-recovery.json) preserves earlier original targets, replacements, and reasons. This refresh does not silently rewrite historical source claims or remove failed access attempts. The newly supplied Meyen author-PDF route returned HTTP 503; the bibliography also provides DOI and PubMed identity alternatives. A transient author-copy failure does not establish a missing or invalid study.

Seven endpoints failed direct requests in this pass:

- [https://sleepdata.org/about](https://sleepdata.org/about) — URLError
- [https://sleepdata.org/datasets](https://sleepdata.org/datasets) — URLError
- [https://www.psych.upenn.edu/history/orne/evansetal1969jnmd467476.html](https://www.psych.upenn.edu/history/orne/evansetal1969jnmd467476.html) — URLError
- [https://www.psych.upenn.edu/history/orne/evansetal1970jnmd171187.html](https://www.psych.upenn.edu/history/orne/evansetal1970jnmd171187.html) — URLError
- [https://www.psych.upenn.edu/history/orne/orneetal1968jpsp189196.html](https://www.psych.upenn.edu/history/orne/orneetal1968jpsp189196.html) — URLError
- [https://www.psych.upenn.edu/history/orne/orneholland1968ijp282293.html](https://www.psych.upenn.edu/history/orne/orneholland1968ijp282293.html) — URLError
- [https://www.psych.upenn.edu/history/orne/sheehanetal1968jnmd209220.html](https://www.psych.upenn.edu/history/orne/sheehanetal1968jnmd209220.html) — URLError

These failures limit live direct access. They do not erase identifiable underlying studies or certify another access route. Earlier manual identity and web-content checks have not been relabeled as newly performed work.

## Reproduce

Run `python3 tools/audit_source_links.py --output sources/link-audit.json --refresh` for fresh HTTP/metadata checks, `python3 tools/reindex_collection.py` for indexes and audit-report digests, and `python3 tools/verify_collection.py` for corpus coverage and integrity. The auditor verifies TLS, caps samples at 128 KiB, and uses bounded concurrency. Without `--refresh`, it reuses same-day results. Manual and connector checks are separately dated; a CLI refresh does not reproduce them.

Scientific verification still requires methods, corrected publications, numerical extraction, replication, and disconfirming evidence. This access report does not certify all substantive claims.
