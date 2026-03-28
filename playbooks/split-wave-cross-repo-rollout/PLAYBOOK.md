---
id: AOA-P-0017
name: split-wave-cross-repo-rollout
status: experimental
summary: Coordinates an ordered cross-repo rollout through upstream bridge publication, downstream revalidation against updated upstream main, and bounded defer-or-merge closure.
scenario: split_wave_cross_repo_rollout
trigger: cross_repo_change_requiring_ordered_merge_and_downstream_revalidation
prerequisites:
  - owning_repos_identified
  - upstream_bridge_surface_defined
  - downstream_revalidation_surface_named
  - downstream_dependency_window_named
  - rerun_policy_defined
  - rollback_or_deferral_plan_defined
participating_agents:
  - architect
  - coder
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - source-of-truth
  - change-protocol
  - review
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
  - boundary_map
  - wave_plan
  - bridge_surface_pack
  - wave_decision
  - downstream_revalidation_pack
  - handoff_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - wave_plan
  - wave_decision
  - downstream_revalidation_pack
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
eval_anchors:
  - aoa-approval-boundary-adherence
  - aoa-scope-drift-detection
  - aoa-verification-honesty
memo_recall_modes:
  - episodic
  - semantic
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_capsule_then_expand
memo_checkpoint_posture: not_needed
memo_source_route_policy: required
memo_contract_refs:
  - examples/recall_contract.router.semantic.json
  - examples/checkpoint_to_memory_contract.example.json
  - examples/provenance_thread.example.json
memo_writeback_targets:
  - decision
  - audit_event
  - provenance_thread
---

# split-wave-cross-repo-rollout

## Intent

Use this playbook when a cross-repo route cannot stay honest as one bounded wave because upstream bridge surfaces must land before downstream repositories can rebase, rerun, or merge cleanly against updated upstream `main`.

The route keeps six things explicit:
- which repositories own the upstream source surfaces and downstream dependents
- which bridge surfaces must publish in wave 1 before downstream motion resumes
- what exact rerun or revalidation policy governs later waves
- what counts as merge-ready versus defer-ready for the downstream wave
- which artifact anchors govern return, review, or rollback when wave integrity is lost
- what provenance-safe handoff survives the ordered rollout

This playbook is narrower than `cross-repo-boundary-rollout`.
Use `AOA-P-0010` for a generic cross-repo route that can stay reviewable in one coherent wave.
Use `AOA-P-0019` for a planned cutover window with freeze, go-no-go, and authority-switch posture.
Use `AOA-P-0020` for live incident stabilization and recovery handoff.
Use this playbook only when ordered waves, updated upstream `main`, and downstream revalidation are part of the scenario contract itself.

## Trigger boundary

Use this playbook when:
- upstream bridge surfaces must land before a downstream repository can validate or merge honestly
- downstream repositories must rebase, rerun bounded checks, or re-evaluate merge posture against updated upstream `main`
- wave boundaries, rerun policy, and defer-or-rollback posture matter as much as the direct code changes
- the route needs a scenario-level method rather than a set of loosely related per-repo tasks

Do not use this playbook when:
- the cross-repo route can remain honest as one bounded wave
- downstream work can validate against a pinned snapshot without an upstream-first merge
- the task is really `AOA-P-0019 release-migration-cutover`, `AOA-P-0020 incident-recovery-routing`, or a single-repo bounded change
- no explicit bridge surface or rerun boundary can be named

## Prerequisites

- the owning repositories are identified before rollout sequencing begins
- the upstream bridge surfaces that unblock downstream work are named explicitly
- the downstream revalidation surface is known before wave 1 mutates anything
- the dependency window for downstream work against updated upstream `main` is bounded
- rerun policy is explicit before the ordered rollout begins
- a rollback or deferral plan exists if wave 2 cannot close honestly

## Participating agents

- `architect` maps repository ownership, bridge surfaces, wave boundaries, and stop conditions before mutation begins
- `coder` executes each bounded wave only after the current source surfaces, downstream dependency window, and rerun obligations are explicit
- `reviewer` checks that bridge publication, downstream revalidation, and merge-or-defer decisions stay reviewable rather than drifting into hidden orchestration
- `evaluator` checks that the downstream revalidation pack supports continue, defer, rollback, or stop without widening scope
- `memory-keeper` preserves the route decision, audit trail, and provenance-safe handoff without inventing a new memo taxonomy

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-adr-write`

## Decision points

1. Decide whether the route truly requires split-wave choreography instead of a single bounded cross-repo wave.
2. Decide which upstream bridge surfaces must be complete before downstream repositories are allowed to resume.
3. Decide what exact condition makes wave 1 bridge-complete and publishable.
4. Decide when downstream rebase and rerun steps are mandatory against updated upstream `main`.
5. Decide whether downstream revalidation supports merge, defer, rollback, or safe stop.
6. Decide whether loss of wave integrity requires return to the last valid `wave_plan` or `wave_decision` anchor before more motion.
7. Decide whether the route closes with a handoff record for a later wave or stops for explicit review.

## Handoffs

- `architect -> coder` after the boundary map, wave plan, bridge surfaces, and rerun policy are explicit
- `coder -> reviewer` after the current wave leaves a reviewable bridge surface pack or downstream change slice
- `reviewer -> evaluator` after the downstream revalidation pack and current wave decision are explicit
- `reviewer or evaluator -> architect` when wave boundaries, rerun policy, or rollback posture drift enough that the route must return to the last valid `wave_plan` or `wave_decision`
- `evaluator -> memory-keeper` after the route can name merge, defer, rollback, or stop with a bounded rationale
- `memory-keeper -> architect` only when the handoff record proves that another governed wave is required

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the upstream bridge surfaces are not clearly source-owned
- downstream validation is not actually running against updated upstream `main`
- rerun policy is vague enough that later waves would guess what needs to be revalidated
- wave 1 merge results invalidate downstream assumptions in a way that broadens the task
- the route starts drifting into release-prep, incident recovery, or hidden runtime choreography

If wave integrity is lost, return to the last valid `wave_plan` or `wave_decision` anchor before any further mutation.
If downstream revalidation fails because upstream bridge publication changed the route shape, re-enter through `previous_phase`, `review_gate`, `rollback_gate`, or `safe_stop` rather than forcing the next wave by inertia.
If rollback or deferral cannot be stated reviewably, stop and re-scope before continuing.

## Expected evidence posture

The route should finish with visible evidence for:
- why split-wave choreography was required instead of a single cross-repo wave
- what exact bridge surfaces landed in the upstream wave and why they were sufficient
- what downstream dependency window and updated upstream `main` reference governed revalidation
- what reruns, contract checks, or review gates actually executed in the downstream wave
- what anchor governed a return, review gate, rollback gate, or safe stop and why the route could or could not resume
- what was merged now, deferred to a later wave, or frozen behind the final handoff record

## Expected artifacts

- `boundary_map`
- `wave_plan`
- `bridge_surface_pack`
- `wave_decision`
- `downstream_revalidation_pack`
- `handoff_record`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-scope-drift-detection`
- `aoa-verification-honesty`

Use `aoa-approval-boundary-adherence` to check that ordered waves respected repository ownership and approval boundaries.
Use `aoa-scope-drift-detection` to check that split-wave coordination did not silently widen the route.
Use `aoa-verification-honesty` to check that downstream reruns and revalidation claims match what actually happened.

## Memory writeback

- `wave_decision` should survive as a `decision`
- `downstream_revalidation_pack` should survive as an `audit_event` when it records the actual rerun and validation closure
- `handoff_record` should survive as a `provenance_thread`
- `boundary_map`, `wave_plan`, and `bridge_surface_pack` remain route artifacts or referenced artifacts rather than memo writeback kinds

The playbook does not create a new memory-object kind and does not move memo taxonomy into the playbook layer.

## Canonical route

1. Map the owning repositories and identify which upstream bridge surfaces must land before downstream work can resume honestly.
2. Use `aoa-source-of-truth-check` and `aoa-bounded-context-map` to separate source-authored surfaces from downstream dependents and define the bounded `wave_plan`.
3. Use `aoa-approval-gate-check` and `aoa-dry-run-first` to confirm bridge-first sequencing, rerun policy, and stop conditions before mutation begins.
4. Execute the upstream wave through `aoa-change-protocol`, tighten bridge confidence with `aoa-contract-test`, and capture any durable interface or rollout rationale through `aoa-adr-write`.
5. Publish or merge the upstream bridge surfaces and record the exact updated upstream `main` reference that downstream revalidation must use.
6. Rebase or reorient the downstream repository against updated upstream `main` and rerun the bounded contract or validation checks required by the `wave_plan`.
7. If downstream revalidation fails or the wave boundary drifts, return to the last valid `wave_plan` or `wave_decision` anchor and re-enter through `previous_phase`, `review_gate`, `rollback_gate`, or `safe_stop`.
8. Merge or defer the downstream wave, then close with the `downstream_revalidation_pack`, final `wave_decision`, and a provenance-safe `handoff_record` for later review or a later wave.
