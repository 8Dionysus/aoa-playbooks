# Playbook Real-Run Harvest

This document defines the evidence-first harvest posture for real runs of selected operational playbooks.

## Core rule

Harvest keeps reviewable evidence.
It does not keep runtime state.

## What harvest is for

- preserving a short, inspectable record of what artifact set actually existed in a real run
- capturing whether the route closed cleanly or handed off residual work
- surfacing possible composition signals without auto-promoting them

## What harvest is not for

- a recovery engine
- an orchestration log
- a persisted run ledger
- a memory canon
- a shortcut around composition review

## Current shipped surface

This repository ships example-only harvest templates at:

- `examples/harvests/split-wave-cross-repo-rollout.harvest-template.md`
- `examples/harvests/release-migration-cutover.harvest-template.md`
- `examples/harvests/incident-recovery-routing.harvest-template.md`

These templates are the only harvest objects validated in this repository.
They exist to keep evidence scaffolding legible without introducing a second runtime substrate.

## Required shape

Each shipped harvest template uses the same section set:

- `Run Header`
- `Entry Signal`
- `Boundary Summary`
- `Required Artifacts`
- `Closure Class`
- `Follow-On Route`
- `Composition Signals`
- `Residual Risk`

## Promotion discipline

Harvest is an input to future composition review, not a promotion signal by itself.
If a real run suggests a new handoff bridge, subagent split, automation seed, or failure/follow-up mapping, that suggestion must still clear [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) before it can enter composition-owned surfaces.
