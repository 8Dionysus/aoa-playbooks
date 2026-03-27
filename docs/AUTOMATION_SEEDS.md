# Automation Seeds

This document defines the automation-seed posture for `aoa-playbooks`.

## Core rule

Automation seeds here are examples only.
They are not live schedules and they are not a canonical automation registry.

## Current surface

`generated/playbook_automation_seeds.json` is derived from `config/playbook_composition_overrides.json`.
The companion Markdown files under `examples/automations/` show human-readable prompt patterns for the same seeds.

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
