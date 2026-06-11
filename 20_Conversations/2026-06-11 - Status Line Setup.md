# 2026-06-11 - Status Line Setup

Config/infra tweak. Not project work.

- Samuel asked why he couldn't see his context window in the terminal. Clarified: this session runs as a background job; the live context gauge only shows in the interactive `claude` terminal (the window where he typed `claude`). `/context` prints the breakdown inline; no special mode needed.
- Concluded a context gauge is low-value for his no-code workflow, but he asked to set one up anyway showing context bar + model + effort level.
- Verified the Claude Code status line JSON schema from docs (code.claude.com/docs/en/statusline). Relevant fields: `model.display_name`, `context_window.used_percentage`, `effort.level` (absent on models without the effort param).
- Built **`C:\Users\srlev\.claude\statusline.ps1`** — PowerShell script: cyan model name, 10-block context bar (green <70%, yellow 70-89%, red 90%+), % used, effort level. Bar chars created by code point so the source file stays pure ASCII (avoids PS 5.1 encoding garble); sets console output to UTF-8.
- Wired into **`C:\Users\srlev\.claude\settings.json`** via `statusLine` command: `powershell -NoProfile -ExecutionPolicy Bypass -File C:/Users/srlev/.claude/statusline.ps1` (forward slashes per Windows/Git Bash routing guidance).
- Tested with mock JSON — renders correctly. Will appear in his next interactive session (background sessions don't show it); may need one restart + trust prompt acceptance.
</content>
