---
id: AOA-P-0024
name: federated-live-publisher-activation
status: experimental
summary: Coordinates owner-ordered activation of federated live publishers through readiness audit, bounded owner fixes, publication checks, and stats-visible closure.
scenario: federated_live_publisher_activation
trigger: federated_receipt_publishers_needing_owner_ordered_activation_and_readiness_closure
prerequisites:
  - reviewed_readiness_audit_named
  - required_live_sources_named
  - owner_activation_order_named
  - per_owner_fix_scope_bounded
  - verification_and_closeout_pack_named
  - residual_stop_or_handoff_posture_named
participating_agents:
  - architect
  - coder
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - source-of-truth
  - approval-gate
  - preview
  - change-protocol
  - evaluation
  - review
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
  - readiness_audit_pack
  - owner_activation_plan
  - owner_change_set
  - publication_verification_pack
  - stats_visibility_pack
  - residual_handoff_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - readiness_audit_pack
  - owner_activation_plan
  - publication_verification_pack
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

# federated-live-publisher-activation

## Intent

Use this playbook when a reviewed readiness audit already shows that the shared
contract and downstream consumer are ready, but several owner repositories still
need ordered live-publisher activation before the federated route becomes
truthful.

The route keeps six things explicit:
- what readiness audit proved the gap is publisher activation rather than
  schema invention
- what owner order is required so activation stays source-owned instead of being
  patched from the consumer side
- what bounded owner change set is honest for each silent or empty publisher
- what publication checks prove each owner actually emits the required live
  surface
- what stats-visible closure proves the federation now sees the publishers
- what residual handoff remains if one owner cannot activate in the current wave

This playbook is narrower than generic cross-repo rollout once the main route is
activating known publishers in owner order, and wider than one ordinary
single-repo fix.
Use `AOA-P-0010` when the route is a broader cross-repo source-of-truth change.
Use `AOA-P-0021` when the real work is first landing a capability in its owner
repo before any publisher activation route is honest.
Use `AOA-P-0023` when the current problem is preserving the next owner move from
reviewed closeout rather than executing owner-ordered activation itself.
Use `AOA-P-0018` when a validator failure is already the route anchor.

## Trigger boundary

Use this playbook when:
- a reviewed readiness audit names missing or empty live publishers across more
  than one owner repository
- the shared consumer surface is already specific enough to say what sources are
  required
- owner order matters because consumer-side patching would land meaning in the
  wrong repo
- the route needs bounded owner activation plus verification, not just a memo or
  a generic multi-repo note

Do not use this playbook when:
- the problem is still unresolved contract ownership rather than publisher
  activation
- one repository alone owns the whole missing publication path
- the route is really a capability landing campaign, documentation cleanup, or a
  generic cross-repo rollout
- no reviewed readiness audit exists yet
- the remaining work is only to inspect stats without mutating owner publishers

## Prerequisites

- the reviewed readiness audit is named before mutation begins
- the required live source set is explicit enough to keep activation reviewable
- the owner activation order is named before any repo is touched
- each owner fix scope is bounded before publication changes begin
- the verification and closeout pack is named before the first publisher lands
- the route can say what condition forces stop, defer, or residual handoff

## Participating agents

- `architect` maps the readiness audit, owner order, and source-owned boundaries
  before mutation begins
- `coder` applies the smallest bounded owner-publisher changes once the current
  owner slice is explicit
- `reviewer` checks that publisher activation stays owner-local and does not
  collapse into consumer-side convenience fixes
- `evaluator` checks that publication and stats-visible verification actually
  support proceed, defer, or stop
- `memory-keeper` preserves the activation decision, audit trail, and residual
  handoff without inventing a new runtime ledger

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-adr-write`

## Decision points

1. Decide whether the reviewed readiness audit is strong enough to treat owner
   activation as the real next move.
2. Decide which owner repo activates first and which repos must wait for that
   proof before their own slice begins.
3. Decide whether the current owner needs a bounded publisher change, a contract
   test extension, or both.
4. Decide what evidence proves a publisher moved from silent or empty to
   truthfully live.
5. Decide whether stats-visible closure is strong enough to continue to the next
   owner.
6. Decide whether the route closes in one wave or leaves a residual handoff for
   later owners.
7. Decide whether a persistent silent publisher changes the route into
   remediation or defer rather than continued activation by inertia.

## Handoffs

- `architect -> coder` after the readiness audit, owner order, and stop
  conditions are explicit
- `coder -> reviewer` after the current owner change set and publication
  verification notes exist
- `reviewer -> evaluator` after stats-visible closure or defer posture is
  explicit enough to support the next owner step
- `reviewer or evaluator -> architect` when owner ordering, boundary handling,
  or verification integrity drifts enough that the route must return to the
  last valid anchor
- `evaluator -> memory-keeper` after the activation decision and residual
  handoff are explicit enough to survive the route
- `memory-keeper -> architect` only when the residual handoff proves another
  governed owner wave still remains

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the readiness audit is weaker than the claimed owner-activation posture
- owner order remains ambiguous
- a consumer-side workaround starts replacing owner-local publication
- publication checks are weaker than the claimed live status
- stats-visible closure is missing or contradictory
- the route widens into generic ecosystem cleanup instead of bounded publisher
  activation

If owner order, publication truth, or verification integrity is lost, return to
the last valid `readiness_audit_pack`, `owner_activation_plan`, or
`publication_verification_pack` anchor before further mutation.
If no honest owner-local move remains, stop and defer rather than narrate the
federation as live when required publishers are still silent.

## Expected evidence posture

The route should finish with visible evidence for:
- what reviewed readiness audit justified owner-ordered activation now
- what owner order was used and why
- what bounded owner changes made publishers live
- what publication checks proved each owner actually emitted the required
  surface
- what stats-visible closure proved the federation now sees the publisher set
- what residual owner handoff remains, if any

## Expected artifacts

- `readiness_audit_pack`
- `owner_activation_plan`
- `owner_change_set`
- `publication_verification_pack`
- `stats_visibility_pack`
- `residual_handoff_record`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-scope-drift-detection`
- `aoa-verification-honesty`

Use `aoa-approval-boundary-adherence` to check that publisher activation stayed
in the owner repositories instead of drifting into the nearest consumer layer.
Use `aoa-scope-drift-detection` to check that the route stayed bounded to owner
activation rather than widening into generic ecosystem cleanup.
Use `aoa-verification-honesty` to check that publication and stats-visible
closure claims match what actually ran.

## Memory writeback

- the activation or defer decision may survive as a `decision`
- the publication and stats-visible closeout may survive as an `audit_event`
- the residual handoff may survive as a `provenance_thread`
- the `readiness_audit_pack`, `owner_activation_plan`, and `owner_change_set`
  remain route artifacts unless a later memo pass promotes them explicitly

The playbook does not move receipt schema truth, stats ownership, or runtime
ledger semantics out of their owner repos.

## Canonical route

1. Start from one reviewed readiness audit and confirm the required live source
   set plus owner boundaries with `aoa-source-of-truth-check` and
   `aoa-bounded-context-map`.
2. Use `aoa-approval-gate-check` and `aoa-dry-run-first` to make write scope,
   owner order, and stop conditions explicit before mutation begins.
3. Activate the first owner-local publisher with the smallest honest change set
   and extend contract tests only as far as needed to prove the live surface.
4. Verify the owner-local publication path before moving to the next owner so
   silent publishers do not hide behind aggregate narrative.
5. Re-run the consumer-visible stats or readiness audit after each owner slice
   to prove whether the federation now sees the required publication.
6. If one owner remains silent, decide whether the route should stop, defer, or
   hand off rather than letting the next repo absorb its meaning.
7. Use `aoa-adr-write` only if the route introduces a durable owner-order or
   publisher-governance decision that later contributors will need to remember.
8. Close with the publication verification pack, stats-visibility pack, and
   residual handoff record; if owner truth or verification honesty is lost,
   return through `previous_phase`, `review_gate`, `rollback_gate`, or
   `safe_stop` before claiming the federation is live.
