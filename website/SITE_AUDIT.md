# Site audit: alloceraintelligence.com (read-only, Sept 25 2026)

**Source:** Nick's two WordPress exports (Sept 25 2026): 16 pages and 35 posts, 51 URLs in all. Each finding below names the pages it affects and the proof.

**Every fix waits on Nick's yes.** Rebuilt pages (Sept 26):
- `/net-marketing-contribution/`: live, Rank Math 91/100.
- `/scale-hold-cut-pause-framework/`: live with its original slug, Rank Math 89/100. Removes the retired 80% claim (A1), thresholds, confidence ranges, and the "five directives" error.
- `/triple-whale-vs-rockerbox-vs-allocera/`: rebuilt, pending paste. Removes the retired 80% claim (A1) and false competitor claims (e.g. "Triple Whale can't reconcile costs", disproved by Triple Whale's own help center).
- `/calculate-contribution-margin/`: live, Rank Math 90/100. Its rebuild also fixes this page's wrong canonical (A3b) and doubled title (A3), and removes false fee claims, double-counted refunds, exposed thresholds, and unsourced statistics.

---

## A. Proven problems

### A1. The retired "80% measured directive accuracy" claim: 11 pages

**Proof:**
- Engine manual v27/v28, §11.3 (line 2062): *"It was never computed: no script, log, or query in the codebase or its history produces that number."*
- The claim was retired Aug 11 2026.

**What the pages say:** "80% measured directive accuracy · 55 of 56 directives scored."

**Affected pages:**
- `/55-directives-study/` (the whole page is built on it: "44 ÷ 55 × 100 = 80%")
- `/30-day-retest-methodology/`
- `/30-day-retest-methodology-2/`
- `/tag-manager-real-roi/`
- `/allocera-vs-salesforce/`
- `/true-cac/`
- `/triple-whale-vs-rockerbox-vs-allocera/`
- `/scale-hold-cut-pause-framework/`
- `/home-sample/rockerbox-alternative/`
- `/home-sample/northbeam-alternative/`
- `/blog/` (a post excerpt)

**Not affected:** other "80%" figures on the site are unrelated industry numbers:
- PI intake rejection (`/cost-per-signed-case/`, `/true-cac-2/`)
- solar financing share (`/true-cost-closed-install/`)
- HVAC peak CPL premium (`/hvac-seasonal-cost-per-lead/`)

Those cite outside sources, which should be checked separately.

### A2. "Every two weeks" newsletter cadence: 2 pages

**Proof:** Nick confirmed on Sept 25 2026 that no issue has been sent yet.

**Affected pages and wording:**
- `/newsletter-welcome/`: "Every two weeks — the cost layers…"
- `/roas-looks-good-campaigns-lose-money/`: "Published every two weeks."

This line was already removed from the homepage for the same reason.

### A3. Doubled page titles: 47 of 51 pages

**Proof:** each page's pasted HTML carries its own `<title>`, and Rank Math adds a second one.

**Affected:** every page except these 4:
- `/`
- `/home-sample/privacy-policy-and-terms-and-conditions/`
- `/home-sample/terms/`
- `/home-sample/data-deletion-instructions/`

**Fix:** the same one used on the homepage.

### A3b. Canonical tags pointing to the wrong URL: 12 pages (high priority)

**Proof:** each page's pasted `<head>` has a `rel="canonical"` tag naming a different address than the page itself. Rank Math outputs its own correct canonical, so Google receives two conflicting answers.

| Page | Its pasted canonical says |
|---|---|
| `/calculate-contribution-margin/` (the site's top page for search impressions) | `/blog/calculate-contribution-margin` |
| `/55-directives-study/` | `/blog/55-directives-scored-methodology` |
| `/true-cost-closed-install/` | `/blog/true-cost-closed-install-window-door` |
| `/30-day-retest-methodology/` | `/blog/30-day-retest-methodology` |
| `/30-day-retest-methodology-2/` | `/blog/tag-manager-real-roi` |
| `/tag-manager-real-roi/` | `/blog/tag-manager-real-roi` |
| `/reconciling-pace-greensky-service-finance/` | `/blog/reconciling-pace-greensky-service-finance` |
| `/allocera-vs-salesforce/` | `/blog/allocera-vs-salesforce` |
| `/true-cac/` | `/blog/true-cac` |
| `/true-cac-2/` | `/true-cac/` |
| `/home-sample/rockerbox-alternative/` | `/rockerbox-alternative/` |
| `/home-sample/northbeam-alternative/` | `/northbeam-alternative/` |

**Fix:** remove the pasted `<head>`, the same fix as A3.

### A4. Duplicate content and titles

- **`/30-day-retest-methodology-2/` duplicates `/tag-manager-real-roi/`.** Its text is word-for-word identical to that page (exact string match), but it carries the Rank Math title "Directive Accuracy: 30-Day Retest Beats Gut-Feel". So it's a duplicate article under the wrong URL and title.
- **`/30-day-retest-methodology/` and `/30-day-retest-methodology-2/` share a Rank Math title:** "Directive Accuracy: 30-Day Retest Beats Gut-Feel".
- **`/true-cac/` and `/true-cac-2/` look like near-duplicates** (rough comparison; needs a side-by-side read before deciding). Titles: "True Cost Per Lead: Why Your Dashboard Is Lying" and "True CAC: The Complete Reconciliation Guide".

### A5. Missing Rank Math title or description: 3 pages

- `/home-sample/privacy-policy-and-terms-and-conditions/`
- `/home-sample/terms/`
- `/home-sample/data-deletion-instructions/`

### A6. Template paths under `/home-sample/`: 6 pages

- privacy
- terms
- data deletion
- `rockerbox-alternative`
- `northbeam-alternative`
- `contribution-margin-marketing` (the validation report; the homepage and VINDEX link to it)

---

## B. Needs Nick's decision (not an error by itself)

### B1. "7 cost layers" framing: 44 of 51 pages

- Nick decided on Sept 25 2026 that it's dead and should be removed completely.
- `/seven-cost-layers/` is an entire post about it.
- Removing it means rewriting copy on 44 pages, so it needs Nick's plan: page by page, or batch the simple mentions.

### B2. Apex mentioned: 6 pages

Nick's rule is that Apex appears only in the homepage reviews. The pages:
- `/` (the reviews: allowed)
- `/allocera-intelligence-case-study-proof/`
- `/case-study-2-oauth-validation/`
- `/proof/`
- `/home-sample/northbeam-alternative/`
- `/marketing-margin-distortion-index/`

---

## C. Checked and fine

- **"AI" mentions:** `/dashboard/` explicitly says CDAI is *not* AI-powered. The "AI-powered" hit on `/triple-whale-vs-rockerbox-vs-allocera/` describes Triple Whale, not CDAI.
- **Wrong acronym:** none found. Neither "Campaign Directive AI" nor "Capital Distortion" appears anywhere on the site.

---

## D. Not yet checked (next pass, page by page)

- Third-party statistics and their sources (e.g. "LEXGRO 2026").
- Claims on pricing, about, and how-it-works against the engine and the live pricing.
- Internal links that point to URLs not in the export (possible 404s). The 404 log in Rank Math would confirm these.

---

## E. Live baseline (OpenRush, Sept 26 2026)

This is the "before" snapshot, so every rebuilt page can be measured against it.

- **Search index:** the domain ranks for **1 keyword** and gets **0 estimated organic visits a month**. The one ranking page is `/calculate-contribution-margin/`.
- **Live crawl:** 51 URLs found in the sitemap and 13 audited, for an on-page score of 95.7.
- **7 pages are ignored by crawlers as "canonicalized"**, because their pasted canonical points to another URL (confirms A3b):
  - `/true-cac/`
  - `/true-cac-2/`
  - `/55-directives-study/`
  - `/tag-manager-real-roi/`
  - `/allocera-vs-salesforce/`
  - `/true-cost-closed-install/`
  - `/30-day-retest-methodology/`
- **Doubled titles are confirmed live** (A3), e.g. `/about/` at 106 characters and `/cost-per-signed-case/` at 182. 11 of 13 audited pages have titles too long for Google to show in full.
- `/newsletter-welcome/` is noindex. That's correct for a thank-you page, so no change is needed.
- `/home-sample/terms/` has a 25-character meta description (A5).
- `/scale-hold-cut-pause-framework/` ranks for 0 keywords, so moving it to a new URL costs nothing.

## F. Search Console + GA4, measured (connected Sept 26 2026; data Jun 28 to Sep 25)

**Search Console, last 3 months:**
- **Totals:** 4,236 impressions, up from 718 in the previous 3 months (5.9 times as many). 24 clicks, up from 6. Average position 10.9.
- **Top pages by impressions:**

| Page | Impressions | Avg position | Clicks |
|---|---|---|---|
| `/calculate-contribution-margin/` | 1,460 | 10.1 | 1 (rebuilt Sept 26) |
| `/triple-whale-vs-rockerbox-vs-allocera/` | 689 | 10.6 | 2 (still carries the retired 80% claim, A1) |
| `/` | 268 | 2.4 | 10 |
| `/seven-cost-layers/` | 246 | 10.9 | 0 (retired concept, but it earns impressions; rewrite, don't delete) |
| `/home-sample/northbeam-alternative/` | 143 | 28.1 | 1 |
| `/net-marketing-contribution/` | 125 | 6.7 | 0 (rebuilt) |
| `/home-sample/rockerbox-alternative/` | 106 | 11.7 | 1 |
| `/tcpa-compliance-cost-for-law-firms/` | 99 | 25.5 | 0 |
| `/blog/` | 95 | 16.4 | 0 |

- **Scale-hold-cut-pause page:** 42 impressions and 1 click. The only queries reported for it are brand searches.

**GA4, last 3 months:**
- 365 sessions and 239 users, down 33% from the previous period.
- **By channel:**
  - Direct: 279 sessions, 12.5s average engagement
  - Organic search: 39 sessions, 46.1s average engagement (the best of any channel)
  - Organic social: 31
  - Referral: 9
  - AI assistants: 3
