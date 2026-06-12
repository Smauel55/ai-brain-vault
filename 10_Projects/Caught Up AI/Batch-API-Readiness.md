---
created: 2026-06-12
updated: 2026-06-12
tags: [project, caught-up-ai, pipeline, cost, readiness]
project: "[[Caught Up AI]]"
---

# Batch API Readiness Note

Migration path for moving the [[Generation-Pipeline]] onto the Anthropic Batches API
(50% off all token usage) IF and WHEN it becomes worth it. Decided 2026-06-12 NOT to
build it yet (premature; see drawbacks). This note keeps the port well-scoped so it is
a known, fast job at launch instead of a research project.

## When to actually do this (trigger conditions)

Build it only when ALL of these hold. Until then, do nothing here.

- Fable 5 has left subscription inclusion, so the nightly run is being billed at API
  rates. While it is subscription-included, run on the subscription via a scheduled
  Claude Code routine instead (no rewrite, no billing).
- The pipeline spec is frozen, i.e. no longer being refined week to week from teacher
  feedback. A frozen batch reimplementation that drifts from the workflow is a
  maintenance tax; do not pay it against a moving spec.
- Volume justifies it. The batch parallelism only pays off when an edition produces
  MANY independent Openers. A single broadcast Opener per day gets only the flat 50%
  discount (no throughput gain) and could get that more simply.

## Why the port is clean when the time comes

Nothing needs building now to stay ready. The hard parts are already in place:

- The stage prompts are self-contained strings in `caughtup-opener.mjs`; they lift out
  directly into SDK calls.
- The schemas (`FACTS_SCHEMA`, `PIECE_SCHEMA`, `CHECKED_SCHEMA`) already exist and map
  straight to structured outputs (`output_config.format` with `json_schema`). Fable 5
  supports structured outputs.
- `render_opener_v2.py` is already imported unmodified via `build()` /
  `randomize_answers()`. In the batch world the render stage stops being an LLM call and
  becomes plain local code (the same `_run_latest.py` driver shape).
- The web steps port to server-side `web_search_20260209` / `web_fetch_20260209`, which
  run inside a batch request (Anthropic runs the agentic loop server-side).

## What changes (workflow -> batch SDK)

| Stage | Now (Claude Code workflow) | Batch SDK version |
|---|---|---|
| Verify | Fable agent; bash `date`, ToolSearch + WebSearch/WebFetch, reads Accuracy-Guardrail off disk | Fable request; orchestrator passes the date in and inlines the guardrail; server-side `web_search` / `web_fetch` tools |
| Compose | Fable agent; reads all binding spec files off disk | Fable request; orchestrator reads the spec files and inlines them (or Files API); schema via `output_config.format` |
| Fact-check | Fable agent, no web | Fable request, no tools |
| Render | Haiku agent writes JSON + a python driver and runs it | NOT an LLM call. Orchestrator runs `render_opener_v2` locally on the returned piece dict. Haiku drops out of the chain entirely. |

Single Opener: run the 3 LLM stages as plain synchronous `messages.create` calls, or as
1-item batches for the discount. Multi-Opener day: stage them. Batch all Verify, poll to
done, batch all Compose, poll, batch all Fact-check, poll, then render each locally
(Verify -> Compose -> Fact-check is a dependency chain, so it is three staged batches,
not one).

## What still has to be built (the real cost of doing it)

- A standalone Python or Node program calling the Anthropic SDK directly.
- An Anthropic API account with billing (separate from the subscription).
- A scheduler to trigger the nightly run, plus retry / error handling and the staging
  orchestration for multi-item days.
- Note: this is code Samuel cannot inspect or debug line by line ([[feedback_no_code_path]]).
  When it fails on the nightly run there is no Claude session in the loop to self-heal,
  so it needs solid logging and a fallback to the workflow path.

## Cost math (measured 2026-06-12, from the 3-Opener workflow run)

Prices per million tokens: Fable 5 $10 in / $50 out, Haiku 4.5 $1 / $5, Opus 4.8 $5 / $25.
Cache writes 1.25x input, cache reads 0.1x input.

- Measured 3-Opener workflow run: Fable ~$16.09 + Haiku ~$0.14 = ~$16.24, about
  $5.41 per Opener at API list rates.
- A daily single Opener at full API rates: roughly $160 to $165 per month (a solo
  nightly run amortizes cache less than a 3-batch, so per-Opener runs a little higher).
- Batches API (50% off): roughly $2.70 per Opener, about $80 per month. A clean
  direct-SDK build could be leaner than the measured workflow number (you control
  exactly what each request carries and can cache the binding files deliberately), so
  treat the measured figure as an upper bound, then halve for batch.
- For comparison, the same run with Compose/Verify on Opus 4.8 instead of Fable prices
  at about $8 (~$2.70/Opener). That ~$80/month Fable premium over Opus is the dollar
  value of keeping the writing on the strongest model, which is the right call because
  the prose is the product and accuracy hits an expert customer.

## Bottom line

The batch discount is a cost optimization for the paying world, not a launch
requirement. The launch-critical gap is scheduling and delivery (still deferred), which
has a no-rewrite path (scheduled routine on the subscription). Revisit this note at
launch.

Related: [[Generation-Pipeline]], [[Caught Up AI]], [[feedback_production_token_budget]],
[[feedback_no_code_path]].
