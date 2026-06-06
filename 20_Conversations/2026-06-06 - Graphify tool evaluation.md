---
created: 2026-06-06
updated: 2026-06-06
tags: [conversation, tooling, evaluation]
project: 
---

# 2026-06-06 — Graphify tool evaluation

## Context

Samuel asked whether the tool in a YouTube video (Chase AI, "This Open Source Repo Just Solved Claude Code's #1 Problem") was worth integrating, suspecting it was a better way to store the vault's data.

## Key points

- Repo is Graphify (https://github.com/safishamsi/graphify), ~60k stars. Turns a codebase into a queryable knowledge graph so an AI agent answers questions about it with fewer tokens instead of grepping files.
- Three passes: pass 1 tree-sitter AST (code, local, free); pass 2 Whisper (audio/video); pass 3 LLM semantic analysis on docs/PDFs/images (costs API). Has --obsidian and --wiki export flags. Auto-rebuilds on git commit via hook.
- Demo token win: ~80k with Graphify vs ~200k without, on a large-repo question. The win comes from avoiding repeated crawls of a big codebase.
- The video's "memory" framing conflates two different problems: Graphify solves efficient comprehension of a large codebase (retrieval cost); the vault solves cross-session context persistence (curation/continuity). Same word, different problem.

## Decisions

- NOT integrating Graphify now. Reasons: it is built for large codebases (the vault is a few dozen curated markdown notes); the vault already gives persistence + curated index + wikilink graph + MCP search; there is no large-repo token cost to cut; and its commit hook would trigger LLM-pass rebuilds on every ~30-min vault-auto commit = recurring API cost for no real gain.

## Open threads

- Revisit only if (a) Samuel starts a real, sizable codebase, or (b) the vault grows to hundreds/thousands of notes and retrieval token cost becomes visible. If revisited, run on demand via --obsidian, not on every commit.
