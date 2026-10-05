# STATE OF PLAY — Oct 5, 2026 (written ~01:25 UTC, replaces the status line and punch list further down)

_Everything in this section was verified by the session that wrote it; tags: [CODE] read in the repo, [DB] queried live (Supabase project
`cdaiwdebsdfgttntxyfp`), [RAN] executed with output, [RENDER] read through the Render MCP, [UNVERIFIED] not provable from here. The sections below
this one are the Oct 3-4 text, kept for history. Where they disagree with this section, this section wins._

## 0. One paragraph
Nick (solo founder, Allocera Intelligence / CDAI, ~3.5 years on a ~40k-line deterministic engine) must be able to stop building and sell by **Tuesday Oct 6, 2026**.
I hold a standing single-engineering-owner mandate (audit own work -> make the retest valid -> build what market readiness needs -> rerun -> rebuild every report
from the rerun -> merge plan). The Oct 4 validation was audited and found invalid in specific ways (below); the engine-side fixes and the new experiment are done,
tested and pushed; the retest's Render crons are configured and Nick has been sent his click list; **no retest cron had been triggered when this was written**
(check `list_events` with `cron_job_run_started` on the crons in §5). Nothing has been merged to `main`, and nothing may be without Nick's explicit approval.
His last instruction: handle everything that can be handled, make it pass the test suite, tell him what it takes -- "I'm done with gaps."

## 1. Phase status
| Phase | State |
|---|---|
| 1 Audit of my own Oct 4 work | DONE (13 findings, WORKLOG "Oct 4-5, 2026") |
| 2 Make the retest valid | DONE: evidence archived, run-tagged orgs, V1 mixed-clock fix, real-CRM time remap, real dev-CRM cleaner, no placeholder campaigns, UTM attribution model, simulated-clock scoring, 3 seeds, snapshot-sourced `report_figures.py` (tested). **Remaining: rewrite `simulation/run_full_report_data.py` as the tag-driven v3 collector (spec in §7).** |
| 3 items 1-7 (bounded windows, canonical metrics, evidence envelope, flagged-OFF shadow rules, finding B, FLAG subtypes, closed-loop value) | DONE, tested, mutation-checked, pushed at `bcc6820` |
| 3 item 8 reliability | IN PROGRESS on `validation/phase3-followups`: Google Ads adapter fixed + tested (3 real defects, §6). Still to do: Salesforce/HubSpot 5xx audit, missed-sync alerting, freshness already exists (`health_monitor`), parallel per-org scheduler plan (doc) |
| 3 item 9 integrations | NOT STARTED. Finding [CODE]: `scheduler.py` nightly wires HubSpot, Salesforce, Meta, Google, LinkedIn, CallRail ONLY. Bing, Ringba, Boberdoo, Stripe adapters exist but nothing in the nightly scheduler calls them -> wire with tests, or hide from signup. Plan Google Ads / Salesforce proofs |
| 3 item 10 platform access evidence (Meta tier / App Review, System User token path, Google dev-token level, LinkedIn MDP) | NOT STARTED; anything not provable from the repo or a live call is written down as [UNVERIFIED] |
| 3 item 11 load-test plan (100 orgs, $1M/mo) | NOT STARTED (plan + a local per-org cycle timing is feasible) |
| 3 item 12 `claims.json` generator feeding CLAUDE.md, `knowledge/cdai_facts.yaml`, website notes (retire Sept 24 set, 98.4%, Oct 4 figures) | NOT STARTED; needs the retest numbers |
| 3 item 13 decision ledger | WIP: `decision_ledger.py` + migration + rollback written. **NOT tested, NOT wired into `directive_engine.py`, migration NOT applied.** Spec: opt-in per org (`api_sync_config->>'decision_ledger'='on'`), flag-gated, failure-isolated, hash chain per org, append-only triggers |
| 4 Retest | Set up (§5). Checklist for Nick: `docs/RETEST-CHECKLIST-oct5.md`. Next: he clicks; I watch logs via the Render MCP |
| 5 Deliverables | NOT STARTED (list in §8) |
| Closing message ("Nick, you spent 3.5 years building this engine and.......") | NOT yet; only after everything is built, run, scored, verified and delivered (see section 6a further down) |

## 2. Branches, commits, and the push rule
* Engine repo: `fullsendorganicks-collab/cdai-engine` (local checkout `/home/user/cdai-engine`; the session's primary dir `/home/user/fullsendorganicks-collab` is a different repo).
* `validation/full-revalidation-sept-2026` -- **every retest cron deploys from it on each commit.** Head `bcc6820` (pushed). Chain: `99e4afd` (Phase 3 items 1-6) -> `561aefa` (closed-loop pre-registration, committed BEFORE any result) -> `bcc6820` (item 7 + run controls + report modules).
  **Do not push to it while retest crons are running**: a push redeploys them and I have not verified that a redeploy leaves a running job alone [UNVERIFIED].
* `validation/phase3-followups` (worktree `/home/user/cdai-engine-followups`) -- everything after `bcc6820` goes here and is merged into the validation branch only when the runs have finished.
* `main` -- untouched. Merge only with Nick's approval; merge plan with rollback + smoke tests is a Phase 5 deliverable.
* Attribution trailers on commits: `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>` and `Claude-Session: https://claude.ai/code/session_013cA3ao3HM1hGUxpTKXDVQQ`. No model identifier anywhere else in anything pushed.

## 3. What is proven (test evidence, all [RAN] unless noted)
Full local sweep at `bcc6820` (every `test_*.py` plain; DB-dependent ones on a throw-away local Postgres via `run_test_on_local_pg.py`; `cdai_test_suite.py` on the same): **44 files pass; 5 files fail for environmental reasons identical to the pre-change baseline** (3 need `SUPABASE_SERVICE_KEY`; `test_upload.py` points at a Windows path; `test_webhook.py` needs outside network) and **`cdai_test_suite.py` locally = 22 PASS / 6 FAIL / 20 SKIP with the identical failure set as before** (sections that need Supabase auth or Demo-org data). Those can only run on Render -> `cdai-verify-db-retry-fix`; **until Nick clicks it after the final merge, do not claim the full suite passes.**
New suites: `test_phase3_closed_loop.py` 93 checks; `test_phase3_evidence_flags_shadow.py` 59; `test_phase3_bounded_windows.py`; `test_phase3_canonical_metrics.py` 12; `test_run_plan_and_world.py` 99; `test_phase4_run_controls.py` 25; `test_report_figures.py` 38; `test_accuracy_stats.py` 32; `test_google_ads_resilience.py` (follow-ups branch) 17.
Mutation checks: ad-hoc scripts in `docs/evidence/ad-hoc-scripts/` (they edit source in place -- never run another test while one runs). Closed-loop sweep: 38 mutants, all killed; run controls: 19; report_figures: 24 (1 equivalent: uuid->str on a driver that already returns str); accuracy_stats: 20. Every survivor found became an assertion.

## 4. Production database (Supabase) -- what I changed, and what I did not
Applied, additive, verified [DB]: `evidence_oct4_archive`, `simulation_crm_map`, `simulation_crm_clean_log`; label of 44 EverSure formula-replica outcome rows (`20261004234000`); **today** `directive_events.evidence jsonb`, `flag_items` (unique open item per org/campaign/cause, one policy, clients SELECT only), `directive_shadow_events` (RLS on, no client grants), `simulation_closed_loop_results` (harness-only).
**Supabase MCP quirk:** multi-statement DDL scripts hang for 60 s and apply nothing (also a semicolon inside a string literal hangs). Apply one statement per `execute_sql` call and verify with a catalog query. `apply_migration` works for a single clean statement.
NOT applied: `20261004233000_true_cost_views_engine_payout_path.sql` (ships with the merge plan; rollback in `docs/rollback/`); `20261005020000_decision_ledger.sql` (WIP).
Never touched: Apex or Demo data or keys, `main`'s production tables beyond the above.

## 5. Render -- retest setup [RENDER]
Workspace crons, all `branch=validation/full-revalidation-sept-2026`, autoDeploy on commit, schedule `5 0 1 1 *` (never fires on its own; **only Nick's "Trigger Run" starts one -- the MCP cannot trigger, resume or edit start commands; suspended crons need him too**). Env-var changes redeploy the cron. Env values cannot be read back through the MCP; empty values are accepted.
| Role | Cron | id | Notes |
|---|---|---|---|
| run | cdai-run-eversure-40days | crn-db0stj2d0e5s73d2onl0 | 81 sim days x 3 seeds |
| run | cdai-run-sunpeak-65days | crn-db0stjqd0e5s73d2opo0 | 90 x 3 |
| run | cdai-run-westbridge-125days | crn-db0stlegekts73b5cdqg | 120 x 3 |
| run | cdai-run-harborview-115days | crn-db0stknavr4c7396ton0 | 150 x 3 |
| run | cdai-run-distressed-partner-90days | crn-db0strmgekts73b5d54g | 150 x 3; `SIM_RUN_DAYS=150` overrides the inline `DISTRESSED_RUN_DAYS=90` |
| run | cdai-run-apex-230days | crn-db0stm2d0e5s73d2p1k0 | 210 x 3 |
| run + real CRM | cdai-run-stormshield-80days-v2 | crn-db09jelg1s2s73d54fug | 90 x 3 no-CRM, then 45 real-HubSpot days (`[v3-f]`). **Currently `SIM_PREFLIGHT=1` (dry run only); set it to `0` after the rehearsal is read OK** |
| run + real CRM | cdai-run-pinnacle-115days | crn-db0r2dfavr4c738vpm00 | 105 x 3 no-CRM, then 45 real-Salesforce days. Same preflight switch |
| verifier | cdai-verify-stormshield-hubspot / cdai-verify-pinnacle-salesforce | crn-db0upgmgekts73bcnet0 / crn-db0uphc9v7es73d49780 | `VERIFY_RUN_TAG=v3-f` picks the fidelity org |
| full suite | cdai-verify-db-retry-fix | crn-db0t64lg1s2s73fi9un0 | runs `test_db_retry.py` + `cdai_test_suite.py` against production Supabase |
| collector | cdai-full-report-data-v1 | crn-db0vqgou01pc73c63aqg | runs `simulation/run_full_report_data.py` (still the Oct 4 version -- rewrite first, §7) |
Env set on the 8 run crons: `SIM_RUN_TAG=v3`, `SIM_SEEDS=1,2,3`, `SIM_REAL_CRM=0`, `SHADOW_RULES=1`, `SIM_RUN_DAYS` empty (distressed 150), `SIM_FIDELITY_DAYS` empty (StormShield/Pinnacle 45), `SIM_PREFLIGHT=0` (StormShield/Pinnacle 1). Builds of `bcc6820` + the env redeploy finished 00:53 UTC.
Orgs created: `[SIM] <Business> [v3-s1|s2|s3]`, `[SIM] <Business> [v3-f]`. `run_plan.sim_org_name` / `report_figures.orgs_for_tag("v3")` find them. An untagged run halts (exit 6); exit 5 = no real CRM token to carry over; exit 7 = real-CRM clean-up failed.
Healthy-run log lines and durations are in `docs/RETEST-CHECKLIST-oct5.md`. Pace estimates: 15-45 s per mocked sim-day (Oct 4 on Render ~10-20 s); real HubSpot ~375 s and Salesforce ~131 s per sim-day (Oct 4 ingestion timestamps [DB]).
Decision recorded: StormShield and Pinnacle are run concurrently, not strictly sequentially (different vendors, separate portals, independent clean-ups; sequencing would add up to ~6 h). Nick can reverse it by clicking Pinnacle later.

## 6. Findings that change what can be claimed (all verified; details in WORKLOG)
1. [DB] 61% of Oct 4's graded outcomes were scored on windows that had not elapsed (production's maturity rule was bypassed). Fixed: `simulation/sim_clock_scoring.py`.
2. [DB] Only 2 orgs had a real CRM; the other businesses generated CRM-sourced leads nothing could ingest. Retest worlds drop CRM archetypes without a CRM; Google/LinkedIn ad-form leads exist only where a CRM can receive them (no-CRM campaigns carry spend and no lead-level data -- attribution gap by design, reported as FLAG counts only).
3. [CODE]+[RAN] Mixed clock (real vs simulated timestamps) fixed; future-timestamp invariant fails a run that violates it.
4. [DB] Oct 4 "Affiliate Broker 100% margin": the dashboard views read `partner_payouts` (CSV endpoint only) while the engine reads `payout_events`. Views migration written, tested, NOT applied. The CSV payout endpoint still writes a table the engine never reads (open).
5. [CODE]+[RAN] Closed-loop response model: first implementation truncated integers and over-cut small campaigns by up to 12%; fixed before any result existed and recorded in the pre-registration addendum, along with two other deviations (the "every cohort sale has closed by day 120" sentence is false for Senior Care, the metric is ledger-based so unaffected; FLAGS_ON vs FOLLOW_ALL implemented as the same analysis with FOLLOW_ALL as baseline).
6. [CODE]+[RAN] **Google Ads adapter had three defects** (follow-ups branch, test_google_ads_resilience.py): any non-200 from the token endpoint DEACTIVATED the client's connection (one 503 disconnected the account); pagination shared the 3-attempt retry counter so result sets over 3 pages were silently truncated; a 429 outlasting the budget returned partial data as if complete. Not merged into the validation branch yet.
7. [CODE] Health gate was not exercised in the accuracy runs (`SIM_HEALTH_GATE` default off; verified by unit tests). Product finding: any spend-without-leads campaign blocks directives org-wide through that gate.
8. [CODE] Pinnacle/StormShield real-CRM runs ingest the WHOLE portal -> the cleaner (`clean_real_crm.py`, dry-run default, exact-marker match, before/after counts in `simulation_crm_clean_log`) runs first. Real-API behaviour of the cleaner is untested until the rehearsal runs on Render.
9. [CODE] Render's full-suite job runs only two scripts; the 3 `SUPABASE_SERVICE_KEY` tests are not included. Plan: let `cdai_test_suite.py` run extra files named in an env var (on the follow-ups branch, so it lands with the merge), and snapshot Demo row counts before/after.

## 7. Closed-loop experiment and the collector
* Pre-registration: `docs/PREREGISTRATION-closed-loop-decision-value.md` (+ addendum). Arms IGNORE / FOLLOW_ALL / FOLLOW_FLAGS_ON; 3 archetypes (Seed Test - Senior Care/Distressed, SunPeak Solar, EverSure Insurance) x seeds 1-6; metric = ground-truth contribution profit per ad dollar for the cohort of days 31-90; decision rule: ADDS_VALUE only if the pooled 95% interval is above zero AND at least 2 of 3 archetype intervals are; otherwise the report says "advisory visibility with no value claim". Sensitivities never chosen as headline.
* Driver: `python3 simulation/closed_loop_local.py --tag headline --out docs/evidence/closed_loop/headline.json` (throw-away local Postgres; never production). Sensitivity configs: `--elasticity 0.7|1.0`, `--cut-mult 0.25`, `--utm-coverage 0.6|1.0`. About 25-35 s per world; 54 worlds per config.
* **Status when written:** headline + sens-e07 + sens-e10 + sens-cut025 launched at ~00:52 UTC in the sandbox against `bcc6820` (utm 0.6/1.0 still to launch); outputs go to `/home/user/cdai-engine/docs/evidence/closed_loop/*.json` (**untracked until committed -- if the container is gone, re-run the commands; results are deterministic**). `closed_loop_local.py` records the git SHA and whether the tree was clean.
* Collector rewrite spec (`simulation/run_full_report_data.py`, runs on Render, writes to a new harness-only table so results can be read through Supabase MCP instead of scraping logs): per org of `report_figures.orgs_for_tag($SIM_RUN_TAG)`: score matured directives with `sim_clock_scoring.score_mature_on_simulated_clock` (the old collector still calls the legacy `score_all_directives`), `shadow_rules.score_shadow_events`, `accuracy_stats.accuracy_table` (rows/campaigns/episodes + Wilson, FLAG counts only) beside `summarize_confidence_calibration` and `detect_false_directives`, the existing math check (`verify_math`), `report_figures.build_org_figures` + `canonical_cross_check`, flag_items / partner scores / decay signals / budget models; real-CRM fidelity for both CRMs reported separately.

## 8. What is left, in order
1. Nick clicks (rehearsal -> I flip `SIM_PREFLIGHT` -> real runs). I watch logs through the Render MCP; any `HALTING` or stalled day counter is mine to diagnose. Verifier crons after each fidelity pass.
2. While runs execute (on the follow-ups branch only): finish items 8-13; closed-loop utm sweeps; collector rewrite + tests; commit the closed-loop JSON evidence; write the claims generator.
3. After runs finish: merge follow-ups into the validation branch -> Nick clicks the full-suite job and the collector.
4. Phase 5 deliverables, all rebuilt from the rerun: Validation Report v3 (artifact + PDF + markdown; every section; commit SHAs, seeds, run ids and commands; per-directive rows/campaigns/episodes with Wilson 95% intervals never blended; attribution coverage beside every figure; FLAG as counts only; scoring-rule table; shadow counterfactuals; closed-loop value; real-CRM fidelity for both CRMs separately; per-business dashboards, partner scorecards, decay, budget reallocation; engineering record; page-1 "proves / does not prove" box; SIMULATED footer on every page), corrected Oct 4 record (internal), Market-Readiness Review (7 pillars RED/AMBER/GREEN; gates: Starter $1,500 + paid design partners; Growth $3,500 / Scale $8,000; Enterprise $15,000+ and investor diligence), Founder sheet (no accuracy percentages in pitch wording), `claims.json` + generator, updated CLAUDE.md facts, dated WORKLOG / manual entries, merge plan with rollback + smoke tests. **Wait for Nick's approval before merging to `main`.**
5. The one-time closing message (section 6a below).

## 9. Disclosures that must travel with every report
Everything is SIMULATED. World assumptions (`utm_coverage` 0.8, response elasticity 0.85) are disclosed and swept. The health gate was off in the accuracy runs. No-CRM Google/LinkedIn campaigns have spend and no lead-level data. EverSure's 44 old outcome rows are formula replicas and excluded. The Oct 4 figures (including 98.4% and the Sept 24 set) are retired, not corrected. Real-world proof (live clients, platform approvals such as Meta App Review / Google developer-token level / LinkedIn MDP, scale behaviour) is not something this retest can produce -- list each as UNVERIFIED unless evidence is found.

## 10. Working conventions
Tag every claim; never report an unrun test as passed; after each item run the touched files' tests plus the full suite and paste raw PASS/FAIL/SKIP; stop only for Nick-only actions (Trigger Run clicks, credential rotation, history purge), decisions that change a scoring rule/threshold/methodology_version (3, frozen), data-loss risk, or the merge to main; batch questions into one message; otherwise decide, record in WORKLOG.md, continue. Nothing that changes what the engine decides for a live client ships unless behind a flag that defaults OFF. No touching Apex/Demo data or keys. Pitch/outreach copy has no accuracy percentages. User preferences: never assume, never lie, short explanations, never cut corners.
Local test runner: `tools/run_all_local_tests.sh <outdir>` (every test plain; DB-dependent ones re-run on a throw-away Postgres; then `cdai_test_suite.py` locally).

---

