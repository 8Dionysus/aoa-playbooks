# Plan Contours

`plan-contours` publishes the small, typed, runtime-neutral
`aoa_playbook_plan_contour_v1` ABI for selected
playbook routes. It lets a control-plane compiler consume playbook-owned
scenario structure without parsing `PLAYBOOK.md` prose or duplicating that
meaning in a downstream repository.

## Owned surfaces

- source config:
  `config/playbook_plan_contours.json`
- public output schema:
  `schemas/playbook-plan-contours.schema.json`
- deterministic generator:
  `scripts/generate_playbook_plan_contours.py`
- public generated projection:
  `generated/playbook_plan_contours.min.json`
- trusted artifact admission:
  `docs/artifact-bundles/playbook_registry.bundle.json` includes both the
  generated projection and its public schema as materialized subjects
- contract explanation:
  `docs/playbook-plan-contour-contract.md`

The initial ABI covers exactly three C2 golden scenarios:

- `AOA-P-0011 bounded-change-safe`
- `AOA-P-0031 a2a-summon-return-checkpoint`
- `AOA-P-0032 runtime-chaos-recovery`

## Boundary

The contour owns abstract scenario order, dependencies, effect classes,
reviewed-input versus step-output artifact roles, reviewed-boolean branch
guards, and evidence/eval/retention/closeout bindings. It does not own concrete
condition values, commands, prompts, tools, arguments, MCP calls, transports,
models, schedulers, runtime state, or dispatch.

`aoa-sdk` may pin and compile this projection into its own typed `RunPlan`.
The SDK remains responsible for binding a reviewed route decision, concrete
scenario inputs, runtime profile, agent/capability provenance, approvals, and
plan identity. It must also bind every declared condition with reviewed
provenance and prune false guarded steps without fabricating their outputs. A
runtime remains responsible for execution and receipts.
Registry/latest consumers must obtain the contour and schema through the
trusted bundle subject store; the root files alone do not prove admission.

## Validation

The executable focused route is owned by
`mechanics/scenario-composition/AGENTS.md` and the repository release gate.
Run that route after changing this config, schema, generator, or an aligned
source playbook.

Do not hand-edit `generated/playbook_plan_contours.min.json`.
