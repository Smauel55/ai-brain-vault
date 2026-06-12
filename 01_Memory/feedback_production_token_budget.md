---
name: feedback-production-token-budget
description: Production/critical-path pipelines must be lean and hard-capped; adversarial multi-agent fan-out is an audit tool only
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f2d9f193-d518-49db-a575-b95c63e4b84c
---

Anything attached to the Caught Up AI production path (the nightly Opener that ships to teachers) must be LEAN and have a HARD token/agent budget so it can never drain Samuel's usage limit. A run hitting the limit the night before send = no product in the morning = a serious failure.

Do NOT run expensive multi-agent / adversarial fan-out (per-fact skeptic swarms, multi-checker QA panels, batch x depth multipliers) on the production path. Those are an AUDIT/research tool, run manually and occasionally, never on the critical path.

**What blew up (2026-06-11):** an "ultracode" 5-opener batch spawned ~100 agents (per opener: 1 verify + ~14 fact-check skeptics each web-searching + 1 compose reading ~11 spec files + 4 QA + 1 fix). It burned Samuel's entire 5-hour limit before finishing the verify phase. The lean 3-phase single opener was 3 agents / ~193k tokens / ~8.5 min and was accurate.

**Token sinks, ranked:** (1) web-search fan-out (verify + 2 skeptics/fact all re-searching the same facts), (2) re-reading the 11 static binding spec docs in every compose/QA agent across 5 openers, (3) ~100 agents' boot overhead, (4) full piece JSON passed into 4 QA + 1 fix per opener.

**Cuts:** single disciplined verify pass (source URL per fact, drop unsourced) instead of skeptic fan-out; distill the 11 specs into ONE compact generator brief read once, not full design docs at runtime; one QA pass max and only off the production path; 1 opener/day (broadcast), not batches; always set a workflow budget cap that aborts cleanly.

**Why:** broadcast means nightly cost is one lean opener regardless of subscriber count, so the scalability risk was never user-scale, it was running an audit-grade pipeline on the production path with no ceiling.

**How to apply:** before launching any sizable workflow tied to the product, price it (agent count x per-agent cost) and tell Samuel the rough cost FIRST; default to the lean pipeline; cap production runs. Reserve adversarial verification for explicit, manual audits. Relates to [[project_caught_up_ai]] and the Generation-Pipeline (lean = production, ultra/batch = audit).
