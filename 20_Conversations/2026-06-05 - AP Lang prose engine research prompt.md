---
created: 2026-06-05
updated: 2026-06-05
tags: [conversation, caught-up-ai, content-engine]
---

# 2026-06-05 - AP Lang prose engine research prompt

## Context
- Paid-writer / commissioning path effectively off the table (cost + earlier ruling). Samuel leaning to FULL AI-GENERATION: Claude writes each piece from scratch off verified facts (facts are not copyrightable), not reproducing or paraphrasing source prose.
- This sidesteps the licensing wall (the whole blocker was reproducing others' text) and moves the main risk to editorial: factual accuracy plus the "AI prose reads same-y / detectable" problem. See [[feedback_ai_writing_formulaic]].

## What we did
- Samuel asked for a prompt he can paste back (in ultracode) to send Claude into deep research on how the PROFESSIONAL nonfiction writers whose work the College Board selects as AP Lang exam source passages actually write, so Claude can emulate that craft with real variety.
- Clarified the target: emulate the SOURCE passages students analyze (Q2 rhetorical-analysis + Q1 synthesis sources), NOT student essays. Honest reframe baked in: there is no single "AP Lang style"; the exam spans centuries and genres, so the target is a PALETTE of registers and the success test is blind-read indistinguishability across that palette. Emulate craft, not topics.
- Built the prompt via a 10-agent workflow: ground the exam facts and real passage corpus (web) -> draft the prompt through 4 expert lenses (rhetoric scholar, stylometry, AI-tells, variety-system) -> adversarial critique -> synthesize one paste-ready commission.

## Output
- [[AP-Lang-Research-Prompt]] saved at 10_Projects/Caught Up AI/AP-Lang-Research-Prompt.md (em-dashes stripped, ASCII-normalized, ready to paste).
- The commission, when run, produces v2 of the [[Writing-Manual]]: Style-Palette, Structural-Templates, Register-Specs (qualitative + stylometric bands), Anti-Tell-List, Cross-Piece-Sameness-Rubric, Annotated-Exemplars, Generation-Briefs, Blind-Test-Protocol, and a master Prose-Engine-Research-Report.

## Open / next
- Samuel to skim the 6 knobs (register count, corpus span, blind-test scale, piece length, detector reliance, exemplar topics) and adjust before running.
- Then run the commission from the vault folder so agents can read Writing-Manual.md and write into the project folder.
- Honest caveats carried: indistinguishability is judge-dependent (pilot = noisy), verbatim AP passages are copyrighted so the work MEASURES not reproduces them, and current-events accuracy is a separate hard requirement.
