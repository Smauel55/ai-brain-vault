---
created: 2026-06-12
updated: 2026-06-12
tags: [conversation, infrastructure, memory]
---

# 2026-06-12 — Response latency diagnosis and memory consolidation

## Context

Samuel asked why Claude Code responses have gotten slow (multi-minute waits) and whether something unnecessary was eating time every response.

## Key points

- Diagnosis: partly normal (thinking time, multi-step tool work, long sessions reprocessing all prior context), but three real overheads found:
  1. MEMORY.md index had grown to 14.2 KB (loaded every session); the Caught Up AI entry alone was ~1,500 words duplicating the project file.
  2. CLAUDE.md's read-two-files-at-session-start rule taxes even trivial questions.
  3. Connected MCP servers add baseline context (smaller now that tool schemas load on demand).
- Biggest *felt* factor is session length: late-session responses slow regardless of index size. Fresh sessions more often is the main user-side fix.

## Decisions

- Ran the memory consolidation. Memory dir cut 124.8 KB -> 66.8 KB:
  - MEMORY.md 14.2 -> 3.9 KB (one line per entry, grouped into sections; Caught Up AI entry collapsed to a pointer).
  - `project_caught_up_ai.md` 54.3 -> 6.2 KB (durable decisions + current state + detail map; dated update blocks retired after verifying each had a matching `20_Conversations/` log or spec file).
  - Fixed index bug: two entries pointed at `feedback_device_vocabulary.md`; renderer/prompt info split out to new `reference_opener_renderer.md`.
  - Retired stale `project_google_drive_mcp.md` (deleted from memory dir AND `01_Memory/` mirror, since the sync never deletes); its durable fact folded into `reference_drive_mcp_formatting.md`.

## New knowledge to file

- Deleting a memory requires deleting both copies (memory dir + `01_Memory/`); robocopy /XO resurrects single-side deletions. Noted here; small enough not to need a 30_Knowledge note.

## Open threads

- If slowness persists after this, next levers: fewer connected MCP servers, shorter sessions.
