---
name: feedback_openers_no_citations
description: Caught Up AI Openers must contain NO in-text citations of any kind (scholarly apparatus is an off-brand AI/academic tell)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d19fccfd-9e64-41f2-beba-9b7d01dd9096
---

Caught Up AI Openers must contain NO in-text citations of any kind. Not just `(Author, year)` parentheticals but the whole scholarly apparatus, including inline forms like "Carstensen's work," "Portfolio studies do find," "researchers at NBER." Facts are stated plainly; naming a body inline ("the GAO reported," "the FAA said") is fine, an academic-paper citation is not.

**Why:** Samuel has never seen an AP Lang exam article with in-text citations; they are too rare to be made normal, and they read as an academic/AI tell, off-brand for the product. (Stated emphatically 2026-06-08 after Issue 2 of the 28-opener batch.)

**How to apply:** Bans any citation in generated Opener prose. Hit only the evergreen/research pieces (#12, #24) because their source stage pulled scholarly refs. Encoded as an explicit ban in the anti-tell verifier brief in `wf_generate.js`; also clarify the distinction in [[Anti-Tell-List]] and [[Accuracy-Guardrail]] (attribute facts to a named body inline, never an academic parenthetical or reference list). Related: [[feedback_ai_writing_formulaic]], [[feedback_device_vocabulary]].
