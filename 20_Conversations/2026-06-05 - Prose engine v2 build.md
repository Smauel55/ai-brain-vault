---
created: 2026-06-05
updated: 2026-06-05
tags: [conversation, caught-up-ai, writing, prose-engine]
project: "[[Caught Up AI]]"
---

# 2026-06-05 — Prose engine v2 build

## Context

- Ran the locked deep-research commission from [[AP-Lang-Research-Prompt]] as an ultracode multi-agent workflow. Goal: replace the single-template v1 [[Writing-Manual]] with a full register palette plus stylometric and detectability layers, so full-AI-generation pieces read like the professional nonfiction source passages on the AP Lang exam.

## Key points

- 56-agent workflow, ~57 minutes: corpus verification, register-palette derivation (3 proposals reconciled), per-register craft + stylometry analysis, Layer-C adversary research, adversarial verification, deliverable writing, exemplars, blind-test proxy pilot, report.
- All 10 deliverables written to `10_Projects/Caught Up AI/`: [[Style-Palette]], [[Structural-Templates]], [[Register-Specs]], [[Anti-Tell-List]], [[Cross-Piece-Sameness-Rubric]], [[Accuracy-Guardrail]], [[Annotated-Exemplars]], [[Blind-Test-Protocol]], [[Generation-Briefs]], [[Prose-Engine-Research-Report]].
- Palette of 7 registers: The Ledger, The Open Letter, The Reckoning, The Tribute, The Long Think, The Witness Stand, The Long Look. The two near-merge pairs were hard-gated by the distinctness audit.
- Corpus: 49 entries. Provenance re-audit found zero false exam-confirmations; all three v1 corrections held; only minor date/slot refinements. Stylometric bands recomputed for 4 public-domain registers and held.

## Decisions

- v1 [[Writing-Manual]] is kept (not overwritten) and now carries a supersession note; v2 is the production apparatus, v1 is the inherited foundation layer (the hard bans still hold).
- The automated proxy pilot is a pre-screen only, never the pass signal. The decisive test is the human AP-Lang-teacher panel specified in [[Blind-Test-Protocol]].

## Findings worth carrying

- Proxy blind read went 7/7 (machine always identified), but it is confounded: the exemplars still carry `[PLACEHOLDER]` tags (a dead giveaway) and topic/era differs from the genuine comparison passages. Not a clean indistinguishability result.
- Band check: only 2 of 8 exemplars sat fully inside their claimed register bands; 6 drifted on rhythm, openers, or length pole. This is the real, useful signal and the first calibration target.
- One material verification correction: arXiv 2506.21817 was mis-cited as evidence for connective overuse / uniform sentence length (it is actually about spiking content words). Logged in the verification log.

## Action items

- [ ] Samuel — read [[Style-Palette]], [[Register-Specs]], [[Generation-Briefs]], [[Annotated-Exemplars]].
- [ ] Samuel — calibrate the 6 out-of-band exemplars back into band; feed fixes into [[Register-Specs]] and [[Anti-Tell-List]] (the iteration loop).
- [ ] Samuel — to run the real blind test: produce placeholder-free pieces with verified facts, build topic-matched pairs, recruit AP-Lang teacher judges (ties to the existing teacher list / [[Outreach-Tracker-2026-05]]).

## New knowledge to file

- Already captured in feedback memory: AI writing reads formulaic when rule-driven (cross-piece sameness is its own tell). The new [[Cross-Piece-Sameness-Rubric]] operationalizes the defense.

## Open threads

- Whether to do a cleaner self-administered proxy (placeholder-neutralized pieces, topic-matched modern comparison passages) before spending human-judge time, or go straight to the human panel.
- Accuracy pipeline (fact sourcing/verification per [[Accuracy-Guardrail]]) still needs wiring before any piece publishes.
