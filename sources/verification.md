# Collection verification

[Home](../README.md) · [Coverage](coverage.md)

Performed October 27, 2026:

- `python3 tools/verify_collection.py` — passed: 91 catalogued records; published SHA-256 digests match; 563 local Markdown links resolve; no uncatalogued research files or matched private backup URLs/credential patterns.
- `gitave diff --check` — passed before staging.
- Reviewed source selection for personal medical context, correspondence, private backup URLs, and local-file references. Explicit selection and visible omissions are documented in coverage; pattern checks cannot prove the absence of every sensitive detail.
- Paginated archived ChatGPT titles to the provider's end; topic-matching histories and the two older Codex dream histories were read as described in coverage.
- Confirmed the requested destination is the public `AveLyra/mind-control` repository and that the `ghave` profile authenticates as AveLyra. Default sandbox network failures were resolved by running the same identity functions with network access.

These checks validate packaging and provenance structure. They do not validate the scientific claims, certify all external links, reproduce historical runs, or establish exhaustive account coverage. Six collected account-reader answers are explicitly marked truncated; backup section boundaries may also interrupt an answer.

Git publication is verified separately against the committed hash and remote branch after pushing. Existing initial repository history is preserved.
