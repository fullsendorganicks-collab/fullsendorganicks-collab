Add the Free Distortion Audit to self-serve signup and billing so it matches the homepage offer exactly.

WHAT THE HOMEPAGE PROMISES (source of truth, alloceraintelligence.com)
- The Free Distortion Audit is free: one campaign, 30-day lookback, no credit card, no commitment, and no consumer identity data needed.
- It runs one campaign through CDAI and shows the gap between what the dashboard reports and what was actually paid, with one decision for that campaign. Delivery is in 5–7 business days.
- Paid Distortion Audits start at $2,500. Retainers start at $1,500/mo.
- Paid audit fees credit 100% toward a retainer started within 30 days.

CURRENT STATE (verify it yourself before changing anything)
- In cdai-engine, billing.py has 7 paid price_keys (quick/standard/deep audit, plus starter/growth/scale/enterprise retainer), with LIVE_PRICING, TEST_PRICING, and a STRIPE_MODE switch.
- The billing.py docstring says the "Free Distortion Audit" tier "is being removed and is not handled here". That's out of date: the homepage offers it and it stays.
- The portal signup (cdai-portal, /signup/) is where the homepage "Get Started" button goes.

WHAT TO BUILD
1. Add a `free_audit` option to self-serve signup.
   - Stripe Checkout can't charge $0 in payment mode, so don't send free_audit through Checkout. Create the org and subscription directly with no card, using the existing audit tier unless a separate tier is clearly needed. Explain the choice.
   - Optionally, create a $0 "Free Distortion Audit" Product in Stripe for catalog records, test mode first.
2. Limit it to 1 campaign and a 30-day lookback in the engine for free_audit orgs. Limit it to one free audit per email and per company domain, and reject obvious throwaway emails.
3. Portal: show Free Distortion Audit first on /signup/, with the same wording as the homepage (free, 1 campaign, 30-day lookback, no credit card). Paid options stay as they are.
4. Upgrade path: after the free audit, the client can buy a paid audit or retainer through the existing Checkout flow.
5. Update the billing.py docstring and any docs or handoff notes that say the free audit is being removed.

FLAG TO NICK (don't decide it yourself)
- The live /pricing/ page says audit fees are "credited toward the first 90 days of any retainer started within 30 days". The homepage says "credit 100% toward a retainer started within 30 days". Ask Nick which is correct, and make any credit logic match his answer.
- The /pricing/ page text is being rebuilt in the website session. Don't edit WordPress. Just report any pricing mismatches you find.

HARD RULES
- The /home/user/cdai-engine checkout is on feat/tiered-rate-limits with uncommitted work in progress. Don't touch it. Do all work in a new git worktree branched from main.
- Use STRIPE_MODE=test and test prices only until Nick approves going live.
- Test only on [SIM] orgs. Never touch Apex or Demo data or keys. Don't run section 3C of cdai_test_suite.py against production.
- Never paste or print API keys in chat. New keys go only into Render env vars. Never use the hardcoded Supabase DB password. The old exposed Anthropic key is compromised; never use it.
- Never merge fix/chat-agent-scale-accuracy or merge/scale-fix-sept2026.
- Nothing on a public page may say "unproven" or "untested", and nothing may expose internal thresholds.

PROCESS
1. Read billing.py, the webhook, onboarding, and the portal signup. Then show Nick a short plan in plain language (what changes, which files, the free-audit limits) and wait for his yes.
2. Build it on the worktree branch. Add tests. Run them in test mode on [SIM] orgs only.
3. Show Nick the results. On his approval, open a PR. Don't merge or deploy without his yes.
4. Update the handoff and checklist notes when done.
