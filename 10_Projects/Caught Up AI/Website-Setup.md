---
created: 2026-06-02
updated: 2026-06-03
tags: [project, caught-up-ai, website, seo, active]
project: "[[Caught Up AI]]"
---

# Caught Up AI — Website Setup

Status doc for the marketing site. Read this first to resume the website / SEO work.

## Goal

A clean marketing/landing site for Caught Up AI, live on a custom domain, findable in Google Search, before cold-email outreach to AP Lang teachers.

**Product (confirmed from live site copy):** a daily, AP-aligned lesson opener for **AP English Language and Composition** teachers, delivered to the inbox every morning at 6am.

## CURRENT STATE (2026-06-03) — site is LIVE and in Google's queue

Big change from 2026-06-02: **abandoned the Cloudflare domain, switched to a new domain on Porkbun, and finished the full technical SEO setup.** The old Cloudflare blocker is no longer relevant.

- **Live domain:** **`caughtupai.com`** (no hyphen). Registered at **Porkbun**. Site resolves and serves correctly (homepage, sitemap, robots all confirmed live).
- **Builder:** still **Base44**. Domain connected via Base44's "Connect existing domain" flow.
- **DNS records at Porkbun:**
  - `ALIAS` `@` (root) → `base44.onrender.com`  (Porkbun supports ALIAS, preferred over A record)
  - `CNAME` `www` → `base44.onrender.com`
  - `TXT` `@` → `google-site-verification=vTYdT2FEkkVhXd409LxO47Y95-RK46Lpvc6h8` (Search Console verification)
- **Google Search Console:** **Domain property for `caughtupai.com` is VERIFIED** (via the DNS TXT record above).
  - Signed in with a **personal Gmail** (NOT the Northwestern account — the school org has Search Console disabled for students; NOT the Workspace account, which is likely being cancelled).
  - Search Console ownership can be transferred to a future business account later with zero loss (verification rides on the DNS record, not the account). SEO history lives on the domain, not the account.
- **Sitemap:** `https://caughtupai.com/sitemap.xml` submitted. Status currently **"Couldn't fetch"** — this is NORMAL for a one-day-old domain, not an error (sitemap is valid and reachable; robots.txt is permissive and references it). Expect it to flip to "Success" within days as Google crawls.
- **On-page SEO done:**
  - **Title** set to: `AP English Language Lesson Openers Daily | Caught Up AI`
  - **Meta description** (kept, it's good): "A daily, AP-aligned lesson opener for AP English Language and Composition teachers, delivered to your inbox every morning at 6am."
  - **Open Graph tags** (title/description/image/url/site_name) already auto-set by Base44 — social sharing looks clean. OG image = logo at 1200x630.
- **Logo:** rising-sun mark, purple-to-coral gradient, **white background** (Samuel chose to keep white bg everywhere, no transparent version). Being placed via Base44 chat editor (header + favicon).

## Where to change SEO in Base44

Dashboard → **Marketing** (left menu, the item tagged "New" — Base44 renamed "Growth" to Marketing) → **SEO & GEO** → **Meta tags** tab → click the **Edit** icon next to the page → update Title/Description → Save. Then Publish.

## Will it appear on Google?

Not instantly. New domain takes **days to a few weeks** to be indexed. First it'll appear for exact-brand / domain searches, NOT competitive terms. Check progress with a Google search for `site:caughtupai.com` — once the page shows, it's indexed. Search Console's Pages/Sitemaps sections will also show crawl activity.

## Open items / next steps (when Samuel returns to SEO)

1. **Wait for indexing.** Check `site:caughtupai.com` in ~1 week. No action needed to trigger it.
2. **Quick technical wins:** add **Bing Webmaster Tools**; confirm the homepage has enough real readable text for Google (a thin/image-only landing page ranks poorly).
3. **Content strategy (the real traffic lever):** add 3–5 pages each targeting a specific AP Lang teacher search (e.g. "AP Lang bell ringers," "free AP English Language warm-ups," "rhetorical analysis activities"). Each page = a new door in.
4. **Backlinks:** teacher communities/directories linking back = the big off-page credibility signal.
5. **Confirm the Google Calendar booking** works end to end on the live site.
6. **Cancel the Workspace account** if not needed — decided Samuel does NOT need Google Workspace (it's only for branded email like you@caughtupai.com, not for SEO or anything done today). Before cancelling, confirm: is it a free trial or already billing? Which domain is it attached to? (A domain used to create a Workspace sometimes must be fully released before reuse elsewhere.)
7. **Let `caughtup-ai.com` (old hyphenated Cloudflare domain) lapse** — do not renew. The Cloudflare support ticket about it can be dropped.

## Notes / loose ends

- **Security:** Samuel's **Base44 API key** was visible in a dashboard screenshot. If that screenshot was shared anywhere, regenerate the key in Base44 settings.
- **Phone limit:** creating a brand-new dedicated Gmail (`caughtupai@gmail.com`) was blocked by Google's "phone connected to too many accounts" limit. Resolved by using an existing personal Gmail instead. The limit resets on its own after a few days if a dedicated account is wanted later.
- **Hosting cost:** the 2026-06-02 note said a custom domain on Base44 needs the Builder plan (~$50/mo). The domain is now live and connected, so either that's been handled or Base44's policy changed — **confirm current plan/billing status** (dashboard showed an "Upgrade" button). Firebase remains the cheap fallback if the monthly cost becomes a burden.
- **"On Google" clarified:** Samuel's goal of being "on Google" means being findable in Google Search (Search Console + SEO), not hosting on Google. Also note: Google Business Profile is NOT applicable — Caught Up AI is fully online with no physical location/service area, so it wouldn't qualify. Search Console is the right tool.
