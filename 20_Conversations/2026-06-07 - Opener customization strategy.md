---
created: 2026-06-07
updated: 2026-06-07
tags: [conversation, product]
project: "[[Caught Up AI]]"
---

# 2026-06-07 — Opener customization strategy

## Context

Samuel raised an unaddressed product question: should Openers be customizable by difficulty level and by political intensity? Options he floated: scrap it (one streamlined version), full customization, or a middle (5-10 openers/day spanning levels). Asked for a recommendation.

## Key points

- The two axes are different kinds of things and need different answers; lumping them together is the trap.
- POLITICAL INTENSITY = a safety/trust gate, not a feature. One bad topic under a teacher's name (e.g. conservative district + hot-button framing) is an existential churn/trust risk. Must be controlled, but as a low-cardinality SETTING set once at signup (~2 tiers: Neutral/apolitical vs Includes civic/current-events), not parallel content streams. It is mostly topic ROUTING, not a second pipeline, because most of the topic universe is naturally low-intensity and AP Lang device analysis works on any subject.
- DIFFICULTY = effectively a different product. AP Lang level is close to fixed and the prose engine is already tuned to it. Offering AP/honors/regular/middle-school = building 4 products and diluting the one thing already invested in. Pick one lane (AP Lang) at launch; difficulty tiers are a v2 expansion play once paying AP teachers ask.
- The 5-10/day buffet is the wrong middle: (1) it breaks the core ritual (open inbox, print today's, done) by handing curation back to the teacher; (2) it multiplies QA load 5-10x at the exact moment QA (accuracy + AI-sameness) is the #1 risk. Under full AI-generation, volume is cheap (compute, not licensing) but VERIFICATION is the bottleneck, so every variant is a recurring QA tax, not a one-time build.
- Cheaper way to serve lower levels without a second product: keep the same passage, add an optional SCAFFOLDING layer (glossary of hard terms, FRQ sentence starters, vocab pre-list). Same content, more support; testable before committing.

## Decisions

- DECIDED (2026-06-07): No difficulty setting. SCRAPPED for now; revisit only after the AP Lang market is fully saturated (Samuel does not see that happening in the near future). Launch is a single AP Lang difficulty.
- DECIDED (2026-06-07): Adopt the political-intensity dial as the one customization axis. To be designed next. (Direction: low-cardinality setting at signup, default neutral, implemented as topic routing not a parallel pipeline.)
- Rejected: the 5-10/day buffet (breaks print-and-go ritual + multiplies QA).

## Action items

- [ ] Design the political-intensity dial (tier count + wording, topic-bucket routing). Next work item.

## Open threads

- Whether scaffolding-layer demand is real (test with users).
- Exact wording/number of political-intensity tiers.
