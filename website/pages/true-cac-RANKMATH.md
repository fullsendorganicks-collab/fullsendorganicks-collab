# Rank Math box: /true-cac/ (merges /true-cac/ + /true-cac-2/)

**LIVE Sept 28: score 81, slug kept.** `/true-cac-2/` trashed; its 301 = R8 in `website/REDIRECTS.md`.

**What this replaces:** two near-duplicate posts. Both carried:
- the fake 80%
- the "seven cost layers" framing
- unsourced "30–70%" and "20–60%" gaps
- a made-up "$47 vs $89" senior care story
- a pasted `<head>`

This is one new post on `/true-cac/`, with a working calculator. `/true-cac-2/` gets a 301 to it.

## Why this topic (live data, Sept 27)
- **Your Search Console:** `/true-cac/` had 20 impressions in the last 28 days at an average position of 5.7; the queries are hidden (too few to show). `/true-cac-2/` had 2. Having two versions splits what little Google gives them, and the merge fixes that.
- **Keyword demand:**

  | Keyword | Searches/mo | Ad value | Competition |
  |---|---|---|---|
  | customer acquisition cost formula | 880 | ~$6/click | Low |
  | how to calculate customer acquisition cost | 720 | ~$9/click | Low |

  That's about 1,600 searches a month for one topic, the biggest opening so far.
- **Google today:**
  - The results are almost all written for software and online stores (Wall Street Prep, Shopify, SaaSHero, Paddle).
  - None handles lead payouts or refunds.
  - People Also Ask:
    - "What is a good cost per customer acquisition?"
    - "What is the CLV to CAC ratio?"
    - "How do you calculate the cost of acquiring a customer?"
    - "How is the CAC calculated?"

    All four are answered on the page.
- **Why it gets clients:** the calculator shows a visitor, with their own numbers, how far their real cost per customer is from the number they've been using. That gap is what CDAI tracks nightly.

## Where to find it
Posts → search "True CAC". Open the **`/true-cac/`** post (the one without "-2"). Delete the old content, paste in `true-cac.html` (or the `-copy-paste.txt` copy), and keep **Elementor Canvas**. Change the WordPress title to the H1 below.

**Then the `-2` post:** trash or unpublish `/true-cac-2/` and add its 301 (R8 below).

## Before you paste
1. Upload `images/customer-acquisition-cost-formula-basic-vs-true-cac.png` to Media.
   - Alt text: `Customer acquisition cost formula example: basic CAC of $250 from ad spend divided by 40 customers, versus true CAC of $458 from all acquisition costs divided by 36 customers kept`
   - Expected URL: `https://alloceraintelligence.com/wp-content/uploads/2026/09/customer-acquisition-cost-formula-basic-vs-true-cac.png`
2. Set it as the Featured and Social image.

## Rank Math fields
| Field | Value |
|---|---|
| Post title / H1 | `Customer Acquisition Cost Formula: How to Calculate Your True CAC` |
| Focus Keyword | `customer acquisition cost formula` |
| Secondary keywords | `how to calculate customer acquisition cost, true cac, cac formula, customer acquisition cost` |
| SEO Title (60 chars) | `Customer Acquisition Cost Formula + Free True CAC Calculator` |
| Permalink | `true-cac` (original slug, per the rule). **Recommended, your call:** `customer-acquisition-cost-formula`. |
| Meta Description (155 chars) | `The customer acquisition cost formula most guides use leaves out lead payouts, fees and refunds. Use the free calculator to see your true CAC per customer.` |
| Schema | Article → Blog Post |

**Old fields to delete** (from the site export):
- the old SEO titles "True Cost Per Lead: Why Your Dashboard Is Lying" and "True CAC: The Complete Reconciliation Guide"
- the old focus keywords "true cost per lead" and "true CAC"

## Redirects (added to `website/REDIRECTS.md`)
- **R8, needed either way:** source `true-cac-2`. Destination: this post's final URL (`/true-cac/`, or `/customer-acquisition-cost-formula/` if you change the slug).
- **R9, only if you change the slug:** source `true-cac` → destination `/customer-acquisition-cost-formula/`. Then point R8 straight at the new URL, so there's no chain of redirects.

## Checks
- **The calculator was tested in a real browser:**

  | Test | Dashboard CPL | Basic CAC | True CAC | Gap |
  |---|---|---|---|---|
  | Example | $50 | $250 | $458 | +83% |
  | Extra costs and lost customers set to 0 | — | $250 | $250 | 0 (message says they match) |

  - Zero customers asks for inputs.
  - 0 script errors.
  - The `calculator_use` event fires once per visit; the numbers typed are never sent.
- **Size:** about 1,830 words. "Customer acquisition cost formula" appears 17 times (~0.9%), including in the H1, the first sentence, three H2s, the SEO title, the description and the alt text. "True CAC" appears 25+ times.
- **Structure:**
  - calculator near the top
  - 9 H2 sections + the final CTA
  - table of contents, 4 steps, 2 tables, image
  - 6 FAQs (the 4 People Also Ask questions + 2 more)
- **Links:** 10 internal links to rebuilt, live pages:
  - ROAS calculator
  - contribution margin calculator
  - marketing costs
  - 30-day retest
  - cost per signed case
  - net marketing contribution
  - validation report, How It Works, pricing, Get Started
- **4 external links**, each seen live in Google's results on Sept 27:

  | Source | What it confirms |
  |---|---|
  | Wall Street Prep | CAC is "dividing the sales and marketing expenses… by the number of new customers acquired" |
  | Shopify | "add up all the costs associated with acquiring new customers in a specific period, then divide the total by the number of new" customers |
  | Smith.ai | costs to include: "Advertising costs, Sales/referral commissions, Outside agency fees" |
  | SaaSHero | "Build a Fully-Loaded CAC Numerator"; "Align CAC With Your Sales-Cycle Timing" |

- **Tracking:** the same GA4 script, plus the calculator event.
- **Layout:** renders at desktop (1280) and phone (390) with no sideways page scrolling and 0 script errors.
- **Byline and title:** no date, no year.

## Every claim, and where it's proven
| Claim | Source |
|---|---|
| Standard CAC formula | Wall Street Prep, Shopify (linked) |
| What to include | Smith.ai, SaaSHero (linked); campaign vs company split explained on the page |
| Example: $250 vs $458 (+83%), $50 CPL, max-CAC example ($800, $342, −$100) | Labeled "illustrative, not client data". Arithmetic: 16,500 ÷ 36 = 458.33; 10,000 ÷ 40 = 250; 10,000 ÷ 200 = 50; 2,000 − 1,200 = 800. |
| CDAI calculates true cost per lead, true CAC, real profit; one decision a night; rechecks math; grades past calls | Same approved wording as the other rebuilt pages |
| Meta, Google Ads, LinkedIn, HubSpot and Salesforce connect in one click | Same wording as your live rebuilt pages |
| 89.5% (1,210/1,352), 9 businesses, 7 industries, math 100% two ways | The validation report |

**Kept out on purpose:**
- the old "30–70%" and "20–60%" gaps
- the "$47 vs $89" story (not provable)
- any CLV:CAC "rule of thumb" ratio (no primary source seen)
- any "layers" framing

## Removed from the old posts
- the fake 80%
- "seven cost layers" (both posts)
- "30–70%" and "20–60%" gaps
- "0 ad platforms report true CAC"
- the "$47 / $89" senior care anecdote
- the "May 19, 2026" byline
- both pasted `<head>`s
