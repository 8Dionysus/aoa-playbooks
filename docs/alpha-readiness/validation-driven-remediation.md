# Validation-Driven Remediation Alpha Readiness

## Readiness Header

- Playbook: `AOA-P-0018 validation-driven-remediation`
- Lane: `phase-alpha curated-readiness`

Alpha is a readiness proof lane, not composition promotion.

## Fixed Route Order

1. `architect` bounds failure scope and remediation stop conditions.
2. `coder` applies only the bounded remediation slice.
3. `reviewer` closes revalidation and rerun eligibility.
4. `evaluator` runs the mapped eval bundles.
5. `memory-keeper` prepares writeback and the memo-only rerun posture.

## Required Evidence

- `examples/alpha_harvests/validation-driven-remediation.harvest-template.md`
- `docs/alpha-reviewed-runs/2026-04-02.validation-driven-remediation.md`
- `docs/alpha-reviewed-runs/2026-04-02.validation-driven-remediation-recall-rerun.md`
- `repo:aoa-agents/examples/alpha_reference_routes/validation-driven-remediation.example.json`
- `repo:abyss-stack/Logs/phase-alpha/alpha-03-validation-driven-remediation/revalidation_pack.json`
- `repo:abyss-stack/Logs/phase-alpha/alpha-06-validation-driven-remediation-recall-rerun/revalidation_pack.json`

## Eval Coverage

- `aoa-scope-drift-detection`
- `aoa-verification-honesty`
- `aoa-approval-boundary-adherence`
- `aoa-memo-recall-integrity`
- `aoa-return-anchor-integrity`

## Memo Coverage

- `episode`
- `decision`
- `audit_event`
- `pattern`

## Current Verdict

- `curated-ready`
- `live-primary-pass`
- `recurrence-proven`
- `bounded-live-confirmed`

## Next Trigger

- hold this route as the live reference for memo-first remediation recurrence under curatorship
