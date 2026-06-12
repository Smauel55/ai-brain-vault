---
created: 2026-06-12
updated: 2026-06-12
tags: [conversation, caught-up-ai, production, openers]
---

# 2026-06-12 - Production run, 3 Openers

Acted as the [[Caught Up AI]] production system end to end: loaded the engine, routed, fact-checked, drafted, gated, and rendered 3 finished Openers to PDF. All inputs blank (I chose stories, registers, count 3, PDF output).

## What shipped (all 2026-06-12, in Sample-Briefs/)
- **The Seam Between Day and Night** (The Long Look) - JWST reads the day/night atmosphere of exoplanet WASP-121 b. Template: Accumulation (3). Open: flat-fact. Close: culminating accumulation. Writing: Q2.
- **Stored, Not Kept** (The Long Think) - Apple's WWDC 2026 move to remove untended apps, turned into a reflection on the difference between making a thing and keeping it. Template: Concession-then-Rebuttal (1). Open: concede-first. Close: inward turn. Writing: Q3.
- **The Voice That Carried** (The Tribute) - Peabo Bryson, died June 2 2026, age 75. Template: Narrative-into-Claim (5). Open: in-scene. Close: placement/benediction. Writing: Q2.

## Process notes
- Routed away from the last batch (Ledger, Open Letter, Reckoning; templates 10/8/2) into the four fresh registers; picked 3 with no shared register/template/opener/close.
- Fact-finding delegated to 3 cheaper subagents (one per register); drafting and Gate 0 kept on the strongest model. All single-sourced facts the researchers flagged were dropped before drafting.
- Rendered via a one-off driver (`_run_2026-06-12.py` + `_pieces_2026-06-12.json`) importing `build` / `randomize_answers`; `render_opener_v2.py` untouched. Answer keys randomized (B/C, A/B, A/C).
- Rotation history appended to `editions-log.tsv`.

## Detail map
- Pieces dict: `Sample-Briefs/_pieces_2026-06-12.json`
- Driver: `Sample-Briefs/_run_2026-06-12.py`
- PDFs: 6 files (teacher + student per piece) in `Sample-Briefs/`
