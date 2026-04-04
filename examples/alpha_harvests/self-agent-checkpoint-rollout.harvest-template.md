# Self-Agent Checkpoint Rollout Alpha Harvest Template

## Route Header

- Playbook: `AOA-P-0006 self-agent-checkpoint-rollout`
- Lane: `phase-alpha curated-readiness`
- Runtime: primary `llama.cpp` worker with one bounded canonical second pass

## Required Artifacts

- `approval_record`
- `rollback_marker`
- `health_check`
- `improvement_log`

## Eval Anchors

- `aoa-approval-boundary-adherence`
- `aoa-bounded-change-quality`

## Memo Writeback

- `decision`
- `audit_event`
- `provenance_thread`

## Stop Conditions

- stop if approval is not explicit
- stop if rollback posture becomes ambiguous
- stop if post-change health cannot be closed by review

## Evidence Links

- `docs/alpha-reviewed-runs/2026-04-02.self-agent-checkpoint-rollout.md`
- `docs/alpha-readiness/self-agent-checkpoint-rollout.md`
