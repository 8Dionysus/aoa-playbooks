---
id: AOA-P-0030
name: component-refresh-cycle
status: experimental
summary: Coordinates one reviewed internal component drift signal through a named owner law, bounded refresh decision, owner validation, derived summary refresh, and optional memo writeback without turning maintenance into hidden scheduler authority.
scenario: component_refresh_cycle
trigger: reviewed_component_drift_with_named_owner_law_and_bounded_refresh_route
prerequisites:
  - component_drift_hint_named
  - owner_repo_and_refresh_law_named
  - followthrough_decision_boundary_named
  - owner_validation_surface_named
  - derived_summary_refresh_surface_named
  - rollback_or_safe_stop_line_named
participating_agents:
  - architect
  - coder
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - source-of-truth
  - approval-gate
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
  - aoa-session-self-diagnose
  - aoa-session-self-repair
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - component_drift_hint
  - component_refresh_followthrough_decision
  - component_refresh_receipt
  - component_refresh_summary
  - memo_writeback_ref
return_posture: artifact_anchor
return_anchor_artifacts:
  - component_drift_hint
  - component_refresh_followthrough_decision
  - component_refresh_receipt
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
eval_anchors:
  - aoa-diagnosis-cause-discipline
  - aoa-repair-boundedness
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

# component-refresh-cycle

## Intent

Use this playbook when one internal AoA component is visibly drifting and the
next honest move is one owner-owned refresh route, not generic remediation,
not rollout-history publication, and not open-ended self-mutation.

The route keeps six things explicit:
- which reviewed `component_drift_hint` is actually live now
- which owner repo and owner-local refresh law govern the route
- which `component_refresh_followthrough_decision` chose repair, rebuild,
  reexport, regenerate, defer, or safe stop
- which owner-local `component_refresh_receipt` proves the refresh really
  happened and stayed inside one bounded owner surface
- which derived `component_refresh_summary` may refresh and what it remains
  subordinate to
- whether any memo writeback is honestly earned as bounded recovery context

This playbook is narrower than `AOA-P-0018` because the route is not a generic
failed-validation remediation pass across owned boundaries; it already has a
reviewed drift hint, a named owner law, and one bounded refresh target.
It is distinct from `AOA-P-0025` because the route anchor is not checkpoint
carry, candidate lineage, seed staging, owner landing, and proof.
It is distinct from `AOA-P-0028` because the route is not a shared-root Codex
rollout campaign with drift windows, rollback windows, and checked-in rollout
history.
It is also distinct from `AOA-P-0026` because the route is not the next owner
move for a reviewed candidate or staged seed, but the next owner refresh move
for a named drifting component.

## Trigger boundary

Use this playbook when:
- a reviewed `component_drift_hint` already names one drifting component
- the drifting component has one named owner repo and one owner refresh law
- the route can stay bounded through one refresh decision plus owner
  validation
- derived stats or optional memo follow-through matter, but remain weaker than
  owner validation

Do not use this playbook when:
- the owner repo or owner law is still ambiguous
- the route is really a generic cross-boundary remediation pass, which belongs
  in `AOA-P-0018`
- the route is really a shared-root rollout campaign, which belongs in
  `AOA-P-0028`
- the route is really a lineage-aware growth cycle, which belongs in
  `AOA-P-0025`
- someone is trying to smuggle scheduler authority, hidden runners, or
  autonomous self-maintenance through "refresh" language

## Prerequisites

- the active `component_drift_hint` is reviewed before mutation begins
- the owner repo and owner-local refresh law are named before any mutation
  begins
- the `component_refresh_followthrough_decision` can say whether the next move
  is repair, rebuild, regenerate, reexport, defer, or safe stop
- the owner validation surface is named before the refresh runs
- the derived summary surface is named before any stats refresh begins
- the route can say when it must roll back, defer, or safe-stop instead of
  widening into open-ended maintenance

## Participating agents

- `architect` maps the drift hint, owner law, stop-lines, and owner validation
  surface before mutation begins
- `coder` applies only the smallest honest refresh move once the owner law and
  fallback posture are explicit
- `reviewer` checks that sdk carry, owner receipts, derived summary refresh,
  and memo aids stay in their owning layers
- `evaluator` checks that diagnosis and repair claims match the evidence
  posture rather than maintenance rhetoric
- `memory-keeper` preserves only bounded lessons or recovery context that do
  not outrank owner truth

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-session-self-diagnose`
- `aoa-session-self-repair`

## Decision points

1. Decide whether the active drift hint is strong enough to justify one owner
   refresh route now.
2. Decide which owner-local refresh law actually governs the component.
3. Decide whether the next honest move is repair, rebuild, regenerate,
   reexport, defer, or safe stop.
4. Decide which owner validation surface proves the refresh really landed.
5. Decide whether the derived summary may refresh without outranking owner
   validation.
6. Decide whether memo writeback earned bounded recovery context or no durable
   writeback at all.
7. Decide whether the route closes as `refresh_complete`,
   `rollback_complete`, `refresh_deferred`, or `safe_stop`.

## Handoffs

- `architect -> coder` after the drift hint, owner law, validation surface,
  and stop-lines are explicit
- `coder -> reviewer` after the refresh artifacts exist and the route can show
  whether it repaired, rebuilt, regenerated, reexported, or stopped
- `reviewer -> evaluator` after owner validation, derived summary posture, and
  boundedness are explicit enough to support proceed, rollback, or stop
- `reviewer or evaluator -> architect` when the route loses owner clarity,
  boundedness, or validation posture and must return to the last honest anchor
- `evaluator -> memory-keeper` after a bounded lesson or recovery pattern is
  explicit enough to survive as subordinate memo writeback

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the owner repo or owner refresh law is ambiguous
- the drift hint is weaker than the claimed repair posture
- owner validation is missing or contradictory
- derived stats start speaking stronger than owner validation
- memo writeback starts acting like refresh truth
- the route starts behaving like scheduler authority or a hidden runner

If owner fit, repair boundedness, or validation posture is lost, return to the
last valid `component_drift_hint`,
`component_refresh_followthrough_decision`, or
`component_refresh_receipt` anchor before further mutation.
If no honest anchor remains, stop and defer rather than narrate the component
as self-maintaining by inertia.

## Expected evidence posture

The route should finish with visible evidence for:
- which reviewed `component_drift_hint` governed the route
- which owner repo and owner-local refresh law were active
- which refresh decision was chosen and why
- which owner-local receipt proves the refresh landed
- what derived summary refreshed and which owner surface remained stronger
- whether memo writeback stayed bounded and subordinate

## Eval anchors

- `aoa-diagnosis-cause-discipline` checks that the named drift signal really
  points at the owner-law refresh route rather than a vaguer remediation story.
- `aoa-repair-boundedness` checks that the refresh stayed inside one bounded
  owner move and did not widen into uncontrolled maintenance.
- These eval anchors are still draft, remain review-only, and stay subordinate
  to owner validation even when the route refreshes a derived summary
  afterward.

## Memory writeback

- `decision` is allowed only when the refresh route leaves one bounded owner
  decision worth preserving.
- `audit_event` is allowed only when the repair or rollback path leaves one
  bounded operational witness worth keeping.
- `provenance_thread` is allowed only when the route needs one bounded replay
  thread across the drift hint, followthrough decision, owner receipt, and
  summary refresh.
- No memo writeback target may outrank the owner-local
  `component_refresh_receipt` or act like refresh truth.

## Canonical route

1. Start from one reviewed `component_drift_hint`.
2. Name one owner repo and one owner refresh law.
3. Issue one `component_refresh_followthrough_decision`.
4. Land one owner-local `component_refresh_receipt`.
5. Refresh one derived `component_refresh_summary` only if the owner receipt is
   already stronger.
6. Optionally keep one bounded memo writeback if repeated evidence earns it.

## Expected artifacts

- `component_drift_hint`
- `component_refresh_followthrough_decision`
- `component_refresh_receipt`
- `component_refresh_summary`
- `memo_writeback_ref`
