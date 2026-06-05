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

Blind test still useful but its question shifts: not "AI vs real to decide if we can go cheap-AI" but "does authentic authorship move teachers at all?" If yes, commission real; if teachers truly can't tell and don't care, lean on AI-draft + light human edit. Either way, the real-content path (commissioning) is now known to be financially viable. [Superseded: commissioning later ruled out by Samuel, see next section.]

## 2026-06-04 (later) - commissioning out; "leave the article untouched" idea (candidate D-009)

- Samuel ruled OUT commissioning writers (not a possibility; reason not specified).
- New idea: do NOT mark up the article inline. Reproduce it verbatim and untouched, and put the rhetorical-device locations in a SEPARATE apparatus in the teacher brief (quote the phrase, give its location, label it, add the analysis).
- Why it matters: the structural blocker was MODIFYING the article (inline markup = derivative work; derivative rights are bespoke and effectively unbuyable, per D-006). Leaving the article untouched means the product needs only REPRODUCTION rights, which are normal and purchasable. Licensing moves from "structurally impossible" to "a question of price and terms."
- Unlocks (preliminary read): (1) mainstream publishers via standard reprint/syndication licenses, because the "used exactly as written" restriction is now satisfied, not violated, so AP/Reuters/Tribune/per-article reprints become a COST question, not a rights wall; (2) CC-BY-ND sources reopen (ND permits verbatim commercial reproduction; clean article + separate apparatus = a collection, not a derivative), with the prize being The Conversation (current, expert, classroom-safe argument pieces) IF its contract terms allow a paid product; (3) minor: CC-BY-SA usable without copyleft attaching to the apparatus.
- Does NOT fix: NonCommercial sources stay out (paid product); reproduction still costs money for copyrighted work (truly free stays PD/CC0/CC-BY plus maybe ND); small pedagogy/UX tradeoff (device map beside a clean article instead of inline highlights).
- To verify before relying: (a) the "separate apparatus is not a derivative" line against each source's actual terms and ideally a lawyer, and keep the article and apparatus physically separate, not interleaved; (b) the ND contract overlays (The Conversation, Aeon, Knowable add no-sell/no-paywall/agreement terms; The Conversation is the swing factor for the free pool); (c) reprint pricing at a daily/near-daily cadence.
- If The Conversation's terms allow a paid product, that may be the engine on its own: free, current, real, classroom-safe, legally clean.

## 2026-06-04 verification result (31-agent workflow)

VERDICT: legal model is SOUND WITH CONDITIONS. It is a litigation thesis, not settled fact: the load-bearing point is that a verbatim article + a physically separate, non-interleaved apparatus = a collection, not a derivative (17 USC 106(2)). Well-reasoned but untested on these facts, so it needs a written copyright-attorney opinion before launch. Full memo: [[Licensing-Verification]].

- Opens new avenues? Yes but narrow and conditional. Genuinely unlocks (if the thesis holds): CC-BY-ND for verbatim paid reuse; standard reprint/syndication licenses become the right SHAPE (but unaffordable, below); direct-from-writer licensing. Reproduction + distribution rights stay fully engaged, so copyrighted sources still need a paid reproduction license; fair use does not rescue full verbatim commercial copying.
- THE CONVERSATION DOES NOT SWING FREE. Derivative problem solved, but The Conversation and Knowable stay closed on a SECOND, independent CONTRACT overlay (no selling separately, no systematic republishing) the apparatus design does nothing to clear; The Conversation also mandates a 1x1 tracking pixel = student-privacy problem in classroom email. Copyright was not the only lock.
- Actually-newly-clean CC-BY-ND pool is thin: Singularity Hub (provisional; guidelines page 404) and OpenMind (conditional; NC-dead if a subscription-outlet waiver fails). Neither is a confirmed pillar.
- Still closed: ProPublica (NC), NYT/WaPo/WSJ general (terms), CC-BY-SA (ShareAlike).
- PRICING: free-in-cash = US federal PD (only fully confirmed base today), Global Voices (free, contact-gated, Left lean), + the two provisionals. Real cost of the free path = curation LABOR ~5-10 hrs/wk. Paid avenues all poor for a small budget: AP smallest tier ~$1,600/mo; Tribune high-hundreds to low-thousands; NYT/WaPo/WSJ per-article reprint ~$9-20k/yr at daily; Reuters enterprise; CCC a rail only. Direct-from-writer is the only paid option that scales to 1/wk; real price needs a blind test. Unit econ: ~$14 net/sub; ~16-46 subs fund one writer-piece/wk (tens, not hundreds).
- 3-5/WEEK? Not on free alone. Honest all-free floor ~2/wk, 3 typical, 4-5 only in good weeks; binding constraint is the four-filter intersection (current + ~400 wds + genuinely argument-driven + classroom-safe/neutral) and only federal PD is confirmed today. Free + ~1 paid writer/wk -> steadier 3-4/wk. A reliable 5-day product is not deliverable on free content. DO NOT advertise a cadence until a 2-4 week real pull counts survivors.
- RECOMMENDED ENGINE: federal PD base (confirmed) + Global Voices and Singularity Hub once gates cleared + OpenMind as upside + ~1 direct-from-writer piece/wk later (after a blind test sets price) to reach 3-4/wk. Format discipline is load-bearing: bit-for-bit article, ZERO inline labels, separate apparatus, short-phrase quotes keyed by location only.
- NEXT STEPS (ordered): (1) volume pressure-test FIRST (2-4 wk real pull, count survivors; no cadence claim before this); (2) clear the 3 free gates (Global Voices contact, re-pull Singularity Hub guidelines, OpenMind classification email); (3) blind-test the writer channel for real prices; (4) scope state/local govt text + institutional CC0; (5) build the apparatus template; (6) HARD LAUNCH GATE: written copyright-attorney opinion on collection-not-derivative + that bare CC does not override publisher contract overlays.

## Next step

Blind teacher test in discovery: unlabeled AI brief vs real brief; does real authorship matter? Likely settles the engine.

Status 2026-06-04: AI side built. Wrote the source-article [[Writing-Manual]] (reverse-engineered from the released AP Lang exam corpus) and 3 AI essays to it ([[Blind-Test-Essays]]), each in its own Google Doc on the Northwestern account. Decision: Claude writes the AI side only; Samuel supplies currently-published real op-eds to pair, strips labels, randomizes order. Remaining: Samuel reviews and owns the essays, selects and pairs the real comparators, builds the scoring instrument (teacher guesses AI vs real, and which they would rather teach), then runs it in discovery. Detail in [[2026-06-04 - Product design and content sourcing]] and [[2026-06-04 - AP Lang writing manual and blind-test essays]].
