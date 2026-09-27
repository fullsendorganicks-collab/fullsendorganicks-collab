# Website master to-do (rebuilt Sept 28 from the Sept 27 WordPress exports)

**Nick's rules:**
- **Never delete or retire a page.** Rebuild it so it adds reach, authority and trust.
- **The blog page is last.** Redirects and link fixes are done at the end.
- **Apex was a real pilot.** Keep it where it's true; the Sid and Rebecca homepage reviews stay.
- **Nothing sensitive or proprietary.**
- **Every page gets:**
  - live data (Search Console, GA4, keyword research, live Google results)
  - a Rank Math box shown in chat
  - GA4 tracking, an image, and a claims table
- **Never:** the fake 80%, "cost layers", "never assumes costs".

**Paste rule (Sept 28):** every page is sent with:
1. the exact edit link by post ID
2. the WordPress title you'll see
3. the slug you should see

Check all three before deleting anything.

**Where this list comes from:**
- **Sept 27 exports:** all 51 posts and pages, checked by post ID for which of my built pages is actually live in each one
- **Search Console and GA4:** the last 3 months (4,267 impressions, 23 clicks, 346 visits)
- **A scan of every internal link on the live site**

Redirect details are in `REDIRECTS.md`.

## Scoreboard
- **Done and live:** 17
  - 15 rebuilt posts/pages
  - the homepage
  - the blog (which gets a final re-paste)
- **Built but NOT live:** 1 (Northbeam)
- **Not touched yet:** 33
  - 12 pages
  - 21 older posts

## A. Fixes on pages already done (Nick, in WordPress; about 15 minutes, no new building)
| # | Post ID / edit link | What's wrong (from the Sept 27 export) | Fix |
|---|---|---|---|
| A1 | **252** `post.php?post=252&action=edit` | The 30-Day Retest IS live here (score 82), but the slug is still `30-day-retest-methodology-2`. 7 pages link to `/30-day-retest-methodology/`. | Change the slug to `30-day-retest-methodology`. First check that Rank Math → Redirections has no redirect named `30-day-retest-methodology` (R12). Then add R11. |
| A2 | **654** `post.php?post=654&action=edit` (page, `/home-sample/northbeam-alternative/`) | My rebuild (`pages/northbeam-alternative.html`) was never pasted. The old page with the fake 80% and "cost layers" is live (142 impressions, position 27.9, score 74). | Paste the existing file plus its Rank Math box. No new build. |
| A3 | Featured image missing | 245 lead quality, 260 offline conversion, 267 contribution margin, 501 signed case, 506 avg cost per lead, 563 net marketing contribution, 850 validation report | Set each post's own image (the file names are in each RANKMATH box). |
| A4 | **284** | The WordPress title is still the old "Salesforce Marketing Cloud: The Margin Reconciliation Gap" | Change it to `Salesforce Campaign Influence: 4 Things Campaign ROI Misses` |

## B. Pages not touched yet (12), in build order
| Order | Post ID | Slug you'll see | WordPress title you'll see | Search (3 mo) | Job |
|---|---|---|---|---|---|
| B1 | 451 | `how-it-works` | How to Calculate True Cost Per Lead — CDAI Engine | 28 impr | Full rebuild (has "cost layers") |
| B2 | 483 | `about` | About CDAI Engine — Allocera Intelligence / Nick Baum | 46 impr, 2 clicks | Full rebuild (has "cost layers") |
| B3 | 478 | `dashboard` | Campaign Analytics Dashboard — CDAI Engine | 35 impr, 1 click | Rebuild (has "cost layers") |
| B4 | 457 | `proof` | Paid Advertising Case Study — CDAI Engine | 16 impr | Full rebuild: validation first, provable Apex pilot story |
| B5 | 133 | `allocera-intelligence-case-study-proof` | Allocera Intelligence - Case Study - Proof | 23 impr | Full rebuild (has "cost layers"); its own purpose |
| B6 | 342 | `case-study-2-oauth-validation` | CDAI Engine OAuth validation | 12 impr | Full rebuild; its own purpose |
| B7 | 850 | `contribution-margin-marketing` (validation report) | Contribution Margin Marketing: What It Means… | — | Quick fix: remove "cost layers", fix the `/seven-cost-layers/` link |
| B8 | 162 | `terms` | Terms | — | Quick fix (one "cost layers" mention) |
| B9 | 524 | `newsletter-welcome` | Newsletter Welcome | — | Quick fix ("every two weeks", "cost layers", old link) |
| B10 | 155 | `privacy-policy-and-terms-and-conditions` | Privacy Policy | — | Check only |
| B11 | 173 | `data-deletion-instructions` | Data Deletion Instructions | — | Check only |
| B12 | 437 | `pricing` | Paid Ads Audit Cost — CDAI Engine | 52 impr | **ON HOLD (Nick)** |

## C. Older posts not touched yet (21), in order of search impressions
All 21 still have "cost layers" wording, and most link to old URLs (`/seven-cost-layers/`, `/true-cac-2/`, `/home-sample/…`). Each one gets rebuilt with its own keyword, checked against the pages already live so two pages don't compete for one keyword.

| Order | Post ID | Slug you'll see | WordPress title you'll see | Search (3 mo) |
|---|---|---|---|---|
| C1 | 739 | `tcpa-compliance-cost-for-law-firms` | TCPA Compliance Cost for Law Firms Buying Leads | 100 impr, pos 25 |
| C2 | 490 | `true-cost-per-move-in` | True Cost Per Move-In: Senior Living Margin Reconciliation | 71 impr, 1 click |
| C3 | 786 | `hvac-customer-lifetime-value` | HVAC Customer Lifetime Value: Why Membership Plans Change the Math | 61 impr, pos 5.7 |
| C4 | 277 | `reconciling-pace-greensky-service-finance` | Merchant Fees: GreenSky, PACE, Service Finance Guide | 54 impr |
| C5 | 765 | `angi-homeadvisor-lead-cost` | Angi HomeAdvisor Lead Cost: The Real Cost Per Booked Job | 43 impr |
| C6 | 549 | `cost-per-admission-addiction-treatment` | True Cost Per Admission: Addiction Treatment | 35 impr |
| C7 | 746 | `cost-per-booked-job-hvac-plumbing` | True Cost Per Booked Job for HVAC and Plumbing Contractors | 34 impr |
| C8 | 315 | `financing-fees-home-services` | Financing Fees: How They Quietly Eat Home Services Margin | 33 impr |
| C9 | 779 | `hvac-marketing-channel-mix` | HVAC Marketing Channel Mix: What the Right Spend Split Looks Like | 16 impr |
| C10 | 715 | `personal-injury-case-type-cac` | Personal Injury Case Type CAC: Why One Threshold Fails | 14 impr, 1 click |
| C11 | 703 | `personal-injury-ad-spend-attribution` | Personal Injury Ad Spend Attribution: Why Blended CPL Hides Winners | 13 impr |
| C12 | 233 | `true-cost-closed-install` | true-cost-closed-install | 12 impr |
| C13 | 588 | `true-marketing-roi` | True Marketing ROI: Why These Platforms Get It Wrong | 12 impr |
| C14 | 576 | `chargebacks-marketing-cost` | How Chargebacks Inflate True Marketing Cost | 10 impr |
| C15 | 758 | `mass-tort-lead-aggregator-economics` | Mass Tort Lead Aggregator Economics: Why Blended CPL Hides Cost | 10 impr |
| C16 | 772 | `hvac-seasonal-cost-per-lead` | HVAC Seasonal Cost Per Lead: Why Flat Budgets Waste Money | 10 impr (has the fake 80%) |
| C17 | 556 | `cost-per-enrolled-member-medicare-advantage` | True Cost Per Enrolled Member: Medicare Advantage | 9 impr |
| C18 | 722 | `multi-state-pi-firm-attribution` | Multi-State PI Firm Attribution: Why One Blended CAC Fails | 7 impr |
| C19 | 730 | `personal-injury-settlement-lag` | Personal Injury Settlement Lag: Why 30-Day CAC Dashboards Fail | 5 impr |
| C20 | 793 | `hvac-customer-acquisition-cost` | True HVAC Customer Acquisition Cost: Why It Runs 3x CPL | 3 impr |
| C21 | 530 | `roas-looks-good-campaigns-lose-money` | Why ROAS Looks Good But Campaigns Lose Money | 2 impr |

## D. End of rebuild (after B and C)
1. **Redirects:** add every row in `REDIRECTS.md` (R1–R20).
2. **Link check:** re-run the live-link scan on a fresh export. It must find 0 links to missing URLs.
3. **Blog page:** re-paste with final URLs (pending list below).
4. **Optional:** GA4 tracking on the 8 early pages.

## Done and live (from the Sept 27 export, by post ID)
| Post ID | Live URL | Rank Math score | Featured image |
|---|---|---|---|
| 9 | `/` (homepage) | 81 | yes |
| 187 | `/blog/` | 72 | — (final re-paste) |
| 563 | `/net-marketing-contribution/` | 91 | **missing** |
| 267 | `/calculate-contribution-margin/` | 91 | **missing** |
| 322 | `/scale-hold-cut-pause-framework/` (Marketing Budget Allocation) | 89 | yes |
| 308 | `/triple-whale-vs-rockerbox-vs-allocera/` | 90 | yes |
| 646 | `/home-sample/rockerbox-alternative/` | 90 | yes |
| 501 | `/cost-per-signed-case/` | 90 | **missing** |
| 252 | `/30-day-retest-methodology-2/` → slug fix A1 | 82 | yes |
| 301 | `/marketing-costs/` | 89 | yes |
| 228 | `/roas-calculator/` | 90 | yes |
| 260 | `/tag-manager-real-roi/` (Offline Conversion Tracking) | 80 | **missing** |
| 284 | `/salesforce-campaign-influence/` | 89 | yes (WP title fix A4) |
| 294 | `/true-cac/` (Customer Acquisition Cost Formula) | 81 | yes |
| 506 | `/average-cost-per-lead/` | 83 | **missing** |
| 245 | `/lead-quality/` | 88 | **missing** |
| 543 | `/true-cac-2/` | trashed (merged into 294) | — |

## Blog page: pending changes (ON HOLD until the rebuild is done, per Nick)
`pages/blog.html` already has the first two. Paste only when Nick says the rebuild is finished.
- [x] Add card: Marketing Costs → `/marketing-costs/`
- [x] Add card: 30-Day Retest → `/30-day-retest-methodology/`
- [ ] Add card: ROAS Calculator → `/roas-calculator/`
- [ ] Update card: Tag Manager → Offline Conversion Tracking → `/tag-manager-real-roi/` (slug kept)
- [ ] Update card: Allocera and Salesforce → Salesforce Campaign Influence → `/salesforce-campaign-influence/`
- [ ] Update card: True CAC → Customer Acquisition Cost Formula (final URL); remove any `/true-cac-2/` card
- [ ] Update card: Margin Distortion Index → Average Cost Per Lead by Industry → `/average-cost-per-lead/`
- [ ] Add a card for `/lead-quality/`; remove cards for pages that get 301'd (e.g. `/30-day-retest-methodology-2/`, `/true-cac-2/`) and update titles/descriptions for every rebuilt page
- [ ] Re-check every card link against the live URLs before handing over
- [ ] Remove the `/allocera-vs-salesforce/` and `/marketing-margin-distortion-index/` links the live blog still has (link scan, Sept 27)

---

# Archive: the old tier list (superseded Sept 28 by sections A–D above)

## Tier 1: false claims (fix first)
| # | Page | Problems | Fix |
|---|---|---|---|
| 1 | `/30-day-retest-methodology/` | 80%, "55 of 56", seven layers, $2,500 guarantee, wrong `/blog/` links, pasted head | **LIVE Sept 27, score 82.** |
| 2 | `/55-directives-study/` | The whole page is the fake 80% | **LIVE Sept 27, score 90**, now at `/roas-calculator/` (brand-new ROAS calculator). 301 = R3 in `REDIRECTS.md`. |
| 3 | `/30-day-retest-methodology-2/` | Exact copy of the tag-manager page, and says 80% | **DONE Sept 28:** "Lead Quality" is LIVE at `/lead-quality/` (83), pasted into post 245. Post 252 now takes the 30-day retest post back to `/30-day-retest-methodology/` (R11, R12). Files: `website/pages/lead-quality*`. |
| 4 | `/tag-manager-real-roi/` | 80%, seven layers, 14 unsourced stats, pasted head | **LIVE Sept 27, score 80**, slug kept. New post "Offline Conversion Tracking". |
| 5 | `/allocera-vs-salesforce/` | 80%, seven layers, "cannot" claims about Salesforce, pasted head | **LIVE Sept 27, score 89**, now at `/salesforce-campaign-influence/`. 301 = R7. |
| 6 | `/true-cac/` + `/true-cac-2/` | 80%, seven layers, duplicate pair | **LIVE Sept 28, score 81**, slug kept. `-2` trashed; 301 = R8. |
| 7 | `/marketing-margin-distortion-index/` | 80%, Apex numbers, "2026" in the title, many unsourced stats | **LIVE Sept 28, score 83**, now at `/average-cost-per-lead/`. 301 = R10. |
| 8 | `/proof/`, `/allocera-intelligence-case-study-proof/`, `/case-study-2-oauth-validation/` | Apex story with unprovable numbers | **Full rebuilds (Nick: never retire; Apex was a real pilot).** Keep the pilot story where it's provable, lead with the validation, one clear purpose per page. |

## Tier 2: pages people use to decide
| # | Page | Problems | Fix |
|---|---|---|---|
| 9 | `/pricing/` | Seven layers, "30-day retest", credit wording mismatch | **ON HOLD** (free audit) |
| 10 | `/how-it-works/` | Seven layers, old CTA | Full rebuild |
| 11 | `/about/` | Seven layers, old CTA | Full rebuild |
| 12 | `/dashboard/` | Seven layers, old CTA | Light clean |
| 13 | `/home-sample/contribution-margin-marketing/` (validation report) | Still mentions "cost layers" | **Quick fix:** a few sentences |
| 14 | `/home-sample/terms/` | One "cost layers" mention | Quick fix |
| 15 | `/newsletter-welcome/` | "Every two weeks", seven layers | Quick fix |

## Tier 3: blog posts with seven layers and unsourced stats (all have the pasted head)
Listed in order of search impressions, then by how much is wrong.

| # | Page | Fix |
|---|---|---|
| 16 | `/seven-cost-layers/` | **LIVE Sept 27, score 89**, now at `/marketing-costs/` with a 301. Added to the blog page. |
| 17 | `/roas-looks-good-campaigns-lose-money/` | Full rebuild ("every two weeks", 52 unsourced stats) |
| 18 | `/tcpa-compliance-cost-for-law-firms/` | Full rebuild (99 impressions) |
| 19 | `/true-cost-closed-install/` | Light clean (28 unsourced stats) |
| 20 | `/reconciling-pace-greensky-service-finance/` | Light clean; verify the lender fee percentages or remove them |
| 21 | `/financing-fees-home-services/` | Light clean |
| 22 | `/true-marketing-roi/` | Light clean; soften the "cannot" title |
| 23 | `/true-cost-per-move-in/` | Light clean |
| 24 | `/cost-per-admission-addiction-treatment/` | Light clean; remove "8 to 12 times" |
| 25 | `/cost-per-enrolled-member-medicare-advantage/` | Light clean; remove "3 to 5 times" |
| 26 | `/chargebacks-marketing-cost/` | Light clean |
| 27 | `/personal-injury-ad-spend-attribution/` | Light clean |
| 28 | `/personal-injury-case-type-cac/` | Light clean |
| 29 | `/multi-state-pi-firm-attribution/` | Light clean |
| 30 | `/personal-injury-settlement-lag/` | Light clean |
| 31 | `/mass-tort-lead-aggregator-economics/` | Light clean |
| 32 | `/cost-per-booked-job-hvac-plumbing/` | Light clean |
| 33 | `/hvac-customer-acquisition-cost/` | Light clean; check the "3x CPL" title |
| 34 | `/hvac-customer-lifetime-value/` | Light clean |
| 35 | `/hvac-marketing-channel-mix/` | Light clean |
| 36 | `/hvac-seasonal-cost-per-lead/` | Light clean; source or remove "80 percent more in July" |
| 37 | `/angi-homeadvisor-lead-cost/` | Light clean |

**Clean already:** privacy and data-deletion.

## Suggested pace
- 1 full rebuild or 3–4 light cleans per session.
- Tier 1 first (about 6 sessions), then Tier 2, then Tier 3.
