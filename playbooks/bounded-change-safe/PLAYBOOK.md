---
id: AOA-P-0011
name: bounded-change-safe
status: experimental
summary: Coordinates a bounded repository change through explicit approval, canonical orientation, scoped mutation, verification, and a shareable closeout.
scenario: bounded_change_safe
trigger: non_trivial_repo_change_needing_gate_and_verification
prerequisites:
  - requested_change_scoped
  - approval_boundary_named
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
  - change-protocol
  - verification
  - memory-curation
required_skills:
  - aoa-approval-gate-check
  - aoa-source-of-truth-check
  - aoa-bounded-context-map
  - aoa-dry-run-first
  - aoa-change-protocol
  - aoa-contract-test
  - aoa-tdd-slice
  - aoa-adr-write
  - aoa-sanitized-share
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - approval_record
  - source_map
  - scoped_change_set
  - verification_pack
  - shareable_summary
return_posture: artifact_anchor
return_anchor_artifacts:
  - approval_record
  - scoped_change_set
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

# bounded-change-safe

## Intent

Use this playbook when a non-trivial repository change needs more than one bounded workflow to stay safe and reviewable.

The route keeps five things explicit:

- whether approval is already present
- which docs and boundaries are canonical before mutation
- what exact scoped change is being attempted
- which verification closes the route honestly
- what summary or decision record should travel after the change

## Trigger boundary

Use this playbook when:

- the request changes code, config, docs, or operational surfaces in a meaningful way
- approval, source-of-truth clarity, verification, or reporting are part of the route
- the work is bigger than a tiny wording fix but still bounded enough for one coherent wave
- the final output should leave a reviewable change packet and a concise closeout

Do not use this playbook when:

- one single skill can finish the job without meaningful handoffs
- the route is really a broad multi-repo or long-horizon scenario
- approval posture is irrelevant and the task is an obviously safe tiny fix
- the task is mainly routing logic, role taxonomy, or proof doctrine work

## Prerequisites

- the requested change can be stated in one bounded sentence
- the approval boundary is already explicit
- the current validation surface is named before mutation begins
- a rollback or safe-stop posture exists if verification fails

## Participating agents

- `architect` clarifies canonical docs, boundary notes, and approval posture before the route mutates
- `coder` applies the bounded change once the active slice and verification surface are explicit
- `reviewer` checks that scope, verification, and reporting stayed honest
- `memory-keeper` preserves the surviving decision and audit artifacts without turning the route into a memory taxonomy exercise

## Required skills

- `aoa-approval-gate-check`
- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-tdd-slice`
- `aoa-adr-write`
- `aoa-sanitized-share`

## Decision points

1. Decide whether approval is already explicit enough to proceed.
2. Decide whether the route needs source-of-truth mapping or boundary clarification before mutation.
3. Decide whether a preview or dry-run seam should happen before the real change.
4. Decide whether the current verification pack is strong enough to close the bounded slice honestly.
5. Decide whether the result needs an ADR, a sanitized summary, or both.
6. Decide whether the route should continue, return to the last artifact anchor, or stop for review.

## Handoffs

- `architect -> coder` after the approval boundary, source map, and scoped change target are explicit
- `coder -> reviewer` after the scoped change set and verification pack exist
- `reviewer -> memory-keeper` after the closeout artifacts are explicit enough to survive as a decision, audit event, or provenance thread
- `reviewer or memory-keeper -> architect` when the route must return to the last approval or verification anchor before another pass

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:

- approval is still ambiguous
- the source map is not clear enough to constrain mutation
- the preview seam is being skipped without a named reason
- the verification pack is too weak to trust the result
- the route starts widening into unrelated cleanup or hidden follow-on work

If approval, scope, or verification integrity is lost, return to the last valid `approval_record`, `scoped_change_set`, or `verification_pack` anchor before further mutation.
If those anchors are no longer trustworthy, stop for review rather than improvise continuity.

## Expected evidence posture

The route should finish with visible evidence for:

- how approval was classified
- which source surfaces constrained the change
- what exact scoped change was applied
- what verification actually ran
- which anchor governed any return or safe stop
- what summary or decision artifact survived the route

## Expected artifacts

- `approval_record`
- `source_map`
- `scoped_change_set`
- `verification_pack`
- `shareable_summary`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-bounded-change-quality`

Use `aoa-approval-boundary-adherence` to check that the route did not cross authority boundaries silently.
Use `aoa-bounded-change-quality` to check that the change stayed scoped, verified, and clearly reported.

## Memory writeback

- the main route decision may survive as a `decision`
- the verification closeout may survive as an `audit_event`
- the handoff trail may survive as a `provenance_thread`
- the source map, scoped change set, and shareable summary remain route artifacts unless a later memo pass promotes them explicitly

## Canonical route

1. Use `aoa-approval-gate-check` to classify whether the requested change can proceed now.
2. Use `aoa-source-of-truth-check` and `aoa-bounded-context-map` to make the source map and boundaries explicit.
3. Use `aoa-dry-run-first` when a meaningful preview seam exists.
4. Execute the bounded mutation through `aoa-change-protocol`.
5. Tighten confidence with `aoa-contract-test` or `aoa-tdd-slice` when the verification surface needs strengthening.
6. Record any durable decision through `aoa-adr-write` and prepare any outbound summary through `aoa-sanitized-share`.
7. If the route loses approval, scope, or verification integrity, return to the last artifact anchor and re-enter through `previous_phase`, `review_gate`, or `safe_stop`.
