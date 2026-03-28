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

## Incident-recovery routing boundary

`AOA-P-0020 incident-recovery-routing` may own scenario-level incident mapping, bounded stabilization posture, recovery verification closure, and explicit handoff wording.
It must not be read as a persisted recovery engine, runtime resume protocol, or post-incident remediation runner.
If deeper corrective work remains after stabilization, that work should hand off to a separate governed route such as `AOA-P-0018` rather than continue inside incident recovery by inertia.
