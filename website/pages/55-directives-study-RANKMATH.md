# Rank Math box: /55-directives-study/ → new ROAS Calculator page

**What this replaces:** the old page's only subject was the fake "80%" study. This is a brand-new page: a working ROAS calculator built for lead-driven businesses (break-even ROAS + real profit), aimed at bringing in clients, not just a Rank Math score.

## Why this topic (live data, Sept 27)
- **Your Search Console:** `/55-directives-study/` had **0 impressions** in the last 3 months, so there's no traffic to lose. Your site also has no ROAS rankings yet (GSC: 4 stray impressions in 6 months).
- **Your GA4 (last 3 months):** organic search visitors are your most engaged: 47 seconds on average, vs 12 for direct. So pages that rank bring the best visitors.
- **Keyword demand:**

  | Keyword | Searches/mo | Ad value | Competition |
  |---|---|---|---|
  | roas calculator | 1,300 | ~$15/click | Low |
  | break even roas | 170 | ~$28/click | Low |

  "roas calculator" gets about 5 times the searches of "marketing costs" (260), and the high ad value on "break even roas" means buyers search it.
- **Google today:**
  - The top 10 is almost all simple two-box calculators (rows.com, Sleeknote, small sites) or ecommerce break-even tools asking for product cost and shipping.
  - None handle lead payouts, refunds, or the cost to deliver a service, so a lead-gen version is a real gap.
  - People Also Ask: "How is ROAS calculated?", "Is a 2.5 ROAS good?", "What ROAS is 25% ACoS?", "What does 4:1 ROAS mean?". All four are answered on the page.
- **Why it gets clients:** it shows a visitor, with their own numbers, that a "good" ROAS can lose money. That's the exact problem CDAI solves, and the next step is Get Started.

## Where to find it
Posts (or Pages) → search "55". Delete the old content, paste in `55-directives-study.html` (or the `-copy-paste.txt` copy), and keep **Elementor Canvas**. Change the WordPress title to the H1 below.

## Before you paste
1. Upload `images/roas-calculator-same-roas-different-profit.png` to Media.
   - Alt text: `ROAS calculator example: two campaigns with the same 3.0 ROAS; one keeps $7,100 and the other loses $1,900 once payouts and delivery costs are counted`
   - Expected URL: `https://alloceraintelligence.com/wp-content/uploads/2026/09/roas-calculator-same-roas-different-profit.png`. If WordPress gives it a different URL, tell me and I'll update the page.
2. Set it as the Featured and Social image.

## Rank Math fields
| Field | Value |
|---|---|
| Post title / H1 | `ROAS Calculator: Find Your Break-Even ROAS and Real Profit` |
| Focus Keyword | `roas calculator` |
| Secondary keywords | `break even roas, break even roas calculator, return on ad spend calculator, how to calculate roas` |
| SEO Title (54 chars) | `ROAS Calculator: Is Your 3.0 ROAS Actually Profitable?` |
| Permalink | `55-directives-study` (original slug, per the rule). **Recommended, your call:** `roas-calculator` + the 301 below. |
| Meta Description (153 chars) | `Free ROAS calculator for lead-driven businesses. Add fees, payouts, refunds, and delivery costs to see your break-even ROAS and real profit per campaign.` |
| Schema | Article → Blog Post |

**About the slug:** the old slug names the retired study, and it has 0 impressions. The last page moved from the low 80s to 89 once the keyword was in the URL. For a calculator, the URL also matters in Google's results: people searching "roas calculator" see `/roas-calculator/` and know they've found one.

## Redirect (only if you change the permalink)
Go to **Rank Math → Redirections → Add New**:
- Source URL: `55-directives-study`
- Destination URL: `https://alloceraintelligence.com/roas-calculator/`
- Redirection Type: **301 Permanent Move**

No rebuilt page or the blog links to `/55-directives-study/`, so nothing else needs fixing.

## Checks
- **The calculator was tested in a real browser**, with every result checked by hand:

  | Test | ROAS | Break-even ROAS | Profit | Per $1 of ads |
  |---|---|---|---|---|
  | Example A | 3.00 | 1.75 | $7,100 | $0.71 |
  | Example B (payouts $6,000, delivery $12,000) | 3.00 | 3.70 | −$1,900 | −$0.19 |

  - Costs larger than revenue show "No ROAS can make this campaign profitable."
  - Zero ad spend asks for inputs.
  - 0 script errors.
- **Size:** about 2,000 words. "ROAS calculator" appears 21 times (~1.05%), including in the H1, the first sentence, two H2s, the SEO title, the description, the alt text and an H3. "Break-even ROAS" appears 25+ times.
- **Structure:**
  - calculator placed right after the key takeaways (for people who just want the tool)
  - 9 H2 sections + the final CTA
  - table of contents, usage steps, formula, comparison table, image
  - 7 FAQs (the 4 People Also Ask questions + 3 more)
- **Links:** 10 internal links to rebuilt, live pages:
  - marketing costs
  - contribution margin calculator
  - scale/hold/cut/pause framework
  - 30-day retest
  - cost per signed case
  - net marketing contribution
  - validation report, How It Works, pricing, Get Started
- **4 external links**, each seen live in Google's results on Sept 27:
  - Shopify's break-even ROAS guide: "divide 1 by your pre-ad profit margin"
  - Funnelytics: break-even ROAS is "the minimum return on ad spend at which ad-driven revenue exactly covers your variable costs"
  - Stripe pricing: 2.9% + 30¢
  - Brand Builder University: "ACOS = Ad Spend/Ad Sales… ROAS = Sales/Ad Spend"
- **Tracking:** the same GA4 script as the other rebuilt pages (clicks, scroll depth, sections read, FAQ opens). This page also has a new event, **`calculator_use`** (dataLayer `cdai_calculator_use`), which fires once per visit when someone types into the calculator. The numbers they type are never sent.
- **Layout:** renders at desktop (1280) and phone (390) with no sideways scrolling. The calculator uses 4 results in a row on desktop, 2 on tablets, and stacked fields on phones.
- **Byline and title:** no date, no year.

## Every claim, and where it's proven
| Claim | Source |
|---|---|
| ROAS = revenue ÷ ad spend; 3:1 = 3x = 300% | Standard definition. Google's own AI overview for "roas calculator" gives the same formula. |
| Break-even ROAS = 1 ÷ margin before ads | Shopify guide (linked), Funnelytics (linked) |
| Example A/B numbers (1.75, 3.70, $7,100, −$1,900, 57%, 27%) | Labeled "illustrative, not client data". Arithmetic checked by hand and by the calculator: A: 30,000 − 12,900 = 17,100; 30,000 ÷ 17,100 = 1.75. B: 30,000 − 21,900 = 8,100; 30,000 ÷ 8,100 = 3.70. |
| 25% ACoS = 4.0 ROAS; 50% = 2.0; 33% ≈ 3.0 | Math from the linked ACoS/ROAS definitions |
| Stripe 2.9% + 30¢ | Stripe pricing (linked) |
| What CDAI subtracts, one decision a night, rechecks math, stops on bad data, grades past calls | Same approved wording as the other rebuilt pages; engine true-cost formula, Control Tower, health gate, `score_mature_directives` |
| 89.5% (1,210/1,352), 9 businesses, 7 industries, math 100% two ways | The validation report |

**Kept out on purpose:**
- ROAS "benchmarks" by industry (none from a primary source; the page explains why they're risky)
- anything from the old study
- any "N costs" or "layers" framing
- any claim that CDAI never assumes costs (F5 isn't merged)
- thresholds

## Removed from the old page
The whole page is replaced:
- the fake "80%" study and its "55 directives" framing
- the old pasted `<head>`

## Blog (on hold, per Nick)
When the rebuild is done, the blog gets a card for this page (at `/roas-calculator/` if the slug changes). This is tracked in the blog to-do list.
