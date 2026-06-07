---
created: 2026-06-07
updated: 2026-06-07
tags: [project, caught-up-ai, testing, workflow, openers]
project: "[[Caught Up AI]]"
---

# Opener Batch Test Plan (real production dry run)

Purpose: produce a realistic batch of Openers and review each one before Samuel approaches teachers. This is the dry run that has to convince him the product works. Run as a multi-agent workflow in a fresh session (this is a token-heavy job; opt in with the workflow).

Decisions locked 2026-06-07 (Samuel):
- Fact basis is a MIX, as close to the real product as possible: most openers are real current events, live-sourced; a minority are evergreen or persona-safe. Not all invented, not all real news.
- Run as a multi-agent workflow, in a new session.
- Count: 21 recommended (3 per register, clean rotation). 28 is the heavier option (4 each). Samuel floated 15 or 30; both rotate unevenly across 7 registers, so 21 or 28 is preferred.

## The 7 registers (rotate all of them)

Ledger, Reckoning, Long Think, Open Letter, Witness Stand, Tribute, Long Look. Specs: [[Register-Specs]]. Rotating registers is the primary defense against cross-piece sameness; vary the structural opening/closing within a register too ([[Structural-Templates]]).

## Register x fact-basis matrix (21 openers, 3 each)

R = real news, live-sourced. E = evergreen or persona-safe. Fit governs the split (some registers only fit one basis).

| Register | Count | Basis | Notes |
|---|---|---|---|
| Ledger | 3 | 3R | disputed or misunderstood record; inherently news |
| Reckoning | 3 | 3R | needs a live, datable wrong and a nameable culprit |
| Long Think | 3 | 2R, 1E | a perennial theme behind a current story; one pure evergreen |
| Open Letter | 3 | 2R, 1E | real named powerful addressee held to their own stated values |
| Witness Stand | 3 | 1R, 2E | persona "I" (invented self/family OK); only hard facts must be real |
| Tribute | 3 | 2R, 1E | a real death, milestone, or dedication; one evergreen institution |
| Long Look | 3 | 1R, 2E | a marvel or how-it-works; wrong for conflict or blame |

Totals: 14 real-news, 7 evergreen/persona (about 2:1, leaning real, like the product). For 28, add one of each register (keep the R/E lean).

## Per-opener pipeline (each opener runs this independently)

1. Assign register, fact basis (R/E), and a candidate topic from the matrix. No two openers on the same story.
2. SOURCE.
   - R: live web research. Build a numbered fact list ([[Accuracy-Guardrail]]): every load-bearing fact has 2+ independent sources, primary where possible. Flag single-source or still-developing facts and write around them. Draft only from the fact list, never from a source's sentences.
   - E: assemble stable, well-established facts, or invented persona material (persona/family invention is fine per [[feedback_persona_fabrication]]; hard facts must still be real).
3. DRAFT the passage in the assigned register: hit the [[Register-Specs]] bands, vary the opening/closing ([[Structural-Templates]]), apply the [[Anti-Tell-List]] friction layer (asymmetry, one inert detail, no tidy-button-every-paragraph, no mirror-the-opening close, no signposting). Mark 4 to 6 genuinely-present devices with [[n]]...[[/n]], names ONLY from [[Rhetorical-Device-Vocabulary]] (understatement/litotes is removed; allusions must be widely recognizable).
4. APPARATUS: 2 MCQs targeting DIFFERENT reading skills ([[MCQ-Construction-Spec]]); each distractor fails by a named trap; exactly one defensibly-best answer; rationales reference distractors by CONTENT not letter. FRQ by fit (Q2 for any; Q3 only for argument-bearing passages; never Q1 for a single-source opener). 2 discussion questions, 2 sample responses, 3 to 4 misconceptions, AP alignment, and a one-to-two-line PURPOSE for each device.
5. VERIFY (separate adversarial agents, do not let the drafter grade itself):
   - Accuracy: every name, number, date, quote, and causal claim true and traceable; no orphan facts.
   - Devices: each label is correct and genuinely present; look-alikes right (anaphora vs parallelism, simile vs metaphor, asyndeton vs polysyndeton).
   - MCQ: exactly one best answer; no free-elimination distractor; parallel grammar; two different skills.
   - Mechanical: zero em-dashes, zero emojis; anti-tell sweep; register bands in range.
   Return pass or fail with specific fixes; re-draft on fail.
6. EMIT the structured opener (schema below).

## Cross-batch checks (after all openers, before render)

- Register rotation even; no register over-used; no two adjacent same register.
- Sentence-length means, opener-type splits, and device density SPREAD across pieces (not all clustered at one value); this is the cross-piece sameness gate ([[Cross-Piece-Sameness-Rubric]]).
- Topics all distinct.

## Output schema (must match render_opener_v2.build)

```
{
 "base": "Caught Up AI Opener - YYYY-MM-DD - <Headline> (<Register>)",
 "edition": "Batch test edition",
 "date": "Weekday, Month D, YYYY",
 "headline": "<Headline>",
 "body": ["para 1 ...", "para 2 with [[1]]marked span[[/1]] ...", ...],
 "devices": [{"para": 1, "device": "<from controlled list>", "purpose": "1-2 lines"}, ...],
 "mcq": [
   {"stem": "...", "options": ["...","...","...","..."], "answer": "A", "rationale": "content-referenced"},
   {"stem": "...", "options": ["...","...","...","..."], "answer": "A", "rationale": "content-referenced"}
 ],
 "discussion": ["q1", "q2"],
 "sample_responses": ["r1", "r2"],
 "writing": {"type": "homework or extended in-class, Q2 rhetorical analysis | Q3 argument", "text": "..."},
 "misconceptions": ["m1","m2","m3"],
 "ap_alignment": "..."
}
```

Notes: device n in body matches devices[n-1]; "answer" is the letter of the correct option AS AUTHORED (render_opener_v2.randomize_answers shuffles options and recomputes the letter at render, so keys land randomly like the AP exam). Rationales must be content-referenced so the shuffle cannot break them.

## Render

Collect all opener dicts, then render each as teacher + student PDFs via render_opener_v2.build, calling render_opener_v2.randomize_answers(piece) ONCE per piece before building both roles (keeps teacher key aligned with student option order). Report per opener: page counts and the two answer letters. Confirm no section is split and no header orphaned (already handled by the layout engine, see [[Opener-Print-Format-Spec]]).

## Samuel's per-opener review checklist

- Register fit: does the voice match the story and the register spec?
- Prose: reads human, not machine-smooth (friction present, not over-balanced)?
- Devices: every label correct and actually present?
- MCQs: one clearly-best answer, no give-away distractor, two different skills?
- FRQ: type fits what the passage does?
- Facts: every hard fact true and sourced (spot-check the real-news ones)?
- Format: nothing split across pages, sensible length.

## Related

[[Register-Specs]], [[Anti-Tell-List]], [[Rhetorical-Device-Vocabulary]], [[MCQ-Construction-Spec]], [[Accuracy-Guardrail]], [[Structural-Templates]], [[Cross-Piece-Sameness-Rubric]], [[Opener-Print-Format-Spec]], [[feedback_persona_fabrication]], [[Caught Up AI]].
