> Historical Faraday research note recovered in supplementary search on 2026-10-27. Simulations and hypotheses retain their original limits; no rerun occurred.

[Wiki home](../../README.md) · [Source catalog](../../sources/catalog.md)

# Loaded Dice Directional Drift Results

This dry run operationalizes fine-tuned information curation as a population
vector-drift problem. It asks whether repeated exposure could load the dice of
emotional, political, or commercial response without requiring direct control of
any one person.

## Run

- Harness: `tools/vindication_loaded_dice_power.py`
- Faraday brief: `examples/vindication-machine/loaded_dice_directional_drift_brief.json`
- Seed: `20260912`
- Synthetic participants per scenario: `500`
- Synthetic exposure count: `50`
- Vector dimensions: institutional distrust, threat salience, anger arousal,
  outgroup coldness, purchase impulse, risk tolerance, political efficacy,
  participation intent, shared-reality confidence
- Data CSV SHA-256: `2a35fd9ee37e5705a146fc4ca71c1056d24504046b4265e1cd68b4391d835b9c`
- Replay: matched the same data CSV SHA-256
- Claim ceiling: synthetic or ingested directional-drift analysis only; no
  mechanism, intent, attribution, or direct-control claim

## Scenario Results

The primary statistic is each participant's response-change vector projected
onto a preregistered target direction. A directional-drift detection requires:

- the target-projection 95% confidence interval lower bound to be greater than
  zero; and
- the population resultant vector to align with the target direction
  (`cosine > 0.65`).

| Scenario | Mean target projection | 95% CI | Cosine to target | Detected |
| --- | ---: | ---: | ---: | --- |
| Null | -0.0384 | -0.1318 to 0.0550 | -0.3836 | No |
| Generic broadcast | 0.1259 | 0.0385 to 0.2132 | 0.6960 | Yes |
| Wrong direction | -0.0247 | -0.1125 to 0.0631 | -0.3328 | No |
| Loaded dice | 0.0947 | 0.0098 to 0.1797 | 0.7664 | Yes |

The expanded nine-dimensional run shows the loaded-dice scenario clearing the
gate, but it also shows the generic-broadcast scenario clearing the same broad
target gate. That is scientifically useful. It means the omnibus target vector
can detect population-level drift, but it does not by itself distinguish
personalized curation from broad persuasive broadcast. Any future
personalization-specific claim must therefore require a direct
loaded-dice-minus-generic contrast and common-shock controls.

## Power Implications

Detection rates below are from 120 iterations per cell. Each row uses the same
50-exposure assumption and noise level.

| Participants | Drift 0.02 | Drift 0.04 | Drift 0.08 | Drift 0.12 |
| ---: | ---: | ---: | ---: | ---: |
| 100 | 4.17% | 5.83% | 10.83% | 30.83% |
| 250 | 0.83% | 7.50% | 29.17% | 63.33% |
| 500 | 8.33% | 16.67% | 63.33% | 88.33% |
| 1000 | 9.17% | 26.67% | 87.50% | 100.00% |

This suggests that very small response drifts would be difficult to detect with
ordinary small experiments. Medium directional drift becomes feasible at roughly
500 to 1000 independent participants under these assumptions.

Null false-positive rates in this 120-iteration grid were `0.83%`, `1.67%`,
`0%`, and `0.83%` for 100, 250, 500, and 1000 participants, respectively.

## Pathways Covered

The current Faraday agenda now explicitly covers:

- polarization: threat salience, anger, outgroup coldness, institutional
  distrust;
- partisan demobilization/nullification: lower political efficacy and
  participation intent;
- shared-reality fragmentation: lower confidence that groups share facts,
  salience, or institutional reality;
- commercial activation: purchase impulse and risk-shifted consumer response;
- timing/state amplification: future interaction tests linking delivery state
  to curation effects.

These pathways must be interpreted separately. An omnibus target-vector result
is not enough to say which psychological mechanism is operating.

## Faraday Result

Faraday scaffolded the design as `review_required`, not blocked. The remaining
warnings are appropriate:

- the primary outcome needs a complete measurement contract before any
  confirmatory run;
- measured attitude/affect/behavior/political-efficacy/shared-reality dimensions
  need validity evidence;
- future human or platform-data work needs calibration, timing, ethics, and
  data-custody plans.

## Interpretation

Lay version: the experiment now has a way to test whether many small nudges lean
in one direction instead of canceling out. The synthetic run says that weak
drift is hard to prove, but stronger population-level drift could be detected
with enough participants.

Research version: this is a custom reviewed multivariate directional-drift power
simulation. It estimates detectability of a preregistered mean resultant vector
and target projection under simulated curation assumptions. The expanded model
also demonstrates a key falsification problem: broad generic broadcast can
produce target-direction drift, so curation-specific claims require generic,
wrong-direction, null, and common-shock controls. It does not validate the
latent space, establish a real platform mechanism, or support individual
mind-control claims.

The current scientific claim should be:

> Faraday can now run a reproducible loaded-dice power analysis that estimates
> when population-level directional response drift would be detectable.

The current scientific claim should not be:

> Personalized information curation has been shown here to control individuals
> or prove real-world platform manipulation.
