---
name: reference_opener_renderer
description: Opener PDF renderer + reusable generation prompts — render_opener_v2.py is the source of truth
metadata: 
  node_type: memory
  type: reference
  originSessionId: cff28425-c81b-4fde-97cb-38350e1bf10c
---

How Caught Up AI Openers get rendered and generated on demand.

- **Renderer (source of truth):** `10_Projects/Caught Up AI/Sample-Briefs/render_opener_v2.py`. Builds teacher copy (single light-yellow highlights #FFF3A0 + dark-blue labels, legend, answer key, sample responses, misconceptions, alignment) and clean student copy. Supersedes v1 `render_briefs.py` (six-color scheme) and the Google-Docs-era `render_opener_docx.py` / `render_opener_html.py` (those lack the headnote field).
- **Renderer features:** optional `headnote` field (italic, both copies); `audience` flag (`ap_lang` | `general_english`, swaps labels/alignment only); `randomize_answers()` shuffles MCQ options at render time (keys must never be predictable); backward-compatible with older piece dicts.
- **Reusable prompts** (both in `10_Projects/Caught Up AI/`): `caughtupai-sampleprompt-V1.md` = batch sample runs (set N, Variety Matrix, batch audit); `caughtupai-quickprompt-V1.md` = one on-demand Opener (optional topic/register, recency check vs latest editions).
- **Production path:** the generation pipeline workflow (`.claude/workflows/caughtup-opener.mjs`) imports `build()` / `randomize_answers()` from render_opener_v2 UNMODIFIED; recency persists in `editions-log.tsv`. See [[project_caught_up_ai]].
- **Logo:** `Sample-Briefs/caughtup-logo.png` (real logo, used in the masthead).
- Teacher-copy format matches Samuel's "Teacher Meeting Brief v0.2" structure (numbered paragraphs; marked article + quick reference + answer key + sample responses + misconceptions + alignment).

Related: [[feedback_device_vocabulary]] (what may be highlighted), [[reference_product_naming]] (it's an "Opener", never a "brief").
