# Lossless-backup recovery audit

[Home](../README.md) · [Upload recovery](upload-recovery.md) · [Machine-readable receipt](lossless-backup-audit.json) · [Coverage](coverage.md)

Audit date: October 28, 2026, America/New_York. **The entire multipart Codex backup was retrieved, authenticated, and searched. It did not identify the missing ChatGPT uploads or resolve `turn3file2`.** The 49 previously established shared-text ancestry matches remain valid; the original upload bytes and one source identity remain unavailable.

## What was actually recovered and checked

| Check | Result |
|---|---:|
| Downloaded archive parts, each matching its recorded size and SHA-256 | 16 |
| Combined compressed bytes | 1,576,145,931 |
| Archive files read | 253 |
| Uncompressed file bytes read | 3,766,552,745 |
| Original source files matching the inventory digests | 215 |
| Generated metadata/index files | 38 |
| Session JSONL files parsed | 179 |
| Session JSONL rows parsed | 349,488 |
| History/metadata rows parsed | 105,664 |
| JSONL parsing errors | 0 |
| Identified Codex attachment originals restored privately and hash-verified | 36 |
| Restored attachments matching the retained ChatGPT upload excerpts | 0 |

The compressed archive’s SHA-256 is `e19fd8ab9b5c366379e3fa6d268ff1c365a9acaeec4163f7ca7caf0f9cb05972`, matching both the remote manifest and the existing recovery record. The 179 session files include the archived logs and required base data. The archive was read as a stream across the ordered parts; no live Codex database or chat store was overwritten.

All 215 original source-file digests matched the inventory. Thirty-seven generated companion files also matched their retained local copies. The remaining generated file, `metadata.jsonl`, is authenticated by the complete archive hash; its standalone digest was recorded, every row parsed, and its per-table counts matched the original inventory. This distinguishes a newly recorded member digest from a comparison with a previously recorded digest.

The metadata includes 102,914 history items, 2,354 turns, and the other tables listed in the machine-readable receipt. The selected attachment-table snapshot has zero rows, while 36 identified attachment files are present separately in the archive. Neither fact establishes preservation of ChatGPT’s attachment objects.

## Searches and results

Every file was searched for the raw reference `turn3file2`; the four relevant ChatGPT conversation IDs; the original optical-answer, proposal, upload-card, and five sleeping-answer IDs; distinctive retained optical passages; and the proposal’s awareness wording. All of those exact identifier/passage searches returned **zero matching lines**. The two awareness-paper DOIs used as editorial supplements also returned no matches; they were never treated as original-source mappings.

JSONL rows were parsed so escaped strings and nested serialized history items could be inspected, to depth six. Named base64 fields up to 50 MB were eligible for UTF-8 decoding; none was processed. This is a text/structured-record search, not a claim to recognize every possible encoding or interpret images.

Broader optical terms returned 591 candidate lines. Grouping bounded contexts by content and source-project ancestry, with targeted review of research-related and ambiguous contexts, produced:

| Candidate context | Lines |
|---|---:|
| Literary text or literary-project context | 493 |
| Software display behavior or issue listings | 74 |
| Existing optical research note | 4 |
| Other biomedical, sleep, or hypnosis sources | 19 |
| Accidental substring inside encoded binary text | 1 |

These counts can repeat the same underlying item in a raw log and history metadata. They are search hits, not independent sources or studies. Generic pasted-text filenames likewise do not identify the missing upload.

The relevant positive match is the [existing optical sleep-influence note](../research/notes/vindication-optical-sleep-influence-research.md). A historical command-output record contains its **exact 3,334-byte body**, matching the published record after its collection header. Its body SHA-256 is `2ba077493b7f8e6ad91c4381ce1a407216d15ed999a91b1deb12afb7cf0df23d`. This confirms an existing Codex note; it does not recover the different uploaded optical review. No historical command was executed.

All 36 archived attachment files were restored into private recovery storage: 35 pasted-text files and `goal.md`. Their bytes match the backup inventory. Comparing their full text with the three normalized retained upload excerpts found no match. Restoring these identified Codex originals therefore adds no recovered target ChatGPT upload.

## What the result establishes

This pass closes the earlier gap in which the multipart archive itself had not been inspected. It supplies a verified search of that specific backup, including raw tool records and history data omitted from the readable projections. Private receipts record the archive, part and member hashes, table counts, search queries, candidate review, and attachment comparisons. The public receipt contains selected counts and hashes rather than unrelated account material.

**The main limitation is the backup’s scope:** it is an October 11 selected **Codex** snapshot, not an export of the ChatGPT account. Negative results here cannot establish that the original uploads are absent from ChatGPT, another backup, an omitted source, or an unrecognized encoding. The observed source data do not support reconstructing an unknown original file or assigning `turn3file2` to a particular paper or past chat.

The remaining source requirement is the original ChatGPT attachment data or an account export that actually includes those bytes, together with an identifiable mapping for `turn3file2`. A conversation-text export may still omit attachments. No raw chats, unrelated attachment contents, private account/Drive URLs, authenticated download references, or workspace paths were published. Downloaded parts, restored attachments, and private receipts are retained; nothing was deleted.
