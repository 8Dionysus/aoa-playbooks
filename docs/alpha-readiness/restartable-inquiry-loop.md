# Restartable Inquiry Loop Alpha Readiness

## Readiness Header

- Playbook: `AOA-P-0009 restartable-inquiry-loop`
- Lane: `phase-alpha curated-readiness`

Alpha is a readiness proof lane, not composition promotion.

## Fixed Route Order

1. `architect` owns inquiry boundary and checkpoint posture.
2. `reviewer` closes contradiction and checkpoint integrity.
3. `evaluator` runs the mapped eval bundles.
4. `memory-keeper` prepares recall posture for the next pass.

## Required Evidence

- `examples/alpha_harvests/restartable-inquiry-loop.harvest-template.md`
- `docs/alpha-reviewed-runs/2026-04-02.restartable-inquiry-loop.md`
- `repo:aoa-agents/examples/alpha_reference_routes/restartable-inquiry-loop.example.json`
- `repo:abyss-stack/Logs/phase-alpha/alpha-05-restartable-inquiry-loop/inquiry_checkpoint.json`

## Eval Coverage

- `aoa-long-horizon-depth`
- `aoa-return-anchor-integrity`

## Memo Coverage

- `state_capsule`
- `decision`
- `provenance_thread`

## Current Verdict

- `curated-ready`
- `live-ready`

## Next Trigger

- route `alpha-06-validation-driven-remediation-recall-rerun` may open now that checkpoint pause/resume has closed as a live recurrence proof
