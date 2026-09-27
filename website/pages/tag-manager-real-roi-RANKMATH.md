# Rank Math box: /tag-manager-real-roi/ → new Offline Conversion Tracking post

**LIVE Sept 27: score 80, slug kept (`tag-manager-real-roi`).** The main gap is the keyword not being in the permalink.

**What this replaces:** "Why Tag Manager Will Never Show You Real ROI". The old post carried:
- the fake 80%
- "seven cost layers"
- "30–70%" and 13 other unsourced stats
- a pasted `<head>`
- a dated byline

This is a new post that keeps the useful idea (Tag Manager can't see what happens after the lead) and aims it at a search term buyers actually use.

## Why this topic (live data, Sept 27)
- **Your Search Console:**
  - `/tag-manager-real-roi/`: 4 impressions in the last 28 days, and none that Search Console could tie to a query in 6 months. There's nothing to protect.
  - Its duplicate `/30-day-retest-methodology-2/`: 0.
- **Your GA4 (3 months):** 5 visits landed on it, with 20% engagement.
- **Keyword options checked:**

  | Keyword | Searches/mo | Ad value | Competition | Verdict |
  |---|---|---|---|---|
  | what is google tag manager | 2,900 | ~$13 | Low | Google's own pages, Semrush and Reddit hold the top spots, and searchers are mostly beginners, not buyers. |
  | google tag manager conversion tracking | 20 | — | — | Too small. |
  | offline conversion tracking (+ google ads offline conversions, track offline conversions, meta offline conversions…) | ~400 combined | top bids up to $42/click | Low | **Chosen.** |

- **Why "offline conversion tracking":** the searchers are lead-driven businesses trying to connect ad clicks to closed deals in a CRM. That is the exact customer for CDAI, and the article ends on the one thing offline tracking can't do: show profit.
- **Google today:** the results are tool vendors (Stape, LeadsBridge, KlientBoost) and Google's help page. None explains the limit (revenue ≠ profit).
- **People Also Ask:** Meta's Conversions API questions. Several ranking guides still describe Meta's Offline Conversions API, which was discontinued in May 2025. This page states the current setup.

## Where to find it
Posts → search "Tag Manager". Delete the old content, paste in `tag-manager-real-roi.html` (or the `-copy-paste.txt` copy), and keep **Elementor Canvas**. Change the WordPress title to the H1 below.

## Before you paste
1. Upload `images/offline-conversion-tracking-click-to-closed-deal.png` to Media.
   - Alt text: `Offline conversion tracking flow: ad click, form or call captured with click ID, CRM stages from lead to closed deal, result sent back to the ad platform, then a profit check for refunds, payouts and delivery costs`
   - Expected URL: `https://alloceraintelligence.com/wp-content/uploads/2026/09/offline-conversion-tracking-click-to-closed-deal.png`
2. Set it as the Featured and Social image.

## Rank Math fields
| Field | Value |
|---|---|
| Post title / H1 | `Offline Conversion Tracking: Connect Ad Clicks to Closed Revenue` |
| Focus Keyword | `offline conversion tracking` |
| Secondary keywords | `google ads offline conversions, track offline conversions, meta offline conversions, google tag manager` |
| SEO Title (55 chars) | `Offline Conversion Tracking: 5 Steps From Click to Deal` |
| Permalink | `tag-manager-real-roi` (original slug, per the rule). **Recommended, your call:** `offline-conversion-tracking` + the redirects below. |
| Meta Description (158 chars) | `Offline conversion tracking connects ad clicks to the deals you close in your CRM. Set it up in 5 steps for Google Ads and Meta, and see what it still misses.` |
| Schema | Article → Blog Post |

**About the slug:** keeping `tag-manager-real-roi` costs points because the keyword isn't in the URL. The last two slug changes went to 89 and 90. The old URL has almost no search history.

## Redirects (added to `website/REDIRECTS.md`)
- **R5, needed either way:** `/30-day-retest-methodology-2/` is an exact copy of this old post (and carries the fake 80%).
  - Source `30-day-retest-methodology-2`
  - Destination: this post's final URL (`/tag-manager-real-roi/`, or `/offline-conversion-tracking/` if you change the slug)
  - Then trash or unpublish the duplicate post.
- **R6, only if you change the slug:**
  - Source `tag-manager-real-roi`
  - Destination `https://alloceraintelligence.com/offline-conversion-tracking/`
- **Links:** the blog page links to `/tag-manager-real-roi/` (tracked in the blog to-do). No rebuilt page links to it.

## Checks
- **Size:** about 2,100 words. "Offline conversion tracking" appears 20 times (~1%), including in the H1, the first sentence, three H2s, the SEO title, the description and the alt text. "Offline conversions" appears 14 times; "Tag Manager" 11 times.
- **Structure:** 9 H2 sections + the final CTA, table of contents, key takeaways, 5 numbered steps, 2 comparison tables, a flow image, 6 FAQs.
- **Links:** 11 internal links to rebuilt, live pages:
  - ROAS calculator
  - marketing costs
  - contribution margin calculator
  - scale/hold/cut/pause framework
  - 30-day retest
  - cost per signed case
  - net marketing contribution
  - validation report, How It Works, pricing, Get Started
- **5 external links**, each seen live in Google's results on Sept 27:

  | Source | What it confirms |
  |---|---|
  | Google Ads Help: About offline conversion imports | "save these IDs along with whatever lead information you collect" |
  | Google Tag Manager developer docs | "a tag management system that lets you configure and deploy tags on your website or mobile app" |
  | Google Ads community (enhanced conversions for leads) | "send hashed lead information to Google at the time of the form submission" |
  | Meta developer community | "Offline Conversions API will be discontinued in May 2025" |
  | Stape | offline conversions = "conversions made by phone, in-store orders, offline deals" |

- **Tracking:** the same GA4 script as the other rebuilt pages.
- **Layout:** renders at desktop (1280) and phone (390) with no sideways page scrolling and 0 script errors. The 3-column tables swipe sideways inside their box on phones, the same as the other pages.
- **Byline and title:** no date, no year. The one date in the body ("May 2025") is a sourced fact about Meta.

## Every claim, and where it's proven
| Claim | Source |
|---|---|
| Save the click ID (GCLID) with the lead | Google Ads Help (linked) |
| What Tag Manager is | Google developer docs (linked) |
| Enhanced conversions for leads sends hashed data at form submission | Google Ads community answer (linked); Google's own AI overview cites Google Ads Help 15713840 for the same |
| Meta's Offline Conversions API discontinued May 2025; events now via the Conversions API | Meta developer community (linked); several ranking guides say the same |
| Tag Manager can't see CRM events; offline tracking reports revenue, not profit | How the tools work, as explained on the page (no statistics claimed) |
| What CDAI does; nothing changes in ad accounts unless a person acts | Same approved wording as the other rebuilt pages; engine is advisory (`CLAUDE.md`) |
| 89.5% (1,210/1,352), 9 businesses, 7 industries, math 100% two ways | The validation report |

**Kept out on purpose:**
- the old post's "30–70% gap" and every other unsourced number
- any claim that CDAI uploads conversions to ad platforms (it doesn't)
- any claim about specific CRM integrations beyond "the tools you already use"
- the "90-day" import window, which I couldn't confirm live
- any "layers" framing

## Removed from the old post
- the fake "80%" and "directive accuracy" framing (on the duplicate)
- "seven cost layers" / "cost layers"
- "30–70% structural gap" and 13 other unsourced stats
- "cannot" claims about named tools
- the "June 2, 2026" byline date
- the pasted `<head>`
