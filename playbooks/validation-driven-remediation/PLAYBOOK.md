---
id: AOA-P-0018
name: validation-driven-remediation
status: experimental
summary: Coordinates remediation after a failed validator or proof surface through explicit source-of-truth mapping, bounded corrective change, and revalidation closure across source-owned boundaries.
scenario: validation_driven_remediation
trigger: validation_or_eval_failure_crossing_source_of_truth_boundaries
prerequisites:
  - failing_validation_surface_named
  - owning_source_surfaces_mapped
  - remediation_boundary_defined
  - revalidation_stop_condition_defined
  - rollback_or_deferral_path_named
participating_agents:
  - architect
  - coder
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - source-of-truth
  - change-protocol
  - verification
  - evaluation
  - memory-curation
required_skills:
  - aoa-source-of-truth-check
  - aoa-bounded-context-map
  - aoa-approval-gate-check
  - aoa-dry-run-first
  - aoa-change-protocol
  - aoa-contract-test
  - aoa-adr-write
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - failure_map
  - boundary_map
  - remediation_change_set
  - revalidation_pack
  - remediation_decision
  - handoff_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - failure_map
  - remediation_decision
  - revalidation_pack
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
eval_anchors:
  - aoa-approval-boundary-adherence
  - aoa-scope-drift-detection
  - aoa-verification-honesty
memo_contract_refs:
  - examples/checkpoint_to_memory_contract.example.json
  - examples/provenance_thread.example.json
memo_writeback_targets:
  - decision
  - audit_event
  - provenance_thread
---

# validation-driven-remediation

## Intent

Use this playbook when a failed validator or proof surface becomes the anchor for a remediation route that crosses source-of-truth boundaries between repositories or owned surfaces.

The route keeps six things explicit:
- which failing validator, check, or proof surface triggered remediation
- which source-owned boundaries the failure actually points at
- what the smallest bounded remediation surface is
- what exact revalidation must rerun before the route can close honestly
- whether closure ends in proceed, handoff, or review stop
- what durable decision and audit trail survive the remediation pass

This playbook is narrower than `cross-repo-boundary-rollout`.
Use `AOA-P-0010` for a generic cross-repo rollout request.
Use `AOA-P-0019` for a planned authority-switch cutover window.
Use `AOA-P-0020` when live incident stabilization and recovery handoff are still the active route.
Use this playbook only when a failed validation surface is the route anchor and the remediation must cross owned boundaries to restore closure honestly.

## Trigger boundary

Use this playbook when:
- a validator, contract check, or proof surface failed in a way that points across source-of-truth boundaries
- remediation requires explicit ownership mapping before mutation
- the route needs bounded corrective change plus honest revalidation before it can close
- the remediation is larger than a single bounded skill but still smaller than release cutover or incident response

Do not use this playbook when:
- the failure can be fixed entirely inside one ordinary bounded repository change
- the route is a generic change request that merely happens to include validation
- the work is really `AOA-P-0019 release-migration-cutover`, `AOA-P-0020 incident-recovery-routing`, or long-horizon inquiry
- the failing signal is too vague to define a bounded remediation surface

## Prerequisites

- the failing validation surface is named before any remediation begins
- the owning source surfaces are mapped
- the remediation boundary is explicit enough to keep the route bounded
- the revalidation stop condition is named before mutation
- a rollback or deferral path exists if revalidation does not restore closure

## Participating agents

- `architect` maps the failing signal to its owning boundaries and defines the bounded remediation surface before mutation begins
- `coder` applies only the smallest corrective change once the failure map, boundary map, and stop conditions are explicit
- `reviewer` checks that remediation stays anchored to the failed validation surface rather than widening into unrelated cleanup
- `evaluator` checks that the revalidation pack actually closes or reclassifies the failure instead of merely producing more motion
- `memory-keeper` preserves the remediation decision, audit trail, and provenance-safe handoff without introducing a new memo taxonomy

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-adr-write`

## Decision points

1. Decide whether the failing validation surface reflects real source-of-truth drift rather than local noise or mis-scoped expectations.
2. Decide which repositories or owned surfaces are authoritative for the failure.
3. Decide what the bounded remediation surface is and what must stay out of scope.
4. Decide whether a preview or inspect-first seam is required before the corrective change.
5. Decide what exact revalidation must rerun before the route can close honestly.
6. Decide whether revalidation supports proceed, handoff, rollback, or review stop.
7. Decide whether loss of failure or boundary clarity requires return to the last valid `failure_map`, `remediation_decision`, or `revalidation_pack` anchor before another pass.

## Handoffs

- `architect -> coder` after the failure map, owning boundaries, remediation boundary, and stop conditions are explicit
- `coder -> reviewer` after the remediation change set and revalidation notes exist
- `reviewer -> evaluator` after the revalidation pack is explicit enough to support closure or stop
- `reviewer or evaluator -> architect` when the route must return to the last valid failure or remediation anchor before another pass
- `evaluator -> memory-keeper` after the remediation decision and residual risks are explicit
- `memory-keeper -> architect` only when the handoff record reveals a later bounded follow-on rather than a clean close

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the failing validation surface is not trustworthy enough to anchor remediation
- source-of-truth boundaries remain ambiguous
- the corrective change starts widening beyond the named remediation surface
- revalidation is incomplete, inconsistent, or no longer aimed at the original failure
- rollback or deferral posture cannot be stated reviewably

If failure integrity, ownership clarity, or revalidation closure is lost, return to the last valid `failure_map`, `remediation_decision`, or `revalidation_pack` anchor before further mutation.
If those anchors are no longer trustworthy, stop for review rather than keep remediating by inertia.

## Expected evidence posture

The route should finish with visible evidence for:
- what exact failing validation surface triggered the route
- why the failure pointed at the chosen source-owned boundaries
- what bounded corrective change was made and why it stayed in scope
- what revalidation reran before closure
- what anchor governed return, rollback gate, review gate, or safe stop
- what decision or handoff record remains if the route closes without full restoration

## Expected artifacts

- `failure_map`
- `boundary_map`
- `remediation_change_set`
- `revalidation_pack`
- `remediation_decision`
- `handoff_record`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-scope-drift-detection`
- `aoa-verification-honesty`

Use `aoa-approval-boundary-adherence` to check that remediation respected authority and ownership boundaries.
Use `aoa-scope-drift-detection` to check that a failure-driven route did not silently widen beyond the named remediation surface.
Use `aoa-verification-honesty` to check that revalidation claims match what actually reran.

## Memory writeback

- `remediation_decision` should survive as a `decision`
- `revalidation_pack` should survive as an `audit_event` when it records the actual rerun and closure posture
- `handoff_record` should survive as a `provenance_thread`
- `failure_map`, `boundary_map`, and `remediation_change_set` remain route artifacts or referenced artifacts rather than memo writeback kinds

The playbook does not create a new memory-object kind and does not move memo taxonomy into the playbook layer.

## Canonical route

1. Name the failing validation surface that triggered remediation.
2. Map the owning boundaries with `aoa-source-of-truth-check` and `aoa-bounded-context-map`.
3. Define the remediation boundary, stop conditions, and rollback or deferral posture before mutation begins.
4. Use `aoa-approval-gate-check` and `aoa-dry-run-first` when authority or inspect-first posture must be made explicit.
5. Apply the smallest corrective change through `aoa-change-protocol`.
6. Rerun the failing validation surface and tighten closure with `aoa-contract-test` when the route needs an explicit contract-facing revalidation seam.
7. If failure or boundary clarity is lost, return to the last valid `failure_map`, `remediation_decision`, or `revalidation_pack` anchor and re-enter through `previous_phase`, `review_gate`, `rollback_gate`, or `safe_stop`.
8. Close with the `remediation_decision`, `revalidation_pack`, and provenance-safe `handoff_record`, and use `aoa-adr-write` when the remediation introduces a durable decision.
