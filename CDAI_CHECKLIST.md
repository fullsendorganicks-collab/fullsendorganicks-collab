# Allocera / CDAI: Working Checklist

Nick's running list. Claude keeps it current and checks items off as they ship.
Rule: nothing gets built until Nick has seen it and said yes.

_Last updated: Sept 25, 2026 (dashboard + SCALE fixes live)_

## Done

- [x] Former cofounder removed from all engine email, the repo, and memory (merged Sept 25)
- [x] Chat agent and memory updated: no "7 cost layers", correct qualification rule, free audit kept, no "unproven" wording (merged Sept 25)
- [x] Homepage v1: empty-space bug fixed, real logos, duplicate-title fix, 4-field form, FAQ
- [x] Homepage v2 built: Apex appears only in the two reviews; the validation results lead in the hero.
- [x] Homepage v3: claims audit. Every claim traced to a source; three unprovable claims removed (newsletter cadence, "HOLD is its most common call", "live in about a day"). **Paste `website/homepage.html` (this repo) into the Elementor block.**

## Now (in order)

- [x] **SCALE scoring fix LIVE** (cdai-engine PR #24, deployed on Render web + nightly job Sept 25). The 98.0% rule is now the production rule. Tests: offline 5/5 pass, `test_directive_actions` passes, and a DB re-score gives 818/835. Memory corrected (PR #25).
- [ ] **PAUSE 85.2% (Nick decides):** 71 of 144 HITs are under a 2-point improvement, all from the stress-test business. Keep quoting it, or add a minimum-improvement bar?

- [x] Newsletter cadence: none yet. No issue has gone out; the signup is list-building. No frequency claim on the site.
- [x] Self-serve copy verified against the portal code: account ready seconds after payment, one-click connections, first directives on the next nightly run.
- [x] **Handoff + memory updated:** `docs/HANDOFF-website-trust-sept25.md`, correction notice on the current manual, WORKLOG entry (`cdai-engine` branch `docs/handoff-website-trust-sept25`). **Nick merges.**
- [x] **Dashboard trust fix LIVE** (cdai-portal PR #2, merged and deployed to Vercel production Sept 25): no invented directives before the first run, no default HOLD, legend matches the engine.
0. [ ] **Optional: run the first sync right after connecting**, so new users see their numbers the same day instead of waiting for 2 AM UTC. The engine already has `/sync/*` endpoints. Needs Nick's yes.
- [x] **Chat agent named VINDEX** (final). Prompt identity plus a "VINDEX" label above every chat reply; page labels stay "Ask CDAI". Nick merges `cdai-engine` `docs/handoff-website-trust-sept25` and pastes `website/homepage.html`.
0. [ ] **VINDEX trademark check** (Nick): a registered VINDEX mark exists (Vindex LLC, esports, serial 88671256).
- [x] **Chat agent knowledge audit:** full capability loop added. Wrong claim fixed (INVESTIGATE/RENEGOTIATE numbers do exist); onboarding and free audit corrected. **Nick merges `docs/handoff-website-trust-sept25`.**
0. [ ] **After merge: live test of VINDEX.** Claude runs ~15 real prospect/investor questions against the live bot. Nick reviews the answers.
- [x] **Privacy fix merged** (PR #22): Meta lead forms no longer store names, emails, or phones. Open: Nick decides whether to strip PII keys from the 2,738 simulated-org rows.
- [x] **Homepage v5:**
  - hero unchanged (H1 and H2 kept as-is; no extra subheading, to avoid overwhelming)
  - new "What CDAI does" section (9 verified capability cards) below How It Works
  - How It Works steps 4/5 expanded
  - Validated wording fixed, with the nightly math recheck
  - trust strip gets a "Nightly" card
  - FAQs added: missing/wrong data, customer data safety, lookback
  - How It Works shown as a 3+2 layout

  **FINAL:** blog nav links now point to `/blog/` (the sitemap URL, not the `/home-sample/` template path). The dead `/true-cost-per-lead/` link is removed. **Nick pastes `website/homepage.html` (or `homepage-copy-paste.txt`).**
- [x] **Calculator platform fee** is now 0% by default, with the hint "US ads on Meta & Google: 0%" (tested: $10k spend / 100 leads gives $100 reported and $100 true).
0. [ ] **ENGINE: remove assumed costs (Nick decides).** CSV uploads add 2.9–3% platform fees, and six intake paths add $0.25 per lead in compliance cost. Proposal: default both to $0 unless real values are supplied. Real client unaffected; Demo org affected.
0. [ ] **Apex status (Nick):** 0 ad-spend rows, no active campaigns, last directive Aug 13. Paused, churned, or a sync problem?
0. [ ] **Calculator compliance hint (Nick decides):** it says "default $0.25", but the calculator actually uses $0 unless typed. Proposed text: "only if you pay for per-lead consent certificates".
0. [ ] **Access:** connect the alloceraintelligence@gmail.com Gmail (the Control Tower inbox) if Nick wants Claude to read the nightly emails.

1. [ ] **AI links section (ChatGPT / Claude / Perplexity / Grok):** Nick decides whether to restore it. It doesn't affect rankings (see the Ideas section below). It can go back in within minutes.
2. [ ] **What the intake form should do now that self-serve is live:** Nick decides. Recommendation: it's the free audit request today. Once the free audit is in Stripe, it becomes a "Partner with us / talk to Nick" form for agencies and bigger accounts.
3. [ ] **Free Distortion Audit in Stripe:** add the product, wire checkout (`billing.py`), and add it to the pricing page.
4. [ ] **Homepage video, 90 seconds to 3 minutes:**
   - [ ] Agree on the script
   - [ ] Nick sends a screen recording of the portal, plus the logo and screenshots
   - [ ] Voiceover: Nick's own voice, or free text-to-speech in Clipchamp
   - [ ] Claude renders the motion-graphics cut (free, 1080p, no watermark)
   - [ ] Publish to YouTube and embed it on the homepage
5. [ ] **Rest of the site (51 URLs), one page at a time:** needs the WordPress export (Tools → Export → All content). Fix first:
   - [ ] `/55-directives-study/` (still says the debunked 80%)
   - [ ] Duplicate pages: `/true-cac/` + `-2`, `/30-day-retest-methodology/` + `-2`
   - [ ] 404 page (2nd most viewed page): turn on Rank Math's 404 monitor and redirect the dead links
   - [ ] Doubled titles: strip the pasted header from every page
   - [ ] `/proof/` is the Apex story. Decide whether to keep it, rewrite it around the validation, or remove it from the nav.

## Security (Nick)

- [ ] Rotate the Supabase database password. It's hardcoded in `run_full_directive.py` and `time_engine.py`, and the former cofounder may know it.
- [ ] Rotate other shared keys he could have seen (Resend, Stripe, Render)
- [ ] Check the team member lists in Render and Supabase
- [ ] Delete the 19 old validation cron jobs on Render (`cdai-validation-*`, `cdai-distressed-partner-*`, `cdai-full-revalidation-run1`, `cdai-onboard-remaining6`). Their schedules name a specific day (e.g. `42 20 23 9 *`), so they'll run again every Sept 23 on the paid starter plan.

## Ideas backlog: proposed, not approved

**Homepage conversion proposals (Sept 25 research: NN/g, Stanford, Gartner).** Nick says yes or no to each:
- [ ] **Show the price level near the main CTA.** NN/g: price is buyers' #1 info need, and hiding it reads as evasive. Today it's only in an Explore card and the FAQ.
- [ ] **Founder / real-company block.** Stanford credibility guidelines: show the real organization. Nick, 3 years building, photo, NC, phone. Needs Nick's photo and his OK on the wording.
- [ ] **Sample report buyers can open without talking to anyone.** Stanford: make accuracy easy to verify. Gartner: 67% of B2B buyers prefer rep-free buying. A clearly labeled sample directive sheet or audit on a fictional business. Claude can build it.
- [ ] **"15 minutes with the founder" booking option.** Gartner 2026: 69% of buyers validate AI-generated insights with a person. Needs Nick's free Calendly link.
- [ ] **Date the proof** ("Validated Sept 2026"). NN/g: current content signals trust. Tiny and true.
- [ ] **Get the two Apex reviews onto G2.** NN/g: connection to the rest of the web. Needs Apex.
- [ ] **Site-wide consistency pass.** Gartner: 69% of buyers find inconsistencies between the website and sellers. Needs the WordPress export.

Evidence-backed ideas for a bootstrapped founder. Nick says yes or no to each one before any work starts.

- [ ] **YouTube channel.** Ahrefs' 75,000-brand study found YouTube mentions (title, transcript, description) are the strongest signal for AI visibility (0.737 correlation), about 3x backlinks. The homepage video doubles as the first upload. Cost: free.
- [ ] **Reddit presence** for Perplexity, which cites Reddit heavily (46.7% of citations in one 2026 study). Founder-voice answers in r/PPC, r/marketing, and r/smallbusiness.
- [ ] **Freshness:** content updated within 30 days gets about 3.2x more AI citations. Keep the blog/newsletter cadence and put visible dates on posts.
- [ ] **Organization + SoftwareApplication schema** (JSON-LD) on the homepage, so Google and AI search get clean facts about the company.
- [ ] **Check robots.txt** allows AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended).
- [ ] **Chat agent:** streaming replies, rules for handing off to Nick, weekly transcript review
- [ ] **Manuals:** remove "7 cost layers", "no self-serve", and the old acronym from all manuals
- [ ] **PageSpeed:** Nick runs pagespeed.web.dev (mobile) and sends the score
