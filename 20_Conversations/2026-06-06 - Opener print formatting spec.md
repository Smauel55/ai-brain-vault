---
created: 2026-06-06
updated: 2026-06-06
tags: [conversation, caught-up-ai, format]
project: "[[Caught Up AI]]"
---

# 2026-06-06 — Opener print formatting spec

## Context

Samuel asked for a detailed synopsis of how best to format the Opener for printing (font size, page fitting, no splitting sections across pages) plus a reusable prompt to have Claude build it.

## Key points

- Grounded in the real renderer [[render_opener_v2.py]], not a generic template.
- Core insight: student and teacher copies need DIFFERENT rules. Student = class set, page count is a cost, optimize tight (1 page). Teacher = single copy, optimize for scannability, 3-4 pages fine.
- The "no section split across pages" rule works for bounded blocks (MCQ, device entry, answer key, sample response, misconceptions) but the ARTICLE cannot obey it; it must flow across pages with paragraphs kept intact.
- Print reality: assume B&W laser; keep highlight light; never use color as only signal; build student/teacher as separate files; add a running header on pages 2+.

## Decisions

- Full format spec captured in [[Opener-Print-Format-Spec]] (type sizes, no-split rules, article exception, print rules, page-count strategy).
- Two open decisions left to Samuel: 12pt vs 11pt article body; two-up MCQ options yes/no.
- Delivered a paste-ready build prompt (in transcript) that modifies render_opener_v2.py and ends with verification steps (page counts, no orphaned headers, no split blocks).
- Not implemented yet; awaiting Samuel's go / the two decisions.

## Action items

- [ ] Samuel — decide 12pt vs 11pt article and two-up MCQ, then send the build prompt (or ask Claude to run it on the sample).

## Open threads

- Whether to render the "What the Waiting Did" sample now as a before/after, or adjust the spec first.
