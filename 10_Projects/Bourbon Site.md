---
created: 2026-05-08
updated: 2026-05-10
tags: [project, test, paused]
---

# Bourbon Site (Whisky Site Test)

A throwaway test site Samuel commissioned on May 8 to probe Claude Code's frontend capabilities — specifically expensive-feeling, high-end branding for a fictitious premium whisky/bourbon company. Not a real product, no business goal beyond stress-testing what Claude can build solo.

**On disk:** `C:\Users\srlev\OneDrive\Documents\Claude\Projects\Whisky Site Test\index.html` (final version)
**Iterations archive:** `10_Projects/Bourbon Site/iterations/`

## Iterations

| # | File | What changed | Outcome |
|---|---|---|---|
| v1 | `iterations/v1-line33.html` | Initial build. Dark, expensive-feeling, crisp imagery, professional layout. | Samuel: text boxes blended into background, looked monochrome, only thin line separating elements. |
| v2 | `iterations/v2-line60.html` | More definition between sections, brighter, separated text from background, opening animation added. | Samuel: animation looked "clunky and cheap, like something coded from scratch in middle school." |
| v3 | `iterations/v3-line119.html` | Reworked animation using newly installed animation skills. More refined motion, better bottle shading. | Samuel: bottle shading better, but liquid still looked like "scratch code" — wanted real-liquid viscosity. |
| v4 | `iterations/v4-final.html` (= current `index.html`) | Same as v3 + 5 small edits, plus integration of an externally generated cinematic pour video. | Final state. Final = v3 with the imported `hero-pour.mp4` swapped in as the hero shot. |

## The video

When Samuel pushed for hyper-realistic liquid pouring, I told him I couldn't generate that quality of fluid simulation in plain CSS/JS. He generated a video externally (Adobe Firefly: "Cinematic close-up of golden amber whisky pouring slowly from a tilted dark glass bottle...") and dropped it into the project as `hero-pour.mp4` (9.5 MB). v4 wires that video into the hero section.

## Decisions

- **Realistic liquid simulation is out of scope for code-only generation.** When users want photoreal motion, accept the limit and integrate AI-generated video instead of trying to fake it in CSS.
- **Animation skills (Emil Kowalski / fluid-animation) noticeably improved motion quality** between v2 and v3.

## Status

Paused. This was a capability test, not a real venture. Useful as a reference point for what Claude can build for a frontend ask without a designer.
