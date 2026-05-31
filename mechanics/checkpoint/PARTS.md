# Checkpoint Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `summon-return` | keep A2A child return checkpoint route source-owned | `playbooks/a2a-summon-return-checkpoint/PLAYBOOK.md` | `validate_playbooks.py` | source-playbook |
| `distillation-closed-loop` | keep bounded checkpoint distillation route discoverable | `mechanics/checkpoint/parts/distillation-closed-loop/docs/checkpoint-distillation-closed-loop-pilot.md`, `playbooks/checkpoint-distillation-closed-loop-pilot/PLAYBOOK.md` | focused checkpoint test plus package validator | package-local |
| `activation-example` | keep checkpoint activation example root-public | `mechanics/activation/parts/activation-surface/examples/playbook_activation.checkpoint-distillation-closed-loop-pilot.example.json` | focused checkpoint test | package-local |
| `memo-contract-handoff` | route checkpoint-to-memory contract refs to `aoa-memo` | stronger owner path in refs | `validate_playbooks.py` | stronger-owner |

## Deferred payloads

Payloads moved into package-local parts in this package landing.

Root checkpoint docs/examples are active public routes; memo mapping examples
belong to `aoa-memo`.
