---
created: 2026-05-07
updated: 2026-05-07
tags: [conversation, setup]
project: "[[Second Brain Setup]]"
---

# 2026-05-07 — Vault Setup

## Context

Samuel asked Claude to help build a "second brain" in Obsidian linked to Claude such that knowledge and progress transfer across sessions, eliminating the need to re-prompt context each time.

## Key points

- Existing Obsidian vault discovered at `C:\Users\srlev\OneDrive\Documents\Claude\AI Brain 1.0` — essentially empty (Welcome.md + empty daily note).
- Decided **Claude Code as primary** interface because it auto-loads `CLAUDE.md` from the working directory; no need to manually re-load context each session. Cowork stays as secondary for non-coding work.
- Native Windows Claude Code installer is now available — no Node/npm/WSL required. Install line: `irm https://claude.ai/install.ps1 | iex`.

## Decisions

- **Vault structure:** minimal numbered folders (`00_Index`, `10_Projects`, `20_Conversations`, `30_Knowledge`) over heavier PARA system. Reasoning: easy to grow into, lower friction at start.
- **CLAUDE.md at vault root** as the operating-instructions file. Tells future Claude what to read, how to log, where to file new knowledge.
- **Conversation logs go in `20_Conversations/`** with `YYYY-MM-DD - Topic.md` naming.
- **OneDrive is fine** as the storage backend — gives free backup/sync. Caveat: avoid simultaneous edits across devices.

## Action items

- [ ] Samuel — install Claude Code via PowerShell (`irm https://claude.ai/install.ps1 | iex`)
- [ ] Samuel — fill in `00_Index/About-Me.md` with personal context (the biggest leverage move for individualization)
- [ ] Samuel — `cd` into the vault, run `claude`, verify `CLAUDE.md` auto-loads
- [ ] Samuel — decide whether to also create a global `~/.claude/CLAUDE.md`

## New knowledge to file

- The Claude Code memory hierarchy (root → nested → global) is reusable knowledge — worth a `30_Knowledge/` note.

## Open threads

- Daily notes: turn on Obsidian core daily-note plugin or rely solely on conversation logs?
- Templater plugin: useful for auto-stamping front-matter — worth installing?
- Backup beyond OneDrive (e.g., git) — open question.
