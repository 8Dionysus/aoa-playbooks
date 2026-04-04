# Local Stack Diagnosis Alpha Harvest Template

## Route Header

- Playbook: `AOA-P-0014 local-stack-diagnosis`
- Lane: `phase-alpha curated-readiness`
- Runtime: primary `llama.cpp` worker with one bounded canonical second pass

## Required Artifacts

- `startup_canon_map`
- `preview_evidence`
- `blocker_list`
- `verification_pack`
- `shareable_summary`

## Eval Anchors

- `aoa-verification-honesty`
- `aoa-tool-trajectory-discipline`

## Memo Writeback

- `episode`
- `state_capsule`
- `decision`

## Stop Conditions

- stop if runtime preflight fails
- stop if the canonical startup path is still unclear after verification
- stop if blockers cannot be bounded to source-owned surfaces

## Evidence Links

- `docs/alpha-reviewed-runs/2026-04-02.local-stack-diagnosis.md`
- `docs/alpha-readiness/local-stack-diagnosis.md`
