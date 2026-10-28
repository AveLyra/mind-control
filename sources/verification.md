# Collection verification

[Home](../README.md) · [Coverage](coverage.md)

Initial collection checks, October 27, 2026:

- `python3 tools/verify_collection.py` — passed: 91 catalogued records; published SHA-256 digests match; 563 local Markdown links resolve; no uncatalogued research files or matched private backup URLs/credential patterns.
- `gitave diff --check` — passed before staging.
- The first staged whitespace check found trailing spaces inherited from chat Markdown. The initial publication command continued despite that failure. A follow-up formatting commit strips those spaces, refreshes affected manifest digests, and reruns the staged check. Published history is preserved.
- Reviewed source selection for personal medical context, correspondence, private backup URLs, and local-file references. Explicit selection and visible omissions are documented in coverage; pattern checks cannot prove the absence of every sensitive detail.
- Paginated archived ChatGPT titles to the provider's end; topic-matching histories and the two older Codex dream histories were read as described in coverage.
- Confirmed the requested destination is the public `AveLyra/mind-control` repository and that the `ghave` profile authenticates as AveLyra. Default sandbox network failures were resolved by running the same identity functions with network access.

These initial checks validated packaging and provenance structure. At the first publication, six account-reader answers were marked truncated; those six are now resolved by the supplementary recovery below. Backup section boundaries in other records can still interrupt an answer.

Supplementary recovery checks, October 27, 2026:

- Verified six matching source message IDs and matching normalized openings of 3,809–4,000 characters. For every target, the final 500 normalized characters of its old prefix occur in the recovered text with additional content afterward. Text and HTML snapshot digests and old published digests are retained in the manifest.
- Recovered three additional long answers discovered during the supplementary search before publishing them. No collected record remains flagged as reader-truncated.
- `python3 tools/reindex_collection.py` — regenerated the catalog and public-source index: 128 records and 377 URL leads. URL parsing preserves balanced parentheses and removes tracking query parameters.
- `python3 tools/verify_collection.py` — passed for source hashes, local links, six recovery receipts, research-file coverage, and the existing private-URL/credential patterns. The verifier checks recorded recovery receipts; it does not independently refetch the live account.
- Reviewed supplementary selection for personal medical context, unrelated fictional narrative, hypothetical targeting budgets, correspondence, private URLs, and unresolved control markers. No files or histories were deleted.

The checks do not validate the scientific claims, certify every external link, reproduce experiments, establish complete citation recovery, or establish exhaustive account coverage. Private DOM captures remain outside the public repository. See the recovery and coverage pages for scope and limitations.

Git publication is verified separately against the committed hash and remote branch after pushing. Existing initial repository history is preserved.

Citation and deeper-discovery checks, October 27, 2026:

- The signed-in **deep research** result list was paginated to its observed end at 172 chats. Relevant reader results, rendered messages, and the generated evidence archive were reviewed privately; 16 selected records were added.
- Private snapshot verification checked all 411 original public-citation mappings by conversation ID, message ID, citation index, and normalized primary URL: zero missing snapshots and zero mismatches. Per-record text/HTML snapshot digests and a verification-receipt digest are recorded. This checks retrieval, not whether a cited paper supports every sentence.
- `tools/audit_source_links.py` checked 746 distinct source URLs through full and incremental runs. Final direct-access results: 339 reachable, 230 access challenges, 120 restricted, 48 redirect landing pages, seven request failures, and two HTTP errors. The two official guidance pages were independently retrieved through the web source tool; the access disagreement remains explicit.
- Bibliographic services resolved 467 URL identities. Three index misses were independently matched against institutional or official publication records. All six cited NCT identities were retrieved using ClinicalTrials.gov. Counts refer to URL identities, not independent studies or complete full-text reviews.
- `python3 tools/reindex_collection.py` regenerated the catalog and expanded source index: 144 records and 742 source URLs in research records. Four additional wiki-only URLs bring the access-audit scope to 746.
- `python3 tools/verify_collection.py` passed for research digests, local links, the six original recovery receipts, all 471 citation dispositions, audit coverage/context paths, and the six registry identities. Fifty original upload references remain unrecovered and visibly labeled as editorial supplements. No generic unresolved citation placeholders remain.
- `gitave diff --check` passed. The fetched remote `main` matched the pre-update local base, `677a21ef2b5ee080427bf05c96648e9de4f1cef7`.
- Rechecked publication selection for private case context, account/backup links, workspace paths, and credential patterns. No files, chats, histories, or caches were deleted. Pattern checks supplement manual review; they do not prove the absence of every sensitive detail.

The manifest hashes the citation ledger, link-audit report, and registry receipt. Reindexing refreshes generated audit-report digests after an intentional new audit; it does not silently rehash historical research records. The original source-answer ending that stops mid-sentence is explicit and was not completed by inference.

Upload-source investigation checks, October 28, 2026:

- Reviewed all 50 file-style references. Five original answer snapshots contain 49 citation controls with the exact preview label **Open preview of Pasted text.txt**. Their indices and source text/HTML digests agree with the existing ledger and manifest.
- Captured the five answer-specific Sources panels. Their three distinct retained excerpts match the complete optical review after the documented normalization, including original embedded citation indices 29 and 44–47. The checked-in verifier reproduces the text matches and validates all 49 ancestry mappings, per-answer counts, source hashes, and report digests.
- The separate proposal’s rendered citation index 2 is empty. Its Sources panel lists two past chats and 24 web sources without identifying `turn3file2`. That one source identity remains unresolved; describing it as a definite upload was corrected.
- Verified all 36 indexed attachment originals against their backup inventory SHA-256 digests. Four distinctive optical phrases returned no matches in those attachments or 333 cached readable backup/catalog files. The multipart lossless archive was not downloaded or searched. Original upload preview and download attempts yielded no file bytes.
- `python3 tools/reindex_collection.py` and `python3 tools/verify_collection.py` passed: 144 research records, the six original truncation receipts, 471 citation dispositions, 49 ancestry mappings, three matching excerpts, one unidentified source, all local Markdown links, 746 source-URL audit entries, and six registry identities. The verifier checks the recorded evidence and its consistency; it does not refetch the private account.
- Source URLs and their research/wiki context paths are unchanged. The October 27 external access report remains the recorded audit; this upload investigation did not rerun all external HTTP requests. All editorial supplements remain explicitly labeled.
- Confirmed the AveLyra GitHub CLI account and the `AveLyra/mind-control` remote before publication. Reviewed the changed research records and public receipts for private backup/account links, workspace paths, unrelated library contents, and credential patterns. Private evidence stays outside Git. No files, chats, histories, caches, or backups were deleted.

The [new receipts](upload-recovery.md) establish shared text ancestry, not complete uploaded-file recovery. All original upload bytes and the citation-specific passages remain unavailable. No new scientific result or experiment is claimed.
