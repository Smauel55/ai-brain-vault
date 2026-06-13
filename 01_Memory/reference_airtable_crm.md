---
name: reference-airtable-crm
description: "Airtable CRM coordinates for Caught Up AI outreach (base/table/field IDs, dropdown choices, sync gap)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 5f8fd8b5-f1c5-421c-baa0-f7799ff4e656
---

Caught Up AI outreach CRM lives in Airtable (one base in the account).

- Base: "Clients & Outreach" — `appPzYnVFAN84aIM9`
- Table: "Clients" — `tblhASA0l9a5XSl5B`. Fields: Name (text), Company (= school, text), Email, Phone, Status (singleSelect), Source (singleSelect), Notes (multiline), Outreaches (link), Created (createdTime).
  - Status choices: Lead, Active, Cold, Closed-Won, Closed-Lost
  - Source choices: Northwestern, LinkedIn, Referral, Cold outbound, Other
- Table: "Outreaches" — `tblkzWLfJC29LKNNF`. Fields: Touch, Client (link), Type, Date, Outcome, Next step, Next step date. Logs each outreach touch per client.

As of 2026-06-13 the Clients table held 14 AP Lang teacher leads, all Chicagoland. New prospects import as Status=Lead. CSV import maps by header name; single-select values must match a choice name exactly.

SYNC GAP (2026-06-13): the vault knows more known contacts than Airtable. The vault `Outreach-Tracker-2026-05` adds 4 IATE network hubs (Kim Kotty, Andrew Rodbro, Jennifer Gouin, Michelle Ryan), and `AP-Lang-Teachers-Master-List-2026-05` holds ~46 more guessed/English-only rows. Reconcile before treating Airtable as the full known set. See [[project_caught_up_ai]], [[reference_vault_infrastructure]].
