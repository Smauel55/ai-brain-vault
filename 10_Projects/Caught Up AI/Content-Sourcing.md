---
created: 2026-06-04
updated: 2026-06-04
tags: [project, caught-up-ai, content-sourcing]
project: "[[Caught Up AI]]"
---

# Caught Up AI - Content Sourcing

Living state of the "where does the daily article come from" question. This gates the whole product. Worked 2026-06-04 to the point of an open engine decision.

## The constraint stack

The daily article must be reproduced in full in the email, annotated inline (teacher version marks rhetorical devices in the text), sold (paid subscription), current, classroom-safe, and ~350-450 words.

## What is settled

- Link / point-to-source model: rejected (D-005). Markup cannot live on a remote article.
- Usable licenses (verified): Public Domain, CC0, CC-BY only. CC-BY-SA off (ShareAlike leaks the paid version). NC and ND both fatal.
- Free current pool: too thin for a daily cadence (verified). Global Voices (CC BY 3.0) is the only genuine current qualifying source (~1-2 usable/wk). The 7 vs 30 day window is irrelevant.
- Canon as backbone: rejected (D-008, reaffirms D-004). Supplement only.
- Full verified source table: [[Caught Up AI - content licensing filter]].

## The open decision (the engine)

Cannot keep real + not-commissioned + current + daily + cheap + annotatable. Relax one:
- Cost: license real op-eds (annotation rights hard, enterprise pricing).
- "No commissioning": commission owned originals (~$50-300/piece; flat in user count).
- "No AI": AI plus a human editor.
- "Daily": free 2-3x/week (Global Voices + current public-domain government rhetoric).

Finalists: licensing vs AI-with-editing.

## Next step

Blind teacher test in discovery: unlabeled AI brief vs real brief; does real authorship matter? Likely settles the engine. Detail in [[2026-06-04 - Product design and content sourcing]].
