---
created: 2026-06-12
updated: 2026-06-12
tags: [conversation, caught-up-ai, model-routing]
project: "[[Caught Up AI]]"
---

# 2026-06-12 — Model routing and the 10/80/10 rule

## Context

Samuel saw a newsletter/video arguing Fable 5 is too expensive to use for everything; proposes a 10/80/10 split (plan in Fable, build in Opus 4.8, review in Fable). Asked for an unbiased read in the Caught Up AI context.

## Key points

- The rule's core (strong model for judgment, cheap for mechanical) is already the architecture of the [[Generation-Pipeline]]: Verify/Compose = Fable 5, Render = Haiku.
- Applying 10/80/10 literally would be wrong for the Opener pipeline: the "middle" there is composing the prose, which IS the product (AI-tell + accuracy risk both live there). Broadcast economics amortize Fable's Compose cost across all subscribers; downgrading it saves pennies and risks the differentiator.
- Where it does fit: build chores (Base44 wiring, render scripts, vault upkeep, ideation) can run on Opus 4.8. The opener workflow pins models per stage inside the script, so cheaper everyday sessions do not affect Opener quality.
- Review pass on the strong model matters MORE for Samuel than for the newsletter author: on the no-code path the Fable review is the only code-level safety net.
- Real budget lever stays: capped batch sizes, adversarial fan-outs audit-only (per existing token-budget rule), not downgrading Compose.

## Decisions

- None by Samuel yet; recommendation on the table = run daily/non-pipeline Code sessions on Opus 4.8, leave the pipeline's model routing untouched.

## Housekeeping done this session

- Logged prior session (2026-06-12 batch run, 3 openers, count-arg bug) to 20_Conversations.
- Fixed double-encoded UTF-8 in memory MEMORY.md index.
