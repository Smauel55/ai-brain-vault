---
created: 2026-05-13
updated: 2026-05-13
tags: [conversation, cowork, airtable, mcp]
project: "[[Caught Up AI]]"
---

# 2026-05-13 — Cowork Airtable verification plan

## Context

Samuel finished setting up an Airtable base ("Clients & Outreach", `appPzYnVFAN84aIM9`) and asked whether he could now have Cowork run web searches and write results into it. Before running a real research job, we agreed to verify the wiring first. The conversation produced a runbook for Samuel to execute in Cowork tomorrow. No code was written.

This is a direct follow-up on the open thread from [[2026-05-12 - AI Brain MCP setup]] about Cowork session-level toggle behavior being unclear.

## Key points

- Airtable MCP confirmed working from Claude Code: `ping` -> `pong`, `list_bases` returns the "Clients & Outreach" base with `create` permission. Account-level auth is good.
- Whether Cowork has Airtable attached to a specific session is a separate UI step Samuel needs to check tomorrow.
- Surface routing was flagged: research-and-write jobs belong in Cowork, not Code. Code isn't built for long autonomous runs.

## Decisions

- Verify connection in Cowork before running any real job. Reason: a misconfigured agent could dump bad data into the live base.
- Six-step checklist (open session, confirm Airtable attached, confirm web tools attached, read-only smoke test, web smoke test, optional end-to-end write test). Plan file at `C:\Users\srlev\.claude\plans\so-i-just-finisehd-humming-cocoa.md` — keep this file, Samuel will reference it tomorrow.

## Action items

- [ ] Samuel — tomorrow — run Steps 1-5 (and optionally Step 6) of the plan file in a fresh Cowork session, report which pass.
- [ ] Claude (next session) — once Samuel reports back, draft the real Cowork prompt for the research-and-write job. Will need from Samuel: search topic, target table, column mapping, row cap.

## New knowledge to file

- **Pre-flight checklist for MCP-driven Cowork jobs.** Could become an atomic note in `30_Knowledge/` — the general pattern is: confirm MCP attached in session, confirm web tools attached, run a read-only smoke test, run a web smoke test, optional end-to-end write test on a throwaway row. Reusable for any future Cowork + MCP workflow (Notion, Linear, Gmail, etc.).

## Open threads

- Whether Cowork session-level MCP toggling actually wires the tools through at runtime — yesterday's open thread, still unresolved. Tomorrow's Step 4 (Airtable read smoke test) will answer it.
- Airtable base "Clients & Outreach" is likely tied to [[Caught Up AI]] outreach. Confirm with Samuel before the real research job — the column schema will determine the search prompt.
