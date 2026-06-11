---
created: 2026-05-07
updated: 2026-06-10
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
  - Teacher meeting prep (2026-06-06): meeting with Samuel's own AP Lang teacher in ~2 days (target 2026-06-08). Built **Teacher Meeting Brief v0.3** ([[Teacher-Meeting-Brief-v0.3]]) as a private run-of-show, rebuilt from v0.2 for the AI-generation product. Open-about-AI disclosure; four goals (expert quality review, authenticity verdict, discovery, recruit). Highest-value block = an AP expert-validation checklist (device labels, MCQ validity, answer keys, AP alignment). Sharpest risk flagged: the AI-author pedagogy tension. Detail in [[2026-06-06 - Teacher Meeting Brief v0.3]].
  - Opener samples + PDF format (2026-06-06): named the product unit an **"Opener"** (teacher copy / student copy per edition; not a "brief"). Built a reusable generation prompt ([[caughtupai-sampleprompt-V1]]) and a PDF generator (10_Projects/Caught Up AI/Sample-Briefs/render_briefs.py) that produces real-news Openers in the format of Samuel's "Teacher Meeting Brief v0.2". 3 sample editions live (Ledger/Long Look/Tribute). Device labels locked to a fixed AP list ([[Rhetorical-Device-Vocabulary]]). **PAUSED mid-formatting; resume from the Open threads in [[2026-06-06 - Caught Up AI Opener samples and format]].**
  - Opener customization (2026-06-07): DECIDED. Difficulty setting SCRAPPED (revisit only after AP Lang market saturation, not near-term). Political-intensity dial is the one customization axis, ADOPTED: low-cardinality setting at signup (default neutral), implemented as topic routing not a parallel pipeline. Rejected the 5-10/day buffet (breaks print-and-go + multiplies QA). NEXT: design the political dial (tier count/wording + topic-bucket routing). Detail in [[2026-06-07 - Opener customization strategy]].
  - Editorial guardrails (2026-06-08): Samuel flagged two content problems in the sample Openers. Built [[Editorial-Standards]] (D9) as Gate 0 above every register: (1) NEUTRALITY FIREWALL (no political side, no attack on a person/group, even on the civic tier; Open Letter addressee and Reckoning culprit may never be a politician/party, route to Ledger or drop); (2) PLAIN-KNOWLEDGE ACCESSIBILITY (no unexplained jargon above HS common knowledge; gloss specialist terms or cut). Wired into Generation-Briefs, the sample prompt, Register-Specs, and Style-Palette. Open: regenerate or pull the ~8 existing partisan/jargon samples before any demo. Detail in [[2026-06-08 - Opener content guardrails]].
  - Pre-launch planning (2026-06-08): outlined the full pre-launch roadmap (7 workstreams + critical path). Key reframe: set the launch date by the school calendar (target late-July–early-Sept back-to-school window, aligns with The Garage Sept 2026), not by when testing finishes. Most underrated items: daily operational reliability and launch timing. Offered to build a tracked Launch-Checklist (pending go-ahead). Detail in [[2026-06-08 - Pre-launch roadmap]].
  - Daily edition built (2026-06-08): generated the first full clean daily edition for today's teacher meeting: 3 Openers across 3 registers (Long Look / Tribute / Ledger) from verified real news (Tianwen-2 reaching asteroid Kamo'oalewa; a Peabo Bryson tribute; the GAO report on jobs-survey data quality), teacher + student PDF each (6 files in Sample-Briefs/, from openers-2026-06-08.json via render_batch.py). First edition produced end-to-end under [[Editorial-Standards]] Gate 0 (neutrality + plain-knowledge); all three topics neutral by construction, with distinct templates/openers/closes and an FRQ mix (Q2/Q2/Q3). Detail in [[2026-06-08 - Three Openers for teacher meeting]].
  - Teacher meeting held + headnotes added (2026-06-10): first teacher meeting went well (2026-06-08, Samuel's own AP Lang teacher; very interested). Working his feedback one issue at a time. Issue #1: prose reads impersonal; fix = a register-aware, AP-exam-style **headnote** (one or two italic sentences naming speaker/audience/occasion) on both copies, written FIRST as a forcing function. Built: [[Headnote-Spec]] (D10), `headnote` field rendered on both copies in render_opener_v2.py (verified, backward-compatible), and wired into [[Generation-Briefs]] (write-first step + slot in all 7 briefs + Gate 2 check) and [[caughtupai-sampleprompt-V1]]. Invented personas framed by role (no fake names); no AI disclosure in the headnote. Detail in [[2026-06-10 - Teacher feedback, headnotes]]. Open: more feedback issues to come; demo PDFs not yet backfilled with headnotes.
  - Delivery frequency customization (2026-06-10): teachers will choose how often and which days they get Openers (1-5 days/wk, specific weekdays). DECIDED, three forks all to the lean option: (1) mechanism = magic-link preferences page, NO portal/login (set at signup, changeable via a signed footer link; full portal deferred until multi-seat/billing/archive reasons co-exist); (2) content model = broadcast + edition-rolled rotation (one daily edition, frequency is a receive-filter; register rotation advances by edition date not weekday so part-week teachers still cycle the palette; rejected per-teacher streams); (3) pricing = one price, frequency is free (a churn lever, not a tier). Consistent with the political-dial precedent. Not yet built. Detail in [[2026-06-10 - Delivery frequency customization]].
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
