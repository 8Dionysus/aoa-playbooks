# Playbook Composition Gates

This document is the canonical gate surface for promoting selected operational playbooks from `A+Act+F` toward composition.

## Core rule

No new adjunct reaches `config/playbook_composition_overrides.json` until a real run proves both recurrence and distinct playbook-owned value.
Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.
A selection pass that finds no qualifying case keeps the verdict surface at `hold` and creates no reviewed summary.

The minimum evidence threshold for every gate in this document is one real run.
The living per-playbook verdict surfaces sit under `docs/gate-reviews/` and record the current `hold` versus `ready-for-composition-review` posture.

## AOA-P-0017 split-wave-cross-repo-rollout

- Required real-run artifact set: `wave_plan`, `bridge_surface_pack`, `downstream_revalidation_pack`, `handoff_record`
- Minimum evidence threshold: one real ordered-wave run
- Required dual signal for promotion:
  - at least one stable failure or follow-up mapping not already covered by `AOA-P-0010` or the shared failure catalog
  - at least one stable adjunct candidate in the form of a `handoff bridge`, `subagent split`, or `automation seed`
- Artifact anchor: `wave_plan`, `bridge_surface_pack`, `downstream_revalidation_pack`, `handoff_record`
- Non-promotion default: if the run only shows one-off rollout noise or weak signal, keep `AOA-P-0017` at `A+Act+F`

## AOA-P-0019 release-migration-cutover

- Required real-run artifact set: `cutover_plan`, `cutover_decision`, `post_cutover_verification_pack`, `handoff_record`
- Minimum evidence threshold: one real cutover run
- Required dual signal for promotion:
  - at least one stable failure or follow-up mapping not already covered by neighboring cutover or rollout playbooks or the shared failure catalog
  - at least one stable adjunct candidate in the form of a `handoff bridge`, `subagent split`, or `automation seed`
- Artifact anchor: `cutover_plan`, `cutover_decision`, `post_cutover_verification_pack`, `handoff_record`
- Non-promotion default: if the run only confirms existing cutover wording, keep `AOA-P-0019` at `A+Act+F`

## AOA-P-0020 incident-recovery-routing

- Required real-run artifact set: `incident_map`, `stabilization_plan`, `recovery_decision`, `recovery_verification_pack`, `handoff_record`
- Minimum evidence threshold: one real incident recovery run
- Required dual signal for promotion:
  - at least one stable failure or follow-up mapping not already covered by neighboring recovery or remediation playbooks or the shared failure catalog
  - at least one stable adjunct candidate in the form of a `handoff bridge`, `subagent split`, or `automation seed`
- Artifact anchor: `incident_map`, `stabilization_plan`, `recovery_decision`, `recovery_verification_pack`, `handoff_record`
- Non-promotion default: if the run only shows one-off recovery handling or weak signal, keep `AOA-P-0020` at `A+Act+F`

## Default posture

Weak, single-use, or ambiguous signals do not justify composition growth.
If a candidate adjunct is not clearly stable and scenario-owned, leave it out of composition and keep the evidence inside the harvest review surface.
