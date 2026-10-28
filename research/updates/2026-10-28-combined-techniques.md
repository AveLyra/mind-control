# Combined-technique source checks — October 28, 2026

[Synthesis](../../wiki/combined-techniques.md) · [Research horizon](../../wiki/research-horizon.md) · [Catalog](../../sources/catalog.md)

**Origin:** new editorial research record. These are 16 selected publications, not 16 independent experiments. Reanalyses and publication versions are identified below. The four combination judgments are in the linked synthesis; this record preserves source identity, retrieval scope, and narrow endpoints.

## Search and access scope

Ten distinct PubMed searches used an October 28, 2026 publication-date upper bound. The decoded-feedback control query was paged through both result pages; the other large result sets were screened only on their first returned page. Irrelevant broad-query hits and uninspected pages provide no negative evidence. Web discovery and primary-document inspection supplemented PubMed for AI/HCI publications not identified by the biomedical searches.

| PubMed query | Returned / total records |
|---|---:|
| `"targeted memory reactivation" AND (nightmare* OR "imagery rehearsal")` | 9 / 9 |
| `hypnotic suggestion slow wave sleep` | 10 / 126 |
| `("decoded neurofeedback" OR DecNef) AND (fear OR conditioning OR reinforcement)` | 10 / 20 |
| `associative decoded fMRI neurofeedback color` | 2 / 2 |
| `("generative artificial intelligence" OR "large language model" OR "AI-generated" OR "AI-edited") AND "false memory"` | 2 / 2 |
| `"targeted memory reactivation" AND fear AND (extinction OR return OR replication)` | 3 / 3 |
| `hypnosis AND "targeted memory reactivation"` | 0 / 0 |
| `("decoded neurofeedback" OR DecNef) AND (randomized OR randomised OR sham OR replication OR placebo)` | 12 / 12, two pages |
| `hypnotic suggestion sleep spindle coupling memory` | 6 / 6 |
| `("chatbot" OR "AI-generated") AND (misinformation OR "false memories") AND (warning OR accurate OR replication OR source)` | 10 / 484 |

All 13 selected PMIDs had metadata and complete abstracts retrieved. Complete PMC bodies were retrieved for Beck (36,704 characters), Cushing (32,423), and Borghese (58,462, in contiguous parts). Selected methods/results/discussion were inspected; no raw data, code, figures, supplements, or analyses were independently reproduced. Two connector attempts for Margolles failed; selected primary PMC HTML sections were then read through the web tool. Its access route is separate from the three complete connector bodies.

For Schwartz, the direct publisher PDF returned HTTP 403. A publicly accessible 15-page published-version PDF was then located through the university repository; selected design, results, limitations, and follow-up methods were checked. This established the absence of an unstimulated arm and the three-month follow-up denominator. It is additional primary-text inspection, not a fourth complete PMC connector retrieval or a new experiment.

Selected primary HTML sections were also inspected for the three AI papers. The visual-media study’s final CHI identity and abstract were verified in the institutional repository; its final PDF fetch returned HTTP 429. Detailed results/limitations were inspected in the explicitly identified preprint version, not silently attributed to a newly read final PDF. The conversational paper and 2026 summary paper are treated as preprint texts here; conference-publication status was not independently established for those two. These versions are not additional studies.

Private lookup receipts remain outside Git. No combined intervention, participant experiment, new statistical analysis, or recurring monitor was run. This is a bounded, falsification-oriented review, not a systematic review or a clinical recommendation.

## Selected sources

<a id="d01"></a>
### D01 — Imagery rehearsal plus sleep cueing

Schwartz et al. (2022), [Enhancing imagery rehearsal therapy for nightmares with targeted memory reactivation](https://pubmed.ncbi.nlm.nih.gov/36306786/). DOI: `10.1016/j.cub.2022.09.032`. **Primary randomized study; abstract and selected published-PDF sections checked.** See the [university repository](https://archive-ouverte.unige.ch/unige:165230). N = 36, with 28 follow-up responders. Reports a rescript–cue benefit; no unstimulated arm or full factorial interaction test. Exact dream scripting was not established.

<a id="d02"></a>
### D02 — EMDR plus sleep reactivation

Van der Heijden et al. (2024), [Targeted memory reactivation to augment treatment in post-traumatic stress disorder](https://pubmed.ncbi.nlm.nih.gov/39116885/). DOI: `10.1016/j.cub.2024.07.019`. **Primary augmentation study; abstract checked.** TMR n = 17, sham n = 16. Reports selected avoidance and oscillatory outcomes; does not establish improvement across every clinical endpoint or an instruction-installation capability.

<a id="d03"></a>
### D03 — A null relaxation–cueing combination

Sayk et al. (2026), [Reactivating a Relaxation Exercise During Sleep to Influence Cortical Hyperarousal in Individuals With Frequent Nightmares](https://pubmed.ncbi.nlm.nih.gov/42714131/). DOI: `10.1111/jsr.70443`. **Primary randomized blinded crossover; abstract checked.** N = 25. No benefit on the targeted beta/gamma hyperarousal measures or nightmare symptoms; spindle changes were not an established clinical mechanism. Different procedure from D01, so not its direct replication.

<a id="d04"></a>
### D04 — Social anxiety: no added subjective benefit

Borghese et al. (2022), [Targeted Memory Reactivation During REM Sleep in Patients With Social Anxiety Disorder](https://pubmed.ncbi.nlm.nih.gov/35845468/). DOI: `10.3389/fpsyt.2022.904704`. **Primary randomized study; complete body retrieved, selected sections checked.** N = 48. No between-group added anxiety benefit after a week. Correlations within the cueing group are not substitutes for the group comparison.

<a id="d05"></a>
### D05 — Spindles without added phobia-treatment benefit

Rihm et al. (2016), [Re-presentation of Olfactory Exposure Therapy Success Cues during Non-Rapid Eye Movement Sleep did not Increase Therapy Outcome but Increased Sleep Spindles](https://pubmed.ncbi.nlm.nih.gov/27445775/). DOI: `10.3389/fnhum.2016.00340`. **Primary human study; abstract checked.** Some spindle changes accompanied a null clinical augmentation result. A ceiling effect is a proposed explanation, not proof of the underlying reason.

<a id="d06"></a>
### D06 — Hypnotic suggestion and sleep depth

Cordi et al. (2014), [Deepening sleep by hypnotic suggestion](https://pubmed.ncbi.nlm.nih.gov/24882909/). DOI: `10.5665/sleep.3778`. **Primary controlled nap experiments; abstract checked.** Seventy women participated across the reported experiments. Benefits depended on responsiveness; the overall enrollment must not become the sample size of every individual contrast. No suggestion-plus-TMR interaction was tested by this report.

<a id="d07"></a>
### D07 — Extension to nighttime sleep

Cordi et al. (2020), [Hypnotic suggestions given before nighttime sleep extend slow-wave sleep as compared to a control text in highly hypnotizable subjects](https://pubmed.ncbi.nlm.nih.gov/31914371/). DOI: `10.1080/00207144.2020.1687260`. **Primary human study; abstract checked.** N = 43, including high/low responsiveness. Increased sleep-depth measures against a control text do not establish improvement above no intervention or memory enhancement.

<a id="d08"></a>
### D08 — An important proxy–outcome dissociation

Beck et al. (2021), [Hypnotic Suggestions Increase Slow-Wave Parameters but Decrease Slow-Wave Spindle Coupling](https://pubmed.ncbi.nlm.nih.gov/34393533/). DOI: `10.2147/NSS.S316997`. **Reanalysis of two earlier datasets; complete body retrieved, selected sections checked.** N = 33 highly hypnotizable participants. Slow-wave measures increased without a word-pair retention benefit; coupling decreased. The proposed mechanistic explanation is not a proven mediator. Do not count the reused night/nap data as independent new replications.

<a id="d09"></a>
### D09 — Decoded reinforcement in a small clinical cohort

Cushing et al. (2024), [A double-blind trial of decoded neurofeedback intervention for specific phobias](https://pubmed.ncbi.nlm.nih.gov/39221769/). DOI: `10.1111/pcn.13726`. **Primary controlled trial; complete body retrieved, selected sections checked.** Primary neural analysis n = 18; fear ratings n = 17. Target/control-phobia amygdala interaction p = .033; no significant self-reported fear change. The attentional-task interaction was p = .055, so within-target significance does not establish a significant differential task effect. No long-term or real-life avoidance benefit was established. The 2023 preprint discovered in search is the same trial, not a replication. Registry details were not newly retrieved in this pass.

<a id="d10"></a>
### D10 — Earlier threat-response reinforcement

Taschereau-Dumouchel et al. (2018), [Towards an unconscious neural reinforcement intervention for common fears](https://pubmed.ncbi.nlm.nih.gov/29511106/). DOI: `10.1073/pnas.1721572115`. **Primary human study; abstract checked.** Supports restricted representation-linked reinforcement and physiological endpoints; it is not evidence of arbitrary thoughts or goals being installed.

<a id="d11"></a>
### D11 — Neural induction without intended symbol–meaning transfer

Margolles et al. (2024), [Unconscious Manipulation of Conceptual Representations with Decoded Neurofeedback Impacts Search Behavior](https://pubmed.ncbi.nlm.nih.gov/37985180/). DOI: `10.1523/JNEUROSCI.1235-23.2023`. **Primary experiment; abstract and selected [primary PMC HTML](https://pmc.ncbi.nlm.nih.gov/articles/PMC10866193/) checked after connector errors.** The intended symbol-specific priming was absent despite target-pattern learning; target-category search was impaired. The awareness assessment included 12/18 correct target guesses, low confidence, and a nonsignificant group test. That test cannot establish exactly zero target knowledge.

<a id="d12"></a>
### D12 — Restricted associative perceptual change

Amano et al. (2016), [Learning to Associate Orientation with Color in Early Visual Areas by Associative Decoded fMRI Neurofeedback](https://pubmed.ncbi.nlm.nih.gov/27374335/). DOI: `10.1016/j.cub.2016.05.014`. **Primary human study; abstract checked.** Reports an orientation–color bias and later persistence in its task. Task-specific perception is not flexible symbolic comprehension or autobiographical replacement.

<a id="d13"></a>
### D13 — Confidence as a separate feedback target

Cortese et al. (2017), [Decoded fMRI neurofeedback can induce bidirectional confidence changes within single participants](https://pubmed.ncbi.nlm.nih.gov/28163140/). DOI: `10.1016/j.neuroimage.2017.01.069`. **Primary human study; abstract checked.** Reports opposing confidence changes with order dependence and weaker effects in the second session, interpreted as anterograde learning interference. This is direct evidence against assuming free stackability. Confidence and accuracy remain separate; this is not a general will-control result.

<a id="d14"></a>
### D14 — AI-edited visual material and recall errors

Pataranutaporn et al. (2025), [Synthetic Human Memories: AI-Edited Images and Videos Can Implant False Memories and Distort Recollection — final CHI metadata/abstract](https://dspace.mit.edu/entities/publication/7d46de1f-6a49-42ab-9700-c37efa0ba991). DOI: [10.1145/3706598.3713697](https://doi.org/10.1145/3706598.3713697). **Primary preregistered study, N = 200; final identity/abstract and selected [preprint v1 results/limitations](https://arxiv.org/html/2409.08895v1) checked.** Final PDF retrieval was blocked by HTTP 429. The inspected results concern errors about probed images after limited exposure, not entire invented life histories. Published and preprint versions are one study. The numerical ranking of media conditions is not an interaction test.

<a id="d15"></a>
### D15 — Suggestive AI interviews

Chan et al. (2024), [Conversational AI Powered by Large Language Models Amplifies False Memories in Witness Interviews](https://arxiv.org/abs/2408.04681); selected [v1 methods/results](https://arxiv.org/html/2408.04681v1). **Primary experimental preprint, N = 200; selected sections checked.** Suggestive interviews increased detail-level errors and confidence, with a one-week test. No peer-reviewed publication identity was established here; additional feedback/content in the generative condition complicates attributing the effect to conversational form alone.

<a id="d16"></a>
### D16 — Misleading content versus supposed authorship

Sim, Eiger, and Kohno (2026), [AI-Enabled Human Memory Manipulation: Misleading AI-Generated Summaries Distort Human Memory](https://arxiv.org/abs/2609.28820); selected [v1 results/limitations](https://arxiv.org/html/2609.28820v1). **Primary experiment inspected as a preprint; final conference publication not independently verified.** Of 331 completers, 328 entered analyses. Misleading content affected a critical recognition answer; source attribution and tested trust/use interactions were nonsignificant. All experimental summaries were AI-generated, including those labeled human, so this is not a comparison of actual human and AI composition.

## What the checks do not establish

None of these sources tests a system combining sleep cueing, hypnosis, decoded reinforcement, and generated autobiographical feedback. Neither a missing search hit nor a null outcome proves impossibility. Conversely, a neural change, a within-group correlation, a two-arm benefit, and a numerically larger mean do not jointly establish interaction, generalization, intent, or source attribution. Fictional uses must preserve that boundary.
