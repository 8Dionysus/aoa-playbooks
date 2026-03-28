# Handoff Contracts

This document defines the bounded handoff bridge for the composition surfaces in `aoa-playbooks`.

## Core rule

`aoa-playbooks` may publish derived handoff packets for scenarios.
It must not absorb skill meaning from `aoa-skills`.

## Source of truth

`generated/playbook_handoff_contracts.json` is derived from:

- `playbooks/*/PLAYBOOK.md`
- `config/playbook_composition_overrides.json`
- `../aoa-skills/generated/skill_handoff_contracts.json`

Reviewable evidence templates for future handoff candidates also live under `examples/harvests/`.
They are governed by [PLAYBOOK_REAL_RUN_HARVEST](PLAYBOOK_REAL_RUN_HARVEST.md) and do not create new composition entries by themselves.
Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.

The playbook bundle still owns the scenario route.
`aoa-skills` still owns the bounded execution unit.

## What the handoff bridge may contain

- exact `required_skills`
- derived decision points and handoff bullets
- expected artifacts and return anchors
- refs back to the skill-derived handoff contracts
- a compact playbook-level packet template

## What it must not contain

- persisted run state
- hidden runtime routing
- tool bindings
- transport contracts
- a second authored playbook object

## Boundary to preserve

If a handoff packet starts encoding runtime-local recovery or execution state, it has crossed out of the playbook layer.
If a new handoff bridge candidate appears in a real-run harvest, it must still clear [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) before it can enter `config/playbook_composition_overrides.json`.
