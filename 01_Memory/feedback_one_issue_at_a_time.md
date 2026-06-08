---
name: feedback_one_issue_at_a_time
description: "On QA/fix work, go one issue at a time (including issues only Claude caught), and make permanent fixes at the source not the symptom"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d19fccfd-9e64-41f2-beba-9b7d01dd9096
---

When working through a list of defects (e.g. an Opener batch QA pass), go **one issue at a time** rather than batching all fixes together. This includes the issues only Claude caught, not just the ones Samuel flagged.

A "permanent fix" means fixing it **at the source**, not patching the symptom. Example (2026-06-08): a render-time `normalize_closers()` guard was only half the fix; the real fix was a deterministic lint gate in the generation workflow (`wf_generate.js`) so a malformed draft is caught and repaired before acceptance.

**Why:** one-at-a-time keeps each fix verifiable and prevents scope creep / re-introducing bugs; source-level fixes stop recurrence instead of masking it. (Samuel, 2026-06-08.)

**How to apply:** kicks in on any multi-defect cleanup. Sequence the issues, confirm each before moving on, and when asked for a "permanent" or "real" fix, default to the generation/source layer. Related: [[feedback_no_code_path]] (verify by behavior, not code inspection).
