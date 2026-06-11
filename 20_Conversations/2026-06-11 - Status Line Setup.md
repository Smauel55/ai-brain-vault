# 2026-06-11 - Status Line Setup

Config/infra tweak. Not project work.

- Samuel asked why he couldn't see his context window in the terminal. Clarified: this session runs as a background job; the live context gauge only shows in the interactive `claude` terminal (the window where he typed `claude`). `/context` prints the breakdown inline; no special mode needed.
- Concluded a context gauge is low-value for his no-code workflow, but he asked to set one up anyway showing context bar + model + effort level.
- Verified the Claude Code status line JSON schema from docs (code.claude.com/docs/en/statusline). Relevant fields: `model.display_name`, `context_window.used_percentage`, `effort.level` (absent on models without the effort param).
- Built **`C:\Users\srlev\.claude\statusline.ps1`** — PowerShell script: cyan model name, 10-block context bar (green <70%, yellow 70-89%, red 90%+), % used, effort level. Bar chars created by code point so the source file stays pure ASCII (avoids PS 5.1 encoding garble); sets console output to UTF-8.
- Wired into **`C:\Users\srlev\.claude\settings.json`** via `statusLine` command: `powershell -NoProfile -ExecutionPolicy Bypass -File C:/Users/srlev/.claude/statusline.ps1` (forward slashes per Windows/Git Bash routing guidance).
- Tested with mock JSON — renders correctly. Will appear in his next interactive session (background sessions don't show it); may need one restart + trust prompt acceptance.

## Civic / pointed-pieces policy revisit (discussed, NOT yet confirmed)

- Samuel raised reopening the earlier ban on "pointed" pieces (the example was the birthright-citizenship Open Letter that read as aimed at President Trump). After his teacher meeting, he believes civic-subscription teachers actually want pointed pieces — pointed but not aggressive — because AP Lang teaches persuasion and the richest rhetoric takes a position.
- Claude's recommendation (Samuel had not explicitly accepted by session end): separate **pointed at an issue** from **pointed at a named person**. Allow issue-pointed advocacy (e.g. "An Open Letter on Birthright Citizenship," target = the policy) — rhetorically rich, analyzable, fine. Keep the **hard ban on targeting named living politicians** ("...to President Trump") on every tier, since person-targeting is what reads as a partisan shot. This maps to the teacher's own "pointed but not aggressive" line — the aggressive part is the person-targeting.
- Net: this CLARIFIES rather than overturns [[feedback_opener_neutrality]] (the existing ban was on person-targeting; issue-advocacy was over-suppressed). OPEN action: Samuel to confirm, then update Editorial-Standards Gate 0 + neutrality memory to explicitly permit issue-pointed advocacy on the civic tier while preserving the named-living-politician ban.
</content>
