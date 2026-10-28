# Sleep measurement, models, and datasets

[Home](../README.md) · [Experiments](experiments.md)

The Codex **Assess breathing-based sleep staging** conversation explored a bedside smartphone research app. It distinguished breathing measurement from sleep-stage inference and causal real-time prediction from retrospective classification.

## Recovered candidate assessment

| Candidate | What the historical review found | Unresolved dependency |
|---|---|---|
| Asleep SleepTrack | Commercial API/SDK route; review reported live updates at five-minute intervals | Current terms, server processing, and actual supported latency need verification before use. |
| SoundSleepNet / HomeSleepNet | Relevant smartphone-audio studies | Downloadable checkpoints were not verified; future context in an architecture precludes assuming live performance. |
| Nidra | Public code and demonstration weights | Loading/compilation and surrounding-epoch dependence needed resolution in the original review. |
| PSG-Audio | Ambient/tracheal audio, PSG, expert labels; publication described 212 participants | Download and current licence were not verified; clinical recordings do not establish home-phone performance. |

This is a recovered assessment dated October 27, 2026, not a fresh vendor recommendation or tested integration. The three original answers and their source links appear in the [catalog](../sources/catalog.md).

## Constraints worth preserving

Use subject-disjoint validation and independently scored polysomnography for a staging claim. A model trained on respiratory belts does not automatically accept microphone audio. Breaths per minute discard information available in richer acoustic patterns. Device placement, fans, bedding, a second sleeper, and device-specific audio processing can change signal quality.

A proposed 30-second update rate was a design choice, not measured performance. Likewise, accuracy from a model using future audio cannot establish a live model's accuracy. The prototype discussion proposed uncertainty and insufficient-signal outputs, synchronized timestamps, and optional consented recording for validation. No app was implemented or activated by this collection task.

## Intraoral sensing and brain interfaces

The ChatGPT **Research sleep influence benefits** answers explore an intraoral stimulus dosimeter and physiological sensor. The [tooth-mounted sensing note](../research/notes/vindication-tooth-mounted-sensing-power.md) separates dental-crown geometry and power constraints from larger mouthguards. An experimental oral EEG result or a large intraoral sensor does not establish equivalent performance inside a crown. Measuring local exposure also does not identify a message, source, or intent.

**Research Brain Computer Interfaces** surveys decoding intended actions and speech with different recording systems. Its long answer is truncated. Instrumented implanted decoding, wearable EEG, and unrestricted transcription of inner thought must remain separate capability claims; see [magnetic and neural interfaces](magnetic.md).
