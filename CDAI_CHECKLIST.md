# Allocera / CDAI: Master List

Nick's running list. Claude keeps it current and checks items off as they ship.

**Rules:**
- Nothing gets built until Nick has seen it and said yes.
- Every public claim must be provable, and nothing proprietary or sensitive goes on a public page (no thresholds, no internal data).
- No years or dates in titles or bylines.
- Keep the original slugs unless Nick chooses to change one (he decides per page; every change gets a 301 in `website/REDIRECTS.md`).

**Website rules (Nick, Sept 28):**
- **Never delete or retire a page or post.** Anything not needed gets completely redone into a new page that builds reach, authority, and trust.
- **The blog page is last.** It gets rebuilt once, after every page and post, with every final title and slug.
- **Apex was a real pilot.** It stays on the site where it's true: the Sid and Rebecca reviews stay on the homepage, and rebuilt proof pages can tell the pilot story using only provable facts. Never touch Apex data.
- **Every page is built with the live tools** (Search Console, GA4, keyword research, live Google results), aimed at ranking in Google and winning clients, not just a Rank Math score. Each ships with a Rank Math box, GA4 tracking, an image, and a claims table.
- **No "N layers" framing, no fake 80%, no claim that CDAI never assumes costs** (until F5 is merged).

_Last updated: Nov 7, 2026 ~04:40 UTC, after a full night of GoHighLevel marketplace-app work (section I2 rewritten below — everything in it as of Nov 6 is superseded). **New session: read `cdai-engine` repo's `docs/HANDOFF-oct13-2026-go-live.md` §38-39.5 first for GHL state; this file's own `HANDOFF-engine-fixes-sept26.md` is Sept-era engine/website work, separate track.**_

**Scope note (Nov 7):** sections A-H and the "Done" list below this point are UNVERIFIED tonight — they were not re-checked against current Render/GitHub/Supabase state in this session. Only section I2 (GoHighLevel) was fully re-verified. Website work (sections A, B, C) has had no dedicated session since the Sept 27 pause noted below, aside from the unrelated $497 Entry-plan pricing change (handoff §29, live Oct 17) and the blog-build-rules addition (`docs/website/PAGE-BUILD-RULES-nick-oct31-2026.md`, Oct 31) — neither updated this checklist at the time. Treat every website status line below as "as of Sept 27-28" unless a later date is named.

---

## ⚠ Website status (paused end of Sept 27)

**13 pages live and done.** Scores: homepage 81, blog 72, scale/hold/cut 89, 30-day retest 82, marketing costs 89, ROAS calculator 90, offline conversion tracking (tag manager URL) 80, Salesforce Campaign Influence 89. Full table and the 30 remaining items are in `website/FIX_LIST.md`.

**True CAC live at 81 (Sept 28).** Next: Then Nick decides on #7 (margin distortion index) and #8 (proof/case-study pages): rebuild or retire.

**Do these when every page and post is finished (Nick, Sept 27):**
- [ ] **Redirects.** Every slug change needs a 301. The full list, plus a one-minute test, is in `website/REDIRECTS.md`:

  | Old URL | New URL |
  |---|---|
  | `seven-cost-layers` and `blog/seven-cost-layers` | `/marketing-costs/` |
  | `55-directives-study` | `/roas-calculator/` |
  | `allocera-vs-salesforce` | `/salesforce-campaign-influence/` |
  | `true-cac-2` | `/true-cac/` (Nick adding it now) |
  | `marketing-margin-distortion-index` | `/average-cost-per-lead/` |
  | `calculate-marketing-contribution-margin` | Check it lands on `/calculate-contribution-margin/` |

  Add a row the same day any slug changes.
- [ ] **Link pass.** Re-scan every page for links to old slugs; the target is 0. As of Sept 27: 0 on rebuilt pages. Older pages still linking to changed URLs get fixed in their own rebuild or clean.
- [ ] **Blog page.** Rebuild and paste once, with final URLs (pending list in `website/FIX_LIST.md`).
- [ ] **Optional:** GA4 tracking script on the 8 earlier rebuilt pages.

## ⚠ Start here: engine fixes waiting for Nick's yes (built Sept 26 night, nothing live)

Approval sheet: https://claude.ai/artifact/3hNXn12DXcbCd5Q8Nj3EyB · Full details: `HANDOFF-engine-fixes-sept26.md`

- [ ] **D11. Pick one version of the onboarding fixes.** The local session's **PR #37** and the cloud session's branches overlap (F1/F2/F4/F6/Google redirect) and conflict, so only one set can be merged. *Recommendation:* cloud branches (they add Google/LinkedIn, pickers, portal screens), after the local session runs the live test suite on `integration/all-fixes-sept26`.
- [ ] **S1. CRITICAL: close the live data exposure.** Two dashboard views can be read with the public key: 69 campaign rows across all 10 businesses, Apex included. Fix: 2 lines of SQL (`security/views-invoker`), tested 7/7. **Approve first.**
- [ ] **S2. Clients read-only.** Clients could edit or delete their own engine data and read stored logins (`security/clients-read-only`), tested 15/15.
- [ ] **F1+F2. Connect actually syncs + pulls history** (`feat/sync-on-connect`), 45/45. Needs one supervised live test with Nick's own Meta + HubSpot.
- [ ] **F4. Industry at signup + dashboard setting** (`feat/industry-at-signup`), 15/15.
- [ ] **F3. Dashboard shows the engine's own numbers** (`feat/dashboard-engine-numbers`), 12/12.
- [ ] **F6. Test businesses out of the nightly job** (`fix/nightly-skip-test-orgs`), 9/9.
- [ ] **D1. Client email bug + weekly cadence with urgent alerts** (`fix/digest-weekly-latest`), 13/13. It was showing old or duplicate decisions.
- [ ] **F9a. Meta reconnect reminders** (`fix/reconnect-reminders`), 8/8.
- [ ] **F9b. Keep the nightly PDF reports** (`fix/store-audit-reports`), 6/6.
- [ ] **Portal branch** `feat/engine-numbers-industry-connect` (goes live after F1, F4, F3).
- [ ] **F5. No assumed costs** (`fix/no-assumed-costs`), 14/14. **Held until the validation re-run** (at most 3 of 1,352 decisions change).
- [ ] After approval: the full test suite once against live, then the connect test, then F5 last.
- [ ] **Not built, Nick decides:** the reactivated-campaign data window (changes decision math); the unauthenticated connect link (needs design).

---

## A. Nick's list for tomorrow (WordPress / Google, no code)

1. ~~Paste the updated homepage~~ **DONE Sept 26** (Rank Math 81).
2. ~~Merge engine PRs #33, #34, #35~~ **MERGED Sept 26** (all tests pass on combined main). Memory updated (PR #36).
2b. **GA4 key events.** In GA4 → Admin → Events, after the first visits come in, mark these as Key events:
   - `generate_lead`
   - `signup_click`
   - `chat_open`
   - `calculator_code_verified`
3. **Schema.** Set Rank Math → Schema → **Article → Blog Post** on the Northbeam, Rockerbox, and validation report (contribution-margin-marketing) pages. The Pages default was already changed to "None" on Sept 26.
4. **Company info.** Rank Math → Titles & Meta → Local SEO: set Organization, "Allocera Intelligence", and the new logo.
5. **Comments and pings.** Turn them off on every post.
6. **Redirects:** the full list is in `website/REDIRECTS.md` section 0. Post 252 now holds the 30-day retest post at its original slug, and `/30-day-retest-methodology-2/` gets a 301 to it (R11). **Never** a redirect from `/30-day-retest-methodology/` to `/lead-quality/` (R12).
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
| 8 | `/blog/` (Nick's design, new content) | LIVE, **72** (normal for a directory page). **ON HOLD until the rebuild is done (Nick).** Pending list in `website/FIX_LIST.md` → "Blog page: pending changes". |
| 9 | Homepage | LIVE, **81** (Nick: fine as is). Pasted Sept 26: Ask AI section back, F6S logo, tracking, the "What is true cost per lead?" FAQ. Rank Math box in `website/homepage-RANKMATH.md`. |
| 10 | `/30-day-retest-methodology/` | **LIVE in post 252 at 82 (Sept 27 export); slug still `-2`, so change it to `30-day-retest-methodology` (fix-list A1)**. Was (79 → 82 after the title v2; the last points need the keyword in the permalink, Nick's call). Built (`website/pages/30-day-retest-methodology.html` + RANKMATH). Focus keyword "marketing measurement". Every claim checked against the engine code. Includes GA4 tracking. |
| 11 | `/marketing-costs/` (was `/seven-cost-layers/`) | LIVE, **89**. New post, focus keyword "marketing costs"; permalink changed + 301 from the old URL. Built (`website/pages/seven-cost-layers.html` + RANKMATH + image). No "layers" wording anywhere. Includes GA4 tracking. |
| 12 | `/roas-calculator/` (was `/55-directives-study/`) | LIVE, **90**. Brand-new ROAS calculator page (not a 301, per Nick): working calculator with break-even ROAS + real profit for lead-gen. Focus "roas calculator" (1,300/mo). Slug changed; 301 from the old URL (R3 in `website/REDIRECTS.md`). GA4 tracking + `calculator_use` event. |
| 13 | `/tag-manager-real-roi/` | LIVE, **80** (slug kept). New post "Offline Conversion Tracking" (focus "offline conversion tracking"). `/30-day-retest-methodology-2/` will be rebuilt into its own new post (no redirect). |
| 13b | `/salesforce-campaign-influence/` (was `/allocera-vs-salesforce/`) | LIVE, **89**. New post "Salesforce Campaign Influence". Slug changed; 301 = R7 in `website/REDIRECTS.md`. |
| 13c | `/true-cac/` (merged `/true-cac-2/`) | LIVE, **81** (slug kept). New post "Customer Acquisition Cost Formula" + true CAC calculator. `/true-cac-2/` trashed; its 301 = R8 in `website/REDIRECTS.md`. |
| 14 | `/average-cost-per-lead/` (was `/marketing-margin-distortion-index/`) | LIVE, **83**. Rebuilt as "Average Cost Per Lead by Industry". Slug changed; 301 = R10 in `website/REDIRECTS.md`. |
| 14b | `/lead-quality/` (post 245) | LIVE, **88** (featured image still to set). New post "Lead Quality". Pasted into post 245 (the retest post's home), so the 30-day retest post (#10) is restored into post 252 with its original slug `/30-day-retest-methodology/`. R11 (`-2` → retest) and R12 (make sure no `30-day-retest-methodology` → `lead-quality` redirect exists) in `website/REDIRECTS.md`. |
| 14c | Master to-do (Sept 28) | **`website/FIX_LIST.md` rebuilt from the Sept 27 exports:** 17 done, 1 built but not pasted (Northbeam, A2), 33 untouched (sections B and C, by post ID). Redirects R1–R22 in `website/REDIRECTS.md`. |
| 15 | `/proof/`, `/allocera-intelligence-case-study-proof/`, `/case-study-2-oauth-validation/` | **Full rebuilds (Nick: never retire; Apex was a real pilot).** Keep the pilot story where it's provable, lead with the validation, and give each page its own purpose. |
| 16 | `/how-it-works/`, `/about/` | Full rebuilds |
| 17 | `/dashboard/`, validation report, terms, newsletter welcome | Light cleans or quick fixes |
| 18 | `/pricing/` | **ON HOLD** while the free audit is worked out |
| 19 | 22 remaining blog posts | Full rebuild if they have traffic, light clean if not (see FIX_LIST Tier 3) |

**What "light clean" means:** keep the post and its design. Remove the pasted head, the seven layers, the 80%, any Apex claim that can't be proven, the unsourced numbers, and the old "$2,500, don't pay if…" offer, and fix the links.

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

- **D2. BUILT Sept 26 night (in F5, held for the validation re-run).** Engine default costs: CSV uploads add a 2.9–3% platform fee, and Meta lead forms, Ringba, Boberdoo, CSV, and webhook leads add $0.25 per lead of compliance cost. Neither affects the validation or Apex. CallRail is already $0.
  - *Recommendation:* default both to $0 unless the client supplies real values, before the first client who uploads a CSV.
- **D3. Calculator hint.** It says "default $0.25", but the calculator actually uses $0.
  - *Recommendation:* reword it to "only if you pay for per-lead consent certificates".
- ~~D4. Fake names and emails~~ **DONE Sept 26:** removed from all 2,738 test-business records (8 test businesses). 0 real-client rows were touched, and 0 records with names or emails remain.
- **D5. Sync on connect: BUILT Sept 26 night** (`feat/sync-on-connect` + portal branch; also PR #37 from the local session; see D11). Original analysis:
  - **Critical gap found:** a self-serve client who connects Meta, Google, or LinkedIn in one click never gets their ad spend pulled, not even nightly. The nightly job only syncs orgs with a saved ad-account setting, and nothing creates that setting (only Apex has one, set by hand). HubSpot, Salesforce, and CallRail are fine.
  - **The fix:** at connect, find the ad account, create the channel, save the setting, and run the first pull in the background. Directives stay on the nightly run.
  - **Effect on accuracy scores:** none. The directive rules and the validation are untouched.
  - **Trade-offs:**
    - Meta and LinkedIn need an "which ad account?" picker when a login has several (Google already has one).
    - The first pull is 90 days, so it has to run in the background.
    - It adds a little load on the API server during the pull.
- ~~D6. AI links section~~ **DONE:** Nick said yes, and it's back in `website/homepage.html` with real logos and click tracking.
- **D7. The intake form's job** now that self-serve is live.
  - *Recommendation:* free-audit request now; "Partner with us / talk to Nick" once the free audit is settled.
- ~~D8. Apex~~ **CLOSED (Nick, Sept 26):** Apex is not running ads. It stays connected on purpose (to keep working API keys, and as proof of a connected client). The nightly Apex errors are expected. Don't touch Apex. Original finding, kept for reference:
- **(ref) D8. Apex (Sept 26, Render logs + database, read-only).**
  - **What's wrong:** Apex's Meta sync fails every night with a database error (`campaigns_channel_id_fkey`). Apex's saved Meta settings point to a channel (`7acaf75a…`) that no longer exists; Apex only has one channel, `paid_search`. So no Meta spend has come in, and there have been no decisions since Aug 13.
  - **Google:** every night the log also says "No Google Ads token found", because the saved Google settings don't match the Google token on file.
  - **The fix:** repoint Apex's Meta and Google settings to a real channel. That's a small change to Apex's data, so **Claude needs Nick's explicit OK** (the standing rule is never to touch Apex data).
  - **Optional code guard:** when a saved channel is missing, create it instead of failing. That would protect every future client.
  - **Nick decides:** fix Apex (yes/no), and add the guard (yes/no).
- **D9. Stripe, Boberdoo, Ringba accuracy fixes: BUILT Sept 26 night in F5** (`fix/no-assumed-costs`), held until the validation is re-run. Original note: Saved to the engine memory TODO. When they're picked up: test suite first, then re-run the validation. The Sept 2026 validation ran its data through these three adapters exactly as they are today, so changing how they count money would move the 89.5% results and would need a re-test.
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
- [ ] **Render: move `allocera-control-tower` from `1 2 * * *` to `0 11 * * *`.** It currently runs while the engine is still mid-run (F7).
- [ ] **Supabase secret key in plain text** in `cdai-admin-backend/README.md` (line 8): rotate it, then remove it from the file.
- [ ] **Reconnect Apex's Meta login before Oct 10, 2026** (the token expires; Apex is kept connected for working keys).
- [ ] **S1 data exposure:** see "Start here" (approve the fix first).

---

## I2. GoHighLevel marketplace app (Nov 6-7, 2026 — rewritten Nov 7 ~04:40 UTC, everything above this point in I2 is superseded)

Cross-repo work (`cdai-engine` + `cdai-portal`); nothing here touches this repo's own code. Full detail: `cdai-engine` repo `docs/HANDOFF-oct13-2026-go-live.md` §38-39.5 and `docs/ops/GHL-APP-DESIGN-RECORD-nov4-2026.md`.

**Shipped overnight Nov 6-7 (all merged, all verified — tests, mutants, independent review, each per IC8 gate):**
- [x] Engine: `free_plan` sign-in message — a confirmed admin on an unpaid sub-account gets a distinct "CDAI is on the Free plan" answer instead of the generic failure (cdai-engine PR #195, portal message PR #23 on `cdai-portal`). A real client-side bug (reading the response body only on HTTP success, so the engine's actual 403 response was never read) was caught by independent review before merge and fixed.
- [x] Engine PR #196: handoff doc recording the above, retroactively verified.
- [x] Engine PR #197: handoff doc — first real admin-confirmation attempt against the live GoHighLevel API found a new, real blocker (next item).
- [x] **Engine PR #198 (merged): fixed `GET /users/{id}` sending the wrong GoHighLevel API version header.** This call — which confirms a sign-in claimant really is an admin of the real sub-account, the security-critical step — had NEVER actually been exercised against the real GoHighLevel API before tonight (an older code path always refused before reaching it). First real attempt got HTTP 400 on every try. Root cause: the call sent `Version: 2021-07-28` (correct for the engine's other, older GoHighLevel endpoints — contacts, opportunities — already proven live), but GoHighLevel's own current docs for this specific endpoint require `Version: v3`, a separate, newer API generation running in parallel. Fixed, tested (regression test + 82/82 mutants), independently reviewed. **Deployed; not yet re-tried live** — next real sign-in attempt will show whether `v3` is the whole fix or whether another gap is under it (the fix is doc-based, not yet proven against the real API).
- [x] Investigated "Open the CDAI portal link goes to Demo Lead Gen" (Nick's live report) — **not a bug, not a security issue.** Zero Supabase identities of the GHL-sign-in shape exist yet (no GHL sign-in has ever actually succeeded, for anyone); the link just opens the portal homepage, and Nick's own browser was already logged into his own Demo account. Confirmed via direct Supabase/Render evidence, not inference.
- [x] Confirmed via GoHighLevel's own dev-portal Testing tab: "CDAI Test Agency" (`D2ez121Jz46ooatsAzGA`) IS GoHighLevel's real Sandbox/App Test Account mechanism — Active, CDAI connected, expires May 3 2027. No new test account needed for the billing test below.

**Still gated exactly as designed — nothing bills, nothing goes live:** `CDAI_APP_SSO_ENABLED` is ON (live, that's how tonight's bugs were caught); `CDAI_APP_PAID_TIERS` and `CDAI_APP_ORGS_ENABLED`'s paid-marking path stay OFF. App form stays DRAFT.

**Open, in strict order (don't skip ahead — each unblocks the next):**
1. [ ] **Verify the Nov 7 `v3` fix against a real sign-in attempt.** Needs Nick to open the CDAI page on sub-account `49617 US-550` again. If it still fails, the error class returned (now logged) narrows down whether it's a scope, parameter, or response-shape problem next — not another blind guess.
2. [ ] **P4: one real test payment + refund**, on the GoHighLevel Sandbox account, cheapest plan (Entry, $497/mo). **Blocked on one unresolved question Claude could not verify from GoHighLevel's docs: whether a paid-plan subscription inside the Sandbox account triggers a real charge.** Nick's call once step 1 is confirmed working: try it and watch closely, or ask GoHighLevel support first. This settles `CDAI_GHL_AMOUNT_UNIT` and the real PlanChange event shape.
3. [ ] **Digest-recipient gate** (a GHL sign-in's identity is a private synthetic address that can't receive mail — needs a real contact e-mail captured somewhere before any paid GHL org gets the nightly digest).
4. [ ] **Apply migration `20261105100000`**, then set `CDAI_APP_PAID_TIERS=retainer` — turns real billing mapping on. Needs Nick's explicit yes; this is the actual "GHL clients start getting charged and served" switch.
5. [ ] **Untick unused OAuth scopes** in the dev portal (several were requested for later features, never used; least-privilege cleanup) and **set the 5 real paid plan IDs** (Entry/Starter/Growth/Scale/Enterprise — only Free's was captured) for `CDAI_APP_PLAN_MAP`.
6. [ ] **Listing assets, lawyer review of the GoHighLevel developer agreement, terms/privacy wording, the E5 Wheels pilot friend's written OK.** Nothing here is built — see Listing section below.
7. [ ] **Nick submits the public listing for GoHighLevel's own review** (their process: "within 10 business days," real reports run 2-4 weeks — expected wait, not a problem to chase). App stays DRAFT until this and everything above it is done.

---

## I3. GoHighLevel marketplace listing copy (status as of Nov 6, re-confirmed Nov 7 — unchanged tonight, not worked on)

Location: `docs/listing/` in `cdai-engine` (not this repo). **DRAFT ONLY — never published, pasted, or submitted.**

- [x] Research done; one draft file written: `01-listing-draft.md` (name, tagline, description, how it works, plans, data/permissions, FAQ).
- [ ] **Not started:** site copy for the listing (02), pricing-page copy for GHL clients (03), terms draft (04), privacy draft (05), social posts (06).
- [ ] **Lawyer review** of GoHighLevel's developer agreement, terms, and privacy wording — not done, flagged as required before anything is submitted.
- [ ] **E5 Wheels pilot friend's written OK** and free-pilot terms — not obtained.
- [ ] Four open questions for Nick sitting in the listing folder's own README, unanswered: (1) how "one campaign" is enforced for the free audit, (2) uninstall data retention (keep vs delete after N days — affects privacy-policy wording), (3) whether CDAI checks ad spend against a GHL plan's spend band, (4) whether GoHighLevel's listing has specific asset-size/field requirements — not yet read.
- **Why this is blocked, not just slow:** the listing copy can't be finalized responsibly until the app itself actually works end to end (GHL gameplan steps 1-5 above) — otherwise the copy would describe capabilities not yet proven, which is exactly what the founder's proof-bar rule forbids. This is sequential by design, not an oversight.

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

- [x] **Sept 26 (night, cloud session):**
  - All blueprint findings built as 10 engine branches + 1 portal branch, pushed, not merged.
  - 144 new test checks pass; existing tests unchanged vs main.
  - Found and fixed (awaiting approval): the live data exposure (S1), clients able to write their own data (S2), the digest showing old decisions (D1).
  - Handoff written: `HANDOFF-engine-fixes-sept26.md`.
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
- [x] **Nov 6, 2026: GoHighLevel marketplace app — real bugs fixed, three env vars flipped live, one new blocker found.** Full detail in section I2 above. Summary: cdai-engine PR #189 merged (a test-blind-spot and a real `.fullmatch()` production fix, 75/75 + 66/66 mutants); cdai-portal PR #20 opened and made fully green (test coverage for the `/ghl.html` relay plus 3 unrelated CI infra fixes), awaiting Nick's merge; `CDAI_APP_ENABLED`/`CDAI_APP_ORGS_ENABLED`/`CDAI_APP_SSO_ENABLED` flipped on on Render (`cdai-engine`), `/health` verified 200; live probe of production found `GHL_APP_SHARED_SECRET` is not set, blocking every sign-in — reported to Nick, needs his action.
- [x] **Nov 3, 2026 (separate from CDAI engine): HubSpot/Salesforce detection
  scanner built for Nick's own cold-outreach prospecting.** Standalone tool, not
  part of the CDAI product, delivered to Nick directly as `scanner_final.py`
  (v14.0.0). Full writeup: `HANDOFF-crm-detection-scanner-nov3-2026.md`. 8 code-review
  bugs found and fixed (SSRF gap, a NameError, imprecise career-page evidence,
  testimonial-card misattribution, incomplete robots.txt precedence, sitemap
  recursion, duplicate-signal double-counting, batch-cleanup-on-interrupt), plus
  one more found live after merging Nick's own additions (a Google-link classifier
  false positive). 36/36 self-tests, 3/3 live regression against real companies.
  G2/Capterra/TrustRadius/Google/Facebook review scraping explicitly evaluated and
  declined — their own Terms of Use prohibit it.

**Verified facts to reuse:**
- 89.5% overall (1,210/1,352), math 100%.
- By decision: Scale 98.0%, Hold 95.2%, Pause 85.2%, Flag 70.9% (82 neutral), Cut 55.6%, Investigate 100%, Renegotiate 100%, Quarantine 12/12 caught.
- CDAI = Capital, Decision, Accuracy, Intelligence.
- Clients need HubSpot or Salesforce, plus paid ads and/or bought leads.
- Self-serve is live.
- Retainers start at $1,500/mo.
- USA only.
- Seven cost layers is dead.
