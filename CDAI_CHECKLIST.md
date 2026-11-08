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
- [x] **S1. Re-verified Nov 8 2026: production is actually already safe, but the fix was never in tracked history — now closed.** Checked directly against the live database: `vw_contribution_margin_v2` and `vw_true_cost_recent30d` already have `security_invoker=true` and zero `anon` SELECT grant — the Sept 26 exposure is not currently live. But the fix (`security/views-invoker`, commit `bb4020d`) was applied to production outside git, never merged into `main` — a real drift: a schema rebuild from migrations alone would have silently reintroduced it. Closed via `cdai-engine` PR #213 (cherry-picked onto current `main`, conflicts in shared test-harness files resolved by keeping `main`'s current versions, 7/7 test pass against current schema, zero regressions on adjacent suites, protected files untouched, confirmed a no-op against live production before opening). Awaiting Nick's merge.
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

- [x] **Nov 8 2026: `v3` fix confirmed against real sign-in attempts — found and fixed a second real bug, found a third (open), and settled why no directive ever appeared.** Full sequence, from live Render logs and direct production Supabase reads, not inferred:
  - **Second real bug, found and fixed: agency-admin sign-in always refused (`agency_not_installed`).** `_company_connection()` required `status='active'` on the agency (Company) connection row, but nothing in the codebase ever sets that status for a Company row (org-linking, the only thing that flips a row to `'active'`, is keyed exclusively by `location_id`, and a Company row always has `location_id IS NULL`). Structurally unreachable — every agency-admin sign-in was refused, for every company, always. Found live at 18:34:27 UTC during Nick's own GHL submission-video recording. Fixed, deployed (`cdai-engine` PR #207, confirmed live). The test suite never caught it because its fixture hardcoded `status='active'` on the Company row directly in SQL, bypassing the real insert path (which produces `'pending'`) — fixture corrected too.
  - **Third real finding, open: `no_access`.** Past the fix above, a real sign-in (both agency-view and a direct sub-account login, confirmed both) reaches GoHighLevel's real `GET /users/{id}` and gets refused because `_can_reach()` can't confirm the signed-in user is an admin who lists this sub-account — exactly the gap `_can_reach()`'s own docstring already named as open until a real answer was seen (P4). A temporary, reviewed, no-PII diagnostic (`cdai-engine` PR #211, logs response *shape* only — key names, never values) is live; next real sign-in attempt will capture the actual shape and settle it.
  - **Real GHL data pull against the seeded `49617 US-550` sub-account, via `tools/ghl_probe.py` (read-only, no DB writes):** all 5 live API calls succeeded (contacts search/detail, won + all opportunities, payment transactions). 5 contacts, 4 opportunities (1 won $3,934 — matches the dashboard's $3.93K exactly, 2 open, 1 abandoned), 0 payment transactions. The adapter's own email-hashing and timestamp-parsing logic ran clean against the real response shapes, no crashes. **Real finding, not a bug:** none of this sandbox's seeded contacts carry GoHighLevel's own first-touch attribution data (`attributionSource`/`attributions` both absent on the detail call) — these leads land unattributed by design, not by error.
  - **Why no directive has ever appeared for this org, settled, not a gap:** `tools/ghl_e2e.py`'s own precondition (`installed sub-accounts without an organization: 0`) correctly reported zero, because every real install now auto-creates its org immediately — expected given current config, not a bug. The deeper reason nothing shows (the portal itself says "Payment pending — preview mode"): this test sub-account was created on the **Free plan**, and Free (tier `audit`) is *never* marked `payment_status='received'` — confirmed working exactly as Nick's own §12b decision (Nov 7 2026) specifies: *"its 1 free campaign audit... we are not giving things away for free beyond that."* `scheduler.py --org <org_id>` (the manual override) still correctly refuses an unpaid org — it bypasses the test-org-name filter, not the payment gate, by design. The free audit is explicitly meant to be run by hand, not by the automatic nightly engine — exactly the mechanism being exercised by hand right now. **This is the exact same gate item 4 below is about, now proven real on a live org instead of theoretical.**
  - org_id for `49617 US-550` (location `etxQraCiShaq6WowIJIE`): `d9a69755-299a-47da-ade1-3f31ac1854ad`, `status='active'` in `cdai_app_connections`, `user_type='Location'`.
- [x] **Nov 8 2026, same session: full real end-to-end pipeline run proven against the seeded `49617` org — real GHL data in, real rows out, correctly unattributed.**
  - **`SCHEDULER_GHL_SYNC=on` and `CDAI_APP_ENABLED=on` set permanently** on both Render `cdai-engine` services (the web service AND the cron job — they are separate services on Render despite sharing a name and an environment group; env vars do NOT propagate between them, confirmed the hard way when the first attempt silently did nothing because it was set on the wrong one). This is the last switch named in the design record's "before the switch is turned on in production" sequence (§22) — flipped only after P4 (this run) and the §12b decision (already made Nov 7) were both satisfied.
  - **Confirmed safe to leave on:** queried every active GHL-linked org directly — only two exist (`etxQraCiShaq6WowIJIE` / our test org, and one other, `lr3uZVFUkNLk3yaFQAPO`), both `payment_status='pending'`. `CDAI_APP_PAID_TIERS` is still unset, so nothing else can be marked paid yet — turning the sync switch on has zero effect on any real client right now, by construction, not by luck.
  - **Test method:** org `d9a69755-299a-47da-ade1-3f31ac1854ad`'s subscription was set to `payment_status='received'` (Nick's explicit yes), `scheduler.py --org <id>` run twice (once before, once after the env fix) on Render's Shell, then reverted to `pending` immediately after — confirmed reverted directly in the database, and confirmed zero leftover rows anywhere unexpected.
  - **Result, verified directly against the database, not just logs:** `[CDAI_APP][GHL] contacts sync: ok pages=1 seen=5 no_email=2 ... unattributed=3`, `won-deals sync: ok pages=1 seen=1 ... inserted=1`. Database read-back: 3 `lead_events` (`ingestion_source='ghl'`, correctly labeled, not defaulting to `'csv'`), 1 `sales_events` row (the real $3,934 won deal), 0 `campaigns`, 0 `directive_events`. Exactly right: with zero attribution data on any of this sandbox's seeded contacts (confirmed earlier by the probe), the engine correctly refuses to invent a campaign or issue a directive for revenue it can't attribute to one — the "never guesses" rule holding under a real run, not just in tests.
  - **Still open, unaffected by any of this:** the `no_access` sign-in finding (diagnostic is live, next real sign-in attempt will capture it); `CDAI_APP_PAID_TIERS` (item 4 below) is what would let a *real* GHL client's payment actually reach this now-working pipeline.

**Open, in strict order (don't skip ahead — each unblocks the next):**
1. [x] **Verify the Nov 7 `v3` fix against a real sign-in attempt — done, see Nov 8 entry above.** The `v3` header fix itself is confirmed correct (sign-in reaches the real GoHighLevel admin-confirmation call now); what blocks a successful sign-in today is the separate, still-open `no_access` finding above.
2. [ ] **P4: one real test payment + refund**, on the GoHighLevel Sandbox account, cheapest plan (Entry, $497/mo). **Blocked on one unresolved question Claude could not verify from GoHighLevel's docs: whether a paid-plan subscription inside the Sandbox account triggers a real charge.** Nick's call once step 1 is confirmed working: try it and watch closely, or ask GoHighLevel support first. This settles `CDAI_GHL_AMOUNT_UNIT` and the real PlanChange event shape.
3. [x] **Digest-recipient gate: done, Nov 7 2026.** `cdai-engine` PR #210, merged, live (Render confirmed `live` on both the web service and the nightly cron). `scheduler.get_client_email()` now reads the real captured `ghl_contact_email` first and never falls back to the undeliverable synthetic sign-in address — returns `None` (skips the digest that cycle) instead of attempting to mail an address that can't receive it. Tested: 6/6 new test cases, 5/5 mutants killed, zero regressions on the one other caller.
4. [ ] **Apply migration `20261105100000`**, then set `CDAI_APP_PAID_TIERS=retainer` — turns real billing mapping on. Needs Nick's explicit yes; this is the actual "GHL clients start getting charged and served" switch.
5. [ ] **Untick unused OAuth scopes** in the dev portal — **blocked while the app is In Review.** Nick confirmed directly (Nov 8 2026): the dev portal will not let him change anything while the listing is under review. My earlier claim here that scopes are "confirmed editable even post-submission" was wrong — unverified, inferred from a general lifecycle screenshot that never actually said that, and I stated it as fact. Corrected: this item waits until the app is either approved (Live) or sent back (Disapproved reverts it to editable, per the same lifecycle screen), whichever comes first. **Keep exactly these 7 once editing is possible again** (confirmed directly in `cdai_app.py`'s `LOCATION_SCOPES`/`COMPANY_SCOPES`): `contacts.readonly`, `opportunities.readonly`, `payments/transactions.readonly`, `locations.readonly`, `users.readonly`, `oauth.readonly`, `oauth.write`. Untick anything else. Also **set the 5 real paid plan IDs** (Entry/Starter/Growth/Scale/Enterprise — only Free's was captured) for `CDAI_APP_PLAN_MAP`, same blocker. Nick's own action, dev-portal UI.
6. [ ] **Listing assets, lawyer review of the GoHighLevel developer agreement.** Terms/privacy wording is **done** (Nov 7, GHL-specific clauses added to the live Terms of Service and Privacy Policy — see I3 below). Lawyer review and the E5 Wheels pilot friend's written OK are still open.
7. [x] **Nick submitted the public listing for GoHighLevel's own review, Nov 7 2026.** App version 1.0.0, status In Review, 2 installs recorded at submission. (Their process: "within 10 business days," real reports run 2-4 weeks — expected wait, not a problem to chase.)
8. [ ] **NEW (Nick, Nov 8 2026): update `chat_agent.py` (VINDEX) to actually know about GoHighLevel.** Checked directly — zero mentions of "GoHighLevel" or "GHL" anywhere in `chat_agent.py` right now. A prospect asking "do you integrate with GoHighLevel?" gets no accurate answer today. Needs: GHL added as a supported CRM-category integration in the system prompt (consistent with the homepage marquee addition, Nov 7), accurate current status (app is submitted and **In Review** — not yet publicly listed/installable by the general public, so VINDEX must not claim it's live on the Marketplace yet), and how a GHL client actually gets started (install from inside GoHighLevel, first-open onboarding screen, Company-level install for agency resale). Not started.
9. [ ] **NEW (Nick, Nov 8 2026): full regression sweep of the entire test suite (171 files), in progress.** Started after today's GHL work (PRs #207/#210/#211 merged) to confirm nothing else broke. Protected files confirmed byte-identical to pre-session `main` across the *whole day* (not just per-PR): `git diff 855b2f8..HEAD -- directive_engine.py campaign_detector.py confidence_scorer.py decay_predictor.py health_monitor.py adapters/ billing.py onboarding.py` is empty. `scheduler.py`'s only change all day is the one documented digest-recipient-gate fix (PR #210) — confirmed via diff, nothing else touched it. Sweep itself: running, results pending.

---

## I4. Cross-platform self-serve disconnect (Nick, Nov 7 2026 — new, not started, not GHL-specific)

**Checked, not assumed:** no platform (Salesforce, HubSpot, Meta, Google, LinkedIn, GoHighLevel) requires CDAI itself to provide a disconnect button — every one of them already lets the client revoke access from that platform's own settings regardless of what CDAI offers. `cdai-portal/index.html`'s existing Salesforce "Disconnect" button (`POST /oauth/salesforce/disconnect`, Oct 7 2026) was a convenience add-on, not a platform requirement.

**The real issue: consistency.** A client sees "Reconnect" for Meta/Google/LinkedIn/HubSpot but no "Disconnect" — only Salesforce has one. That's a real, if non-urgent, trust/UX gap worth closing.
- [ ] Build the same self-serve disconnect for HubSpot, Meta, Google, LinkedIn, following the exact Salesforce pattern (`disconnectButtonHtml()` already takes a `platform` param — it's gated to `'salesforce'` only and needs the condition widened, plus one engine endpoint per platform that revokes the token and deletes the stored connection, mirroring `POST /oauth/salesforce/disconnect`).
- [ ] Each platform's own token-revocation call differs (Meta/Google/LinkedIn OAuth revoke endpoints, HubSpot's) — needs its own real design pass per IC8 rule (read the real revoke API for each, test, mutant, independent review), not a copy-paste.
- GoHighLevel needs none of this — see `cdai-engine` handoff §41: disconnect happens by uninstalling inside GoHighLevel itself, already built.

---

## I3. GoHighLevel marketplace listing copy (status as of Nov 7, 2026 — submission day, worked on)

Location: `docs/listing/` in `cdai-engine` (not this repo). **Terms, privacy, and homepage are done and live. The listing itself was submitted to GoHighLevel Nov 7 (In Review) — see I above, item 7.**

- [x] Research done; one draft file written: `01-listing-draft.md` (name, tagline, description, how it works, plans, data/permissions, FAQ).
- [x] **Terms draft (04) and privacy draft (05): done, Nov 7 2026.** GHL-specific clauses added to the live Terms of Service (section 9.2) and Privacy Policy (section 9 bullet + section 6 sentence), delivered to Nick as complete files and pasted live. Confirmed done by Nick.
- [x] **Homepage: done, Nov 7 2026.** GoHighLevel added to the "Built for the tools you already use" integrations row (real live favicon, same method as every other logo there). Delivered to Nick, pasted live. Confirmed done by Nick.
- [ ] **Not started:** site copy for the listing (02), pricing-page copy for GHL clients (03), social posts (06).
- [ ] **Lawyer review** of GoHighLevel's developer agreement — not done, flagged as required before anything is submitted. (Terms/privacy wording itself is done; the lawyer review of that wording, and of the developer agreement, is still open.)
- [ ] **E5 Wheels pilot friend's written OK** and free-pilot terms — not obtained.
- [ ] Four open questions for Nick sitting in the listing folder's own README, unanswered: (1) how "one campaign" is enforced for the free audit, (2) uninstall data retention (keep vs delete after N days — affects privacy-policy wording), (3) whether CDAI checks ad spend against a GHL plan's spend band, (4) whether GoHighLevel's listing has specific asset-size/field requirements — not yet read.
- **Remaining copy items (02, 03, 06) are not blocking the submission** that already happened — they're follow-on polish, not required for GoHighLevel's review.

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

- [x] **Nov 7, 2026: GHL Marketplace submission day — real bug found and fixed live, listing submitted, homepage updated.**
  - **Real bug found and fixed:** agency/company-admin sign-in (`_company_connection()` in `cdai_app_sso.py`) required `status='active'` on the agency connection row, but no code path anywhere ever sets that status for a Company-type row (org-linking, the only thing that flips a row to 'active', is keyed exclusively by `location_id` on sub-account rows). Every agency-admin sign-in was refused with `agency_not_installed`, for every company, always — found live via Render logs during Nick's own submission-video recording session (refusal at 18:34:27 UTC right after a fresh install). Root cause: the test suite's `reset()` fixture hardcoded `status='active'` on the fixture Company row instead of going through the real insert path, which actually produces `'pending'` — masking the bug from day one.
  - Fix: `cdai-engine` PR #207, merged by Nick, deployed live (Render `dep-dbnndkvb9u1s73csopkg`, confirmed `live` at 19:08:29 UTC). Verified: `test_cdai_app_sso.py` ALL PASS, `mut_cdai_app_sso.py` 90/90 killed, 5 adjacent suites (tokens/orgs/billing/e2e/base app) zero regressions, protected files confirmed byte-identical to `main`.
  - GHL Marketplace listing submitted: app version 1.0.0, status **In Review**, 2 installs recorded. Test-credentials and other-details review boxes filled (SSO launches from inside GHL, no separate login; read-only scope summary).
  - **Open, needs Nick to confirm:** whether his submitted demo video actually shows a working sign-in — it was recorded before the fix above was deployed, during the exact window the bug was live. If GoHighLevel's own reviewers test agency-level sign-in themselves (not just watch the video), the fix being live now is what matters; the video's correctness is a separate open question.
  - Homepage: GoHighLevel added to the "Built for the tools you already use" integrations row, same real-favicon method already used for every other logo there (no placeholder/generic icon). Updated file delivered to Nick directly; not yet pasted into Elementor.
  - **Left untouched, flagged for Nick's yes/no:** the FAQ "Who is CDAI for?" answer still names only HubSpot/Salesforce as qualifying CRMs. GoHighLevel reads contacts/won deals through the same mechanism, but CLAUDE.md's founder-confirmed qualification rule only lists HubSpot/Salesforce — expanding that public claim needs Nick's explicit say-so, not an inference.
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
