# AGENTS.md

## Applies to

This card applies to `mechanics/antifragility/` and every nested path until a
nearer `AGENTS.md` narrows the lane.

## Role

`antifragility/` is the `head-fed/local` playbook mechanic for bounded
stress lanes, re-entry gates, stress harvest, runtime-chaos rehearsal, and via
negativa pruning at the playbook layer.

It receives center pressure from `Agents-of-Abyss/mechanics/antifragility/`,
but this package owns only the playbook-local operation.

## Route by task

- Part payload: use the target part README and exact doc, schema, or example.
- Package topology or provenance: use `README.md`, `PARTS.md`, and
  `PROVENANCE.md`.
- Runtime-chaos scenario meaning: use
  `playbooks/operations/recovery/runtime-chaos-recovery/PLAYBOOK.md`.

## Boundaries

- Source playbook canon stays in `playbooks/operations/recovery/runtime-chaos-recovery/PLAYBOOK.md`.
- Runtime owners own live faults and repair execution.
- `aoa-evals` owns proof, verdicts, and resilience evidence.
- `aoa-memo` owns durable lessons.
- `aoa-kag`, routing, agents, and stats keep their own authority.
- This package may name degraded lanes and re-entry gates; it must not make
  playbooks a runtime repair engine.

## Validation

Run:

Run `VALIDATION.md` in this directory, then the common mechanics route in the root `VALIDATION.md`.

## Closeout

Report which part changed, whether a schema/example moved or changed, whether
source playbook canon moved, which validators ran, and which stronger-owner
boundary stayed intact.
