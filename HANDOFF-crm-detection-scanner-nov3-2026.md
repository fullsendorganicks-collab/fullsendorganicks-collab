# Handoff: HubSpot/Salesforce Detection Scanner (Nov 3, 2026)

**Status: built, tested, delivered to Nick as a file. Not part of the CDAI engine codebase — a separate, standalone outreach/lead-gen tool for Nick's own prospecting.**

## What this is

A public-surface scanner that checks whether a company's website shows any public
evidence of using HubSpot or Salesforce — for Nick's own cold-outreach prospecting
(target market: established 40+-year-old companies in West Palm Beach / Palm Beach
Gardens / Jupiter FL). It is a plain Python script, not part of the CDAI product and
not deployed anywhere — it runs locally wherever Nick puts it.

File delivered to Nick directly (not committed to any repo, per his own file-delivery
preference during the build): `scanner_final.py`, version `14.0.0`, 4,546 lines.

## Why this exists

Nick wanted a free alternative to paid "is this company using HubSpot/Salesforce"
tools (origami.chat, Heeet.io, Wappalyzer, BuiltWith), plus local-business discovery
so he isn't the only one supplying target lists, plus a way to turn vendor
testimonial pages into qualified leads (a real person who publicly says "I'm the
Salesforce Administrator at X").

## What it does (evidence tiers, strongest to weakest — never a binary yes/no)

1. **DIRECT_PUBLIC_INTEGRATION_FOUND** — live HubSpot/Salesforce script, form, or API call
2. **CORROBORATED_PUBLIC_PLATFORM_EVIDENCE** — 2+ independent strong indicators
3. **STRONG_PUBLIC_PLATFORM_SIGNAL** — one strong indicator
4. **JOB_POSTING_SIGNAL_FOUND** — the company's own careers page names the platform as a required/preferred skill (this is what caught the one real company — wrightsimpactwindowanddoor.com — that confirmed Salesforce directly to Nick but showed zero script/DNS/GTM evidence)
5. **SUPPORTING_SIGNAL_ONLY** — weak/generic marker, needs manual check
6. **NOT_OBSERVED** — never printed as "doesn't use it," only "no public evidence found"

Plus: DNS evidence (with a DNS-over-HTTPS fallback for restrictive networks), Google
Tag Manager inspection, ecosystem detection (Pardot, Marketing Cloud, Experience
Cloud, Improveit 360), free OpenStreetMap-based local business discovery, testimonial
lead extraction (finds a named person on a vendor's own testimonial/case-study page
who self-identifies as using the platform — e.g. "Jordan Doe, Salesforce
Administrator"), review-markup intelligence (reads a scanned company's own embedded
review/rating markup and its own outbound links to review platforms — never fetches
a third-party review site directly), and a JS-challenge analyzer that only ever
inspects a script a page explicitly marks as its own (inert on every real
third-party site).

## What it deliberately does NOT do, and why

- **Never scrapes G2, Capterra, or TrustRadius.** Checked their actual Terms of Use
  directly (Nov 3, 2026): G2's ToS explicitly prohibits automated extraction of
  reviews and reviewer identities, citing recent case law as binding on automated
  agents. TrustRadius backs this with an active Cloudflare bot-wall. This was Nick's
  own idea initially (he'd seen tools that pull from these sites) and was explicitly
  declined after checking, with the reasoning given to him directly.
- **Never scrapes Google or Facebook reviews** — same reasoning, those platforms'
  own terms prohibit it.
- **Never attempts to defeat a real anti-bot wall** (Cloudflare, DataDome, Akamai,
  Imperva). It only detects and reports one; a human operator may optionally clear
  it themselves in a visible browser window with `--interactive-challenges`.
- **Never automates a LinkedIn lookup.** A testimonial lead gives a name/title/company;
  finding their LinkedIn profile is a deliberate manual step, by design.

## Engineering record

- **8 real bugs found by code review and fixed, each with a test:** an SSRF gap in
  the redirect-following logic (no private-IP/metadata-endpoint protection), a
  NameError in the browser event-capture path, imprecise career-page evidence
  (no negative-context filtering, no stale-listing handling), cross-testimonial-card
  name/title misattribution, an incomplete robots.txt parser (no Allow-overrides-
  Disallow precedence), sitemap indexes not recursively followed, duplicate-signal
  double-counting in the confidence scoring, and incomplete batch-worker cleanup on
  interrupt.
- **One more bug found live during final testing** (after merging Nick's own
  additional build): the review-link classifier matched any `google.com` link,
  including a Google Play Store app-store page — fixed to only match actual Google
  review-profile links (`g.page`, `google.com/maps/place/...`).
- **Final state: 36/36 offline self-tests pass; 3/3 live regression checks pass**
  against real companies with independently-confirmed answers (hedrickbrothers.com →
  HubSpot direct integration; relatedross.com → Salesforce SPF record; 
  wrightsimpactwindowanddoor.com → Salesforce via the job-posting-only path, the one
  real case nothing else could catch).

## Known limitations (told to Nick directly)

- Local-business discovery (OpenStreetMap Overpass) and the headless-Chromium browser
  layer could not be live-tested from the cloud sandbox this was built in — both are
  blocked by that sandbox's own network policy, not a code defect. Confirmed working
  on an ordinary machine once the Python dependencies are installed
  (`pip install requests dnspython playwright beautifulsoup4 && python -m playwright
  install chromium`).
- A public scanner can never certainly confirm a *private* CRM — the honest ceiling
  is evidence tiers, never a yes/no, and this is stated explicitly in every report.
