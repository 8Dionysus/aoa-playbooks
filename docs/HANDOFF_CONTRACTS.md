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
