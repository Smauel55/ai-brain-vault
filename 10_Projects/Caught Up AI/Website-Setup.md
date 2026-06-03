---
created: 2026-06-02
updated: 2026-06-02
tags: [project, caught-up-ai, website, active]
project: "[[Caught Up AI]]"
---

# Caught Up AI — Website Setup

Status doc for the marketing site. Read this first to resume the website work.

## Goal

A clean, modern marketing/landing site to show off Caught Up AI and let prospects book meetings, live on a custom domain before the cold-email outreach to AP Lang teachers goes out.

## Where things stand (2026-06-02)

- **Builder:** Site is built on **Base44** (Samuel found a design he liked there). It is a static "just pages" site (no login, no database). It is already live at the Base44 URL: `teach-caught-up.base44.app`.
- **Domain:** `caughtup-ai.com`, registered **through Cloudflare Registrar** (Cloudflare is both registrar and DNS).
- **Hosting decision:** Stay on **Base44** hosting for the convenience of editing by chat. Keeping a custom domain on Base44 requires the **Builder plan (~$50/mo) ongoing, forever** (downgrade or cancel disconnects the domain and reverts to the base44.app subdomain). Considered exporting the static site and hosting free on Google Firebase (one-time ~$50 to export, then ~$0/mo) but chose Base44 to keep the visual editor. Revisit if the $50/mo becomes a burden; Firebase remains the cheap fallback and Samuel would lose easy editing (small edits could still be done via Claude editing the exported code).
- **DNS records (in Cloudflare, both set correctly):**
  - `@` (root) CNAME to `base44.onrender.com`, **DNS only (grey cloud)**
  - `www` CNAME to `base44.onrender.com`, **DNS only (grey cloud)**
  - Note: Base44's connect screen asks for ANAME/ALIAS at `@` + CNAME at `www` pointing to `base44.onrender.com`. Cloudflare has no ANAME, so use a CNAME at `@` (Cloudflare flattens it). Proxy MUST be off (grey cloud) or Base44/Render SSL verification fails.

## BLOCKER (current)

The domain does not resolve. Confirmed from DNS-over-HTTPS that `caughtup-ai.com` returns **NXDOMAIN with no nameserver delegation**. Cloudflare zone status shows **"invalid nameservers."**

Diagnosis: a **stuck / half-finished Cloudflare registration.** The domain appears under **Domain Registration > Manage Domains**, but there is **no subscription** and **no invoice**. The registration started but never fully provisioned (likely payment did not complete). Because Cloudflare is the registrar, Samuel cannot set nameservers himself, and re-registering will not work since the domain already shows as his.

This is not self-fixable. It needs **Cloudflare Support.**

## Action in progress

- Open a Cloudflare Support case under **Domain Registration Failed / Setup Issue** (and optionally post on community.cloudflare.com to speed it up; staff work that forum).
- Ticket text to use:
  > I registered caughtup-ai.com through Cloudflare Registrar. It appears under Domain Registration > Manage Domains, but there is no matching subscription, no invoice, and the zone is stuck on "invalid nameservers." The domain does not resolve at all (public DNS returns NXDOMAIN with no nameserver delegation). The registration appears to have started but never fully provisioned. Please complete the registration and fix the nameserver delegation, or confirm whether payment failed so I can redo it.
- Expected response: ~1 to 3 business days (free-tier account, no SLA).

## Key clarification: "on Google"

Samuel's original "host it on Google" goal really meant **being findable in Google Search**, not hosting on Google infrastructure. Those are unrelated. (Also: Google Domains no longer exists; it was sold to Squarespace in 2023.) The site can rank on Google regardless of being hosted on Base44.

## Next steps (in order, once the domain is unstuck)

1. **Domain:** When Cloudflare fixes the registration and `caughtup-ai.com` resolves, go to Base44 and click **Verify Domain**. SSL turns on automatically.
2. **Google Search Console:** Add a **Domain property** for `caughtup-ai.com`, verify with a **DNS TXT record in Cloudflare** (`@`, the `google-site-verification=...` value). Use a **personal Google account, not the Northwestern one.** Then submit the sitemap and request indexing of the homepage.
3. **Booking:** Samuel believes the Google Calendar booking already works. Confirm it end to end on the live site.
4. **SEO basics:** In Base44, set the page title (e.g. "Caught Up AI: Daily AP Lang lesson openers") and a one-sentence meta description.
5. **Outreach:** Draft cold emails. If the domain is still delayed, the `teach-caught-up.base44.app` URL works as a fallback link.

## Notes

- Earlier in the 2026-06-02 chat, Claude produced a full, detailed "world-class website" design prompt for Lovable/Bolt (dawn-gradient theme, full copy, motion spec). Samuel went with the Base44 site instead, so that prompt is reference only. It lives in that chat transcript if needed.
- Account check flagged: Samuel is in the Cloudflare account tied to his Northwestern email. Confirm this is the same account holding the DNS zone and Base44 connection, and that there is no second Cloudflare account where the domain lives.
