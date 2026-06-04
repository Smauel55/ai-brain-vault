---
created: 2026-06-04
updated: 2026-06-04
tags: [conversation, caught-up-ai, content-sourcing, blind-test]
---

# 2026-06-04 - AP Lang writing manual and blind-test essays

Continuation of the content-engine work. Built the AI side of the blind teacher test. See [[2026-06-04 - Product design and content sourcing]] for the engine decision that prompted it.

## Decisions
- Blind test setup: Claude writes the AI essays only. Samuel supplies the real comparators (currently-published op-eds he selects), pairs by topic and register, strips all labels, randomizes order before showing teachers. Reason: he is the AP Lang quality bar, and current real op-eds make the test valid and avoid reproducing copyrighted text in Drive.
- Topic lane: safe + pointed (evergreen, non-partisan strong arguments).
- Samuel added a rule to the manual: ban monotone syntax, not just monotone sentence length. Blend simple/compound/complex sentences and vary openings, for the humanity of the piece.

## Produced
- Research on the released AP Lang exam corpus (Q2 rhetorical-analysis passages 2005-2024, verbatim where available). Corrections carried forward: Chavez nonviolence = 2015 Q2 (not a 2014 argument prompt); Orwell/Didion/Staples/Carson/MLK are teaching mentor texts, not exam passages.
- [[Writing-Manual]] (10_Projects/Caught Up AI/Writing-Manual.md). Reverse-engineered register: open/build/close spine, one structural engine, long-vs-short plus syntactic-variety rhythm rules, earned-device palette, AI-tell blocklist (no em-dashes, banned diction and constructions), markability test, paste-ready generation brief.
- 3 AI essays written to the manual, each in its own Google Doc on the Northwestern account. Backup: [[Blind-Test-Essays]].
  - Essay 1, Passion Myth: https://docs.google.com/document/d/1LtX4RMpRsmLxlpLXzfNDGu6Iv1bskUipNQGSulaglA8/edit
  - Essay 2, Optimized Life: https://docs.google.com/document/d/13PahuIvP7U9_62SjWlJKg67hHAzst7kF4iDTwmO7cRo/edit
  - Essay 3, True Crime: https://docs.google.com/document/d/1JG2A8KbkFemIU82BCEfnBdUdbnhwd86JnwUHsk8Q0qY/edit

## Open / next
- Samuel reviews and owns the three essays (must be able to defend every line as if he wrote it).
- Select and pair the real op-eds; build the scoring instrument (teacher guesses AI vs real, plus which they would rather teach and why).
- Run inside customer discovery. Result likely settles the content engine (license real vs AI-with-editing).
