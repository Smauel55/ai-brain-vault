---
created: 2026-06-03
updated: 2026-06-03
tags: [conversation, caught-up-ai, website, seo]
project: "[[Caught Up AI]]"
---

# 2026-06-03 — Domain switch, Porkbun, Search Console SEO

## Context

Samuel was stuck following up on the Cloudflare support ticket for `caughtup-ai.com` (the "Cannot locate dashboard account" page kept appearing). Decided to abandon Cloudflare, switch domains, and get the site live + set up for Google. Went from blocked to fully live and SEO-ready in one session. See [[Website-Setup]] for the full status doc.

## Key points

- The Cloudflare "follow up on ticket" page is a known Help Center / dashboard linking glitch. Email reply to the ticket confirmation is the reliable follow-up channel, but Samuel chose to drop it entirely.
- **Switched domains:** old `caughtup-ai.com` (hyphen, stuck on Cloudflare) → new **`caughtupai.com`** (no hyphen, cleaner brand). Registered at **Porkbun** (recommended over registering inside Base44 to keep the domain portable).
- Connected to Base44 via DNS: ALIAS `@` + CNAME `www` → `base44.onrender.com`. Confirmed the site serves live on the new domain.
- **Untangled three Google products:** Workspace (paid, branded email only) vs Google Business Profile (free, but not applicable to an online-only product) vs Search Console (free, the actual tool for being found in search). Samuel needs only Search Console.
- **Google Search Console Domain property verified** for `caughtupai.com` via DNS TXT. Sitemap submitted ("Couldn't fetch" = normal for a new domain). robots.txt confirmed permissive.
- **On-page SEO:** title set to `AP English Language Lesson Openers Daily | Caught Up AI`; kept the existing meta description; OG tags already handled by Base44.

## Decisions

- **Drop Cloudflare / `caughtup-ai.com`.** Let it lapse, don't renew, abandon the support ticket. Cleaner non-hyphen brand is worth more than fighting the stuck registration.
- **Buy domains at a real registrar (Porkbun), not inside the app builder.** Keeps the domain portable; Samuel just felt the pain of a registrar lock-up.
- **Don't buy Google Workspace.** Not needed for SEO or anything current. Only buy it later if/when branded email is wanted.
- **Don't use the Northwestern account for business infrastructure.** The school controls it (Search Console is disabled on it) and it disappears when he leaves. Use a personal/owned account; transfer to a business account later (lossless).
- **Keep the white-background logo everywhere.** No transparent version.

## Action items

- [ ] Samuel — check `site:caughtupai.com` in Google in ~1 week to confirm indexing
- [ ] Samuel — confirm Workspace trial-vs-billing status and which domain it's on, then cancel if unneeded
- [ ] Samuel — let `caughtup-ai.com` lapse; drop the Cloudflare ticket
- [ ] Samuel — regenerate Base44 API key if the dashboard screenshot was shared anywhere
- [ ] Next SEO session — Bing Webmaster Tools, check homepage text depth, then plan 3–5 content pages

## New knowledge to file

- Reusable pattern: technical SEO setup order for a new site (buy domain at real registrar → connect to builder via DNS → verify Domain property in Search Console via DNS TXT → submit sitemap → set title/meta → wait for indexing). Could become a `30_Knowledge/` note if this recurs.

## Open threads

- Is the site one page only? Content depth is the real SEO lever and is still untouched (Samuel paused SEO here).
- Base44 hosting cost (Builder plan ~$50/mo for custom domain) — confirm current billing.
- Google Calendar booking on the live site — not yet confirmed end to end.
