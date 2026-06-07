---
created: 2026-06-06
updated: 2026-06-06
tags: [project, caught-up-ai, format, reference]
project: "[[Caught Up AI]]"
---

# Opener Print Format Spec

Print-formatting decisions for the daily [[Caught Up AI]] Opener PDFs. IMPLEMENTED in the renderer ([[render_opener_v2.py]]) on 2026-06-06. See also [[Product naming]] (Opener, teacher copy / student copy, edition).

Status (2026-06-06): built and verified on the "What the Waiting Did" sample. Teacher copy = 3 pages, Student copy = 2 pages (1 double-sided sheet per student). No orphaned headers, no atomic block split; multi-item sections (answer key, MCQ) flow across pages with each item kept whole. Two-up MCQ NOT used (Samuel: definitely no).

Implementation notes:
- Orphan-header prevention uses keepWithNext on the section-header style + the rule, NOT KeepTogether(header+block). The KeepTogether approach forced whole blocks onto the next page and ballooned the doc to 8/3 pages; keepWithNext fixed it to 3/2.
- Article paragraphs are NOT each wrapped in KeepTogether (that wasted pages). They flow with widow/orphan control (allowWidows=0, allowOrphans=0) so no single line is stranded, but a paragraph may break across a page. This is the deliberate relaxation of "keep each paragraph whole."
- Atomic units still wrapped in KeepTogether: each MCQ (stem+options), each device entry, each answer-key item, each sample response, each misconception bullet.

## Core principle

Student and teacher copies get DIFFERENT formatting rules because they print differently:

- Student copy: printed as a class set (~30, daily). Page count = real paper/toner cost. Optimize tight: 1 page ideal, 2 max.
- Teacher copy: printed once. Page count barely matters. Optimize for live-class scannability. 3-4 pages fine.

## Type

- Article body: 11pt serif, leading ~15.5pt (DECIDED 2026-06-06; keeps student copy to one page more easily). Current renderer is already 11pt.
- Student copy article only: raise leading to ~17pt for annotation room.
- All apparatus (MCQ, discussion, writing prompt, teacher notes, device explanations): 11pt serif, leading ~14.5pt.
- Headline 18pt bold. Section headers 12pt bold sans + 0.5pt rule beneath (current headers are 11pt, too weak a hierarchy).
- Footer / running header: 7.5-8pt grey.
- Note: at 0.9in side margins an 11pt line runs ~95 chars (wider than the ideal 65-75). Accepted as the cost of staying on one page; do not narrow margins (that adds pages).

## No-split rules (keep whole on one page)

- Each MCQ: stem + all four options together.
- Each device entry: name + quoted phrase + purpose together.
- Each answer-key item; each sample response.
- Misconceptions list; AP-alignment paragraph; writing prompt.
- Section header never the last flowable on a page (bind to first block beneath).

## Article exception (cannot obey no-split)

- Passage may flow across pages.
- Each paragraph stays intact (no mid-sentence split across a break).
- Do not orphan the article's section header; avoid a lone trailing line.

## Print-medium rules

- Assume black-and-white laser. Keep the yellow highlight (#FFF3A0) light enough to read as faint grey. Never use color as the only signal (device name is always printed in brackets, so B&W loses nothing).
- Build Student and Teacher as SEPARATE PDF files (PDF renderer already does; HTML version does not). Lets teacher print student x30, teacher x1 without page-range fiddling.
- Running header on pages 2+: "Caught Up AI Opener . [date] . [headline] . Teacher/Student copy", small grey, so dropped/mixed stacks stay identifiable.

## Page-count strategy

- Student target: 1 page (~450-word article + 2 MCQ + 2 discussion + 1 prompt), 2 max.
- Avoid the orphan-page problem (2-3 lines onto a blank page 2): tighten spacing or trim, do not ship a near-empty page.
- Space saver: two-up MCQ options (A/B on one line, C/D on next). Optional; looks more worksheet-like.

## Open decisions before building

1. RESOLVED 2026-06-06: article body stays 11pt.
2. Two-up MCQ options: default NO (cleaner reading-page look). Add only if the student copy overflows one page.

The full paste-ready build prompt is in [[2026-06-06 - Opener print formatting spec]].
