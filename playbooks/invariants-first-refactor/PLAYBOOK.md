---
id: AOA-P-0013
name: invariants-first-refactor
status: experimental
summary: Coordinates a structural refactor through explicit boundary mapping, property capture, bounded code movement, and post-change coverage audit.
scenario: invariants_first_refactor
trigger: structural_refactor_needing_invariant_guardrails
prerequisites:
  - refactor_target_bounded
  - boundary_question_named
  - invariant_surface_named
  - verification_path_named
participating_agents:
  - architect
  - coder
  - reviewer
  - memory-keeper
required_skill_families:
  - context-mapping
  - core-boundary
  - invariants
  - refactor
  - verification
required_skills:
  - aoa-bounded-context-map
  - aoa-core-logic-boundary
  - aoa-property-invariants
  - aoa-tdd-slice
  - aoa-port-adapter-refactor
  - aoa-invariant-coverage-audit
  - aoa-contract-test
  - aoa-adr-write
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - context_map
  - invariant_ledger
  - refactor_change_set
  - verification_pack
  - architecture_note
return_posture: artifact_anchor
return_anchor_artifacts:
  - context_map
  - invariant_ledger
  - verification_pack
return_reentry_modes:
  - previous_phase
  - review_gate
  - safe_stop
eval_anchors:
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

# invariants-first-refactor

## Intent

Use this playbook when a structural refactor needs explicit boundaries and behavioral invariants before code movement accelerates.

The route keeps explicit:

- which contexts and seams the refactor is about
- which properties must survive the change
- which bounded slice is actually moving now
- what audit closes the route after the code shifts

## Trigger boundary

Use this playbook when:

- the route is a real structural refactor rather than a tiny local fix
- behavior must stay stable while boundaries move
- context mapping, core-vs-edge decisions, and invariants all matter
- the final route should leave a context map, invariant ledger, and verification pack

Do not use this playbook when:

- the task is a one-file bugfix with no meaningful boundary change
- the route is mainly operational or infrastructure work
- the invariant surface is still too vague to name
- the task is really a scenario about routing, agents, or memory rather than code structure

## Prerequisites

- the refactor target is bounded enough to describe
- the core-vs-edge or context boundary question is explicit
- the invariant surface is named before code movement begins
- a bounded verification path exists before the refactor starts

## Participating agents

- `architect` names the context map, boundary line, and invariant surface
- `coder` performs the bounded code movement once the active slice and audit posture are clear
- `reviewer` checks that the route did not smuggle in silent scope drift or weak verification
- `memory-keeper` preserves the surviving decision, audit, and provenance artifacts without absorbing refactor semantics into the memory layer

## Required skills

- `aoa-bounded-context-map`
- `aoa-core-logic-boundary`
- `aoa-property-invariants`
- `aoa-tdd-slice`
- `aoa-port-adapter-refactor`
- `aoa-invariant-coverage-audit`
- `aoa-contract-test`
- `aoa-adr-write`

## Decision points

1. Decide which contexts or seams must be named before refactor.
2. Decide which invariants must be explicit before code movement starts.
3. Decide whether the route needs a test-first slice before the main refactor.
4. Decide whether the post-change audit is strong enough to trust the new boundary.
5. Decide whether the refactor changed architecture enough to require an ADR.
6. Decide whether the route should continue, return to the invariant ledger, or stop for review.

## Handoffs

- `architect -> coder` after the context map, boundary line, and invariant ledger are explicit
- `coder -> reviewer` after the bounded refactor slice and verification pack exist
- `reviewer -> memory-keeper` after the route can preserve a decision, audit event, or provenance thread without flattening the refactor into folklore
- `reviewer or memory-keeper -> architect` when the route must return to the last context or invariant anchor before another slice

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:

- the context map is still fuzzy
- the invariant ledger is missing or too thin
- the refactor slice is trying to move more than one boundary at once
- the post-change audit is weaker than the structural risk
- the route starts using new abstractions that belong in another AoA layer

If boundary or invariant integrity is lost, return to the last valid `context_map`, `invariant_ledger`, or `verification_pack` anchor before further movement.
If no honest anchor remains, stop for review rather than simulate continuity.

## Expected evidence posture

The route should finish with visible evidence for:

- which contexts and boundaries were named
- which invariants were treated as non-negotiable
- what code movement actually happened
- what coverage audit or contract test closed the route
- what anchor governed any return or stop
- what architectural note survived the route

## Expected artifacts

- `context_map`
- `invariant_ledger`
- `refactor_change_set`
- `verification_pack`
- `architecture_note`

## Eval anchors

- `aoa-scope-drift-detection`
- `aoa-verification-honesty`

Use `aoa-scope-drift-detection` to check that the refactor did not silently widen beyond the named slice.
Use `aoa-verification-honesty` to check that the route reports its post-change evidence truthfully.

## Memory writeback

- the main architectural choice may survive as a `decision`
- the closing audit may survive as an `audit_event`
- the route handoff trail may survive as a `provenance_thread`
- the context map, invariant ledger, and refactor change set remain route artifacts unless a later memo pass promotes them explicitly

## Canonical route

1. Use `aoa-bounded-context-map` and `aoa-core-logic-boundary` to make the active seam explicit.
2. Use `aoa-property-invariants` to capture the behavior that must survive the change.
3. Use `aoa-tdd-slice` when a bounded test-first slice will lower risk before the larger refactor.
4. Move the system through `aoa-port-adapter-refactor`.
5. Close the route with `aoa-invariant-coverage-audit` and `aoa-contract-test`.
6. Record any durable structural decision through `aoa-adr-write`.
7. If the route loses boundary or invariant integrity, return to the last artifact anchor and re-enter through `previous_phase`, `review_gate`, or `safe_stop`.
