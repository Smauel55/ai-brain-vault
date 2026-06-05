---
created: 2026-06-05
updated: 2026-06-05
tags: [project, caught-up-ai, writing, research-report, prose-engine, ap-lang, anti-ai-tell]
project: "[[Caught Up AI]]"
---

# Prose Engine Research Report

The top-level, auditable record of the research that produced the full AI-generation prose engine for [[Caught Up AI]]. It ties together every deliverable: the corpus it is built on, the register palette, the three research layers, the verification logs, the proxy pilot, and the day-to-day operating instructions. Read this first; follow the wiki-links into the specs when you need detail.

Companion documents: [[Style-Palette]], [[Register-Specs]], [[Structural-Templates]], [[Annotated-Exemplars]], [[Anti-Tell-List]], [[Cross-Piece-Sameness-Rubric]], [[Generation-Briefs]], [[Blind-Test-Protocol]]. Upstream context: [[Writing-Manual]] (the v1 manual this supersedes), [[Content-Sourcing]] (where facts come from), [[Accuracy-Guardrail]] (the separate, non-negotiable fact-checking gate), [[Caught Up AI]] (the product).

## 1. Executive summary and how this supersedes v1

- The product writes short original current-events catch-up pieces, 350 to 600 words, by full AI generation. The model reads sources for FACTS ONLY (facts are not copyrightable) and writes entirely original prose. It does not reproduce, summarize, or paraphrase source prose. This sidesteps the licensing wall documented in [[Licensing-Verification.md]] and shifts the risk onto two things: factual accuracy (handled separately, see section 8 and [[Accuracy-Guardrail]]) and AI-sameness (the whole subject of this report).
- The quality target is craft, not topic. The pieces must read with the register and rhetorical architecture of the PROFESSIONAL nonfiction source passages the College Board selects for the AP English Language exam (the Q2 rhetorical-analysis passages and the Q1 synthesis documents), not student essays. There is no single AP Lang voice. The target is a PALETTE of distinct professional registers spanning the 18th to 21st century.
- Two failure modes drive the entire design: (1) the per-piece AI tell (one piece reads machine-made), and (2) cross-piece sameness (a batch reads like one voice with the topic swapped out). Deliberate, controlled variety across registers is the primary defense against the second, and per-register craft bands plus a mechanical blocklist are the defense against the first.

How this supersedes the v1 [[Writing-Manual]]:

- v1 was a single house voice. It reverse-engineered one composite "AP Lang argument" register, one three-part spine (open, build, close), and one blocklist. It was correct as far as it went, but a single voice applied across a weekly batch is itself the cross-piece tell. v1 had no answer to failure mode (2).
- v2 (this engine) replaces the single voice with a SEVEN-REGISTER PALETTE. Each register has its own power-relation, its own sentence-rhythm signature, and its own closing move. The week's batch rotates registers so no two pieces share a skeleton. See [[Style-Palette]].
- v2 grounds every register in measurable bands recomputed from real exemplars rather than in intuition, and tags each register by confidence (VERIFIED, MEASURED-NOT-RE-VERIFIED, PROVISIONAL ANCHOR). See [[Register-Specs]].
- v2 updates the blocklist from the burned 2023-2024 vocabulary ("delve", "tapestry") to the live 2025-2026 signature (significance-inflation and copula-avoidance), and adds a batch-level rubric v1 never had. See [[Anti-Tell-List]] and [[Cross-Piece-Sameness-Rubric]].
- What v1 got right and v2 keeps: facts-only sourcing, the markability principle, the hard personal rules (no em-dashes, no emojis), and the insistence that current-events accuracy is a separate gate from style. v1 is retained as the readable on-ramp and historical record; v2 is the operating standard.

## 2. Methodology

The engine was built by a multi-agent research process designed to be adversarial against its own conclusions, not just productive.

- Fan-out research. Separate agents worked the three research layers in parallel (craft, stylometry, detectability) plus a provenance layer for the corpus. Each produced its own findings against its own sources.
- Adversarial verification. Every load-bearing claim was handed to a verification pass whose job was to disprove it, not confirm it. Provenance claims (which exam year, which author, which form) were re-checked against official College Board PDFs and primary archives. Stylometry claims were RECOMPUTED from public-domain full texts with an independent script. Empirical tell claims were re-checked against their cited papers and vendor pages. The results are logged claim-by-claim in section 6.
- Quarantine over deletion. Where a claim could not be independently re-verified (a blocked source, a non-parsing scanned PDF, a paywalled exemplar), it was QUARANTINED and labeled rather than dropped or asserted. The engine is built on what survived; the quarantined items are disclosed so a reader can see exactly what rests on softer ground.
- Blind-test PROXY. Because the real gold standard (human AP Lang teachers who cannot tell which is which) was not yet runnable, a proxy stood in: an independent judge read matched pairs of a generated register-piece against a genuine professional passage in the same register, blind to which was which, and guessed the machine. This is a pre-screen, not the verdict. See section 7 and [[Blind-Test-Protocol]].
- Separation of concerns. Style tuning never touches factual correctness. Accuracy is verified on its own track ([[Accuracy-Guardrail]]); nothing in this report bends a fact to fit a register.

## 3. Corpus manifest

The corpus is the set of real AP English Language source passages the engine emulates for craft. Provenance status: "exam-confirmed" means the year, author, and form were verified against official College Board materials or primary archives; "adjacent" means the prompt is confirmed but the per-source attribution could not be lifted (usually a scanned, non-parsing PDF). Public-domain status governs only whether a verbatim excerpt may be quoted for study; it never affects the product, which reproduces no source prose.

### Q2 rhetorical-analysis passages

| Year | Author | Title | Form | Era | Public domain | Provenance |
|---|---|---|---|---|---|---|
| 1791 | Benjamin Banneker | Letter to Thomas Jefferson | letter | pre-1900 | yes | exam-confirmed (2010 Q2) |
| 1780 | Abigail Adams | Letter to John Quincy Adams | letter | pre-1900 | yes | exam-confirmed (2014 Q2) |
| 1827 | William Hazlitt | On the Want of Money | essay | pre-1900 | yes | exam-confirmed (2006 Q2) |
| 1905 | Florence Kelley | NAWSA child-labor speech | speech | 1900-1950 | yes | exam-confirmed (2011 Q2) |
| 1962 | John F. Kennedy | Steel-price opening statement | public statement | 1950-2000 | yes | exam-confirmed (2012 Q2) |
| 1930 | Mohandas K. Gandhi | Letter to Lord Irwin | open letter | 1900-1950 | likely (URAA open) | exam-confirmed (2019 Q2); excerpt withheld |
| 1960 | Clare Boothe Luce | Women's National Press Club address | speech | 1950-2000 | no | exam-confirmed (2017 Q2) |
| 1978 | Cesar Chavez | Article on nonviolence | magazine article | 1950-2000 | no | exam-confirmed (2015 Q2) |
| 1993 | Scott Russell Sanders | Staying Put | essay | 1950-2000 | no | exam-confirmed (2007 Q2) |
| 2004 | John M. Barry | The Great Influenza | narrative nonfiction | post-2000 | no | exam-confirmed (2008 Q2, not 2020) |
| 2005 | Richard Louv | Last Child in the Woods | argumentative nonfiction | post-2000 | no | exam-confirmed (2013 Q2, not 2012) |
| 2018 | Reshma Saujani | Essay in American Like Me | memoir essay | post-2000 | no | exam-confirmed (2024 Q2 Set 1) |
| 2004 | Margaret Thatcher | Eulogy for Reagan | eulogy | post-2000 | no | exam-confirmed (2016 Q2) |
| 1997 | Madeleine Albright | Mount Holyoke commencement | commencement | 1950-2000 | no | exam-confirmed (2018 Q2) |
| 2013 | Barack Obama | Rosa Parks statue dedication | speech | post-2000 | yes (17 USC 105) | exam-confirmed (2021 Q2) |
| 2005 | The Onion | MagnaSoles mock press release | satirical mock release | post-2000 | no | exam-confirmed (2005 Q2) |
| 2005 | John M. Barry | Rising Tide | narrative nonfiction | 1950-2000 | no | exam-confirmed (2005 Form B Q2); book first pub. 1997 |
| 2006 | George Bernard Shaw | Saint Joan (trial scene) | drama | 1900-1950 | yes | exam-confirmed (2006 Form B Q2) |
| 2008 | Leonid Fridman | America Needs Its Nerds | op-ed | 1950-2000 | no | exam-confirmed (2008 Form B Q2); orig. NYT 1990 |
| 2009 | Edward O. Wilson | The Future of Life (paired satire) | nonfiction with satire | post-2000 | no | exam-confirmed (2009 Form A Q2) |
| 1939 | Walter Lippmann | The Indispensable Opposition | essay / magazine article | 1900-1950 | no | exam-confirmed (2009 Form B Q2); orig. Atlantic 1939 |
| 1964 | Claudia "Lady Bird" Johnson | Tribute to Eleanor Roosevelt | eulogistic tribute | 1950-2000 | unknown | exam-confirmed (2020 operational Q2) |
| 2001 | Sonia Sotomayor | A Latina Judge's Voice | lecture / essay | post-2000 | no | exam-confirmed (2022 Q2) |
| 2016 | Rita Dove | UVA commencement address | commencement | post-2000 | no | exam-confirmed (2023 Q2 Set 2) |

Note on the "Year" column for several entries: it records the EXAM year where the underlying work predates the exam (Rising Tide book 1997, Fridman op-ed 1990, Lippmann 1939, Saint Joan 1923/24). All disclosed in the provenance log.

### Q1 synthesis source documents

| Year | Author | Prompt / source | Form | Era | Public domain | Provenance |
|---|---|---|---|---|---|---|
| 2006 | Jennifer Maiser | 2011 Locavore, Source A | advocacy web article | post-2000 | no | exam-confirmed |
| 2007 | James E. McWilliams | 2011 Locavore, Source C | skeptical op-ed | post-2000 | no | exam-confirmed |
| 2008 | Pallavi Gogoi | 2011 Locavore, Source E | business-news article | post-2000 | no | exam-confirmed |
| 2011 | U.S. GAO | 2012 USPS, Source A | agency oversight report | post-2000 | yes | exam-confirmed (prompt); GAO=A via search only |
| c.2009-11 | editorial board | 2012 USPS, editorial slot | newspaper editorial | post-2000 | no | adjacent (scanned PDF; attribution unverified) |
| 2009 | Kirk Savage | 2013 Memorialization, Source A | scholarly book excerpt | post-2000 | no | exam-confirmed |
| c.2007 | Lawrence Downes | 2013 Memorialization, Source C | NYT opinion column | post-2000 | no | exam-confirmed |
| 2000 | Maya Lin | 2013 Memorialization, Source G | practitioner statement | post-2000 | no | exam-confirmed |
| 2005 | McCabe and Pavela | 2015 Honor Code, Source F | higher-ed policy article | post-2000 | no | exam-confirmed (date refined to 2005) |
| c.2012 | Dirmeyer and Cartwright | 2015 Honor Code, Source C | economists' op-ed | post-2000 | no | exam-confirmed |
| c.2015 | U.S. DOJ | 2018 Eminent Domain, Source A | agency web explainer | post-2000 | yes | exam-confirmed |
| c.2015 | Ilya Somin | 2018 Eminent Domain, Source C | legal-academic op-ed | post-2000 | no | exam-confirmed |
| 2014 | Troy A. Rule | 2019 Wind Power, Source B | scholarly book excerpt | post-2000 | no | exam-confirmed (slot soft) |
| 2014 | Rani Molla | 2019 Wind Power | WSJ data journalism | post-2000 | no | exam-confirmed (slot soft) |
| 2016 | Anne Trubek | 2021 Handwriting, Source C | NYT opinion column | post-2000 | no | exam-confirmed |
| c.2012 | David Kysilko | 2021 Handwriting, Source D | NASBE policy report | post-2000 | no | exam-confirmed |
| c.2020 | National Park Service | 2024 Historic Preservation Set 1, Source A | agency web text | post-2000 | yes | exam-confirmed |
| c.2020 | Binyamin Appelbaum | 2024 Historic Preservation Set 1, Source C | NYT-style op-ed | post-2000 | no | exam-confirmed |
| 2016 | Jepson and Schepers | 2023 Urban Rewilding Set 1, Source B | NGO policy brief | post-2000 | no | exam-confirmed |
| 1975 | Jeffrey Schrank | 2007 Advertising, Source E | book excerpt | 1950-2000 | no | exam-confirmed |
| 2003 | Shaw and Alan | 2007 Advertising, Source B | encyclopedia entry | post-2000 | no | exam-confirmed |
| 2005 | David Prerau | 2010 Form B Daylight Saving | popular-history book | post-2000 | no | exam-confirmed (prompt); per-source partial |
| 1975 | U.S. DOT | 2010 Form B Daylight Saving | government study findings | 1950-2000 | likely | adjacent (standalone attribution unclear) |
| 2008 | multiple | 2008 Penny Elimination | mixed policy/opinion roster | post-2000 | no | adjacent (prompt confirmed; roster unverified) |
| 2022 | multiple | 2022 STEM Education | mixed report/op-ed roster | post-2000 | no | adjacent (prompt confirmed; roster unverified) |

## 4. The register palette in brief

Seven registers, each a distinct professional voice. One register per piece, rotated across the batch. Full identities, lineages, exemplars, and signature craft live in [[Style-Palette]]; the measurable bands and drift cues live in [[Register-Specs]].

- The Ledger (anchor, default workhorse): impersonal, evidence-forward; authority is the documented record, not a speaking self. Lays out and lightly weighs facts.
- The Open Letter: one voice addressing one more-powerful party, surface deference over moral pressure, the public invited to overhear.
- The Reckoning: a speaker with moral standing pressing a gathered audience toward feeling and action, turning a shared principle into an accusation the reader cannot dodge.
- The Tribute: a dignified voice consecrating a person or moment; the speaker recedes behind the honored subject.
- The Long Think: a writer thinking aloud to a peer-reader, exploratory and unhurried, granting the other side real ground before turning. Annexes controlled satire as a tonal mode.
- The Witness Stand: a contemporary first-person voice building authority from lived experience offered up, with self-aware warmth.
- The Long Look: an absorbed observer rendering a phenomenon with precision and awe, so the prose enacts the complexity it admires rather than arguing.

Why seven beats both failure modes: each register carries its own sentence-length distribution and cadence, so committing fully to one per piece defeats the per-piece tell, and the seven span six different power-relations and five different rhythmic skeletons, so rotating them forces structurally different pieces rather than synonym swaps across a batch.

## 5. The three research layers

The engine rests on three layers of research, each with its own verification and its own deliverable.

- Layer A, CRAFT (qualitative). What each register actually does: power-relation, rhetorical architecture, signature moves, opening and closing logic, how it braids ethos, pathos, and logos. Sourced from close reading of the corpus passages. This is the qualitative half of every register sheet in [[Register-Specs]] and the worked examples in [[Annotated-Exemplars]]; the skeletons are in [[Structural-Templates]].
- Layer B, STYLOMETRY (quantitative). The measurable fingerprint of each register: sentence-length mean and variance (burstiness), sentence-type mix, opener variety, punctuation-per-100-words, type-token ratio, readability grade. Computed from exemplar texts and turned into BANDS, never single targets, each carrying a plain "you have drifted if..." cue for a no-code operator. These are the quantitative half of [[Register-Specs]]. Four of seven registers were recomputed from public-domain full text and reproduced within rounding; see the stylometry verification in section 6.
- Layer C, DETECTABILITY (what to avoid). The empirical anti-AI-tell research: which features make text read machine-made to detectors and to human judges, and which surface tells are reputationally toxic regardless of statistical weight. The headline findings: burstiness (sentence-length variance) is the single most-cited statistical discriminator, perplexity is what most detectors actually measure, and a small set of surface tells (em-dashes, the burned AI lexicon, significance-inflation, copula-avoidance) carry outsized human-facing weight. This is the basis for the per-piece blocklist in [[Anti-Tell-List]] and the batch-level rubric in [[Cross-Piece-Sameness-Rubric]]. Layer C also enumerates the cross-piece sameness signals (opening-gambit clustering, identical skeleton, convergent rhythm, pet-phrase tics, same-close clustering, register flattening) that the rubric exists to catch.

## 6. Claims and verification log

Every load-bearing claim was adversarially re-checked. Status values: VERIFIED (independently confirmed), CORRECTED (a real error found and fixed), PARTIALLY-VERIFIED (confirmed in part, with a documented gap), QUARANTINED (could not be independently verified; flagged, not relied on as measured).

### Provenance

| Claim | Verified by / how | Source | Status |
|---|---|---|---|
| All exam-year and author attributions in the Q2 corpus | Re-checked each against official College Board PDFs and primary archives | CB scoring guidelines and FRQ packets; Founders Online; primary transcriptions | VERIFIED (zero false exam-confirmations found) |
| The Great Influenza is the 2008 Q2 (not the widespread "2020") | Checked against the 2008 CB scoring guidelines; 2020 Q2 separately confirmed as Lady Bird Johnson | CB ap08 and ap20 materials | CORRECTED-and-VERIFIED |
| Last Child in the Woods is the 2013 Q2 (not 2012) | Multiple study reproductions; topic match | CB 2013 materials | CORRECTED-and-VERIFIED |
| Saujani / American Like Me is the 2024 Q2 Set 1 (not a memoir or TED talk) | Direct text extraction of the 2024 scoring guidelines; earlier hallucinated attribution disavowed | CB ap24 Set 1 | CORRECTED-and-VERIFIED |
| Rita Dove UVA address is the 2023 Q2 Set 2 (resolves a set ambiguity) | Official 2023 Set 2 sample responses | CB ap23 Set 2 | VERIFIED |
| 2015 Honor Code Source F (McCabe and Pavela) dated to 2005, not "c.2004" | Citation recovered | Inside Higher Ed, 11 Mar 2005 | CORRECTED |
| Gandhi letter US public-domain status: likely, not certain (URAA live question) | India PD 2009 (life+60); still copyrighted in India on the 1996 URAA date | Wikisource PD rationale; URAA analysis | VERIFIED-as-hedged (excerpt withheld) |
| 2012 USPS GAO = Source A at the citation level | Could not lift the citation line; the CB PDF is a non-parsing scanned image | CB ap12 (scanned) | QUARANTINED (GAO is a plausible lead source; editorial slot stays adjacent) |
| 2010 Form B Daylight Saving DOT-study slot; 2008 Penny and 2022 STEM per-source rosters | Prompts confirmed as released; per-source attributions could not be extracted | CB scanned PDFs | QUARANTINED (prompt-level only, honestly labeled) |

### Stylometry

| Claim | Verified by / how | Source | Status |
|---|---|---|---|
| The Reckoning bands (Kelley + JFK) | Recomputed from PD full text with an independent Python script | speeches-usa.com; presidency.ucsb.edu | VERIFIED (within rounding; "while we sleep" x3, "when we" x3 runway confirmed) |
| The Tribute bands (Obama Rosa Parks) | Recomputed from PD full text | obamawhitehouse.archives.gov | VERIFIED (and validated the em-dash to comma substitution method) |
| The Open Letter bands (Banneker) | Recomputed from PD full text | encyclopediavirginia.org / Founders Online | PARTIALLY-VERIFIED (word count, TTR, compound-complex dominance, semicolon density confirmed; mean and SD splitter-dependent, same conclusion) |
| The Ledger primary anchor (GAO-11-282) | gao.gov returned Akamai 403; WebFetch refused verbatim text | GAO-11-282 | QUARANTINED (raw numbers not citable as measured; bands stand as moderated synthesis; public-facing Obama pole confirmed) |
| The Long Think, Witness Stand, Long Look bands | Rest on copyrighted, paywalled exemplars (Sanders, Lippmann, Dove, Barry) | manifest descriptions | MEASURED-NOT-RE-VERIFIED (qualitative-only, self-flagged) |

### Empirical tells (Layer C)

| Claim | Verified by / how | Source | Status |
|---|---|---|---|
| Five Pangram AI-phrase frequency multipliers | All five matched exactly on fetch | Pangram Labs blog | VERIFIED |
| "delve" spiked after late 2023 then dropped as writers stripped it | Confirmed | Liang et al., Nature Human Behaviour 2025 / arXiv 2502.09606 | VERIFIED |
| Wikipedia "Signs of AI writing" tells (copula-avoidance, participle significance tails, formulaic close) | All three confirmed in the live text | Wikipedia | VERIFIED |
| arXiv 2506.21817 supports the moreover/furthermore connective ban and uniform-sentence tell | The paper is about semantic clusters of spiking CONTENT words, not connectives or sentence length | arXiv 2506.21817 | CORRECTED (citation misattributed; the connective ban may still be sound but its cited backing is wrong, re-cite or downgrade to heuristic) |
| Burstiness / perplexity thresholds | Vendor-sourced, labeled directional by the author | detection-vendor material | QUARANTINED (keep the "directional" caveat; do not present as established fact) |
| Verbatim corpus quotes underpinning craft claims (Kelley lines, Banneker, Gandhi, Sanders "Norway rats", Onion "kilofrankels") | Confirmed word-for-word | primary sources | VERIFIED |

Bottom line of the verification pass: zero false exam-confirmations, all three "correction to carry" provenance items hold, the recomputable stylometry bands stand with none contradicted, and one material Layer-C citation error was caught and flagged. The open items are the blocked-source quarantines (GAO anchor, scanned synthesis PDFs) and the copyrighted exemplars that could not be re-measured.

## 7. Proxy pilot results

The pilot did two things: a BAND CHECK (does a generated piece sit inside its register's measured bands?) and a BLIND READ (can an independent judge, blind, tell the generated register-piece from a genuine professional passage in the same register?).

- Blind-read result: the proxy judge scored 7 of 7, correctly identifying the machine text in every matched pair.
- Honest caveat, stated plainly: this is the OPPOSITE of a pass. A 7 of 7 proxy means the generated drafts in the pilot were still distinguishable from professional prose. The recurring tells the judge named were the same ones the research predicts: relentless rhetorical symmetry, per-paragraph antithesis used as a crutch, manufactured aphoristic closers, self-glossing parentheticals, and metronomic balance. The judge also leaned on PLACEHOLDER tokens that were an artifact of the test harness, not the prose, which inflates the result; but the rhythm-and-symmetry tells were real and independent of the placeholders.
- Band-check result: most pilot pieces landed partly out of band, usually on burstiness (too even, or in one case too jagged), opener variety (too subject-first), and sentence-type mix. The Tribute and the essayistic-argument pieces came closest to fully in-band. One piece tripped the diction blocklist ("leverage"). These are exactly the knobs the per-register bands exist to tighten.
- What the pilot is and is not. It is an automated AI-proxy pre-screen and a stylometric band check. It is NOT a human-judge result, and topic and era differed between the matched texts (the proxy was told to ignore them, but a human protocol must control for this). The pilot's value is diagnostic: it confirms the tells the engine targets are the tells that actually show up, and it tells the operator which bands to pull on. It does not certify the engine as human-passing.
- The validation principle the pilot enforces: tune toward the HUMAN distribution of measurable features (raise burstiness, raise and roughen perplexity, raise lexical diversity, rotate registers), never toward beating one detector's score, which overfits and degrades under the next model update. The real gold standard is a blind human read against genuine professional nonfiction. See [[Blind-Test-Protocol]] for the human test Samuel still needs to run.

## 8. How to operate the engine day to day

The per-piece instruction set lives in [[Generation-Briefs]]; this is the loop around it.

1. Get the facts first and verify them. Accuracy is a separate, non-negotiable gate that sits entirely outside style. Pull facts from sources per [[Content-Sourcing]] and run them through [[Accuracy-Guardrail]]. Never bend a fact to fit a register.
2. Pick the register before drafting. Match the register to the news, not the news to the register. No nameable opposing party means it is not a Reckoning; an occasion to honor rather than argue is a Tribute; no genuine awe means it is not a Long Look. Forcing the wrong register is itself a tell. See [[Style-Palette]] for the routing tests.
3. Assemble the brief from the register sheet. Take the qualitative craft and the quantitative bands for the chosen register out of [[Register-Specs]], pair them with the matching skeleton in [[Structural-Templates]], and build the generation brief per [[Generation-Briefs]].
4. Draft, generating original prose from verified facts only. No reproduction, summary, or paraphrase of source prose.
5. Run the per-piece gate. Re-check the piece against [[Anti-Tell-List]] first (it is cheap and high-value: scan for em-dashes, emojis, the diction blocklist, significance-inflation, copula-avoidance), then check it against its register bands and drift cues.
6. Rotate across the batch. Over a week of roughly five to seven pieces, vary the register so no two pieces share a skeleton, an opening move, or a closing move. A good spread is one Ledger anchor plus a selection from the hotter and more intimate registers, never the same two running.
7. Run the batch-level gate before anything ships. Line the week's pieces up side by side and score them against [[Cross-Piece-Sameness-Rubric]]. A piece can read fine alone and the batch still fail; this is the side-by-side pass that catches shared openings, repeated skeletons, recurring phrases, convergent rhythm, and same-close clustering.
8. Keep accuracy verification separate throughout. Nothing in the style loop touches factual correctness, and nothing in the accuracy loop touches style.

## 9. Open limitations and what still needs the human blind test

- The headline open item: the engine has NOT been validated by human judges. The proxy pilot went 7 of 7 against the machine, meaning the pilot drafts were still distinguishable. The real test is blind human readers (ideally AP Lang teachers) who cannot beat chance distinguishing a generated piece from a genuine professional passage of the same register. That protocol is specified in [[Blind-Test-Protocol]] and is Samuel's to run. Until it is run and passed, treat the engine as a strong hypothesis, not a proven product.
- Band drift in drafts. The pilot showed real generated pieces landing out of band on burstiness, opener variety, and sentence-type mix. The bands diagnose this, but the generation step has to actually hit them; this is the main craft work remaining and the thing the human test will most directly judge.
- Quarantined anchors. The Ledger's primary numeric anchor (GAO-11-282) is unverified because the source was blocked; its bands stand only as a moderated synthesis with a confirmed public-facing pole. Three copyrighted-exemplar registers (Long Think, Witness Stand, Long Look) rest on bands that could not be independently re-measured. If any of these registers underperforms in the human test, re-measuring them from a lawfully obtained full text is the first fix.
- Provenance blind spots. A handful of synthesis prompts (2012 USPS per-source, 2010 Form B DOT slot, 2008 Penny, 2022 STEM) are confirmed at the prompt level only because the College Board PDFs are non-parsing scans. These inform the institutional and policy registers loosely; none is load-bearing for a single register's bands.
- One Layer-C citation to repair. The connective-overuse and uniform-sentence claim was mis-cited to arXiv 2506.21817, which is actually about spiking content words. The connective-reflex ban in [[Anti-Tell-List]] may still be sound, but it needs a correct citation or a downgrade to a labeled heuristic.
- Detector caveat stands. Burstiness and perplexity thresholds are vendor-sourced and directional, not academically established. Use detectors only as a coarse secondary canary, never as the optimization target.
- Two near-merge register pairs to keep watching. The distinctness audit flagged The Reckoning vs The Tribute (highest near-merge risk) and The Long Think vs The Long Look (fuzziest after that). Both were hardened with binary gates in [[Style-Palette]] and [[Register-Specs]], but they are the pairs most likely to collapse in practice and worth re-checking in the first live batches.
