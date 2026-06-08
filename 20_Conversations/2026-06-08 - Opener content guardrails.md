---
created: 2026-06-08
updated: 2026-06-08
tags: [conversation, caught-up-ai, editorial, generation]
project: "[[Caught Up AI]]"
---

# 2026-06-08 — Opener content guardrails (neutrality + reading level)

## Context

Samuel flagged two content problems in the existing sample Openers and asked that they never recur.

## The two issues

- **Divisive / partisan content.** An early Open Letter ("Decide What Your Oath Was For") was addressed to an unnamed "Mr. President" — transparently the sitting president — and took a strong stance against him. Stop writing pieces that attack a specific person or group, or take a partisan side. This holds even for teachers on the civic-pieces tier.
- **Unexplained jargon.** The $35-cap Medicare Ledger used "Part D" and "Part B" with no explanation; a typical high schooler does not know those. Everything used unexplained must be common knowledge to a high schooler.

## What was built (fix at the source)

- New authority file **[[Editorial-Standards]]** (D9): two cross-cutting guardrails above every register, on every political-intensity tier.
  - **Guardrail 1 — neutrality firewall:** no political side, no attack on a person/group. Civic topics are fine; stance is not. Open Letter addressee and Reckoning culprit may never be a politician/party/identifiable political figure; route those stories to The Ledger or drop them. The neutral path always exists via The Ledger.
  - **Guardrail 2 — plain-knowledge accessibility:** every unexplained term must be high-school common knowledge; gloss specialist terms in one in-line clause on first use or cut. Not "dumb down the prose" — governs assumed background knowledge/jargon only. Don't over-explain genuine common knowledge.
- Wired in as **Gate 0** (runs first, before accuracy/register/anti-tell/sameness):
  - [[Generation-Briefs]] pre-flight is now five gates, Gate 0 added.
  - [[caughtupai-sampleprompt-V1]] — added to binding-file list, HARD RULES block, TOPIC MODE neutral-angle instruction, gate count to five.
  - [[Register-Specs]] — neutrality drift cue added to The Open Letter and The Reckoning.
  - [[Style-Palette]] — neutrality + plain-knowledge routing note in "How to use".

## Open threads

- Existing Sample-Briefs artifacts that violate the new rules are NOT yet regenerated: partisan Open Letters ("Decide What Your Oath Was For", "The Forty-Year Rule You Wrote", "The Principles You Already Signed", "The Purse You Promised to Guard"), partisan Reckonings ("The $186 Billion Nobody Stopped", "The Papers on the Table", "The First State to Name the Man"), and the jargon Ledger ("The $35 Cap and the People It Misses"). Regenerate or pull before any teacher demo.
- The Open Letter register now has a much smaller honest target pool (no political addressees). Worth checking it still earns its slot, or whether its non-partisan addressee variants (company/industry/profession/institution) carry enough weekly material.
