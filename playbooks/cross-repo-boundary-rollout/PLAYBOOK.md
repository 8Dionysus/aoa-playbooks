---
id: AOA-P-0010
name: cross-repo-boundary-rollout
status: experimental
summary: Coordinates a bounded cross-repo change through explicit ownership mapping, rollout sequencing, validation closure, and provenance-safe handoff.
scenario: cross_repo_boundary_rollout
trigger: multi_repo_source_of_truth_change
prerequisites:
  - owning_repos_identified
  - source_surfaces_mapped
  - generated_surface_impact_mapped
  - review_boundary_defined
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
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - boundary_map
  - repo_change_set
  - rollout_decision
  - validation_pack
  - handoff_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - boundary_map
  - rollout_decision
  - validation_pack
return_reentry_modes:
  - previous_phase
  - review_gate
  - safe_stop
eval_anchors:
  - aoa-approval-boundary-adherence
  - aoa-scope-drift-detection
memo_contract_refs:
  - examples/checkpoint_to_memory_contract.example.json
  - examples/provenance_thread.example.json
memo_writeback_targets:
  - decision
  - audit_event
  - provenance_thread
---

# cross-repo-boundary-rollout

## Intent

Use this playbook when one bounded scenario needs coordinated changes across more than one AoA source-owned repository.

The route keeps five things explicit:
- which repository owns which meaning
- which surfaces are source-authored versus derived
- what rollout order keeps downstream consumers honest
- what validation must close before the next repo handoff
- what provenance-safe handoff record survives the route

This playbook exists to keep cross-repo motion reviewable without turning `aoa-playbooks` into routing logic, skill canon, eval doctrine, or memo taxonomy.

## Trigger boundary

Use this playbook when:
- the route changes source-owned surfaces in more than one AoA repository
- a generated or derived surface in one repo depends on a source-owned change in another repo
- rollout order, ownership boundaries, and validation closure must stay explicit
- the route needs a scenario-level method rather than isolated per-repo changes

Do not use this playbook when:
- one repository fully owns the change and the rest only consume already-generated outputs later
- the real need is a single bounded skill or a normal single-repo safe rollout
- the task is mainly routing implementation, proof doctrine, or memory taxonomy work
- no reviewable rollout order can be named

## Prerequisites

- the affected repositories and their owning surfaces are named
- source-authored surfaces are separated from generated or downstream surfaces
- generated-surface impact is mapped before mutation begins
- the review boundary and sequencing plan are explicit
- a rollback or defer path exists if one repository fails validation

## Participating agents

- `architect` maps repository ownership, source-of-truth boundaries, and rollout order before mutation begins
- `coder` applies bounded per-repo changes only after the current ownership boundary is explicit
- `reviewer` checks that source-owned meaning stayed in the correct repository and that downstream sync is reviewable
- `evaluator` checks that the validation pack supports proceed, defer, or stop without silent scope expansion
- `memory-keeper` preserves the surviving provenance and handoff record without introducing a new memo taxonomy

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`

## Decision points

1. Decide whether the scenario truly crosses more than one source-of-truth repository.
2. Decide which repository mutates source-owned meaning first and which repositories only regenerate or consume.
3. Decide whether the rollout can remain one bounded wave or must split into staged handoffs.
4. Decide whether ownership drift, source-versus-derived confusion, or failed per-repo validation requires return to the last valid boundary anchor before the next repository step.
5. Decide whether current per-repo validation is strong enough to continue to the next repository.
6. Decide whether the route can close with a handoff record or must stop for further review.

## Handoffs

- `architect -> coder` after the boundary map, repo sequence, and stop conditions are explicit
- `coder -> reviewer` after the current repo slice and downstream impact notes exist
- `reviewer -> evaluator` after boundary handling and per-repo validation evidence are explicit
- `reviewer or evaluator -> architect` when the route must return to the last valid boundary map or rollout decision before another repo handoff
- `evaluator -> memory-keeper` after the validation pack and residual cross-repo risks are explicit
- `memory-keeper -> architect` only when the handoff record reveals unresolved ownership drift or a required follow-on wave

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- repository ownership is unclear
- a source-owned change is drifting into a neighboring repo for convenience
- generated-surface impact cannot be traced before a downstream update
- one repository fails validation in a way that invalidates the next repo step
- the route starts absorbing routing, skill, eval, or memo meaning that belongs elsewhere

If repository ownership becomes unclear, if source-authored and generated surfaces stop being separable, or if a validation failure invalidates the next repo step, return to the last valid `boundary_map` or `rollout_decision` anchor before any further rollout motion.
If boundary integrity cannot be restored, stop for review rather than continue the wave.

If the route cannot preserve source-versus-derived separation, stop and re-scope before continuing.

## Expected evidence posture

The route should finish with visible evidence for:
- why each changed surface landed in its chosen repository
- what stayed source-authored versus what remained generated
- what rollout order was used and why
- what validators, bounded checks, or review gates ran in each repository
- what boundary anchor governed return, review gate, or stop, and why the route could or could not resume
- what had to be handed off, deferred, or frozen for a later wave

## Expected artifacts

- `boundary_map`
- `repo_change_set`
- `rollout_decision`
- `validation_pack`
- `handoff_record`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-scope-drift-detection`

Use `aoa-approval-boundary-adherence` to check that the route respected repository ownership and approval boundaries.
Use `aoa-scope-drift-detection` to check that cross-repo coordination did not silently widen the task surface.

## Memory writeback

- `rollout_decision` should survive as a `decision`
- `validation_pack` should survive as an `audit_event` when it records cross-repo validation closure
- `handoff_record` should survive as a `provenance_thread`
- `boundary_map` and `repo_change_set` remain route artifacts or referenced artifacts rather than memo writeback kinds

The playbook does not create a new memory-object kind and does not move memo taxonomy into the playbook layer.

## Canonical route

1. Map the owning repositories and separate source-authored surfaces from generated dependents.
2. Use `aoa-source-of-truth-check` and `aoa-bounded-context-map` to confirm that repository boundaries are explicit.
3. Decide rollout order, stop conditions, and approval posture before mutation begins.
4. Use `aoa-dry-run-first` when downstream impact or generated-surface sync is still ambiguous.
5. Execute each bounded repo slice with `aoa-change-protocol` and keep the repo change set reviewable.
6. Validate the current slice before continuing to the next repository and record the rollout decision.
7. If boundary integrity is lost, return to the last valid boundary anchor and re-enter through `previous_phase`, `review_gate`, or `safe_stop`.
8. Close the route with a validation pack and provenance-safe handoff record for the next wave or final review.
