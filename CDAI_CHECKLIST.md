# Allocera / CDAI: Game Plan

Nick's running list. Claude keeps it current and checks items off as they ship.
Rule: nothing gets built until Nick has seen it and said yes. Every public claim must be provable.

_Last updated: Sept 25, 2026 (everything from the session consolidated)_

---

## 1. Do today (Nick)

- [ ] **Paste the homepage.** Copy `website/homepage.html` (or `homepage-copy-paste.txt`) into the single Elementor HTML widget, replacing everything in it.
- [ ] **Set the homepage title and description in Rank Math.** The block no longer carries its own, which fixes the doubled title.

---

## 2. Decisions for Nick (open; Claude acts only after a yes)

- [ ] **D1. PAUSE 85.2%:** 71 of its 144 "right" calls improved by less than 2 points, all in the stress-test business. *Recommendation:* stop quoting it publicly until a minimum-improvement bar is added and it's re-scored.
- [ ] **D2. Engine default costs:** CSV uploads add a 2.9–3% platform fee, and six lead paths add $0.25 per lead of compliance cost. Neither affects the validation or Apex. *Recommendation:* default both to $0 unless the client supplies real values; fix before the first client who uploads a CSV.
- [ ] **D3. Calculator compliance hint:** it says "default $0.25", but the calculator actually uses $0. *Recommendation:* change it to "only if you pay for per-lead consent certificates".
- [ ] **D4. The 2,738 simulated-business lead records** that still hold fake names and emails. *Recommendation:* strip them (it's test data).
- [ ] **D5. Sync on connect:** run the first data pull right after a client connects, instead of waiting for 2 AM UTC. *Recommendation:* yes; new clients see numbers the same day.
- [ ] **D6. AI links section** (ChatGPT/Claude/Perplexity/Grok) on the homepage. *Recommendation:* leave it off; no proven SEO effect, and it sends visitors away.
- [ ] **D7. Intake form's job** now that self-serve is live. *Recommendation:* free-audit request now; "Partner with us / talk to Nick" once the free audit is in Stripe.
- [ ] **D8. Apex status:** 0 ad-spend rows, no active campaigns, last directive Aug 13. *Ask Nick:* paused, churned, or investigate a sync problem?
- [x] **D9 (CallRail part). LIVE Sept 25 (PR #28):** a saved CallRail key is now pulled every night. Still off: Ringba, Boberdoo, Bing, Stripe. Each needs its own fix first: Bing puts all spend under one campaign, Boberdoo's lead cost never reaches true cost, Stripe assumes a 7% fee, and Ringba drops partner payouts.
- [x] **D10. LIVE Sept 25 (PR #28):** each CallRail call is matched to its ad campaign by its campaign tag. Unmatched calls stay unattributed. Tested with 30 checks.
- [x] **D2 for calls. LIVE Sept 25 (PR #30):** CallRail calls now add $0 compliance cost. The other $0.25 defaults (Meta lead forms, Ringba, Boberdoo, CSV, webhook) are still open under D2.

---

## 3. Product / engine (after decisions)

- [ ] **Free Distortion Audit in Stripe**: create the product, wire checkout (`billing.py`), and add it to the pricing page.
- [ ] **Live test of VINDEX** (the chat agent): run ~15 real prospect and investor questions against the live bot; Nick reviews the answers.
- [ ] **Chat agent upgrades**: streaming replies, clear rules for handing off to Nick, and a weekly review of real transcripts.
- [ ] **Manuals rewrite**: remove "7 cost layers", "no self-serve", the old acronym, and the stale integration counts from all manuals. A correction notice already sits at the top of the current one.
- [ ] **VINDEX trademark check** (Nick): a registered VINDEX mark exists (Vindex LLC, esports, serial 88671256).

---

## 4. Homepage video (90 seconds to 3 minutes)

- [ ] Claude writes the script. Nick approves it.
- [ ] Nick sends a screen recording of the portal, plus the logo and screenshots.
- [ ] Voiceover: Nick's own voice (best for trust and YouTube search), or free text-to-speech in Clipchamp.
- [ ] Claude renders a motion-graphics cut: free, 1080p, no watermark.
- [ ] Publish on YouTube with "Allocera" and "CDAI" in the title and description, then embed it on the homepage.

---

## 5. Rest of the website (51 URLs), one page at a time

**Blocker (Nick, 2 minutes):** WordPress → Tools → Export → All content → send the XML file. It holds every page's text and its Rank Math fields.

**Per page:** audit it against the engine, the validation report, GA, and Search Console. Nick says yes or no to each change, and Claude delivers the finished HTML block plus Rank Math fields.

**Order:**
1. **Fix-first pages**
   - `/55-directives-study/`: still claims the debunked 80%. Rewrite it around the Sept 2026 validation, or redirect it.
   - Duplicate pages: `/true-cac/` + `/true-cac-2/`, and `/30-day-retest-methodology/` + `-2/`. Merge each pair and 301-redirect the extra.
   - 404s: the "Page Not Found" page is the 2nd most-viewed page. Turn on Rank Math's 404 monitor and redirect each dead URL.
   - Doubled titles: strip the pasted `<head>` from every page, as already done on the homepage.
   - `/home-sample/` template paths: move those pages to clean URLs and 301 the old ones. This includes the validation report, terms, privacy, and the Northbeam/Rockerbox pages.
   - `/proof/`: it's the Apex story. Keep it, rewrite it around the validation, or drop it from the nav.
2. **Pages with real traffic**: pricing (add the free audit; match the site), about, how-it-works, blog, dashboard.
3. **Closest to Google page 1**: `/scale-hold-cut-pause-framework/` (position 8.2), `/calculate-contribution-margin/` (109 impressions, position 20), `/triple-whale-vs-rockerbox-vs-allocera/`, and the Northbeam/Rockerbox alternative pages.
4. **Long-tail industry pages** (HVAC, personal injury, senior living, and others): only after 1–3 show results.

---

## 6. Growth ideas (proposed; Nick says yes or no to each)

**Homepage conversion**
- [ ] Show the price level near the main button. Retainers from $1,500/mo appear today only in an Explore card and the FAQ.
- [ ] Founder block: Nick, 3 years building, photo, based in NC, phone. Needs a photo and Nick's OK on the wording.
- [ ] Sample report visitors can open without talking to anyone (a clearly labeled fictional business).
- [ ] "15 minutes with the founder" booking button (a free Calendly link).
- [ ] Date the proof: "Validated Sept 2026".
- [ ] Get the two Apex reviews onto G2.

**AI search / SEO**
- [ ] YouTube channel. The homepage video is the first upload.
- [ ] Founder-voice answers on Reddit (r/PPC, r/marketing, r/smallbusiness).
- [ ] Organization + SoftwareApplication schema on the homepage.
- [ ] Check robots.txt allows AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended).
- [ ] Keep content fresh, with visible dates on posts.

_Research caveat: Nielsen Norman Group, Stanford, Gartner, and Ahrefs figures came from search results. Their original pages are blocked in this environment, so re-verify them from the source before quoting any of them publicly._

---

## 7. Security (Nick)

- [ ] Rotate the Supabase database password. It's hardcoded in `run_full_directive.py` and `time_engine.py`, and the former cofounder may know it.
- [ ] Rotate other shared keys he could have seen (Resend, Stripe, Render).
- [ ] Check the team member lists in Render and Supabase.
- [ ] Delete the 19 old validation cron jobs on Render. Each has a fixed date in its schedule, so they re-run every year.

---

## 7b. Partnerships

- [ ] **CallRail:** book the call with Karina and Eric (Eric is CallRail's partner marketing manager), then send the final email (full text in the engine repo's `docs/HANDOFF-website-trust-sept25.md`).
- [ ] Before the call: have the logo and a one-paragraph listing description ready. The CallRail sync is live.

---

## 8. Access that would help Claude (Nick)

- [ ] **WordPress export**: needed for section 5.
- [ ] **Network allowlist** in the environment settings (cloud environment menu → Edit → Network access). Add `nngroup.com`, `gartner.com`, `support.google.com`, `facebook.com`, `wikipedia.org`, and your own site, so sources can be verified from the originals.
- [ ] **Gmail for alloceraintelligence@gmail.com**, if you want Claude to read the Control Tower emails. The connected Gmail is fullsendorganicks@gmail.com.
- [ ] **PageSpeed score**: run pagespeed.web.dev (mobile) on the live homepage and send the number.

---

## Done (Sept 25, 2026)

- [x] Former cofounder fully offboarded: engine email is staff-only; repo, docs, and memory cleaned (PR #16).
- [x] Chat agent named **VINDEX** (a label above every reply; page buttons stay "Ask CDAI"). Full capability knowledge, honest identity rules, wrong facts fixed (PRs #15, #17, #18, #20, #21).
- [x] **Dashboard trust fix LIVE** (portal PR #2): no fake directives before a client's first run.
- [x] **SCALE scoring fix LIVE** (PR #24): the 98.0% rule is the production rule. Memory corrected (PR #25).
- [x] **Privacy fix LIVE** (PR #22): Meta lead forms no longer store names, emails, or phones.
- [x] **Math and accuracy re-verified read-only**: all 1,352 validation grades reproduced exactly. The $0.25 and CSV fee change nothing except PAUSE's thin results.
- [x] **Homepage final**:
  - hero kept
  - "What CDAI does" section (9 verified cards)
  - trust FAQs
  - sitemap-verified links, dead link removed
  - US-accurate calculator (0% platform fee)
  - real logos
  - no fake numbers
- [x] Handoff doc, worklog, and a correction notice on the manual written. CLAUDE.md memory holds every verified fact and rule.
