---
created: 2026-05-07
updated: 2026-05-07
tags: [knowledge, claude-code, reference]
---

# Claude Code memory hierarchy

How Claude Code decides what context to load into a session.

## The three layers

1. **Root `CLAUDE.md`** in the folder where `claude` is launched.
   Auto-loads every session. Roughly the first 200 lines / 25KB are pulled in.
2. **Nested `CLAUDE.md`** in subfolders.
   Not preloaded. Loads on demand when Claude touches files inside that subfolder. Useful for per-project context that shouldn't bloat the main one.
3. **Global `~/.claude/CLAUDE.md`** (Windows: `C:\Users\<you>\.claude\CLAUDE.md`).
   Loads across all projects. Use for cross-cutting personal context: tone preferences, working style, things true regardless of project.

## Practical rule

- Vault-specific operating instructions → root `CLAUDE.md` of the vault.
- Project-specific context → that project's folder, as a nested `CLAUDE.md`.
- Personal preferences true everywhere → global file.

## Inspecting what's loaded

Inside Claude Code, the `/memory` command lists all currently loaded memory files for the session.

## Source

Verified from official docs: https://code.claude.com/docs/en/memory (May 2026).
