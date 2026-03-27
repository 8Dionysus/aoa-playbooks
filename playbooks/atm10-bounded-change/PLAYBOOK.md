---
id: AOA-P-0016
name: atm10-bounded-change
status: experimental
summary: Coordinates an ATM10-scoped repository change through explicit ATM10 canon mapping, overlay-aware bounded mutation, verification, and shareable closeout.
scenario: atm10_bounded_change
trigger: atm10_repo_change_needing_overlay_canon_and_verification
prerequisites:
  - atm10_repo_surface_named
  - overlay_authority_named
  - validation_surface_named
  - rollback_or_safe_stop_named
participating_agents:
  - architect
  - coder
  - reviewer
  - memory-keeper
required_skill_families:
  - approval-gate
  - source-of-truth
  - preview
  - change-protocol
  - verification
required_skills:
  - aoa-approval-gate-check
  - atm10-source-of-truth-check
  - aoa-dry-run-first
  - atm10-change-protocol
  - aoa-contract-test
  - aoa-sanitized-share
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - approval_record
  - atm10_canon_map
  - preview_evidence
  - atm10_change_set
  - verification_pack
  - shareable_summary
return_posture: artifact_anchor
return_anchor_artifacts:
  - approval_record
  - atm10_change_set
  - verification_pack
return_reentry_modes:
  - previous_phase
  - review_gate
  - safe_stop
eval_anchors:
  - aoa-approval-boundary-adherence
  - aoa-bounded-change-quality
memo_contract_refs:
  - examples/checkpoint_to_memory_contract.example.json
  - examples/provenance_thread.example.json
memo_writeback_targets:
  - decision
  - audit_event
  - provenance_thread
---

# atm10-bounded-change

## Intent

Use this playbook when an ATM10 repository needs a bounded change route that keeps the project overlay in front without losing the broader AoA safety rails.

The route keeps explicit:

- whether approval is already present
- which ATM10 docs or overlays are authoritative
- what preview happened before mutation
- what bounded ATM10 change actually occurred
- which verification and shareable closeout survive the route

## Trigger boundary

Use this playbook when:

- the task is inside an ATM10-flavored repository or overlay
- the route needs ATM10-specific canon before mutation
- approval, preview, verification, or reporting remain part of the work
- the result should leave an overlay-aware change packet rather than generic repo folklore

Do not use this playbook when:

- the repository is not ATM10-shaped
- the task is really a broad architecture refactor outside the ATM10 overlay
- one single skill can finish the work without scenario-level handoffs
- no bounded change surface can be named before execution

## Prerequisites

- the ATM10 repository surface is named
- the overlay authority and canonical docs are explicit
- the validation surface is named before mutation
- the route can stop safely if approval, preview, or verification posture degrades

## Participating agents

- `architect` clarifies the ATM10 canon, approval boundary, and bounded route before mutation
- `coder` applies the ATM10 overlay change once the preview seam and active slice are explicit
- `reviewer` checks that the overlay stayed in scope and that verification remained honest
- `memory-keeper` preserves the resulting `decision`, `audit_event`, and `provenance_thread` without turning project overlay semantics into memo canon

## Required skills

- `aoa-approval-gate-check`
- `atm10-source-of-truth-check`
- `aoa-dry-run-first`
- `atm10-change-protocol`
- `aoa-contract-test`
- `aoa-sanitized-share`

## Decision points

1. Decide whether approval is explicit enough to proceed.
2. Decide which ATM10 surface is authoritative before mutation begins.
3. Decide whether a preview seam should happen before the overlay change.
4. Decide whether the current verification pack is strong enough to trust the ATM10-specific result.
5. Decide whether the route should close with a shareable summary or stop for further review.

## Handoffs

- `architect -> coder` after the ATM10 canon, approval boundary, and bounded slice are explicit
- `coder -> reviewer` after the preview evidence, ATM10 change set, and verification pack exist
- `reviewer -> memory-keeper` after the route can preserve a `decision`, `audit_event`, or `provenance_thread` without widening the overlay semantics
- `reviewer or memory-keeper -> architect` when the route must return to the last approval or verification anchor before another pass

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:

- approval is still ambiguous
- the ATM10 canon is unclear
- the preview seam is being skipped without a named reason
- the overlay change is trying to widen beyond one bounded slice
- the verification pack is too weak for the claimed result

If approval, ATM10 canon, or verification integrity is lost, return to the last valid `approval_record`, `atm10_change_set`, or `verification_pack` anchor before continuing.
If those anchors are no longer trustworthy, stop for review rather than improvise an overlay narrative.

## Expected evidence posture

The route should finish with visible evidence for:

- how approval was classified
- which ATM10 surfaces constrained the route
- what the preview seam did and did not prove
- what exact overlay-aware change was applied
- what verification actually ran
- which artifact anchor governs return, review, or safe stop

## Expected artifacts

- `approval_record`
- `atm10_canon_map`
- `preview_evidence`
- `atm10_change_set`
- `verification_pack`
- `shareable_summary`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-bounded-change-quality`

Use `aoa-approval-boundary-adherence` to check that ATM10 overlay work respected authority boundaries.
Use `aoa-bounded-change-quality` to check that the ATM10 route stayed scoped, verified, and clearly reported.

## Memory writeback

- the main route outcome may survive as a `decision`
- the closing verification record may survive as an `audit_event`
- the handoff trail may survive as a `provenance_thread`
- the ATM10 canon map, preview evidence, and ATM10 change set remain route artifacts unless a later memo pass promotes them explicitly

## Canonical route

1. Use `aoa-approval-gate-check` to classify whether the requested ATM10 change may proceed.
2. Use `atm10-source-of-truth-check` to identify the overlay-aware canonical docs and commands.
3. Use `aoa-dry-run-first` when a meaningful preview seam exists before the real mutation.
4. Use `atm10-change-protocol` to execute the bounded overlay change.
5. Use `aoa-contract-test` when the change touches a boundary worth tightening.
6. Use `aoa-sanitized-share` to prepare a clean closeout when the result must travel beyond the immediate repo context.
7. If approval, canon, or verification integrity is lost, return to the last artifact anchor and re-enter through `previous_phase`, `review_gate`, or `safe_stop`.
