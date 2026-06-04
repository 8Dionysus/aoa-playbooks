---
id: AOA-P-0046
name: checkpoint-distillation-closed-loop-pilot
status: experimental
summary: Coordinates one reviewed checkpoint distillation into a closed-loop pilot runbook without turning pilot notes into execution canon.
scenario: checkpoint_distillation_closed_loop_pilot
trigger: reviewed_checkpoint_needing_distillation_into_a_closed_loop_pilot_runbook
prerequisites:
  - reviewed_checkpoint_artifact_named
  - pilot_boundary_named
  - closed_loop_review_surface_named
  - source_of_truth_boundary_named
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
  - aoa-checkpoint-closeout-bridge
  - aoa-source-of-truth-check
  - aoa-bounded-context-map
  - aoa-change-protocol
  - aoa-contract-test
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: safe_stop
expected_artifacts:
  - checkpoint_distillation_brief
  - closed_loop_pilot_runbook
  - pilot_guardrail_notes
  - residual_handoff_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - checkpoint_distillation_brief
  - closed_loop_pilot_runbook
  - pilot_guardrail_notes
return_reentry_modes:
  - review_gate
  - safe_stop
eval_anchors:
  - aoa-bounded-change-quality
  - aoa-verification-honesty
memo_recall_modes:
  - episodic
  - semantic
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_then_expand
memo_checkpoint_posture: not_needed
memo_source_route_policy: required
---

# checkpoint-distillation-closed-loop-pilot

## Intent

Use this playbook when a reviewed checkpoint needs to be distilled into a
closed-loop pilot runbook that stays bounded, readable, and owner-local.

The route keeps four things explicit:

- what reviewed checkpoint is being distilled
- what the pilot boundary allows and forbids
- what the runbook must preserve for later review
- what residual handoff remains if the pilot cannot be named honestly yet

## Trigger boundary

Use this playbook when:

- a reviewed checkpoint exists and needs a smaller pilot-shaped next move
- the useful output is a runbook, not a live runner
- the main risk is that pilot language could outrun evidence

Do not use this playbook when:

- the task is only a single doc or note cleanup
- the route needs live execution authority
- the route is really broader session growth, rollout, or proof work

## Prerequisites

- the reviewed checkpoint artifact is named
- the closed-loop pilot boundary is explicit before distillation begins
- the source-of-truth boundary is named before the runbook is written

## Participating agents

- `architect` keeps the checkpoint, pilot boundary, and stop line explicit
- `coder` writes the smallest bounded runbook once the boundary is clear
- `reviewer` checks that the runbook does not outrun the reviewed checkpoint
- `evaluator` checks that the pilot readout stays below runtime authority
- `memory-keeper` preserves only bounded decisions or audit context

## Required skills

- `aoa-checkpoint-closeout-bridge`
- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-change-protocol`
- `aoa-contract-test`

## Decision points

1. Decide whether the reviewed checkpoint is strong enough to distill.
2. Decide whether the pilot boundary is narrow enough for a reviewable runbook.
3. Decide whether the current route needs defer or safe stop instead of
   distillation.
4. Decide what stop line or residual handoff should survive if the pilot is
   still too thin.

## Handoffs

- `architect -> coder` after the checkpoint and pilot boundary are explicit
- `coder -> reviewer` after the pilot runbook draft exists
- `reviewer -> evaluator` after the boundary note is readable enough to judge
- `reviewer or evaluator -> architect` when the route loses boundary clarity
- `evaluator -> memory-keeper` only when a bounded decision or audit trail
  should survive

## Fallback and rollback posture

Fallback mode is `safe_stop`.

Pause or stop when:

- the checkpoint is too thin to distill honestly
- the pilot boundary would imply runtime authority
- the runbook starts replacing owner-local review
- the stop line or residual handoff is missing

If boundary clarity is lost, return to the last valid checkpoint, boundary
note, or runbook draft before continuing. If no honest anchor remains, stop
and defer.

## Expected evidence posture

The route should finish with visible evidence for:

- what checkpoint was distilled
- what closed-loop pilot boundary was named
- what runbook was written
- what stop condition or handoff remains

## Expected artifacts

- `checkpoint_distillation_brief`
- `closed_loop_pilot_runbook`
- `pilot_guardrail_notes`
- `residual_handoff_record`

## Eval anchors

- `aoa-bounded-change-quality`
- `aoa-verification-honesty`

## Memory writeback

- the distilled checkpoint note may survive as a `decision`
- the pilot boundary note may survive as an `audit_event`
- the surviving route thread may survive as a `provenance_thread`
- the runbook itself remains a route artifact unless a later memo pass
  promotes it explicitly

## Canonical route

1. Name the reviewed checkpoint and the pilot boundary.
2. Distill the checkpoint into one bounded pilot runbook.
3. Check that the runbook stays below runtime or governance authority.
4. Preserve the stop line or residual handoff if the pilot is still too thin.
5. Return through `review_gate` or `safe_stop` when the route loses boundary
   clarity.
