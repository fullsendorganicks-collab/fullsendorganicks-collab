# Rank Math box: /lead-quality/ (post ID 245)

**LIVE Sept 28: score 83, slug `lead-quality`.** Nick pasted it into post **245**, which held the live 30-day retest post (`/30-day-retest-methodology/`, 82), not into post 252. Fix: the 30-day retest post moves into post 252 and takes back its original slug (see `30-day-retest-methodology-RANKMATH.md` → "Sept 28 restore" and R11/R12 in `website/REDIRECTS.md`). Nothing is lost: both posts stay live.

_The notes below were written for post 252; the content, fields and claims are the same._

**What this replaces:** post 252, titled "Directive Accuracy: 30-Day Retest Beats Gut-Feel". Its body was an old copy of the Tag Manager post, and it carried:
- the fake 80% (in its meta description)
- a duplicate title and keyword of the live `/30-day-retest-methodology/` post (82)

Having two posts with the same title and keyword splits what Google gives both. Per your rule it isn't deleted or redirected. It's rebuilt as a new post with its own keyword, and it links to the real 30-day retest post, so the two posts support each other instead of competing.

## Why this topic (live data, Sept 28)
- **Your Search Console:** this -2 URL had 0 impressions in the last 3 months. The original `/30-day-retest-methodology/` had all 38, so the duplicate was doing nothing.
- **Your GA4:** the -2 URL had 0 visits in the last 3 months. The original had 1.
- **Keyword demand:**

  | Keyword | Searches/mo | Ad value | Competition |
  |---|---|---|---|
  | lead quality | 260 | ~$9/click | Low |
  | how to improve lead quality | 70 (up to 320 in recent months) | — | Low |
  | high quality lead | 50 | ~$104/click | Low |

  The ad value is high because the people searching buy leads or run lead-gen, which is our buyer.
- **Google today:**
  - The results are vendor and agency guides (Integrate, Mailchimp, ActiveProspect, WhatConverts, Cognism).
  - They measure lead quality with scores and checklists.
  - None puts a dollar value on a lead source or shows a worked profit-per-lead example.
  - People Also Ask:
    - "What is considered a good lead?"
    - "How to identify quality leads?"
    - "What is the 5 minute rule for leads?"
    - "What is a qualified vs unqualified lead?"

    All four are answered on the page.
- **Why it gets clients:** the page ends where CDAI starts. It shows a business why the cheaper lead source can be the one losing money, and that ranking sources by profit is what CDAI does every night.

## Where to find it
Open `alloceraintelligence.com/wp-admin/post.php?post=252&action=edit` (you already have it open). Delete the old content, paste in `30-day-retest-methodology-2.html` (or the `-copy-paste.txt` copy), and keep **Elementor Canvas**. Change the WordPress title to the H1 below.

## Before you paste
1. Upload `images/lead-quality-profit-per-lead-example.png` to Media.
   - Alt text: `Lead quality example: $30 leads from Source A earn $6 profit per lead, while $80 leads from Source B earn $46 profit per lead`
   - Expected URL: `https://alloceraintelligence.com/wp-content/uploads/2026/09/lead-quality-profit-per-lead-example.png`
2. Set it as the Featured and Social image.

## Rank Math fields
| Field | Value |
|---|---|
| Post title / H1 | `Lead Quality: How to Measure It by What Each Lead Is Worth` |
| Focus Keyword | `lead quality` |
| Secondary keywords | `how to measure lead quality, lead quality metrics, how to improve lead quality, quality leads` |
| SEO Title (53 chars) | `Lead Quality: 6 Metrics to Measure It in Real Dollars` |
| Permalink | `30-day-retest-methodology-2` (original slug, per the rule). **Recommended, your call:** `lead-quality`. |
| Meta Description (146 chars) | `Lead quality is how likely a lead is to become a customer who stays. Measure it with 6 metrics, plus an example of profit per lead by lead source.` |
| Schema | Article → Blog Post |

**Old fields to delete:**
- SEO title "Directive Accuracy: 30-Day Retest Beats Gut-Feel"
- focus keyword "directive accuracy"
- the old description (the one that says "80% accuracy")

**If you change the slug:** add a 301 from `30-day-retest-methodology-2` to `/lead-quality/`. I'll log it as R11 in `website/REDIRECTS.md` once you tell me.

## Checks
- **Size:** about 1,860 words. "Lead quality" appears 27 times (~1.4%), including in the H1, the first sentence, the SEO title, the description, the alt text, and several H2s.
- **Structure:**
  - 8 H2 sections + the final CTA
  - table of contents and key takeaways
  - 2 tables: the 6 metrics, and the Source A vs. B example
  - 5 steps
  - image
  - 6 FAQs (the 4 People Also Ask questions + 2 more)
- **Links:** 11 internal links to rebuilt, live pages:
  - average cost per lead
  - marketing costs
  - true CAC calculator
  - 30-day retest
  - scale/hold/cut/pause framework
  - offline conversion tracking
  - cost per signed case
  - ROAS calculator
  - validation report, How It Works, pricing, Get Started
- **5 external links**, each seen live in Google's results on Sept 28:

  | Source | What it confirms |
  |---|---|
  | Integrate | Definition: "the degree to which a lead is accurate, relevant, and ready for the next step in your revenue process" |
  | Mailchimp | Definition: lead quality "identifies how likely a prospect is to buy your product or service" |
  | ActiveProspect | Metrics: conversion rate (lead to opportunity or sale), contact rate, lead-to-sale velocity, cost |
  | Search Influence | Sources are compared by "conversion rates, cost per qualified lead, and long-term customer value" |
  | LeanData | Responding within five minutes makes a team "21 times more effective than waiting 30 minutes" |

- **Tracking:** the same GA4 script as the other rebuilt pages.
- **Layout:** renders at desktop (1280) and phone (390) with no sideways page scrolling and 0 script errors.
- **Byline and title:** no date, no year.

## Every claim, and where it's proven
| Claim | Source |
|---|---|
| Definitions, metrics, 5-minute rule | Linked sources above, each attributed by name on the page |
| Example: Source A ($30, 5%, 4 kept, $750 per customer, $600, $6 per lead) vs. Source B ($80, 15%, 14 kept, $571, $4,600, $46) | Labeled "illustrative, not client data". Arithmetic: A: 100 × 30 = 3,000; 5 − 1 = 4; 3,000 ÷ 4 = 750; 4 × 900 − 3,000 = 600; ÷ 100 = 6. B: 100 × 80 = 8,000; 15 − 1 = 14; 8,000 ÷ 14 = 571.43; 14 × 900 − 8,000 = 4,600; ÷ 100 = 46. "More than seven times": 46 ÷ 6 = 7.7. |
| $66.69 lead → $437 customer | Our live average cost per lead page (WordStream benchmark + labeled example) |
| CDAI: true cost per lead, true CAC, real profit, one decision nightly, rechecks math, grades past calls | Same approved wording as the other rebuilt pages |
| Meta, Google Ads, LinkedIn, HubSpot and Salesforce connect in one click | Same wording as your live rebuilt pages |
| 89.5% (1,210/1,352), 9 businesses, 7 industries, math 100% two ways | The validation report |

**Kept out on purpose:**
- "directive accuracy" as the keyword (it belongs to the live 30-day retest post)
- any accuracy claim other than the validation numbers
- secondhand stats I couldn't tie to a named source: the "22 times", "900%", and "25% qualified / 40% conversion" figures in other results
- lead scoring thresholds
- client or pilot data

## Removed from the old post
- the fake 80%
- the duplicate title and keyword
- the copied Tag Manager body, with its pasted `<head>`
