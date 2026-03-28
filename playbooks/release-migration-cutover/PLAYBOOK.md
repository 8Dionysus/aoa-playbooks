---
id: AOA-P-0019
name: release-migration-cutover
status: experimental
summary: Coordinates a bounded release or migration cutover window through explicit freeze posture, go-no-go gating, authority switch, post-cutover verification, and rollback-or-handoff closure across neighboring AoA layers.
scenario: release_migration_cutover
trigger: release_or_migration_window_requiring_authority_switch
prerequisites:
  - cutover_window_named
  - authority_switch_boundary_defined
  - pre_cutover_freeze_posture_named
  - go_no_go_gate_defined
  - post_cutover_verification_surface_named
  - rollback_or_reversal_path_named
  - downstream_consumer_handoff_boundary_named
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
  - review
  - memory-curation
required_skills:
  - aoa-source-of-truth-check
  - aoa-bounded-context-map
  - aoa-approval-gate-check
  - aoa-dry-run-first
  - aoa-change-protocol
  - aoa-contract-test
  - aoa-adr-write
  - aoa-sanitized-share
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - authority_map
  - cutover_plan
  - cutover_decision
  - cutover_change_set
  - post_cutover_verification_pack
  - handoff_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - cutover_plan
  - cutover_decision
  - post_cutover_verification_pack
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

# release-migration-cutover

## Intent

Use this playbook when a named release or migration window must switch authoritative surfaces, supported references, or downstream consumer posture across neighboring AoA layers or repositories.

The route keeps six things explicit:
- which current and target authority surfaces are actually changing during the window
- what pre-cutover freeze posture keeps the switch reviewable
- what exact go-no-go gate must clear before the authority switch happens
- what post-cutover verification must run before the route can close honestly
- when the route confirms the switch, reverses it, or stops for review
- what provenance-safe handoff survives the cutover window

This playbook is narrower than `release-prep`.
Use `AOA-P-0004` for checklist-style merge or release preparation.
Use `AOA-P-0010` for a generic cross-repo rollout with no authority switch.
Use `AOA-P-0017` for ordered bridge publication rather than a cutover window.
Use `AOA-P-0020` for live incident stabilization rather than a planned release or migration window.
Use this playbook only when the cutover window and authority switch are the scenario contract itself.

## Trigger boundary

Use this playbook when:
- a named cutover window must switch authority, supported references, or downstream consumer posture across neighboring AoA layers or repos
- pre-cutover freeze posture, go-no-go gating, and post-cutover verification matter as much as the direct mutations
- the route needs an explicit switch boundary instead of a generic multi-repo rollout
- rollback or reversal posture must stay reviewable before the authority switch begins

Do not use this playbook when:
- the task is ordinary release prep with no real authority switch
- the route is `AOA-P-0010 cross-repo-boundary-rollout` or `AOA-P-0017 split-wave-cross-repo-rollout`
- the work is really a long migration program with staged compatibility windows
- the task is `AOA-P-0020 incident-recovery-routing` rather than a planned cutover window
- no bounded post-cutover verification surface can be named

## Prerequisites

- the cutover window is named before the route begins
- the authority switch boundary between current and target surfaces is explicit
- pre-cutover freeze posture is defined before mutation begins
- the go-no-go gate is explicit before the authority switch
- the post-cutover verification surface is named before the cutover change set lands
- a rollback or reversal path exists if the cutover cannot close honestly
- the downstream consumer handoff boundary is explicit before the route closes

## Participating agents

- `architect` maps the current versus target authority surfaces, freeze posture, and go-no-go gate before mutation begins
- `coder` applies the bounded cutover change set only after the authority map, switch boundary, and reversal path are explicit
- `reviewer` checks that freeze posture, switch scope, and downstream handoff stay reviewable rather than widening into a migration program
- `evaluator` checks that post-cutover verification supports continue, rollback, handoff, or review stop without overstating closure
- `memory-keeper` preserves the cutover decision, audit trail, and provenance-safe handoff without inventing a new memo taxonomy

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-adr-write`
- `aoa-sanitized-share`

## Decision points

1. Decide whether a true cutover window is required instead of ordinary release prep or a generic rollout.
2. Decide what exact authority switches during the window and what must remain unchanged.
3. Decide whether the pre-cutover freeze posture is strong enough to make the switch reviewable.
4. Decide what evidence clears the go-no-go gate before the cutover change set lands.
5. Decide what exact post-cutover verification is mandatory before the authority switch can be confirmed.
6. Decide whether post-cutover results support continue, rollback, handoff, or review stop.
7. Decide whether loss of authority clarity, freeze integrity, or verification closure requires return to the last valid `cutover_plan`, `cutover_decision`, or `post_cutover_verification_pack` anchor before another pass.

## Handoffs

- `architect -> coder` after the authority map, cutover plan, freeze posture, and go-no-go gate are explicit
- `coder -> reviewer` after the bounded cutover change set and post-cutover verification notes exist
- `reviewer -> evaluator` after the cutover decision and verification pack are explicit enough to support continue, rollback, handoff, or stop
- `reviewer or evaluator -> architect` when authority boundaries, freeze posture, or verification closure drift enough that the route must return to the last valid cutover anchor
- `evaluator -> memory-keeper` after the route can name confirm, reverse, handoff, or stop with a bounded rationale
- `memory-keeper -> architect` only when the handoff record proves that follow-on migration work still needs a separate governed route

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the current and target authority surfaces are not clearly source-owned
- freeze posture is too weak to keep the cutover boundary reviewable
- the go-no-go gate is vague enough that the authority switch would rely on guesswork
- post-cutover verification is incomplete, inconsistent, or aimed at the wrong surface
- the route starts widening into long migration choreography, incident recovery, or hidden runtime operations

If authority clarity, freeze integrity, or post-cutover verification closure is lost, return to the last valid `cutover_plan`, `cutover_decision`, or `post_cutover_verification_pack` anchor before further mutation.
If the authority switch cannot be confirmed honestly, reverse the cutover through the named rollback or reversal path and re-enter through `previous_phase`, `review_gate`, `rollback_gate`, or `safe_stop`.
If reversal posture is no longer reviewable, stop and re-scope before continuing.

## Expected evidence posture

The route should finish with visible evidence for:
- what current and target authority surfaces the cutover window actually switched
- what freeze posture kept the window bounded and why it was sufficient
- what go-no-go evidence justified the authority switch
- what bounded cutover change set landed during the window
- what post-cutover verification ran before the route closed
- what anchor governed a return, rollback gate, review gate, or safe stop
- what downstream consumers were handed off, updated, or told to defer

## Expected artifacts

- `authority_map`
- `cutover_plan`
- `cutover_decision`
- `cutover_change_set`
- `post_cutover_verification_pack`
- `handoff_record`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-scope-drift-detection`
- `aoa-verification-honesty`

Use `aoa-approval-boundary-adherence` to check that the cutover respected authority and approval boundaries.
Use `aoa-scope-drift-detection` to check that the cutover route did not silently widen into broader migration work.
Use `aoa-verification-honesty` to check that go-no-go and post-cutover verification claims match what actually ran.

## Memory writeback

- `cutover_decision` should survive as a `decision`
- `post_cutover_verification_pack` should survive as an `audit_event` when it records the actual go-no-go and post-cutover verification closure
- `handoff_record` should survive as a `provenance_thread`
- `authority_map`, `cutover_plan`, and `cutover_change_set` remain route artifacts or referenced artifacts rather than memo writeback kinds

The playbook does not create a new memory-object kind and does not move memo taxonomy into the playbook layer.

## Canonical route

1. Map the current and target authority surfaces with `aoa-source-of-truth-check` and `aoa-bounded-context-map`.
2. Define the freeze window, authority switch boundary, downstream handoff boundary, and bounded `cutover_plan` before mutation begins.
3. Use `aoa-approval-gate-check` and `aoa-dry-run-first` to make the go-no-go gate, inspect-first posture, and reversal path explicit.
4. Apply the bounded `cutover_change_set` through `aoa-change-protocol` once the cutover window opens.
5. Tighten cutover confidence with `aoa-contract-test` and record any durable authority or interface decision through `aoa-adr-write`.
6. Run the named `post_cutover_verification_pack` against the target authority surface and decide whether the switch is confirmed or reversed.
7. If authority clarity or verification closure is lost, return to the last valid `cutover_plan`, `cutover_decision`, or `post_cutover_verification_pack` anchor and re-enter through `previous_phase`, `review_gate`, `rollback_gate`, or `safe_stop`.
8. Close with the final `cutover_decision` and provenance-safe `handoff_record`, and use `aoa-sanitized-share` when the downstream handoff must travel outside the immediate cutover owners.
