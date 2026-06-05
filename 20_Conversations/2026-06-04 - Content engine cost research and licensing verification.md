---
created: 2026-06-04
updated: 2026-06-04
tags: [conversation, caught-up-ai, content-sourcing, licensing, blind-test]
---

# 2026-06-04 - Content engine: cost research, D-009, licensing verification

Continuation of the [[Caught Up AI]] content-engine work. Picked up from the open engine decision, designed the blind test, built a writing manual and AI essays, then ran cost research and a 31-agent verification that reshaped the whole sourcing picture. See also [[2026-06-04 - AP Lang writing manual and blind-test essays]] and [[2026-06-04 - Product design and content sourcing]].

## Arc of the session
- Recapped the engine options (license real op-eds, AI-with-editing, drop cadence, commission), then designed the blind teacher test (AI brief vs real brief; does authentic authorship matter).
- Built [[Writing-Manual]] from the released AP Lang exam corpus, and wrote 3 AI essays to it ([[Blind-Test-Essays]], each in a Google Doc on the Northwestern account).
- Samuel rejected the essays as too formulaic (same start, end, cadence across all three). Logged as feedback (rule-driven AI prose reads formulaic across pieces). This became evidence against the pure-AI path.
- Ran cost research: commissioning original work-for-hire content briefly emerged as front-runner (~$860-1,300/mo at 2-3x/wk, The Juice as proof model). Samuel then ruled commissioning OUT.
- Samuel proposed D-009: do NOT mark up the article inline; reproduce it verbatim and put rhetorical-device locations in a SEPARATE apparatus, so the product needs only reproduction rights, not derivative rights.
- Ran a 31-agent adversarial verification workflow on D-009.

## Verdict (D-009 verification)
- Legal model is SOUND WITH CONDITIONS: verbatim article + physically separate, non-interleaved apparatus = a collection, not a derivative (17 USC 106(2)). Well-reasoned but untested on these facts, so it needs a written copyright-attorney opinion before launch (hard gate).
- Opens new avenues but narrow/conditional: CC-BY-ND for verbatim paid reuse, standard reprint licenses become the right shape (but unaffordable for a small budget), direct-from-writer licensing. Reproduction + distribution rights still engaged; fair use does not rescue full verbatim commercial copying.
- The Conversation and Knowable stay CLOSED on a separate CONTRACT overlay (no selling separately, no systematic republishing), not copyright; The Conversation also mandates a tracking pixel (student-privacy). The hoped-for swing factor does not swing free.
- Newly-clean CC-BY-ND pool is thin: Singularity Hub (provisional, guidelines 404) and OpenMind (conditional, NC-dead if a waiver fails). Still closed: ProPublica (NC), NYT etc (terms), ShareAlike.
- Pricing: free-in-cash = federal public domain (only fully confirmed base) + Global Voices (contact-gated, Left lean) + provisionals; real cost = curation labor ~5-10 hrs/wk. Paid avenues all poor for a small budget (AP ~$1,600/mo smallest, Tribune high-hundreds to low-thousands, NYT/WaPo/WSJ ~$9-20k/yr at daily, Reuters enterprise, CCC rail-only). Direct-from-writer is the only paid option that scales to 1/wk; price TBD by a blind test. Unit econ: ~$14 net/sub; ~16-46 subs fund one writer-piece/wk.
- 3-5/wk is NOT deliverable on free sources alone: honest floor ~2/wk, 3 typical, 4-5 rare. Free + ~1 paid writer/wk -> steadier 3-4. Do not promise a cadence until a real 2-4 week pull counts survivors.
- Full memo: [[Licensing-Verification]].

## Decisions / status
- Commissioning writers: OUT.
- D-009 (untouched article + separate apparatus): adopted as the working model, conditional on a lawyer opinion.
- Recommended engine: federal public-domain base + gated free sources (Global Voices, Singularity Hub) + OpenMind upside + ~1 direct-from-writer piece/wk to reach 3-4/wk.
- Format discipline is load-bearing: bit-for-bit article, zero inline labels, separate apparatus, short-phrase quotes keyed by location only.

## RESUME HERE (next session)
Pick one to start (ordered by value):
1. Volume pressure-test FIRST: define the four-filter screen (current, ~350-600 wds, genuinely argument-driven, classroom-safe/neutral), pull 2-4 weeks of real candidates across federal PD + Global Voices, count survivors. Gates the cadence promise.
2. Clear the three free-pool gates (Global Voices regular-republisher contact; re-pull Singularity Hub guidelines; OpenMind classification email).
3. Blind-test the writer channel: cold-email 10-15 classroom-safe Substack writers for yes-rate and per-piece price; verify clean rights per piece.
4. Scope state/local government text + institutional CC0 sources.
5. Build the apparatus template (enforced physical separation).
6. Hard launch gate: written copyright-attorney opinion on the collection-not-derivative point, and that a bare CC-BY-ND grant does not override publisher contract overlays.

Also still open from earlier: the blind teacher test itself (rewrite the 3 AI essays without a single rigid template so they are not formulaic; pair each with a real op-ed Samuel selects; ask teachers which a person wrote and which they would rather teach).
