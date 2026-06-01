# Checkpoint Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | head-fed/local |
| role | keep checkpoint return and distillation routes explicit without absorbing memo truth |
| trigger | A2A summon return changes, checkpoint distillation changes, memo checkpoint posture changes, or activation examples for checkpoint routes |
| playbooks owns | checkpoint choreography and source playbook return posture |
| stronger owner split | `aoa-memo` owns checkpoint memory contracts and durable recall truth |
| inputs | source playbooks, checkpoint distillation doc, activation example, memo contract refs |
| outputs | checked package-local checkpoint posture and stronger-owner handoff |
| must not claim | memory write, recall truth, child automation authority, or hidden scheduler action |
| validation | `python mechanics/checkpoint/scripts/validate_checkpoint_package.py` |
| next route | source playbook, activation example, `aoa-memo`, or recurrence mechanic |

## Active route

This package is active as package-local checkpoint posture.

`mechanics/checkpoint/parts/distillation-closed-loop/docs/checkpoint-distillation-closed-loop-pilot.md`
is package-local and still public as a playbook-layer route through README,
docs-map, and focused tests.

## Source surfaces

- `mechanics/checkpoint/parts/distillation-closed-loop/docs/checkpoint-distillation-closed-loop-pilot.md`
- `playbooks/a2a-summon-return-checkpoint/PLAYBOOK.md`
- `playbooks/checkpoint-distillation-closed-loop-pilot/PLAYBOOK.md`
- `mechanics/activation/parts/activation-surface/examples/playbook_activation.checkpoint-distillation-closed-loop-pilot.example.json`

## Stronger owner route

The path
`mechanics/checkpoint/parts/checkpoint-to-memory-mapping/examples/checkpoint_to_memory_contract.example.json`
is a playbook-layer reference to the stronger `aoa-memo` checkpoint mapping
contract, not a local copied payload.
