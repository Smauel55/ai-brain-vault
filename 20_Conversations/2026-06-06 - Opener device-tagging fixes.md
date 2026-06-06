---
created: 2026-06-06
updated: 2026-06-06
tags: [conversation, caught-up-ai, opener, rhetoric]
---

# 2026-06-06 - Opener device-tagging fixes

New draft of the "What the Waiting Did" (Long Think) [[Caught Up AI]] opener.

## What Samuel asked for
- Cleaner, concise draft integrating prior work.
- Highlight color in yellow (was light blue).
- Fix rhetorical-device highlighting: drafts only marked the START of a device.
  - Volta tagged as just "And yet" — the connective, not the turn.
  - Concession/refutation tagged as "it would be foolish to pretend otherwise" — which is neither.
- Wanted pushback if I disagreed.

## What I concluded
- Agreed on both. "And yet" is only the signal; volta is the clause after it. "It would be foolish to pretend otherwise" only asserts the grant is sincere; the real concession is the substance ("we were right to want it").
- One nuance: concession and its refutation straddle the para 2 -> para 3 break, and the refutation sits on the same clause as the volta. Anchored each highlight on a distinct span; purpose notes cross-reference.

## Changes made
- `Sample-Briefs/render_opener_v2.py`: HL_BG -> yellow (#FFF3A0); concession span moved to "We bought back the time... right to want it"; volta span extended to full turn clause; rewrote both purpose notes; added two teacher misconceptions (And-yet trap, foolish-to-pretend trap). Regenerated both PDFs.
- `Rhetorical-Device-Vocabulary.md`: added durable rule — highlight the whole device, not its trigger word.

## Open
- Prose left untouched (defects were tagging-only). Offered a prose-tightening pass if wanted.
