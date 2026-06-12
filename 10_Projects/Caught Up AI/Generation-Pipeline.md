---
created: 2026-06-11
updated: 2026-06-11
tags: [project, caught-up-ai, generation, pipeline, beta]
project: "[[Caught Up AI]]"
---

# Caught Up AI Generation Pipeline (beta engine)

The production engine that turns the v2 prose system into a finished Opener with one
command. Built 2026-06-11 as the beta for the real product, replacing the manual
paste-prompt ([[caughtupai-quickprompt-V1]]) with an enforced, repeatable workflow.

Lives at `.claude/workflows/caughtup-opener.mjs` (project-local workflow).

## What it does

Three phases, with model routing ENFORCED per phase (not advisory):

| Phase | Model | Work |
|---|---|---|
| Verify | Fable 5 (strongest) | Fetch today's real date, pick a real story from the last 5 days (or take a given topic), web-confirm every fact against a source, return a sourced fact list. Rejects person-attacks and national third rails. |
| Compose | Fable 5 (strongest) | Read all binding spec files, write the headnote first, draft the 350-600 word piece, self-run the 4 gates with the friction/anti-symmetry layer, tag devices from the controlled list, build 2 MCQs + full apparatus. Emits a schema-valid piece dict. The load-bearing creative + editorial stage. |
| Render | Haiku (cheap) | Write the piece dict to JSON + a driver that imports `build()` / `randomize_answers()` from `render_opener_v2.py` unmodified, produce the teacher + student PDFs, append to the editions log. |

Routing rule: strongest model for anything involving judgment (story choice, fact
verification, prose + editorial), cheap model only for the genuinely mechanical render
step. Verify was moved from Haiku to Fable 5 on 2026-06-11: accuracy is the #1 open
risk, a wrong fact hits an expert (teacher) customer, and because the product is
broadcast (one edition/day amortized across all subscribers) the model-cost saving
from a cheap verify is a rounding error not worth the accuracy risk. This routing flips
only if the product ever moves to per-teacher personalized editions. See [[caughtupai-quickprompt-V1]].

## Two things that make it reliable

- **Locked data contract.** Compose is forced (JSON schema) to emit the exact piece
  dict `render_opener_v2.py` consumes: the `[[n]]...[[/n]]` device marks (mark n maps
  to `devices[n-1]`, whose `para` is its 1-based paragraph), the `devices` / `mcq` /
  `writing` / `misconceptions` shapes. The renderer is never modified.
- **Persistent recency.** Each run appends register / template / opener / close to
  `Sample-Briefs/editions-log.tsv`; Compose reads it and steers off the last edition,
  so consecutive runs do not drift into sameness.

## How to run

Ask Claude (in a session from this vault): "build today's Opener", or "build an
Opener on <topic>", or add "...in the <register> register". Optional args: `topic`,
`register`. Everything else the pipeline decides. Output PDFs land in `Sample-Briefs/`.

## Proven (2026-06-11 first run)

- Story: 2026 US measles totals (The Ledger). Both PDFs (~850KB each) written
  unattended in ~8.5 min / ~193k tokens.
- Facts independently re-confirmed against CDC / CIDRAP / CNN: the Haiku verify pass
  was accurate.
- Structure clean: device marks mapped correctly, 2 MCQs on different skills, devices
  named only from the controlled list, no em-dashes / emojis / scholarly citations.

## Scope and what's deferred

- This build = generation pipeline only. No mid-run human approval (runs end to end).
- Deferred: email-PDF delivery to beta teachers, daily scheduling. The full teacher
  portal / prefs page stays deferred until multi-seat exists.
- Beta discipline: eyeball the facts before any Opener reaches a real teacher, until
  it holds across a batch.

## Cost and scaling

At API rates the measured cost is ~$5.40 per Opener (Fable Verify + Compose +
Fact-check, Haiku render), ~$160/month for a daily Opener. Cheaper paths (Batches API
at 50% off, scheduled routine on subscription) are scoped in [[Batch-API-Readiness]];
decided 2026-06-12 not to build the batch port yet (premature against a moving spec).

Related: [[caughtupai-quickprompt-V1]], [[caughtupai-sampleprompt-V1]],
[[Generation-Briefs]], [[Editorial-Standards]], [[Headnote-Spec]],
[[Batch-API-Readiness]], [[Caught Up AI]].
