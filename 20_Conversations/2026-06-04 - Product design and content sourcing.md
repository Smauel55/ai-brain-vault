---
created: 2026-06-04
updated: 2026-06-04
tags: [conversation, caught-up-ai, product-design, content-sourcing]
project: "[[Caught Up AI]]"
---

# 2026-06-04 - Product design and content sourcing

## Context

Started designing the Caught Up AI product. Chose to map the end-to-end teacher journey first, but the session went deep on one blocker: where the daily article actually comes from. That question now gates the whole product.

## Where we are / resume here (read this first)

- We were designing the product, starting with the end-to-end JOURNEY MAP. Agreed spine: Discovery, Landing, Signup/trial, Setup form, First brief (activation), Daily habit, Conversion, Retention. We had NOT yet deep-designed any stage. Next deep-dive stage was Landing.
- We detoured (correctly) into the CONTENT ENGINE question because it gates everything. That is where the session ended.
- Open decision to resume on: which content engine. See "The fork" below. Honest finalists: licensing vs AI-with-human-editing.
- Proposed next step: draft a blind side-by-side test (AI-written brief vs a real one) to put in front of teachers in discovery, to settle whether real authorship is load-bearing. Alternative: return to the journey map at Landing.

## Key points established

- Product mechanic that drives everything: the teacher version reproduces the full article text with rhetorical devices marked up inline. That requires reproducing AND modifying the text inside the email.
- Feasibility (honest): the end goal (daily 6am email, two versions) is buildable with today's tech. Delivery is a solved problem. The CONTENT ENGINE is the hard part and the real risk, not the software.
- Claude's coding: high skill, but not a drop-in engineering team. Samuel (no-code operator) plus AI plus tools can reach an MVP; production hardening and scaling likely need a contractor later. Run costs are small; content-generation cost is flat in user count because content is shared. The ~95% margin target is realistic.
- Build path sketched in phases: Phase 0 manual MVP (~$0-20/mo, all human, this fall), Phase 1 semi-auto (Base44 + Resend + Stripe, ~$50-150/mo), Phase 2 automated (~$150-400/mo run, ~$3-25k one-time build). Humans required for: deployment + email auth (SPF/DKIM/DMARC), deliverability (biggest underestimated risk), legal/privacy, on-call.

## Decisions (today)

- D-005 Link model REJECTED. Pointing to a hosted article (not reproducing it) is off the table. Inline rhetorical markup cannot live on a remote article; the marked-up text must be reproduced and modified in the email. This also forces the license requirement below.
- D-008 Canon-as-backbone REJECTED (reaffirms D-004). Using famous speeches/essays as the daily backbone is easier to build but guts the product: teachers have no prep pain with the canon, it is free and saturated (CommonLit, AP Classroom, textbooks), there is no moat, and it kills the subscription/habit logic. The modern canon (MLK, DFW Kenyon, Saunders) is also still copyrighted; only pre-1930 plus some government speeches are cleanly public domain. Canon stays a SUPPLEMENT only (Friday classic / thematic pairing), per D-004.
- Content-engine choice DEFERRED to a blind teacher test (see open threads).

## Findings (verified this session)

- License filter (deep research, primary sources, high confidence). To reproduce-in-full, annotate inline, and sell, the ONLY usable licenses are Public Domain, CC0, CC-BY. CC-BY-SA legally qualifies but its ShareAlike clause forces the marked-up teacher version to be released CC-BY-SA (subscribers could redistribute it free), so treat CC-BY-SA as off. ALL NonCommercial (NC) excluded because it is a paid product. ALL NoDerivatives (ND) excluded because annotation is a derivative.
  - The Conversation = CC-BY-ND (excluded; also forbids editing; commercial-exam fees).
  - ProPublica = CC-BY-NC-ND (excluded three ways).
- Supply (own spot-check, verified licenses). The free CC-BY/CC0/PD pool of CURRENT, argument-driven, classroom-safe nonfiction is too thin to anchor a daily product.
  - Global Voices (CC BY 3.0) is the ONE genuine qualifying current source. Global, activism-heavy; ~1-2 usable pieces/week after AP-worthiness and neutrality filters. A supplement, not a backbone.
  - Excluded by license: openDemocracy (BY-NC-ND), Aeon (BY-ND), YES! Magazine (BY-NC-ND), Common Dreams (BY-NC).
  - Structural reason it is dry: free publishers pick NC (block competitors) or ND (protect the author's words); opinion outlets especially favor ND, the exact right we must break.
  - The 7-day vs 30-day window is irrelevant. The constraint is licensing structure, not recency. Relaxing currency does not refill the pool.
- AI writing-quality scope (honest). The right bar is "a ~400-word piece with genuine analyzable rhetorical craft," not "pass the student exam." AI does structure, devices, and register well, and clears "useful daily analysis text." Real ceilings: the AI tell (reducible with strong prompting plus a human edit, not erasable on autopilot), authentic pathos / lived experience (genuine wall), and the missing real rhetorical situation (no real author or occasion to analyze). Conclusion: AI at the product's quality bar = AI plus a human editor per piece (labor, not free) plus trust/disclosure tradeoffs. Fully automated and unattended = the spottable, hollow version.

## The fork (the open decision to resume on)

Cannot keep every constraint (real + not-commissioned + current + daily + cheap + annotatable = empty set). Relax exactly one:
- Relax cost: license real current op-eds (annotation/derivative rights are the hard ones to get; enterprise pricing).
- Relax "no commissioning": commission owned originals (~$50-300/piece, ~$12-75k/yr at daily volume; flat in user count).
- Relax "no AI": AI plus a human editor.
- Relax "daily": free 2-3x/week product (Global Voices + current public-domain government rhetoric).
- Relax currency: canon (rejected, D-008).

Honest finalists: licensing (spend money) vs AI-with-editing (spend labor, accept authenticity/trust tradeoffs).

## Key reframe (keep in mind)

The sourcing difficulty is the MOAT, not a bug. Current, license-clean, annotatable content is scarce precisely because it is valuable, which is why teachers can't DIY it and would pay. The apparatus (questions, marked devices, answer key, model responses) is the real IP and is worth most on fresh content no one else has made materials for. Currency and value are coupled.

## Action items

- [ ] Decide the content engine (the fork above), or run the blind teacher test to inform it.
- [ ] Samuel: send discovery/outreach emails (planned 2026-06-05).
- [ ] When project files are next touched, add D-005 and D-008 to the formal Decisions Log in the Projects folder; this session created them only here.
- [ ] Eventually resume the journey map at Landing.

## New knowledge filed

- [[Caught Up AI - content licensing filter]] (30_Knowledge): the reproduce + annotate + commercial license rule and the verified source statuses.

## Open threads

- Blind A/B teacher test: show teachers an unlabeled AI-written brief and a real one; does real authorship matter, or does good AI-assisted writing pass? Likely settles the engine.
- Does the product need true per-teacher uniqueness, or is a tiered (class-level) shared brief enough? Affects cost/feasibility; raised earlier, unresolved.
- Licensing reality check: will any syndicator grant reproduce + annotate (derivative) rights, and at what price for a small edtech buyer? Deep research did not get cost numbers (budget-dropped).
- This content question does NOT block the fall manual MVP; the MVP and discovery are where it gets tested. It is the weakest link, not a stopper.
