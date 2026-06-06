---
created: 2026-05-07
updated: 2026-06-06
tags: [index, projects]
---

# Active Projects

> One line per project. Status emoji optional. Detailed notes live in `10_Projects/[Project Name].md`.

## In flight

- 🟢 [[Second Brain Setup]] — Build out this vault and the Claude Code workflow around it. *Status: in progress (started 2026-05-07).*
- 🟢 [[Caught Up AI]] — AP Lang teacher daily-brief startup. *Status: spec v1.1 (D-002 script revision, D-003 scope cut); one-pager v0.4 paused; teacher meeting brief v0.2 with real sample "The Quiet Classroom" (2026-05-19); customer discovery ~May 25. Product work otherwise paused until ~May 25 (Claude mastery plan).*
  - Website thread (2026-06-03): UNBLOCKED. Dropped Cloudflare/caughtup-ai.com, switched to **caughtupai.com** (no hyphen) on **Porkbun**, connected to Base44. Site live; Google Search Console Domain property verified; sitemap submitted; title/meta set. SEO paused at the content stage. Full status and next steps in [[Website-Setup]].
  - Product design thread (2026-06-04): Began product design (journey map agreed, paused before deep-designing Landing). Hit the core CONTENT ENGINE blocker. Verified: to reproduce + annotate + sell, only PD/CC0/CC-BY licenses work (NC and ND both fatal); the free current pool is too thin for a daily cadence (Global Voices the lone real source). Open decision: the content engine, with licensing vs AI-with-editing as the finalists. Full detail in [[2026-06-04 - Product design and content sourcing]]; state in [[Content-Sourcing]].
  - Content engine pivot (2026-06-05): leaning to FULL AI-GENERATION (write each piece from verified facts, do not reproduce source text), which sidesteps the licensing wall.
  - Opener samples + PDF format (2026-06-06): named the product unit an **"Opener"** (teacher copy / student copy per edition; not a "brief"). Built a reusable generation prompt ([[caughtupai-sampleprompt-V1]]) and a PDF generator (10_Projects/Caught Up AI/Sample-Briefs/render_briefs.py) that produces real-news Openers in the format of Samuel's "Teacher Meeting Brief v0.2". 3 sample editions live (Ledger/Long Look/Tribute). Device labels locked to a fixed AP list ([[Rhetorical-Device-Vocabulary]]). **PAUSED mid-formatting; resume from the Open threads in [[2026-06-06 - Caught Up AI Opener samples and format]].**
  - Prose engine v2 DELIVERED (2026-06-05): ran the commission as a 56-agent workflow. v2 apparatus written to 10_Projects/Caught Up AI/ (10 files): [[Style-Palette]] (7 registers: Ledger, Open Letter, Reckoning, Tribute, Long Think, Witness Stand, Long Look), [[Structural-Templates]], [[Register-Specs]], [[Anti-Tell-List]], [[Cross-Piece-Sameness-Rubric]], [[Accuracy-Guardrail]], [[Annotated-Exemplars]], [[Blind-Test-Protocol]], [[Generation-Briefs]], [[Prose-Engine-Research-Report]]. Supersedes (does not overwrite) [[Writing-Manual]]. **NEXT ACTIONS:** (1) read Style-Palette + Register-Specs + Generation-Briefs + Annotated-Exemplars; (2) calibrate the 6 of 8 out-of-band exemplars and feed fixes into Register-Specs/Anti-Tell-List; (3) for the real blind test, make placeholder-free verified-fact pieces and recruit AP-Lang teacher judges. NOTE: the automated proxy pilot (7/7) is a pre-screen only and is confounded by leftover placeholder tags; the decisive test is the human panel. Detail: [[2026-06-05 - Prose engine v2 build]].

## Paused / on hold

_(Projects deferred but not abandoned. Add a one-line reason.)_

- ⏸ [[Bourbon Site]] — Whisky Site Test, capability-test for frontend builds. *Reason: not a real venture, kept as reference.*

## Recently completed

_(Move projects here when done. Keep the last 30 days; archive older ones.)_

## Backlog

_(Things you want to start but haven't. One line each — don't expand into project files until you commit to starting.)_

---

**How to use this file:**

When you start a project, add a line under "In flight" and create `10_Projects/[Project Name].md`. When status changes, move the line. Don't let this file grow past one screen — that's the signal to archive.
