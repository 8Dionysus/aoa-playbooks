# Failure Recovery

This document defines the bounded failure posture for the playbook composition layer.

## Core rule

`aoa-playbooks` may own scenario-level failure codes and follow-up recommendations.
It does not own a persisted recovery engine.

## Current surface

`generated/playbook_failure_catalog.json` is derived from `config/playbook_composition_overrides.json`.
It exists to keep a shared failure vocabulary reviewable across the managed playbook cohort.

## What the catalog is for

- naming recurring scenario failures explicitly
- pointing to follow-up skills that reduce ambiguity
- making stop, review, or bounded return posture legible

## What the catalog is not for

- storing run-state packets
- resuming hidden orchestration
- replacing playbook fallback sections
- introducing a tool-level recovery protocol

## Boundary to preserve

Failures stay scenario-owned hints.
Actual execution-state recovery remains outside this repository until a separate runtime home is chosen.

Real-run evidence captured through `examples/harvests/` is reviewable scaffolding, not persisted recovery state, orchestration history, or memory canon.
Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.
If a harvest suggests a new failure or follow-up mapping, that mapping still stays out of `config/playbook_composition_overrides.json` until [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) clears promotion.
`AOA-P-0025 session-growth-cycle` may name stop lines around candidate loss, owner-fit drift, proof overreach, or repair widening, but it does not become a persisted recovery engine for checkpoint carry, proof, memo, or stats.

## Incident-recovery routing boundary

`AOA-P-0020 incident-recovery-routing` may own scenario-level incident mapping, bounded stabilization posture, recovery verification closure, and explicit handoff wording.
It must not be read as a persisted recovery engine, runtime resume protocol, or post-incident remediation runner.
If deeper corrective work remains after stabilization, that work should hand off to a separate governed route such as `AOA-P-0018` rather than continue inside incident recovery by inertia.
