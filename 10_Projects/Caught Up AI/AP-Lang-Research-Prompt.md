---
created: 2026-06-05
updated: 2026-06-05
tags: [project, caught-up-ai, content-engine, prompt]
---

# AP Lang Prose Engine - Deep Research Commission

> Paste the fenced block below verbatim into a fresh ultracode multi-agent run, launched from this vault folder so agents can read Writing-Manual.md and write into 10_Projects/Caught Up AI/. Fully self-contained. Produces v2 of the Writing Manual. See chat for the knobs and caveats.

```text
======================================
DEEP RESEARCH COMMISSION, "AP-Lang-Caliber Prose Engine for Caught Up AI"
Run this as an ultracode multi-agent (fan-out / verify / synthesize) job.
======================================

--------------------------------------------------------
0. READ THIS FIRST, YOU HAVE NO MEMORY OF PRIOR SESSIONS
--------------------------------------------------------
You are a research swarm with no prior context. Everything you need is stated here. Do not assume facts not given; verify the ones that are.

WHO THIS IS FOR
Samuel is a solo founder building a product called "Caught Up AI." It publishes short, original, current-events "catch-up" pieces (roughly 350-600 words each) written to professional nonfiction quality. He is a no-code operator: he directs AI and verifies by reading output, not by inspecting code. Hard personal style constraints that override everything below: NO em-dashes anywhere (use commas, colons, periods, parentheses), and NO emojis.

THE PRODUCT DECISION THIS SERVES
Caught Up AI is going full AI-generation. Claude reads current sources for FACTS ONLY (facts are not copyrightable), then writes an entirely original piece from scratch. We are not reproducing, summarizing, or paraphrasing source prose; we are reporting verified facts in original sentences. Current-events ACCURACY is therefore non-negotiable and is a separate requirement from style: a beautifully written piece that misstates a fact is a failure.

THE EXACT QUALITY TARGET (read carefully, this is the whole job)
The pieces must read with the craft and register of the PROFESSIONAL NONFICTION PASSAGES that the College Board selects as source texts for the AP English Language and Composition exam, specifically the rhetorical-analysis (Q2) source passages and the synthesis (Q1) source documents. These are the real, professionally written essays, speeches, letters, and articles that students are given and then write analysis essays ABOUT.

Be precise about three things, because earlier framing got them wrong:
  (a) We are emulating the PROFESSIONAL SOURCE PROSE, NOT student essays. The target is the writing students analyze, never the writing students produce. Do not study, score against, or import the conventions of high-scoring student FRQ responses. Where a source describes "what graders reward," translate it into properties of the SOURCE TEXT, not the response.
  (b) There is NO SINGLE "AP LANG STYLE." This is the central correction. The exam deliberately draws across centuries (18th to 21st), genres (familiar essay, political speech, open letter, eulogy, commencement address, memoir, narrative nonfiction, op-ed, public statement), and rhetorical situations. The correct target is therefore a PALETTE of distinct professional registers, not one house voice. The deliverables must preserve and operationalize that RANGE.
  (c) We emulate CRAFT, not TOPICS. The corpus is about child labor, money, nature, nonviolence, public service. Our pieces are about today's news. The transferable thing is rhetorical architecture, sentence craft, register, and the management of ethos/pathos/logos, never subject matter, period diction, or pretending a current piece was written in 1850.

SAMUEL'S SUCCESS TEST, IN HIS WORDS
The pieces should be "indistinguishable from any essay you find when you look up past AP Lang exam FRQ prompts." Operationalized: across a blind read by qualified judges (AP Lang teachers / experienced readers), a current-events Caught Up AI piece written by this system, when placed beside genuine AP-Lang-selected professional passages of comparable length and matched register, cannot be reliably identified as the machine-written or the modern-outsider one at a rate better than chance, and shows none of the known AI tells. "Indistinguishable across the palette," not "indistinguishable as one style."

THE HARD PROBLEM YOU MUST SOLVE
AI nonfiction reads same-y and is increasingly detectable: a recognizable house cadence, predictable structure, a fixed lexicon, suspiciously even sentence length, mechanical symmetry, and stock transitions. Two failure modes must be beaten at once: (1) the per-piece AI tell (any single piece reads as machine-made), and (2) CROSS-PIECE SAMENESS (twenty pieces share an obvious skeleton, opening move, and rhythm even if each passes alone). Beating cross-piece sameness via DELIBERATE, CONTROLLED VARIETY across registers is a first-class objective, not a nice-to-have.

WHAT ALREADY EXISTS (your starting point and baseline to beat, not the ceiling)
A v1 apparatus already exists in this vault at 10_Projects/Caught Up AI/Writing-Manual.md, reverse-engineered from the released exam corpus. It contains: a verified corpus table (below), a single open/build/close structural spine, long-vs-short sentence-rhythm rules, an earned-device palette, and an AI-tell blocklist. Treat it as v1 PRIOR WORK to extend, stress-test, and partly supersede, NOT as settled truth. Its main known weakness is exactly the thing this commission must fix: it encodes essentially ONE structural template and ONE rhythm rule, which, applied repeatedly, will itself become a detectable house style. Your job is to replace the single template with a RANGE, validate every claim empirically, and add the stylometric and detectability layers it lacks.

VERIFIED CORPUS ANCHORS (confirmed from released exams; use as seed, expand, and re-verify each)
  2006 William Hazlitt, "On the Want of Money", familiar essay; cumulative syntax, anaphora ("it is to...")
  2007 Scott Russell Sanders, "Staying Put", essay; concession then rebuttal; withheld metaphor at the turn
  2008 John M. Barry, "The Great Influenza", narrative nonfiction; antithesis (certainty vs uncertainty), short declaratives
  2010 Benjamin Banneker, letter to Jefferson, letter; quotes the Declaration back at its author; appeal to conscience
  2011 Florence Kelley, child-labor speech, speech; present-tense pivot ("Tonight while we sleep"); concrete child imagery
  2012 John F. Kennedy, steel-price statement, public statement; "ordinary citizens" vs "a tiny handful of steel executives"; statistics
  2013 Richard Louv, "Last Child in the Woods", essay; irony, anecdote, nostalgic tonal shift at the close
  2014 Abigail Adams, letter to her son, letter; maternal ethos; aphorism ("Great necessities call out great virtues")
  2015 Cesar Chavez, nonviolence article, op-ed; antithesis as engine; aphoristic button
  2016 Margaret Thatcher, Reagan eulogy, eulogy; "Others... He..." anaphora; balanced periodic syntax
  2017 Clare Boothe Luce, press-club speech, speech; disarms a hostile audience by conceding first
  2018 Madeleine Albright, commencement, speech; refrain ("have courage still"); exemplification escalating in scale
  2019 Gandhi, letter to Lord Irwin, letter; measured concessive tone; paradox; ethos of humility
  2021 Obama, Rosa Parks statue dedication, speech; narrative, anecdote, antithesis
  2024 Reshma Saujani, "American Like Me", memoir; perfection vs bravery antithesis; self-deprecation
Carry these corrections: the Chavez nonviolence passage is 2015 Q2 (not a 2014 argument prompt); Orwell, Didion, Staples, Carson, and MLK "Letter from Birmingham Jail" are TEACHING mentor texts, NOT exam passages, the exam deliberately avoids the most-anthologized pieces. Re-verify year/author/form for every anchor against primary College Board materials before relying on it; flag any you cannot confirm.

--------------------------------------------------------
0.5 LOCKED PARAMETERS (non-negotiable; do not deviate, do not treat as open choices)
--------------------------------------------------------
These six settings are fixed by Samuel because each one widens the range the prose can blend into and hardens it against detection. Treat them as constraints, not defaults to reconsider.
  P1. REGISTER COUNT. The style palette must contain 5 to 9 distinct registers, derived from the corpus. Do not collapse toward a single house voice and do not drop below 5. Breadth of distinct registers is the primary defense against cross-piece sameness.
  P2. CORPUS SPAN. Study BOTH Q1 synthesis sources AND Q2 rhetorical-analysis sources, spanning ~1999 to 2024 AND older released forms wherever available. Do not narrow to the contemporary era; the historical registers are load-bearing parts of the palette.
  P3. BLIND-TEST. Fully specify the runnable human-judge protocol AND run a self-administered proxy pilot now: an automated-detector pre-screen, a Layer-B stylometric-band check, and an independent-agent "is this machine-written" read on each exemplar. The real AP-Lang-teacher panel is Samuel's to run later; never fabricate or simulate human-judge results.
  P4. PIECE LENGTH. Calibrate everything to a 350 to 600 word piece. The stylometric bands, templates, and exemplars all assume this length.
  P5. DETECTOR RELIANCE. Automated AI detectors are a PRE-SCREEN only; blind human judgment is the decisive gold standard. Tune toward the measured human distribution and never overfit to any single detector.
  P6. EXEMPLAR TOPICS. Write the annotated exemplars on plausible, clearly-labeled placeholder current topics, and flag every invented specific as a placeholder so no unverified fact ships. Do not present fabricated specifics as real.

--------------------------------------------------------
1. THE CORPUS YOU MUST STUDY
--------------------------------------------------------
Assemble and study the largest defensible corpus of GENUINE AP-Lang-selected professional source passages:
  - Q2 rhetorical-analysis SOURCE passages across released exams (target span ~1999-2024; older released forms welcome for range). Verbatim text where lawfully obtainable; otherwise work from confirmed identification (author, title, year, form) plus the public source text.
  - Q1 SYNTHESIS source documents (these widen the register range: reports, opinion columns, public-institution prose, advocacy writing).
  - The full GENRE SPREAD must be represented: 18th-19th c. oratory and open letters; the familiar/personal essay; the political speech and public statement; the eulogy and commencement address; narrative nonfiction; the modern op-ed; memoir.
  - Both HISTORICAL (pre-1950) and CONTEMPORARY (post-2000) registers, because the palette must span them.
Exclude and explicitly mark: student response samples, teaching mentor texts that the exam itself avoids, and any passage you cannot tie to an actual released exam (label these "adjacent / not exam-confirmed" and keep them out of the core stylometric baseline).
Document provenance for every text (exam year, question, author, form, era, word count) so claims are auditable. Be transparent about copyright: study and measure freely (facts, statistics, and stylistic features are not protected), but do NOT have the eventual product reproduce these passages, the product writes original prose informed by their CRAFT.

--------------------------------------------------------
2. RESEARCH QUESTIONS, THREE LAYERS
--------------------------------------------------------
Investigate all three. Keep them distinct; do not let craft description smuggle in unmeasured claims.

LAYER A, RHETORICAL CRAFT (qualitative, close reading)
  A1. Partition the corpus into a set of distinct REGISTERS (the palette). Derive them from the texts; do not impose a list. For each register name it, characterize its voice, and identify exemplar passages.
  A2. For each register: what is the characteristic stance, implied audience, occasion logic, and authorial ethos? How is ethos established (vantage, restraint, credential-by-implication, moral authority, intimacy)?
  A3. How are the rhetorical appeals BRAIDED (ethos/pathos/logos interleaved within sentences) versus siloed? Where does pathos actually live (specific nouns and concrete scenes vs abstraction and emotion-words)?
  A4. Structural architectures BEYOND the single open/build/close spine. Catalogue the real range: concession-then-rebuttal, antithesis-as-engine, accumulation under a repeated frame, escalating exemplification, narrative-into-claim, problem-reframe, dialectic, withheld-turn, periodic build to a button, and others you find. Note which registers favor which.
  A5. Opening and closing MOVES as a typology (not one rule): how these passages actually start and land, the variety of each, and what makes a close earn its landing in each register.
  A6. The role of allusion, irony/understatement, rhetorical questions, aphorism, and figurative language per register, including where each is ABSENT (some registers are plainer; record that).

LAYER B, MEASURABLE STYLOMETRIC FINGERPRINTS (quantitative)
  Compute, per register and across the corpus, and report distributions (mean, spread, range), not single numbers:
  B1. Sentence-length distribution and, critically, sentence-length VARIANCE / burstiness (the long-against-short signature).
  B2. Sentence-TYPE mix (simple / compound / complex / compound-complex) and sentence-OPENER variety (subject-first vs dependent-clause / adverbial / prepositional / fragment openings).
  B3. Syntactic measures: clause depth, periodic vs loose ratio, parallelism rate, fragment rate, punctuation profile (colon/semicolon/comma/parenthesis usage, with em-dashes recorded for the corpus but BANNED in our output).
  B4. Lexical measures: type-token ratio / lexical diversity, concreteness/abstractness ratio, Latinate vs Anglo-Saxon diction lean, function-word fingerprints, hapax rate, readability indices (per register).
  B5. Rhythm and sound: cadence at sentence ends, monosyllable runs, stress patterning where detectable.
  B6. Device DENSITY: how many "markable" rhetorical moves per 100 words, by register, and how they cluster.
  Deliver these as target RANGES per register (e.g., "register X: mean sentence length 14-22 words, variance high, fragments 0-2 per 400 words"), so a writer can be tuned to hit a register's measured envelope and told when it has drifted out of band.

LAYER C, AI-DETECTABILITY TELLS (the adversary)
  C1. Catalogue known AI-nonfiction tells empirically: lexical (the "delve/tapestry/underscore/robust/nuanced/multifaceted" family and current equivalents), syntactic (suspiciously even sentence length, mechanical parallelism, participial-opener stacks, tricolon-on-autopilot), structural (the tidy three-point bow, the "It's not just X, it's Y" reveal cadence, "In a world where...", "Here's the thing", throat-clearing rhetorical questions), and discourse (over-hedging, false balance, generic authority like "studies show" with nothing attached).
  C2. Where do these tells OVERLAP with legitimate corpus craft (genuine antithesis, genuine anaphora, genuine tricolon), and how do you tell the real move from the AI imitation? This boundary is essential, the manual must encourage real devices while banning their machine-counterfeits.
  C3. CROSS-PIECE tells specifically: what makes a SET of pieces read as one author/model even when each piece passes alone (shared opening gambits, identical skeletons, recurring pet phrases, same rhythm signature, same close type). Define how to measure sameness across a batch.
  C4. Survey current AI-text detectors and the academic state of detection (capabilities and limits, false-positive behavior). Identify which measurable features (Layer B) most separate AI nonfiction from the human corpus, so the writing spec can be tuned toward the human distribution. Do not overfit to any one detector; treat blind human judges as the gold standard.

--------------------------------------------------------
3. METHODOLOGY (mandatory)
--------------------------------------------------------
  M1. MULTI-AGENT FAN-OUT. Parallelize: agents per era, per genre/register, per layer (craft / stylometry / detectability). Each agent works from primary materials and reports with citations.
  M2. ADVERSARIAL VERIFICATION. Every non-trivial claim (a corpus fact, a stylometric number, a "this is a tell" assertion) is checked by a second, independent agent against primary sources or recomputed from text. Stylometric numbers must be reproducible from the stated corpus. Flag and quarantine anything unverified; never present a guess as a finding. Separately verify corpus provenance (that a passage really is an exam source text).
  M3. BLIND-TEST PROTOCOL (operationalize "indistinguishable"). Design and SPECIFY a runnable protocol, and run the self-administered proxy pilot from P3 now:
      - Build matched pairs: a system-written current-events Caught Up AI piece vs a genuine AP-Lang professional passage of comparable length and the SAME target register. Multiple pairs across MULTIPLE registers (not one).
      - Strip all identifying marks (no period-specific topical giveaways; control for the fact that ours are current-events, match on register and craft, not subject).
      - Randomize order; present to qualified blind judges (AP Lang teachers / experienced readers). Judges (a) guess machine vs human and (b) state the cues they used.
      - Metrics: identification accuracy (chance = 50%), inter-judge agreement, and a catalogue of the CUES judges report (these feed straight back into the anti-tell list).
      - Also run candidate pieces through the Layer B stylometric bands and at least one automated detector as a pre-screen, but treat blind human judgment as decisive.
      - Define the PASS BAR explicitly (e.g., judges at or near chance, no consensus tell, within stylometric band for the claimed register).
      - Specify iteration: feed every failure cue back into the spec and re-test. The deliverable is a protocol Samuel can re-run on real production pieces, plus pilot results.

--------------------------------------------------------
4. DELIVERABLE ASSETS (concrete, operational, this is what gets used)
--------------------------------------------------------
Produce ALL of the following, written so a no-code operator and a drafting model can apply them directly:

  D1. THE STYLE PALETTE. A NAMED set of distinct registers (target ~5-9), derived from the corpus. For each: a one-line identity, the era/genre it descends from, when to use it for a current-events piece, exemplar source passages, and its signature craft. This palette is the backbone that beats cross-piece sameness.

  D2. ROTATING STRUCTURAL TEMPLATES. A library of distinct structural architectures (not the single open/build/close spine), each as a reusable skeleton with its open-move options, engine, and close-move options. Enough templates that a daily cadence can rotate without repeating a recognizable shape. Include an explicit ROTATION SCHEME / selection logic so successive pieces deliberately differ in register, structure, opening type, and rhythm.

  D3. PER-REGISTER WRITING SPECS. For EACH palette register, a single spec sheet combining:
      - QUALITATIVE: voice, stance, ethos strategy, device palette, opening/closing repertoire, what to do and what to avoid in this register.
      - QUANTITATIVE: the Layer-B target bands (sentence-length mean and variance, type/opener mix, parallelism and fragment rates, lexical concreteness, device density), stated as ranges with explicit drift-out-of-band warnings.

  D4. ANTI-TELL DO/DON'T LIST. A hard, current blocklist (diction, constructions, structures) PLUS, for each banned item, the legitimate craft move it is often mistaken for and how to do the real thing instead. Must absorb and update the existing v1 blocklist (no em-dashes; the "it's not just X, it's Y" reveal; "in a world where" / "here's the thing" / "at the end of the day" / "more than ever" / "from X to Y"; the delve/tapestry/underscore/robust/nuanced/multifaceted family; tidy three-point bows; participial-opener stacks; tricolon-on-autopilot; vague "studies show"). Keep em-dashes and emojis permanently banned regardless of corpus usage.

  D5. CROSS-PIECE SAMENESS RUBRIC. A scoring tool to run over a BATCH of pieces (e.g., a week's output) that flags shared openings, repeated skeletons, recurring phrases, convergent rhythm, and same-close-type clustering, with thresholds and a remediation step. This is the operational defense against batch detectability.

  D6. ANNOTATED EXEMPLARS. A set of FULLY WRITTEN current-events Caught Up AI catch-up pieces (use plausible, clearly-labeled illustrative current topics; mark any invented specifics as placeholders so no unverified fact ships), one per palette register, EACH annotated to show: which register and template it uses, where each craft move happens and why, the stylometric bands it hits, and how it dodges each relevant tell. These are the gold-standard models the production system imitates. Include at least one "before/after" showing a tell-laden draft repaired into the target register.

  D7. PRODUCTION GENERATION BRIEFS. For each register, a paste-ready drafting brief (the prompt Claude uses to write that day's piece), plus a master orchestration note explaining how Samuel selects register + template per piece to maintain variety, and a pre-flight checklist per piece (accuracy check, register-band check, anti-tell scan, batch-sameness check).

  D8. CURRENT-EVENTS ACCURACY GUARDRAIL. A short protocol ensuring the craft layer never overrides factual fidelity: how facts are sourced and verified before drafting, how to keep original prose from drifting into a source's protected expression, and a fact-check step in the per-piece pre-flight.

--------------------------------------------------------
5. OUTPUT FORMAT AND STORAGE
--------------------------------------------------------
  - Save all deliverables into this vault under 10_Projects/Caught Up AI/. Suggested files: "Style-Palette.md", "Structural-Templates.md", "Register-Specs.md", "Anti-Tell-List.md", "Cross-Piece-Sameness-Rubric.md", "Annotated-Exemplars.md", "Generation-Briefs.md", "Blind-Test-Protocol.md", and a top-level "Prose-Engine-Research-Report.md" that ties them together with the methodology, the corpus manifest, and the verification log. Do not overwrite Writing-Manual.md; supersede it explicitly and note in it that these files extend and replace v1.
  - Use the vault style: front-matter (created / updated / tags) on every file, bullet-first, wiki-links between files and to [[Writing-Manual]], [[Content-Sourcing]], [[Caught Up AI]]. NO em-dashes, NO emojis, in any deliverable.
  - Include a corpus manifest (every text, provenance, word count) and a claims/verification log (claim, who verified, against what source, status).
  - Keep specs operational: ranges and checklists a non-coder can apply by reading, not formulas requiring tooling. Where a number matters, give the band and a plain-language "you have drifted if..." cue.

--------------------------------------------------------
6. SUCCESS CRITERIA (the job is done when...)
--------------------------------------------------------
  S1. The PALETTE is real: a current-events piece can be written in any of the named registers and the registers are audibly distinct from one another (not one voice with cosmetic changes).
  S2. BLIND-READ INDISTINGUISHABILITY: in the specified blind protocol, system pieces matched to genuine AP-Lang passages by register are identified by qualified judges at no better than near-chance, with no consensus tell, across MULTIPLE registers. The pilot reports actual numbers, not assurances.
  S3. NO PER-PIECE TELLS: exemplars and a sample of test pieces pass the anti-tell list and sit inside their register's stylometric bands.
  S4. NO CROSS-PIECE SAMENESS: a batch of pieces, run through the sameness rubric, shows deliberate variation in register, structure, opening, rhythm, and close, below the rubric's sameness thresholds.
  S5. CRAFT, NOT TOPIC: the system transfers rhetorical architecture and register to current subjects without importing period diction or pretending to be a historical author; current-events accuracy is preserved (D8 guardrail satisfied).
  S6. AUDITABLE: every craft claim is grounded in cited corpus passages, every stylometric number is reproducible from the stated corpus, and the verification log shows adversarial checking. Unverifiable claims are quarantined, not shipped.
  S7. OPERATIONAL: Samuel, a no-code operator, can pick up the deliverables and produce a varied week of pieces using the palette, templates, specs, briefs, and checklists alone.

Deliver rigor over brevity. This apparatus is the core IP of the product; build it to be used daily and defended line by line.
======================================
```

## 2026-06-05 — Register palette derived (7 registers)

Partition by ETHOS strategy + emotional temperature, reconciled against genre/period/syntax. Spans 1780–2016. Load-bearing historical anchors carried.

1. **Prophetic Indictment** (moral-authority, hot, accusatory) — Banneker 1791, Kelley 1905, JFK 1962, Chavez 1978, Gandhi 1930.
2. **Reasoned Restraint** (measured civic argument, cool, visible reasoning) — Lippmann 1939, Hazlitt 1827, GAO/DOJ/NPS agency prose, McWilliams/Somin op-eds.
3. **Intimate Counsel** (confessional, warm, first-person experience as evidence) — Abigail Adams 1780, Sotomayor 2001/2022, Saujani 2018/2024, Sanders 1993.
4. **Plain Witness** (factual testimony, flat affect, particulars carry weight) — Kelley documentary stretches, Gogoi/Molla business press, Shaw encyclopedia.
5. **Lyric Awe** (contemplative wonder, mid-warm, accretive precision) — Barry/Rising Tide 2005, Barry/Great Influenza 2008, Louv 2005, Maya Lin 2000.
6. **Ironic Detachment** (deadpan satire, cool-charged, sees through pretense) — The Onion 2005, Wilson 2009, Trubek 2016, Appelbaum 2020.
7. **Ceremonial Grace** (commemorative elevation, warm-formal, consecrates) — Obama 2013, Thatcher 2004, Albright 1997, Lady Bird Johnson 1964, Dove 2016.

Distinctness check: indictment vs. ceremony both hot+formal but opposite vectors (accuse vs. consecrate); reasoned restraint vs. plain witness both cool but one foregrounds the arguer's reasoning/concession, the other suppresses the arguer behind verifiable particulars. Primary defense against cross-piece AI sameness = rotate registers across a batch.