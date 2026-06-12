---
name: feedback_name_canary
description: "Address Samuel as 'sir' in every response as a context-degradation canary; if Claude drops it, that's his cue to start a fresh session"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b721cdf0-ff73-47d8-a1cc-4768012a1cfa
---

Samuel uses a "canary in the cave" strategy to detect when a session is degrading: Claude should address him as "sir" in every response. When Claude stops doing it, that is his signal that context has decayed and he should start a fresh session. (Changed 2026-06-12 from using his name "Samuel" — hearing his name every response got annoying.)

**Why:** He wants a visible, low-effort tripwire for session degradation rather than guessing when context is stale.

**How to apply:** Address Samuel as "sir" naturally in responses across the session. Honest caveat already told to him: a name is highly salient and so trips LATE; subtler degradation (contradicting earlier decisions, re-asking for context already given, dropping nuance) shows up first. So treat the name as a backstop, not the only signal, and never game it deliberately to mask decay. Relates to [[feedback_communication_style]].
