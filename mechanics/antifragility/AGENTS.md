# AGENTS.md

## Applies to

This card applies to `mechanics/antifragility/` and every nested path until a
nearer `AGENTS.md` narrows the lane.

## Role

`antifragility/` is the head-fed plus local playbook mechanic for bounded
stress lanes, re-entry gates, stress harvest, runtime-chaos rehearsal, and via
negativa pruning at the playbook layer.

It receives center pressure from `Agents-of-Abyss/mechanics/antifragility/`,
but this package owns only the playbook-local operation.

## Read before editing

Read:

1. root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/HEAD_MECHANICS.md`
4. `mechanics/LOCAL_MECHANICS.md`
5. `mechanics/PLACEMENT_AUDIT.md`
6. this package `README.md`
7. `PARTS.md`
8. target part README/doc/schema/example
9. `playbooks/runtime-chaos-recovery/PLAYBOOK.md` when the runtime-chaos route
   is involved

## Boundaries

- Source playbook canon stays in `playbooks/runtime-chaos-recovery/PLAYBOOK.md`.
- Runtime owners own live faults and repair execution.
- `aoa-evals` owns proof, verdicts, and resilience evidence.
- `aoa-memo` owns durable lessons.
- `aoa-kag`, routing, agents, and stats keep their own authority.
- This package may name degraded lanes and re-entry gates; it must not make
  playbooks a runtime repair engine.

## Validation

Run:

```bash
python mechanics/antifragility/scripts/validate_antifragility_package.py
python scripts/validate_playbooks.py
python -m pytest -q tests/test_antifragility_public_surface.py tests/test_runtime_chaos_recovery.py tests/test_antifragility_mechanics_package.py
```

## Closeout

Report which part changed, whether a schema/example moved or changed, whether
source playbook canon moved, which validators ran, and which stronger-owner
boundary stayed intact.
