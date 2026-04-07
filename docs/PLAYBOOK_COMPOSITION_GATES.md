# Playbook Composition Gates

This document is the canonical gate surface for promoting selected operational playbooks from `A+Act+F` toward composition.

## Core rule

No new adjunct reaches `config/playbook_composition_overrides.json` until a real run proves both recurrence and distinct playbook-owned value.
Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.
A selection pass that finds no qualifying case keeps the verdict surface at `hold` and creates no reviewed summary.
When a bounded review does land composition, the verdict surface should move to `composition-landed` so the repo does not pretend the playbook is still waiting on promotion.

The minimum evidence threshold for every gate in this document is one real run.
The living per-playbook verdict surfaces sit under `docs/gate-reviews/` and record the current `hold`, `ready-for-composition-review`, or `composition-landed` posture.

## AOA-P-0017 split-wave-cross-repo-rollout

- Required real-run artifact set: `wave_plan`, `bridge_surface_pack`, `downstream_revalidation_pack`, `handoff_record`
- Minimum evidence threshold: one real ordered-wave run
- Required dual signal for promotion:
  - at least one stable failure or follow-up mapping not already covered by `AOA-P-0010` or the shared failure catalog
  - at least one stable adjunct candidate in the form of a `handoff bridge`, `subagent split`, or `automation seed`
- Artifact anchor: `wave_plan`, `bridge_surface_pack`, `downstream_revalidation_pack`, `handoff_record`
- First landing rule: if promotion lands, start with the smallest honest adjunct. For `AOA-P-0017`, that first landing is a minimal playbook-owned `handoff bridge` through `generated/playbook_handoff_contracts.json`, not a new failure code, subagent recipe, or automation seed.
- Non-promotion default: if the run only shows one-off rollout noise or weak signal, keep `AOA-P-0017` at `A+Act+F`

## AOA-P-0018 validation-driven-remediation

- Required real-run artifact set: `failure_map`, `boundary_map`, `remediation_change_set`, `revalidation_pack`, `remediation_decision`, `handoff_record`
- Minimum evidence threshold: one real remediation run
- Required dual signal for promotion:
  - at least one stable failure or follow-up mapping not already covered by neighboring rollout, cutover, or incident playbooks or the shared failure catalog
  - at least one stable adjunct candidate in the form of a `handoff bridge`, `subagent split`, or `automation seed`
- Artifact anchor: `failure_map`, `boundary_map`, `remediation_change_set`, `revalidation_pack`, `remediation_decision`, `handoff_record`
- Non-promotion default: if the run only confirms existing remediation wording or weak signal, keep `AOA-P-0018` at `A+Act+F`

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

## AOA-P-0021 owner-first-capability-landing

- Required real-run artifact set: `candidate_lineage_pack`, `owner_landing_bundle`, `landing_decision`, `rollout_pack`, `validation_pack`, `hardening_record`, `handoff_record`
- Minimum evidence threshold: one real owner-first capability landing route
- Required dual signal for promotion:
  - at least one stable follow-up mapping showing that a reviewed staged lineage pack must land through owner-first closure and post-merge reality sync before broader rollout can stay honest
  - at least one stable adjunct candidate in the form of a `handoff bridge`, `subagent split`, or `automation seed`
- Artifact anchor: `candidate_lineage_pack`, `owner_landing_bundle`, `landing_decision`, `rollout_pack`, `validation_pack`, `hardening_record`, `handoff_record`
- First landing rule: if review-track landing becomes honest, start with the smallest truthful playbook-owned bridge. For `AOA-P-0021`, that first landing is the bounded bridge between staged lineage intake and merged owner truth plus post-merge reality sync, not a new automation seed or subagent recipe.
- Non-promotion default: if the route never leaves staged lineage, never lands in owner surfaces, or never closes with reality sync, keep `AOA-P-0021` at `A+Act+F`

## AOA-P-0024 federated-live-publisher-activation

- Required real-run artifact set: `readiness_audit_pack`, `owner_activation_plan`, `owner_change_set`, `publication_verification_pack`, `stats_visibility_pack`, `residual_handoff_record`
- Minimum evidence threshold: one real owner-local publisher activation route
- Required dual signal for promotion:
  - at least one stable follow-up mapping showing that a reviewed readiness audit and explicit owner-local publication gap must close through owner-ordered publisher activation before the federation can honestly claim live closure
  - at least one stable adjunct candidate in the form of a `handoff bridge`, `subagent split`, or `automation seed`
- Artifact anchor: `readiness_audit_pack`, `owner_activation_plan`, `owner_change_set`, `publication_verification_pack`, `stats_visibility_pack`, `residual_handoff_record`
- First landing rule: if review-track landing becomes honest, start with the smallest truthful adjunct tied to readiness closure, such as a bounded bridge between warning-first readiness audit and later strict non-empty closure, not a new runtime ledger or broad automation claim.
- Non-promotion default: if the route only proves one owner-local activation wave or never surfaces a stable adjunct candidate, keep `AOA-P-0024` at `A+Act+F`

## Default posture

Weak, single-use, or ambiguous signals do not justify composition growth.
If a candidate adjunct is not clearly stable and scenario-owned, leave it out of composition and keep the evidence inside the harvest review surface.
After a landing, keep later growth bounded. Another adjunct family still needs fresh evidence and a new explicit review rather than piggybacking on the first promotion.
