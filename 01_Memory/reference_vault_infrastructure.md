---
name: Vault and memory infrastructure
description: Hooks, scripts, paths, and how the AI Brain vault and memory system are wired together. Reference this before suggesting new infrastructure.
type: reference
originSessionId: 02c26749-5f7d-4cd4-8a80-0629c2b72a8d
---
This file documents the existing Claude Code infrastructure on Samuel's Windows machine. Read it before proposing new hooks, sync mechanisms, or memory automation; chances are it already exists.

## Memory architecture

There are TWO project transcript directories under `C:\Users\srlev\.claude\projects\`:
- `C--Users-srlev\` (created when Claude is launched from `C:\Users\srlev\` or anywhere outside the AI Brain vault)
- `C--Users-srlev-OneDrive-Documents-Claude-AI-Brain-1-0\` (created when Claude is launched from the AI Brain vault)

**They share the same memory directory.** The AI Brain project's `memory\` is a Windows junction (symlink-equivalent) pointing at `C--Users-srlev\memory\`. So every Claude Code session, no matter where launched, reads and writes the same memory files. There is one canonical memory directory, accessed via two paths.

**Canonical path:** `C:\Users\srlev\.claude\projects\C--Users-srlev\memory\`
**Junction path:** `C:\Users\srlev\.claude\projects\C--Users-srlev-OneDrive-Documents-Claude-AI-Brain-1-0\memory\`

Both paths resolve to the same files. Writes through either are visible through the other.

## Hooks (configured in `C:\Users\srlev\.claude\settings.json`)

### Stop hooks (fire after every assistant turn)

1. **`sync-memory.ps1`** at `C:\Users\srlev\.claude\sync-memory.ps1`
   - Reads memory files from the canonical directory and rewrites the `<!-- MEMORY-SYNC-START -->` ... `<!-- MEMORY-SYNC-END -->` block in `C:\Users\srlev\.claude\CLAUDE.md`.
   - This is what makes memory visible to all Claude Code sessions globally (any session reads `~/.claude/CLAUDE.md`).
   - Reads from the canonical path; junction means writes from any project end up in canonical.

2. **`vault-log-reminder.ps1`** at `C:\Users\srlev\.claude\hooks\vault-log-reminder.ps1`
   - Nags the assistant to log substantive sessions into the vault at end of turn.
   - Soft reminder, not enforced.

### SessionStart hooks (fire when a session opens, including `/clear` and `/resume`)

3. **`vault-pull.ps1`** at `C:\Users\srlev\.claude\hooks\vault-pull.ps1`
   - Runs `git -C "<vault>" pull --rebase --autostash` to bring down any commits pushed to GitHub since last session. The MCP server (used by chat and Cowork) commits straight to `origin/main`, so without this pull, Code sessions miss memory updates made outside of Code.
   - After the pull, invokes `sync-memory.ps1` so the canonical memory dir catches up via robocopy before the assistant starts reading files. The `~/.claude/CLAUDE.md` MEMORY-SYNC block has already been loaded into the session at this point, so the *index* in the current session is one session stale; per-file reads are correct.
   - Targets the vault root explicitly via `git -C`, so launching from inside a worktree does not pull into the worktree's branch.
   - Fails silently (exits 0) if the vault folder is missing or `git pull` fails (offline, lock contention, etc.). Hook never blocks session start.
   - Ordered before `vault-prior-session-review.ps1` in `settings.json` so the review reads up-to-date memory.

4. **`vault-prior-session-review.ps1`** at `C:\Users\srlev\.claude\hooks\vault-prior-session-review.ps1`
   - Two responsibilities (in priority order):
     - **Always:** verifies the project's `MEMORY.md` index lines match the underlying memory files. Flags structural drift (file indexed but missing from disk; file on disk but not indexed) and semantic drift (file frontmatter and index entry share zero substantial keywords). Surfaces the issues to the assistant so they can be fixed before responding to the user.
     - **Always (any launch location):** finds the most recent prior session transcript across both project directories (`C--Users-srlev` and `C--Users-srlev-OneDrive-...`), and instructs the assistant to recover artifacts, log decisions, persist feedback rules, and write a conversation log into the vault. Uses sentinel files at `C:\Users\srlev\.claude\hooks\.vault-log-state\processed-<session-id>` to avoid re-processing.
   - The hook is portable: works from any working directory. The vault review now fires regardless of launch location.
   - File is intentionally pure ASCII (PowerShell 5.1 reads `.ps1` files as ANSI without a BOM, which would corrupt non-ASCII bytes). The regex uses `—` and `–` escapes to match em-dash and en-dash in MEMORY.md index lines.

## Scripts (not hooks)

5. **`backup-claude-folder.ps1`** at `C:\Users\srlev\.claude\scripts\backup-claude-folder.ps1`
   - Robocopies `C:\Users\srlev\OneDrive\Documents\Claude\` to `C:\Users\srlev\ClaudeBackups\YYYY-MM-DD\` and prunes anything older than 12 weeks.
   - Note: this does NOT cover `C:\Users\srlev\.claude\projects\` or memory. Memory backup is implicit via the sync to global CLAUDE.md, which IS in the OneDrive folder via... wait, no, global CLAUDE.md is at `~/.claude/CLAUDE.md` which is also outside the backup. Memory is currently NOT backed up by this script.

6. **`register-claude-backup-task.ps1`** at `C:\Users\srlev\.claude\scripts\register-claude-backup-task.ps1`
   - One-time install for the Windows scheduled task `ClaudeFolderWeeklyBackup`. Already registered.
   - Schedule: every Sunday at 12:00 PM, catches up if the laptop was asleep.

## Vault structure

The vault is a separate concept from memory. Memory is loaded automatically into every Claude Code session. The vault is markdown notes Samuel reads in Obsidian.

**Vault root:** `C:\Users\srlev\OneDrive\Documents\Claude\AI Brain 1.0\`

| Folder | Purpose |
|---|---|
| `00_Index/` | Top-level orientation (Active-Projects.md, About-Me.md). Read at session start in vault. |
| `10_Projects/` | One file per project. Active or recently active. |
| `20_Conversations/` | Bullet logs of substantive conversations. `YYYY-MM-DD - Topic.md`. |
| `30_Knowledge/` | Atomic notes. One idea per file. |

The vault is governed by `C:\Users\srlev\OneDrive\Documents\Claude\AI Brain 1.0\CLAUDE.md`, which is loaded only when a Claude Code session is launched from inside the vault folder.

## Permission model

`C:\Users\srlev\.claude\settings.local.json` is in wildcard mode:
- Allow: `Bash(*)`, `PowerShell(*)`, broad Read/Edit/Write under `~/.claude/`, the vault, and the OneDrive Claude folder.
- Deny: 28 destructive patterns (`rm -rf /`, `dd if=*`, `mkfs*`, `curl|sh`, etc.).

This trades fine-grained control for zero permission prompts during normal work. The Stop hook auto-allowlist (`fewer-permission-prompts` skill) is now redundant given the wildcard allow.

## When you find this file useful

Before suggesting any of the following, check whether it already exists here:
- "Build a SessionStart hook to..."
- "Create a sync mechanism for memory..."
- "Set up a scheduled backup..."
- "Add a check that verifies the index..."
- "We need a way for memory to be shared across sessions..."

If it's documented here, use the existing infrastructure. Don't reinvent it.
