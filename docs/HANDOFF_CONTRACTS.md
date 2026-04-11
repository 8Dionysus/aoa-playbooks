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
`AOA-P-0017 split-wave-cross-repo-rollout` is the first operational playbook whose post-gate promotion lands here as a minimal playbook-owned handoff bridge.
That bridge is derived from the playbook artifact contract plus upstream skill handoff contracts; it is not copied from source-repo PR prose or from reviewed-summary evidence.

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
If a bounded review lands a handoff bridge, keep that landing scenario-level and skill-derived; do not widen it into routing-specific implementation doctrine.
`AOA-P-0025 session-growth-cycle` currently keeps checkpoint carry, reviewed harvest, seed-stage follow-through, and owner-layer handoff in the authored playbook itself.
That recurring route may later justify a smaller playbook-owned handoff bridge, but not before reviewed evidence proves that the bridge adds scenario value without becoming a hidden runner.
