---
name: reference_graphify_tool
description: Graphify (codebase-to-knowledge-graph tool) — evaluated and parked; raise it when a large codebase or large vault appears
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1de63f48-5e07-4bde-8e00-e414f416aa7f
---

Graphify (https://github.com/safishamsi/graphify, ~60k stars) turns a codebase into a queryable knowledge graph so an AI agent answers structure questions with far fewer tokens than grepping files. Pass 1 = tree-sitter AST (code, local, free); pass 2 = Whisper (audio/video); pass 3 = LLM semantic analysis on docs/PDFs/images (costs API). Has `--obsidian` / `--wiki` export. Auto-rebuilds via a git commit hook. Demo: ~80k tokens vs ~200k on a large-repo question.

Evaluated 2026-06-06 (Chase AI video) and PARKED — not integrated. It solves large-codebase retrieval cost, not Samuel's cross-session context persistence, which [[reference_vault_infrastructure]] already handles. The commit hook would also fire LLM rebuilds on every ~30-min vault-auto commit = recurring cost for no gain.

**Why remembered:** Samuel asked me to proactively surface this when it becomes relevant, rather than re-evaluate from scratch.

**How to apply — bring Graphify up unprompted if EITHER trigger fires:**
- Samuel starts a real, sizable codebase (not the small Caught Up AI render scripts) that I have to reason about repeatedly.
- The AI Brain vault grows to hundreds/low-thousands of notes AND retrieval token cost becomes visibly high.
If revisited: run on demand (`--obsidian`), NOT on every commit, to avoid the auto-commit rebuild cost.
