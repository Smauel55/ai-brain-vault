# CLAUDE.md — Vault Operating Instructions

> This file auto-loads at the start of every Claude Code session launched from this folder. It tells Claude how to use Samuel's second brain.

## What this vault is

This is **Samuel's second brain** — a long-term knowledge base where context, decisions, and progress persist across sessions. The goal is that Claude should never need to be re-prompted on basic context: who Samuel is, what projects are active, what's been decided previously.

## Read these first, every session

At the start of any new conversation, before doing anything else, read:

1. `00_Index/About-Me.md` — who Samuel is, preferences, working style
2. `00_Index/Active-Projects.md` — what's currently in flight

That is enough context for most conversations. If the user mentions a specific project by name, also read the matching file in `10_Projects/`.

## Folder map

| Folder | What goes here |
|---|---|
| `00_Index/` | Top-level orientation files. Read at start of every session. |
| `01_Memory/` | Mirror of Claude Code's auto-memory dir. Auto-synced by a Stop hook. Don't edit by hand in Obsidian; edit in Code or via the MCP server and it will propagate. |
| `10_Projects/` | One file per active or recent project. File name = project name. |
| `20_Conversations/` | One file per meaningful conversation. Named `YYYY-MM-DD - Topic.md`. Use `_template.md` as the starting point. |
| `30_Knowledge/` | Atomic notes — one idea, fact, or reference per file. Linked from elsewhere. |
| `.obsidian/` | Obsidian config. Do not touch. |

## End-of-conversation protocol

When a conversation produces lasting value (a decision, a plan, learning, a project update), before the conversation ends:

1. **Log it.** Write a new file in `20_Conversations/` using the template format. Keep summaries short — bullet points over prose.
2. **Update the relevant project.** If the conversation moved a project forward, update its file in `10_Projects/`.
3. **File new knowledge.** If we generated reusable knowledge (a framework, a how-to, a definition), put a brief note in `30_Knowledge/`.
4. **Update Active-Projects** if status changed (started, paused, completed).

Do this without asking — it's the whole point of the vault.

## Linking

Use Obsidian wiki-links: `[[Project Name]]`, `[[2026-05-08 - Topic]]`. Linking is what makes this a brain rather than a folder of notes.

## Style rules

- Bullet-first. Prose only when nuance requires it.
- Front-matter on every note: `created`, `updated`, `tags`. Example:
  ```yaml
  ---
  created: 2026-05-07
  updated: 2026-05-07
  tags: [project, active]
  ---
  ```
- Keep file names short and human-readable. Spaces are fine; Obsidian handles them.
- Don't create files just to be thorough. Create them when there's something to remember.

## Things not to do

- Don't edit `Welcome.md` or `.obsidian/`. Both are vault default infrastructure.
- Don't create deeply nested folders. Two levels deep is the cap.
- Don't write speculative content into the vault. Only durable, reusable context.

## OneDrive note

This vault lives in OneDrive (`C:\Users\srlev\OneDrive\Documents\Claude\AI Brain 1.0`), so it backs up and syncs automatically. Avoid editing the same file simultaneously from Obsidian and Claude Code on different devices — OneDrive will create `*-conflicted` copies.

## Memory sync

`01_Memory/` is a mirror of the Claude Code auto-memory directory at `~/.claude/projects/C--Users-srlev/memory/`. A Stop hook (`sync-memory.ps1`) runs two robocopy passes after every session, one each direction, both with `/XO` (skip older). Net effect: newest mtime wins per file, nothing ever deleted. The vault copy is what gets pushed to GitHub and served by the MCP server, so chat and Cowork can read the same memory that Code reads locally.

If you need to update a memory entry, edit it in `~/.claude/projects/C--Users-srlev/memory/` (Code reads from there directly) or use the MCP server's `vault_create` / `vault_append` tools on a file in `01_Memory/`. Either way, both copies converge on the next Stop.

## Global memory

If you ever read facts that are true across all of Samuel's projects (not project-specific), they may belong in `~/.claude/CLAUDE.md` (the global memory file) instead of here. Suggest moving them when appropriate.
