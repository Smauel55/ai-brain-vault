---
created: 2026-06-13
updated: 2026-06-13
tags: [conversation, caught-up-ai, outreach]
project: "[[Caught Up AI]]"
---

# 2026-06-13 — AP Lang teacher prospecting pass

## Context

Samuel wants another pass to find more AP Lang teachers (not already in the database) and get their data into the Airtable outreach pipeline. Asked whether to run it in Code or Cowork.

## Key points

- **Routing:** Cowork for the gathering pass (browsing-heavy, autonomous), Code for the dedupe + import. [[feedback_surface_routing]]
- **Confirmed the live CRM:** Airtable base "Clients & Outreach" (`appPzYnVFAN84aIM9`), table "Clients" (`tblhASA0l9a5XSl5B`). Fields: Name, Company (school), Email, Phone, Status, Source, Notes. Status choices: Lead / Active / Cold / Closed-Won / Closed-Lost. Source choices: Northwestern / LinkedIn / Referral / Cold outbound / Other. 14 records, all Chicagoland. Captured in [[reference_airtable_crm]].
- **Built a reusable Cowork prospecting prompt** with the 14 current contacts embedded as a dedup exclusion list; output is a CSV whose headers map 1:1 to the Clients table (Status pre-set to "Lead"). Saved to [[AP-Lang-Prospecting-Prompt]].
- **SYNC GAP found:** the vault [[Outreach-Tracker-2026-05]] holds 18 contactable rows = the 14 in Airtable PLUS 4 IATE network hubs (Kim Kotty, Andrew Rodbro, Jennifer Gouin, Michelle Ryan), and [[AP-Lang-Teachers-Master-List-2026-05]] holds ~46 more guessed/English-only rows. None of those extras are in Airtable. A clean pass should exclude them too, or sync them into Airtable first.

## Decisions

- "Our database" = the Airtable Clients table (the 14). The dedup list in the prompt covers exactly those.

## Action items

- [ ] Samuel — decide: sync the 4 IATE hubs (and promote master-list rows) into Airtable before the pass, or just add them to the prompt's exclusion list.
- [ ] Run the prompt in Cowork, then bring the CSV back to Code to re-dedup against the live table and import via the Airtable MCP.

## Open threads

- Geographic scope of the new pass (prompt default = Chicago metro / Illinois, expandable to other metros).
