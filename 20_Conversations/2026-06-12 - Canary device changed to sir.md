---
created: 2026-06-12
updated: 2026-06-12
tags: [conversation, feedback, working-style]
---

# 2026-06-12 - Canary device changed to "sir"

## What happened
- Samuel said hearing his name in every response got annoying; changed the session-degradation canary from "Samuel" to "sir".

## Changes made
- Updated [[feedback_name_canary]] (memory) — description + body, both the live Claude Code memory copy and the `01_Memory/` vault mirror.
- Updated both `MEMORY.md` index entries to match.

## Net effect
- Claude now addresses Samuel as "sir" in every response as the tripwire. Same logic otherwise: if it drops, that's the cue to start a fresh session; it trips late, so it stays a backstop not the only signal.
