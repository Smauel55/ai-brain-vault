---
created: 2026-06-13
updated: 2026-06-13
tags: [conversation, caught-up-ai, renderer]
project: "[[Caught Up AI]]"
---

# 2026-06-13 — Opener page-break rule (no split sections)

## Context

Samuel: some Opener sections were getting cut off at the bottom of a page (section header plus a line or two, then the body spilling overleaf). Wanted a rule: if a section will not fit, it starts on a new page.

## Key points

- Fixed in `Sample-Briefs/render_opener_v2.py`, the `sec()` helper (renderer source of truth).
- Each section (header + rule + all blocks) is now wrapped in one `KeepTogether`, so it bumps to the next page whole instead of being split. The article opts out (`keep_whole=False`) since it is meant to flow paragraph by paragraph.
- Trap found and fixed: the section blocks come in pre-wrapped as inner `KeepTogether` (one per MCQ item, device, etc.). `KeepTogether.wrap()` returns a sentinel height `0xffffff`, so nesting them made the section measure as astronomically tall and forced EVERY section onto its own page (teacher copy ballooned 3 -> 7 pages, pages ~75% empty). Fix: unwrap (flatten) the inner blocks before the outer `KeepTogether`, so it measures a real height and sections pack normally.
- Verified by rendering the sample piece and rasterizing with PyMuPDF: teacher copy 4 pages (was 3), every section whole, none split; student 2 pages; general-English teacher 4 pages.
- Residual cost (expected, acceptable): a section that will not fit leaves a bottom-of-page gap, and a short trailing section (e.g. alignment) can land alone on the last page. That is the honest price of never cutting a section.

## Decisions

- Keep sections whole over packing density. Sections never split across a page; minor bottom gaps are accepted.
- Flatten-then-wrap is the mechanism (avoids the nested-KeepTogether sentinel-height bug). Build signature unchanged, so the production workflow import (`build` / `randomize_answers`) is unaffected.

## Open threads

- Edge case not hit in practice: a single kept-whole section taller than a full page would split and an inner item could break mid-entry. With 2 MCQs and a controlled device list, no section approaches a page, so this is latent only.
