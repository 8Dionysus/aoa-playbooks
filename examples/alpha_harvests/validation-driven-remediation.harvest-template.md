# Validation-Driven Remediation Alpha Harvest Template

## Route Header

- Playbook: `AOA-P-0018 validation-driven-remediation`
- Lane: `phase-alpha curated-readiness`
- Runtime: primary `llama.cpp` worker with final memo-only rerun

## Required Artifacts

- `failure_map`
- `boundary_map`
- `remediation_change_set`
- `revalidation_pack`
- `remediation_decision`
- `handoff_record`

## Eval Anchors

- `aoa-scope-drift-detection`
- `aoa-verification-honesty`
- `aoa-approval-boundary-adherence`

## Memo Writeback

- `episode`
- `decision`
- `audit_event`

## Stop Conditions

- stop if failure scope cannot be bounded
- stop if remediation widens beyond the named change axis
- stop if revalidation remains blocked after reviewer closure

## Evidence Links

- `docs/alpha-reviewed-runs/2026-04-02.validation-driven-remediation.md`
- `docs/alpha-readiness/validation-driven-remediation.md`
