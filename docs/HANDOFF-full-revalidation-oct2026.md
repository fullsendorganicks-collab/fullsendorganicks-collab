# NICK'S REQUIREMENTS, EXPECTATIONS AND GAME PLAN -- read this first (quotes are verbatim, Oct 5, 2026)

> "It is not a fucking toy. It is a enterprise level truth engine."
> "get everything fixed. Make sure that all the CRON jobs are ready to rock and ready for me to trigger and do not miss a single thing again not one no gaps no holes nothing"
> "the accuracy number is the math number the true CPL the true CAC all of it needs to be 100% accurate and viable if a CFO looks at the report reports that are produced after this test and they find any gaps or anything I'm screwed, which means it cannot happen"
> "there will be no assumptions or guessing everything must be proven, tried true and tested"
> "We can update all the stuff inside the database and everything else later all I care about is being ready for Tuesday."
> "Is this really fixing and making it all ready or is it forcing it to achieve a task fast?"
> "Remember to take your time don't rush follow the rules and check your work as you go."

Earlier and still binding: "I'm done with gaps. This needs to be market ready by Tuesday." Nick is a solo bootstrapped founder; on Tuesday Oct 6, 2026 he must be able to stop building and sell
(Starter $1,500 + paid design partners; Growth $3,500 / Scale $8,000; Enterprise $15,000+ and investor diligence). A CFO or diligence reader will look for gaps in the reports; one gap is fatal.

## A. What "done" means (the acceptance tests I hold myself to)
1. **Every cron click works the first time.** For each job: exact first log lines (including the exact `days=` value), exit codes, and what a red flag looks like (`docs/RETEST-CHECKLIST-oct5.md`). I read the logs from Render within minutes of each click and say so; unit tests alone are not proof the cron path works.
2. **Reports a CFO cannot find a gap in.** Every figure is read from snapshot rows (`simulation/report_figures.py`) and cross-checked:
   a. *Reconciliation bridge* (world ground truth -> database) for leads, spend, payouts, sales, refunds, chargebacks, per org. Every difference lands in a NAMED category (sale still pending by sales delay, +/-1-day boundary, unattributed lead, dropped by design); no unexplained residual. **[NOT BUILT]**
   b. *True CPL and true CAC*: the engine/dashboard value equals an independent recompute from the world ledger within a stated tolerance, per campaign and per org. **[NOT BUILT; partial: the collector's `math` section compares DB-derived vs engine values only, and it lists ground-truth gross vs DB net without a bridge -- in the local test truth gross was $848k vs DB net $396k, unexplained in the output]**
   c. *Two numbers, never blended.* (i) Directive accuracy: hit rate per directive type on matured outcomes, Wilson 95% intervals, rows / campaigns / episodes reported separately, FLAG counts only, attribution coverage beside every figure **[tooling built and tested: accuracy_stats.py, collect_report_v3.py]**. (ii) Math accuracy: share of checked metrics where engine == independent recompute == ground truth; its exact definition, tolerance, and what it does and does not prove must be written in the collector docstring BEFORE the run **[NOT DEFINED YET]**.
   d. ROI for the simulated client and every figure on the Vercel client dashboard path: dashboard value == report value **[not cross-checked yet]**.
3. No claim without a tag ([CODE] [DB] [RAN] [RENDER] [RENDER-LOG] [UNVERIFIED]); nothing reported as passed that was not run.
4. Database clean-up, migrations not yet applied, replacing the retired public numbers: later, with Nick's approval (merge plan). Not on the critical path to Tuesday. No merge to `main` without his explicit OK.

## B. Honest answer to "is this really fixing it, or forcing a task through fast?"
**Real fixes (evidence exists):** invalid-retest causes found and fixed (production maturity rule bypassed; no-CRM businesses emitting CRM leads; mixed real/simulated clock; real-CRM data not cleaned) [RAN, tests + DB queries]; closed-loop experiment pre-registered before any result and run (verdict: no value claim) [RAN]; Google Ads adapter defects fixed [RAN, 22 checks]; scheduler API-key syncs wired dormant [RAN, 26 checks]; report/collector/claims tooling [RAN, 41 + 39 checks]; every mutation survivor became an assertion.
**NOT yet proven (and I will not call it ready until it is):**
* The cron path with the NEW code (tag/seeds/fidelity/preflight) has never executed end to end -- not locally (mitmdump will not import here; unresolved) and not on Render. Only unit tests exist for it.
* The reconciliation bridge, true CPL/CAC ground-truth comparison and the math-accuracy number (A.2a-c) do not exist yet. Without them a CFO could ask "why does ground truth not equal the database?" and the report would have no answer.
* Render env values cannot be read back; every env claim is verified only by the first log lines after a click.
* The real-CRM clean-up (`clean_real_crm.py`) has never run against the real HubSpot / Salesforce APIs; the rehearsal on Render is the first proof.
* The full suite on Render (`cdai_test_suite.py`) has not been run on the final code; locally 22 PASS / 6 FAIL / 20 SKIP with the same failure set as the pre-change baseline (all environmental).
**Defect in my own set-up found Oct 5 ~01:30 UTC while preparing the URL list [CODE] [RENDER]:** the Distressed cron's start command exports `DISTRESSED_RUN_DAYS=90` and `cloud_runner_distressed.py:77` resolves `SIM_RUN_DAYS or DISTRESSED_RUN_DAYS or 150`. An unset or empty `SIM_RUN_DAYS` would have run Distressed for 90 days -- the length that "matured nothing" on Oct 4 -- while the click list said 150. The handoff itself contradicted itself (section 5 said SIM_RUN_DAYS=150 on that cron, the env line said empty). Fix: `SIM_RUN_DAYS=150` set on the cron (merge mode) at 01:34 UTC and the redeploy went live 01:35:53 UTC [RENDER]. The value cannot be read back: **the first Distressed log line must show `days=150`; if it shows 90, cancel the run and tell me.**

## C. Exact remaining work, in order (a line is done only with raw output pasted into WORKLOG)
1. DONE -- Distressed run length pinned (above). Click list re-issued with the expected `days=` per business and a do-not-click list.
2. Prove the cron path locally with the new code: `cloud_runner.py` one business, 1 seed, a few sim days, real adapters through the mock vendor + mitmdump, on a throw-away local Postgres. Needs a working `mitmdump` (use a clean venv). Any defect found is fixed on the follow-ups branch and, if it is in code the run crons execute, carried to the validation branch BEFORE Nick clicks (pushing there only while no run cron is running).
3. Build the reconciliation bridge + ground-truth true CPL/CAC + math-accuracy definition in `simulation/collect_report_v3.py` (+ tests, mutation sweep). Prove it on a local world where every difference is explained.
4. Nick clicks; I watch (first-line checks, day counters, HALTING, exit codes 5/6/7); rehearsal -> I flip `SIM_PREFLIGHT=0` on StormShield/Pinnacle -> real runs -> verifier crons after the fidelity passes.
5. After runs finish: merge follow-ups into the validation branch (collector, claims, ledger, scheduler, Google fixes), re-run the full local sweep (`tools/run_all_local_tests.sh`), Nick clicks `cdai-verify-db-retry-fix` and `cdai-full-report-data-v1` (set `SIM_RUN_TAG=v3` first).
6. Phase 5 deliverables rebuilt from the rerun only; merge plan with rollback + smoke tests; wait for Nick's approval; then the one-time closing message.
7. **Repo secrets hygiene (promised in the Oct 4 plan, NOT done -- verified Oct 5 [CODE]):** `client_secrets.json` (Google OAuth client secret) is still tracked on the validation branch; `.gitignore` is UTF-16 so its patterns do nothing; `time_engine.py` and `run_full_directive.py` carry a Supabase pooler URL WITH the DB password in their text. Repo side (untrack, UTF-8 `.gitignore`, scrub the URLs, secret scan) goes on the follow-ups branch. **Nick-only:** rotate the Google OAuth client secret and the Supabase DB password, then update `DATABASE_URL` on every Render service that uses it; history purge needs a force-push and his explicit OK. Rotate BEFORE the clicks or AFTER the runs, never during.
8. **Full-suite job on Render is NOT extended yet:** `cdai_test_suite.py` has no hook for the 3 `SUPABASE_SERVICE_KEY` tests and no Demo-org row-count snapshot before/after. Plan: env-var-driven extra test files + Demo counts in the suite itself, on the follow-ups branch, so Nick's one-time Render start-command edit is no longer needed. Until built, the Render suite click proves less than the plan said.
9. **Disclosure missing from section 9 until now:** the SCALE rule was calibrated on validation data (commit `2efc188`, Phase 1 audit [CODE]). A v3 SCALE hit rate is an in-sample number for that rule unless the world seeds are shown to be disjoint from the calibration data; the report must say so beside every SCALE figure and in the page-1 box.
Still open from earlier: item 11 load-test plan, HubSpot/Salesforce 5xx retry audit, scheduler heartbeat, `sens-utm06` / `sens-utm10` evidence.

---

# STATE OF PLAY — Oct 5, 2026 (updated ~01:50 UTC, replaces the status line and punch list further down)

_Everything in this section was verified by the session that wrote it; tags: [CODE] read in the repo, [DB] queried live (Supabase project
`cdaiwdebsdfgttntxyfp`), [RAN] executed with output, [RENDER] read through the Render MCP, [UNVERIFIED] not provable from here. The sections below
this one are the Oct 3-4 text, kept for history. Where they disagree with this section, this section wins._

## 0. One paragraph
Nick (solo founder, Allocera Intelligence / CDAI, ~3.5 years on a ~40k-line deterministic engine) must be able to stop building and sell by **Tuesday Oct 6, 2026**.
I hold a standing single-engineering-owner mandate (audit own work -> make the retest valid -> build what market readiness needs -> rerun -> rebuild every report
from the rerun -> merge plan). The Oct 4 validation was audited and found invalid in specific ways (below); the engine-side fixes and the new experiment are done,
tested and pushed; the retest's Render crons are configured and Nick has been sent his click list; **no retest cron had been triggered when this was updated**
(check `list_events` with `cron_job_run_started` on the crons in §5). Nothing has been merged to `main`, and nothing may be without Nick's explicit approval.
His last instruction: handle everything that can be handled, make it pass the test suite, tell him what it takes -- "I'm done with gaps."

## 1. Phase status
| Phase | State |
|---|---|
| 1 Audit of my own Oct 4 work | DONE (13 findings, WORKLOG "Oct 4-5, 2026") |
| 2 Make the retest valid | DONE: evidence archived, run-tagged orgs, V1 mixed-clock fix, real-CRM time remap, real dev-CRM cleaner, no placeholder campaigns, UTM attribution model, simulated-clock scoring, 3 seeds, snapshot-sourced `report_figures.py` (tested), tag-driven v3 collector `simulation/collect_report_v3.py` (tested, 20-mutant sweep; `run_full_report_data.py` is now a shim to it; **on the follow-ups branch only**; its production table `simulation_report_data` is applied). |
| 3 items 1-7 (bounded windows, canonical metrics, evidence envelope, flagged-OFF shadow rules, finding B, FLAG subtypes, closed-loop value) | DONE, tested, mutation-checked, pushed at `bcc6820` |
| 3 item 8 reliability | PARTLY DONE on `validation/phase3-followups`: Google Ads adapter (3 defects + optional developer token, 22 checks). Freshness already exists (`health_monitor`, 49 h warn / 73 h critical -- that is also today's missed-sync detection latency; a scheduler heartbeat would make it ~26 h and is NOT built). Not done: HubSpot/Salesforce 5xx audit, parallel per-org scheduler plan (doc) |
| 3 item 9 integrations | DONE in code, dormant: `scheduler.run_api_key_syncs` pulls Ringba / Boberdoo / Bing / Stripe nightly behind `SCHEDULER_API_KEY_SYNCS` (26 checks, 30-mutant sweep). Finding: before this, **no production path called those four adapters** although the signup wizard offers their connect cards. None is proven against a live vendor account. Switch on at merge, or hide the cards (Nick's call). Google Ads / Salesforce live proofs still need Nick's accounts |
| 3 item 10 platform access | DONE as a document: `docs/PLATFORM-ACCESS-STATUS-oct2026.md` (web-search evidence; vendor pages unreachable from the sandbox; Meta / Google / LinkedIn approval status is [UNVERIFIED] and needs Nick's dashboards). Finding: Google reportedly sunset developer tokens on Sept 9, 2026 |
| 3 item 11 load-test plan (100 orgs, $1M/mo) | NOT STARTED (plan + a local per-org cycle timing is feasible) |
| 3 item 12 `claims.json` generator | TOOL DONE (`tools/claims.py`, 39 checks, 27-mutant sweep): builds claims from collector rows, renders the CLAUDE.md block and a facts yaml, and lints for RETIRED claims. **Not yet run on real data (needs the retest).** Lint of the repo found 14 live occurrences of retired numbers: `CLAUDE.md` lines 13, 15, 137; `CDAI_MANUAL_MOST_UP_TO_DATE.md` lines 8, 45; `CDAI_FULL_CAPABILITY_READINESS_Oct_2026.md` (8 lines); **`chat_agent.py:271` -- the live "Ask CDAI" system prompt quotes the Sept 24 set**. Replacing public wording needs Nick's OK (his Sept 25 decision was to keep quoting PAUSE 85.2%) |
| 3 item 13 decision ledger | DONE in code, dormant: `decision_ledger.py` + migration `20261005020000` (NOT applied) + two failure-isolated hooks in `directive_engine.py`; opt-in per org; 54 checks, 30-mutant sweep (2 equivalent) |
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
New suites: `test_phase3_closed_loop.py` 93 checks; `test_phase3_evidence_flags_shadow.py` 59; `test_phase3_bounded_windows.py`; `test_phase3_canonical_metrics.py` 12; `test_run_plan_and_world.py` 99; `test_phase4_run_controls.py` 25; `test_report_figures.py` 38; `test_accuracy_stats.py` 32; follow-ups branch: `test_google_ads_resilience.py` 22, `test_decision_ledger.py` 54, `test_scheduler_api_key_syncs.py` 26, `test_collect_report_v3.py` 41, `test_claims.py` 39, `test_closed_loop_exploratory.py` 10. The follow-ups branch's full local sweep before the last three additions: 46 files OK + the same 5 environmental failures; re-run `tools/run_all_local_tests.sh` before merging.
Mutation checks: ad-hoc scripts in `docs/evidence/ad-hoc-scripts/` (they edit source in place -- never run another test while one runs). Closed-loop sweep: 38 mutants, all killed; run controls: 19; report_figures: 24 (1 equivalent: uuid->str on a driver that already returns str); accuracy_stats: 20. Every survivor found became an assertion.

## 4. Production database (Supabase) -- what I changed, and what I did not
Applied, additive, verified [DB]: `evidence_oct4_archive`, `simulation_crm_map`, `simulation_crm_clean_log`; label of 44 EverSure formula-replica outcome rows (`20261004234000`); **today** `directive_events.evidence jsonb`, `flag_items` (unique open item per org/campaign/cause, one policy, clients SELECT only), `directive_shadow_events` (RLS on, no client grants), `simulation_closed_loop_results` and `simulation_report_data` (both harness-only).
**Supabase MCP quirk:** multi-statement DDL scripts hang for 60 s and apply nothing (also a semicolon inside a string literal hangs). Apply one statement per `execute_sql` call and verify with a catalog query. `apply_migration` works for a single clean statement.
NOT applied: `20261004233000_true_cost_views_engine_payout_path.sql` (ships with the merge plan; rollback in `docs/rollback/`); `20261005020000_decision_ledger.sql` (dormant until the merge).
Never touched: Apex or Demo data or keys, `main`'s production tables beyond the above.

## 5. Render -- retest setup [RENDER]
Workspace crons, all `branch=validation/full-revalidation-sept-2026`, autoDeploy on commit, schedule `5 0 1 1 *` (never fires on its own; **only Nick's "Trigger Run" starts one -- the MCP cannot trigger, resume or edit start commands; suspended crons need him too**). Env-var changes redeploy the cron. Env values cannot be read back through the MCP; empty values are accepted.
| Role | Cron | id | Notes |
|---|---|---|---|
| run | cdai-run-eversure-40days | crn-db0stj2d0e5s73d2onl0 | 81 sim days x 3 seeds |
| run | cdai-run-sunpeak-65days | crn-db0stjqd0e5s73d2opo0 | 90 x 3 |
| run | cdai-run-westbridge-125days | crn-db0stlegekts73b5cdqg | 120 x 3 |
| run | cdai-run-harborview-115days | crn-db0stknavr4c7396ton0 | 150 x 3 |
| run | cdai-run-distressed-partner-90days | crn-db0strmgekts73b5d54g | 150 x 3. Start command exports `DISTRESSED_RUN_DAYS=90`; `SIM_RUN_DAYS=150` re-set explicitly 01:34 UTC Oct 5 (redeploy live 01:35:53) because an empty `SIM_RUN_DAYS` lets the 90 win. Not readable back: first log line must show `days=150` |
| run | cdai-run-apex-230days | crn-db0stm2d0e5s73d2p1k0 | 210 x 3 |
| run + real CRM | cdai-run-stormshield-80days-v2 | crn-db09jelg1s2s73d54fug | 90 x 3 no-CRM, then 45 real-HubSpot days (`[v3-f]`). **Currently `SIM_PREFLIGHT=1` (dry run only); set it to `0` after the rehearsal is read OK** |
| run + real CRM | cdai-run-pinnacle-115days | crn-db0r2dfavr4c738vpm00 | 105 x 3 no-CRM, then 45 real-Salesforce days. Same preflight switch |
| verifier | cdai-verify-stormshield-hubspot / cdai-verify-pinnacle-salesforce | crn-db0upgmgekts73bcnet0 / crn-db0uphc9v7es73d49780 | `VERIFY_RUN_TAG=v3-f` picks the fidelity org |
| full suite | cdai-verify-db-retry-fix | crn-db0t64lg1s2s73fi9un0 | runs `test_db_retry.py` + `cdai_test_suite.py` against production Supabase |
| collector | cdai-full-report-data-v1 | crn-db0vqgou01pc73c63aqg | runs `simulation/run_full_report_data.py` (still the Oct 4 version -- rewrite first, §7) |
Env set on the 8 run crons: `SIM_RUN_TAG=v3`, `SIM_SEEDS=1,2,3`, `SIM_REAL_CRM=0`, `SHADOW_RULES=1`, `SIM_RUN_DAYS` empty on the other run crons (their code default is the intended length) and `150` on the Distressed cron, `SIM_FIDELITY_DAYS` empty (StormShield/Pinnacle 45), `SIM_PREFLIGHT=0` (StormShield/Pinnacle 1). Builds of `bcc6820` + the env redeploy finished 00:53 UTC.
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

10. [RAN] **Closed-loop result (pre-registered rule): the directives are 'advisory visibility with no value claim'.** Headline + three sensitivities (elasticity 0.7 and 1.0, CUT 0.25) give the same verdict; 1 of 3 archetype intervals above zero (the Distressed archetype, +0.84 profit per ad dollar [+0.21, +1.48]); SunPeak -64.7 [-77.5, -51.8] and EverSure -2.3 [-4.6, -0.05]; pooled -22.1 [-26.4, -17.7]. Files: `docs/evidence/closed_loop/*.json`.
11. [RAN, POST HOC -- labelled, not a claim] The pre-registered metric is an efficiency ratio: scaling a profitable campaign under diminishing returns lowers it even when profit rises, and the pooled mean is dominated by SunPeak, whose ratio is ~280 because its Boberdoo / CallRail / HubSpot sources have no ad spend. In DOLLARS of ground-truth profit per world (`simulation/closed_loop_exploratory.py`): SunPeak +912,656 [+618,862, +1,206,451] (+15%), EverSure +38,335 [+21,938, +54,733] (+19%), Distressed Senior Care -75,599 [-187,976, +36,779] (not significant). These are hypotheses for a new pre-registered experiment; the verdict above stands.
12. [RAN] **Mechanism in the Distressed world (diagnostic, seed 1, `docs/evidence/closed_loop/diagnostic-senior-care-s1.json`):** the engine PAUSED 'Affiliate Broker PPL Network' on sim day 11 and 'Incentivized Co-Registration Sweepstakes' on day 13 -- both genuinely profitable on ground truth (cohort profit +$159k and +$50k) -- because payouts are booked at lead time while sales close 7-90 days later, so a young campaign looks like it is bleeding (confidence tier was MEDIUM, and only LOW blocks PAUSE). A paused campaign then shows no new spend and its margin recovers as old sales land, which the frozen scorer reads as a PAUSE HIT. **This needs a decision from Nick: PAUSE gating for long-sales-cycle verticals before sales mature, and whether the frozen PAUSE scoring rule (methodology v3) rewards a self-fulfilling pause. I did NOT change either (not approved).**
13. [RAN, POST HOC] FOLLOW_FLAGS_ON (pause while a FLAG item is open) is worse than FOLLOW_ALL in SunPeak (-9.8 per ad dollar; profit 600k vs 913k) and EverSure: those FLAGs are ATTRIBUTION_GAP on campaigns that earn money (unattributed revenue), so pausing them is wrong. A FLAG is a request for a human to look, not a reason to pause.
14. [PROCESS] The first closed-loop headline run was discarded after I found its local database silently lacked the evidence layer (a migration loader split files on a '-- ROLLBACK:' comment near their tops). The driver now applies whole files and refuses to run on an incomplete schema (recorded in each JSON's `schema_checks`). Never trust a run without checking its schema.

## 7. Closed-loop experiment and the collector
* Pre-registration: `docs/PREREGISTRATION-closed-loop-decision-value.md` (+ addendum). Arms IGNORE / FOLLOW_ALL / FOLLOW_FLAGS_ON; 3 archetypes (Seed Test - Senior Care/Distressed, SunPeak Solar, EverSure Insurance) x seeds 1-6; metric = ground-truth contribution profit per ad dollar for the cohort of days 31-90; decision rule: ADDS_VALUE only if the pooled 95% interval is above zero AND at least 2 of 3 archetype intervals are; otherwise the report says "advisory visibility with no value claim". Sensitivities never chosen as headline.
* Driver: `python3 simulation/closed_loop_local.py --tag headline --out docs/evidence/closed_loop/headline.json` (throw-away local Postgres; never production). Sensitivity configs: `--elasticity 0.7|1.0`, `--cut-mult 0.25`, `--utm-coverage 0.6|1.0`. About 25-35 s per world; 54 worlds per config.
* **Status:** headline + sens-e07 + sens-e10 + sens-cut025 FINISHED (54 worlds each, ~18 min on 4 cores). Run from branch `exp/closed-loop-bcc6820-fix` (= bcc6820 + the driver schema fix `bcea9a8`, tree clean, SHA recorded in each JSON). Sensitivity configs `sens-utm06` and `sens-utm10` (UTM coverage 0.6 / 1.0) were still running when this was written. Outputs: `docs/evidence/closed_loop/*.json` on the follow-ups branch. Results: finding 10-13 in section 6.
* Collector: BUILT -- `simulation/collect_report_v3.py` (spec in its docstring); the cron entry `run_full_report_data.py` is a shim. It lives on the follow-ups branch, so it reaches the `cdai-full-report-data-v1` cron only after the follow-ups are merged into the validation branch (after the runs). Unscorable directives ('No data in pre or post windows') are reported separately from immature ones; both are 'unscored' in the accuracy table.

## 8. What is left, in order
0. **Decisions only Nick can make (batched; nothing waits on them except the report wording):** (a) PAUSE gating / scoring rule for long-sales-cycle verticals (finding 12) -- changing either means a new methodology version; (b) switch on `SCHEDULER_API_KEY_SYNCS` at merge or hide the Ringba / Boberdoo / Bing / Stripe signup cards; (c) replace the retired public numbers (the `chat_agent.py` prompt, CLAUDE.md, the manual) once v3 numbers exist; (d) supply Meta / Google / LinkedIn approval status (platform doc). (e) credential rotation: has it been done, and before or after the runs (item C.7)? (f) StormShield and Pinnacle concurrently (current set-up) or strictly one after the other (the Oct 4 plan) -- different vendors, separate portals after the CRM split, concurrency saves ~6 h; the first rehearsal/real-run logs will show any cross-effect.
1. Nick clicks (rehearsal -> I flip `SIM_PREFLIGHT` -> real runs). I watch logs through the Render MCP; any `HALTING` or stalled day counter is mine to diagnose. Verifier crons after each fidelity pass.
2. While runs execute (follow-ups branch only): `sens-utm06` / `sens-utm10` evidence, item 11 load plan (not started), HubSpot/Salesforce retry audit, optional scheduler heartbeat.
3. After runs finish: merge follow-ups into the validation branch -> Nick clicks the full-suite job and the collector (`SIM_RUN_TAG=v3` on `cdai-full-report-data-v1`; set it first).
4. Phase 5 deliverables, all rebuilt from the rerun (the closed-loop section must lead with the pre-registered verdict; the exploratory dollar table is labelled post hoc): Validation Report v3 (artifact + PDF + markdown; every section; commit SHAs, seeds, run ids and commands; per-directive rows/campaigns/episodes with Wilson 95% intervals never blended; attribution coverage beside every figure; FLAG as counts only; scoring-rule table; shadow counterfactuals; closed-loop value; real-CRM fidelity for both CRMs separately; per-business dashboards, partner scorecards, decay, budget reallocation; engineering record; page-1 "proves / does not prove" box; SIMULATED footer on every page), corrected Oct 4 record (internal), Market-Readiness Review (7 pillars RED/AMBER/GREEN; gates: Starter $1,500 + paid design partners; Growth $3,500 / Scale $8,000; Enterprise $15,000+ and investor diligence), Founder sheet (no accuracy percentages in pitch wording), `claims.json` + generator output, updated CLAUDE.md facts, dated WORKLOG / manual entries, merge plan with rollback + smoke tests (apply the views migration and the decision-ledger migration, set the two flags, replace retired claims). **Wait for Nick's approval before merging to `main`.**
5. The one-time closing message (section 6a below).

## 9. Disclosures that must travel with every report
Everything is SIMULATED. World assumptions (`utm_coverage` 0.8, response elasticity 0.85) are disclosed and swept. The health gate was off in the accuracy runs. No-CRM Google/LinkedIn campaigns have spend and no lead-level data. EverSure's 44 old outcome rows are formula replicas and excluded. The Oct 4 figures (including 98.4% and the Sept 24 set) are retired, not corrected. The SCALE rule was calibrated on validation data (`2efc188`): SCALE figures are in-sample for that rule. Real-world proof (live clients, platform approvals such as Meta App Review / Google developer-token level / LinkedIn MDP, scale behaviour) is not something this retest can produce -- list each as UNVERIFIED unless evidence is found.

## 10. Working conventions
Tag every claim; never report an unrun test as passed; after each item run the touched files' tests plus the full suite and paste raw PASS/FAIL/SKIP; stop only for Nick-only actions (Trigger Run clicks, credential rotation, history purge), decisions that change a scoring rule/threshold/methodology_version (3, frozen), data-loss risk, or the merge to main; batch questions into one message; otherwise decide, record in WORKLOG.md, continue. Nothing that changes what the engine decides for a live client ships unless behind a flag that defaults OFF. No touching Apex/Demo data or keys. Pitch/outreach copy has no accuracy percentages. User preferences: never assume, never lie, short explanations, never cut corners.
Local test runner: `tools/run_all_local_tests.sh <outdir>` (every test plain; DB-dependent ones re-run on a throw-away Postgres; then `cdai_test_suite.py` locally).

---

# (History) The Oct 3-4 text below is superseded where it conflicts with the section above


# HANDOFF (Oct 3-4 text): Full re-validation test — read this first, nothing else is in scope

_Written Oct 3, 2026, end of a reconciliation session. For the next Claude Code session._

**Status in one line:** branch `validation/full-revalidation-sept-2026` is now reconciled
(`a97a555`) and pushed. Every original validation org is gone from the database. The next
session starts the real, full run from zero. **Nothing else is this session's job — not
website work, not CallRail, not LinkedIn, not anything in `fullsendorganicks-collab`. Only
this test.**

**Real deadline (Nick, Oct 4 2026, late night, verbatim): "I wanna switch to sales marketing and
pitching mode by Tuesday of next week and today's Saturday."** That's the actual constraint, not
"before bed tonight" (an earlier, softer ask the same night — see WORKLOG.md for both, in order).
All 8 jobs (7 businesses + Distressed Partner archetype) are running or ready to trigger as of
this note. At observed per-day rates this finishes well before Tuesday without needing to rush or
cut anything — do not compress quality or skip verification to beat an earlier, superseded
deadline. If Tuesday itself is genuinely at risk, say so plainly and early, the same way every
other finding this session got surfaced — don't let it go unmentioned until it's too late to act on.

**Standing authorization (Nick, Oct 4 2026, verbatim intent):** "Everything that I want out of
this test... if you need to add something to get what I need to do it, add another business, add
another part of the [build/engine], I don't care, but those end results are what I'm gonna get
after this. I don't care how long it takes." This means: the exact end-state in §4/§4a below is
fixed and non-negotiable, but the PATH to it is not — adding a business, a channel, a script, or
closing a gap found along the way (e.g. Bing never being wired into any simulated business, found
Oct 4) is all in scope without asking first, as long as it serves getting to the real, exact
deliverable. Do not stop at "good enough" or a partial result and call it done. Full ownership
applies (see `CLAUDE.md`'s standing rule of the same name) — this is its strongest form yet.

**Open punch list as of Oct 4, 2026, 00:xx UTC (update this list as items close, don't let it go
stale):**
1. Fix HubSpot's broken attribution write: `hs_analytics_source_data_2` is a HubSpot-owned,
   system-calculated property and rejects external writes (`READ_ONLY_VALUE`) — confirmed live,
   not assumed, from HubSpot's own API error during StormShield's completed 40-day run. Needs a
   real custom HubSpot contact property (same fix pattern already proven for Salesforce's
   `UTM_Campaign__c`), with `seed_hubspot()` repointed at it.
2. StormShield's business profile has no Bing channel at all — true of every business in this
   harness, not a new regression. If "all 10 adapters on one business" must be literally true,
   this needs a Bing channel added to `world_state.py`'s StormShield entry, mirroring how the
   Salesforce channel was added for this same reason.
3. Re-run StormShield clean once 1 (and 2, if pursued) are fixed — the current 40-day run is good
   data (math 9/9 match, 0 misses on every directive type that fired) but doesn't yet have working
   HubSpot attribution.
4. Re-add the rc==0 day-count-verification safeguard to `cloud_runner.py`'s `main()` — it did not
   survive the Oct 3 merge (confirmed: the shipped completion message lacks the
   "verified against cost_events" line this session's own earlier fix added). Without it, confirming
   a run is real requires manually paging through Render logs, which is exactly the friction this
   safeguard exists to remove.
5. Run the other 6 businesses (EverSure, SunPeak, HarborView, Pinnacle, Westbridge, Apex) to their
   full designed lengths.
6. Run the Distressed Partner archetype (90 days) — the only source of CUT/PAUSE/QUARANTINE/
   RENEGOTIATE accuracy data; nothing else in this harness produces those.
7. Build and run the Layer 2 independent re-derivation (see §0 item 5) — a genuinely separate
   method from `verify_math.py`'s own internal check, not just citing that same check twice.
8. Assemble the actual final report per §4/§4a — not started for any business yet.

---

## 0. The mandate, exact, do not narrow or substitute it

One test. Everything else — the LinkedIn post, CallRail partnership terms, the marketing
website cleanup on `fullsendorganicks-collab` — is a different, separate thread. Do not pick
any of it up from here; if asked, point back to this repo's own docs and that repo's own
branches.

The test itself, Nick's own words, unchanged since he first specified it:

1. **The full 7-business re-validation**, each business run to its full designed length so
   every directive type gets a real chance to fire (`CANONICAL_ORDER` in
   `simulation/cloud_runner.py`):

   | Business | Vertical | Days | Real HubSpot | Real Salesforce |
   |---|---|---|---|---|
   | StormShield Roofing | roofing | 40 | yes | no (see amendment below) |
   | EverSure Independent Insurance | insurance | 40 | yes | no |
   | SunPeak Residential Solar | solar | 65 | yes | no |
   | HarborView Senior Living Advisors | senior_care | 115 | yes | no |
   | Pinnacle Home Lending | mortgage | 115 | no | yes (moved from StormShield, see below) |
   | Westbridge Injury Law | legal | 125 | yes | no |
   | Apex Trial Recruitment Partners | clinical_trial | 230 | yes | no |

2. ~~StormShield Roofing is the one business running all 10 real adapters (Meta, Google,
   LinkedIn, Bing, HubSpot, Salesforce, Ringba, CallRail, Boberdoo, Stripe) with real HubSpot
   and real Salesforce connected simultaneously — not split across two businesses.~~
   **AMENDED Oct 4 2026, founder's own explicit call, real-time during the live run:** both real
   CRMs on StormShield simultaneously hit `run_simulation.py`'s own timing-regression gate at
   day 5 (`sync_window = min(new_day, 7)`, `run_simulation.py:332` — the real HubSpot+Salesforce
   lookback window ramps 1→7 days over a run's first week by design, same in production, but two
   real CRMs at once, compressed into minutes of wall-clock time instead of real days, roughly
   doubles the real API load during that ramp). When this was explained, the founder pointed out
   himself: no real client has ever run two CRMs for one business, and never would — so the
   combined-CRM case was never representative of real usage, just an artifact of how the test was
   originally scoped. **Decision: split it.** StormShield keeps its real HubSpot connection and
   its already-banked real days; the real Salesforce connection moves to Pinnacle Home Lending
   (already the dedicated Salesforce-only business in this roster — see
   `simulation/split_crm_stormshield_pinnacle.py` for the exact, idempotent steps, and
   `cloud_runner.py`'s `CANONICAL_ORDER` comment for the same reasoning in the code itself). This
   does not remove anything from §4's report requirements — every number, every dashboard
   section, and the report's full depth still apply to both businesses; "all 10 adapters live"
   is now proven across the 7-business suite rather than on one single business. StormShield's
   archetype still has its 6th channel (`"Salesforce Realtor Partner Channel (Roofing)"` in
   `world_state.py`'s `CAMPAIGN_ARCHETYPES`) — now unused by StormShield's own real-CRM run, left
   in place rather than ripped out, since removing it is not required by this change.
3. **The Distressed Partner archetype** (`simulation/cloud_runner_distressed.py`,
   `DISTRESSED_RUN_DAYS=90`, senior_care vertical, fast `cycle_days=30` so it matures within
   the window) — run at its **full 90 days**, not shortened. This is the one archetype
   designed to actually produce QUARANTINE / PAUSE / RENEGOTIATE / CUT / FLAG — the rare
   directive types the other 7 businesses mostly won't surface on their own. Do not cut this
   one short to save compute; it exists specifically to not be a "we never saw this directive
   type" gap in the final report.
4. **Run `verify_math.py` and `verify_directive_accuracy.py` for every business, inline, in
   the same container/process the simulation just ran in** — `SimWorld`'s state was
   local-disk-only in every version of this harness before today's merge; it's now DB-backed
   (see §2), but still verify inline per business rather than assume a later separate
   verification pass will find it, until that DB-backed path has itself been proven on a live
   run.
5. **Independent monitoring, both layers**, so the "finds one problem, keeps going, misses
   others" failure pattern cannot repeat:
   - **Layer 1 — hard per-day invariant gate.** Already built and merged (`rc=4` in
     `run_simulation.py`, halts immediately and permanently — never auto-retried — on an
     adapter sync raising, or a seed call writing 0%-attributed records). **Not yet
     independently verified by this session** — read, not proven live. Verify it actually
     fires before trusting it on the real run (see §3, step 2).
   - **Layer 2 — independent live re-derivation.** Re-derive key numbers (spend, leads,
     revenue, directive counts) directly from the raw DB tables by a separate method than
     whatever `verify_math.py`/`verify_directive_accuracy.py` use internally, and compare. This
     is the same method that caught the Ringba/Stripe near-miss earlier in this effort — it
     must actually be exercised against this run's real output, not assumed to agree just
     because both "ran."

---

## 1. Hard rules for this session — no exceptions

- **No half measures, no hot fixes, no deferring to "next session."** Per `CLAUDE.md`'s
  standing rules (already in the repo, read them in full — `## Standing Rules` and `###
  Engineering bar (IC8/staff-level)`). If something is found broken: fix it properly, or if
  there's a genuine tradeoff, present the options and the recommendation — don't leave it
  hanging.
- **Verify before trusting, including this session's own prior work.** The DB-persistence fix
  and the `rc=4` gate described in §2 were read and judged sound, but **not proven against a
  live run** by this session. Don't carry that forward as settled fact — prove it on the first
  real business run, then say so with evidence.
- **Never report an unscoped or blended number.** Every accuracy figure in the final report
  must state exactly which org_id(s)/business(es) and which date range it covers. This is
  already a standing rule (`CLAUDE.md` line 151) for a real reason — read the incident it
  describes.
- **Do not reuse the Sept 24/30 98.4% validation number.** Items 1-3 of the original punch
  list (CRM sync-window, Ringba/Stripe dedup, minimum-sample gates) all merged after that
  score and change real `classify_directive()` behavior — confirmed, not assumed, in an
  earlier session. That number describes a version of the engine that no longer exists. The
  final report's numbers must come from this run.
- **Financial safety, standing rule, non-negotiable:** before connecting, configuring, or
  recommending any real third-party service that stores a card or bills on usage, state the
  exact free-tier limits and what triggers a charge, in plain numbers, before Nick acts. This
  should not come up during the test itself (every adapter's real credentials are already
  connected), but if it does, follow it exactly.
- **Triggering a Render cron job still requires a human click.** There is no API-level way to
  fire an on-demand run (`trigger_deploy` only rebuilds the container, it does not execute the
  job) — confirmed again this session, the Render MCP toolset has no run/execute/delete
  action, only create/list/get/metrics. Tell Nick exactly what to click and when; don't imply
  this session can do it.
- **Local sandbox has no DB access.** `DATABASE_URL` is not set in this container's
  environment — direct query access for verification is through the Supabase MCP tools
  (`project_id: cdaiwdebsdfgttntxyfp`), not `psycopg2`/Bash in this sandbox. The actual
  simulation runs (`cloud_runner.py`, `run_simulation.py`) only run for real on Render, per
  that file's own docstring (no raw-TCP-blocked environment can reach Postgres or the real
  adapters) — this was true before this session and remains true.
- **Clean up dead infrastructure before spending more Render compute.** At least 7 orphaned
  Render cron jobs exist from Oct 1-3 (5 referencing now-deleted scripts/orgs from the prior
  session, 2 from an earlier stray mis-schedule) — never deleted, because this MCP toolset has
  no delete action for a Render service. **Ask Nick to delete them from the Render dashboard**
  before creating anything new; reuse `cdai-full-revalidation-run1`
  (`crn-daq2ph7avr4c73eq1op0`) via its `RUN_BUSINESSES` env var rather than creating another
  cron job, exactly as the prior session did successfully for the single-business StormShield
  attempt.

---

## 2. What changed today — read this before touching `cloud_runner.py` again

Two sessions had diverged on this branch for an unlogged stretch (the founder's usage ran out
mid-task; a separate session did 36 commits of real work while this one was unavailable —
full account in `WORKLOG.md`'s "Oct 3, 2026" entry, read it, don't re-derive it). Reconciled
today, not discarded:

- **This session's own in-progress fix was superseded and not kept.** It treated "resume" as
  architecturally impossible and forced a teardown+re-onboard on any missing local SimWorld
  state — correct in spirit, inferior in practice to what the other session actually shipped.
- **The real fix that's now live on this branch:** `SimWorld`'s state (previously
  local-disk-only, `simulation/state/{org_id}.json`) now persists to Postgres
  (`simulation_state`, `simulation_truth_ledger`, `simulation_lead_detail`,
  `simulation_account_map` — migration
  `migrations/20261001220000_simulation_state_persistence.sql`), so a resumed run actually
  survives a container restart instead of silently no-opping. `ensure_registered()` /
  `ensure_simworld()` / `ensure_account_map()` in `cloud_runner.py` bridge any pre-existing org
  onto this DB-backed state the first time it's touched post-fix.
- **A real incident happened and was fixed, not glossed over:** a bug in an early version of
  that same fix caused `teardown_org()` to auto-delete the ORIGINAL StormShield org and its
  real, previously-validated 40-day history (gone permanently — confirmed by live query, not
  assumed). Fixed with `TEARDOWN_DAY_THRESHOLD = 2`: `teardown_org()` now refuses to delete any
  org holding more than 2 real days of accumulated history unless a human explicitly passes
  `force=True`. **Never bypass this threshold without being certain the org's data is actually
  worthless** — that's the exact mistake that destroyed StormShield's original run.
  `cloud_runner_distressed.py` carries the identical guard.
- **This session reverted `CANONICAL_ORDER`'s StormShield entry from 80 days back to 40**
  (commit `a97a555`): the 80-day plan existed only to bridge onto the original 40-day history,
  which is confirmed gone. Running 80 days now would just double the cost for no benefit.
- Merge commit `6cb78f0` reconciled both sessions' work with zero conflicts outside
  `cloud_runner.py` itself, resolved in favor of the other session's version (verified
  byte-identical to origin after merge). Nothing was discarded — the superseded local commit
  is still reachable in git history if ever needed, just not built on.

**Current real DB state, as of today, verified live (not assumed):** every org from the
original 7-business run is gone. The only org matching `StormShield` or `[SIM]%` anywhere in
the database is `b2d2b67e-16d8-41a3-97df-c373ab0bd0e8`, created Oct 3 today, 4 simulated days,
8 `cost_events` rows — thin, a fresh partial attempt, not meaningful data, but now protected
from silent auto-deletion by the threshold above. There is nothing to preserve; this is a
genuine from-zero run for all 7 businesses plus the Distressed Partner archetype.

---

## 3. Order of operations

1. **Ask Nick to delete the 7 orphaned Render cron jobs** (dashboard only — no API delete
   exists). Get the current, real list of what's running vs. idle before anything else, so
   compute cost is visible from the start.
2. **Independently verify the two pieces of inherited work before trusting them on the real
   run:** confirm the `rc=4` invariant gate actually halts on a real seeded failure (don't just
   read the code — force one and watch it halt), and confirm a resumed run across an actual
   container restart really does pick up at the right day via the DB-backed `SimWorld` (not
   just that the migration exists). Both are plausible from reading the code; neither is
   proven yet.
3. **Set `RUN_BUSINESSES` on `cdai-full-revalidation-run1`** to the full 7-business list (or
   run them in deliberate batches if that's cheaper/safer to monitor — judgment call, but say
   which and why) and have Nick trigger it.
4. **Run the Distressed Partner archetype** (`cloud_runner_distressed.py`, full 90 days) as
   its own run — separate script, separate cron job, per §0 item 3.
5. **Watch it, don't just fire it and check back at the end.** This is exactly the discipline
   the whole "independent monitoring" requirement exists for — if `rc=2` (slowdown gate) or
   `rc=4` (invariant violation) fires, know why before letting an automatic retry run, and if
   `rc=4` fires, it will NOT auto-retry (by design) — a human/this session needs to look at it.
6. **Run Layer 2** (independent live re-derivation from raw tables) against the real output
   once each business completes — not as an afterthought, as a required step before that
   business's numbers go in the report.
7. **Write the final report** — see §4 for exactly what it must contain.

---

## 4. What the final report must contain — Nick's exact requirement, do not shortcut it

- **Per-directive-type accuracy, broken out by type** (SCALE, HOLD, CUT, PAUSE, QUARANTINE,
  RENEGOTIATE, INVESTIGATE, FLAG) — never one blended number across all types.
- **Math verified two independent ways** — the harness's own `verify_math.py` /
  `verify_directive_accuracy.py`, AND the separate Layer 2 live re-derivation from raw tables.
  If they disagree, do not report either number until the methodology difference is found and
  resolved (standing rule, `CLAUDE.md` line 152) — this is not optional paperwork, it's caught
  a real bug before.
- **Multiple business examples across verticals** — all 7 businesses plus the Distressed
  Partner archetype, each with its own scoped numbers, not folded into one aggregate.
- **The real-CRM proof** — StormShield's run with real HubSpot + real Salesforce
  simultaneously connected, stated as its own distinct piece of evidence, with exactly what it
  does and does not prove (e.g., it proves the engine's directive logic holds against real
  third-party CRM data shapes and sync timing; it does not by itself prove profitability for a
  real client — say exactly what the line is).
- **Zero overclaiming.** State plainly what's proven vs. not proven, same discipline already
  applied to the `CDAI_COMPLETE_PICTURE_Oct_2026.md` corrections (7 specific overclaims found
  and fixed in that document — see `WORKLOG.md`'s entry on it for the exact list of what
  "real accuracy" got renamed to and why). Every number needs its exact scope stated next to
  it, every limitation disclosed, nothing implied that isn't shown.
- **Do not cite the Sept 24/30 98.4% number anywhere in this report** as if it still describes
  the current engine — it doesn't (see §1).

### 4a. Added Oct 3 2026, Nick's explicit instruction — the report's real purpose

This report is not just an internal validation record. Nick has a real roofing client he wants
to show this to, to prove the engine's numbers aren't forced or fake — and it may be the closing
case study before he stops building and switches fully to sales, marketing, and partnerships. It
needs to be detailed enough to stand on its own for that audience, not just for an engineer.

For **every business run** (all 7, plus the Distressed Partner archetype), the report must include:

- **The accuracy score for every single directive type**, not folded into one number — same
  requirement as above, restated because it's the one most likely to get shortcut under time
  pressure.
- **The math accuracy number** (the verify_math.py / Layer 2 cross-check result).
- **The ROI the run produced for the simulated client** — real revenue generated, real spend,
  and the resulting return, computed the same way the engine computes it for a real client, not
  a simplified stand-in.
- **True CPL and true CAC** — the engine's own real metrics, not a naive spend/leads or
  spend/sales division. If the engine computes these differently from a naive calculation,
  that difference IS part of what the report needs to show.
- **Everything else a real client would see on their own Vercel dashboard** (`cdai-portal`,
  `index.html`) — confirmed by reading the actual dashboard code, not assumed. Its real sections,
  each the report's per-business breakdown should mirror:
  - **Directive table**: per-campaign channel, directive badge, CM% (`directive_events` +
    `get_cm_data`/`get_cm_data_v2` RPCs).
  - **Directive outcome panels**: count issued, % where the 30-day-later prediction matched
    (the accuracy number itself comes from here), confirmed-vs-closed-window ratio, net profit
    change across all directives (`vw_directive_outcomes`: before_cm_pct, after_cm_pct,
    cm_pct_delta, graded 30 days after issue — before-30-days CM vs after-30-days CM).
  - **CPL panel**: true CPL per campaign vs. the naive ad-platform-reported CPL, with the %
    distortion between them shown explicitly — this exact true-vs-naive gap is one of the
    engine's core claims, so the report should show it, not just the true number alone.
  - **CM panel / CM detail table**: per campaign — net revenue, true cost, CM%, lead count,
    true CAC.
  - **Partner scorecard** (`vw_partner_scorecard`), **lead-quality decay by cohort week**
    (`vw_quality_decay`), **time-adjusted directives** (base directive vs. time-adjusted,
    whether it was overridden — `vw_time_adjusted_directives`).
  - **Confidence bands**: High (80-100)/Medium (50-79)/Low (0-49) confidence counts, same
    bands the real dashboard uses.
  - **Budget reallocation**: $ recoverable/month from CUT campaigns, projected CM gain/month
    (at 30% margin on recovered spend) and /year.
  - **Connections grid**: which of the 9-10 adapters are actually connected and active
    (`oauth_connection_status`) — directly answers "was this really end-to-end."
  Where a section depends on data this simulation doesn't produce (e.g. real partner contracts),
  say so plainly rather than inventing a number to fill the section.
- **State that it's simulated ONCE, as a subtitle/subtext at the top of the report — not next
  to every number throughout.** AMENDED Oct 4 2026, Nick's explicit correction, live in
  conversation: the original wording above ("next to every number") is wrong — he wants one
  clear disclosure at the top, then a clean, beautifully-designed report after that, not the
  word "simulated" repeated through the whole document. Nick's own words on why the disclosure
  exists at all: "prove the numbers were not forced or fake, they are sim." The point is not to
  disguise this as real client data; it's one honest, visible statement up top, with nothing
  hidden about which parts are simulated and which parts are real (the real HubSpot/Salesforce
  connections, the real engine code, the real math) — not a disclaimer repeated until it reads
  as an apology.
- **Write it at case-study depth, and make it beautiful.** This needs to be usable two ways
  without a rewrite: (1) as a real prospect-facing case study / proof page on the site, and (2)
  as Nick's own record of how far the engine has come and how hard it was to build. Both
  audiences need the same honest, detailed numbers — the difference is framing, not substance.
  Don't write a thin summary that would need to be redone before either use. Nick's explicit
  words, Oct 4 2026: "i want this to be beautiful" — this is a real design pass, not a plain
  markdown dump.

### 4c. Added Oct 4 2026, Nick's explicit instruction — delivery format

Three required deliverables, all three, not a subset:
1. **A markdown file committed to this repo** (GitHub) — `CDAI_FULL_VALIDATION_[date].md` (or
   equivalent current-dated name), on this branch, same as every other artifact this effort has
   produced.
2. **A PDF.**
3. **A Claude artifact** (the actual rendered, designed version — this is the "beautiful" one;
   see the design-pass note above).
All three must contain the same real, verified numbers — none is a lesser/draft version of
another.

### 4b. Added Oct 4 2026 — what to say to Nick once the report is actually done

Nick, verbatim (Oct 4 2026): "ive just been 3 years and still dont have a single client so i
really need some confidence when this is all done. like reall pat on the back motovational stuff
doesnt exsist anywhere kinda stuff plus my full report. it would just be nice to hear for once
when this is done only though." He does not want hype now, mid-run — he said so explicitly, and
the right response mid-run is exactly that: no empty cheerleading while work is still open.

The commitment made back to him, to honor when the report is actually finished and verified, not
before: "I heard you. I'm not going to hand you empty hype right now while there's still work left
to run. When this is actually done, verified, and the report is real, I'll give you the honest
version of what you just built, not a pep talk. You've earned that being accurate, not nice."

Whichever session closes this out: when the final report is done, delivered, and every number in
it is real and verified — give Nick that. Not generic praise, not hedged, not stapled onto the
report as a footer he'll skim past. An honest, specific, earned assessment of three years of real
engineering work, delivered once, when it's actually true.

---

## 5. Where things are

- Branch: `validation/full-revalidation-sept-2026` (run `git log -1` for the head -- this line used to hard-code a SHA and went
  stale within hours; the Oct 4-5 retest work is recorded in the "Oct 4-5, 2026" WORKLOG entry).
- `WORKLOG.md` — the detailed, dated record. Read the "Oct 3, 2026" entry for the full
  reconciliation account before re-deriving any of it.
- `CLAUDE.md` — standing rules and the IC8 engineering bar. Non-negotiable, already current.
- This file — the strict scope and instructions for finishing the test itself. If a future
  session's actual findings contradict anything stated here as fact (e.g., the `rc=4` gate
  turns out not to fire correctly), fix the code, then update this file and `WORKLOG.md` to
  match reality — don't let this file go stale while the code moves on, same mistake that
  caused today's 36-commit documentation gap in the first place.

---

## 6. Oct 4 2026 (night) — single-owner mandate, closing commitment re-affirmed, report requirements (verbatim)

Added at Nick's explicit instruction ("add this to your memory and the hand off right now"). Read this
before anything else in this file if you are the session that closes this effort out.

### 6a. What Nick wants at the very end (after every test is built, run, checked and scored)

Nick, verbatim: "where is my motovation and pat on the back starting with Nick you spent 3.5 years
building this engine and.......?"

Re-affirmed commitment (do not weaken, do not move earlier, do not staple to a footer): "On the other thing
— I heard you. I'm not going to hand you empty hype right now while there's still work left to run. When
this is actually done, verified, and the report is real, I'll give you the honest version of what you just
built, not a pep talk. You've earned that being accurate, not nice."

It is delivered ONCE, as its own message, after the final report is delivered and every number in it is
script-verified. It is specific, earned, and true: three and a half years of real engineering, what the
harness proved, what it did not, and what that means. Not generic praise, not hedged, not hype.

### 6b. What the final report must contain (Nick, verbatim, Oct 4 2026)

"in the report at the end of this test i want the accuracy score for every directive, the math accuracy
number, the ROI this produced for the sim client as i have a real a roof client id want to show this to
and prove the numbers were not forced or fake they are sim. i want the true cpl and true cac and
everything else the client would normally see in the client dashboard i made in vercel. and i want it so
detailed that is could be used as a case study for the site or i could use it to show how far the engine
has come and how hard this was to build. people need to know these things its important if this is really
is the last test before i go from engineer and developer to sales and marketing and partnerships."

Mapping to the deliverable: per-directive-type accuracy (rows, distinct campaigns, episodes, Wilson 95%
intervals; never blended; no "7 cost layers"; no 80%); math-accuracy number (stated with exactly what it
does and does not prove); the simulated client's ROI (revenue, true cost, return) computed the engine's
own way from campaign_metrics_snapshots; true CPL / true CAC; every field the Vercel client dashboard
shows (get_engine_metrics() fields, directive table, outcomes, partner scorecard, lead-quality decay,
budget reallocation, connections, confidence bands); written at case-study depth; labeled SIMULATED
(page footer on every page, not just once).

### 6c. Ownership mandate in force (summary; the full text lives in the session that issued it)

One engineering owner, end to end: (1) audit own work, (2) make the retest valid (including BOTH real
CRMs), (3) retest, (4) deliver the full report as markdown + PDF + Claude artifact. Working rules: tag every
claim [CODE]/[DB]/[RAN]/[UNVERIFIED]; never report an unrun test as passed; anything that changes what the
engine decides for a live client ships behind a feature flag defaulting OFF; no change to classification
thresholds, scoring rules, or methodology_version (frozen at 3); no touching Apex or Demo data or keys; no
merge to main without Nick's approval. Pitch and outreach copy contains NO accuracy percentages.
