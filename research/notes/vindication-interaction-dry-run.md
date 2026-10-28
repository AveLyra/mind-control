> Archived research note from Faraday workspace; recovered 2026-10-27. Original claims and status are historical and were not rerun in this collection pass.

[Wiki home](../../README.md) · [Source catalog](../../sources/catalog.md)

# State Cue By Associative Pairing Dry Run

This dry run tests the corrected mechanism hypothesis at the design level:
pink noise or another state-shaping cue may not be the semantic payload. Instead,
it may amplify previously learned associations from media, phone cues, or other
low-awareness inputs.

The runnable test is a 2x2 interaction:

- associative condition: paired versus unpaired;
- state condition: state cue versus sham state;
- primary estimand: `(paired + state cue) - (paired + sham) - (unpaired + state cue) + (unpaired + sham)`.

This interaction is the key bridge between "pink noise alone" and "state cueing
amplifies an associative payload."

## Association Payload Families

The "paired" condition can now be decomposed into more specific payload
families before any human study is designed:

- passive semantic exposure: the participant hears, reads, or sees a target
  word cluster;
- semantic self-generation: the participant says, types, chooses, or completes
  target-cluster words without being explicitly told the theme;
- affective pairing: the semantic cluster is paired with stress, shame,
  confusion, fatigue, social threat, or uncertainty;
- kinesthetic pairing: the semantic or affective pairing co-occurs with a
  measurable body cue such as speech production, typing, gesture, posture,
  haptic vibration, breathing rhythm, or movement cadence.
- financial-threat interruption: a financial-salience cue, such as a balance,
  bill, overdraft, market, tax, debt, or account notification, is delivered
  during a measured task state and tested against matched neutral and
  unrelated-negative notifications.

The self-generation version matters because producing a word oneself may create
a different association than merely hearing it. The kinesthetic version matters
because a later movement, posture, vibration, or speech-motor cue could be a
reactivation cue rather than the semantic payload itself.

Any measured study must keep these channels separate. A result from passive word
exposure should not be promoted to evidence for covert self-generation. A result
from a haptic cue should not be promoted to evidence for posture, speech motor
acts, or whole-body movement. A result from financial-threat notification should
not be promoted to evidence of targeting unless timestamped notification logs,
task-state records, and random-time or neutral-notification controls rule out
ordinary salience, app defaults, and memory-selection effects.

The harness in `tools/vindication_interaction_sim.py` generates synthetic data
under five scenarios:

- null;
- state-only;
- association-only;
- additive state plus association;
- true interaction.

The dry run can support whether the planned analysis discriminates those models.
It cannot support any claim that subconscious influence occurs in people.

See also `docs/vindication-semantic-kinesthetic-association.md` for the proposed
semantic self-generation and kinesthetic association extension.

See also `docs/vindication-financial-notification-interruption.md` for the
financial-threat notification interruption pathway.

See also `docs/vindication-acoustic-feature-sleep-state-coding.md` for the
separate acoustic-feature x sleep-state x prior-pairing pathway.

See also `docs/vindication-tooth-mounted-sensing-power.md` for the local
tooth-mounted sensing and power pathway.
