# Rank Math box: /30-day-retest-methodology/

## Sept 28 restore: this post moves into post 252

**What happened:** the Lead Quality post was pasted into post **245**, which is where this post lived. Post 245 is now `/lead-quality/` (score 83). This post (score 82) isn't live anywhere right now. 7 rebuilt pages link to `/30-day-retest-methodology/`:
- marketing costs
- ROAS calculator
- offline conversion tracking
- Salesforce campaign influence
- true CAC
- lead quality
- the blog file

Search Console's 38 impressions are on that URL too.

**The fix (nothing is deleted, no content changes):** paste this post into **post 252** and give it back its original slug.

1. **Rank Math → Redirections first.** If there's a redirect with source `30-day-retest-methodology` (Rank Math can create one automatically when a slug changes), **delete it**. Otherwise it sends visitors to Lead Quality instead of this post.
2. Open `alloceraintelligence.com/wp-admin/post.php?post=252&action=edit`. Delete the old content (the leftover Tag Manager copy), paste in `30-day-retest-methodology.html` (or the `-copy-paste.txt` copy), and keep **Elementor Canvas**.
3. WordPress title: `Marketing Measurement That Grades Its Own Decisions: The 30-Day Retest`
4. **Permalink: change `30-day-retest-methodology-2` to `30-day-retest-methodology`.** It's free now that post 245 is `lead-quality`.
5. **Featured and Social image:** `30-day-retest-marketing-measurement-timeline.png`. It should already be in Media, so upload it only if it's missing.
6. Rank Math fields: use the table below (same as before).
7. **Old fields to delete on post 252:**
   - SEO title "Directive Accuracy: 30-Day Retest Beats Gut-Feel"
   - focus keyword "directive accuracy"
   - the old description with "80% accuracy"
8. **Add the 301** from `30-day-retest-methodology-2` to `https://alloceraintelligence.com/30-day-retest-methodology/` (R11 in `website/REDIRECTS.md`).
9. **Quick test:**
   - `/30-day-retest-methodology/` should open this post, not Lead Quality.
   - `/lead-quality/` should open Lead Quality.
   - `/30-day-retest-methodology-2/` should land on this post.

---

Search Console (last 3 months): 11 impressions, 0 clicks, average position 9.2, all for "allocera intelligence". The old page carried the retired 80% claim, "seven cost layers", an unsourced "60–70% industry accuracy" stat, and a dated byline. This rebuild targets a real search term and is built around the validation.

## Where to find it
Posts → search "retest" (the old title starts "The 30-Day Retest"). Delete the old content and paste in the contents of `30-day-retest-methodology.html`. Keep **Elementor Canvas**.

## Before you paste
1. Upload `images/30-day-retest-marketing-measurement-timeline.png` to Media.
   - Alt text: `Marketing measurement timeline: a decision is recorded, its window plays out, then margin before and after is compared and the call is graded`
   - Expected URL: `https://alloceraintelligence.com/wp-content/uploads/2026/09/30-day-retest-marketing-measurement-timeline.png` (the page already points here; if WordPress gives it a different URL, tell me and I'll update the page).
2. Set it as the Featured and Social image.

## Rank Math fields
| Field | Value |
|---|---|
| Focus Keyword | `marketing measurement` |
| Secondary keywords | `30-day retest, marketing decision accuracy, measure marketing effectiveness, marketing attribution` |
| SEO Title (57 chars) | `Marketing Measurement: Grading 8 Decisions Against Profit` (v2 after the first score of 79; adds a number) |
| Permalink | `30-day-retest-methodology` (the original slug; in post 252 it must be changed from `-2`, see step 4) |
| Meta Description (142 chars) | `Most marketing measurement never checks its own calls. See how CDAI grades every decision against real profit, and the 89.5% validated result.` |
| Schema | Article → Blog Post |

**Keyword choice:** "marketing measurement" gets about 170 US searches a month, with a high ad value (about $46 per click), and the page answers it honestly. "Incrementality testing" gets more searches, but it's a different method CDAI doesn't use, so the page explains the difference instead of targeting it.

**Score: 82 (Sept 27).** 79 on the first paste, 82 after the v2 title (added a number). The remaining gap is the keyword not being in the permalink (we kept the original slug). Optional, Nick's call: change the permalink to `marketing-measurement` + a 301 from the old URL (the old URL has only 11 impressions).

**Original score note:** Rank Math will dock a few points because the keyword isn't in the permalink. We keep the original slug (the rule), so expect the high 80s rather than 90+.

## Checks
- **Size:** about 2,480 words. The keyword appears 17 times (~1.4%), including in the H1, the first sentence, two H2s, the image alt text, the title and the description.
- **Structure:** 11 H2s, a table of contents, key takeaways, 6 FAQs.
- **Links:** 16 internal links to rebuilt pages only: the scale/hold/cut framework, contribution margin, net marketing contribution, cost per signed case, the Triple Whale and Northbeam comparisons, the validation report, How It Works, pricing and the blog.
- **5 external links**, all seen live in Google's results for "marketing measurement" on Sept 26:
  - BCG
  - Supermetrics
  - SAS
  - Funnel
  - Nielsen
- **Tracking:** the page includes the GA4 tracking (same GA4 ID as the homepage, and it loads GA4 only if the site doesn't already). It records:
  - Get Started, pricing and validation-report clicks
  - internal and outbound links
  - table-of-contents clicks and FAQ opens
  - scroll depth and which sections are read

  No personal data is sent.
- **Layout:** renders at desktop (1280) and phone (390) with no sideways scrolling and 0 script errors.

## Every claim, and where it's proven
| Claim | Source |
|---|---|
| Every decision is stored with its numbers, confidence and reasons | `directive_engine.issue_directive()` (reason codes include the margin) |
| Graded correct, wrong or neutral, by each decision type's own rule | `directive_engine.measure_directive_outcome()` |
| Window = the industry's sales cycle (21/30/45/60/90/150 days) | `vertical_config.VERTICAL_CYCLE_DAYS`; also stated on the homepage |
| Graded automatically each night once the window has passed | `scheduler.score_mature_directives()` |
| Each grade is stored with its method version; old and new never blended | `directive_outcomes.methodology_version` |
| Flags are never counted wrong (82 neutral) | code (a flag is correct or neutral only) + the validation |
| Math rechecked nightly; bad data stops decisions; advisory only | Control Tower math check; health gate; engine `CLAUDE.md` |
| 89.5% (1,210/1,352) and the per-decision table; math 100%, checked two ways | the validation report; same wording as the other rebuilt pages |

**Kept out on purpose:** the exact grading thresholds (proprietary), any "guarantee", and any comparison accuracy figures for other tools (none could be sourced).

## Removed from the old page
- the fake "80 percent directive accuracy" (7 times on the old page)
- "seven-cost stack" (5 mentions)
- "60 to 70 percent directional accuracy" for attribution and MMM (no source)
- "none of them measure whether they were right" about named competitors
- "no human override" (a person decides on every call)
- the "June 5, 2026" byline date


## Image update (Sept 29)
The made-up chart image was removed; it now uses the real client portal screenshot already in Media.
- **Featured image:** `Client-portal-for-cdai-example.png` (nothing to upload)
- **Alt text:** `Marketing measurement in the CDAI client portal: every decision graded against the profit that followed`
