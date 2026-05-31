# Antifragility Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `stress-lanes` | define playbook stress-lane doctrine, schema, and examples | `parts/stress-lanes/docs/`, `parts/stress-lanes/schemas/`, `parts/stress-lanes/examples/` | package validator and stress-lane schema tests | active |
| `reentry-gates` | define explicit re-entry gates for resuming, holding, retiring, or safe-stopping after stress | `parts/reentry-gates/schemas/`, `parts/reentry-gates/examples/` | package validator and re-entry schema tests | active |
| `stress-harvest` | define harvest loops for stressed playbook runs | `parts/stress-harvest/docs/playbook-stress-harvest.md` | package validator and `validate_playbooks.py` | active |
| `runtime-chaos-wave1` | record bounded runtime-chaos degraded-lane posture around `AOA-P-0032` | `parts/runtime-chaos-wave1/docs/playbook-stress-chaos-wave1.md` | runtime-chaos focused tests | active |
| `via-negativa` | keep pruning and negative checks explicit | `parts/via-negativa/docs/via-negativa-checklist.md` | package validator | active |

## Deferred payloads

- `playbooks/runtime-chaos-recovery/PLAYBOOK.md` stays in `playbooks/` as
  source playbook canon.
- Generated registry, activation, federation, review, and landing outputs stay
  in root `generated/`.
- Runtime, eval, memo, KAG, route, and agent truth stay with stronger owners.

## Part growth rule

A part can grow only when it keeps:

- one clear stress or re-entry operation;
- part-local schema/example/doc validation;
- source playbook truth out of the package;
- proof, runtime, memory, KAG, routing, and role authority out of the package.
