# Playbook Real-Run Workflow

This document defines the repo-first workflow for taking a real operational run from scenario selection to a reviewed summary and then to an explicit gate verdict.

## Core rule

Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.

This workflow is for reviewable summary and verdict surfaces only.
It is not a place to store raw logs, runtime traces, or execution-state packets.

## Route

1. Choose the scenario route through [PLAYBOOK_OPERATIONAL_FAMILY](PLAYBOOK_OPERATIONAL_FAMILY.md).
2. Execute the real run in the owning repository or repositories that actually carry the operational work.
3. Write one reviewed summary in `docs/real-runs/YYYY-MM-DD.<playbook-slug>.md` using the matching source template from `examples/harvests/` plus `Evidence Links`.
4. Update the matching verdict surface under `docs/gate-reviews/` with the latest reviewed run, the dual-signal result, and the current verdict.
5. Consider composition only if the verdict surface moves from `hold` to `ready-for-composition-review`.

## Source templates

The shipped templates under `examples/harvests/` remain the only source templates for reviewed summaries:

- `split-wave-cross-repo-rollout.harvest-template.md`
- `release-migration-cutover.harvest-template.md`
- `incident-recovery-routing.harvest-template.md`

Do not create a second template family for the same summaries.

## Reviewed summary home

`docs/real-runs/` stores short human-reviewed packets only.

A committed summary must:

- use the filename pattern `YYYY-MM-DD.<playbook-slug>.md`
- stay within the allowed slug set for this wave
- reuse the harvest heading set and add `Evidence Links`
- state artifact presence, closure class, follow-on route, composition signals, residual risk, and pointers to external evidence

If no real run has been harvested yet, `docs/real-runs/` should remain empty except for its `README.md`.

## Gate review home

`docs/gate-reviews/` stores one living verdict surface per playbook:

- `split-wave-cross-repo-rollout.md`
- `release-migration-cutover.md`
- `incident-recovery-routing.md`

Each verdict doc keeps the current `hold` versus `ready-for-composition-review` posture explicit without pretending that composition already exists.

## Active first candidates

The first expected reviewed summaries are for `AOA-P-0017` and `AOA-P-0019`.
`AOA-P-0020` uses the same summary and verdict workflow, but only a live incident should open its first reviewed run.

## Boundary to preserve

Do not use this workflow to introduce candidate dossiers, rehearsal artifacts, raw execution traces, or implicit composition promotions.
The only durable outputs in this repository from a real run should be a short reviewed summary and an explicit gate verdict.
