---
name: Caught Up AI — project state
description: Full state of Samuel's AP Lang teacher startup as of May 2026
type: project
originSessionId: 0989c639-71c6-4076-bd4f-12a75fc43788
---
**What it is:** Daily 10–15 minute lesson opener for AP English Language & Composition teachers. Two auto-generated versions (student + teacher) delivered M–F at 6am local. One-time 4-minute setup form. Zero manual work per teacher after setup.

**Target customer:** ~10,000 U.S. high school AP Lang teachers. Spends 8–15 hrs/week on article prep. Already pays out of pocket for EdTech tools. Active on Facebook AP Lang groups and AP Lang subreddit.

**The daily artifact:**
- Student version: 350–450 word nonfiction article (current within 7 days), 2 discussion questions, 2–3 AP-style MC (no answers), 1 writing prompt (Q1/Q2/Q3, rotates per D-001)
- Teacher version: all above + rhetorical devices pre-marked with para/line refs, MC answer key, sample strong responses, common misconceptions, AP exam alignment notes
- Delivery: email (default) + web link + Google Doc + PDF

**Pricing:** $19.99/mo solo, $190/yr annual, $14.99/seat/mo dept (5+ seats annual), "Contact us" for school/district. 14-day free trial, no card required. One plan, no Pro tier.

**Key decisions locked:**
- AP Lang only in 2026 (not AP Lit, not other subjects)
- Dual-version output by default, no toggle
- 350–450 word article target
- 2 discussion questions per brief
- Writing prompt framed as homework/extended writing, not part of opener
- Annual billing default + summer-as-feature (no pause option)
- No Pro tier in year 1
- D-001 (May 2, 2026): AP unit handling = mixed-by-default rotation (Q1/Q2/Q3), teacher-version footer shows current state with one-click lock override. "Current AP unit" setup field now optional with "skip if cycling" framing.
- D-002 (May 13, 2026): Build-readiness session. Locked 7 decisions: (1) Samuel is the quality bar, AP Lang reviewer only on a defined trigger; (2) hallucination control = sample-based audit (position 2); (3) article sourcing = open/CC-commercial/public-domain only (option D); (4) format-drift = hybrid now, regression suite at ~200 teachers; (5) editorial neutrality = 3-tier framework draft; (6) ops = Claude support agent post-MVP + optimized infra targeting ~95% margin; (7) timeline reframe (see below). Discovery script revised → Product Brief v1.1. Core throughline: build risk is a 2027 scale-phase problem; September 2026 is a sales/evidence problem solvable with zero code.

**Timeline (revised by D-002, May 13 — calendar-collision fix):**
- ✅ Lock spec v1.0 — April 27, 2026; v1.1 (discovery script revision) — May 13, 2026
- Task #2: Teacher-facing one-pager (paused, see below)
- May 25 → end June 2026: customer discovery (target 30, realistic 15–25 solo)
- Jul → mid-Aug: NO classroom (school out). Concept/sample validation, collect pre-commitments, build safe delivery rails, recruit fall pilot cohort
- Mid/late Aug → September: Manual MVP runs for real (4 weeks, hand-written briefs in live classrooms)
- September: arrive at Northwestern with spec + interviews + live pilots + pre-commitments (NOT converted paying users — calendar makes that impossible before October)
- October: convert pilots to paying
- ⚠️ Samuel's homework: verify the Wildfire fall-2026 application deadline. If spring 2027, calendar collision evaporates and timeline relaxes.

**Current task (as of 2026-05-11, post-pivot):** Operator-level Claude mastery, no code. Third revision of the 2-week plan, same file at `C:\Users\srlev\.claude\plans\you-know-how-we-elegant-graham.md`. Samuel started Day 1 of the Python plan, hit a SyntaxError, decided 6 months of part-time Python would not make him a competent code reviewer, and pivoted to concept-only + operator skills. Week 1: conceptual map (model vs. harness, context, prompts, tools, slash/plan, skills, MCPs/agents/hooks). Week 2: directing Claude well (scoping, plan mode, verification by behavior, spotting bullshit, course-correcting, memory). Daily one-paragraph note in `30_Knowledge/claude-day-N.md`. No code, no new infrastructure. Caught Up AI product work paused until ~2026-05-25. Started 2026-05-11. Day 1 = model vs. harness distinction.

**Paused task (Task #2):** Teacher-facing one-pager at v0.4 with five outstanding edits (Zoom capitalization, "appreciated" softening, RA-vs-mixed-rotation tension, "entrepreneur" reframe, hyphenate "AP-style"). Resume after learning plan completes ~2026-05-24, or earlier if customer discovery interviews need it sooner.

**Teacher Meeting Brief (started 2026-05-17, discovery prep):** New in-room artifact, separate from the one-pager. v0.1 saved to project folder. Hybrid: Page 1 teacher-facing (One-Pager v0.3 voice), Back Page A illustrative sample day (labeled placeholder), Back Page B = Samuel's question script (12 Qs after two rounds of cuts on 2026-05-19: first the class-level-vocab question with the D-003 scope cut; then a question audit cut three more — old Q4 hypothetical pain-magnitude, old Q9 trust-loss folded into the cancellation probe as an error-category follow-up, old Q11 topics-to-avoid forced choice deferred to pilot. 6-Q core for short meetings: 2, 3, 4, 7, 8, 12). Sample brief written 2026-05-19: "The Quiet Classroom," original ~410-word essay on K-12 phone bans, with inline rhetorical-device marks (==highlight== + bracketed labels) in the teacher version, full 4-option MC with answer key and reasoning, sample strong responses, misconception notes. Open: Samuel reviews and owns every choice before any live meeting (a teacher question on a device call or an MC option has to be answerable as if he wrote it). Print-ready file synced. One-pager's stale "thirteen-question" count should be fixed when it is next touched. D-003 (2026-05-19): Scope discipline — removed "Subjects taught" multi-select from Section 4 (AP Lang only, no subject choice). Kept "Class level" (within-AP difficulty calibration, the "calibrated to your class" core). Removed the dangling "only shown if AP Lang selected" conditional on "Current AP unit." Brief v1.1 header, changelog, and Section 4 all reconciled. Flagged but not fixed: D-001's Section 4 change ("Current AP unit" → optional with "skip if cycling") is still unapplied in v1.1; next reconciliation pass should handle it. Conversation logged at 20_Conversations/2026-05-17 - Teacher Meeting Brief.md.

**Build-readiness plan-of-record:** `C:\Users\srlev\.claude\plans\we-have-been-working-silly-cloud.md` — canonical record of the May 13 7-issue session: honest confidence assessment, stress-tested numbers, every decision, full QA scaffolding spec for the eventual build, the synthesis. Start future Caught Up AI build sessions by reading this file.

**Files in project folder:** C:\Users\srlev\OneDrive\Documents\Claude\Projects\Caught Up AI\
- Product Brief v0.1.md, v0.2.md, v1.0.md (LOCKED canonical), v1.1.md (Section 8 discovery-script revision; rest unchanged)
- One-Pager v0.1.md, v0.2.md, v0.3.md (v0.4 not yet saved to folder — only pasted in chat)
- Teacher Meeting Brief v0.1.md and v0.1 - Print Ready.md (historical; v0.1 drafted 2026-05-17)
- Teacher Meeting Brief v0.2.md and v0.2 - Print Ready.md (current; 2026-05-19 snapshot of all changes: D-003 scope cut applied, question audit cuts, real sample brief "The Quiet Classroom" added)
- Samuel's Voice - Style Guide.md
- Decisions Log.md (has D-001, D-002)
- Project Synopsis - May 2026.md

**Why:** Samuel wants The Garage evidence stack by September 2026. The Caught Up AI vehicle satisfies three criteria: concrete measurable pain, workflow-based moat, solo-buildable MVP phase.
