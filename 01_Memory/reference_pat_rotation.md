---
name: AI Brain MCP — PAT rotation reminder
description: GitHub fine-grained PAT used by the AI Brain MCP Cloudflare Worker expires around 2027-05-11. Rotate before then.
type: reference
---

The fine-grained GitHub Personal Access Token powering the AI Brain MCP Cloudflare Worker expires around **2027-05-11** (1 year from generation on 2026-05-11).

**Token identity:** PAT named "AI Brain MCP" at github.com/settings/personal-access-tokens, scoped to ONLY the `ai-brain-vault` repo with permissions Contents: Read and write, Metadata: Read.

**Symptom of expiry:** every MCP tool call starts returning errors. Samuel will see "AI Brain connector failed" or similar in chat, Code, and Cowork.

**Rotation procedure (when expiry is near, or after expiry):**
1. Go to github.com/settings/personal-access-tokens, find "AI Brain MCP", click "Regenerate token" (or generate a fresh one with the same scope and permissions).
2. Copy the new token.
3. In the Worker project directory: `wrangler secret put GITHUB_TOKEN`, paste the new token when prompted.
4. `wrangler deploy` to push the secret to production.
5. On GitHub, revoke the old token if still active.

If Samuel mentions any of: "MCP not working," "vault tools failing," "connector disconnected" after mid-2027, check the PAT first.
