---
created: 2026-06-11
updated: 2026-06-11
tags: [conversation, caught-up-ai]
---

# 2026-06-11 - Quick Opener Prompt

## What happened
- Samuel asked for a paste-ready prompt to build Openers on a whim, outside formal batch runs.
- Built [[caughtupai-quickprompt-V1]] in 10_Projects/Caught Up AI/, a companion to [[caughtupai-sampleprompt-V1]].

## Design choices
- Optional inputs (TOPIC, REGISTER, COUNT, OUTPUT); all may be left blank and the engine decides.
- Defaults: 1 Opener from a real story in the last 5 days, register routed by Style-Palette, teacher + student PDFs rendered via render_opener_v2.py.
- Batch-sameness gate replaced with a recency check against the latest rendered editions in Sample-Briefs, so consecutive one-off Openers do not repeat register/template/opener/close.
- All standing rules carried over: Gate 0 neutrality + plain-knowledge, headnote first, verified fact list, controlled device vocabulary, MCQ spec with randomized keys, no em-dashes, no in-text citations.

## Also
- Prior session (general-English Base44 build) was cut off before producing anything; only file reads, nothing to salvage. That build is still open.
