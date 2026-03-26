# Playbook Execution Seam

This document defines the bounded execution seam for `aoa-playbooks`.

The goal is not to turn the playbook layer into runtime implementation.
The goal is to expose a small derived activation surface that a runtime can read without replacing the authored playbook bundle, while keeping a separate federation-readable surface for cross-repo closure checks.

## Core rule

`aoa-playbooks` owns executable scenario composition at the playbook layer.

It does not own:

- agent taxonomy
- skill execution
- eval doctrine
- memory taxonomy
- routing logic
- runtime or network implementation

Those neighboring layers stay authoritative for their own objects.

## Canonical source of truth

The canonical authored surfaces remain:

- `generated/playbook_registry.min.json`
- `playbooks/*/PLAYBOOK.md`

The activation surface is derived from those source-owned objects.
It exists to make recurring scenarios runtime-readable without adding a second authored playbook object.
The current compiled activation output lives at `generated/playbook_activation_surfaces.min.json` and is produced by `scripts/generate_playbook_activation_surfaces.py`.

The current compiled federation output lives at `generated/playbook_federation_surfaces.min.json` and is produced by `scripts/generate_playbook_federation_surfaces.py`.
It is a validator-facing closure surface, not a runtime execution interface.

## Activation surface

The derived activation surface should stay compact.
It should expose only the fields a runtime needs to understand:

- which playbook this is
- which scenario it names
- when it triggers
- which agents participate
- which skill families are expected
- which artifacts should exist
- which evaluation and memory posture apply
- which fallback mode governs the route
- which compact return hints govern an honest re-entry when the route loses axis

It should not expose:

- execution state
- tool bindings
- MCP or A2A transport
- prompt-tool-server details
- runtime-local memory
- hidden wiring or infrastructure assumptions

If protocol examples are mentioned elsewhere, treat them as examples only, not as playbook canon.

## Current activation scenarios

The current activation-eligible scenarios for this seam are:

- `AOA-P-0008 long-horizon-model-tier-orchestra`
- `AOA-P-0009 restartable-inquiry-loop`
- `AOA-P-0010 cross-repo-boundary-rollout`

These runtime-readable playbooks already define:

- explicit triggers
- participating agents
- expected artifacts
- evaluation posture
- memory posture
- bounded fallback posture
- compact return posture where the route may need governed re-entry

The activation surface may project:
- `return_posture`
- `return_anchor_artifacts`
- `return_reentry_modes`

These fields describe where the scenario may return, not how a runtime performs that return.

Their derived activation entries are validated against the generated collection and the matching fixture examples in `examples/`.

## Federation surface

The federation surface should stay compact.
It should expose only the fields needed to check cross-repo closure:

- which playbook this is
- which agents participate
- which exact skills must resolve in `aoa-skills`
- which eval anchors must resolve in `aoa-evals`
- which memo contracts must resolve in `aoa-memo`
- which memo writeback kinds the route allows

It should not expose:

- runtime execution state
- transport details
- hidden cross-repo wiring
- new memo or skill semantics invented inside `aoa-playbooks`

## Current federation-checked cohort

The current federation-checked playbooks for this seam are:

- `AOA-P-0007 witness-to-compost-pilot`
- `AOA-P-0008 long-horizon-model-tier-orchestra`
- `AOA-P-0009 restartable-inquiry-loop`
- `AOA-P-0010 cross-repo-boundary-rollout`

Their derived federation entries are validated against `aoa-skills/generated/governance_backlog.json` and the referenced `aoa-memo/examples/*.json` contracts.

## Boundary to preserve

The activation surface may help a runtime read playbooks.
It must not turn the playbook layer into:

- an agent registry
- a skill runner
- an eval engine
- a memory store
- a transport spec

The playbook still owns the recurring scenario route.
The runtime only reads a bounded projection of that route.
