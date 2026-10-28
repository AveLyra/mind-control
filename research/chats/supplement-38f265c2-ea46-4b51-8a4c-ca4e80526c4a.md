# Invisible Signals Experiment — supplementary research

> Historical research recovered in supplementary search; not independently reverified.

Source: chatgpt thread `6ab16e89-dda4-83ea-9b00-17522496c389`, item `38f265c2-ea46-4b51-8a4c-ca4e80526c4a`

Citation provenance: The original answer cites an unavailable uploaded file (`turn3file2`). Links labeled **editorial source** or **editorial synthesis** were added during this audit. They supply related published evidence or an explicitly labeled interpretation; they are not recovered links from that upload. See the [attachment gap](../../sources/citation-audit.md#unavailable-upload).

Selection: Complete research answer; source citations and limitations retained. Personal prompts and unrelated correspondence are excluded.

[Wiki home](../../README.md) · [Source catalog](../../sources/catalog.md)

---

**Yes—there is a worthwhile experiment here.** The most informative question would be:

> **Can a person recover a simple encoded message from light whose flicker they cannot consciously perceive—and how does that compare with a computer recovering the same information from their EEG?**

That tests the important gap in the research rather than assuming the answer. I would leave the false-tooth hardware out of the first experiment: it adds an engineering problem without helping answer the neuroscience question.

## 1. Separate three different kinds of success

The same transmission could succeed at one level and fail at another:

| Level | What you test | What success would establish |
|---|---|---|
| **Electronic reception** | Can a light sensor recover the transmitted code? | The equipment carries information reliably. |
| **Neural recording** | Can a computer identify the transmitted code from EEG alone? | The stimulus produces a distinguishable, instrument-recorded response, provided artifacts are excluded. |
| **Human reception** | Can the participant identify what was transmitted, without seeing the EEG decoder’s answer? | The person can use information from the stimulus. Whether this involves awareness requires separate measurement. |

**The central distinction is that a computer decoding information from someone’s brain does not necessarily mean that person knows the information.**

There is already a close precedent for the neural-recording level. A 2022 study used imperceptible flicker and MEG to identify which location participants voluntarily attended to; a 2023 study demonstrated an EEG-based interface using imperceptible flicker. These are instrumented interfaces—not demonstrations of people understanding secretly delivered sentences. [source 0](https://pubmed.ncbi.nlm.nih.gov/36228894/)

Also, **imperceptible flicker does not mean invisible content**. A person may consciously see the target while not noticing its rapid brightness changes. That distinction matters enormously when interpreting these studies. [source 1](https://pubmed.ncbi.nlm.nih.gov/36228894/)

## 2. The experiment I would propose

### Start with two neutral symbols, not sentences

Teach consenting, awake adult participants a simple code: one light pattern corresponds to **circle**, and another corresponds to **triangle**.

First establish that they can learn and recognize the code under readily perceptible conditions. Then test whether recognition survives when the modulation becomes difficult to perceive.

This would be a proposed **vision-laboratory protocol**, with professionally reviewed stimulation parameters—not a recommendation to improvise flashing-light exposure at home.

### Compare three conditions

| Condition | What the participant receives | Why it is needed |
|---|---|---|
| **Perceptible positive control** | A readily distinguishable version of the learned code. | Confirms that the code, instructions, and response task work. |
| **Candidate imperceptible condition** | The code presented under individually assessed conditions where the flicker is not readily noticed. | Tests the actual hypothesis. |
| **Matched sham** | Light matched as closely as possible in average brightness, color, and duration, but without the message-bearing modulation. | Tests guessing, expectations, and unintended cues. |

For each test trial, software randomly selects the intended symbol. The participant answers **circle or triangle**, records confidence, and reports what—if anything—they perceived.

The EEG system independently attempts to classify the transmitted symbol. **Its answer must remain hidden until after the participant has responded**, or the experiment could accidentally become ordinary computer-assisted communication.

The operator interacting with the participant should not know the trial’s intended symbol.

### Measure the light, not just the software command

Use a photodiode—a light-measuring sensor—to record what the equipment actually emits. That recording is the delivery check.

I would require this before interpreting any human result: the intended code must reach the test position, and the two codes must not accidentally differ in an obvious brightness change, onset flash, sound, or other cue.

For EEG, I would also require a hardware-only control to check whether the system can “decode” the stimulus even without a participant. That would reveal electrical interference or information leaking through the recording setup rather than a biological response.

## 3. The hardest part is defining “without awareness”

There are at least three different things a participant might be unaware of:

**The flicker:** “The light looked steady.”

**The code:** “I noticed something change, but could not identify the pattern.”

**The meaning:** “I could not tell whether it meant circle or triangle.”

These are not interchangeable.

Someone might fail to notice flicker yet consciously recognize a faint change that identifies the symbol. That would still be interesting communication—but not unconscious message reception.

Conversely, someone might answer above chance while saying they were guessing. The appropriate initial conclusion would be **“discrimination with low reported awareness,”** not automatically “unconscious comprehension.” Published experiments illustrate how difficult it is to separate genuinely unconscious performance from residual conscious perception and task-specific effects. [editorial source attachment-turn3file2a](https://journalofcognition.org/articles/10.5334/joc.419) [editorial source attachment-turn3file2b](https://doi.org/10.1016/j.concog.2026.104018)

I would therefore measure both reported experience and performance on a separate, carefully matched flicker-detection task. Importantly, that detection task tests awareness of **modulation**, not necessarily awareness of **message content**.

A small test that happens to produce approximately 50% accuracy does not establish complete absence of awareness. Before collecting the confirmatory data, define how close to chance performance must be, how precisely it must be measured, and what result would count as inconclusive.

## 4. What the possible results would mean

| Result | Defensible interpretation |
|---|---|
| **EEG decoder succeeds; participant does not.** | Information is recoverable from the recorded response, but human access to the message has not been demonstrated. |
| **Participant succeeds and reports perceiving a cue.** | The system supports perceptual communication, potentially without noticeable flicker. |
| **Participant succeeds while consistently reporting no relevant experience.** | A candidate low-awareness discrimination effect worth independently replicating and examining for partial awareness or unintended cues. |
| **Neither succeeds, while the positive control works.** | Communication was not demonstrated under the tested conditions—not proof that every possible version must fail. |

To make these conclusions credible, I would preregister the main comparison, sample-size rationale, exclusions, and analysis. The decoder should be tested on genuinely held-out trials or sessions, not neighboring fragments of its training data. Report uncertainty and individual results, and repeat any positive finding on another day.

**A two-symbol result would establish, at most, two-symbol discrimination.** A later test could examine learned sequences and previously untested combinations. That is how to investigate richer communication without jumping directly from a small effect to “complex thoughts can be transmitted.”

## 5. Where the other ideas belong

### The miniature receiver: a separate bench experiment

For the tooth-computer concept, initially put the receiver on a bench. Transmit a randomized sequence and measure whether it is received correctly, how much power reception requires, and how errors change with position and distance.

That would test the electronic communication link. It would not establish communication with the wearer’s nervous system.

Keeping these projects separate makes the evidence clearer: **miniaturization cannot substitute for a demonstrated biological receiving mechanism.**

### Infrared conversion: an equipped sensory channel

The 2025 contact-lens study used upconversion materials to make near-infrared information perceptible to equipped participants. That supports an engineered sensory channel; the external carrier can be invisible while the converted signal becomes visible to its recipient. [source 3](https://pubmed.ncbi.nlm.nih.gov/40409271/)

I would not make experimental contact lenses part of an initial project. A separate external detector and display could test the communication concept without putting experimental materials on an eye—but it would remain ordinary equipment-assisted reception.

### Closed eyelids and sleep: later, distinct experiments

An awake, eyes-closed condition could be a subsequent comparison after the eyes-open protocol is established.

Sleep should be another study, with physiological sleep monitoring and checks for awakenings. The 2021 interactive-dreaming work demonstrated some correct responses during verified REM sleep, including lucid dreaming; it does not establish routine decoding of complex, unnoticed messages by ordinary sleepers. [source 4](https://pubmed.ncbi.nlm.nih.gov/33607035/)

## 6. Safety changes the starting point

**Do not treat “imperceptible” as synonymous with “safe.”** Flashing light can provoke seizures in susceptible people, and relevant frequencies can extend up to approximately 60 flashes per second. A blanket “40–60 Hz is invisible and harmless” assumption would be inappropriate. [source 5](https://www.epilepsy.org.uk/info/seizure-triggers/photosensitive-epilepsy)

Invisible infrared also lacks the ordinary visible-light warning that prompts someone to look away; sufficiently intense near-infrared exposure can injure the eye. I would exclude improvised infrared eye exposure, lasers, homemade contact lenses, and unattended overnight stimulation from this project. [source 6](https://ehs.lbl.gov/resource/laser-bio-effects/)

**My recommendation:** start with the randomization, recording, analysis, and bench-level signal verification. Then take the human experiment to a vision or EEG research group.

The scientifically valuable result would be a clear answer to **“the brain registered it—but did the person gain information?”** That is a meaningful experiment even if the two answers turn out to be different.
