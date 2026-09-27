# Redirects and link register

One place for every slug change, every redirect, and every internal link that points at an old URL. Update it each time a slug changes. Check it before the final blog paste.

**How links were checked (Sept 27):**
1. Every rebuilt page file in `website/pages/` and the homepage were searched for the old slugs.
2. The WordPress export of all 51 live pages (Sept 26) was searched for every `href` to an old slug.
3. Search Console (last 28 days) was checked for old URLs Google still shows.

## 0. Master table: every rebuilt page, its live URL, title, and redirect (updated Sept 28)

| Post/page | Live URL now | WordPress title / H1 | Old URL | Redirect | Score |
|---|---|---|---|---|---|
| Homepage | `/` | (homepage) | — | — | 81 |
| Blog | `/blog/` | Marketing ROI Blog | — | — | 72 (re-paste at the end) |
| Net marketing contribution | `/net-marketing-contribution/` | Net Marketing Contribution | — | — | done |
| Contribution margin | `/calculate-contribution-margin/` | Calculate Contribution Margin | `/calculate-marketing-contribution-margin/` (old) | R4 (check) | done |
| Scale/hold/cut/pause | `/scale-hold-cut-pause-framework/` | Scale, Hold, Cut, Pause | — | — | 89 |
| Triple Whale vs Rockerbox | `/triple-whale-vs-rockerbox-vs-allocera/` | Triple Whale vs Rockerbox | — | — | done |
| Northbeam alternative | `/home-sample/northbeam-alternative/` | Northbeam Alternative | — | — | done |
| Rockerbox alternative | `/home-sample/rockerbox-alternative/` | Rockerbox Alternative | — | — | done |
| Cost per signed case | `/cost-per-signed-case/` | Cost Per Signed Case | — | — | 90 |
| **Post 252** | `/30-day-retest-methodology/` **after the restore** (now `-2`) | Marketing Measurement That Grades Its Own Decisions: The 30-Day Retest | `/30-day-retest-methodology-2/` | R11 (+ R12 check) | 82 (re-check after the restore) |
| **Post 245** | `/lead-quality/` | Lead Quality: How to Measure It by What Each Lead Is Worth | held `/30-day-retest-methodology/` until Sept 28 | none into it; R12 must not exist | 83 |
| Marketing costs | `/marketing-costs/` | Marketing Costs: What $10,000 in Ad Spend Really Costs You | `/seven-cost-layers/`, `/blog/seven-cost-layers` | R1, R2 | 89 |
| ROAS calculator | `/roas-calculator/` | ROAS Calculator: Find Your Break-Even ROAS and Real Profit | `/55-directives-study/` | R3 | 90 |
| Offline conversion tracking | `/tag-manager-real-roi/` | Offline Conversion Tracking: Connect Ad Clicks to Closed Revenue | — (slug kept) | — | 80 |
| Salesforce campaign influence | `/salesforce-campaign-influence/` | Salesforce Campaign Influence: What It Shows, and the Profit It Misses | `/allocera-vs-salesforce/` | R7 | 89 |
| Customer acquisition cost formula | `/true-cac/` | Customer Acquisition Cost Formula: How to Calculate Your True CAC | `/true-cac-2/` (trashed) | R8 | 81 |
| Average cost per lead | `/average-cost-per-lead/` | Average Cost Per Lead by Industry, and What a Customer Really Costs | `/marketing-margin-distortion-index/` | R10 | 83 |

**Redirects Nick still has to add or confirm (8):**
- R1: confirm
- R2: add
- R3: confirm
- R4: check
- R7: add
- R8: confirm
- R10: add
- R11: add after the restore

Plus R12: check it does **not** exist.

**Internal links:** every rebuilt page links to live final URLs, except the blog file, which is re-pasted at the end. It needs:
- new cards for Lead Quality and Average Cost Per Lead
- URLs updated for every changed slug

## 1. Slug changes and the redirects they need

In WordPress: **Rank Math → Redirections → Add New**, then type **301 Permanent Move**.

| # | Old URL (Source) | New URL (Destination) | Why | Status |
|---|---|---|---|---|
| R1 | `seven-cost-layers` | `https://alloceraintelligence.com/marketing-costs/` | Slug changed Sept 27 (score 89) | **Nick: confirm it's added** (instructions sent Sept 27) |
| R2 | `blog/seven-cost-layers` | `https://alloceraintelligence.com/marketing-costs/` | 5 old posts link to this wrong path, which was already broken before the change; this rescues them | **To add** |
| R3 | `55-directives-study` | `https://alloceraintelligence.com/roas-calculator/` | Slug changed Sept 27 (score 90) | **Nick: confirm it's added** |
| R5 | `30-day-retest-methodology-2` | — | **Cancelled (Nick, Sept 28): never delete a page.** Superseded: see R11 and R12. | Not needed |
| R6 | `tag-manager-real-roi` | — | Slug kept (Nick, Sept 27) | Not needed |
| R7 | `allocera-vs-salesforce` | `https://alloceraintelligence.com/salesforce-campaign-influence/` | Slug changed Sept 27 (score 89) | **To add** |
| R8 | `true-cac-2` | `https://alloceraintelligence.com/true-cac/` | Duplicate merged; Nick kept it trashed | **Nick adding it now (Sept 28)** |
| R9 | `true-cac` | — | Slug kept (Nick, Sept 28) | Not needed |
| R10 | `marketing-margin-distortion-index` | `https://alloceraintelligence.com/average-cost-per-lead/` | Slug changed Sept 28 (score 83) | **To add** |
| R11 | `30-day-retest-methodology-2` | `https://alloceraintelligence.com/30-day-retest-methodology/` | Sept 28: the 30-day retest post moves into post 252 and takes back its original slug, so the -2 URL goes away | **To add, after the restore** (steps in `pages/30-day-retest-methodology-RANKMATH.md`) |
| R12 | `30-day-retest-methodology` | — | **Must NOT exist.** If Rank Math auto-created a redirect from this to `/lead-quality/` when post 245's slug changed, delete it, or the restored retest post can't be reached. | **Nick: check and delete if present** |
| R4 | `calculate-marketing-contribution-margin` | `https://alloceraintelligence.com/calculate-contribution-margin/` | Google still shows this old URL (1 impression, last 28 days). It isn't in the page list, so it's an old slug. | **Nick: open it once.** If it already lands on `/calculate-contribution-margin/`, mark done; if it shows a 404, add it. |

**Planned (from the fix list, not done yet):**

| # | Old URL | New URL | When |
|---|---|---|---|
| P3 | any future slug change | its new URL | Add a row the same day |

**Not changed, no redirect needed:** `/scale-hold-cut-pause-framework/` still has its original slug (Search Console still shows it; `marketing-budget-allocation` never went live), and every other rebuilt page kept its slug.

**Quick test after adding the redirects** (takes one minute). Open each in a private window; each should land on the new page:
- `alloceraintelligence.com/seven-cost-layers/` → Marketing Costs
- `alloceraintelligence.com/blog/seven-cost-layers` → Marketing Costs
- `alloceraintelligence.com/55-directives-study/` → ROAS Calculator
- `alloceraintelligence.com/allocera-vs-salesforce/` → Salesforce Campaign Influence
- `alloceraintelligence.com/true-cac-2/` → Customer Acquisition Cost Formula
- `alloceraintelligence.com/marketing-margin-distortion-index/` → Average Cost Per Lead
- `alloceraintelligence.com/30-day-retest-methodology/` → **Marketing Measurement / 30-Day Retest** (not Lead Quality)
- `alloceraintelligence.com/30-day-retest-methodology-2/` → Marketing Measurement / 30-Day Retest
- `alloceraintelligence.com/lead-quality/` → Lead Quality

## 2. Internal links pointing at old URLs

**Rebuilt pages: 0 links to any old slug.** That covers the homepage, blog file, net marketing contribution, contribution margin, scale/hold/cut/pause, Triple Whale vs Rockerbox, Northbeam, Rockerbox, cost per signed case, 30-day retest, marketing costs and ROAS calculator. The blog file already uses `/marketing-costs/`.

**Older pages that still link to `/seven-cost-layers/` (or the broken `/blog/seven-cost-layers`).** With R1 and R2 in place, every one of these links works. When each page gets its rebuild or light clean, the link is changed to point straight at `/marketing-costs/` (and its "seven cost layers" wording goes).

| Page | Links to | Fixed when |
|---|---|---|
| `/home-sample/contribution-margin-marketing/` (validation report) | `/seven-cost-layers/` | Fix list #13 (quick fix) |
| `/true-cost-closed-install/` | `/blog/seven-cost-layers` | #19 |
| `/reconciling-pace-greensky-service-finance/` | `/blog/seven-cost-layers` | #20 |
| `/allocera-vs-salesforce/` | `/blog/seven-cost-layers` | #5 |
| `/true-cac/` | `/blog/seven-cost-layers` | #6 |
| `/true-cac-2/` | `/seven-cost-layers/` | #6 (gets a 301) |
| `/financing-fees-home-services/` | `/seven-cost-layers/` | #21 |
| `/true-cost-per-move-in/` | `/seven-cost-layers/` | #23 |
| `/marketing-margin-distortion-index/` | `/seven-cost-layers/` | #7 |
| `/roas-looks-good-campaigns-lose-money/` | `/seven-cost-layers/` | #17 |
| `/cost-per-admission-addiction-treatment/` | `/seven-cost-layers/` | #24 |
| `/cost-per-enrolled-member-medicare-advantage/` | `/seven-cost-layers/` | #25 |
| `/chargebacks-marketing-cost/` | `/seven-cost-layers/` | #26 |
| `/true-marketing-roi/` | `/seven-cost-layers/` | #22 |
| `/tcpa-compliance-cost-for-law-firms/` | `/seven-cost-layers/` | #18 |
| `/cost-per-booked-job-hvac-plumbing/` | `/seven-cost-layers/` | #32 |
| `/angi-homeadvisor-lead-cost/` | `/seven-cost-layers/` | #37 |

**`/allocera-vs-salesforce/`:** after R7 these links work. Two places still link to it: the blog page (card updated at the end) and `/true-cost-closed-install/` (fixed in its light clean, #19). No rebuilt page links to it.

**`/55-directives-study/`:** no live page links to it any more. The only links were on the old versions of the blog, Northbeam, Rockerbox and scale/hold/cut/pause pages, all since replaced.

**What the scan can't see:**
- WordPress menus (Appearance → Menus)
- theme header/footer widgets
- links from outside the site

The redirects cover all of these. If a menu item points at an old URL, change it in the menu.

## 3. Final pass (at the end, with the blog)

1. Every row in section 1 is marked done and passes the quick test.
2. Re-run the link scan on every page file (one command) and confirm 0 links to any old slug.
3. The blog paste uses only final URLs (pending list in `FIX_LIST.md`).
