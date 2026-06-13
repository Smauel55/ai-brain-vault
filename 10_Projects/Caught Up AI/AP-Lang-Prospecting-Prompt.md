---
created: 2026-06-13
updated: 2026-06-13
tags: [project, caught-up-ai, outreach, prompt]
---

# AP Lang Teacher Prospecting Prompt (for Cowork)

Reusable prompt for a prospecting pass: find new AP English Language teachers not already in the Airtable CRM, and output a CSV that imports straight into the Clients table.

## How to use

1. Edit the SCOPE line (default = Chicago metro / Illinois; widen for other metros).
2. Refresh the exclusion list if the Airtable Clients table has grown since 2026-06-13 (pull current Name + Email from base `appPzYnVFAN84aIM9`, table `tblhASA0l9a5XSl5B`). See [[reference_airtable_crm]].
3. Paste into Cowork. It returns `new-ap-lang-teachers.csv`.
4. Import into the Clients table (headers already match), or hand the CSV to Claude Code to re-dedup against the live table and push via the Airtable MCP.

## Caveat — vault vs Airtable sync gap (2026-06-13)

The exclusion list below = the 14 rows currently in Airtable. The vault knows more people who are NOT in Airtable: 4 IATE network hubs (Kim Kotty, Andrew Rodbro, Jennifer Gouin, Michelle Ryan) in [[Outreach-Tracker-2026-05]], plus ~46 guessed / English-only rows in [[AP-Lang-Teachers-Master-List-2026-05]]. To avoid re-surfacing known names, either sync those into Airtable first or add them to the exclusion list before running.

## The prompt

```text
You are helping me build a prospecting list of US high-school AP English Language
teachers for a cold-email outreach pipeline. Your output feeds a small Airtable CRM,
so format matters (see OUTPUT).

CONTEXT: The product is a daily lesson "Opener" for AP English Language & Composition
teachers. I need real AP Lang teachers with reachable school email addresses.

SCOPE (edit this line): Chicago metro and Illinois suburban high schools, public and
private. If that pool runs thin, expand to other large US metros. [Replace with specific
states/metros to target elsewhere.]

TASK:
1. Find teachers who CURRENTLY teach AP English Language & Composition (AP Lang).
   Confirm AP Lang specifically, not just "English." A course catalog, department page,
   or bio that names AP Lang and the teacher is good evidence.
2. For each, find a real, currently-valid school email (district .org / school .edu).
   DO NOT invent, guess, or pattern-fill emails. If you can identify the teacher but
   cannot verify an email, put them in a separate "Leads missing email" list, not the CSV.
3. Exclude anyone already in my database (list at the bottom). Dedup by email first
   (case-insensitive); also skip the same person at the same school by name. Lane Tech
   is already heavily covered, so deprioritize it.

SOURCING (use several and cross-check):
- School faculty/staff directories and English-department pages
- Course catalogs or program-of-study PDFs that name AP Lang and its teacher
- District staff directories
- LinkedIn profiles stating "AP English Language"
- "Meet the teacher" bios, school newsletters, news mentions
Prefer evidence you can cite with a URL.

QUALITY BAR:
- Target 25 to 40 verified teachers. Quality over volume. A shorter list of correctly
  attributed real emails beats a long speculative one.
- Every CSV row must have: confirmed AP Lang teaching + a real email + a source URL.

OUTPUT:
Produce a downloadable CSV file named new-ap-lang-teachers.csv with EXACTLY these
headers, in this order:

Name,Company,Email,Phone,Status,Source,Notes

- Name    = teacher full name
- Company = school name
- Email   = verified school email
- Phone   = leave blank unless a real direct line is publicly listed
- Status  = Lead   (literally "Lead" on every row)
- Source  = LinkedIn  if found via LinkedIn, otherwise  Cold outbound
- Notes   = what confirms they teach AP Lang + the source URL + year if known

Status and Source values must match exactly as written (they map to Airtable dropdowns).
Do not add extra columns. After the CSV, add a short "Leads missing email" section
(name, school, why promising, source URL) for strong candidates without a verified email.

ALREADY IN DATABASE — DO NOT INCLUDE (dedup by email):
- kelaroche1@cps.edu  (Lane Tech College Prep)
- dastrom@cps.edu  (Lane Tech College Prep)
- asfine@cps.edu  (Lane Tech College Prep)
- srweathers@cps.edu  (Lane Tech College Prep)
- ewserilla@cps.edu  (Lane Tech College Prep)
- jacwiak@cps.edu  (Lane Tech College Prep)
- mrossi@ipsd.org  (Michael Rossi, Neuqua Valley HS)
- aschultes@glenbrook225.org  (Anna Schultes, Glenbrook North HS)
- mccraem@dist113.org  (Michael McCrae, Highland Park HS)
- ferrarim@dist113.org  (Matthew Ferrari, Highland Park HS)
- wwolfe@dist113.org  (Warren Wolfe, Highland Park HS)
- gchandle@hinsdale86.org  (Gina Chandler, Hinsdale Central HS)
- jmehta@d125.org  (Jay Mehta, Adlai E. Stevenson HS)
- weilerk@nths.net  (Kurt Weiler, New Trier HS)
```
