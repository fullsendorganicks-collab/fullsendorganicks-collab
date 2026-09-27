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
| **Post 252** | `/30-day-retest-methodology-2/` → change to `/30-day-retest-methodology/` (fix-list A1) | Marketing Measurement: Grading 8 Decisions Against Profit | `/30-day-retest-methodology-2/` | R11 (+ R12 check) | 82 (re-check after the restore) |
| **Post 245** | `/lead-quality/` | Lead Quality: 6 Metrics to Measure It in Real Dollars | held `/30-day-retest-methodology/` until Sept 28 | none into it; R12 must not exist | 88 (featured image not set yet) |
| Marketing costs | `/marketing-costs/` | Marketing Costs: What $10,000 in Ad Spend Really Costs You | `/seven-cost-layers/`, `/blog/seven-cost-layers` | R1, R2 | 89 |
| ROAS calculator | `/roas-calculator/` | ROAS Calculator: Find Your Break-Even ROAS and Real Profit | `/55-directives-study/` | R3 | 90 |
| Offline conversion tracking | `/tag-manager-real-roi/` | Offline Conversion Tracking: Connect Ad Clicks to Closed Revenue | — (slug kept) | — | 80 |
| Salesforce campaign influence | `/salesforce-campaign-influence/` | Salesforce Campaign Influence: What It Shows, and the Profit It Misses | `/allocera-vs-salesforce/` | R7 | 89 |
| Customer acquisition cost formula | `/true-cac/` | Customer Acquisition Cost Formula: How to Calculate Your True CAC | `/true-cac-2/` (trashed) | R8 | 81 |
| Average cost per lead | `/average-cost-per-lead/` | Average Cost Per Lead by Industry, and What a Customer Really Costs | `/marketing-margin-distortion-index/` | R10 | 83 |

**Redirects Nick still has to add or confirm (the full list is in section 1, R1–R22):**
- **Confirm they're in:** R1, R3, R8
- **Check once:** R4
- **Add now:**
  - R7, R10, R13, R14, R15, R16
  - R17 (regex; it covers R2), with R21 above it
  - R18, R19, R20, R22
- **Add right after fix-list A1:** R11

Plus R12: check it does **not** exist.

**Internal links:** every rebuilt page links to live final URLs, except the blog file, which is re-pasted at the end. It needs:
- new cards for Lead Quality and Average Cost Per Lead
- URLs updated for every changed slug

## 1. Slug changes and the redirects they need

In WordPress: **Rank Math → Redirections → Add New**, then type **301 Permanent Move**.

| # | Old URL (Source) | New URL (Destination) | Why | Status |
|---|---|---|---|---|
| R1 | `seven-cost-layers` | `https://alloceraintelligence.com/marketing-costs/` | Slug changed Sept 27 (score 89) | **Nick: confirm it's added** (instructions sent Sept 27) |
| R2 | `blog/seven-cost-layers` | `https://alloceraintelligence.com/marketing-costs/` | 5 old posts link to this wrong path, which was already broken before the change; this rescues them | **Covered by R17** (add R2 only if you don't use the regex) |
| R3 | `55-directives-study` | `https://alloceraintelligence.com/roas-calculator/` | Slug changed Sept 27 (score 90) | **Nick: confirm it's added** |
| R5 | `30-day-retest-methodology-2` | — | **Cancelled (Nick, Sept 28): never delete a page.** Superseded: see R11 and R12. | Not needed |
| R6 | `tag-manager-real-roi` | — | Slug kept (Nick, Sept 27) | Not needed |
| R7 | `allocera-vs-salesforce` | `https://alloceraintelligence.com/salesforce-campaign-influence/` | Slug changed Sept 27 (score 89) | **To add** |
| R8 | `true-cac-2` | `https://alloceraintelligence.com/true-cac/` | Duplicate merged; Nick kept it trashed | **Nick adding it now (Sept 28)** |
| R9 | `true-cac` | — | Slug kept (Nick, Sept 28) | Not needed |
| R10 | `marketing-margin-distortion-index` | `https://alloceraintelligence.com/average-cost-per-lead/` | Slug changed Sept 28 (score 83) | **To add** |
| R11 | `30-day-retest-methodology-2` | `https://alloceraintelligence.com/30-day-retest-methodology/` | Sept 27 export: the 30-Day Retest IS live in post 252 (score 82). Only its slug still needs to change from `-2` (fix-list A1). | **To add, right after the A1 slug change** |
| R12 | `30-day-retest-methodology` | — | **Must NOT exist.** If Rank Math auto-created a redirect from this to `/lead-quality/` when post 245's slug changed, delete it, or the restored retest post can't be reached. | **Nick: check and delete if present** |
| R13 | `home-sample/allocera-intelligence-case-study-proof` | `https://alloceraintelligence.com/allocera-intelligence-case-study-proof/` | Link scan Sept 27: **21 live posts** link to this old path; the page now lives at the root | **To add** |
| R14 | `home-sample/blog` | `https://alloceraintelligence.com/blog/` | 6 live pages link here (pricing, how it works, proof, dashboard, about, financing fees) | **To add** |
| R15 | `home-sample/case-study-2-oauth-validation` | `https://alloceraintelligence.com/case-study-2-oauth-validation/` | Linked from the proof and case study pages | **To add** |
| R16 | `northbeam-alternative` | `https://alloceraintelligence.com/home-sample/northbeam-alternative/` | The old Northbeam page links to itself at the wrong path | **To add** |
| R17 | `blog/(.+)` (Rank Math: set match type to **Regex**) | `https://alloceraintelligence.com/$1/` | Posts 233 and 277 link to `/blog/<slug>` paths that don't exist. One regex covers all 9, and replaces R2. | **To add** |
| R18 | `contribution-margin` | `https://alloceraintelligence.com/calculate-contribution-margin/` | Linked from posts 549 and 556; no such page | **To add** |
| R19 | `salesforce-marketing-cloud` | `https://alloceraintelligence.com/salesforce-campaign-influence/` | Linked from post 588; no such page | **To add** |
| R20 | `scale-hold-cut-pause` | `https://alloceraintelligence.com/scale-hold-cut-pause-framework/` | Linked from post 588; no such page | **To add** |
| R21 | `blog/true-cost-closed-install-window-door` | `https://alloceraintelligence.com/true-cost-closed-install/` | Linked from post 233 (an old slug); add this **above** R17 | **To add** |
| R22 | `about-us` | `https://alloceraintelligence.com/about/` | GA4 shows visits landing on this missing URL | **To add** |
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

## 2. Internal links pointing at missing URLs (live-site scan of the Sept 27 export)

Every `href` on all 50 live posts and pages was checked against the live URLs.

| Missing URL | Linked from (post IDs) | Covered by |
|---|---|---|
| `/30-day-retest-methodology/` | 228, 245, 260, 284, 294, 301, 850, 730, 772 | Fix-list A1 (slug change on 252) |
| `/seven-cost-layers/` | 850, 315, 490, 530, 549, 556, 576, 588, 654, 739, 746, 765 | R1 |
| `/true-cac-2/` | 576, 588, 703, 715, 722, 730, 746, 758, 765 | R8 |
| `/marketing-margin-distortion-index/` | 187 (blog), 524, 530, 588, 703, 715 | R10 |
| `/allocera-vs-salesforce/` | 187 (blog) | R7 |
| `/55-directives-study/` | 654 | R3 |
| `/home-sample/allocera-intelligence-case-study-proof/` | 21 posts (233 … 793), 342, 457 | R13 |
| `/home-sample/blog/` | 315, 437, 451, 457, 478, 483 | R14 |
| `/home-sample/case-study-2-oauth-validation/` | 133, 457 | R15 |
| `/northbeam-alternative/` | 654 | R16 (and fix-list A2) |
| `/blog/<slug>` (9 paths) | 233, 277 | R17 + R21 |
| `/contribution-margin/` | 549, 556 | R18 |
| `/salesforce-marketing-cloud/`, `/scale-hold-cut-pause/` | 588 | R19, R20 |

**Rebuilt pages link only to final URLs.** The only exceptions are the blog (re-pasted at the end) and the validation report (fix-list B7). Each older post's links get corrected in its own rebuild, and the redirects cover them until then.

**What the scan can't see:** WordPress menus, theme header/footer widgets, and links from other sites. The redirects cover those.

## 3. Final pass (at the end, with the blog)

1. Every row in section 1 is marked done and passes the quick test.
2. Re-run the link scan on every page file (one command) and confirm 0 links to any old slug.
3. The blog paste uses only final URLs (pending list in `FIX_LIST.md`).
