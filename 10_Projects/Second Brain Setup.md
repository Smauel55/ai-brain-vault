---
created: 2026-05-07
updated: 2026-05-07
tags: [project, active]
status: in-progress
---

# Second Brain Setup

## Goal

Build a persistent knowledge base in Obsidian, hooked into Claude Code, so context and decisions transfer across sessions instead of being lost between conversations.

## Why

Eliminate re-prompting. Eventually the assistant becomes individualized — knows the projects, the working style, the prior decisions, without being told each time.

## Status

- [x] Install Claude Code on Windows (native installer)
- [x] Connect Cowork to vault (`C:\Users\srlev\OneDrive\Documents\Claude\AI Brain 1.0`)
- [x] Create folder structure (`00_Index`, `10_Projects`, `20_Conversations`, `30_Knowledge`)
- [x] Create root `CLAUDE.md` with vault operating instructions
- [x] Seed `About-Me.md` and `Active-Projects.md` (templates — needs filling)
- [ ] Fill in `About-Me.md` with real personal context
- [ ] Launch Claude Code from the vault and verify CLAUDE.md auto-loads
- [ ] Decide whether to add a global `~/.claude/CLAUDE.md`
- [ ] First real working session that produces a conversation log

## Decisions made

- **Vault location:** `C:\Users\srlev\OneDrive\Documents\Claude\AI Brain 1.0` (OneDrive-backed, auto-synced).
- **Primary interface:** Claude Code (terminal) for the auto-loading CLAUDE.md behavior. Cowork as secondary.
- **Structure:** Minimal numbered folders, not a full PARA system. Easy to grow into.
- **Conversation logs:** stored in `20_Conversations/` as `YYYY-MM-DD - Topic.md`.

## Open questions

- Should daily notes be enabled in Obsidian's core plugin, or are conversation logs enough?
- Templater plugin — install now or later?
- Backup beyond OneDrive — git? something else?

## Related

- [[About-Me]]
- [[Active-Projects]]
- See `CLAUDE.md` at vault root for the operating protocol.
