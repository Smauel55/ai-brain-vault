---
created: 2026-05-12
updated: 2026-05-12
tags: [conversation, mcp, infrastructure]
project: "[[Second Brain Setup]]"
---

# 2026-05-12 — AI Brain MCP setup

## Context

Samuel wanted the AI Brain vault and Claude Code memory to be accessible from claude.ai chat and Cowork, not just from Claude Code locally. We built a remote MCP server backed by GitHub so all three surfaces read and write the same vault.

## Key points

- Vault is now a private GitHub repo at `Smauel55/ai-brain-vault`. Local copy stays in OneDrive; Obsidian Git plugin auto-commits and auto-pulls every 5 min.
- Memory dir at `~/.claude/projects/C--Users-srlev/memory/` mirrors into the vault's `01_Memory/` via two robocopy passes in the existing `sync-memory.ps1` Stop hook. Newest mtime wins per file, nothing deleted.
- MCP server is a Cloudflare Worker at `https://ai-brain-mcp.samuel-levy.workers.dev`. Built from the cloudflare/ai `remote-mcp-github-oauth` template. Source lives at `C:\Users\srlev\Dev\ai-brain-mcp\`.
- Five tools exposed by the server: `vault_search`, `vault_list`, `vault_read`, `vault_create`, `vault_append`. No `update`, `delete`, or `rewrite` tools by design.
- Auth: OAuth via GitHub. Samuel's GitHub login (Smauel55) is the only allowed user. Worker holds a fine-grained GitHub PAT (Contents R/W on the vault repo only, Metadata R) as a secret to perform repo operations.
- Cookie encryption key, OAuth client ID/secret, and the PAT are stored as Cloudflare Worker secrets via `wrangler secret put`.
- Cloudflare account uses subdomain `samuel-levy.workers.dev`; Workers free tier handles personal usage indefinitely.
- Registered the MCP in Claude Code via `claude mcp add` (stored in `~/.claude.json`) and in claude.ai chat via Settings -> Connectors. Cowork registration in progress.

## Decisions

- **Read + add permission model, no rewrite or delete.** Enforced by tool-surface absence (the model literally cannot ask for an op that doesn't exist). Chat and Cowork can read anything and create new files or append to existing ones; they cannot replace bytes or delete. Motivation: Samuel wants progress made in any surface to propagate, but never silently overwrite hand-curated content.
- **Vault stays in OneDrive.** Avoided forcing a path migration. OneDrive + git coexist for a single-editor setup; the Obsidian Git 5-min commit interval gives OneDrive time to sync first.
- **Vault is the single source of truth.** Memory dir is mirrored INTO the vault rather than the other way around, so GitHub holds everything chat and Cowork can see.
- **Skipped Node-free deploy paths in favor of `wrangler` local CLI.** Samuel installed Node.js LTS; I keep all deploy commands in PowerShell with PATH refresh and bash with explicit `export PATH`.
- **50KB hard cap on `vault_read`.** Protects against pathological token spend on a single oversized file; tool errors with a hint to use `vault_search` instead.
- **Path-match fallback in `vault_search`.** GitHub's code search index has multi-hour lag for fresh private repos. The tool now does both GitHub Search (content) AND filename substring match (path), merges results, returns either or both. Works immediately even on a cold index.

## Bugs hit, root-causes, fixes

- **PowerShell pipeline added a UTF-8 BOM to secrets.** First deploy round, `'Ov23...' | npx wrangler secret put GITHUB_CLIENT_ID` uploaded `<BOM>Ov23...` as the value. GitHub returned 404 on `/login/oauth/authorize?client_id=%EF%BB%BFOv23...`. Root cause: PowerShell 5.1 encodes string-to-native-exe stdin with BOM by default. Fix: re-uploaded all four secrets via bash with `printf '%s' VALUE | npx wrangler secret put NAME`. `printf` writes raw bytes, no BOM. Lesson for future Worker secret rotations: always use bash + printf, never PowerShell pipe.
- **Workers subdomain not provisioned at first deploy.** Cloudflare requires you to visit Workers & Pages once in the dashboard to claim a `*.workers.dev` subdomain. Samuel did that, picked `samuel-levy`, retried `wrangler deploy`. Worked.
- **TypeScript didn't know about Node `Buffer`.** Used Worker-native `TextEncoder` / `TextDecoder` + `btoa` / `atob` for base64 instead. No `@types/node` dependency needed.
- **Junk `skill-creator/` folder in vault from a prior session.** Cleaned with `git rm -r skill-creator` + commit + push. Anthropic's skill-creator is still available as a registered plugin skill; the folder was leftover scaffolding output.

## Action items

- [ ] Samuel — finish registering the MCP in Cowork (per-session toggle if needed) and run round-trip verification
- [ ] Samuel — rotate the GitHub OAuth Client Secret and fine-grained PAT once, since values were pasted in chat history. Not urgent.
- [ ] Samuel — verify the Cloudflare scheduled-task reminder for PAT rotation will fire on 2027-05-04 (one-shot routine `trig_013xp5GvpvT8vyZk9T6e39Ep`)
- [ ] Samuel — add a phone calendar reminder for 2027-05-04 "Rotate AI Brain MCP GitHub PAT" as a third layer of redundancy
- [ ] Future — consider adding `vault_update_section` (replace a specific markdown heading section, not the whole file) if the read+add model proves too limiting in practice

## New knowledge to file

- **Cloudflare Workers MCP setup pattern.** Could become an atomic note in `30_Knowledge/` documenting the Cloudflare template, secrets list (CLIENT_ID, CLIENT_SECRET, COOKIE_ENCRYPTION_KEY, GITHUB_TOKEN), KV namespace requirement, and OAuth callback URL flow. Useful if Samuel ever stands up another remote MCP.
- **GitHub Code Search indexing lag.** New private repos can take hours to a day before content search returns hits. Tree API and Contents API work immediately.
- **PowerShell stdin pipe BOM trap.** Worth a knowledge note for any future secret-rotation work.

## Open threads

- Search indexing on the new repo: confirm content search starts working within 24h.
- Path-based search fallback covers cases where the filename is descriptive (`reference_number_255.md` matches "number"). It does NOT cover keyword searches against file CONTENT (e.g., "what did I decide last Tuesday" can't be answered until GitHub indexes). Consider a smarter fallback later that fetches MEMORY.md and project files and greps in-Worker.
- Cowork session-level toggle behavior is unclear from our test. Samuel saw AI Brain in the Customize panel but Cowork didn't call the tools when prompted ambiguously. Need a more explicit prompt to confirm it actually works end-to-end.
