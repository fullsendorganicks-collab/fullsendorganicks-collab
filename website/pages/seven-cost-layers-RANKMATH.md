# Rank Math box: /marketing-costs/ (was /seven-cost-layers/)

**LIVE Sept 27: score 89.** Permalink changed to `marketing-costs`, with a 301 from `/seven-cost-layers/`. Added to the blog page the same day.

Search Console: 246 impressions on the old post, all for off-topic searches like "sales layer cost" and "layer cost", so there's no useful traffic to protect. The old post was built on the retired "seven cost layers" framing. This is a brand-new post on a real search term, **marketing costs**. The words "seven", "layer" and "layers" appear nowhere on the page.

## Where to find it
Posts → search "seven" (the old post). Delete the old content, paste in the contents of `seven-cost-layers.html` (or the `-copy-paste.txt` copy), and keep **Elementor Canvas**. Change the post title in WordPress to the H1 below.

## Before you paste
1. Upload `images/marketing-costs-10000-ad-spend-example.png` to Media.
   - Alt text: `Marketing costs example: $10,000 in ad spend and a 3.0 ROAS look like $20,000 of profit, but after every cost the campaign keeps $7,100`
   - Expected URL: `https://alloceraintelligence.com/wp-content/uploads/2026/09/marketing-costs-10000-ad-spend-example.png`. The page already points here. If WordPress gives it a different URL, tell me and I'll update the page.
2. Set it as the Featured and Social image.

## Rank Math fields
| Field | Value |
|---|---|
| Post title / H1 | `Marketing Costs: What $10,000 in Ad Spend Really Costs You` |
| Focus Keyword | `marketing costs` |
| Secondary keywords | `costs of marketing, examples of marketing costs, what are marketing costs, marketing campaign costs` |
| SEO Title (54 chars) | `Marketing Costs: What $10,000 in Ad Spend Really Costs` (keyword first, with a number, which lifted the last page from 79 to 82) |
| Permalink | `marketing-costs` (**Nick chose to change it**; add the 301 below) |
| Meta Description (146 chars) | `Marketing costs go far beyond ad spend. See the full list, a $10,000 worked example, and how to count every cost per campaign to find real profit.` |
| Schema | Article → Blog Post |

**Keyword choice:** "marketing costs" gets about 260 US searches a month, with low competition and a high ad value (about $22 per click). The top Google results are budget guides, so this page answers the budget question too, then goes further: the costs a budget guide leaves out.

**Expected score:** low-to-mid 80s. The keyword can't be in the permalink while we keep `seven-cost-layers`, and here the old slug actually works against the page because it names the retired idea. **Recommended, your call:** change the permalink to `marketing-costs` and add a 301 from `/seven-cost-layers/`. The old URL's impressions are all off-topic, so there's nothing to lose, and it should push the score toward 90.

## Redirect (after you change the permalink)
Go to **Rank Math → Redirections → Add New**:
- Source URL: `seven-cost-layers`
- Destination URL: `https://alloceraintelligence.com/marketing-costs/`
- Redirection Type: **301 Permanent Move**
- Click **Add Redirection**.

No other rebuilt page links to `/seven-cost-layers/`, so no links need fixing. **To do after the score:** add this post and the 30-Day Retest to the blog page (neither is listed there yet).

## Checks
- **Size:** about 2,100 words. The keyword appears 26 times (~1.2%), including in the H1, the first sentence, the SEO title, the description, the image alt text, and two H2s.
- **Structure:** 9 H2 sections plus the final CTA, a table of contents, key takeaways, a costs table, a worked example (table + image), 8 steps and 6 FAQs.
- **Links:** 11 internal links, to rebuilt pages only:
  - contribution margin (guide + calculator)
  - net marketing contribution
  - scale/hold/cut/pause framework
  - cost per signed case
  - 30-day retest
  - Triple Whale vs Rockerbox vs Allocera
  - validation report, How It Works, pricing, blog and Get Started
- **5 external links**, all seen live in Google's results on Sept 27:
  - Mercury: "most small businesses can plan to spend between 5% and 20% of revenue on marketing"
  - BDC: "B2B companies should spend between 2 and 5% of their revenue on marketing", with B2C often higher
  - Stripe pricing: 2.9% + 30¢ per successful US online card payment
  - Stripe's Chargebacks 101: "There is a $15 fee for each chargeback" (the pricing page also lists "Dispute received fee $15.00")
  - WebFX digital marketing pricing: linked as a reference only, no numbers quoted
- **Tracking:** the same GA4 script as the 30-Day Retest. It uses the same GA4 ID and loads GA4 only if the site doesn't already. It records:
  - Get Started, pricing and validation-report clicks
  - internal and outbound links
  - table-of-contents clicks and FAQ opens
  - scroll depth and which sections are read

  No personal data is sent.
- **Layout:** renders at desktop (1280) and phone (390) with no sideways scrolling and 0 script errors. The example table fits a phone screen without scrolling.
- **Byline:** no date. The title has no year.

## Every claim, and where it's proven
| Claim | Source |
|---|---|
| The worked example ($30,000 revenue, $22,900 costs, $7,100 = 23.7%) | Labeled "illustrative, not client data" on the page and in the image. Arithmetic checked: 10,000 + 1,500 + 900 + 1,200 + 300 + 9,000 = 22,900. 13,900 ÷ 10,000 = 1.39. |
| 5% to 20% of revenue | Mercury (quoted from its own text in Google's results) |
| 2% to 5% for B2B, often more for B2C | BDC (same) |
| Stripe 2.9% + 30¢; $15 per dispute | stripe.com pricing and Chargebacks 101 (same) |
| What CDAI subtracts: ad spend, fees, partner payouts, refunds, chargebacks, compliance costs and operating costs you add | Engine true-cost formula; the same sentence already runs on the contribution margin and net marketing contribution pages |
| Rechecks its math, stops on bad data, grades past decisions, advisory only | Control Tower math check; health gate; `score_mature_directives`; engine `CLAUDE.md` |
| 89.5% (1,210/1,352), 9 businesses, 7 industries, math matched 100% two ways | The validation report; same wording as the other rebuilt pages |

**Kept out on purpose:**
- any "N costs" or "layers" framing
- any claim that CDAI never assumes a cost (the fee fix, F5, isn't merged yet)
- agency fee percentages (none from a primary source)
- any unsourced industry averages

**One thing to know:** the page advises readers to use real fees rather than guesses. That's general advice, not a claim about CDAI. Once F5 is merged, CDAI matches it exactly; until then, live CDAI still uses a default fee for some CRM sources.

## Removed from the old post
The whole old post is replaced:
- the "seven cost layers" framing throughout
- the old pasted `<head>` and second `<title>`
