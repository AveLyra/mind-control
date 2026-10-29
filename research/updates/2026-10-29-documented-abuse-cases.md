# Documented abuse cases and psychological harm: source checks

Date: October 29, 2026 (America/New_York).

[Home](../../README.md) · [Case synthesis](../../wiki/documented-abuse-and-evidence.md) · [Corrections](../../sources/corrections.md) · [Access audit](../../sources/link-audit.md)

## Scope and method

This follow-up tests the documentary basis of eight previously invented worst-case scenarios involving hypnosis, sleep influence, and manipulation. It does not identify those characters as real patients. Primary records govern case descriptions; laboratory effects are not clinical outcomes. Allegations, firsthand accounts, procedural rulings, causal inferences, and fictional extrapolations remain distinct.

Selected **26 source entries**: six legal-record entries, one expert-witness case report, two retraction-account publications, and 17 other scientific publications including a critique and a correction. The legal entries include related proceedings and documents; this is not a count of independent cohorts or established abuse findings. Eighteen PubMed title/PMID/DOI relationships were checked. Sixteen provided complete abstracts; D16 and D17 have none and received primary-text checks instead.

### Bounded PubMed discovery

All queries used publication-date upper bound `2026/10/29`, relevance ordering, offset 0, and abstract caps of 6,000-7,000 characters. Counts are reported by the connector at retrieval. These were focused discovery searches, not a systematic review.

| Query | Returned / total | Limit |
|---|---:|---|
| `(hypnosis[Title/Abstract] OR hypnotic[Title/Abstract]) AND ("sexual abuse"[Title/Abstract] OR "sexual assault"[Title/Abstract])` | 8 / 63 | Remaining pages not read; sedative-drug results were unrelated. |
| `("psychic driving"[Title/Abstract] OR "depatterning"[Title/Abstract]) AND (Cameron[Title/Abstract] OR follow-up[Title/Abstract] OR patients[Title/Abstract])` | 3 / 3 | Historical syntheses used as leads, not substitutes for records. |
| `Ost[Author] AND (retract*[Title/Abstract] OR recovered[Title/Abstract])` | 8 / 11 | Broad author match returned unrelated material; not exhausted. |
| `"nonbelieved memories"[Title/Abstract] AND (emotion*[Title/Abstract] OR distress[Title/Abstract] OR belief[Title/Abstract])` | 8 / 17 | Remaining pages not read. |
| `"Sleep deprivation does not work"[Title]` | 0 / 0 | Known item recovered by direct PMID; a search miss is not absence. |
| `"Retractors of false memories"[Title]` | 0 / 0 | D08 recovered at its primary publisher. |
| `depatterning[Title/Abstract] OR "psychic driving"[Title/Abstract]` | 7 / 7 | Included unrelated ECT material; historical technique papers not treated as verified efficacy. |
| `Ost J[Author] AND (retract*[Title/Abstract] OR recovered[Title/Abstract])` | 2 / 2 | D09 found through a separate primary university/publisher lookup. |
| `"false autobiographical memories" AND (revers*[Title/Abstract] OR correct*[Title/Abstract])` | 2 / 2 | Missed D21; recovered by the next title query. |
| `"Rich false memories"[Title]` | 5 / 5 | Located original, critique, correction, reversal, and reused-video publication. |

Targeted primary-site discovery located case records, publisher notices, and lawful author/university copies. Some broad web queries returned irrelevant namesakes or legal/technical records. Contemporary news was used to locate the Fine filing, not to substitute a criminal judgment. Burgus-related reports and settlement narratives were screened as leads but not adopted as adjudicated case findings.

### Inspection and access boundaries

- Downloaded the complete public 45-page Fine emergency-motion PDF, four-page resignation order, and 41-page Quebec authorization judgment. Inspected selected relevant text; visually checked the Fine cover and sealed-exhibit placeholders and the Quebec medical-note/allegation pages. Poppler warned about malformed streams in the Fine file, so the inspected page images and extracted text were compared. The sealed client-affidavit contents and underlying recordings were not available or reconstructed.
- Read selected Ramona opinion sections and selected Orlikow background, causation, and limitations discussion from published judicial-text mirrors. The Trochym source is the court registrar's official bulletin: disposition and headnote, including differing judicial positions. Full-reasons routes were blocked or redirected. Historical dispositions are described at their dates; subsequent litigation and current legal rules were not comprehensively checked.
- Retrieved the complete four-page published Frenda PDF from an author's university site and a complete 20-page Oeberst author manuscript from its university repository; inspected methods/results/limitations and the follow-up denominator. The manuscript and indexed final publication are versions of one work. Selected pages of the six-page Wade published-PDF copy were inspected; the primary publisher supplied the correction's table and explanatory text.
- One complete PMC article body, D26, was retrieved through Europe PMC XML (32,766 extracted body characters); selected methods/results/data-reuse sections were inspected. Two D11 full-text connector calls and one D21 call failed internally; direct PMC D11 access challenged, and its/D21's Europe PMC XML routes returned HTTP 500. Those failures are not recast as successful connector retrievals. Author copies supplied the successful alternative checks.
- D03 publisher body returned 403. D08's publisher abstract was available but its article body restricted. D09's university abstract was available, but its linked PDF returned 403 through both web and CLI routes. D10's PubMed/publisher abstract was inspected, without a complete body. D12-D15 and D18-D20/D22-D25 received complete provided abstract/metadata checks, not fresh complete-body reviews. D23-D25 also retain the earlier, separately scoped technique review.
- No participant-level data, analysis code, effect size, or clinical diagnosis was independently reproduced. No full-case merits trial, missing affidavit, full recording, or whole archive was reconstructed.

## Source entries

<a id="d01"></a>
### D01 — Lorain County Bar Association v. Michael W. Fine: emergency motion and public exhibits

Lorain County Bar Association, Ohio Supreme Court case 2014-2005 (November 2014). [Public filed copy](https://mediaassets.news5cleveland.com/uploads/michal-fine-filing.pdf). **Filing and sworn investigator account, not a merits judgment.** Selected motion text and the public investigator affidavit (PDF pp. 39-40) describe recordings and a monitored encounter. PDF p. 37 labels the first client affidavit sealed; its text is absent. Public allegations cannot be counted as independently read client affidavits, verified complete videos, or quantified long-term effects. The referenced psychologist's opinion is not a controlled mechanism test.

<a id="d02"></a>
### D02 — In re Resignation of Fine, 143 Ohio St.3d 1287, 2015-Ohio-3265

Ohio Supreme Court, August 17, 2015, case 2015-1084. [Official order](https://www.supremecourt.ohio.gov/rod/docs/pdf/0/2015/2015-Ohio-3265.pdf). **Actual licensing disposition.** Paragraphs 1-3 accept resignation with disciplinary action pending and withdraw practice privileges. The disciplinary report is described as sealed. This order is not a criminal conviction or a finding that every allegation in D01 was proved. Complete public PDF obtained; selected controlling paragraphs inspected. The direct web route timed out before successful CLI retrieval.

<a id="d03"></a>
### D03 — Sexual abuse and the abuse of hypnosis in the therapeutic relationship

E Hoencamp (1990 Oct). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/2258245/). DOI: `10.1080/00207149008414528`. **Expert-witness case report; complete provided abstract.** The author reports involvement in a Dutch case with nine alleged victims and discusses therapeutic authority and subjective nonvolition. Judicial outcome and standardized long-term diagnoses are absent from the inspected abstract. Publisher body returned 403; the contemporary legal description is not used as current legal guidance.

<a id="d04"></a>
### D04 — Ramona v. Superior Court (Ramona), 57 Cal.App.4th 107

California Court of Appeal, August 19, 1997, B111565. [Published opinion](https://law.justia.com/cases/california/court-of-appeal/4th/57/107.html). **Evidentiary ruling with recorded family/employment consequences.** The court describes uncertainty before a sodium-amytal interview, later assurances/certainty, divorce and job loss, then excludes the challenged testimony. Selected factual and holding sections inspected. Drug-assisted memory recovery is distinct from hypnotic induction and sleep cueing. Exclusion does not independently prove every allegation false; opposing expert positions and the procedural burden remain relevant.

<a id="d05"></a>
### D05 — Orlikow v. United States, 682 F.Supp. 77

U.S. District Court for the District of Columbia, January 19, 1988, 80-3163. [Published judicial text](https://law.counselstack.com/opinion/orlikow-v-united-states-dcd-1988). **Summary-judgment opinion, not a completed clinical or merits adjudication.** Selected background and causation/limitations sections inspected. CIA funding and exposure to components are recorded; the treatment's character and injury causation remain disputed. The opinion expressly distinguishes real concealed funding from unresolved causal questions. It does not isolate sleep, hypnosis, repeated verbal material, drugs, or electroconvulsive treatment as a sufficient cause.

<a id="d06"></a>
### D06 — Tanny, Ponting and Edwards Roberge v. Royal Victoria Hospital and others: class-action authorization

Quebec Superior Court, Dominique Poulin J.S.C., July 31, 2025, 500-06-000972-196. [Complete judgment](https://clg.org/pdf/9/1/0/2/Judgment-Granting-Authorization.pdf). **Authorization, not final liability.** Selected paragraphs 119-141/PDF pp. 24-26 distinguish medical-note material, family allegations, and the threshold for proceeding. Tanny's alleged confusion, later detachment and family harm, and Ponting's alleged nightmares/functional loss concern mixed historical treatments. They do not establish successful personality programming or a pink-noise mechanism. Related historical proceedings are not independent experimental replications.

<a id="d07"></a>
### D07 — R. v. Trochym, 2007 SCC 6: official disposition and headnote

Supreme Court of Canada, February 1, 2007; registrar's bulletin dated February 2. [Official bulletin](https://decisions.scc-csc.ca/scc-csc/bulletins/en/2480/1/document.do), printed pp. 137 and 143-145 (PDF pp. 42 and 48-50). **Official procedural report/headnote, not a retrieved full opinion or certified court record.** Selected sections record the changed sighting day after hypnosis, withheld background from jurors, conviction set aside and new trial. Other evidentiary issues also mattered. Concurrence/dissent caution against indiscriminate exclusion. No factual-innocence finding or deliberate fabrication is inferred.

<a id="d08"></a>
### D08 — Retractors of false memories: The evolution of pseudo-memories

Harold I. Lief and Janet Fetkewicz (September 1995), The Journal of Psychiatry & Law 23(3):411-435. [Primary publisher abstract](https://journals.sagepub.com/doi/10.1177/009318539502300305). DOI: `10.1177/009318539502300305`. **Selected retrospective accounts.** Forty responses from 100 approached after FMSF telephone contact. Accounts concern memory beliefs, perceived therapy worsening, and family reconciliation. The available abstract supports those reporting themes, not independently verified event falsity, clinical prevalence, a specific induced disorder, or a causal effect of hypnosis in every respondent. Body restricted.

<a id="d09"></a>
### D09 — False confessions and false memories: a model for understanding retractors' experiences

James Ost, Alan Costall and Ray Bull (2001), The Journal of Forensic Psychiatry 12(3):549-579. [Primary university record/abstract](https://researchportal.port.ac.uk/en/publications/false-confessions-and-false-memories-a-model-for-understanding-re/). DOI: `10.1080/09585180127393`. **Qualitative/model comparison.** Accounts were analyzed for similarities with false-confession contexts; the authors acknowledge reliability/generalization concerns. Abstract inspected; linked university PDF returned 403. No uninspected individual history or sample-detail claim is supplied. The repository identifies 2001 publication despite a later publisher online-posting date.

<a id="d10"></a>
### D10 — Sleep deprivation does not work: Epidemiology, impacts and outcomes of incidental and systematic sleep deprivation in a sample of Palestinian detainees

Mahmud Sehwail, Pau Pérez-Sales, Khader Rasras et al. (2019). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/31670704/). DOI: `10.7146/torture.v29i2.115381`. **Retrospective survivor study; complete provided abstract and publisher abstract.** N=600 former detainees. Sleep-deprivation categories were associated with acute/chronic suffering and some longer-term family/social/physical impacts. Selection, recall, and co-occurring detention exposures limit causal isolation. Increased signed statements did not correspond to significantly greater conviction rates or sentences in this sample. Sleep deprivation is distinct from sleep conditioning. No complete body inspected.

<a id="d11"></a>
### D11 — Sleep deprivation and false confessions

Steven J Frenda, Shari R Berkowitz, Elizabeth F Loftus et al. (2016 Feb 23). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/26858426/). DOI: `10.1073/pnas.1521518113`. **Quasi-random laboratory comparison; published author copy inspected.** N=88, 44 per condition. Initial false admissions: 22/44 deprived versus 8/44 rested; OR=4.5, 95% CI 1.7-11.8. Methods explicitly say quasi-random assignment. Admissions lacked detailed post-admission narratives; true-confession effects and enduring injury were not established. [Author's published PDF](https://bpb-us-e2.wpmucdn.com/faculty.sites.uci.edu/dist/c/571/files/2024/07/Frenda_SleepFalseConfess_PNAS2016.pdf), selected pp. 2-4. Connector/XML routes failed; PDF alternative succeeded.

<a id="d12"></a>
### D12 — Hypnotically created memory among highly hypnotizable subjects

J R Laurence, C Perry (1983 Nov 04). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/6623094/). DOI: `10.1126/science.6623094`. **Selected-sample experiment; complete provided abstract.** Thirteen of 27 highly hypnotizable participants later accepted a suggested waking-at-night event. No population susceptibility rate, complex traumatic biography, lifelong guilt, or long-term functional disability follows from that endpoint.

<a id="d13"></a>
### D13 — Hypnosis and pseudomemories: the effects of prehypnotic expectancies

S J Lynn, M Milano, J R Weekes (1991 Feb). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/2016672/). DOI: `10.1037//0022-3514.60.2.318`. **Contrary experiment; complete provided abstract.** None of 47 subjects exhibited pseudomemory at the final recall trial. Procedure and expectancy manipulations differ from D12, so it is not represented as a definitive exact replication. Supports heterogeneity rather than guaranteed creation or permanent retention.

<a id="d14"></a>
### D14 — Reports of real and false memories: the relevance of hypnosis, hypnotizability, and context of memory test

A J Barnier, K M McConkey (1992 Aug). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/1500609/). DOI: `10.1037//0021-843x.101.3.521`. **Induction versus individual responsiveness; complete provided abstract.** Thirty high- and 30 low-hypnotizable participants. Hypnotizability, rather than hypnosis itself, was associated with false reports, and test context mattered. This constrains a uniquely hypnotic-power interpretation. No lasting abuse outcome measured in the inspected abstract.

<a id="d15"></a>
### D15 — Constructing rich false memories of committing crime

Julia Shaw, Stephen Porter (2015 Mar). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/25589599/). DOI: `10.1177/0956797614562862`. **Crime-memory induction report; complete provided abstract.** The original authors classified 70% of crime-condition participants as false memories. Interpret with D16's same-data recoding and D17's calculation corrections. Reports of remembering a crime are not a measurement of enduring guilt, actual criminal acts, or hypnosis/sleep-induced compliance.

<a id="d16"></a>
### D16 — Deconstructing Rich False Memories of Committing Crime: Commentary on Shaw and Porter (2015)

Kimberley A Wade, Maryanne Garry, Kathy Pezdek (2018 Mar). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29315022/). DOI: `10.1177/0956797617703667`. **Reanalysis plus new observer judgments; selected published-PDF sections inspected.** Two established recoding approaches placed apparent crime false memories around 26%-30%, versus the original 70% classification. New lay judgments evaluated reports rather than replicating the induction. [University-hosted published PDF](https://studieinfo.liu.se/download/coursedocument/6bfc54b6-00ec-4a0b-a275-bed9843e12d6/Wade%202018%20Deconstructing%20Rich%20False%20Memories%20of%20Committing%20Crime%20Commentary%20on%20Shaw%20and%20Porter%20%282015%29.pdf), pp. 2-4. The PubMed record has no abstract. No underlying transcripts were independently recoded here.

<a id="d17"></a>
### D17 — Corrigendum: Constructing Rich False Memories of Committing Crime

Publisher correction (2018 Apr). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29529385/). DOI: `10.1177/0956797618762341`. **Correction, not a retraction or replication.** Complete substantive [publisher notice and table](https://journals.sagepub.com/doi/10.1177/0956797618762341) inspected. Repairs incorrect cells, detail means, confidence intervals and other calculations; a perspective comparison becomes nonsignificant. The note does not replace the original headline rate with D16's recoding estimate. PubMed has no abstract. Original statistics were not independently recalculated.

<a id="d18"></a>
### D18 — Nonbelieved memories

Giuliana Mazzoni, Alan Scoboria, Lucy Harvey (2010 Sep). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/20689053/). DOI: `10.1177/0956797610379865`. **Survey; complete provided abstract.** About 20% of the initial sample reported at least one nonbelieved autobiographical memory, sharing recollective features with believed memories and more negative emotions. Self-report and population/sample limits remain; no induced chronic disorder or prognosis was established.

<a id="d19"></a>
### D19 — Experimentally evoking nonbelieved memories for childhood events

Henry Otgaar, Alan Scoboria, Tom Smeets (2013 May). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/22905934/). DOI: `10.1037/a0029668`. **Experimental childhood-event reports; complete provided abstract.** Some adults and children retained a recollective experience after disbelieving the suggested event; others retracted. One-month phenomenological persistence does not establish persistent distress or a lifelong false belief. The PubMed issue date is 2013, despite the 2012 DOI/early-publication context.

<a id="d20"></a>
### D20 — Inducing emotionally negative nonbelieved memories using negative pictures

Chunlin Li, Henry Otgaar, Peter Muris et al. (2024 Jan). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/37432570/). DOI: `10.3758/s13421-023-01441-3`. **Two negative-picture experiments; complete provided abstract.** N=35 and N=43. Challenges reduced belief more than recollection, including for true events; no notable changes in emotional state occurred. This directly limits the leap from a nonbelieved negative recollection to psychologically devastating injury. Journal issue date is January 2024.

<a id="d21"></a>
### D21 — Rich false memories of autobiographical events can be reversed

Aileen Oeberst, Merle Madita Wachendörfer, Roland Imhoff et al. (2021 Mar 30). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/33753514/). DOI: `10.1073/pnas.2026447118`. **Reversal/follow-up; author manuscript methods/results inspected.** Final N=52; 38 returned roughly one year later. False reports fell after sensitization/debriefing, with low residual endorsement at follow-up. [Complete author manuscript](https://pure.port.ac.uk/ws/portalfiles/portal/26903394/Oeberst_et_al._PNAS_REVsubmission_final.pdf), selected pp. 5-10. True-event comparisons do not supply an untreated reversal-control arm; component effects and attrition require care. No guarantee of recovery from severe real-world abuse. Same work as the indexed final article.

<a id="d22"></a>
### D22 — Trained but still tricked: source sensitisation training fails to reduce false memory reports

Charlotte A Bücken, Paul Riesthuis, Giorgia Caon et al. (2026 Jan). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/41242760/). DOI: `10.1080/09658211.2025.2585095`. **Different training intervention, null protection; complete provided abstract.** N=294 initially; the abstract reports 276 in the later comparison. Training did not reduce false reports. Different task and intervention from D21, so neither an exact failed replication nor proof that all correction fails. PubMed issue date January 2026; the DOI contains the earlier online-publication year.

<a id="d23"></a>
### D23 — Post-hypnotic suggestion improves confidence and speed of memory access with long-lasting effects

Barbara Schmidt, Justin Böhmer, Martin Schnuerch et al. (2024 May). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/38569321/). DOI: `10.1016/j.actpsy.2024.104240`. **Posthypnotic confidence; complete provided abstract.** N=24 highly suggestible participants, with one-week transfer to new material. Recognition confidence/speed improved without accuracy improvement. Does not measure trauma, consent, or reliable memory verification. Same source as the separately scoped earlier technique review.

<a id="d24"></a>
### D24 — Exposure to extinction-associated contextual tone during slow-wave sleep and wakefulness differentially modulates fear expression

Si-Zhi Ai, Jie Chen, Jian-Feng Liu et al. (2015 Sep). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/26071676/). DOI: `10.1016/j.nlm.2015.06.005`. **Learned pink-noise context; complete provided abstract.** Sleep re-exposure and waking re-exposure had different effects on laboratory fear expression; sleep profiles were unchanged. No durable phobia, chosen attachment, or complex behavioral control established. Retains the earlier review's limited body access; unassociated background pink noise is a distinct exposure.

<a id="d25"></a>
### D25 — Efficacy of pink noise and earplugs for mitigating the effects of intermittent environmental noise exposure on sleep

Mathias Basner, Michael G Smith, Makayla Cordoza et al. (2026 May 12). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/41627391/). DOI: `10.1093/sleep/zsag001`. **Sleep-physiology trial; complete provided abstract plus retained earlier scoped body inspection.** N=25. Pink-noise conditions reduced REM and worsened some subjective outcomes, with no measured morning cognitive effect. No demonstrated permanent injury, memory implantation or behavioral programming. The companion source-specific-arousal report in the earlier review is the same registered trial, not replication.

<a id="d26"></a>
### D26 — Do False Memories Look Real? Evidence That People Struggle to Identify Rich False Memories of Committing Crime and Other Emotional Events

Julia Shaw (2020). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/32322232/). DOI: `10.3389/fpsyg.2020.00650`. **New observer samples using older induction footage; complete Europe PMC XML body, selected sections inspected.** Reported N=124 and N=82. Classification performance does not establish a general demeanor/consent test; D15's disputed induction categories remain relevant. Study 2's methods list 61 women, 21 men and one other despite N=82: this unresolved accounting discrepancy is retained. Observer experiments are not independent replications of memory induction.

## Interpretation checks

The strongest documented parallels concern violated professional trust, disputed memory recovery, impaired evidence, and alleged or reported harm from mixed coercive exposures. They do not jointly establish one reproducible hypnosis/sleep-control system. Disbelief and recollection, admissions and internalized guilt, sleep loss and sleep learning, and licensing/authorization decisions and merits findings remain separate.

The eight-row [scenario crosswalk](../../wiki/documented-abuse-and-evidence.md#scenario-crosswalk) identifies the exact fictional extensions. Future evidence that would strengthen claims includes corroborated individual exposure, independent comparison samples, specified behavioral outcomes against resistance, after-exposure follow-up, and validated measures of clinical and social harm. No participant intervention, experiment, new simulation, or canon promotion was performed.
