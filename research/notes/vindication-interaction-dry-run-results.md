> Archived research note from Faraday workspace; recovered 2026-10-27. Original claims and status are historical and were not rerun in this collection pass.

[Wiki home](../../README.md) · [Source catalog](../../sources/catalog.md)

# State Cue By Associative Pairing Results

This run reevaluates the vindication-machine sleep/noise idea around the revised
mechanism: a state-shaping cue such as timed sound is not assumed to carry the
emotional payload by itself. The tested mechanism is that a state cue could
amplify a previously learned association.

## Run

- Harness: `tools/vindication_interaction_sim.py`
- Faraday brief: `examples/vindication-machine/state_association_interaction_dry_run_brief.json`
- Seed: `20260911`
- Synthetic participants: `48`
- Repeats per 2x2 cell: `8`
- Trial CSV SHA-256: `703ab4d5d4a6c5486d044932ec0e455fb37f56f159fda616ea842e7b99d04c3d`
- Replay: matched the same trial CSV SHA-256
- Claim ceiling: synthetic dry run; design discriminability only

## Scenario Results

The primary estimate is the participant-level interaction:

`(paired state-cue - paired sham-state) - (unpaired state-cue - unpaired sham-state)`

| Scenario | Estimated interaction | 95% CI | Detected |
| --- | ---: | ---: | --- |
| Null | -0.0059 | -0.1534 to 0.1416 | No |
| State-only | 0.0818 | -0.0695 to 0.2330 | No |
| Association-only | -0.0064 | -0.1758 to 0.1630 | No |
| Additive | 0.0178 | -0.1685 to 0.2042 | No |
| Interaction | 0.5605 | 0.3837 to 0.7374 | Yes |

In this synthetic run, the analysis did what it was supposed to do. It did not
mistake a direct state effect, a direct association effect, or an additive
combination for interaction evidence. It detected the configured interaction.

## Sensitivity

With `8` repeats per cell and the configured noise level, small interactions are
harder to recover than medium ones.

| Participants | True interaction 0.15 | True interaction 0.30 | True interaction 0.45 |
| ---: | ---: | ---: | ---: |
| 12 | 20.0% detected | 55.0% detected | 90.0% detected |
| 24 | 38.75% detected | 82.5% detected | 95.0% detected |
| 48 | 57.5% detected | 100.0% detected | 100.0% detected |
| 96 | 86.25% detected | 100.0% detected | 100.0% detected |

The null false-positive checks were noisy at this small grid size: `1.25%` for
12 participants, `10%` for 24, `0%` for 48, and `6.25%` for 96 across 80
iterations each. A real planning pass should use more iterations and a frozen
power method before human data collection.

## Faraday Result

Faraday scaffolded the revised brief with status `review_required`, not
`blocked`. The remaining warnings are appropriate:

- the repeated-measures interaction uses a custom reviewed analysis rather than
  a built-in two-group estimator;
- the synthetic outcome does not establish measurement validity for a human
  construct;
- any human version would need calibration, validity, consent, and review before
  collection.

## Interpretation

Lay version: the machine can now test the right shape of the hypothesis. It asks
whether a cue plus a learned association produces more than either ingredient
alone. In simulation, the test can tell those apart.

Research version: this is a factorial repeated-measures design dry run with a
participant-level interaction contrast. It supports analysis-pipeline
discriminability under simulated assumptions, not the existence, magnitude,
ethics, real-world availability, or deployment of subconscious influence.

The current scientific claim should be:

> We can specify and reproducibly test an interaction model that separates state
> cueing, associative pairing, additive effects, and their interaction in
> synthetic data.

The current scientific claim should not be:

> Pink noise, notifications, commercials, or subliminal media have been shown by
> this run to steer real people's emotions or thoughts.
