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

## Build (same day)

- Samuel chose 11pt article and a firm NO on two-up MCQ.
- [[render_opener_v2.py]] updated: stronger 12pt section headers with a thin rule, role-based article leading (teacher 15.5, student 17 for annotation room), tighter apparatus leading (14.5), running header on pages 2+, separate teacher/student PDFs, B&W-safe yellow highlight kept.
- First render came out 8 pages (teacher) / 3 (student): KeepTogether on every header+block and every article paragraph forced early page breaks. Fixed by switching to keepWithNext for headers and widow/orphan control for article paragraphs. Result: teacher 3 pages, student 2 (1 double-sided sheet).
- Verified visually (PyMuPDF render): no orphaned headers, no atomic block split, multi-item sections flow with each item whole.

## Action items

- [ ] None open. Renderer is ready for the next edition's content.

## Open threads

- Student copy is 2 pages for a ~470-word article; 1 page is not realistic without cutting content. Lever if ever wanted: drop student article leading from 17 back to 15.5 (loses annotation room).
