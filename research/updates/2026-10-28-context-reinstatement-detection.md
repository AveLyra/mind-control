# Context reinstatement and discrepancy detection: source checks

[Synthesis](../../wiki/context-reinstatement-and-detection.md) · [Earlier prediction/RES review](../../wiki/prediction-error-and-suggestibility.md) · [Catalog](../../sources/catalog.md)

**Origin:** bounded editorial review, October 28, 2026, America/New_York. The 26 selected entries are source publications, including a same-data analysis and a meta-analysis, not 26 independent experiments or replications. Earlier research records remain preserved.

## Discovery and inspection scope

Sixteen distinct PubMed queries used the publication-date upper bound October 28, 2026. Titles/metadata were screened; overlapping counts are not additive study counts. Broad discrepancy and AI queries included irrelevant results and were not exhausted. Some known-item title searches did not retrieve articles later located through primary sites/PMC identifiers and direct PMID lookup. These observed misses further limit negative discovery claims.

| Query | Distinct PMIDs screened / returned total |
|---|---:|
| `("context reinstatement"[Title/Abstract] OR "mental reinstatement"[Title/Abstract] OR "contextual reinstatement"[Title/Abstract]) AND (misinformation[Title/Abstract] OR "false memory"[Title/Abstract] OR "false memories"[Title/Abstract])` | 9 / 9 |
| `("discrepancy detection"[Title/Abstract] OR "discrepancies"[Title/Abstract] OR "change recollection"[Title/Abstract]) AND (misinformation[Title/Abstract] OR "false memories"[Title/Abstract])` | 35 / 60 |
| `("context reinstatement"[Title/Abstract] OR "context reactivation"[Title/Abstract] OR "contextual cues"[Title/Abstract]) AND sleep[Title/Abstract]` | 18 / 18 |
| `(context[Title/Abstract] OR reinstatement[Title/Abstract]) AND (hypnosis[Title/Abstract] OR "hypnotic"[Title/Abstract]) AND (memory[Title/Abstract] OR recall[Title/Abstract])` | 30 / 33 |
| `(chatbot[Title/Abstract] OR "AI-generated"[Title/Abstract] OR "generative AI"[Title/Abstract] OR deepfake[Title/Abstract]) AND ("context reinstatement"[Title/Abstract] OR "discrepancy detection"[Title/Abstract] OR "misinformation detection"[Title/Abstract])` | 10 / 10 |
| `("targeted memory reactivation"[Title/Abstract] OR "memory reactivation"[Title/Abstract]) AND sleep[Title/Abstract] AND ("false memory"[Title/Abstract] OR "false memories"[Title/Abstract] OR "source memory"[Title/Abstract])` | 1 / 1 |
| `"discrepancy detection"[Title/Abstract] AND (memory[Title/Abstract] OR misinformation[Title/Abstract])` | 6 / 6 |
| `("change recollection"[Title/Abstract] OR "change detection"[Title/Abstract]) AND misinformation[Title/Abstract]` | 2 / 2 |
| `("cognitive interview"[Title/Abstract] OR "context reinstatement"[Title/Abstract]) AND hypnosis[Title/Abstract]` | 5 / 5 |
| `("context reinstatement"[Title/Abstract] OR "contextual reinstatement"[Title/Abstract]) AND (misattribution[Title/Abstract] OR false[Title/Abstract] OR misinformation[Title/Abstract])` | 14 / 14 |
| `sleep[Title/Abstract] AND (context[Title/Abstract] OR contextual[Title/Abstract]) AND ("targeted memory reactivation"[Title/Abstract] OR "memory reactivation"[Title/Abstract])` | 22 / 22 |
| `("AI-generated"[Title/Abstract] OR "generative AI"[Title/Abstract] OR chatbot[Title/Abstract]) AND (misinformation[Title/Abstract] OR "false memories"[Title/Abstract]) AND (warning[Title/Abstract] OR detection[Title/Abstract] OR accuracy[Title/Abstract])` | 25 / 112 |
| `"Protecting memory from misinformation"[Title] OR "Warning before misinformation exposure"[Title] OR "In search of a Goldilocks zone"[Title]` | 0 / 0 |
| `"Promoting memory consolidation during sleep"[Title] OR "false memories"[Title] AND "reactivation"[Title]` | 1 / 1 |
| `"Memory and belief updating following complete and partial reminders of fake news"[Title]` | 0 / 0 |
| `10.3758/s13415-024-01183-y` | 1 / 1 |

Primary-site web searches supplemented the connector for source identification, cohort relationships, and date checks. Software-agent memory, detector benchmarks and general AI-answer quality were not counted as human context/episodic-memory evidence. An AI-news candidate with a November 2026 issue date was not used because an earlier online date was not verified within this pass. No completeness or field-wide absence is claimed.

All 26 selected PMIDs supplied complete provided abstracts and citation metadata. Twenty-five had DOIs in that retrieval; K22 did not. The incremental Europe PMC check subsequently supplied K22's DOI, `10.2307/30039056`; an independent Crossref lookup matched its title, authors and journal. The provider distinction is preserved rather than attributing that DOI to the PubMed connector. Nine PMC article bodies were retrieved in complete contiguous coverage: K05, K06, K08, K14, K15, K16, K17, K20 and K25. Selected methods/results/limitations were inspected; this is not a full independent review of every table, supplement, cohort or model. K07 had two failed body requests and K19 one; these remain abstract-level checks. K01's earlier complete-body check is retained through P13 rather than counted as a fresh retrieval.

The warning encoding paper explicitly reuses data and behavioral results from the earlier fMRI report, with only two conditions analyzed. The 2020 paper separately reports a behavioral experiment with 81 participants and an fMRI final sample of 65; the 2024 analysis uses 43 from that fMRI sample. The reports differ in exclusion accounting (80 recruited/19 excluded/65 final in 2020; 80/15/65 in 2024). The earlier arithmetic is internally inconsistent; participant-level records were not checked and the discrepancy was not silently repaired. Neither paper count nor publication date supplies an independent replication.

Primary neural effects and the proposed mediator remain separate causal claims. The TMR false-memory subgroup estimate is reported from the synthesis, not independently recalculated. Raw retrieval receipts remain private. No participant intervention, scientific experiment, data/code reanalysis, or recurring monitor was performed.

## Selected sources and roles

<a id="k01"></a>
### K01 — Telling a good story: The effects of memory retrieval and context processing on eyewitness suggestibility

Jessica A LaPaglia et al. (2019). [Telling a good story: The effects of memory retrieval and context processing on eyewitness suggestibility](https://pubmed.ncbi.nlm.nih.gov/30789952/). DOI: `10.1371/journal.pone.0212592`. **Primary context/RES experiments; fresh abstract, prior P13 body check retained.** Context during the later account affected RES across narrative/question formats. Earlier complete-body inspection and its conditional-analysis cautions remain recorded in P13; this is not a newly counted replication.

<a id="k02"></a>
### K02 — Discrepancy detection in the retrieval-enhanced suggestibility paradigm

Brendon Jerome Butler et al. (2018 Apr). [Discrepancy detection in the retrieval-enhanced suggestibility paradigm](https://pubmed.ncbi.nlm.nih.gov/28899262/). DOI: `10.1080/09658211.2017.1371193`. **Three primary discrepancy experiments; complete abstract checked.** Concurrent consistency assessment negated overall RES. Retrospective detection associated with resistance but not uniform immunity. Detected subgroups are post-treatment selections, not randomized moderator groups.

<a id="k03"></a>
### K03 — When Misinformation Improves Memory

Adam L Putnam et al. (2017 Jan). [When Misinformation Improves Memory](https://pubmed.ncbi.nlm.nih.gov/27879321/). DOI: `10.1177/0956797616672268`. **Two primary change-memory experiments; complete abstract checked.** Original recognition improved for changes both noticed and remembered. This conditional pattern supports recursive reminding, while memory/item strength remains a competing explanation for some associations.

<a id="k04"></a>
### K04 — Effects of postwarning specificity on memory performance and confidence in the eyewitness misinformation paradigm

Philip A Higham et al. (2017 Dec). [Effects of postwarning specificity on memory performance and confidence in the eyewitness misinformation paradigm](https://pubmed.ncbi.nlm.nih.gov/28816470/). DOI: `10.1037/xap0000140`. **Two primary postwarning experiments; complete abstract checked.** Item-specific warnings were more effective than general warnings in the tested recognition/recall formats. Discrepancy detection and specific-warning conditions also produced facilitation. No universal warning rule follows.

<a id="k05"></a>
### K05 — Protecting memory from misinformation: Warnings modulate cortical reinstatement during memory retrieval

Jessica M Karanian et al. (2020 Sep 15). [Protecting memory from misinformation: Warnings modulate cortical reinstatement during memory retrieval](https://pubmed.ncbi.nlm.nih.gov/32868423/). DOI: `10.1073/pnas.2008595117`. **Primary behavioral/fMRI report; complete PMC body, selected sections checked.** Separate behavioral experiment (81 reported participants) and fMRI experiment (65 final participants reported). Warning conditions altered errors and source-modality-related retrieval activity. The fMRI methods list 80 recruited, 19 excluded and 65 final, an unresolved arithmetic inconsistency. No participant-level flow audit here.

<a id="k06"></a>
### K06 — Warning before misinformation exposure modulates memory encoding

Jessica M Karanian et al. (2024 Jun). [Warning before misinformation exposure modulates memory encoding](https://pubmed.ncbi.nlm.nih.gov/38504050/). DOI: `10.3758/s13415-024-01183-y`. **Same-data encoding analysis; complete PMC body and selected publisher HTML checked.** Explicitly reuses K05's fMRI data and behavioral results, selecting prewarning/no-warning groups (21 + 22 = 43). This adds encoding-phase analysis, not an independent behavioral replication. Reports 80 recruited/15 excluded/65 final, differing from K05's exclusion count. Neural mediator specificity remains inferred.

<a id="k07"></a>
### K07 — Neural context reinstatement predicts memory misattribution

Samuel J Gershman et al. (2013 May 15). [Neural context reinstatement predicts memory misattribution](https://pubmed.ncbi.nlm.nih.gov/23678104/). DOI: `10.1523/JNEUROSCI.0096-13.2013`. **Primary neural context/misattribution study; complete abstract checked.** Classifier-related reinstatement during new learning predicted later source errors. Two PMC attempts returned internal errors; no fresh complete-body inspection. Related to the Hupbach updating research line, not an independent proof of trace erasure.

<a id="k08"></a>
### K08 — Reinstatement of item-specific contextual details during retrieval supports recombination-related false memories

Alexis C Carpenter et al. (2021 Aug 01). [Reinstatement of item-specific contextual details during retrieval supports recombination-related false memories](https://pubmed.ncbi.nlm.nih.gov/33836273/). DOI: `10.1016/j.neuroimage.2021.118033`. **Primary inference/context study; complete PMC body, selected sections checked.** Successful inference was linked to reinstatement of the wrong overlapping context and source misattributions. These neural associations do not by themselves establish what caused the source error.

<a id="k09"></a>
### K09 — The Dark Side of Context: Context Reinstatement Can Distort Memory

Manoj K Doss et al. (2018 Jun). [The Dark Side of Context: Context Reinstatement Can Distort Memory](https://pubmed.ncbi.nlm.nih.gov/29671680/). DOI: `10.1177/0956797617749534`. **Primary context-recognition experiments; complete abstract checked.** Reinstated backgrounds increased hits and similar-lure false alarms, including confident errors despite warnings. Multiple within-report tests are not multiple independent-team replications.

<a id="k10"></a>
### K10 — Litmus test of rich episodic representations: Context-induced false recognition

Ágnes Szőllősi et al. (2023 Jan). [Litmus test of rich episodic representations: Context-induced false recognition](https://pubmed.ncbi.nlm.nih.gov/36156388/). DOI: `10.1016/j.cognition.2022.105287`. **Primary related-lure experiment; complete abstract checked.** Different research team, related item/context-lure design. Supports conceptual convergence of true/false recognition effects, not an unchanged exact replication of K09.

<a id="k11"></a>
### K11 — Reducing false memories via context reinstatement: the roles of encoding and retrieval contexts

Kerri A Goodwin (2013). [Reducing false memories via context reinstatement: the roles of encoding and retrieval contexts](https://pubmed.ncbi.nlm.nih.gov/23858954/). DOI: `10.5406/amerjpsyc.126.2.0213`. **Three primary strategy-reinstatement experiments; complete abstract checked.** Elaborative encoding and its reinstatement reduced DRM false recall under specified conditions. Encoding strategy is a different kind of context from a perceptual scene.

<a id="k12"></a>
### K12 — Putting false memories into context: the effects of odour contexts on correct and false recall

Joshua A Woods et al. (2019 Mar). [Putting false memories into context: the effects of odour contexts on correct and false recall](https://pubmed.ncbi.nlm.nih.gov/30139301/). DOI: `10.1080/09658211.2018.1512632`. **Two primary odor-context experiments; complete abstract checked.** Correct recall benefited from matching context; false recall was unaffected in one experiment and reduced in the other. Delay/material changes and different outcome directions limit universal claims.

<a id="k13"></a>
### K13 — Context reinstatement increases true and false recognition of associated words: Evidence from the Deese/Roediger-McDermott (DRM) illusion

Asia Bayoud et al. (2026 Apr 29). [Context reinstatement increases true and false recognition of associated words: Evidence from the Deese/Roediger-McDermott (DRM) illusion](https://pubmed.ncbi.nlm.nih.gov/42056461/). DOI: `10.3758/s13421-026-01892-4`. **Three primary word-context experiments; complete abstract checked.** Conceptual extension from the same broader Gallo research line as K09. Reinstatement increased true/false word recognition; a stronger warning attenuated both. Not independent exact replication or guaranteed protection.

<a id="k14"></a>
### K14 — Memory and belief updating following complete and partial reminders of fake news

Paige L Kemp et al. (2024 May 07). [Memory and belief updating following complete and partial reminders of fake news](https://pubmed.ncbi.nlm.nih.gov/38713308/). DOI: `10.1186/s41235-024-00546-w`. **Three primary fake-news reminder experiments; complete PMC body, selected sections checked.** Prior exposure/accessibility changed whether complete or partial reminders better supported correction. Remembering both versions tracked accuracy. News-headline belief and episodic source accuracy are distinct endpoints; no AI/sleep/hypnosis combination.

<a id="k15"></a>
### K15 — Memory consolidation during sleep involves context reinstatement in humans

Eitan Schechtman et al. (2023 Apr 25). [Memory consolidation during sleep involves context reinstatement in humans](https://pubmed.ncbi.nlm.nih.gov/37014750/). DOI: `10.1016/j.celrep.2023.112331`. **Primary sleep-context experiment; complete PMC body, selected sections checked.** N = 29; cued and contextually linked non-cued object memories changed as a function of initial strength. Sigma/context-pattern associations support contextual spread; no new story transmission, false-memory or source-misattribution endpoint was demonstrated.

<a id="k16"></a>
### K16 — Time, not sleep, unbinds contexts from item memory

Roy Cox et al. (2014). [Time, not sleep, unbinds contexts from item memory](https://pubmed.ncbi.nlm.nih.gov/24498441/). DOI: `10.1371/journal.pone.0088307`. **Primary sleep/wake context study; complete PMC body, selected sections checked.** Context-cue benefit declined with elapsed time, without a sleep-specific modulation in the tested comparisons. Context dependence differs from source-memory accuracy; not a failed replication of every sleep/context result.

<a id="k17"></a>
### K17 — Promoting memory consolidation during sleep: A meta-analysis of targeted memory reactivation

Xiaoqing Hu et al. (2020 Mar). [Promoting memory consolidation during sleep: A meta-analysis of targeted memory reactivation](https://pubmed.ncbi.nlm.nih.gov/32027149/). DOI: `10.1037/bul0000223`. **TMR meta-analysis; complete PMC body, selected subgroup sections checked.** The false-memory subgroup comprised four experiments/seven effects with no detectable pooled benefit. It included unpublished dissertation/dataset evidence. The overall retention benefit cannot substitute for this specific endpoint. No independent effect-size recalculation or underlying-study/data audit.

<a id="k18"></a>
### K18 — No evidence for a targeted memory reactivation effect on word-meaning priming

Lewis V Ball et al. (2025 Dec 15). [No evidence for a targeted memory reactivation effect on word-meaning priming](https://pubmed.ncbi.nlm.nih.gov/40885484/). DOI: `10.1016/j.neuropsychologia.2025.109264`. **Primary semantic TMR study; complete abstract checked.** No added word-meaning-priming/context-recall benefit despite cue-related spindle/beta response. Restricted null, not evidence that all TMR or linguistic processing fails.

<a id="k19"></a>
### K19 — Odor-Cued Targeted Reactivation Was Unable to Selectively Benefit Declarative Memories During Sleep

Gautam Narayan et al. (2026 Aug). [Odor-Cued Targeted Reactivation Was Unable to Selectively Benefit Declarative Memories During Sleep](https://pubmed.ncbi.nlm.nih.gov/41656173/). DOI: `10.1111/jsr.70281`. **Primary odor-set TMR study; complete abstract checked.** N = 32; no overall selective cued-set advantage, with encoding-strength-dependent findings. Generalized benefit is a possible explanation, not established by the absence of selectivity. One PMC request failed; no complete-body inspection.

<a id="k20"></a>
### K20 — No effect of odor-induced memory reactivation during REM sleep on declarative memory stability

Maren J Cordi et al. (2014). [No effect of odor-induced memory reactivation during REM sleep on declarative memory stability](https://pubmed.ncbi.nlm.nih.gov/25225474/). DOI: `10.3389/fnsys.2014.00157`. **Primary REM reactivation experiment; complete PMC body, selected sections checked.** N = 16, counterbalanced within-subject study; no added memory stability against interference. Different stage and endpoint from positive NREM context work.

<a id="k21"></a>
### K21 — The effects of hypnosis, context reinstatement, and anxiety on eyewitness memory

D J Ready et al. (1997 Jan). [The effects of hypnosis, context reinstatement, and anxiety on eyewitness memory](https://pubmed.ncbi.nlm.nih.gov/8991296/). DOI: `10.1080/00207149708416106`. **Primary hypnosis/context study; complete abstract checked.** No significant treatment effects on factual memory or suggestion susceptibility; some facial-recognition and susceptibility/anxiety-related outcomes differed. No general accuracy or general susceptibility conclusion.

<a id="k22"></a>
### K22 — The cognitive interview: does it successfully avoid the dangers of forensic hypnosis?

Wayne G Whitehouse et al. (2005). [The cognitive interview: does it successfully avoid the dangers of forensic hypnosis?](https://pubmed.ncbi.nlm.nih.gov/15989121/). **Primary interview comparison; complete abstract checked.** N = 72; hypnosis, cognitive interview and motivated repeated-recall control. Greater spontaneous output under hypnosis did not translate into a condition difference on the forced test. Report criterion/accessibility require separation. PubMed supplied no DOI. Europe PMC subsequently supplied `10.2307/30039056`, independently matched to title, authors and journal in Crossref. This resolves the identifier without implying full-text inspection.

<a id="k23"></a>
### K23 — Enhancing witness memory with techniques derived from hypnotic investigative interviewing: focused meditation, eye-closure, and context reinstatement

Graham F Wagstaff et al. (2011 Apr). [Enhancing witness memory with techniques derived from hypnotic investigative interviewing: focused meditation, eye-closure, and context reinstatement](https://pubmed.ncbi.nlm.nih.gov/21390976/). DOI: `10.1080/00207144.2011.546180`. **Two primary component experiments; complete abstract checked.** Focused meditation/eye closure without a hypnosis label. One child comparison and a separate adult combination with context reinstatement reported benefit/resistance. These are different samples/endpoints, not proof of a special hypnotic-state mechanism or a combined AI/sleep effect.

<a id="k24"></a>
### K24 — "Don't know" responding to answerable and unanswerable questions during misleading and hypnotic interviews

Alan Scoboria et al. (2008 Sep). ["Don't know" responding to answerable and unanswerable questions during misleading and hypnotic interviews](https://pubmed.ncbi.nlm.nih.gov/18808279/). DOI: `10.1037/1076-898X.14.3.255`. **Primary interview/reporting study; complete abstract checked.** Don't-know responses had different meanings, including explicit knowledge that queried information was absent. Their treatment changed accuracy estimates. Not a measure of erased details or a universal interview diagnostic.

<a id="k25"></a>
### K25 — In search of a Goldilocks zone for credible AI

Kevin Allan et al. (2021 Jul 01). [In search of a Goldilocks zone for credible AI](https://pubmed.ncbi.nlm.nih.gov/34211064/). DOI: `10.1038/s41598-021-93109-8`. **Three primary AI/human-source experiments; complete PMC body, selected sections checked.** Partner responses were simulated and attributed to AI/human sources. Conformity depended on source credibility/accuracy and own capability. A controlled source-influence task, not an autonomous generative model, durable autobiographical rewriting or direct contextual mediation.

<a id="k26"></a>
### K26 — Resisting misinformation via discrepancy detection: effects of an unaware suspicion cue

Rona Sheaffer et al. (2022 Jul). [Resisting misinformation via discrepancy detection: effects of an unaware suspicion cue](https://pubmed.ncbi.nlm.nih.gov/33896371/). DOI: `10.1080/09658211.2021.1917618`. **Primary suspicion-context study; complete abstract checked.** Reports resistance with an indirect discrepancy measure. Its pilot assessed the cue/suspicion link; no independent full-effect replication or fresh appraisal of awareness methods was established here. PubMed issue year 2022 differs from the 2021 DOI/online year.

## Interpretation boundary

Which context returns, its timing, and whether a discrepancy is retained can change the direction of the observed effect. Physical/strategy contexts, narrative coherence, neural source-related activity, source decisions, and remembered change are different variables. The selected evidence supports restricted components and competing predictions for AI applications, not a validated AI–sleep–hypnosis mechanism or a general method of replacing personal history.
