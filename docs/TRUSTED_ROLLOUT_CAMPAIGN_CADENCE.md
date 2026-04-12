# Trusted Rollout Campaign Cadence

This note is the bounded cadence adjunct for
`AOA-P-0028 trusted-rollout-operations`.

Use it when the route is no longer just one checked-in rollout history line but
one grouped maintenance cadence over that history.

It remains companion-only.
It is not a second playbook.
It is not a hidden runner.
It is not a scheduler.

## Core route

`rollout_campaign_window -> drift_review_window -> rollback_followthrough_window? -> summary refresh -> bounded memo writeback`

These windows stay source-owned in `8Dionysus`.
This repository only names the scenario-level adjunct posture around them.

## What this adjunct keeps explicit

- one bounded campaign window rather than loose repeated maintenance
- one drift-review window with named signals and one explicit decision
- one rollback-followthrough window when rollback remains contingent
- the return path into `AOA-P-0028` evidence and stop-lines

## Boundary

Prefer:

1. deploy-local trust-state and rollout receipt
2. checked-in trusted rollout history in `8Dionysus/generated/codex/rollout/`
3. source-owned cadence windows in `8Dionysus/examples/*.example.json`
4. `aoa-stats` derived cadence summaries
5. `aoa-memo` cadence-shaped recall objects

This adjunct does not:

- mint a new playbook id
- create activation or federation ownership
- replace source-owned cadence windows
- let stats, memo, or sdk speak stronger than owner truth
