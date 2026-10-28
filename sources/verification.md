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
