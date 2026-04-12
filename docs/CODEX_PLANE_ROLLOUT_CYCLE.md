# Codex Plane Rollout Cycle

This note is the shared-root deployment continuity companion for
`AOA-P-0028 trusted-rollout-operations`.

It keeps one recurring rollout lane explicit for the live AoA Codex plane
after regeneration has already produced reviewable rollout artifacts and
`8Dionysus` is publishing checked-in rollout campaign history.

It does not authorize rollout by itself.
It does not replace live trust-state, rollout receipts, or owner-local proof.
It does not introduce a new playbook, activation surface, or hidden runner.
The grouped cadence adjunct for repeated maintenance lives in
`docs/TRUSTED_ROLLOUT_CAMPAIGN_CADENCE.md` and stays subordinate to
`AOA-P-0028` rather than becoming a second playbook.

## Phase order

1. render
2. trust-check
3. dry-run validate
4. execute apply
5. doctor verify
6. activate bounded rollout
7. observe drift window
8. repair or rollback
9. publish rollout history
10. stats refresh
11. memo writeback

## Cadence adjunct

When the same shared-root route needs one grouped review window above the
checked-in rollout history, keep the adjunct explicit as:

- `rollout_campaign_window`
- `drift_review_window`
- `rollback_followthrough_window`

Those windows stay source-owned in `8Dionysus`.
This companion only names the recurring lane around them.

## Stop lines before apply

- trust posture is `root_mismatch`
- trust posture is `config_inactive`
- stable MCP names drift from `aoa_workspace`, `aoa_stats`, and `dionysus`
- dry-run validation fails

## Rollback recommendation after apply

- doctor returns `fail`
- hooks are not active
- project config is not active
- drift is detected immediately after rollout

## Required artifacts

- trust-state
- regeneration report
- rollout receipt
- deploy-status snapshot
- rollout campaign record
- drift window record
- rollback window record
- rollout campaign window
- drift review window
- rollback followthrough window
- rollout operations summary
- rollout drift summary
- memo writeback record

## Source precedence

1. `8Dionysus` trust-state and rollout receipt
2. `8Dionysus` checked-in rollout campaign history
3. `aoa-sdk` typed deploy-status snapshot
4. `aoa-stats` derived deployment, rollout-operations, and drift summaries

The deployment summary may shape continuity review, but it does not overrule
live trust evidence, checked-in rollout history, or rollout receipts.
