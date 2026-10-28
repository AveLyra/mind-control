# Decoded-feedback and AI-memory follow-up source checks

[Synthesis](../../wiki/decoded-feedback-and-ai-memory.md) · [Earlier combination review](../../wiki/combined-techniques.md) · [Catalog](../../sources/catalog.md)

**Origin:** new editorial review, October 28, 2026. The 26 selected entries comprise 25 PubMed publications and one HCI conference publication; they are not 26 new studies or independent replications. Earlier AI studies remain linked through D14–D16 in the prior record. Original collection records remain preserved.

## Discovery and inspection scope

Fourteen distinct PubMed queries used a publication-date upper bound of October 28, 2026. Returned titles/metadata were screened; selected abstracts were retrieved in full. Some broad result sets contain irrelevant records, and incomplete pages do not support literature-absence claims. In particular, the exact phrase “decoded neurofeedback” misses titles containing intervening words such as “fMRI”; the expanded query below mitigates that search limitation.

| Query | Records screened / returned total |
|---|---:|
| `("decoded neurofeedback" OR DecNef OR "multivoxel neuroreinforcement") AND (replication OR reproducibility OR randomized OR randomised OR sham OR placebo OR blind)` | 16 / 16 |
| `("decoded neurofeedback" OR DecNef OR "multivoxel neuroreinforcement") AND (sleep OR nap OR dreaming OR hypnosis OR hypnotic)` | 0 / 0 |
| `"decoded neurofeedback" AND (perceptual OR orientation OR confidence OR fear)` | 21 / 21 |
| `("artificial intelligence" OR "AI-generated" OR "AI-edited" OR chatbot OR deepfake) AND ("false memory" OR "false memories" OR "misinformation effect")` | 8 / 8 |
| `(chatbot OR "AI-generated" OR "generative AI" OR deepfake) AND (memory OR misinformation) AND (sleep OR hypnosis OR hypnotic)` | 36 / 36, two pages |
| `(neurofeedback OR "real-time fMRI") AND (hypnosis OR hypnotic suggestion)` | 28 / 28, two pages |
| `decoded[Title/Abstract] AND neurofeedback[Title/Abstract]` | 54 / 54, two pages |
| `((decoded[Title/Abstract] AND neurofeedback[Title/Abstract]) OR DecNef[Title/Abstract] OR neuroreinforcement[Title/Abstract]) AND (sleep[Title/Abstract] OR nap[Title/Abstract] OR hypno*[Title/Abstract])` | 0 / 0 |
| `neurofeedback[Title/Abstract] AND sleep[Title/Abstract] AND (memory[Title/Abstract] OR consolidation[Title/Abstract])` | 21 / 21 |
| `(deepfake[Title/Abstract] OR chatbot[Title/Abstract] OR "AI-generated"[Title/Abstract]) AND ("false memories"[Title/Abstract] OR "false memory"[Title/Abstract])` | 2 / 2 |
| `sleep[Title/Abstract] AND misinformation[Title/Abstract]` | 25 / 58 |
| `sleep[Title/Abstract] AND "false memories"[Title/Abstract]` | 25 / 60 |
| `hypno*[Title/Abstract] AND ("false memory"[Title/Abstract] OR "false memories"[Title/Abstract] OR misinformation[Title/Abstract])` | 25 / 36 |
| `("false memories"[Title/Abstract] OR "false memory"[Title/Abstract]) AND (chatbot[Title/Abstract] OR deepfake[Title/Abstract] OR "AI-generated"[Title/Abstract]) AND (sleep[Title/Abstract] OR hypno*[Title/Abstract])` | 0 / 0 |

Targeted primary-site web searches supplemented PubMed for HCI publications and replication leads. They identified the final IUI study below, but did not establish an independent exact replication of the focal generative-witness or confidence protocol. This is bounded negative discovery, not proof of universal absence. Articles about an AI agent’s own stored memory, sleep-health misinformation, chatbot automation of a memory task, and conceptual LLM/hypnosis parallels were not counted as human distortion-combination experiments.

Citation metadata were retrieved for all 25 selected PMIDs; 24 supplied complete abstracts. R05 supplied no abstract in either PubMed or PMC; its selected 2,500-character primary-body opening was inspected instead, with the remaining body not retrieved in this pass. Ten other rights-eligible PMC bodies were retrieved in complete contiguous coverage: original visual learning, visual-motion extension, both confidence reports, fear-decoder validation, the data collection, movie deepfakes, the sleep-reactivation pilot, insomnia sham control, and decoded fNIRS. Selected methods/results/limitations and cohort relationships were inspected; no participant data, code, or original analyses were rerun. Selected results/design/limitations in the 17-page final IUI PDF were also inspected. Other entries remain abstract-level checks. Private lookup/text receipts are outside Git.

The 2017 confidence paper explicitly says its experimental data are identical to the 2016 companion’s. The release paper’s Tables 1–2 independently groups those reports as one ten-person feedback study. It also maps shared common-fear data to two publications; checking the decoder paper shows additional validation data, so that mapping does not mean its entire dataset is identical to the intervention paper’s. Released subsets differ from original cohorts in some rows; the release is not a new intervention. Publication issue dates below follow PubMed; the release paper uses the earlier online date for the Molecular Psychiatry report.

## Selected sources and study roles

<a id="r01"></a>
### R01 — Original orientation learning

Shibata et al. (2011), [Perceptual learning incepted by decoded fMRI neurofeedback without stimulus presentation](https://pubmed.ncbi.nlm.nih.gov/22158821/). DOI: `10.1126/science.1212003`. **Primary study; complete body retrieved, selected sections checked.** Ten feedback participants; decoder construction involved real visual stimuli. The no-target-stimulus claim concerns induction, not an absence of previous exposure or calibration.

<a id="r02"></a>
### R02 — New visual-motion experiment

Wang et al. (2021), [Visual perceptual learning of a primitive feature in human V1/V2 as a result of unconscious processing, revealed by decoded functional MRI neurofeedback](https://pubmed.ncbi.nlm.nih.gov/34431964/). DOI: `10.1167/jov.21.8.24`. **New primary experiment; complete body retrieved, selected sections checked.** Eight feedback and eight analyzed controls; two control participants excluded for age mismatch. Shared researchers and changed visual features make this a conceptual extension, not independent exact replication.

<a id="r03"></a>
### R03 — Confidence companion report

Cortese et al. (2016), [Multivoxel neurofeedback selectively modulates confidence without changing perceptual performance](https://pubmed.ncbi.nlm.nih.gov/27976739/). DOI: `10.1038/ncomms13669`. **Primary report; complete body retrieved, selected sections checked.** Seventeen usable initial decoding datasets, ten feedback participants after selection. Shares experimental data with R04.

<a id="r04"></a>
### R04 — Same data, order and interference analysis

Cortese et al. (2017), [Decoded fMRI neurofeedback can induce bidirectional confidence changes within single participants](https://pubmed.ncbi.nlm.nih.gov/28163140/). DOI: `10.1016/j.neuroimage.2017.01.069`. **Companion analysis; complete body retrieved, selected sections checked.** Explicit same-data declaration in Participants. Useful order/interference findings do not constitute independent replication of R03.

<a id="r05"></a>
### R05 — Conditioned-threat starting point

Koizumi et al. (2016), [Fear reduction without fear through reinforcement of neural activity that bypasses conscious exposure](https://pubmed.ncbi.nlm.nih.gov/28989977/). DOI: `10.1038/s41562-016-0006`. **Primary study; citation metadata and selected PMC-body opening checked; no abstract supplied.** Restricted conditioned-threat endpoints; later studies change targets/populations. Publication count does not establish broad symptom relief. Only the opening 2,500 characters of the body were retrieved in this pass.

<a id="r06"></a>
### R06 — Common-fear extension

Taschereau-Dumouchel et al. (2018), [Towards an unconscious neural reinforcement intervention for common fears](https://pubmed.ncbi.nlm.nih.gov/29511106/). DOI: `10.1073/pnas.1721572115`. **Primary study; abstract checked, dataset relationship checked through R10.** A target/population extension within an overlapping collaboration. R07 analyzes the same study family.

<a id="r07"></a>
### R07 — Subjective fear is not its physiological proxy

Taschereau-Dumouchel et al. (2020 journal issue), [Multivoxel pattern analysis reveals dissociations between subjective fear and its physiological correlates](https://pubmed.ncbi.nlm.nih.gov/31659269/). DOI: `10.1038/s41380-019-0520-3`. **Decoder-validation study with shared/additional data; complete body retrieved, selected sections checked.** Discovery n = 31; a new-person validation cohort n = 12; a different-task validation dataset n = 17 overlaps discovery participants. Distinguishes reported fear from physiology. No new intervention replication is established. R10 uses the earlier online year, 2019.

<a id="r08"></a>
### R08 — Clinical extension, not large-scale confirmation

Cushing et al. (2024), [A double-blind trial of decoded neurofeedback intervention for specific phobias](https://pubmed.ncbi.nlm.nih.gov/39221769/). DOI: `10.1111/pcn.13726`. **Primary clinical extension; fresh abstract/identity, prior selected full-text checks retained in D09.** Neural analysis n = 18; self-reported fear did not significantly change. Shared investigators and changed cohort/endpoint differ from independent exact replication. The earlier preprint is the same trial.

<a id="r09"></a>
### R09 — Independent conceptual boundary test

Margolles et al. (2024), [Unconscious Manipulation of Conceptual Representations with Decoded Neurofeedback Impacts Search Behavior](https://pubmed.ncbi.nlm.nih.gov/37985180/). DOI: `10.1523/JNEUROSCI.1235-23.2023`. **Primary experiment; fresh abstract/identity, prior selected primary-HTML checks retained in D11.** Different research team; failed intended symbol-specific priming alongside target-category search impairment. Not a direct replication of R01 or R03.

<a id="r10"></a>
### R10 — Published-data collection

Cortese et al. (2021), [The DecNef collection, fMRI data from closed-loop decoded neurofeedback experiments](https://pubmed.ncbi.nlm.nih.gov/33623035/). DOI: `10.1038/s41597-021-00845-7`. **Data release; complete body retrieved, selected tables/sections checked.** Five earlier study datasets; cohort/publication mapping confirms reuse. No raw dataset was downloaded or independently analyzed in this review.

<a id="r11"></a>
### R11 — Co-adaptation engineering

Abdennour et al. (2026), [Enhancing fMRI Decoded Neurofeedback with Co-adaptive Training: Simulation and Proof-of-principle Evidence](https://pubmed.ncbi.nlm.nih.gov/41644844/). DOI: `10.1007/s12021-026-09768-3`. **Simulation and real-time proof-of-concept report; abstract checked.** Addresses context/distribution differences between decoder construction and feedback. Improved target induction is not clinical replication or demonstrated semantic transfer.

<a id="r12"></a>
### R12 — Decoded fNIRS and limited transfer

Zeng et al. (2025), [Improving interference control without conflict exposure: prefrontal fNIRS-decoded neurofeedback training](https://pubmed.ncbi.nlm.nih.gov/41347227/). DOI: `10.1117/1.NPh.12.4.045009`. **Primary randomized double-blind study; complete body retrieved, selected sections checked.** Groups n = 20/25; Stroop benefit, no Stop-Signal Task transfer. Individual calibration, group decoder differences, and lack of short-channel regression constrain interpretation of possible physiological-noise effects.

<a id="r13"></a>
### R13 — Decoded EEG with an explicit strategy

Li et al. (2024), [Decoded EEG neurofeedback-guided cognitive reappraisal training for emotion regulation](https://pubmed.ncbi.nlm.nih.gov/39555250/). DOI: `10.1007/s11571-024-10108-x`. **Primary study; abstract checked.** N = 42, healthy adults, explicit reappraisal. Restricted low-positive-valence benefit is not a sleep, hypnosis, or arbitrary-writing result.

<a id="r14"></a>
### R14 — Conventional feedback plus sleep reactivation

Lechinger et al. (2025), [Effects of Olfactory Learning Context Reactivation During Sleep on Training Success in a Double-Blind Randomized Controlled Sensorimotor Rhythm Neurofeedback Protocol: A Pilot Study](https://pubmed.ncbi.nlm.nih.gov/41060038/). DOI: `10.1111/psyp.70154`. **Primary randomized pilot; complete body retrieved, selected sections checked.** N = 49; no immediate reactivation benefit. Only 29 attended follow-up; the favorable contrast was exploratory. Conventional band-based EEG feedback, not decoded fMRI.

<a id="r15"></a>
### R15 — Feedback before hypnotic analgesia

Jensen et al. (2016), [Use of Neurofeedback to Enhance Response to Hypnotic Analgesia in Individuals With Multiple Sclerosis](https://pubmed.ncbi.nlm.nih.gov/26599991/). DOI: `10.1080/00207144.2015.1099400`. **Primary pilot; abstract checked.** N = 20, 18 completers; positive reported pain contrast against relaxation-plus-hypnosis. Conventional EEG preparation; no decoded-feedback or false-memory endpoint.

<a id="r16"></a>
### R16 — Later clinical preparation pilot

Jensen et al. (2018), [Use of neurofeedback and mindfulness to enhance response to hypnosis treatment in individuals with multiple sclerosis](https://pubmed.ncbi.nlm.nih.gov/29856281/). DOI: `10.1080/00207144.2018.1460546`. **Primary pilot; abstract checked.** N = 32; changed comparators and overlapping investigators. Individual participant overlap with R15 was not authenticated from abstract retrieval; no independent exact-replication claim is made.

<a id="r17"></a>
### R17 — No unique susceptibility advantage

Batty et al. (2006), [Relaxation strategies and enhancement of hypnotic susceptibility: EEG neurofeedback, progressive muscle relaxation and self-hypnosis](https://pubmed.ncbi.nlm.nih.gov/17113932/). DOI: `10.1016/j.brainresbull.2006.08.005`. **Primary randomized comparison; abstract checked.** N = 30; susceptibility increased across groups without superiority of theta/alpha feedback. Endpoint differs from clinical analgesia.

<a id="r18"></a>
### R18 — An active-control challenge in conventional feedback

Schabus et al. (2017), [Better than sham? A double-blind placebo-controlled neurofeedback study in primary insomnia](https://pubmed.ncbi.nlm.nih.gov/28335000/). DOI: `10.1093/brain/awx011`. **Primary controlled follow-up; complete body retrieved, selected sections checked.** N = 25; subjective improvements were comparable to sham and objective measures did not support the proposed benefit. Not a decoded-fMRI replication.

<a id="r19"></a>
### R19 — Deepfake format is not consistently superior

Murphy and Flynn (2022 journal issue), [Deepfake false memories](https://pubmed.ncbi.nlm.nih.gov/33910482/). DOI: `10.1080/09658211.2021.1919715`. **Two primary experiments; abstract checked.** N = 682 across experiments. Video did not consistently increase false-memory rates relative to text/photo formats. Publication issue year differs from the DOI’s 2021 year; these are one publication.

<a id="r20"></a>
### R20 — Movie-remake extension

Murphy et al. (2023), [Face/Off: Changing the face of movies with deepfakes](https://pubmed.ncbi.nlm.nih.gov/37410765/). DOI: `10.1371/journal.pone.0287503`. **Primary study; complete body retrieved, selected sections checked.** N = 436; false movie recollections, no deepfake advantage over written descriptions. Same research line as R19; not an exact replication of generated-image editing or chatbot interviewing.

<a id="r21"></a>
### R21 — A separate article-discussion experiment

Pataranutaporn et al. (2025), [Slip Through the Chat: Subtle Injection of False Information in LLM Chatbot Conversations Increases False Memory Formation](https://dspace.mit.edu/entities/publication/4425a046-bb57-49ac-911a-90ca9869d7bc). DOI: [10.1145/3708359.3712112](https://doi.org/10.1145/3708359.3712112). **Published IUI study; selected [final-PDF sections](https://dam-prod.media.mit.edu/x/2025/08/25/IUI-2025-Slip%20Through%20the%20Chat.pdf) checked.** N = 180; same research network as the earlier AI studies, new material/design. Immediate recall, one model; misleading chat exceeded misleading summary, while a general long-term or multimodal interaction effect was not tested.

<a id="r22"></a>
### R22 — Sleep effects depend on the memory task

Newbury and Monaghan (2019 journal issue), [When does sleep affect veridical and false memory consolidation? A meta-analysis](https://pubmed.ncbi.nlm.nih.gov/30264239/). DOI: `10.3758/s13423-018-1528-4`. **Synthesis; abstract checked.** No overall effect within the themed-word-list literature; task features moderated results. No AI studies or new intervention cohort are supplied by this synthesis.

<a id="r23"></a>
### R23 — A story-based null sleep effect

Van Rijn et al. (2017), [Sleep does not cause false memories on a story-based test of suggestibility](https://pubmed.ncbi.nlm.nih.gov/28458092/). DOI: `10.1016/j.concog.2017.04.010`. **Primary experiment; abstract checked.** Accurate memory preservation and no false-memory difference oppose a universal sleep-amplification claim. No generated-content intervention.

<a id="r24"></a>
### R24 — Deprivation and encoding timing

Frenda et al. (2014), [Sleep deprivation and false memories](https://pubmed.ncbi.nlm.nih.gov/25031301/). DOI: `10.1177/0956797614534694`. **Primary experiments; abstract checked.** Increased misinformation errors depended on deprivation during encoding, not merely after encoding. Does not establish the same effect of normal sleep, AI content, or hypnotic induction.

<a id="r25"></a>
### R25 — Trait, induction, and context separated

Barnier and McConkey (1992), [Reports of real and false memories: the relevance of hypnosis, hypnotizability, and context of memory test](https://pubmed.ncbi.nlm.nih.gov/1500609/). DOI: `10.1037//0021-843x.101.3.521`. **Primary experiment; abstract checked.** N = 60; hypnotizability and test context predicted false reports while induction did not supply the proposed enhancement. Not an AI-combination experiment or a universal null for hypnosis.

<a id="r26"></a>
### R26 — Overnight retention in motor-imagery feedback

[Event-related desynchronization in motor imagery with EEG neurofeedback in the context of declarative interference and sleep](https://pubmed.ncbi.nlm.nih.gov/40568446/). DOI: `10.1016/j.ynirp.2021.100058`. **Primary EEG-feedback experiment; abstract checked.** Within-session gains, no overnight gain in the reported desynchronization endpoint. The group manipulation concerned memory interference, not a randomized sleep/wake contrast. Adjacent evidence, not an fMRI-DecNef replication.

## Interpretation boundary

Direct replication requires an appropriately matched new experiment; research-team independence is a further dimension. Data release, secondary analysis, independent conceptual extension, and a changed clinical endpoint are valuable but different evidence. No direct combined DecNef–sleep/hypnosis or AI-distortion–sleep/hypnosis endpoint was established in this review. The adjacent positive pilots, null comparisons, and measurement limits remain visible rather than averaged into a single capability score.
