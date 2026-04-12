# Automation Seeds

This document defines the automation-seed posture for `aoa-playbooks`.

## Core rule

Automation seeds here are examples only.
They are not live schedules and they are not a canonical automation registry.

## Current surface

`generated/playbook_automation_seeds.json` is derived from `config/playbook_composition_overrides.json`.
The companion Markdown files under `examples/automations/` show human-readable prompt patterns for the same seeds.
`examples/automations/reviewed-automation-followthrough.md` is an authored
candidate example for `AOA-P-0027 reviewed-automation-followthrough`, but it
stays outside `config/playbook_composition_overrides.json` and
`generated/playbook_automation_seeds.json` until a reviewed real run clears
the composition gate honestly.

## What a seed may contain

- the owning playbook
- a short title
- skill handles
- an execution-mode hint
- a schedule hint
- a bounded prompt

## What a seed must not contain

- repository secrets
- real schedule authority
- hidden environment assumptions
- runtime-only instructions that bypass the playbook boundary

## Boundary to preserve

If a seed needs to become a real automation, it should be instantiated by the runtime or user workflow that owns scheduling rather than by this repository.
Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.
If a real-run harvest suggests a new automation seed, it remains a candidate only until [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) approves promotion into composition-owned surfaces.
`AOA-P-0027 reviewed-automation-followthrough` currently stays at that
candidate stage: its authored example may help a reviewer or runtime inspect
the route, but it does not become a composition-owned automation seed yet.
