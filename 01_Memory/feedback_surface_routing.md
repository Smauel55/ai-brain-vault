---
name: Surface routing — flag when Cowork or Chat would fit better
description: When Samuel asks Code to do something that would be genuinely better in claude.ai chat or Cowork, point it out. Applies in every session, not just one-off.
type: feedback
---

Samuel uses three Claude surfaces: Code (primary), claude.ai chat, and Cowork. The AI Brain MCP server shares vault context across all three, so handoffs are seamless. Samuel's stated preference: Code-primary for ~80% of work, with chat and Cowork reserved for cases where they're clearly the better tool.

**HOW TO APPLY**

When Samuel asks Code to do something, briefly consider whether another surface would actually serve him better. If yes, mention it in one line before or alongside doing the work. Don't refuse to do the task in Code — just flag the better fit so he can decide.

**Strong signals to suggest switching:**

- Long-running agent work that would benefit from running while Samuel is away from his computer → Cowork (it runs in the cloud for hours, he doesn't have to leave his computer on or watch).
- Tasks that specifically need a Cowork-only plugin or connector not available in Code.
- Samuel mentions he's on his phone, away from his desk, or in transit → claude.ai chat is more comfortable than Code on mobile.
- Pure brainstorming or writing with no file output AND he wants quick back-and-forth → chat's conversational UI is friendlier than a terminal.

**Do NOT suggest switching when:**

- Task involves local file edits, terminal commands, builds, deploys, or anything filesystem-touching → Code is the right tool.
- The fit is only marginally better elsewhere — don't be a nag.
- Samuel is mid-flow on a multi-step task in Code; switching mid-stream costs more than it saves.
- Task takes under ~5 minutes; switching overhead exceeds the benefit.

**Format**

One-line aside, not a full pitch. Example: "I'll handle this. By the way, if you ever want this kind of thing running overnight while you're not at your computer, Cowork can do it as a background job." Then do the task.

**Handoff mechanics (good to know)**

Cross-surface handoff is fast: chat or Cowork writes via MCP, commits to vault repo immediately, Samuel's local Obsidian pulls within ~5 min. He can finish a thought in chat and pick it up in Code five minutes later. If suggesting a handoff, offer to write a brief handoff note to `20_Conversations/` via `vault_create` so the next surface has context.

**WHY Samuel cares**

He wants each task done on the most efficient surface, and the AI Brain MCP exists specifically to make cross-surface workflows seamless. But he doesn't want to manually evaluate routing every time. Surfacing the suggestion when it matters lets him benefit from multi-surface workflow without thinking about it.
