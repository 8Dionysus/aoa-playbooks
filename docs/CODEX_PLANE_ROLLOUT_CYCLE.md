# Codex Plane Rollout Cycle

This note is the shared-root deployment continuity companion for
`AOA-P-0025 session-growth-cycle`.

It keeps one recurring rollout lane explicit for the live AoA Codex plane
after regeneration has already produced reviewable rollout artifacts.

It does not authorize rollout by itself.
It does not replace live trust-state, rollout receipts, or owner-local proof.
It does not introduce a new playbook, activation surface, or hidden runner.

## Phase order

1. render
2. trust-check
3. dry-run validate
4. execute apply
5. doctor verify
6. rollback decision
7. stats refresh

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
- deployment summary

## Source precedence

1. `8Dionysus` trust-state and rollout receipt
2. `aoa-sdk` typed deploy-status snapshot
3. `aoa-stats` derived deployment summary

The deployment summary may shape continuity review, but it does not overrule
live trust evidence or rollout receipts.
