---
created: 2026-06-05
updated: 2026-06-05
tags: [project, caught-up-ai, writing, blind-test, validation, anti-ai-tell]
project: "[[Caught Up AI]]"
---

# Blind-Test Protocol (D7)

> The runnable human-judge protocol for [[Caught Up AI]]. This is the real gold standard for the style work: a Turing-style read in which qualified human judges try to tell a system-written piece from a genuine professional nonfiction passage of the same register. The pieces are written under [[Register-Specs]], built from [[Annotated-Exemplars]], and pre-cleaned against [[Anti-Tell-List]]. If judges cannot beat chance, the style spec is working. If they can, every cue they name is fed back into the spec and the test is re-run.

## What this test does and does not measure

- This test measures STYLE only: whether a piece reads with the craft of professional nonfiction or gives itself away as machine prose. It says nothing about whether the facts in a piece are true.
- Factual accuracy is a separate gate governed by [[Accuracy-Guardrail]]. Never fold accuracy checking into this test, and never let a judge's factual quibble count as a style cue. The texts here are deliberately stripped of checkable specifics (see masking below) so judges cannot use facts as a shortcut.
- The two failure modes the whole style apparatus exists to beat are: (1) the per-piece AI tell (a single piece sounds machine-made), and (2) cross-piece sameness (a batch of pieces all sound like one house voice). This protocol tests BOTH. The pairwise read catches per-piece tells; the batch-scan task (Task C below) catches sameness.

## The short version

- Build matched pairs: one system piece, one genuine AP-Lang-grade professional passage, same register, same length band, topic and era masked.
- Strip every identifying mark from both. Randomize which is which and the order they appear.
- Recruit judges who actually read this kind of prose for a living: AP English Language teachers first, experienced editors or professional writers second.
- Give each judge two tasks per pair: guess which is the machine, and write down the cues they used.
- Score against chance (50%). Pass when judges sit at or near chance, no single cue recurs as a consensus tell, and every system piece is inside its register band.
- Feed every named cue back into [[Anti-Tell-List]] and [[Register-Specs]], regenerate, re-test.

---

## 1. Building the matched pairs

A pair is one system piece and one genuine human passage that a fair judge should not be able to separate on anything except craft. Everything that is not craft must be held constant or removed.

### 1.1 Match on register

- Each system piece is written in one of the seven registers in [[Register-Specs]]. Its human partner must be a passage in the SAME register, drawn from the kind of professional nonfiction the College Board selects for the AP English Language exam: the Q2 rhetorical-analysis source passages and the Q1 synthesis source documents.
- Use the register map below to pick the human partner. These are register ANCHORS, not the only allowed sources. Any professional passage that genuinely sits in the register works; the named authors are there so you know what the register sounds like.

| Register (per [[Register-Specs]]) | Human-passage anchor for the partner |
|---|---|
| The Ledger | Agency or commission report prose; op-ed-pole public finance and policy explainer |
| The Open Letter (deferential periodic appeal) | Banneker to Jefferson; epistolary appeal to a powerful addressee |
| The Reckoning (civic indictment) | Florence Kelley 1905; Kennedy-era civic address |
| The Tribute (eulogy) | Obama or Bush memorial remarks; occasional tribute prose |
| The Long Think (essayistic argument) | Hazlitt; Lippmann; Sanders-pole persuasive op-ed |
| The Witness Stand (confessional spoken essay) | Rita Dove; Saujani; commencement-address voice |
| The Long Look (modern cumulative) | John M. Barry, Rising Tide; long-form narrative nonfiction |

- Do not pair across registers. A Ledger piece judged against a Tribute passage is an unfair, uninformative test: the judge can separate them on register alone and learns nothing about the tell.

### 1.2 Match on length

- The two texts in a pair must sit in the same length band. Target both at the product length, 350 to 600 words, and keep them within about 50 words of each other.
- You will almost always need to excerpt the human passage to fit. Cut at a natural paragraph or sentence boundary so the excerpt still reads as a complete movement, not a severed fragment. A passage that ends mid-thought reads as "the cut one" and becomes its own giveaway.

### 1.3 Control for topic and era (the giveaway you must remove)

This is the most important and most violated control. If the system piece is about a 2026 news event and the human passage is an 18th-century letter about something else, a judge does not need to hear the prose: subject and period hand them the answer. The proxy pilot reported below was explicitly told to ignore topic and era, but a human cannot un-know what they have read. So you remove the cue instead of asking judges to suppress it.

Three settings, in order of rigor. Use the strongest one you can manage.

- BEST, topic-matched generation. Before the test, pick the human passage first. Note its subject area and rhetorical situation at a high level (for example: "an appeal to an authority about an injustice," or "a reflective essay about work and money"). Generate the system piece on a DIFFERENT but tonally comparable subject in the same register, so the two are about adjacent things, not the same thing. Then mask both as in section 2. Judges see two texts on plausibly similar territory, neither obviously "ripped from today's news."
- ACCEPTABLE, era-neutralizing mask. If the system piece is necessarily about current events, mask hard: replace every dated proper noun, every figure, every place, every brand, and every period-specific reference in BOTH texts with a neutral placeholder of the same shape (see section 2.2). A heavy mask flattens the era signal so the surviving difference is mostly craft. This is weaker than topic-matched generation because syntax and diction still leak period, but it is honest if you label it as the weaker setting.
- LAST RESORT, instructed suppression. Tell judges to ignore subject and era and judge craft only, exactly as the proxy was told. This is the weakest control because humans cannot truly comply. Only use it if you cannot generate a topic-matched piece and cannot mask without destroying the prose. If you use it, say so in the results and treat any near-chance result with extra caution.

Whatever setting you use, record it per pair. Mixing settings inside one test batch is fine as long as you log which pair got which.

### 1.4 Batch composition

- Build at least two pairs per register so a result is about the register, not one lucky or unlucky piece. With seven registers that is a minimum of 14 pairs; 21 (three per register) is better and still runnable.
- For the cross-piece sameness task (Task C), also assemble a SYSTEM-ONLY set: 8 to 12 system pieces spread across all seven registers, no human partners. This set tests whether the batch reads as many voices or one.

---

## 2. Masking (stripping identifying marks)

Every text, system and human, goes through the same scrub. The goal: a judge cannot use anything except the prose itself.

### 2.1 Remove provenance marks

- Strip titles, bylines, datelines, publication names, and any "by" line.
- Remove footnotes, citation markers, source tags, and any "[PLACEHOLDER: ...]" tokens left over from the exemplar scaffolding. The bracketed placeholder tokens in [[Annotated-Exemplars]] are an authoring artifact; they are a dead giveaway and must be gone before any human sees the text. (In the proxy pilot below, the presence of placeholder tokens was a cue the automated judge leaned on. Do not let that happen with humans.)
- Normalize formatting across both texts: same font, same spacing, same paragraph style, no markdown, no smart quotes on one and straight quotes on the other. Formatting asymmetry is a tell about which file came from where.

### 2.2 Neutralize topic and era markers (when using the masking setting)

- Replace dated or identifying specifics with same-shape neutral placeholders, applied to BOTH texts equally: a year becomes "a recent year" or a bracketed neutral token, a named agency becomes "a federal body," a named person becomes "an official" or a generic role, a brand becomes "a company," a city becomes "a city."
- Match the placeholder DENSITY across the pair. If one text ends up bristling with "[a body]" tokens and the other reads clean, the masking itself becomes the tell. If a passage cannot survive masking without looking peppered, pick a different passage.

### 2.3 Label the texts neutrally

- Call them TEXT 1 and TEXT 2 (or A and B). Never "the AI one" / "the real one," never a number that encodes which is which.

---

## 3. Randomization

- For each pair, flip a coin (or use a random number) to decide whether the system piece is TEXT 1 or TEXT 2. Log the true answer in a key the judge never sees.
- Randomize the ORDER pairs are presented to each judge, and ideally vary that order between judges, so position cannot become a habit ("the machine is always second").
- Counterbalance: across the whole batch, the system piece should land in the TEXT 1 slot about half the time. Check this after you build the key; if it skewed, reshuffle.
- One person who is not a judge holds the key. Judges score blind; the key is opened only at scoring.

---

## 4. Recruiting judges

- PRIMARY judges: AP English Language teachers. They read professional source passages and student attempts at them all year; they are the closest thing to a calibrated instrument for this exact register palette. Samuel already has an outreach list (see [[Outreach-Tracker-2026-05]] and the verified-teacher list in the project folder).
- SECONDARY judges: experienced editors, professional nonfiction writers, English or writing instructors. Use these to round out numbers or if teacher recruiting is slow.
- Disqualify: anyone who built, tuned, or has read the system pieces; anyone who has seen [[Register-Specs]] or [[Anti-Tell-List]]; close friends doing a favor (politeness skews their guesses). The test only means something if the judge is genuinely blind and genuinely qualified.
- NUMBERS: aim for at least 5 judges, 8 to 12 is better. More judges is the cheapest way to make the chance comparison trustworthy and to measure whether a cue is idiosyncratic or shared.
- Each judge sees every pair (fully crossed) so you can measure inter-judge agreement on the same items. If that is too long a sitting, split into blocks but keep at least 3 judges per pair overlapping so agreement is still measurable.
- Keep judges independent: no conferring during the test. Discussion after scoring is welcome and is a good source of cues, but capture each judge's INDIVIDUAL answers first.

---

## 5. The judge tasks

Give judges a short, plain briefing: "One of these two texts was written by a machine imitating professional nonfiction. The other is genuine professional nonfiction. They are matched for register and length and have been stripped of identifying detail. We want your honest read." Do not coach them on what tells to look for; the cues they volunteer are data.

### Task A, forced choice (per pair)

- "Which text was written by the machine, TEXT 1 or TEXT 2?" No "can't tell" option; force the guess so the result is scorable against 50% chance.
- "How confident are you: low, medium, or high?"

### Task B, cues (per pair)

- "Whatever you guessed, write one to three specific cues you used. Point to a sentence or a feature, not a vibe." Capture verbatim. This is the iteration fuel.

### Task C, batch sameness (run once, on the system-only set)

- Hand the judge the 8 to 12 system-only pieces (masked, unlabeled) and ask: "Do these read as written by one author or several? If you can group any of them as sharing a voice, mark the groups and say what they share."
- This is how you catch cross-piece sameness, the second failure mode. A judge who confidently clusters several pieces as "obviously the same hand" has found a sameness tell even if each piece individually passed Task A. Record the grouping logic; it feeds [[Cross-Piece-Sameness-Rubric]].

---

## 6. Metrics

Compute these after opening the key.

- IDENTIFICATION ACCURACY. Across all pairs and judges, the share of times the judge correctly named the machine. Chance is 50%. Report the overall number, and also break it out per register (which registers are giving themselves away) and per masking setting (did topic-matched pairs score closer to chance than instructed-suppression pairs, as expected).
- CONFIDENCE-WEIGHTED VIEW. Cross accuracy with stated confidence. The worst outcome is high-confidence-correct, that is a clean tell. High-confidence-wrong is a good sign (the judge was sure and was fooled). Track the high-confidence-correct rate specifically.
- INTER-JUDGE AGREEMENT. For each item, do the judges converge on the same answer? High agreement that is also correct means a shared, real tell. High agreement that is wrong means the texts are genuinely confusable (good). Scattered answers near 50% mean judges are guessing (the target state). A simple percent-agreement per item is enough; a no-code operator does not need a kappa statistic, just "did the judges mostly agree, and were they right."
- CUE CATALOGUE. Collect every cue from Task B verbatim, then group them by theme (for example: "balanced antithesis every paragraph," "aphoristic closers," "too-even rhythm," "tells the reader something matters," "placeholder tokens left in"). Count how many judges independently named each theme. A cue named by many judges across many pieces is a CONSENSUS TELL and is the top priority for the next spec revision.
- BAND CHECK (run in parallel, not by judges). Before or alongside the human read, confirm each system piece sits inside its register band per [[Register-Specs]]. A piece can fool a judge and still be out of band; both must be true to pass. Use the same measured-feature read the proxy used (sentence-length mean and variance, type mix, opener variety, punctuation rates, the surface-tell blocklist).

---

## 7. The pass bar (explicit)

A test batch PASSES only when all four hold. If any one fails, the batch fails and you iterate.

1. IDENTIFICATION AT OR NEAR CHANCE. Overall identification accuracy is at or near 50%. Treat anything in roughly 40 to 60% as at chance for a small panel. You have drifted if accuracy sits at 70% or higher, that means judges can reliably pick the machine.
2. NO CONSENSUS TELL. No single cue theme is named by a majority of judges across multiple pieces. One judge's idiosyncratic hunch is noise; a tell half the panel independently names is a real defect, even if accuracy happened to land near chance on that batch.
3. EVERY SYSTEM PIECE IN BAND. Each system piece is inside its register band per [[Register-Specs]] (or its out-of-band flags are minor and explained). A piece that fools judges but is out of band is on borrowed time and does not pass.
4. NO SAMENESS CLUSTER. In Task C, judges cannot confidently group multiple system pieces as one voice. If they cluster three or more pieces and agree on what they share, cross-piece sameness has failed regardless of per-pair results.

A near-chance result with a clean cue catalogue, in-band pieces, and no sameness cluster is the win condition. Banking a single near-chance batch is not proof for all time; re-run on a fresh batch after any meaningful spec change or model update.

---

## 8. The iteration loop

This is the engine, not a footnote. The test exists to produce cues, and the cues exist to fix the spec.

1. RUN the test, compute section 6 metrics.
2. RANK the cue catalogue by how many judges named each theme. Consensus tells first.
3. FEED each tell to its home:
   - Surface tells (a banned word slipped through, a stray em-dash, a placeholder token, an emoji) go straight to [[Anti-Tell-List]] as a mechanical re-check item. These are cheap to kill and should never recur.
   - Craft tells (balanced antithesis in every paragraph, aphoristic closers on cue, too-even rhythm, telling the reader something matters, relentless not-X-but-Y) go to [[Register-Specs]] as a band tightening or a new drift cue, and the matching model in [[Annotated-Exemplars]] gets re-annotated so the counterfeit move is named and the real move shown.
   - Sameness tells (pieces clustering as one voice, repeated opening or closing shapes across the batch) go to [[Cross-Piece-Sameness-Rubric]] and tighten the rule that no two consecutive pieces share an opening or closing move, with registers rotated across the batch.
4. REGENERATE the failing pieces against the revised spec.
5. RE-TEST on a fresh pair set with fresh judges where possible (a judge who has seen the texts is no longer blind). Repeat until the section 7 bar holds.

Do not tune by submitting drafts to one automated detector and editing until it passes; that overfits to the tool and degrades on the next model update. The human read is the gold standard. Automated detectors are a coarse secondary canary only (see section 9).

---

## 9. Proxy pilot results (automated, NOT human judges)

> CAVEAT, verbatim: These are automated AI-proxy results and a stylometric pre-screen only. They are NOT human-judge results. The real blind test with AP Lang teachers is specified in Blind-Test-Protocol.md for Samuel to run. Topic/era differ between matched texts; the proxy was instructed to ignore them but a human protocol must control for this.

What was run: a stylometric band check on eight system pieces (one per register-plus-pole), and an eight-pair blind read in which an automated judge model, told to ignore topic and era, guessed which of two texts was the machine and named its cues. This is a PRE-SCREEN to catch obvious problems before spending scarce human-judge time, not a substitute for section 1 through 8.

### 9.1 Blind read (automated judge)

- Result: the automated judge went 7 for 7 on the pieces it was shown, every guess correct, confidence high to medium. In plain terms, the proxy was NOT fooled.
- This is expected and is not a failure of the style spec on its own. The automated judge leaned heavily on artifacts the human protocol removes by design:
  - The leftover "[PLACEHOLDER: ...]" tokens in the exemplar texts. Section 2.1 strips these. The proxy named them as a cue in nearly every read.
  - Topic and era contrast between the matched texts. Section 1.3 controls this; the proxy was only told to ignore it, which is the weakest setting and exactly the gap a human protocol must close.
- The CRAFT cues the proxy named are the useful output, because they are the same kind of cue a human will name and they point straight at spec fixes. The recurring ones:
  - Balanced antithesis in nearly every paragraph; the "X, not Y" / "cuts in two directions" move used as a metronome.
  - Aphoristic closers on cue; almost every paragraph resolving into a quotable button.
  - Relentless not-X-but-Y patterning and evenly weighted tricola that read as engineered rather than felt.
  - Too-even, frictionless rhythm; the absence of the uneven, content-driven cadence the human anchors show.
  - Telling the reader something matters instead of showing it (the significance-inflation reflex [[Anti-Tell-List]] already targets).
- ACTION TAKEN: these craft cues are exactly what section 8 routes into [[Register-Specs]] and [[Anti-Tell-List]]. The placeholder-token cue is a section-2 masking fix, not a prose defect.

### 9.2 Band check (stylometric pre-screen)

Eight pieces measured against their [[Register-Specs]] bands. Two were in band; six drifted. None contained an em-dash or emoji. One banned-list term ("leverage") appeared once and must come out.

| Register / pole | In band | Headline drift (full detail in the per-piece read) |
|---|---|---|
| The Ledger, agency-report pole (per-mile fee) | No | Mean 23.1 w/sent sits at top of the 18 to 24 band, above the 19 to 21 anchor; one 47-word sentence over the 44 cap; std dev 11.6 over the 6 to 9 target (too bursty for the even surveying rhythm); too few simple sentences, too many complex and compound-complex; 81% subject-first openers (band 50 to 60); slightly plainer diction than the register wants |
| The Open Letter, deferential periodic appeal | No | Mean 18.8 w/sent below the 24 to 34 band (drifted to the clipped Gandhi pole); 12 sentences under 12 words vs 2 to 4 expected; 40% simple vs 10 to 25%; 72% subject-first openers vs 45 to 60; only 2 semicolons vs the 0.3 to 0.6 per-sentence band |
| The Reckoning, civic indictment | No | Mean 18.3 w/sent below the 22 to 28 band (pulled down by short buttons); longest runway 72 words over the 45 to 70 cap, plus two more near-runway sentences when the band wants one; compound-complex under band, simple over band; 75% subject-first openers (band 50 to 65) though opener TYPE variety is fine |
| The Tribute, eulogy | Yes | Coordinating-conjunction openers 6% vs 17 to 21 target (biggest miss; under-uses And/Yet/But/So chaining); 84% subject-first; button-heavy skew; otherwise in band |
| The Long Think, essayistic argument | Yes | Mean 21.0 w/sent just below the 22 to 28 center but inside the wider band; simple-sentence share low because short sentences carry a subordinate clause; opener variety slightly thin; the only materially out-of-band metric is the simple/complex label split |
| The Witness Stand, confessional spoken essay | No | Mean 14.2 w/sent below the 17 to 24 band floor (many 3 to 6 word lines); comma density 4.5/100w below the 6 to 9 band; the banned term "leverage" present once (must be removed) |
| The Long Look, modern cumulative | No | Longest sentence 89 words over the 40 to 60 ceiling (two showpieces at 89 and 65); burstiness CV 1.09 above the 0.7 to 0.9 target; 1 semicolon vs the 3 to 7 floor (colons over-substituting); subject-first openers slightly high |

### 9.3 What the pilot tells us going into the human test

- The style spec is producing prose that an automated perplexity-style judge still catches, mostly via removable artifacts (placeholder tokens, topic/era) plus a real cluster of craft tells (balanced antithesis, aphoristic closers, too-even rhythm, significance-inflation). The craft tells are the genuine signal and are the priority for the next [[Register-Specs]] and [[Anti-Tell-List]] revision.
- Most pieces are slightly out of band on the same axes: rhythm too even or too bursty for the register, openers too subject-first, length means drifting toward the wrong pole. Fixing band drift and the craft tells are the same project: more genuine, content-driven variability and less engineered symmetry.
- Detector guidance to carry forward (do not over-apply): tune toward the HUMAN distribution of measurable features, not toward any one detector's score. Raise burstiness honestly (at least one sub-8-word sentence and one 30-plus-word sentence per piece, adjacent sentences rarely the same length). Raise lexical diversity and forbid a reused transition kit. Keep the surface blocklist mechanical and absolute (no em-dashes, no emojis, no AI-lexicon words). Treat cross-piece sameness as a first-class failure by rotating registers and never repeating an opening or closing shape back to back. Do NOT chase a single detector or rely on "make it sound human" prompting; neither moves the real needle.
- Bottom line: the pilot is a useful pre-screen and a source of concrete fixes. It is NOT the pass signal. The pass signal is the human panel at or near chance under sections 1 through 8, with no consensus tell, in-band pieces, and no sameness cluster.

---

## Cross-links

- [[Annotated-Exemplars]]: the worked model pieces these system texts are written toward; re-annotate here when a craft tell surfaces.
- [[Anti-Tell-List]]: the mechanical blocklist; surface tells from the cue catalogue land here.
- [[Register-Specs]]: the per-register bands and drift cues; craft tells and band misses land here.
- [[Cross-Piece-Sameness-Rubric]]: governs the batch-sameness defense tested in Task C.
- [[Style-Palette]], [[Structural-Templates]]: register selection and skeletons behind each piece.
- [[Accuracy-Guardrail]]: the separate, non-negotiable factual gate this test never touches.
- [[Outreach-Tracker-2026-05]]: the AP Lang teacher recruiting pipeline that supplies judges.
