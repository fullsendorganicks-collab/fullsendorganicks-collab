# Redirects and link register

One place for every slug change, every redirect, and every internal link that points at an old URL. Update it each time a slug changes. Check it before the final blog paste.

**How links were checked (Sept 27):**
1. Every rebuilt page file in `website/pages/` and the homepage were searched for the old slugs.
2. The WordPress export of all 51 live pages (Sept 26) was searched for every `href` to an old slug.
3. Search Console (last 28 days) was checked for old URLs Google still shows.

## 1. Slug changes and the redirects they need

In WordPress: **Rank Math → Redirections → Add New**, then type **301 Permanent Move**.

| # | Old URL (Source) | New URL (Destination) | Why | Status |
|---|---|---|---|---|
| R1 | `seven-cost-layers` | `https://alloceraintelligence.com/marketing-costs/` | Slug changed Sept 27 (score 89) | **Nick: confirm it's added** (instructions sent Sept 27) |
| R2 | `blog/seven-cost-layers` | `https://alloceraintelligence.com/marketing-costs/` | 5 old posts link to this wrong path, which was already broken before the change; this rescues them | **To add** |
| R3 | `55-directives-study` | `https://alloceraintelligence.com/roas-calculator/` | Slug changed Sept 27 (score 90) | **Nick: confirm it's added** |
| R5 | `30-day-retest-methodology-2` | the offline conversion tracking post's final URL (`/tag-manager-real-roi/`, or `/offline-conversion-tracking/` if the slug changes) | Exact duplicate of the old tag manager post with the fake 80% | **To add** when the new post is pasted; then trash the duplicate |
| R6 | `tag-manager-real-roi` | `https://alloceraintelligence.com/offline-conversion-tracking/` | Only if Nick changes the slug | Pending Nick's slug decision |
| R4 | `calculate-marketing-contribution-margin` | `https://alloceraintelligence.com/calculate-contribution-margin/` | Google still shows this old URL (1 impression, last 28 days). It isn't in the page list, so it's an old slug. | **Nick: open it once.** If it already lands on `/calculate-contribution-margin/`, mark done; if it shows a 404, add it. |

**Planned (from the fix list, not done yet):**

| # | Old URL | New URL | When |
|---|---|---|---|
| P2 | `true-cac-2` | `/true-cac/` | With the true CAC merge |
| P3 | any future slug change | its new URL | Add a row the same day |

**Not changed, no redirect needed:** `/scale-hold-cut-pause-framework/` still has its original slug (Search Console still shows it; `marketing-budget-allocation` never went live), and every other rebuilt page kept its slug.

**Quick test after adding the redirects** (takes one minute). Open each in a private window; each should land on the new page:
- `alloceraintelligence.com/seven-cost-layers/` → Marketing Costs
- `alloceraintelligence.com/blog/seven-cost-layers` → Marketing Costs
- `alloceraintelligence.com/55-directives-study/` → ROAS Calculator
- `alloceraintelligence.com/30-day-retest-methodology-2/` → Offline Conversion Tracking (after R5)

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
