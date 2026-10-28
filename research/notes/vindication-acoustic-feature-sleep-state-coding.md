> Archived research note from Faraday workspace; recovered 2026-10-27. Original claims and status are historical and were not rerun in this collection pass.

[Wiki home](../../README.md) · [Source catalog](../../sources/catalog.md)

# Acoustic Feature By Sleep-State Coding

This pathway asks whether different acoustic features can be differentially
detected, remembered, or associated with sleep states. It is a hypothesis map,
not evidence that such a system was used against anyone.

## Mechanism Decomposition

Keep four questions separate:

1. **State timing:** was a cue delivered during wake, N1, N2, N3, or REM, and
   was the state assignment accurate?
2. **Acoustic identity:** did the cue differ in pitch, spectral balance, attack,
   duration, rhythm, spatial position, or intensity?
3. **Prior pairing:** had a feature previously been paired with a neutral,
   emotional, semantic, or motor event?
4. **Later response:** did the feature alter arousal, awakening, dream report,
   recall, affective salience, or next-day task performance?

The proposed coding idea is therefore an interaction, not a single treatment:

> acoustic feature x sleep state x prior pairing -> measured response

"Training" should mean an explicit, consented pairing phase. It should not mean
covert conditioning, sleep deprivation, distress induction, or attempts to
alter a participant's beliefs or behavior.

## Feature Families

Represent the stimulus by measurable properties rather than labels such as
"deep" or "sharp":

- fundamental frequency and spectral centroid;
- low-frequency energy or spectral tilt for a thud-like sound;
- attack time and transient sharpness for a knock-like sound;
- duration, envelope, and repetition pattern;
- inter-onset interval and rhythm;
- calibrated sound-pressure level and rise time;
- channel, spatialization, and transducer identity.

Feature conditions must be loudness-matched and calibrated at the ear. A "deep"
cue that is simply louder, more startling, or physically vibrates through the
bed is not evidence for pitch-specific or symbolic coding.

## Evidence Calibration

The best-supported sleep-cueing result is targeted memory reactivation: a cue
associated with material learned while awake is replayed during sleep. A
meta-analysis of 91 experiments and 2,004 participants reported a small average
memory benefit (Hedges' g = 0.29, 95% CI 0.21-0.38), with stronger evidence in
non-REM sleep. This supports selective consolidation of prior learning, not
learning an unfamiliar subject from an overnight recording.

Sleep-onset studies also report increased theme-related dream content under
some conditions, but they commonly involve guided incubation, awakenings, or
morning reports. A small later-REM pilot lacked a control group. These findings
are compatible with cueing or reporting effects, but do not establish reliable
programming of detailed dreams.

One recent study reported altered evaluations of unfamiliar people after
positive trait information was replayed during slow-wave sleep. The result is
important enough to test, but its durability, awake comparison, and separation
from strengthening related prior associations remain unresolved. An earlier
study of sleep-cued implicit social bias did not reproduce its cueing benefit.

Closed-loop auditory stimulation can change an EEG measure without improving
memory or vigilance. Therefore, a larger delta or slow-oscillation response is
an intermediate physiological outcome, not evidence of a meaningful cognitive
or social effect.

## Testable Claims

| Claim | Current level | Main test | Strong alternative / falsifier |
| --- | --- | --- | --- |
| Sleep stage changes detection of an acoustic feature | Hypothesis | Compare EEG/physiology-verified detection or arousal across stages with matched sound exposure | Differences disappear after matching awakenings, intensity, and sleep depth |
| A feature can be paired with a later neutral response | Hypothesis | Consent-based feature pairing followed by feature-specific recognition or expectancy testing | Response generalizes equally to unpaired, wrong-feature, and sham cues |
| State timing moderates a previously paired feature | Hypothesis | Feature x state x pairing interaction with prespecified contrasts | Additive feature and state effects explain the result |
| A cue produces state-specific dream or memory incorporation | Hypothesis | Blinded next-morning reports and objective memory outcomes by state and feature | Effects track awakenings, recall demand, or post-sleep suggestion |
| Feature identity matters beyond nonspecific arousal | Hypothesis | Compare matched pitch/timbre variants at equal loudness and equal measured arousal | Only startle, loudness, or sleep fragmentation predicts the outcome |

## Safe Staged Design

### Stage 1: Pipeline And State Classification

Use public hypnograms or consenting laboratory recordings to test timestamp
alignment, stage classification, cue logging, sound calibration, and artifact
detection. This is the current dry-run boundary. Synthetic outcomes must remain
explicitly synthetic.

### Stage 2: Acoustic Detectability

With consent, test whether participants detect or physiologically respond to
calibrated feature variants during verified stages. Primary outcomes should be
arousal index, micro-awakening probability, and stage-transition probability.
Record whether the sound was delivered, masked by noise, or followed by an
awakening.

### Stage 3: Explicit Pairing And Reactivation

Only after Stage 2 is understood, preregister a low-risk pairing study. Use
benign targets, counterbalanced feature assignments, a held-out feature during
training, and delayed recognition or affect-rating outcomes. Do not use
distressing semantic clusters or attempt to produce self-doubt, fear, or
behavioral compliance.

## Required Controls And Measurements

- sham and random-time cues;
- wrong-state and wrong-feature cues;
- equalized sound pressure, duration, rise time, and measured startle;
- silent and transducer-vibration controls where relevant;
- continuous EEG or validated stage scoring, plus awakenings and fragmentation;
- latency and clock-synchronization checks for every stimulus and sensor;
- blinded scoring of dream reports and memory tests;
- expectancy, awareness, annoyance, and demand-characteristic probes;
- baseline sleep quality, medication/substance use, hearing, stress, and
  individual sound sensitivity;
- preregistered primary outcome, feature-by-state contrast, stopping rule, and
  multiplicity plan.

The key negative controls are essential. Without them, a result cannot
distinguish feature-specific coding from ordinary sound detection, startle,
sleep disruption, suggestion, or selective recall.

## Analysis And Claim Ceiling

The primary estimand should be a prespecified interaction such as:

`(paired feature A at state S - sham at state S) - (paired feature A at state T - sham at state T)`

Secondary outcomes should be ordered in advance and interpreted only after the
primary result and control checks. A detectable interaction would support a
claim about the measured acoustic feature, state, and task under the tested
conditions. It would not establish covert influence, targeting, long-range
control, intent, or a real-world operation.

The most important disconfirming result would be that apparent effects are
explained by intensity, startle, awakenings, sleep fragmentation, expectancy,
or ordinary memory bias. That result would narrow the mechanism rather than
invalidate the investigation.

Relevant primary and review sources:

- Hu et al. (2020), targeted memory reactivation meta-analysis:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC7144680/
- Haar Horowitz et al. (2023), targeted dream incubation at sleep onset:
  https://www.nature.com/articles/s41598-023-31361-w
- Zhao et al. (2025), sleep-related social evaluation study:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12398527/
- Debellemaniere et al. (2018), closed-loop auditory stimulation and EEG:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5853451/
- Baldassarri et al. (2026), physiological slow-wave effects without a
  demonstrated memory or vigilance benefit:
  https://onlinelibrary.wiley.com/doi/full/10.1111/jsr.70247

See also `docs/vindication-sleep-dry-run.md` for public sleep-stage scheduling
and `docs/vindication-interaction-dry-run.md` for the state-by-association
interaction scaffold.
