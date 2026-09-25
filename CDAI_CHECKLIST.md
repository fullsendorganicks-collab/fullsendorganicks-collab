# Allocera / CDAI: Working Checklist

Nick's running list. Claude keeps it current and checks items off as they ship.
Rule: nothing gets built until Nick has seen it and said yes.

_Last updated: Sept 25, 2026 (claims audit)_

## Done

- [x] Former cofounder removed from all engine email, the repo, and memory (merged Sept 25)
- [x] Chat agent and memory updated: no "7 cost layers", correct qualification rule, free audit kept, no "unproven" wording (merged Sept 25)
- [x] Homepage v1: empty-space bug fixed, real logos, duplicate-title fix, 4-field form, FAQ
- [x] Homepage v2 built: Apex appears only in the two reviews; the validation results lead in the hero.
- [x] Homepage v3: claims audit. Every claim traced to a source; three unprovable claims removed (newsletter cadence, "HOLD is its most common call", "live in about a day"). **Paste the latest `homepage-final.html`.**

## Now (in order)

- [x] Newsletter cadence: none yet. No issue has gone out; the signup is list-building. No frequency claim on the site.
- [x] Self-serve copy verified against the portal code: account ready seconds after payment, one-click connections, first directives on the next nightly run.
- [x] **Dashboard trust fix built and tested** (`cdai-portal` branch `fix/honest-preliminary-dashboard`): no invented directives before the first run, no default HOLD, legend matches the engine. **Nick merges → Vercel deploys to production.**
0. [ ] **Optional: run the first sync right after connecting**, so new users see their numbers the same day instead of waiting for 2 AM UTC. The engine already has `/sync/*` endpoints. Needs Nick's yes.
0. [ ] **Name the chat agent:** Nick picks. Research and options are in the chat.
0. [ ] **Chat agent full claims audit:** trace every price, timeframe, and number in its prompt to a source, the same way the homepage was checked.

1. [ ] **AI links section (ChatGPT / Claude / Perplexity / Grok):** Nick decides whether to restore it. It doesn't affect rankings (see the Ideas section below). It can go back in within minutes.
2. [ ] **What the intake form should do now that self-serve is live:** Nick decides. Recommendation: it's the free audit request today. Once the free audit is in Stripe, it becomes a "Partner with us / talk to Nick" form for agencies and bigger accounts.
3. [ ] **Free Distortion Audit in Stripe:** add the product, wire checkout (`billing.py`), and add it to the pricing page.
4. [ ] **Homepage video, 90 seconds to 3 minutes:**
   - [ ] Agree on the script
   - [ ] Nick sends a screen recording of the portal, plus the logo and screenshots
   - [ ] Voiceover: Nick's own voice, or free text-to-speech in Clipchamp
   - [ ] Claude renders the motion-graphics cut (free, 1080p, no watermark)
   - [ ] Publish to YouTube and embed it on the homepage
5. [ ] **Rest of the site (51 URLs), one page at a time:** needs the WordPress export (Tools → Export → All content). Fix first:
   - [ ] `/55-directives-study/` (still says the debunked 80%)
   - [ ] Duplicate pages: `/true-cac/` + `-2`, `/30-day-retest-methodology/` + `-2`
   - [ ] 404 page (2nd most viewed page): turn on Rank Math's 404 monitor and redirect the dead links
   - [ ] Doubled titles: strip the pasted header from every page
   - [ ] `/proof/` is the Apex story. Decide whether to keep it, rewrite it around the validation, or remove it from the nav.

## Security (Nick)

- [ ] Rotate the Supabase database password. It's hardcoded in `run_full_directive.py` and `time_engine.py`, and the former cofounder may know it.
- [ ] Rotate other shared keys he could have seen (Resend, Stripe, Render)
- [ ] Check the team member lists in Render and Supabase
- [ ] Delete the 19 old validation cron jobs on Render (`cdai-validation-*`, `cdai-distressed-partner-*`, `cdai-full-revalidation-run1`, `cdai-onboard-remaining6`). Their schedules name a specific day (e.g. `42 20 23 9 *`), so they'll run again every Sept 23 on the paid starter plan.

## Ideas backlog: proposed, not approved

Evidence-backed ideas for a bootstrapped founder. Nick says yes or no to each one before any work starts.

- [ ] **YouTube channel.** Ahrefs' 75,000-brand study found YouTube mentions (title, transcript, description) are the strongest signal for AI visibility (0.737 correlation), about 3x backlinks. The homepage video doubles as the first upload. Cost: free.
- [ ] **Reddit presence** for Perplexity, which cites Reddit heavily (46.7% of citations in one 2026 study). Founder-voice answers in r/PPC, r/marketing, and r/smallbusiness.
- [ ] **Freshness:** content updated within 30 days gets about 3.2x more AI citations. Keep the blog/newsletter cadence and put visible dates on posts.
- [ ] **Organization + SoftwareApplication schema** (JSON-LD) on the homepage, so Google and AI search get clean facts about the company.
- [ ] **Check robots.txt** allows AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended).
- [ ] **Chat agent:** streaming replies, rules for handing off to Nick, weekly transcript review
- [ ] **Manuals:** remove "7 cost layers", "no self-serve", and the old acronym from all manuals
- [ ] **PageSpeed:** Nick runs pagespeed.web.dev (mobile) and sends the score
