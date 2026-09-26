# Allocera / CDAI: Master List

Nick's running list. Claude keeps it current and checks items off as they ship.

**Rules:**
- Nothing gets built until Nick has seen it and said yes.
- Every public claim must be provable, and nothing proprietary goes on a public page.
- No years or dates in titles or bylines.
- Keep the original slugs.

_Last updated: Sept 26, 2026 (late), after the engine fixes Nick approved and the homepage AI section was restored._

---

## A. Nick's list for tomorrow (WordPress / Google, no code)

1. ~~Paste the updated homepage~~ **DONE Sept 26** (Rank Math 81).
2. **Merge these engine PRs** after you've read each one; all are tested:
   - **#33** Bing + labels: https://github.com/fullsendorganicks-collab/cdai-engine/pull/33
   - **#34** Digest logo: https://github.com/fullsendorganicks-collab/cdai-engine/pull/34
   - **#35** Test-business errors: https://github.com/fullsendorganicks-collab/cdai-engine/pull/35
2b. **GA4 key events.** In GA4 → Admin → Events, after the first visits come in, mark these as Key events:
   - `generate_lead`
   - `signup_click`
   - `chat_open`
   - `calculator_code_verified`
3. **Schema.** Set Rank Math → Schema → **Article → Blog Post** on the Northbeam, Rockerbox, and validation report (contribution-margin-marketing) pages. The Pages default was already changed to "None" on Sept 26.
4. **Company info.** Rank Math → Titles & Meta → Local SEO: set Organization, "Allocera Intelligence", and the new logo.
5. **Comments and pings.** Turn them off on every post.
6. **One redirect.** `/30-day-retest-methodology-2/` → `/tag-manager-real-roi/` (it's an exact copy). Don't redirect `/seven-cost-layers/`; it's getting a new post.
7. **Delete "every two weeks"** from `/newsletter-welcome/` and `/roas-looks-good-campaigns-lose-money/`. No newsletter has been sent yet.
8. **Turn on Rank Math → 404 Monitor.**
9. **Search Console exports.** Click each reason and export its URL list:
   - "Crawled – currently not indexed" (16)
   - "noindex" (4)
   - "404" (2)
   - "Redirect error" (1)
10. **Rank Math titles and descriptions** for the privacy, terms, and data-deletion pages. They have none.
11. **Categories (later).** Every post is "Uncategorized". Create these and assign each post:
    - Marketing Methodology
    - Tool Comparisons
    - Personal Injury Law
    - Home Services
    - More Industries
12. **`/home-sample/` pages (later, no rush).** Set Parent to "(no parent)" on these 7, and add a 301 from each old URL:
    - Northbeam
    - Rockerbox
    - validation report
    - case study
    - privacy
    - terms
    - data deletion

    Claude then updates every internal link.
13. **Tag Manager (optional).** Tracking now runs straight into GA4. If you create a GTM container, send the `GTM-XXXXXXX` ID; the events already push to `dataLayer`, so GTM picks them up too.

**Done Sept 26:** every page is on Elementor Canvas (leave it), and the schema defaults are fixed (Posts: Article → Blog Post; Pages: None).

---

## B. Website pages (Claude builds, Nick pastes)

Full page-by-page list: **`website/FIX_LIST.md`** (41 pages still carry old or false info).

| # | Page | Status |
|---|---|---|
| 1 | `/net-marketing-contribution/` | LIVE, **91** |
| 2 | `/calculate-contribution-margin/` | LIVE, **90** |
| 3 | `/scale-hold-cut-pause-framework/` | LIVE, **89** |
| 4 | `/triple-whale-vs-rockerbox-vs-allocera/` | LIVE, **90** (optional: drop "2026" from the SEO title) |
| 5 | `/home-sample/northbeam-alternative/` | LIVE, **90** |
| 6 | `/home-sample/rockerbox-alternative/` | LIVE (score not reported) |
| 7 | `/cost-per-signed-case/` | LIVE, **90** |
| 8 | `/blog/` (Nick's design, new content) | LIVE, **72** (normal for a directory page) |
| 9 | Homepage | LIVE, **81** (Nick: fine as is). Pasted Sept 26: Ask AI section back, F6S logo, tracking, the "What is true cost per lead?" FAQ. Rank Math box in `website/homepage-RANKMATH.md`. |
| 10 | **NEXT: `/30-day-retest-methodology/`** | Rebuild around the Sept 2026 validation (89.5%) and remove the fake 80%. Nick sent the current HTML. Verify every "retest" claim against the engine first. |
| 11 | `/seven-cost-layers/` | New post at the same URL (246 impressions). The concept is dead; the new topic is hidden marketing costs, stated plainly. |
| 12 | `/55-directives-study/` | 301 to the validation report (the whole page is the fake 80%) |
| 13 | `/tag-manager-real-roi/`, `/allocera-vs-salesforce/`, `/true-cac/` + `/true-cac-2/` (merge) | Full rebuilds (80%, seven layers, pasted head) |
| 14 | `/marketing-margin-distortion-index/` | **Nick decides:** rebuild or retire (80%, Apex, "2026" in the title, unsourced stats) |
| 15 | `/proof/`, `/allocera-intelligence-case-study-proof/`, `/case-study-2-oauth-validation/` | **Nick decides:** these are the Apex story. Rewrite around the validation, or retire. |
| 16 | `/how-it-works/`, `/about/` | Full rebuilds |
| 17 | `/dashboard/`, validation report, terms, newsletter welcome | Light cleans or quick fixes |
| 18 | `/pricing/` | **ON HOLD** while the free audit is worked out |
| 19 | 22 remaining blog posts | Full rebuild if they have traffic, light clean if not (see FIX_LIST Tier 3) |

**What "light clean" means:** keep the post and its design. Remove the pasted head, the seven layers, the 80%, Apex, the unsourced numbers, and the old "$2,500, don't pay if…" offer, and fix the links.

**Google index (Sept 26):** 46 pages indexed, 44 not. 16 are "crawled, not indexed", which the rebuilds fix. The rest need Nick's exports (A9).

---

## C. Homepage tracking (added Sept 26, in `website/homepage.html`)

Everything reports to GA4 `G-29J4V3VQ7B`. It loads GA4 only if the site doesn't already, so page views never double-count. Every event also pushes to `dataLayer` for Tag Manager. No names, emails, or chat text are ever sent.

| Event | When it fires |
|---|---|
| `chat_open`, `chat_message_sent`, `chat_suggestion_click`, `chat_close` | VINDEX / Ask CDAI |
| `calculator_start`, `calculator_code_requested`, `calculator_code_verified` | Distortion calculator |
| `form_submit`, `generate_lead` | Free audit / contact form (`generate_lead` fires on success) |
| `signup_click`, `portal_click`, `pricing_click` | Get Started, Client Portal, and any pricing link |
| `button_click`, `scroll_link_click`, `email_click`, `phone_click`, `menu_open` | Every other button and link, with its text and section |
| `section_view` | Each homepage section a visitor reaches: hero, tools, problem, how, capabilities, calculator, FAQ, intake |

**Views of the pricing page itself:** GA4 → Reports → Pages and screens → `/pricing/`.

Tested in a browser Sept 26: all events fired with 0 errors.

---

## D. Decisions for Nick (open)

- **D2. Engine default costs.** CSV uploads add a 2.9–3% platform fee, and Meta lead forms, Ringba, Boberdoo, CSV, and webhook leads add $0.25 per lead of compliance cost. Neither affects the validation or Apex. CallRail is already $0.
  - *Recommendation:* default both to $0 unless the client supplies real values, before the first client who uploads a CSV.
- **D3. Calculator hint.** It says "default $0.25", but the calculator actually uses $0.
  - *Recommendation:* reword it to "only if you pay for per-lead consent certificates".
- ~~D4. Fake names and emails~~ **DONE Sept 26:** removed from all 2,738 test-business records (8 test businesses). 0 real-client rows were touched, and 0 records with names or emails remain.
- **D5. Sync on connect.** Today, when a new client connects Meta, Google, or their CRM, nothing is pulled until the nightly run at 2 AM UTC (about 10 PM Eastern). A client who signs up at 9 AM sees an empty dashboard all day. "Sync on connect" means the first pull starts the moment they click Connect, so they see their numbers within minutes.
  - *Recommendation:* yes. It's the first impression for every self-serve client.
  - Say yes and Claude builds and tests it.
- ~~D6. AI links section~~ **DONE:** Nick said yes, and it's back in `website/homepage.html` with real logos and click tracking.
- **D7. The intake form's job** now that self-serve is live.
  - *Recommendation:* free-audit request now; "Partner with us / talk to Nick" once the free audit is settled.
- **D8. Apex: ROOT CAUSE FOUND (Sept 26, Render logs + database, read-only).**
  - **What's wrong:** Apex's Meta sync fails every night with a database error (`campaigns_channel_id_fkey`). Apex's saved Meta settings point to a channel (`7acaf75a…`) that no longer exists; Apex only has one channel, `paid_search`. So no Meta spend has come in, and there have been no decisions since Aug 13.
  - **Google:** every night the log also says "No Google Ads token found", because the saved Google settings don't match the Google token on file.
  - **The fix:** repoint Apex's Meta and Google settings to a real channel. That's a small change to Apex's data, so **Claude needs Nick's explicit OK** (the standing rule is never to touch Apex data).
  - **Optional code guard:** when a saved channel is missing, create it instead of failing. That would protect every future client.
  - **Nick decides:** fix Apex (yes/no), and add the guard (yes/no).
- **D9. Stripe, Boberdoo, Ringba accuracy fixes: NEEDS NICK (these would change validated numbers).** The Sept 2026 validation ran its data through these three adapters exactly as they are today, so changing how they count money would move the 89.5% results and would need a re-test.
  - **Stripe** assumes a 7% processing fee on every sale. Real Stripe US pricing is about 2.9% + 30¢. Fixing it means every validated business shows higher margins.
  - **Boberdoo:** the price paid for each lead lands only in dashboard CPL and is never counted in true cost. Fixing it means Boberdoo campaigns show higher costs, and those campaigns include the source of all 169 PAUSE results.
  - **Boberdoo** also puts all leads under one campaign, regardless of which Boberdoo campaign they came from.
  - **Ringba** drops partner payouts when a call has no partner ID.
  - *Recommendation:* fix all four for real clients, then re-run the validation so the published numbers match. Claude does nothing until Nick says go.
- **Free audit credit wording.** Pricing page: "first 90 days"; homepage: "100% toward a retainer". Pick one when the free audit is settled.

---

## E. Engine and product (Claude, after a yes)

- [ ] **Free Distortion Audit in Stripe.** Being handled in another Claude Code session; the prompt is in `STRIPE_FREE_AUDIT_PROMPT.md`. On hold while Nick works it out.
- [x] **Bing fixed (PR #33, awaiting merge).** Spend now lands per campaign, and a re-sync no longer counts the same spend twice (a second bug found along the way). 19/19 checks pass. Bing isn't live yet, and it wasn't part of the validation.
- [x] **Ringba and Boberdoo leads are labeled correctly (PR #33).** A client's CSV re-upload can no longer delete them. No math changes. 6/6 checks pass.
- [ ] **Stripe, Boberdoo, Ringba money fixes:** waiting on Nick (see D9).
- [ ] **Turn on the nightly pull for Bing, Ringba, Boberdoo, and Stripe** once D9 is decided.
- [x] **Digest email logo fixed (PR #34, awaiting merge).** Gmail blocks embedded images, so the logo showed broken; it now uses the logo hosted on the website. The health report also switched to the new logo.
- [x] **Test-business nightly errors fixed (PR #35, awaiting merge).** The Salesforce sync no longer calls a fake address for the 9 test businesses, which was 27 errors every night.
- [ ] **VINDEX live test.** Ask about 15 real prospect and investor questions; Nick reviews the answers.
  - Must say: clients need HubSpot or Salesforce, and run paid ads and/or buy leads.
  - Must never contradict the validation.
- [ ] **VINDEX upgrades:** streaming replies, clear hand-off-to-Nick rules, and a weekly transcript review.
- [ ] **Manuals rewrite.** Remove "7 cost layers", "no self-serve", the old acronym, the stale integration counts, and the 80%.
- [ ] **VINDEX trademark check** (Nick): a registered VINDEX mark exists (Vindex LLC, esports, serial 88671256).
- [ ] **Competitive research.** Offered, awaiting a yes.

---

## F. Homepage video (Nick: "needs to be redone: good but cheap")

- [ ] Claude writes the script (demo/explainer style, 90 seconds to 3 minutes). Nick approves it.
- [ ] Nick sends a screen recording of the portal, plus the logo and screenshots.
- [ ] Voiceover: Nick's own voice (best for trust), or free text-to-speech.
- [ ] Claude renders a motion-graphics cut (1080p, no watermark).
- [ ] Publish on YouTube with "Allocera" and "CDAI" in the title, then embed it at the top of the homepage. It must autoplay muted and load instantly.

---

## G. Growth ideas (Nick says yes or no to each)

- [ ] Show the price level ("from $1,500/mo") near the main button.
- [ ] Founder block: Nick, 3 years building, photo. Needs a photo and Nick's OK.
- [ ] A sample report visitors can open (a clearly labeled fictional business).
- [ ] "15 minutes with the founder" booking button (free Calendly).
- [ ] Date the proof: "Validated Sept 2026".
- [ ] Get the two Apex reviews onto G2.
- [ ] YouTube channel (the video is the first upload), and founder-voice answers on Reddit (r/PPC, r/marketing, r/smallbusiness).
- [ ] Organization + SoftwareApplication schema on the homepage.
- [ ] Check that robots.txt allows AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended).
- [ ] New posts for high-value keywords:
  - "google ads optimization" (390/mo)
  - "personal injury law firm marketing" (720/mo, CPC about $106)

---

## H. Security (Nick; important)

- [ ] **Supabase service-role key:** it was pasted in chat on Sept 21. Rotate it in Supabase → Settings → API, then update it everywhere it's used (Render env vars).
- [ ] **Supabase database password:** hardcoded in `run_full_directive.py` and `time_engine.py`, and the former cofounder may know it. Rotate it.
- [ ] **Anthropic key pasted in chat on Sept 25:** make sure it's revoked in the Anthropic console. The chat bot must only use the new key stored in Render (`ANTHROPIC_API_KEY_chat_bot`).
- [ ] Rotate other shared keys the former cofounder could have seen (Resend, Stripe, Render).
- [ ] Check the team member lists in Render and Supabase.
- [ ] Delete the 19 old validation cron jobs on Render (they re-run every year).

---

## I. Partnerships

- [x] CallRail email sent Sept 25, with the logo and listing description. The call with Karina and Eric is **booked**.
- [ ] Before the call: be ready to explain how the integration will be promoted (pricing page, integration docs, outreach).
- [ ] Direction: partner with companies that already have the customers (CallRail first).

---

## J. Access that would help Claude (Nick)

- [ ] **Network allowlist** (cloud environment → Edit → Network access). Add your own site so Claude can check live pages, plus `support.google.com`, `nngroup.com`, `gartner.com`, `facebook.com`, and `wikipedia.org`.
- [ ] **Gmail for alloceraintelligence@gmail.com**, if Claude should read the Control Tower emails. The connected Gmail is fullsendorganicks@gmail.com.
- [ ] **PageSpeed score:** run pagespeed.web.dev (mobile) on the homepage and send the number.

---

## Done

- [x] **Sept 26 (late):**
  - Engine PRs #33, #34, #35 built and tested.
  - Fake names and emails stripped from the test data.
  - Apex root cause found.
  - Homepage AI section restored, and F6S shows its real logo.
- [x] **Sept 26:**
  - 8 pages rebuilt (scores above).
  - Blog rebuilt on Nick's design.
  - Every page moved to Elementor Canvas.
  - Schema defaults fixed.
  - Homepage tracking built and tested.
  - Full fix list written.
  - Stripe free-audit prompt written.
- [x] **Sept 25:**
  - Homepage final and live: hero kept, "What CDAI does", trust FAQs, US-accurate calculator, real logos, no fake numbers.
  - VINDEX chat live.
  - Dashboard trust fix, SCALE fix (98.0%), privacy fix, CallRail nightly sync + campaign mapping, and $0 call compliance cost.
  - Math re-verified: all 1,352 validation grades reproduced exactly.
  - PAUSE 85.2%: keep quoting it (Nick).
- [x] Former cofounder fully offboarded (PR #16).

**Verified facts to reuse:**
- 89.5% overall (1,210/1,352), math 100%.
- By decision: Scale 98.0%, Hold 95.2%, Pause 85.2%, Flag 70.9% (82 neutral), Cut 55.6%, Investigate 100%, Renegotiate 100%, Quarantine 12/12 caught.
- CDAI = Capital, Decision, Accuracy, Intelligence.
- Clients need HubSpot or Salesforce, plus paid ads and/or bought leads.
- Self-serve is live.
- Retainers start at $1,500/mo.
- USA only.
- Seven cost layers is dead.
