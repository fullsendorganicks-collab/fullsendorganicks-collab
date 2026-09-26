# Website fix list: every page still carrying old, false, or unsourced info

This list comes from a scan of the WordPress export run on Sept 26. It covers all 41 pages not yet rebuilt.

**Already fixed (9):**
- Net Marketing Contribution
- Calculate Contribution Margin
- Scale Hold Cut Pause
- Triple Whale vs Rockerbox
- Northbeam Alternative
- Rockerbox Alternative
- Cost Per Signed Case
- Blog
- Homepage

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

## Tier 1: false claims (fix first)
| # | Page | Problems | Fix |
|---|---|---|---|
| 1 | `/30-day-retest-methodology/` | 80%, "55 of 56", seven layers, $2,500 guarantee, wrong `/blog/` links, pasted head | **Full rebuild (NEXT)**, built around the 89.5% validation. Nick sent the current HTML. |
| 2 | `/55-directives-study/` | The whole page is the fake 80% | **301** to the validation report |
| 3 | `/30-day-retest-methodology-2/` | Exact copy of the tag-manager page, and says 80% | **301** to `/tag-manager-real-roi/` |
| 4 | `/tag-manager-real-roi/` | 80%, seven layers, 14 unsourced stats, pasted head | Full rebuild (it also ties into the GTM work) |
| 5 | `/allocera-vs-salesforce/` | 80%, seven layers, "cannot" claims about Salesforce, pasted head | Full rebuild |
| 6 | `/true-cac/` + `/true-cac-2/` | 80%, seven layers, duplicate pair | Merge into one full rebuild, then 301 the `-2` page |
| 7 | `/marketing-margin-distortion-index/` | 80%, Apex, "2026" in the title, many unsourced stats, "measured using CDAI" claim | Full rebuild, or retire. **Nick decides.** |
| 8 | `/proof/`, `/allocera-intelligence-case-study-proof/`, `/case-study-2-oauth-validation/` | Apex story | **Nick decides:** rewrite around the validation, or retire |

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
| 16 | `/seven-cost-layers/` | **New post** at the same URL (246 impressions) |
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
