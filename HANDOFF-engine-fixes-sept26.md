# HANDOFF: engine fixes from the Sept 26 cloud session (read this first)

_Written Sept 26, 2026, end of the cloud session. For the next Claude Code session (local or cloud)._

**Status in one line:** 12 fixes are built, tested locally and pushed as branches. **Nothing is merged, deployed or applied to the database.** Nick approves each item before anything goes live.

Nick's approval sheet (private artifact): https://claude.ai/artifact/3hNXn12DXcbCd5Q8Nj3EyB
Engine blueprint (the findings these fix): https://claude.ai/artifact/FDddft2fX8cQiS9dsHjN9S

---

## 0. Do this first: two sessions built overlapping fixes

While this cloud session worked, the local session opened **cdai-engine PR #37** (`fix/blueprint-findings-sept26`). It covers F1/F2 (Meta only), F4 (engine side only), F6 and the Google success redirect.

The cloud branches below cover those same items and more:
- Google and LinkedIn account setup, not just Meta
- account pickers with one-time links
- a nightly retry of unfinished history pulls
- HubSpot, Salesforce and CallRail history pulls
- the portal UI for the industry field and connect results
- the reconnect-after-expiry fix

**They conflict. Merge one set, never both.**

| Overlapping item | PR #37 | Cloud branch |
|---|---|---|
| F6: test orgs out of nightly | yes (`get_paid_orgs` only) | `fix/nightly-skip-test-orgs` (also API sync, outcome scoring, custom digests; env switch `CDAI_NIGHTLY_INCLUDE_TEST_ORGS`) |
| F1/F2: connect configures account + history pull | Meta only, multi-account stored for a future picker | `feat/sync-on-connect`: Meta, Google, LinkedIn with pickers; history pull for Meta/Google/LinkedIn/HubSpot/Salesforce/CallRail; nightly finishes an interrupted pull |
| F4: industry at signup | engine only (checkout metadata to onboarding) | `feat/industry-at-signup` (engine + `/settings/industry`) + portal branch UI |
| F9: Google redirect | success only | every outcome, including denied and no-accounts |

**Recommendation (cloud session's view; Nick decides):** use the cloud branches and close PR #37 unmerged, **but first** use the local session's live `.env` to run what the cloud couldn't:
1. Check out `integration/all-fixes-sept26` in a worktree (never touch the `feat/tiered-rate-limits` WIP checkout).
2. Run `python cdai_test_suite.py` against the live DB (skip nothing but section 3C, which writes to Demo). The PR #37 baseline was 66/66.
3. Run each new `test_*.py` listed in section 3. They use a throwaway local Postgres, so they're safe anywhere.
4. Report to Nick. If the local session prefers PR #37's approach for any item, say so with the reason.

---

## 1. What was built (each its own branch, all pushed)

Repo `fullsendorganicks-collab/cdai-engine`. Every branch is off `main` at `6d0be90`. Main has since gained one docs-only commit (`4761d98`), and every branch still merges cleanly.

| # | Branch | What it fixes | New test (checks) | Moves validated numbers? |
|---|---|---|---|---|
| S1 | `security/views-invoker` | **CRITICAL, live now:** `vw_contribution_margin_v2` and `vw_true_cost_recent30d` lack `security_invoker` and are SELECT-granted to anon. Anyone with the public anon key (it's in the portal JS) can read every org's campaign names, revenue and costs. Verified read-only: as anon, 69 rows across 10 orgs. The fix is a migration: `security_invoker = true` + revoke anon. | `test_views_no_cross_client_leak.py` (7) | No |
| S2 | `security/clients-read-only` | Every engine table's `org_isolation` policy was FOR ALL, so a logged-in client could insert, edit or delete their own org's spend, directives, outcomes, health and settings, and could read their own stored OAuth tokens. The migration makes it SELECT-only, revokes client writes, and hides token secret columns. The portal writes nothing directly (verified). | `test_clients_read_only.py` (15) | No |
| F6 | `fix/nightly-skip-test-orgs` | [SIM] orgs out of the nightly job | `test_nightly_skips_test_orgs.py` (9) | No |
| F1+F2 | `feat/sync-on-connect` | New `ad_connect.py`. Meta/Google/LinkedIn connect writes `api_sync_config.<platform>` and starts a background history pull, window = max(org lookback, 56 days for decay's 8 weeks). State lives in `api_sync_config.backfill`; the nightly finishes pending/failed pulls; advisory lock. Also: Meta account discovery + picker; one-time nonce on all 3 pickers; names escaped; Meta/HubSpot reconnect now sets `is_active = TRUE` (an expired token stayed inactive forever). | `test_sync_on_connect.py` (45) | No |
| F4 | `feat/industry-at-signup` (stacked on F1) | Checkout carries `vertical`; the webhook fills it only if empty; `GET/POST /settings/industry` (Supabase session auth); a longer window re-pulls history. | `test_industry_at_signup.py` (15) | No |
| F3 | `feat/dashboard-engine-numbers` | New table `campaign_metrics_snapshots` + `get_engine_metrics()`. The engine saves the exact CampaignMetrics each cycle, via a 4-line additive hook in `run_directive_cycle_with_gates`: own connection, never raises. Example: the dashboard showed −100%, the engine decided on 25%. | `test_dashboard_engine_numbers.py` (12) | No |
| D1 | `fix/digest-weekly-latest` | Digest bug: it took the 10 highest-priority directive rows ever (no date filter, no latest-per-campaign), so it could show old or duplicate calls. Now: current directive per active campaign; weekly (Monday, `DIGEST_WEEKDAY`) + same-night alert for a new PAUSE/QUARANTINE/CUT/FLAG; `DIGEST_CADENCE=daily` reverts; the "7-cost" wording is removed. | `test_digest_current_weekly.py` (13) | No |
| F9a | `fix/reconnect-reminders` | New `token_expiry.py`: emails the client 7 days, 1 day and 0 days before a Meta login (or LinkedIn without a refresh token) expires. Skips Apex (digest paused), SIM orgs and self-renewing logins. | `test_reconnect_reminders.py` (8) | No |
| F9b | `fix/store-audit-reports` | New `report_store.py` + `audit_reports` table: the nightly narrative + PDF were written to the cron's discarded disk. Keeps the last 30 per org. | `test_store_audit_reports.py` (6) | No |
| F5 | `fix/no-assumed-costs` | HubSpot/Salesforce/Ringba 7% fee → 0 unless configured. Stripe uses the exact per-charge fee (`expand=["data.balance_transaction"]`). No $0.25 compliance cost; no CSV 2.9–3% platform fee. Boberdoo lead price recorded as a payout (counts in true cost). Ringba payouts kept with a default partner. | `test_no_assumed_costs.py` (14) | **Yes, slightly.** Read-only estimate: at most 3 of 1,352 validated decisions change (CUTs lifted above 10%). **Hold until the validation re-run** (the SIM mock Stripe server must support `expand`). |
| — | `integration/all-fixes-sept26` | All 10 merged together, for test runs only. **Never merge this branch itself.** | all | — |

Portal repo `fullsendorganicks-collab/cdai-portal`, branch `feat/engine-numbers-industry-connect`:
- margin panels read `get_engine_metrics`, falling back to `get_cm_data_v2` labeled "Preliminary"
- industry picker at signup and in the dashboard
- connect-result banner

It needs the engine F1, F4 and F3 branches (plus the F3 migration) live first.

**Scale of change, excluding tests:** `directive_engine.py` +4 lines (snapshot hook only). Classification rules, thresholds, stability gate, grading and attribution are unchanged. The largest change is the connect flow (`ad_connect.py` + callbacks).

---

## 2. Deploy order (only after Nick approves each item)

1. S1 migration, then S2 migration (apply to Supabase; both idempotent, rollback SQL in the files).
2. Merge engine branches: F6 → F1+F2 → F4 → F3 → D1 → F9a → F9b. Render auto-deploys on merge to main.
3. Apply the F3 and F9b table migrations (order vs deploy doesn't matter: the code carries on if a table is missing).
4. Merge the portal branch (Vercel deploys on merge).
5. Live checks: the full suite once (skip 3C); a supervised connect test with an ad account and HubSpot account Nick controls. Meta's `me/adaccounts` fields came from the docs; the sandbox can't reach Meta.
6. F5 last, after the validation re-run.

`scheduler.py` is touched by F6, F1, D1 and F9a. They merge cleanly in the order above (verified by the integration branch).

---

## 3. Test evidence (cloud session, Sept 26)

- Test harness: `local_test_pg.py` + `local_test_schema.sql` (production columns, defaults and unique indexes, copied read-only) start a throwaway local Postgres per test. They're identical on every branch.
- **144 new checks pass** on the integration branch. Each new test was also run against `main` and fails there (it proves the bug).
- **Existing tests:** every existing `test_*.py` gives the identical result on `main` and on the integration branch.
- **Needs the live environment on both:** `test_duplicate_email_onboarding_race`, `test_hubspot_no_shared_fallback`, `test_phase2_webhook_security` and `test_unauthenticated_rate_limit` (real Supabase Auth); `test_meta_sync` and `test_webhook` (live network); `test_upload` (a Windows file path); `test_google_sync` (pytest not installed).
- `test_validation_harness_fixes` is 21/22 on both. The 1 failure is its own fixture inserting `payout_events` with a NULL `partner_id` (NOT NULL in production).
- **`cdai_test_suite.py` on a local DB:** 22 pass / 5 fail / 15 skip, identical on both except the intended fee line (7% → 0). The 5 failures need live Stripe, Supabase Auth or real campaigns; the 15 skips need platform credentials. **The live run is the local session's job (section 0).**

---

## 4. Found, not built (Nick decides)

- **Reactivated campaigns mix in pre-pause data.** `fetch_campaign_metrics()` computes each campaign's `_get_effective_since()` but queries with `batch_since = min(...)`, which is always the plain window. So the reactivation floor never applies. `CLAUDE.md` claims otherwise; no public page or chat script does. Fixing it changes decision math, so it needs Nick's yes and a validation re-run.
- **OAuth `/authorize?org_id=` is unauthenticated.** Anyone who knows an org UUID can attach their own ad account to that org. Needs a design choice (a signed session from the portal).
- **Secret in a repo:** `cdai-admin-backend/README.md` line 8 has a Supabase secret key in plain text. Nick rotates it and removes it from the file. Don't repeat the key anywhere.
- `vw_contribution_margin_v2` drops revenue after an org's last cost date. This is moot once F3 is live.
- Boberdoo per-campaign split: needs Boberdoo's real campaign field name. Don't guess it.

## 5. Nick-only actions

- Render: `allocera-control-tower` schedule `1 2 * * *` → `0 11 * * *` (F7). Keep `cdai-daily-health` suspended or move it too.
- Render: delete or suspend the 19 old validation crons (F8).
- **Reconnect Apex's Meta login before Oct 10, 2026** (its token expires then; Apex is kept connected for working keys).
- Rotate keys: Anthropic, the Supabase service key, the key in the admin README, and the hardcoded DB password.

## 6. Nick's decisions made this session

- F5: build + impact report, hold for the validation re-run.
- SIM orgs: exclude from nightly with a switch.
- Digest: he asked what's best for retainer clients. Answer: weekly + urgent alerts, reversible by env var.
- Backfill window: derived from the engine's own windows (not a new judgment).
- He was worried the engine's architecture was being changed. Keep repeating the facts: decision rules untouched, one 4-line additive hook, everything else plumbing, one branch per item.
- He wants: approve item by item, leave the engine alone after approval, then finish the website, then the rest of the list one at a time.

## 7. Standing rules (unchanged, from engine `CLAUDE.md`)

- Never touch Apex or Demo data or keys; test only on [SIM] or throwaway orgs.
- Don't touch the `feat/tiered-rate-limits` WIP.
- Nick's permission is required before any merge, deploy or database change.
- Plain language; prove every claim.
