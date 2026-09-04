# AGENTS.md

## Applies to

This card applies to `mechanics/checkpoint/`.

## Role

`checkpoint/` is the `head-fed/local` mechanic for checkpoint return
choreography in playbooks: A2A summon return, checkpoint distillation, and
memo-checkpoint handoff posture.

It does not own memory objects. Checkpoint memory truth remains in `aoa-memo`.

## Route by task

Use the exact checkpoint doc or source playbook that owns the return
choreography. Use `README.md` for package topology or stronger-owner route
orientation.

## Boundaries

- Do not move authored checkpoint playbooks out of `playbooks/`.
- Do not copy or fork `aoa-memo` checkpoint mapping truth into this repo.
- Do not claim automatic child execution, memory writeback, or recall truth.

## Validation

Run `VALIDATION.md` in this directory, then the common mechanics route in the root `VALIDATION.md`.

## Closeout

Report whether checkpoint docs, activation examples, source playbooks, or
memo-contract refs changed.
