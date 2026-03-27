# Subagent Patterns

This document defines the bounded subagent recipe posture for `aoa-playbooks`.

## Core rule

Subagent recipes in this repository are explicit scenario helpers.
They are not role canon and they are not automatic orchestration.

## Current surface

`generated/playbook_subagent_recipes.json` is derived from `config/playbook_composition_overrides.json`.
It keeps explicit splits reviewable for scenarios where a bounded parallel pass helps.

## What a recipe may contain

- the owning playbook
- when the split is helpful
- bounded roles inside the split
- exact skill refs
- expected handoff artifacts
- one caution about scope drift

## What a recipe must not become

- automatic spawning logic
- a role registry
- a hidden routing table
- a replacement for the authored playbook

## Boundary to preserve

Use subagent recipes only when the split is clean enough that the main thread can merge back short ledgers instead of raw traces.
