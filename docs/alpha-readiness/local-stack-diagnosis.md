# Local Stack Diagnosis Alpha Readiness

## Readiness Header

- Playbook: `AOA-P-0014 local-stack-diagnosis`
- Lane: `phase-alpha curated-readiness`

Alpha is a readiness proof lane, not composition promotion.

## Fixed Route Order

1. `architect` owns preflight and source-of-truth checks.
2. `coder` performs only the bounded diagnosis pass.
3. `reviewer` closes blocker review and artifact completeness.
4. `evaluator` runs the mapped eval bundles.
5. `memory-keeper` prepares memo writeback.

## Required Evidence

- `examples/alpha_harvests/local-stack-diagnosis.harvest-template.md`
- `docs/alpha-reviewed-runs/2026-04-02.local-stack-diagnosis.md`
- `repo:aoa-agents/examples/alpha_reference_routes/local-stack-diagnosis.example.json`
- `repo:abyss-stack/Logs/phase-alpha/alpha-01-local-stack-diagnosis/verification_pack.json`

## Eval Coverage

- `aoa-verification-honesty`
- `aoa-tool-trajectory-discipline`

## Memo Coverage

- `episode`
- `state_capsule`
- `decision`

## Current Verdict

- `curated-ready`
- `live-ready`

## Next Trigger

- route `alpha-02-self-agent-checkpoint-rollout` may open because the canonical startup path, recurrence pass, and bounded blocker list are now explicit and reviewable
