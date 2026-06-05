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

Finalists (pre-research): licensing vs AI-with-editing. Reframed by the cost research below.

## 2026-06-04 cost research and reframe

Researched the three relaxations with concrete numbers (3 parallel research agents; full sourced reports in the session). Headline: commissioning original work-for-hire content moves to front-runner.

- LICENSING: price is the smaller problem, rights are the dealbreaker. Major publishers (NYT/WSJ/WaPo/AP/Reuters/Tribune) are effectively closed: standard reprint licenses are verbatim-only (AP: "used exactly as written"); inline annotation is a derivative work sold only as bespoke, lawyer-negotiated enterprise contracts, plus an author moral-rights/integrity gate. Not obtainable by a solo founder for a $20/mo product. The one commercial precedent that reproduces AND modifies current journalism is Newsela (pays 175+ publishers for adaptation rights, rewrites in-house, raised $150M+); not copyable solo. Only surviving licensing channel: direct from independent/Substack writers who own their rights and can grant reproduce+annotate+commercial in one contract, roughly $150-600/piece (about $1,650/mo at 2-3x/wk, up to $8,800/mo daily). Turns the engine into a weekly rights-acquisition + contracting operation.
- FREE POOL at reduced cadence: dropping cadence does NOT solve sourcing. Constraint is supply of license-clean (PD/CC0/CC-BY) current, argument-driven, classroom-safe prose, which does not grow because fewer pieces are needed. Only one scaled CC-BY op-ed newsroom (Global Voices, ~1-3 usable/wk, international skew). The deep free vein is US federal public-domain text (speeches, testimony, SCOTUS opinions): rhetorically excellent, current, freely annotatable, but inherently partisan = classroom-neutrality/adoption risk. Honest free cadence: 1x/wk comfortable, 2x/wk strained (needs US-gov PD load-bearing + weekly neutrality calls), 3x/wk breaks. Free-only does not reach a clean safe 3x/wk.
- COMMISSION ORIGINALS (work-for-hire): the research promotes this to front-runner. Solves all four hard constraints at once: real human authorship (passes the blind test), full ownership (annotate freely, no rights problem), current, and classroom-neutral (you pick topics). Cost is modest and flat in user count: ~$100/piece mid (work-for-hire, 400-600 wds; ~$50 budget, ~$225 top journalist). 2x/wk about $860/mo, 3x/wk about $1,300/mo mid; break-even ~65 subs (mid 3x/wk) or ~22 subs (budget 2x/wk). Real proof: The Juice (daily classroom current-events) runs exactly this, original journalist+educator content, leveled, 6am delivery, explicitly no verbatim reposting; owns everything so reproduce/annotate/level never hits a rights wall. The reduced-cadence lever matters HERE (makes commissioning affordable pre-revenue), not for the free pool.

REFRAMED FINALISTS:
- Front-runner: commission original work-for-hire content at 2-3x/wk, supplemented by free PD/Global Voices and a canon "classic" slot on off-days. Real + owned + current + classroom-safe + affordable, the only config that satisfies all.
- AI-with-editing is now the cost-saver variant of commissioning (AI drafts, paid human rewrites/fact-checks to quality). The 2026-06-04 formula problem shows even rules-guided AI drifts to a detectable house style, so the AI path really means paying for substantial human rewriting, which converges toward commissioning.
- Licensing survives only as direct-from-independent-writers; commissioning dominates it (topic/neutrality/format control licensing lacks).

Blind test still useful but its question shifts: not "AI vs real to decide if we can go cheap-AI" but "does authentic authorship move teachers at all?" If yes, commission real; if teachers truly can't tell and don't care, lean on AI-draft + light human edit. Either way, the real-content path (commissioning) is now known to be financially viable.

## Next step

Blind teacher test in discovery: unlabeled AI brief vs real brief; does real authorship matter? Likely settles the engine.

Status 2026-06-04: AI side built. Wrote the source-article [[Writing-Manual]] (reverse-engineered from the released AP Lang exam corpus) and 3 AI essays to it ([[Blind-Test-Essays]]), each in its own Google Doc on the Northwestern account. Decision: Claude writes the AI side only; Samuel supplies currently-published real op-eds to pair, strips labels, randomizes order. Remaining: Samuel reviews and owns the essays, selects and pairs the real comparators, builds the scoring instrument (teacher guesses AI vs real, and which they would rather teach), then runs it in discovery. Detail in [[2026-06-04 - Product design and content sourcing]] and [[2026-06-04 - AP Lang writing manual and blind-test essays]].
