---
created: 2026-05-10
updated: 2026-05-10
tags: [conversation, infrastructure, memory]
project: "[[Bourbon Site]]"
---

# 2026-05-10 — Memory recovery and permission overhaul

## Context

Samuel asked if Claude remembered the bourbon website. Claude didn't — that work happened May 8, but the SessionStart auto-log hook wasn't built until May 9. The session pivoted into fixing the gap permanently.

## Key points

- Bourbon site was built May 8, vault protocol existed May 7, but no automation tied them together until May 9.
- The vault-log-reminder Stop hook only nags at end of turn; it doesn't read prior transcripts on session start.
- Claude Code only loads `settings.json` and `settings.local.json` at session start. Mid-session edits don't take effect.
- The `fewer-permission-prompts` skill is built into Claude Code (not a file on disk), and was generating exact-command-match rules instead of wildcards, which is why permission prompts kept recurring.

## Decisions

- Built `vault-prior-session-review.ps1` as a SessionStart hook. It injects a protocol prompt telling Claude to grep the prior transcript, recover unsaved artifacts, log substantive sessions, and write a sentinel so a transcript is never re-processed.
- Switched permissions to wildcard mode in `settings.local.json`: `Bash(*)` + `PowerShell(*)` allow, with 28 deny patterns covering destructive commands (`rm -rf /`, `dd if=*`, `mkfs*`, `curl|sh`, etc.). Trades fine-grained control for zero permission prompts.
- Set up a weekly Windows scheduled task (`ClaudeFolderWeeklyBackup`) that robocopies the entire Claude folder to `C:\Users\srlev\ClaudeBackups\YYYY-MM-DD\`, prunes anything older than 12 weeks. Runs Sundays at noon, catches up if asleep. First snapshot taken (9.79 MB).

## Action items

- [ ] Samuel — restart Claude Code to load the new hook + permission rules.
- [ ] Next session — verify the SessionStart hook fires and produces a clean review pass (this session).

## Artifacts produced

- Recovered 4 bourbon HTML iterations from May 8 transcript → [10_Projects/Bourbon Site/iterations/](../10_Projects/Bourbon%20Site/iterations) (v1, v2, v3, v4-final).
- New project summary → [Bourbon Site](../10_Projects/Bourbon%20Site.md).
- New SessionStart hook → `C:\Users\srlev\.claude\hooks\vault-prior-session-review.ps1`.
- New backup script + scheduled task → `C:\Users\srlev\.claude\scripts\backup-claude-folder.ps1`, `register-claude-backup-task.ps1`.

## New knowledge to file

- "Settings load only at session start" is a recurring foot-gun — could be a knowledge note if it bites again. Skipping for now.

## Open threads

- None. The verification is just whether the SessionStart hook fires cleanly on next launch.
