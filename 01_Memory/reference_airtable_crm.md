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

As of 2026-06-13 the Clients table holds 18 AP Lang teacher leads/contacts, all Chicagoland (the 4 IATE network hubs were synced in from the vault on 2026-06-13). Existing pre-2026-06-13 rows have Status/Source blank; the 4 hubs are Status=Lead, Source=Referral. New prospects import as Status=Lead. CSV import maps by header name; single-select values must match a choice name exactly.

RESERVE (not in CRM by design): `AP-Lang-Teachers-Master-List-2026-05` in the vault holds ~46 guessed/English-only rows deliberately kept OUT of Airtable (low confidence, would dilute the pipeline and risk bounces). Promote individually only if/when an email gets verified. See [[project_caught_up_ai]], [[reference_vault_infrastructure]].
