> Archived research note from Faraday workspace; recovered 2026-10-27. Original claims and status are historical and were not rerun in this collection pass.

[Wiki home](../../README.md) · [Source catalog](../../sources/catalog.md)

# Sleep And Pink-Noise Dry Run

This dry run uses public sleep-stage hypnograms to exercise the Faraday-style
experiment chain before any human-participant collection.

## What It Tests

The harness in `tools/vindication_sleep_sim.py` tests whether the machine can:

- ingest public EDF+ hypnogram files;
- preserve source-file hashes;
- identify N2, N3, and REM windows;
- synthesize cue markers for a pink-noise-style slow-wave condition, a sham N2
  marker condition, and an off-target REM marker condition;
- produce deterministic outputs from a seed;
- keep the claim ceiling at simulation-only.

It does not test whether pink noise changes sleep, memory, dreams, evaluation,
or behavior. The outcome column is synthetic, so any contrast is only a plumbing
check.

The literature boundary is also narrower than the phrase "sleep influence"
suggests. The strongest evidence concerns targeted memory reactivation of
material learned while awake; dream-theme and social-evaluation findings are
more context-dependent, and physiological EEG changes do not guarantee a useful
memory or behavioral outcome. Any future human study must measure the chain
separately: cue delivered, cue received, brain-state response, and delayed
behavioral or memory outcome.

The related feature-coding question is specified separately in
`docs/vindication-acoustic-feature-sleep-state-coding.md`. The current harness
does not claim that pitch, timbre, thud depth, knock sharpness, or rhythm carry
state-specific meaning.

## Useful Public Sources

- Sleep-EDF Expanded provides public PSG and hypnogram EDF files suitable for
  testing sleep-stage parsing and cue-window scheduling:
  https://www.physionet.org/content/sleep-edfx/1.0.0/
- NSRR provides larger PSG and actigraphy resources, usually requiring an
  account and data request:
  https://sleepdata.org/about
- Published closed-loop acoustic-stimulation studies provide protocol templates
  and expected effect-size priors, but they should not be treated as if their
  outcomes were present in Sleep-EDF.

## Interpretation Rule

Results from this dry run may support statements like:

> The local analysis pipeline can schedule deterministic sham and simulated
> stimulation markers over real sleep-stage timelines and preserve source hashes.

They may not support statements like:

> Pink noise influenced sleep, memory, dreams, or subconscious attitudes in this
> dataset.
