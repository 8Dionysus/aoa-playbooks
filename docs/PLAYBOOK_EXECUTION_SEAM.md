# Playbook Execution Seam

This document defines the bounded execution seam for `aoa-playbooks`.

The goal is not to turn the playbook layer into runtime implementation.
The goal is to expose a small derived activation surface that a runtime can read without replacing the authored playbook bundle.

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

It should not expose:

- execution state
- tool bindings
- MCP or A2A transport
- prompt-tool-server details
- runtime-local memory
- hidden wiring or infrastructure assumptions

If protocol examples are mentioned elsewhere, treat them as examples only, not as playbook canon.

## Reference scenarios

The first reference scenarios for this seam are:

- `AOA-P-0008 long-horizon-model-tier-orchestra`
- `AOA-P-0009 restartable-inquiry-loop`

These are the first runtime-readable playbooks because they already define:

- explicit triggers
- participating agents
- expected artifacts
- evaluation posture
- memory posture
- bounded fallback posture

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
