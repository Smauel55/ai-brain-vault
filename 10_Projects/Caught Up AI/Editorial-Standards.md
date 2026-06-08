---
created: 2026-06-08
updated: 2026-06-08
tags: [project, caught-up-ai, generation, editorial, guardrail, neutrality, accessibility]
project: "[[Caught Up AI]]"
---

# Editorial Standards (D9)

Two non-negotiable content guardrails that sit above every register and apply to every Opener, in every political-intensity tier. They are not craft preferences; they are gates, like accuracy. A piece can be beautifully written, perfectly in register, and factually airtight and still fail here. If it fails here, it does not ship.

These exist because the product goes into a classroom under a teacher's name, in front of minors, across districts of every political makeup. The voice of Caught Up AI is the teacher's borrowed voice. Two things would break that trust faster than anything else: a piece that takes a political side, and a piece a student cannot actually read without a glossary.

Binds the [[Generation-Briefs]] pre-flight (Gate 0). Companion to [[Accuracy-Guardrail]] (facts true), [[Anti-Tell-List]] (not AI-sounding), [[Cross-Piece-Sameness-Rubric]] (varied across the batch). Routing context in [[Style-Palette]]; the customization model is the political-intensity dial in [[2026-06-07 - Opener customization strategy]].

---

## Guardrail 1: The neutrality firewall (no partisan stance, no attack)

**The rule.** An Opener may cover civic and political subjects. It may never take a political side, attack a specific person, or attack a group. We report the issue and the documented competing positions fairly, then hand the analysis to the student. We do not argue for an outcome, and we do not cast anyone as villain or hero.

**This holds even on the "includes civic / current events" tier.** That setting opts a teacher into civic *topics*, not into advocacy. A teacher who is comfortable with a piece *about* an immigration ruling is not thereby comfortable with a piece *arguing* the ruling was a betrayal. One hot-button, clearly-sided piece under a teacher's name in the wrong district is an existential churn and trust risk. The dial widens the topic pool; it never licenses a stance.

**The three hard bans:**

1. **No attack on a specific person.** Do not name, or transparently imply, a living political figure as the wrongdoer, the target, or the addressee of a critical piece. "Mr. President" with no name is still the sitting president: banned. A real official can appear as a neutral *actor* in sourced reporting ("the Secretary announced the rule"); what is banned is *stance toward* them (wrong, hypocritical, failing, owing an apology).
2. **No attack on a group.** No piece that indicts or argues against a political party, a religion, a nationality, an ideology, or a demographic.
3. **No side on a partisan dispute.** On the live partisan flashpoints (elections and candidates, abortion, guns, immigration, partisan personalities and parties), present the documented record and the strongest version of each side; never endorse one.

**Routing consequences for the two stance-driven registers.** The Open Letter and The Reckoning are the registers that most easily slide into partisan attack, because their engines require a target. They are constrained, not banned:

- **The Open Letter.** The named addressee may not be a sitting or identifiable political officeholder, a candidate, or a partisan body (a party, a caucus). Redirect the moral-pressure engine onto a non-partisan powerful addressee: a company or its CEO over a documented practice, an industry, a profession, a standards body, an institution acting in a non-partisan capacity, or a role or idea. If the only honest addressee is a political figure, the story is not an Open Letter; route it to The Ledger or drop it.
- **The Reckoning.** The nameable responsible party may not be a partisan political target. It can be a corporation, an institution, a documented system or practice, an industry. If the only culprit the facts support is a politician or a party, route the story to The Ledger (neutral explainer) or drop it. Forcing the blame onto a political figure to make the register work is exactly the failure this guardrail exists to stop.

**The neutral path always exists.** The Ledger can carry any civic or political story by laying out the documented record and the competing positions without endorsing one. When a story is genuinely newsworthy but cannot be handled without taking a side in a hotter register, route it to The Ledger. When in doubt, route to The Ledger.

**Drift cues (check at routing AND on the finished piece):**
- Drifted if a reader could tell which side the writer is on. The reader should be able to tell what *happened* and what each side *says*, not what to *think*.
- Drifted if a living political figure is the addressee, the villain, or the hero, or is clearly implied to be (an unnamed "Mr. President", "the governor", "this administration" used accusingly).
- Drifted if the piece would make a teacher in a district of the opposite political lean uncomfortable to put their name on it. That teacher is the test, not the sympathetic one.
- Drifted if the close is a verdict on a partisan question, a charge to act politically, or a moral indictment of an identifiable political actor.
- Drifted if only one side of a contested partisan issue is given its strongest form and the other is summarized weakly or skipped.

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
