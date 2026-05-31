# AGENTS.md

## Applies to

This card applies to `mechanics/checkpoint/`.

## Role

`checkpoint/` is the head-fed and local mechanic for checkpoint return
choreography in playbooks: A2A summon return, checkpoint distillation, and
memo-checkpoint handoff posture.

It does not own memory objects. Checkpoint memory truth remains in `aoa-memo`.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/README.md`,
this package `README.md`, and the source playbooks that mention checkpoint
return.

## Boundaries

- Do not move authored checkpoint playbooks out of `playbooks/`.
- Do not copy or fork `aoa-memo` checkpoint mapping truth into this repo.
- Do not claim automatic child execution, memory writeback, or recall truth.

## Validation

```bash
python mechanics/checkpoint/scripts/validate_checkpoint_package.py
python scripts/validate_playbooks.py
```

## Closeout

Report whether checkpoint docs, activation examples, source playbooks, or
memo-contract refs changed.
