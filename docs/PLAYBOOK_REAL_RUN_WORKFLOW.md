# Playbook Real-Run Workflow

This document defines the repo-first workflow for taking a real operational run from scenario selection to a reviewed summary and then to an explicit gate verdict.

## Core rule

Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.

This workflow is for reviewable summary and verdict surfaces only.
It is not a place to store raw logs, runtime traces, or execution-state packets.

## Route

1. Choose the scenario route through [PLAYBOOK_OPERATIONAL_FAMILY](PLAYBOOK_OPERATIONAL_FAMILY.md).
2. Execute the real run in the owning repository or repositories that actually carry the operational work.
3. Select only a closed case that clearly satisfies the playbook boundary, the required anchor artifacts, and reviewable `Evidence Links`.
4. If selection finds no qualifying case, do not create a placeholder summary; leave `docs/real-runs/` unchanged and keep the matching gate at `hold`.
5. If a case qualifies, write one reviewed summary in `docs/real-runs/YYYY-MM-DD.<playbook-slug>.md` using the matching source template from `examples/harvests/` plus `Evidence Links`.
6. Update the matching verdict surface under `docs/gate-reviews/` with the latest reviewed run, the dual-signal result, and the current verdict.
7. Consider composition only if the verdict surface moves from `hold` to `ready-for-composition-review`; if a bounded review lands a composition-owned adjunct, move the verdict to `composition-landed`.

## Source templates

The shipped templates under `examples/harvests/` remain the only source templates for reviewed summaries:

- `split-wave-cross-repo-rollout.harvest-template.md`
- `validation-driven-remediation.harvest-template.md`
- `release-migration-cutover.harvest-template.md`
- `incident-recovery-routing.harvest-template.md`
- `owner-first-capability-landing.harvest-template.md`
- `closeout-owner-follow-through-continuity.harvest-template.md`
- `session-growth-cycle.harvest-template.md`
- `trusted-rollout-operations.harvest-template.md`
- `federated-live-publisher-activation.harvest-template.md`

Do not create a second template family for the same summaries.

## Reviewed summary home

`docs/real-runs/` stores short human-reviewed packets only.

A committed summary must:

- use the filename pattern `YYYY-MM-DD.<playbook-slug>.md`
- stay within the allowed slug set for this wave
- reuse the harvest heading set and add `Evidence Links`
- state artifact presence, closure class, follow-on route, composition signals, residual risk, and pointers to external evidence
- contain at least one reviewable Markdown link in `Evidence Links`

If a playbook has no harvested real run yet, its gate should remain at `hold` and no placeholder summary should be committed for that playbook.
A selection pass that finds no qualifying case should leave the matching playbook summary absent rather than inventing one.

## Gate review home

`docs/gate-reviews/` stores one living verdict surface per playbook:

- `split-wave-cross-repo-rollout.md`
- `validation-driven-remediation.md`
- `release-migration-cutover.md`
- `incident-recovery-routing.md`
- `owner-first-capability-landing.md`
- `closeout-owner-follow-through-continuity.md`
- `federated-live-publisher-activation.md`
- `trusted-rollout-operations.md`

Each verdict doc keeps the current `hold`, `ready-for-composition-review`, or `composition-landed` posture explicit without pretending that composition exists before it really lands.
If a bounded review does land composition, the verdict doc should move to `composition-landed` rather than leaving the playbook in a permanent pre-promotion state.

## Active first candidates

The remaining first-run evidence gaps are now `AOA-P-0019` and `AOA-P-0020`.
`AOA-P-0017` now has reviewed summaries at `docs/real-runs/2026-03-21.split-wave-cross-repo-rollout.md`, `docs/real-runs/2026-03-28.split-wave-cross-repo-rollout.md`, and `docs/real-runs/2026-04-07.split-wave-cross-repo-rollout.md`, and its composition-landed handoff bridge now covers both routing-adjacent and surface-detection split-wave closures.
`AOA-P-0018` now has a first qualifying general reviewed summary at `docs/real-runs/2026-04-05.validation-driven-remediation.md`, and its gate remains `hold` pending a second different-family remediation run or a stable adjunct candidate.
`AOA-P-0021` now has reviewed summaries at `docs/real-runs/2026-04-07.owner-first-capability-landing.md`, `docs/real-runs/2026-04-08.owner-first-capability-landing.md`, and `docs/real-runs/2026-04-08.owner-first-capability-landing.tos-graph-curation.md`, and its gate remains `composition-landed` because the route now proves a stable owner-first landing bridge from staged lineage intake to merged owner truth and post-merge reality sync across remediation-heavy, inspect-first via-negativa, and bounded runtime-hardening families.
`AOA-P-0023` now has reviewed summaries at `docs/real-runs/2026-04-08.closeout-owner-follow-through-continuity.md`, `docs/real-runs/2026-04-09.closeout-owner-follow-through-continuity.workspace-checkpoint-growth.md`, and `docs/real-runs/2026-04-13.closeout-owner-follow-through-continuity.aoa-kag-owner-followthrough.md`, and its gate remains `composition-landed` because the route now proves the same continuity bridge from reviewed closeout through owner handoff, bounded owner authorship, and merged closure across canonical skill-bundle landing, repo-local quest continuity capture, and bounded eval-owned proof carry.
`AOA-P-0024` now has a first qualifying reviewed summary at `docs/real-runs/2026-04-07.federated-live-publisher-activation.md`, and its gate remains `hold` because the route now proves a real owner-local publisher activation closure but not yet a stable playbook-owned adjunct candidate.
As of April 12, 2026, `AOA-P-0019` still has no qualifying reviewed summary committed.
`AOA-P-0020` uses the same summary and verdict workflow, but only a live incident should open its first reviewed run.
`AOA-P-0025` now has a first qualifying reviewed summary at `docs/real-runs/2026-04-12.session-growth-cycle.md`, which proves one real lineage-bound session-growth route across reviewed closeout, seed-trace continuity, owner landings, proof-adjacent follow-through, bounded writeback, and derived stats visibility. It remains ungated and outside composition-owned adjunct surfaces until a later review decides that gate posture explicitly.
`AOA-P-0028` now has reviewed summaries at `docs/real-runs/2026-04-11.trusted-rollout-operations.initial-stable-regen.md` and `docs/real-runs/2026-04-11.trusted-rollout-operations.md`, and its gate remains `hold` because the stabilized-plus-rollback pair still proves route identity more strongly than it proves a stable playbook-owned adjunct.
Its shared-root deployment continuity lane still lives at
`docs/CODEX_PLANE_ROLLOUT_CYCLE.md` plus
`examples/codex_plane_rollout_lane.example.json`, but that companion does not
count as a reviewed run or a gate verdict by itself.

## Boundary to preserve

Do not use this workflow to introduce candidate dossiers, rehearsal artifacts, raw execution traces, or implicit composition promotions.
The only durable outputs in this repository from a real run should be a short reviewed summary and an explicit gate verdict.
