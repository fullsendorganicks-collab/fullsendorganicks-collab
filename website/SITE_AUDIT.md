# Site audit: alloceraintelligence.com (read-only, Sept 25 2026)

**Source:** Nick's two WordPress exports (Sept 25 2026): 16 pages and 35 posts, 51 URLs in all. Each finding below names the pages it affects and the proof.

**Nothing has been changed on the site.** Every fix waits on Nick's yes.

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
