> Archived research note from Faraday workspace; recovered 2026-10-27. Original claims and status are historical and were not rerun in this collection pass.

[Wiki home](../../README.md) · [Source catalog](../../sources/catalog.md)

# Tooth-Mounted Sensing And Power Pathway

This note records a possible measurement pathway for local oral and mechanical
signals. It is an engineering hypothesis, not evidence that a device exists in
or was used on any particular person.

## What A Crown Could Measure

A sealed sensor on or inside a crown might measure:

- tooth or jaw strain from biting and contact;
- vibration associated with chewing, speech, or nearby mechanical events;
- local temperature;
- selected saliva or plaque chemistry, such as pH;
- timestamps and short sensor summaries when an external reader is present.

It would not directly measure thoughts, subconscious interpretation, sleep
stage, hidden messages, targeting, or intent. Tooth vibration is a mixed signal:
chewing, speech, jaw movement, contact, ambient sound, and device artifacts can
all contribute to it.

Sound transmission through teeth is established in hearing-rehabilitation
devices, and removable oral appliances can collect some physiological or
sleep-related measurements. Those facts establish delivery or measurement
capability, not a bypass of the auditory system, accurate brain-state
measurement, or a cognitive effect from a crown.

## Power Options

### Primary candidate: passive NFC or inductive power

A small receiving coil and sensor would be sealed into the dental appliance. A
reader coil in a mouthguard, cheek-side appliance, or handheld probe would
provide energy at close range and receive a short data packet. This is the most
practical architecture for intermittent measurements because it avoids a
permanent battery.

The main constraints are reader distance, coil alignment, metal or ceramic
effects on tuning, limited read windows, and the need for careful encapsulation.
Published intraoral systems have used 13.56 MHz NFC links for battery-free
sensing and wireless readout, but these are research devices rather than
ordinary clinical crowns.

The present sleep literature does not identify an advantage for putting the
delivery system inside a crown. Targeted memory reactivation mainly depends on
an association formed during waking, verified sleep timing, and a later memory
or behavioral outcome. A crown would address only part of signal delivery. It
would not establish that the cue was heard, that the brain entered the intended
state, or that a meaningful outcome changed.

### Secondary option: rechargeable microbattery

A small battery could support longer sensing windows, but charging, heat,
sealing, replacement, mechanical fatigue, and dental access become significant
problems. Continuous audio would require much more power and storage than
occasional strain or pH measurements.

### Supplemental harvesting

Piezoelectric or triboelectric harvesting from chewing and speech, thermoelectric
harvesting from temperature gradients, and saliva biofuel cells are plausible
supplements. They are intermittent and variable; they should not be assumed to
power a reliable continuous recorder. Harvested energy is better treated as a
way to extend a duty-cycled sensor or recharge a buffer capacitor.

### Poor fits

Ambient light is unreliable inside the mouth. Long-range radio transmission
from a tiny crown is constrained by antenna size, tissue and saliva losses,
power budget, and safety limits. A continuous microphone-plus-radio design is
therefore a poor first target.

## Falsifiable Testing Sequence

1. **Bench phase:** characterize a dummy crown or mouthguard in saline and
   dental-material phantoms. Measure coil tuning, received power, packet loss,
   temperature rise, sealing, and mechanical response.
2. **Non-invasive phase:** use an instrumented mouthguard or jaw/temple
   accelerometer to compare chewing, speech, external sound, phone vibration,
   and quiet controls. Synchronize an external microphone and accelerometer.
3. **Reader phase:** test passive NFC readout during short, predefined windows;
   quantify missed reads and alignment sensitivity.
4. **Clinical phase:** consider a custom crown or other intraoral device only
   for a legitimate dental indication, with a dentist, biomedical engineer,
   biocompatibility review, privacy plan, and independent ethics approval.

The decisive comparison would randomize the same learned cue and EEG-based
timing across a conventional external transducer, a removable oral device, an
inactive matched appliance, and (only if justified) a crown prototype. Primary
outcomes should include delayed memory or clinical benefit, sleep disruption,
tolerability, and blinded behavioral scoring. Sensor amplitude, successful
wireless readout, or a transient EEG response should remain secondary outcomes.

The primary useful output would be a validated local-signal classifier, not a
claim about subconscious influence. A result is informative only if it survives
blinded replay, source-matched controls, chewing and speech controls, reader
artifacts, and independent calibration.

## Claim Ceiling

Evidence from a tooth sensor could support claims about measured local
mechanical, chemical, or thermal conditions. It could not by itself establish
that a person received a covert signal, that a sound carried a hidden semantic
payload, or that any observed event was targeted or coordinated.

## Sources

- Vellappally et al. (2019), wireless tooth-mounted stress and oral-condition
  sensing prototype: https://doi.org/10.1016/j.comcom.2019.09.020
- Wearable battery-free intraoral dental patch using 13.56 MHz NFC power and
  telemetry: https://www.nature.com/articles/s41528-022-00185-5
- Review of oral sensors and biocompatibility, packaging, and power constraints:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC10560166/
- Review of oral wearable energy harvesting and its practical limitations:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC13072814/
- Schwartz, Clerget, and Perogamvros (2022), targeted memory reactivation for
  nightmare treatment using bone conduction:
  https://doi.org/10.1016/j.cub.2022.09.032
- Kou et al. (2025), dental bone-conduction hearing rehabilitation study:
  https://doi.org/10.1097/MAO.0000000000004664
- Mohammadieh et al. (2025), removable oral sleep-monitoring pilot:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12320676/
