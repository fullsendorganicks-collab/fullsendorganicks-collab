# CDAI retest — your click list (Oct 5, 2026)

Everything below is already set up. Code is on the validation branch at commit `bcc6820`; the production database has the new tables;
every cron below has its settings and finished building at 00:53 UTC. **You only click "Trigger Run".** I watch the logs myself.

Run tag: `v3`. Each business runs 3 seeds one after the other (orgs `[SIM] <Business> [v3-s1]`, `-s2`, `-s3`). The two real-CRM businesses then run one
extra pass against the real HubSpot / Salesforce dev account (`[v3-f]`). Nothing from the Oct 4 run is touched or reused.
(Cron names still show the old day counts — the real lengths come from the code: 81 / 90 / 90 / 105 / 120 / 150 / 150 / 210 days.)

## Step 1 — click now (about 1 minute apart, any order)
| # | Cron | Link | Sim days (×3 seeds) | Expected wall time* |
|---|---|---|---|---|
| 1 | cdai-run-eversure-40days | https://dashboard.render.com/cron/crn-db0stj2d0e5s73d2onl0 | 81 | 1.0 – 3.0 h |
| 2 | cdai-run-sunpeak-65days | https://dashboard.render.com/cron/crn-db0stjqd0e5s73d2opo0 | 90 | 1.1 – 3.4 h |
| 3 | cdai-run-westbridge-125days | https://dashboard.render.com/cron/crn-db0stlegekts73b5cdqg | 120 | 1.5 – 4.5 h |
| 4 | cdai-run-harborview-115days | https://dashboard.render.com/cron/crn-db0stknavr4c7396ton0 | 150 | 1.9 – 5.6 h |
| 5 | cdai-run-distressed-partner-90days | https://dashboard.render.com/cron/crn-db0strmgekts73b5d54g | 150 | 1.9 – 5.6 h |
| 6 | cdai-run-apex-230days | https://dashboard.render.com/cron/crn-db0stm2d0e5s73d2p1k0 | 210 | 2.6 – 7.9 h |

## Step 2 — also click now: the two real-CRM crons, in REHEARSAL mode (about 2 minutes each, deletes nothing)
| # | Cron | Link |
|---|---|---|
| 7 | cdai-run-stormshield-80days-v2 | https://dashboard.render.com/cron/crn-db09jelg1s2s73d54fug |
| 8 | cdai-run-pinnacle-115days | https://dashboard.render.com/cron/crn-db0r2dfavr4c738vpm00 |

These two are set to a dry run of the real-CRM clean-up (`SIM_PREFLIGHT=1`). Tell me "rehearsal clicked". I read the logs; if both end with
`[PREFLIGHT] ALL OK` I switch them to the real run and you click each of them **once more**. If either fails I tell you exactly why and fix it first.
Real run after the rehearsal: StormShield 3 seeds × 90 days, then 45 real-HubSpot days — about 2.7 – 8.1 h. Pinnacle 3 seeds × 105 days, then 45
real-Salesforce days — about 2.9 – 5.9 h. (Real HubSpot is the slow part: ~375 s per simulated day on Oct 4.)

*Estimates use 15 – 45 s per simulated day for mocked vendors (Oct 4 on Render was ~10 – 20 s) and Oct 4's measured 131 – 375 s per day for the real CRMs.
They are estimates; the log will show the real pace within the first hour.

## What a healthy cron looks like (first lines in its Logs tab, within ~2 minutes of clicking)
```
[CLOUD_RUNNER] ######## pass tag=v3-s1 base_seed=1 real_crm=False clean_crm=True utm_coverage=0.8 businesses=['<Business>']
[CLOUD_RUNNER] ==== [SIM] <Business> [v3-s1] (vertical=..., days=..., attempt 1/25) ====
[CLOUD_RUNNER] [SIM] <Business> [v3-s1] at day 0/... — running ... more.
```
then a simulated-day counter that keeps advancing. (Distressed prints `[DISTRESSED_RUNNER] ==== [SIM] Distressed Partner Archetype [v3-s1] ...`.)
Rehearsal prints `[PREFLIGHT] ... rc=0 (OK)` and `[PREFLIGHT] ALL OK`, then the job ends green.

**The `days=` value in the second line must be exactly this (I check it for every cron within minutes of your click; env values cannot be read back, so this line is the proof):**
| Cron | `days=` | Business string in the log |
|---|---|---|
| cdai-run-eversure-40days | 81 | EverSure Independent Insurance |
| cdai-run-sunpeak-65days | 90 | SunPeak Residential Solar |
| cdai-run-westbridge-125days | 120 | Westbridge Injury Law |
| cdai-run-harborview-115days | 150 | HarborView Senior Living Advisors |
| cdai-run-distressed-partner-90days | 150 | Distressed Partner Archetype |
| cdai-run-apex-230days | 210 | Apex Trial Recruitment Partners |
| cdai-run-stormshield-80days-v2 (real run) | 90, then 45 for `[v3-f]` | StormShield Roofing |
| cdai-run-pinnacle-115days (real run) | 105, then 45 for `[v3-f]` | Pinnacle Home Lending |
If a number differs, cancel that run and tell me the cron name -- I fix it before it burns hours.
Oct 5 01:34 UTC: I found the Distressed cron would have run 90 days (its start command exports `DISTRESSED_RUN_DAYS=90`); I set `SIM_RUN_DAYS=150` on it and the rebuild went live 01:35:53 UTC. Its first log line is the proof it took.

Red flags — tell me the cron name, nothing else is needed:
`HALTING` in the log (exit 5 = no real CRM connection to carry over, 6 = run tag missing, 7 = real-CRM clean-up failed), a job that ends red, or a day counter that stops for 15+ minutes.

## Step 3 — later (I tell you when; do not click early)
| When | Cron | Link |
|---|---|---|
| After StormShield's real-HubSpot pass finishes | cdai-verify-stormshield-hubspot | https://dashboard.render.com/cron/crn-db0upgmgekts73bcnet0 |
| After Pinnacle's real-Salesforce pass finishes | cdai-verify-pinnacle-salesforce | https://dashboard.render.com/cron/crn-db0uphc9v7es73d49780 |
| After all runs finish AND I have merged the final code | cdai-verify-db-retry-fix (full test suite) | https://dashboard.render.com/cron/crn-db0t64lg1s2s73fi9un0 |
| Same time, after I set `SIM_RUN_TAG=v3` on it | cdai-full-report-data-v1 (collector) | https://dashboard.render.com/cron/crn-db0vqgou01pc73c63aqg |
The two verifiers take about 2 minutes each and compare what the real CRM holds with what the engine ingested.

## DO NOT CLICK (old one-off jobs that are still active on the same branch; running them can damage retest data)
* cdai-teardown-distressed-partner — https://dashboard.render.com/cron/crn-db0u29dg1s2s73flo5cg (one-off: force-tears down a completed Distressed run)
* cdai-split-crm-stormshield-pinnacle — https://dashboard.render.com/cron/crn-db0r0ahsrm7s738qics0 (one-off: moves the real CRM connections between StormShield and Pinnacle; already done)
* cdai-rebuild-stormshield — https://dashboard.render.com/cron/crn-db08vdugekts738m44m0 (one-off: force-tears down and rebuilds the StormShield org)
* cdai-create-hubspot-utm-property — https://dashboard.render.com/cron/crn-db0qa01srm7s738nvlbg (one-off: creates a HubSpot property; already done)
Every `cdai-validation-*`, `cdai-stormshield-*`, `cdai-distressed-partner-run*`, `cdai-full-revalidation-run1`, `cdai-layer1-gate-proof-v3` and `cdai-salesforce-field-probe` job is suspended; leave them suspended.

## What I deliberately did differently from the sequencing note
StormShield and Pinnacle are not run strictly one after the other: they use different vendors (HubSpot vs Salesforce), each cleans and ingests only its own portal, and strict sequencing would add up to ~6 hours. If you prefer strict order, click Pinnacle only after StormShield's real run ends — nothing else changes.

## What this does not need from you
No credentials, no OAuth clicks, no environment variables, no sending logs. Do not push to the `validation/full-revalidation-sept-2026` branch while these run — every push redeploys these crons, and I have not verified that a redeploy leaves a running job alone. I keep my follow-up work on a separate branch (`validation/phase3-followups`) until the runs finish.
