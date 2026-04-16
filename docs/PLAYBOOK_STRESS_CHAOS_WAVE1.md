# Playbook Stress Chaos Wave 1

This note records the `aoa-chaos-wave1` landing for `aoa-playbooks`.

It does not ask this repository to parse live incident prose or to own runtime
repair. It asks for structured degraded lanes and explicit re-entry gates that
neighboring layers can read without guessing.

## What to own here

- degraded scenario composition
- bounded handoff targets
- re-entry decisions
- explicit reopen scope
- scenario-level evidence expectations

## What not to own here

- skill activation truth
- routing-owned stress meaning
- KAG health truth
- eval verdict meaning
- runtime repair implementation

## Landed route

This wave lands `AOA-P-0032 runtime-chaos-recovery` as the smallest sovereign
playbook that can honestly own these stress-lane and re-entry surfaces without
absorbing owner meaning from `abyss-stack`, `aoa-kag`, `aoa-routing`, or
`aoa-evals`.

Use it when a reviewed runtime stress receipt already exists and the next
honest move is:
- one bounded degraded lane
- one explicit re-entry gate
- source-first regrounding when derived retrieval is unavailable
- proof-facing handoff only after owner evidence exists

## Example surfaces

This wave adds four example surfaces:
- `examples/playbook_stress_lane.runtime-timeout-chaos.example.json`
- `examples/playbook_reentry_gate.runtime-timeout-chaos.example.json`
- `examples/playbook_stress_lane.retrieval-outage-honesty.example.json`
- `examples/playbook_reentry_gate.retrieval-outage-honesty.example.json`

They stay illustrative and machine-readable. They do not turn playbooks into a
runtime log, a repair engine, or a verdict engine.

## Boundary discipline

If a future route already belongs to a stronger sovereign playbook, merge the
stress lane there instead of widening the catalog casually.
If a future route needs full live incident stabilization, shared-root rollout,
or one owner-law refresh decision, prefer `AOA-P-0020`, `AOA-P-0028`, or
`AOA-P-0030` instead of stretching `AOA-P-0032` past its honest shape.
