---
id: AOA-P-0020
name: incident-recovery-routing
status: experimental
summary: Coordinates a bounded incident route through explicit incident mapping, stabilization or rollback choice, recovery verification, and restored-or-degraded handoff closure across neighboring AoA layers.
scenario: incident_recovery_routing
trigger: incident_requiring_cross_boundary_stabilization_and_handoff
prerequisites:
  - incident_surface_named
  - affected_authority_surfaces_mapped
  - blast_radius_boundary_named
  - stabilization_boundary_defined
  - rollback_or_degraded_mode_path_named
  - recovery_verification_surface_named
  - restored_or_degraded_stop_condition_defined
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
  - safe-infra
  - verification
  - memory-curation
required_skills:
  - aoa-source-of-truth-check
  - aoa-bounded-context-map
  - aoa-approval-gate-check
  - aoa-dry-run-first
  - aoa-change-protocol
  - aoa-safe-infra-change
  - aoa-local-stack-bringup
  - aoa-contract-test
  - aoa-adr-write
  - aoa-sanitized-share
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - incident_map
  - stabilization_plan
  - stabilization_change_set
  - recovery_decision
  - recovery_verification_pack
  - handoff_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - incident_map
  - stabilization_plan
  - recovery_decision
  - recovery_verification_pack
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

# incident-recovery-routing

## Intent

Use this playbook when an unplanned incident crosses authority or consumer boundaries and needs one bounded route from incident mapping to stabilization, recovery verification, and a reviewable restored-or-degraded handoff.

The route keeps six things explicit:
- which incident surface triggered the route and which authority surfaces or consumers are affected
- what the bounded blast radius is before the next stabilization step happens
- whether the next governed move is stabilize, roll back, or degrade with an explicit handoff
- what exact recovery verification must run before the route can close honestly
- which closure class applies: `restored`, `degraded-with-handoff`, `rollback-complete`, or `review-stop`
- what provenance-safe handoff survives if follow-on remediation still remains

This playbook is narrower than remediation, cutover, or generic cross-repo rollout.
Use `AOA-P-0018` for post-failure remediation, `AOA-P-0019` for planned cutover windows, and `AOA-P-0010` for generic multi-repo rollout.
Use this playbook only when live incident stabilization and recovery handoff are the scenario contract itself.

## Trigger boundary

Use this playbook when:
- an unplanned incident crosses source-owned authority surfaces, downstream consumers, or neighboring AoA layers
- the route needs bounded stabilization plus recovery verification before it can close honestly
- rollback or degraded-mode posture matters as much as the direct recovery step
- the route must finish with a restored-or-degraded decision and a bounded handoff rather than open-ended recovery motion

Do not use this playbook when:
- the issue is local-only stack diagnosis better handled by `AOA-P-0014 local-stack-diagnosis`
- the route is a preview-first infra change before any live incident, which belongs in `AOA-P-0012 infra-change-guarded`
- the work is a planned authority switch or release window, which belongs in `AOA-P-0019 release-migration-cutover`
- the work is an ordered rollout or bridge-publication route, which belongs in `AOA-P-0010` or `AOA-P-0017`
- the incident is already stabilized and the remaining task is post-incident remediation, which belongs in `AOA-P-0018 validation-driven-remediation`

## Prerequisites

- the incident surface is named before recovery motion begins
- the affected authority surfaces and downstream consumers are mapped
- the blast radius boundary is explicit enough to keep stabilization bounded
- the stabilization boundary is defined before mutation begins
- a rollback or degraded-mode path exists if the incident cannot be fully restored
- the recovery verification surface is named before the recovery step lands
- the route can name a restored-or-degraded stop condition before closure
- the downstream consumer handoff boundary is explicit before the route ends

## Participating agents

- `architect` maps the incident surface, blast radius boundary, authority surfaces, and bounded stabilization plan before mutation begins
- `coder` applies only the smallest stabilization or reversal step once the incident map, recovery path, and stop conditions are explicit
- `reviewer` checks that the route stays inside bounded incident recovery instead of widening into general remediation or hidden orchestration
- `evaluator` checks that the recovery verification pack supports `restored`, `degraded-with-handoff`, `rollback-complete`, or `review-stop` without overstating closure
- `memory-keeper` preserves the recovery decision, audit trail, and provenance-safe handoff without inventing a new memo taxonomy

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-safe-infra-change`
- `aoa-local-stack-bringup`
- `aoa-contract-test`
- `aoa-adr-write`
- `aoa-sanitized-share`

## Decision points

1. Decide whether the signal is a real incident route rather than a validator failure, routine infra change, or planned cutover.
2. Decide what the bounded blast radius is and which authority surfaces or consumers are actually affected.
3. Decide whether the next governed move is stabilize in place, roll back, or degrade with explicit handoff.
4. Decide whether preview or inspect-first posture is still required before the stabilization step.
5. Decide what exact recovery verification is mandatory before the route can close honestly.
6. Decide whether the route closes as `restored`, `degraded-with-handoff`, `rollback-complete`, or `review-stop`.
7. Decide whether loss of incident clarity, blast-radius integrity, or recovery-verification closure requires return to the last valid `incident_map`, `stabilization_plan`, `recovery_decision`, or `recovery_verification_pack` anchor before another pass.

## Handoffs

- `architect -> coder` after the incident map, blast radius boundary, stabilization plan, and rollback-or-degraded path are explicit
- `coder -> reviewer` after the bounded stabilization change set and recovery verification notes exist
- `reviewer -> evaluator` after the recovery decision and verification pack are explicit enough to support `restored`, `degraded-with-handoff`, `rollback-complete`, or `review-stop`
- `reviewer or evaluator -> architect` when incident boundaries, degraded-mode posture, or recovery verification drift enough that the route must return to the last valid recovery anchor
- `evaluator -> memory-keeper` after the route can name a bounded closure class and the remaining consumer risk honestly
- `memory-keeper -> architect` only when the handoff record proves that follow-on remediation belongs in `AOA-P-0018`, `AOA-P-0010`, or a later governed route

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the incident surface is too vague or contradictory to anchor stabilization honestly
- the blast radius boundary remains unclear across authority or consumer surfaces
- the stabilization step starts widening into general cleanup or broad remediation
- the rollback or degraded-mode path is weaker than the proposed stabilization motion
- the recovery verification pack does not match the claimed closure state
- the route starts drifting into a persisted recovery engine, post-incident remediation, or hidden runtime orchestration

If incident clarity, blast-radius integrity, or recovery-verification closure is lost, return to the last valid `incident_map`, `stabilization_plan`, `recovery_decision`, or `recovery_verification_pack` anchor before further mutation.
If the route cannot honestly prove `restored`, `degraded-with-handoff`, or `rollback-complete`, stop as `review-stop` rather than continue recovery by inertia.
If deeper corrective work remains after stabilization, hand it off explicitly instead of widening this playbook past incident closure.

## Expected evidence posture

The route should finish with visible evidence for:
- what exact incident surface triggered the route
- which authority surfaces, consumers, or neighboring layers were inside the bounded blast radius
- why the route chose stabilization, rollback, or degraded-mode posture
- what smallest stabilization or reversal step was actually taken
- what recovery verification ran before closure
- what closure class was declared and why
- what handoff remains for downstream consumers or later remediation work

## Expected artifacts

- `incident_map`
- `stabilization_plan`
- `stabilization_change_set`
- `recovery_decision`
- `recovery_verification_pack`
- `handoff_record`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-scope-drift-detection`
- `aoa-verification-honesty`

Use `aoa-approval-boundary-adherence` to check that stabilization, rollback, or degraded-mode steps respected authority boundaries.
Use `aoa-scope-drift-detection` to check that the incident route stayed within the named blast radius and did not silently widen into other work.
Use `aoa-verification-honesty` to check that recovery verification and closure claims match what actually ran.

## Memory writeback

- `recovery_decision` should survive as a `decision`
- `recovery_verification_pack` should survive as an `audit_event` when it records the actual recovery closure posture
- `handoff_record` should survive as a `provenance_thread`
- `incident_map`, `stabilization_plan`, and `stabilization_change_set` remain route artifacts or referenced artifacts rather than memo writeback kinds

The playbook does not create a new memory-object kind and does not move memo taxonomy into the playbook layer.

## Canonical route

1. Map the incident surface, affected authority surfaces, and bounded blast radius with `aoa-source-of-truth-check` and `aoa-bounded-context-map`.
2. Define the bounded `stabilization_plan`, the rollback-or-degraded path, and the restored-or-degraded stop condition before mutation begins.
3. Use `aoa-approval-gate-check` and `aoa-dry-run-first` to make authority, inspect-first posture, and recovery risk explicit.
4. Apply the smallest stabilization or reversal step through `aoa-change-protocol` and `aoa-safe-infra-change`.
5. Use `aoa-local-stack-bringup` or `aoa-contract-test` to build the `recovery_verification_pack` for the affected surface.
6. Record any durable recovery decision through `aoa-adr-write` and classify closure as `restored`, `degraded-with-handoff`, `rollback-complete`, or `review-stop`.
7. If incident clarity or verification closure is lost, return to the last valid `incident_map`, `stabilization_plan`, `recovery_decision`, or `recovery_verification_pack` anchor and re-enter through `previous_phase`, `review_gate`, `rollback_gate`, or `safe_stop`.
8. Close with the final `recovery_decision` and provenance-safe `handoff_record`, and use `aoa-sanitized-share` when the remaining consumer or remediation handoff must travel beyond the immediate recovery owners.
