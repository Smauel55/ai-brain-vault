---
created: 2026-06-08
updated: 2026-06-11
tags: [project, caught-up-ai, generation, editorial, guardrail, neutrality, accessibility]
project: "[[Caught Up AI]]"
---

# Editorial Standards (D9)

Two non-negotiable content guardrails that sit above every register and apply to every Opener, in every political-intensity tier. They are not craft preferences; they are gates, like accuracy. A piece can be beautifully written, perfectly in register, and factually airtight and still fail here. If it fails here, it does not ship.

These exist because the product goes into a classroom under a teacher's name, in front of minors, across districts of every political makeup. The voice of Caught Up AI is the teacher's borrowed voice. Two things would break that trust faster than anything else: a piece that picks a side on a hot-button national value-dispute or attacks a real person, and a piece a student cannot actually read without a glossary. Note (revised 2026-06-11): the civic tier now *does* allow pointed, persona-driven advocacy on broad civic/policy matters — the firewall narrowed from "no stance ever" to "no person attacks, no group attacks, no side on the national third rails." See Guardrail 1.

Binds the [[Generation-Briefs]] pre-flight (Gate 0). Companion to [[Accuracy-Guardrail]] (facts true), [[Anti-Tell-List]] (not AI-sounding), [[Cross-Piece-Sameness-Rubric]] (varied across the batch). Routing context in [[Style-Palette]]; the customization model is the political-intensity dial in [[2026-06-07 - Opener customization strategy]].

---

## Guardrail 1: The neutrality firewall (issue-advocacy allowed, person/group/hot-rail attack banned)

There are two ways an Opener can handle a civic subject, and which one is allowed depends on the political-intensity tier.

**Default mode (every tier): the neutral explainer.** Report the issue and the documented competing positions fairly, then hand the analysis to the student. Do not argue for an outcome, do not cast anyone as villain or hero. This is the only mode available on the non-civic tier, and it is always a safe fallback on the civic tier.

**Pointed mode (CIVIC tier only): persona-driven issue advocacy.** On the "includes civic / current events" tier, an Opener *may* take a pointed position and argue it with full force, because AP Lang teaches persuasion and position-taking rhetoric is the richest material to analyze. This is allowed under all of the following conditions:

- **A clear speaker, named by role, not by name.** A civilian testifying to a city council, a parent before a school board, a resident addressing Congress about a bill, a nurse, a small-business owner. The headnote names *who is speaking, to whom, on what occasion* (the AP source-passage setup; see [[Headnote-Spec]]). Personas are framed by role, never given an invented proper name and never a real person.
- **First-person emotion is the point.** Let the speaker be angry, grieving, hopeful, indignant. The move from personal stake to public argument is exactly the ethos/pathos the class mines for rhetorical depth. A bloodless position paper has nothing to analyze.
- **The force aims at the issue or the institution, never at a person.** "I am furious that this council voted to close our clinic" is in. "Councilman Reyes is a coward" is out. The target is the bill, the policy, the practice, the body ("the council," "Congress"), never a named or identifiable officeholder.

**The three hard bans (apply in BOTH modes, every tier):**

1. **No attack on a specific person.** Do not name, or transparently imply, a living political figure as the wrongdoer, the target, or the addressee of a critical piece. "Mr. President" with no name is still the sitting president: banned. A real official can appear as a neutral *actor* in sourced reporting ("the Secretary announced the rule"); what is banned is *stance toward* them (wrong, hypocritical, failing, owing an apology).
2. **No attack on a group.** No piece that indicts or argues against a political party, a religion, a nationality, an ideology, or a demographic.
3. **No side on the hottest national value-disputes.** The live national third rails — abortion, guns, partisan elections and candidates, and contested-value immigration questions (e.g. whether birthright citizenship should exist) — stay in neutral-explainer mode only, even on the civic tier. Present the documented record and the strongest version of each side; never endorse one. A one-sided pathos piece on these in an opposite-lean district is the exact existential trust/churn risk this firewall exists to stop. (Birthright citizenship can still be an Opener — as a Ledger explaining the mechanics and the competing positions, not a should-we argument.)

**Where pointed advocacy IS unlocked (civic tier):** the broad civic/policy universe outside the three rails — local services and their funding, a specific bill's tradeoffs, school funding, infrastructure, governance and process, civic participation and duty, a documented institutional practice. The test is value-consensus: if the shared value is broadly agreed and the dispute is over means, competence, or local impact ("don't close our clinic," "this ordinance is unworkable"), pointed advocacy is fair game. If the dispute is over a contested value itself (the third rails), it stays neutral.

**Routing consequences for the two stance-driven registers.** The Open Letter and The Reckoning are the registers built for a target. On the civic tier they may now be genuinely pointed, constrained as follows:

- **The Open Letter.** The addressee may be an institution or body (a city council, Congress, an agency, a company or its CEO over a documented practice, an industry, a standards body) — but never a named or identifiable living political officeholder, candidate, or partisan body (a party, a caucus), and never an argument for one side of a third-rail value dispute. A persona may write *to* the council about a clinic closure with full pathos; a persona may not write *to* the President, nor argue *for* an abortion-law outcome. If the only honest addressee is a political figure, or the only honest content is a third-rail stance, route it to The Ledger or drop it.
- **The Reckoning.** The nameable responsible party may be an institution, a corporation, a documented system or practice, an industry — never a partisan political target, and never the implicit indictment of one side of a third-rail dispute. If the only culprit the facts support is a politician or a party, route to The Ledger. Forcing blame onto a political figure to make the register work is exactly the failure this guardrail stops.

**The neutral path always exists.** The Ledger can carry any civic or political story by laying out the documented record and the competing positions without endorsing one. When a story falls on a third rail, or cannot be handled without targeting a person, route it to The Ledger. When in doubt, route to The Ledger.

**Drift cues (check at routing AND on the finished piece):**
- Drifted if a piece takes a side on a third rail (abortion, guns, partisan elections/candidates, birthright-citizenship-style value questions). Those stay neutral even on the civic tier.
- Drifted if a living political figure is the addressee, the villain, or the hero, or is clearly implied to be (an unnamed "Mr. President", "the governor", "this administration" used accusingly). This holds even inside a pointed persona piece.
- Drifted if the speaker's force turns from the issue/institution onto a named or identifiable person (a character attack rather than a policy argument).
- Drifted if a pointed persona piece runs on the NON-civic tier; pointed mode is civic-tier only.
- Drifted if a persona is given an invented proper name or attributed to a real person, rather than framed by role.
- Drifted (neutral-mode pieces) if a reader could tell which side the writer is on, or if only one side of a contested issue is given its strongest form and the other is summarized weakly or skipped.

---

## Guardrail 2: Plain-knowledge accessibility (no unexplained jargon)

**The rule.** The audience is high school students. Every term, name, or concept the piece uses *without explaining it* must be common knowledge to a typical high schooler. If a specialized term is load-bearing, define it in plain language in-line on first use, or rewrite to avoid it. If it is not load-bearing, cut it.

**What this is not.** This is not "dumb the prose down." AP-Lang sentence craft, sophisticated vocabulary, and the register's reading-grade band (governed in [[Register-Specs]]) all stay. This guardrail governs *assumed background knowledge and domain jargon*, not sentence sophistication. A student can parse a long periodic sentence; they cannot be expected to already know what Medicare Part D is.

**The test.** Would a typical 11th grader who does not follow the news know this term, with no help, from school and ordinary life? If yes, use it bare. If no, define it in a clause on first use, or cut it.

- **Common knowledge, use bare:** president, Congress, the Senate, the Supreme Court, a vote, a tax, a budget, inflation in its everyday sense, a recession, a CEO, a lawsuit, a treaty.
- **NOT common knowledge, must define in-line or avoid:** Medicare Part B and Part D, cloture and the filibuster mechanics, basis points, the GDP deflator, mens rea, habeas corpus, a price-to-earnings ratio, quantitative easing, a cap rate, appropriations versus authorizations, an actuarial cap. (The $35-cap Ledger failed here by using "Part D" and "Part B" with no plain-language gloss.)

**How to define without it reading like a textbook.** A defining clause folded into the sentence, in the piece's own voice, not a parenthetical lecture. "the part of Medicare that pays for prescription drugs" instead of "Part D". One clause, once, on first use. Do not over-explain genuine common knowledge (explaining what Congress is to a high schooler is condescending and reads as an AI tell).

**Drift cues:**
- Drifted if a term appears that a typical 11th grader could not define, with no in-line explanation.
- Drifted if the piece assumes the reader already follows this beat (knows the program's sub-parts, the procedural rule, the financial metric).
- Drifted if an acronym or a numbered program part ("Part D", "Section 230", "Title IX") appears without a plain-language gloss the first time.
- Drifted the other way if the piece pauses to explain something every high schooler already knows; explain only the genuinely specialized.

---

## Where this runs

- **At routing, before drafting:** pick the register and the angle so the piece is non-partisan by construction. A partisan-only story routes to The Ledger or is dropped; a jargon-heavy story is planned with plain-language glosses up front.
- **At pre-flight, before the piece joins the batch:** Gate 0 in [[Generation-Briefs]], run first, before the accuracy, register, anti-tell, and sameness gates. A piece that fails Gate 0 goes back before the later gates are worth running.

## Related

- [[Generation-Briefs]] - the pre-flight checklist; this is Gate 0.
- [[Style-Palette]] - register routing; the neutrality firewall constrains Open Letter and Reckoning routing.
- [[Register-Specs]] - the per-register craft and bands; the Open Letter and Reckoning drift cues carry the neutrality constraint.
- [[Accuracy-Guardrail]] - the parallel fact-fidelity gate.
- [[2026-06-07 - Opener customization strategy]] - the political-intensity dial; this guardrail is what keeps even the civic tier safe.
- [[Caught Up AI]] - project root.
