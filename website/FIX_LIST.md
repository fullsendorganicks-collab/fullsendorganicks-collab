# Website fix list: every page still carrying old, false, or unsourced info

**Nick's rules (Sept 28):** never delete or retire a page; redo it into something that builds reach, authority and trust. The blog page is last. Apex was a real pilot: keep it where it's true (the Sid and Rebecca homepage reviews stay). Nothing sensitive or proprietary.

**Slug changes, redirects and links to old URLs: see `REDIRECTS.md`.** Update it the same day any slug changes.

This list comes from a scan of the WordPress export run on Sept 26 (all live pages).

## Where we are (end of Sept 27): paused for the night

**Live and done (14), with Rank Math scores:**

| Page | Score | Notes |
|---|---|---|
| Homepage | 81 | |
| `/blog/` | 72 | Normal for a directory page. **Re-paste at the end** (pending list below). |
| `/net-marketing-contribution/` | done | |
| `/calculate-contribution-margin/` | done | |
| `/scale-hold-cut-pause-framework/` | 89 | |
| `/triple-whale-vs-rockerbox-vs-allocera/` | done | |
| `/home-sample/northbeam-alternative/` | done | |
| `/home-sample/rockerbox-alternative/` | done | |
| `/cost-per-signed-case/` | done | |
| `/30-day-retest-methodology/` | 82 | |
| `/marketing-costs/` (was `/seven-cost-layers/`) | 89 | |
| `/roas-calculator/` (was `/55-directives-study/`) | 90 | |
| `/tag-manager-real-roi/` (now Offline Conversion Tracking) | 80 | Slug kept |
| `/salesforce-campaign-influence/` (was `/allocera-vs-salesforce/`) | 89 | |
| `/true-cac/` (Customer Acquisition Cost Formula; merged `-2`) | 81 | Slug kept |

**Next:** #7 built (waiting for paste), then #3 (the -2 duplicate becomes a new post), then #8 proof pages, then Tier 2. Then #7 and #8 need Nick's decision (rebuild or retire), then Tier 2.

**Left to do: 30 items**
- Tier 1:
  - #6 true CAC merge
  - #3 `/30-day-retest-methodology-2/` → new post
  - #7 margin distortion index (full rebuild)
  - #8 three proof/case-study pages (full rebuilds)
- Tier 2:
  - #9 pricing (on hold)
  - #10 How It Works (full rebuild)
  - #11 About (full rebuild)
  - #12 Dashboard (light clean)
  - #13–15 quick fixes: validation report, terms, newsletter welcome
- Tier 3: #17–37, which is 2 full rebuilds (#17 ROAS-looks-good, #18 TCPA) and 19 light cleans.

**Saved for the very end (Nick, Sept 27): do these after every page and post is finished.**
1. **Redirects:** add every 301 in `REDIRECTS.md` and run its one-minute test. So far: R1, R2, R3, R4 check, R5, R7.
2. **Link pass:** re-scan every page for links to old slugs (target 0).
3. **Blog page:** rebuild and paste once, with final URLs (pending list below).
4. **Optional:** add the GA4 tracking script to the 8 pages rebuilt before tracking existed (Nick re-pastes them).

**What the scan looks for:**
- **80% claim:** the retired, never-computed "80% measured accuracy".
- **Seven cost layers:** retired framing.
- **Apex:** allowed only in the homepage reviews.
- **30-day retest:** claims about a retest process. These must be checked against the engine before any rewrite.
- **Old CTA:** a "$2,500 audit, don't pay if…" guarantee.
- **Unsourced stats:** numbers like "8 to 12 times" or "30 to 70 percent" with no source.
- **Pasted head:** a second `<title>` and a wrong canonical. This keeps some pages out of Google.

Two kinds of fix:
- **Full rebuild:** new research and a new page, as done so far.
- **Light clean:** keep the post and its design, but strip the pasted head, remove the retired framing and fake stats, and fix the links. About a third of the work of a rebuild.

## Blog page: pending changes (ON HOLD until the rebuild is done, per Nick)
`pages/blog.html` already has the first two. Paste only when Nick says the rebuild is finished.
- [x] Add card: Marketing Costs → `/marketing-costs/`
- [x] Add card: 30-Day Retest → `/30-day-retest-methodology/`
- [ ] Add card: ROAS Calculator → `/roas-calculator/`
- [ ] Update card: Tag Manager → Offline Conversion Tracking → `/tag-manager-real-roi/` (slug kept)
- [ ] Update card: Allocera and Salesforce → Salesforce Campaign Influence → `/salesforce-campaign-influence/`
- [ ] Update card: True CAC → Customer Acquisition Cost Formula (final URL); remove any `/true-cac-2/` card
- [ ] Update card: Margin Distortion Index → Average Cost Per Lead by Industry (final URL)
- [ ] Remove cards for pages that get 301'd (e.g. `/30-day-retest-methodology-2/`, `/true-cac-2/`) and update titles/descriptions for every rebuilt page
- [ ] Re-check every card link against the live URLs before handing over

## Tier 1: false claims (fix first)
| # | Page | Problems | Fix |
|---|---|---|---|
| 1 | `/30-day-retest-methodology/` | 80%, "55 of 56", seven layers, $2,500 guarantee, wrong `/blog/` links, pasted head | **LIVE Sept 27, score 82.** |
| 2 | `/55-directives-study/` | The whole page is the fake 80% | **LIVE Sept 27, score 90**, now at `/roas-calculator/` (brand-new ROAS calculator). 301 = R3 in `REDIRECTS.md`. |
| 3 | `/30-day-retest-methodology-2/` | Exact copy of the tag-manager page, and says 80% | **Full rebuild into a new post (Nick: never delete).** New topic, its own keyword, not a duplicate. |
| 4 | `/tag-manager-real-roi/` | 80%, seven layers, 14 unsourced stats, pasted head | **LIVE Sept 27, score 80**, slug kept. New post "Offline Conversion Tracking". |
| 5 | `/allocera-vs-salesforce/` | 80%, seven layers, "cannot" claims about Salesforce, pasted head | **LIVE Sept 27, score 89**, now at `/salesforce-campaign-influence/`. 301 = R7. |
| 6 | `/true-cac/` + `/true-cac-2/` | 80%, seven layers, duplicate pair | **LIVE Sept 28, score 81**, slug kept. `-2` trashed; 301 = R8. |
| 7 | `/marketing-margin-distortion-index/` | 80%, Apex numbers, "2026" in the title, many unsourced stats, "measured using CDAI" claim | **BUILT Sept 28**: rebuilt as "Average Cost Per Lead by Industry" (`pages/marketing-margin-distortion-index.html` + RANKMATH + image). Focus "average cost per lead" (~$44/click). Recommended slug `average-cost-per-lead` (Nick's call). Waiting for paste + score. |
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
