> Archived research note from Faraday workspace; recovered 2026-10-27. Original claims and status are historical and were not rerun in this collection pass.

[Wiki home](../../README.md) · [Source catalog](../../sources/catalog.md)

# Sleep-EDF Pink-Noise Dry Run Results

Run date: 2026-09-11

This was a non-human dry run over public Sleep-EDF Expanded hypnogram files. It
did not deliver sound, alter sleep, or analyze biological response. The only
outcome values were synthetic, used to exercise scheduling, hashing, sham
controls, and result reporting.

The initial two-recording run was expanded first to 24 cassette hypnograms and
then to all 153 cassette hypnograms discovered from the PhysioNet public index.
The full-index run is the main result below.

## Inputs

- Source dataset: Sleep-EDF Expanded hypnogram EDF+ files from PhysioNet
- Files: all 153 Sleep-EDF cassette hypnogram files discovered from the
  PhysioNet public index, `SC4001EC-Hypnogram.edf` through
  `SC4822GC-Hypnogram.edf`
- Simulation seed: `20260911`
- Maximum selected markers per condition per recording: `60`

## Source Hashes

Source hashes are retained in
`workspaces/vindication-machine/sleep-edf/results-full/sleep-pink-noise-dry-run-results.json`.
The original two-recording source hashes were:

- `SC4001EC-Hypnogram.edf`: `a4cf67694ade1b52a0ddd06d5817fd45d2d3e8bac5302f640f3e9cfbbf12a996`
- `SC4011EH-Hypnogram.edf`: `5bbf7b4ed8a95c8d20e4347b08c2ded2ee21e2dac4680dedf629795adc2edc83`

## Stage Minutes

Full 153-recording sample:

- N1: 10761.0 minutes
- N2: 34566.0 minutes
- N3: 6519.5 minutes
- REM: 12917.5 minutes
- Wake: 142968.5 minutes
- Unknown: 12523.5 minutes
- N3-to-N2 stage-time ratio: 0.1886
- N3-to-REM stage-time ratio: 0.5047

## Marker Counts

Selected synthetic markers in the full-index run:

- Simulated slow-wave pink-noise markers: 2572
- Random N2 sham markers: 9169
- REM off-target markers: 7330
- Total marker rows including CSV header: 19072

The generated marker CSV SHA-256 was:

`434c589c4c6c5b9460c6e6ba7c879cc0ee20c1912d3487e0656e15abfb0923aa`

A replay with the same seed and source files reproduced the same marker CSV
SHA-256.

## Feasibility Findings

The dry run can support design-feasibility conclusions because those are derived
from real hypnogram timing rather than from the synthetic outcome values.

Across the 153-recording full-index sample under the standard rule
30-second edge buffer and 90-second spacing:

- Candidate N2 sham windows: 20792
- Candidate N3 slow-wave simulation windows: 2659
- Candidate REM off-target windows: 8083
- N3 candidate count as a share of N2 candidate count: 0.1279
- N3 candidate count as a share of REM candidate count: 0.3290
- Median N2 candidates per recording: 135
- Median N3 candidates per recording: 11
- Median REM candidates per recording: 53
- Recordings with no eligible N3 candidates: 39 of 153
- Share of N3 minutes in the first sleep third: 0.5321

Design implication: N3 availability is the practical bottleneck for a slow-wave
cueing protocol. A future balanced design that compares N3 pink-noise windows
against N2 sham windows would need to discard many eligible N2 windows, stratify
by night, enrich nights with enough N3, accept unequal condition sizes, or
switch to an adaptive design that treats cue opportunity as the estimand's
denominator. Strict per-recording equality across N3, N2, and REM is impossible
in this full-index sample because 39 recordings have zero eligible N3 windows
under the standard rule.

Sensitivity to scheduling rules:

- Dense rule, 15-second buffer and 60-second spacing: 4936 N3 candidates, N3/N2 share 0.1509
- Standard rule, 30-second buffer and 90-second spacing: 2659 N3 candidates, N3/N2 share 0.1279
- Conservative rule, 60-second buffer and 120-second spacing: 1342 N3 candidates, N3/N2 share 0.0969
- Very conservative rule, 120-second buffer and 180-second spacing: 499 N3 candidates, N3/N2 share 0.0660

This suggests that stricter safety buffers and wider spacing do not merely
reduce sample size; they disproportionately reduce the already scarce N3
condition relative to N2 sham opportunities.

## Synthetic Contrasts

These contrasts use synthetic values and do not estimate sleep or memory effects.

- Mean simulated lapse, slow-wave pink-noise condition: 1.1946
- Mean simulated lapse, random N2 sham condition: 1.0008
- Mean simulated lapse, REM off-target condition: 0.8008
- Slow-wave minus N2 sham synthetic contrast: 0.1937
- Slow-wave minus REM off-target synthetic contrast: 0.3938

These numbers are intentionally not substantive findings. The synthetic generator
was configured with different condition means to exercise the analysis path.

## Claim Ledger

| Claim | Type | Grade | Why |
| --- | --- | --- | --- |
| The parser extracted sleep-stage annotations from 153 public Sleep-EDF hypnogram files. | Observed/computational | A | Reproducible from local source files and parser output. |
| The marker schedule is deterministic for the same source files and seed. | Computational | A | Replay reproduced marker CSV SHA-256 `434c589c4c6c5b9460c6e6ba7c879cc0ee20c1912d3487e0656e15abfb0923aa`. |
| N3 scheduling opportunities are much scarcer than N2 sham opportunities in this sample. | Derived | B | Directly derived from stage annotations, but limited to Sleep-EDF cassette hypnograms and the selected buffer/spacing rules. |
| Conservative buffer/spacing choices disproportionately reduce N3 opportunities. | Derived/model-dependent | B | Supported by sensitivity sweep, but depends on the chosen candidate-window algorithm. |
| Equal per-recording condition counts may be infeasible without discarding data or selecting nights. | Inference | B | Follows from at least one recording with zero eligible N3 windows and the large N2/N3 candidate imbalance. |
| Pink noise changes memory, dreams, evaluation, or sleep quality in these data. | Unsupported | E | No sound was delivered and outcomes are synthetic. |
| This dry run supports claims about covert influence or attribution. | Unsupported | E | The dataset has no exposure, actor, intent, or human-response measurement relevant to attribution. |

## Faraday State

The Faraday design scaffold was initialized at:

`workspaces/vindication-machine/sleep-edf/faraday-dry-run-scaffold`

Faraday status: `blocked`

Hypothesis state: `unreviewed`

Current expected blockers include control measurement coverage, analysis-family
review, measurement-validity planning, measurement contract completion, and
calibration review. This is appropriate: the dry run demonstrates plumbing
readiness, not study approval or evidence of an effect.

## Claim Ceiling

Supported statement:

> The local pipeline can parse public Sleep-EDF hypnograms, schedule deterministic
> simulated cue markers over real sleep-stage timelines, preserve source hashes,
> and reproduce the generated marker digest from the same seed.

Unsupported statements:

- Pink noise changed sleep in these recordings.
- Simulated cue markers caused memory, dream, mood, or attention effects.
- The result supports covert influence, attribution, or intent.

## Primary Artifacts

- `tools/vindication_sleep_sim.py`
- `examples/vindication-machine/sleep_edf_pink_noise_dry_run_brief.json`
- `workspaces/vindication-machine/sleep-edf/results/sleep-pink-noise-dry-run-results.json`
- `workspaces/vindication-machine/sleep-edf/results/synthetic-cue-markers.csv`
- `workspaces/vindication-machine/sleep-edf/results/faraday-scaffold.json`
- `workspaces/vindication-machine/sleep-edf/results/faraday-initialize.json`
