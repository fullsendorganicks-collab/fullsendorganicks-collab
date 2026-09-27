# Rank Math box: /average-cost-per-lead/ (was /marketing-margin-distortion-index/)

**LIVE Sept 28: score 83.** Slug changed; 301 = R10 in `website/REDIRECTS.md`.

**What this replaces:** "The 2026 Marketing Margin Distortion Index". It claimed to be the "first published benchmark", "measured across verticals using the CDAI engine". It carried:
- the fake 80%
- "seven cost layers"
- "2026" in the title
- unsourced stats ("overstate true ROAS by 2.3x", "25–45%", vertical ranges)
- an Apex "case study" with numbers that can't be proven
- a pasted `<head>`

Per your rule, it isn't retired. It's rebuilt into an honest benchmark page that keeps the original idea (how far dashboard numbers are from what a customer really costs) and uses only published, linked benchmarks.

## Why this topic (live data, Sept 28)
- **Your Search Console:** 13 impressions in the last 28 days at an average position of 6.8. The queries are hidden (too few to show).
- **Keyword demand:**

  | Keyword | Searches/mo | Ad value | Competition |
  |---|---|---|---|
  | average cost per lead | 90 | ~$44/click | Low |
  | average cost per lead by industry | 90 | ~$44/click | Low |

  That's one of the highest ad values we've found, so buyers search it.
- **Google today:**
  - The results are agency blogs repeating WordStream/LocaliQ numbers, often mixing years and sources.
  - None follows the lead to what a customer costs.
  - People Also Ask: "What is the average cost per lead in Google Ads?" and "What is considered a good cost per lead?". Both are answered on the page.
- **Why it builds trust and gets clients:** every number links to its named source, and the page shows the gap between a benchmark CPL and real cost per customer, which is the problem CDAI solves.

## Where to find it
Posts → search "Distortion". Delete the old content, paste in `marketing-margin-distortion-index.html` (or the `-copy-paste.txt` copy), and keep **Elementor Canvas**. Change the WordPress title to the H1 below.

## Before you paste
1. Upload `images/average-cost-per-lead-to-cost-per-customer.png` to Media.
   - Alt text: `Average cost per lead example: a $66.69 lead becomes $333 per closed customer at a 20% close rate, $393 with payouts and fees, and $437 per customer kept after refunds`
   - Expected URL: `https://alloceraintelligence.com/wp-content/uploads/2026/09/average-cost-per-lead-to-cost-per-customer.png`
2. Set it as the Featured and Social image.

## Rank Math fields
| Field | Value |
|---|---|
| Post title / H1 | `Average Cost Per Lead by Industry, and What a Customer Really Costs` |
| Focus Keyword | `average cost per lead` |
| Secondary keywords | `average cost per lead by industry, cost per lead benchmarks, good cost per lead, google ads cost per lead` |
| SEO Title (57 chars) | `Average Cost Per Lead by Industry: Benchmarks + True Cost` |
| Permalink | `marketing-margin-distortion-index` (original slug, per the rule). **Recommended, your call:** `average-cost-per-lead`. |
| Meta Description (152 chars) | `Average cost per lead is $66.69 on Google Ads and $27.39 on Facebook, per published benchmarks. See it by industry and what a customer really costs you.` |
| Schema | Article → Blog Post |

**Old fields to delete:**
- SEO title "The 2026 Marketing Margin Distortion Index: True CAC by Vertical | Allocera Intelligence"
- focus keyword "marketing margin distortion"
- the old description

## Checks
- **Size:** about 1,660 words. "Average cost per lead" appears 16 times (~1%), including in the H1, the first sentence, several H2s, the SEO title, the description and the alt text.
- **Structure:** 8 H2 sections + the final CTA, table of contents, key takeaways, 3 tables (by channel, by industry, lead-to-customer), 5 steps, image, 6 FAQs.
- **Links:** 10 internal links to rebuilt, live pages:
  - true CAC calculator
  - ROAS calculator
  - offline conversion tracking
  - marketing costs
  - cost per signed case
  - scale/hold/cut/pause framework
  - validation report, How It Works, pricing, Get Started
- **5 external links**, each seen live in Google's results on Sept 28:

  | Source | What it confirms |
  |---|---|
  | WordStream PPC benchmarks | CTR 6.64%, CPC $5.42, conversion rate 8.18%, CPL $66.69 |
  | WordStream Google Ads benchmarks | $66.69 average; Physicians & Surgeons $40.04; Real Estate $102.51; Restaurants & Food $30.57 |
  | LocaliQ Facebook benchmarks | $27.39 CPL for the leads objective |
  | TheAdSpend | HVAC Google Ads CPL $104 blended (SearchLight study, 816 contractors) |
  | GrowthCentr | CPC range up to $9.87 for Attorneys and Legal Services (WordStream) |

- **Tracking:** the same GA4 script as the other rebuilt pages.
- **Layout:** renders at desktop (1280) and phone (390) with no sideways page scrolling and 0 script errors.
- **Byline and title:** no date, no year. The body says "latest benchmarks" rather than naming a year.

## Every claim, and where it's proven
| Claim | Source |
|---|---|
| Every benchmark number | Linked source in the table, seen live in Google Sept 28 |
| "About 12 clicks at $5.42 per lead" | Math: 1 ÷ 8.18% = 12.2 clicks; 12.2 × $5.42 ≈ $66 |
| Example $66.69 → $333.45 → $393.45 → $437.17 | Labeled "illustrative, not client data". Arithmetic: 66.69 ÷ 0.2 = 333.45; + 60 = 393.45; ÷ 0.9 = 437.17. |
| Max CPL = profit per customer × close rate ($800 × 20% = $160) | Math, labeled as an example |
| CDAI: true cost per lead, true CAC, real profit, one decision nightly, rechecks math, grades past calls | Same approved wording as the other rebuilt pages |
| 89.5% (1,210/1,352), 9 businesses, 7 industries, math 100% two ways | The validation report |

**Kept out on purpose:**
- the old "distortion score" and any claim that CDAI measured industry benchmarks
- the Apex numbers (Apex was a real pilot, but the old figures can't be proven here; the pilot story belongs on the rebuilt proof pages)
- any "layers" framing
- secondhand numbers with conflicting years (for example, the attorney CPL of $131.63 is reported as both 2025 and 2026, so it was left out)
- thresholds

## Removed from the old post
- the fake 80%
- "2026" in the title
- "first published benchmark… measured using CDAI"
- "seven cost layers"
- "2.3x" and "25–45%"
- the Apex case-study numbers
- the pasted `<head>`
