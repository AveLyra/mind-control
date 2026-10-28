> Historical Faraday research note recovered in supplementary search on 2026-10-27. Simulations and hypotheses retain their original limits; no rerun occurred.

[Wiki home](../../README.md) · [Source catalog](../../sources/catalog.md)

# Loaded Dice Directional Drift Dry Run

This design turns personalized information curation into a vector problem.
Instead of asking whether one exposure controls one person, it asks whether many
small response movements fail to cancel at the population level.

The die analogy is the guiding model:

- a fair die produces directions that mostly cancel;
- a physically biased die leaves a larger resultant vector;
- an information environment with tuned curation might similarly leave a
  response-drift vector in attitude, affect, or behavior space.

The target space now includes psychological, political, epistemic, and
commercial dimensions:

- institutional distrust;
- threat salience;
- anger arousal;
- outgroup coldness;
- purchase impulse;
- risk tolerance;
- political efficacy;
- participation intent;
- shared-reality confidence.

The target direction is preregistered in `tools/vindication_loaded_dice_power.py`.
Every participant contributes a before-after movement vector. The analysis
projects that movement onto the target direction, then aggregates:

- mean target projection;
- population resultant-vector length;
- cosine alignment with the target direction;
- sensitivity across sample sizes and drift magnitudes.

## Scenarios

The harness tests four synthetic scenarios:

- `null`: response vectors should cancel;
- `generic_broadcast`: weak shared movement without susceptibility tuning;
- `wrong_direction`: coherent movement in an off-target direction;
- `loaded_dice`: target movement amplified by individual susceptibility.

It can also ingest a measured CSV with `participant_id` and the nine dimension
columns. That lets future work plug in survey, behavior, or platform-export
data without changing the analysis shape.

## Required Experiment Families

Faraday should treat the loaded-dice harness as an umbrella that must branch
into separate pathway tests before any measured study is interpreted:

- **Polarization:** movement toward anger, threat salience, outgroup coldness,
  and institutional distrust.
- **Partisan demobilization or nullification:** movement away from political
  efficacy, participation intent, trust that action matters, or willingness to
  donate, volunteer, vote, persuade, or organize.
- **Fragmented shared reality:** movement away from confidence that opposing
  groups are responding to the same facts or institutions.
- **Commercial activation:** movement toward purchase impulse, urgency,
  status-seeking, or risk-shifted consumer decisions.
- **Mixed affective loading:** combinations where threat or anger does not
  convert beliefs directly, but changes which subsequent messages feel salient
  or emotionally plausible.

Each pathway needs its own positive control, null/sham control, wrong-direction
control, and common-shock control. A pathway label is not allowed to be selected
after observing which dimensions moved.

## Population-Level Harm Models

The design explicitly includes harms that do not require direct individual
control:

- small shifts can increase aggregate polarization even when most individuals
  show noisy or reversible changes;
- demobilizing one coalition can nullify another coalition's ordinary campaign
  or organizing efforts without converting voters;
- fragmented reality can reduce the effectiveness of public correction because
  groups no longer share the same salience map;
- commercial and political systems can interact when identity threat increases
  susceptibility to impulsive purchasing, donation, or attention capture.

These are hypotheses to test, not conclusions. The competing explanations are
ordinary news cycles, campaign contact, sorting, selection into exposure,
seasonality, measurement artifacts, and broad common shocks.

## Claim Ceiling

This dry run can support claims about design power and directional-drift
detectability. It cannot establish direct control over individuals, a real-world
platform mechanism, state intent, or attribution.

The strongest allowable claim is:

> A preregistered vector analysis can detect population-level drift toward a
> specified response direction under simulated curation assumptions.

The disallowed claim is:

> Personalized information systems have been shown here to control thoughts or
> emotions in real people.
