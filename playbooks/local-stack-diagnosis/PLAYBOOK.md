---
id: AOA-P-0014
name: local-stack-diagnosis
status: experimental
summary: Coordinates local environment diagnosis through canonical startup guidance, bounded bring-up, blocker isolation, and a shareable closeout.
scenario: local_stack_diagnosis
trigger: local_stack_unstable_or_startup_path_unclear
prerequisites:
  - canonical_startup_surface_available_or_discoverable
  - bounded_bringup_target_named
  - blocker_reporting_surface_named
  - safe_stop_posture_named
participating_agents:
  - architect
  - coder
  - reviewer
  - memory-keeper
required_skill_families:
  - source-of-truth
  - preview
  - local-bringup
  - verification
  - sharing
required_skills:
  - aoa-source-of-truth-check
  - aoa-dry-run-first
  - aoa-local-stack-bringup
  - aoa-change-protocol
  - aoa-contract-test
  - aoa-sanitized-share
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: safe_stop
expected_artifacts:
  - startup_canon_map
  - preview_evidence
  - blocker_list
  - verification_pack
  - shareable_summary
return_posture: artifact_anchor
return_anchor_artifacts:
  - startup_canon_map
  - blocker_list
  - verification_pack
return_reentry_modes:
  - previous_phase
  - safe_stop
eval_anchors:
  - aoa-verification-honesty
  - aoa-tool-trajectory-discipline
memo_contract_refs:
  - examples/checkpoint_to_memory_contract.example.json
  - examples/provenance_thread.example.json
memo_writeback_targets:
  - decision
  - audit_event
  - provenance_thread
---

# local-stack-diagnosis

## Intent

Use this playbook when the local environment is unstable enough that you need one bounded route from canon discovery to blocker isolation.

The route keeps explicit:

- which startup docs are authoritative
- what the preview seam proved before a bring-up attempt
- what bounded bring-up or repair actually happened
- which blockers still prevent trust in the local stack
- what concise report should survive after the diagnosis

## Trigger boundary

Use this playbook when:

- the local stack will not start or its startup path is unclear
- canonical setup docs, presets, or dependency surfaces may be in tension
- a bounded bring-up attempt is needed before deeper mutation
- the route should end with a blocker report or a small verified fix

Do not use this playbook when:

- the task is purely a broad infra change with a bigger rollback story
- one single skill can finish the work without meaningful handoffs
- the route is really a code-structure refactor rather than local environment diagnosis
- no bounded bring-up target can be named

## Prerequisites

- a likely startup or dependency surface can be named or discovered
- the bring-up target is bounded enough to state before execution
- the report surface for blockers or fixes is explicit
- the route can stop safely if the environment stays unstable

## Participating agents

- `architect` maps the canonical startup surface and the bounded diagnosis target
- `coder` performs the smallest preview, bring-up, or bounded fix once the active seam is clear
- `reviewer` checks that blocker reporting and verification remain honest
- `memory-keeper` preserves the surviving `decision`, `audit_event`, or `provenance_thread` without inventing a new runtime-memory object

## Required skills

- `aoa-source-of-truth-check`
- `aoa-dry-run-first`
- `aoa-local-stack-bringup`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-sanitized-share`

## Decision points

1. Decide which startup surface is actually canonical before touching the environment.
2. Decide whether a preview seam should happen before a real bring-up or reset.
3. Decide whether the current blocker is narrow enough for one bounded `aoa-change-protocol` fix.
4. Decide whether `aoa-contract-test` can strengthen trust around the failing path.
5. Decide whether the route closes with a verified stack, a blocker list, or a safe stop.

## Handoffs

- `architect -> coder` after the startup canon and bounded bring-up target are explicit
- `coder -> reviewer` after preview evidence, bring-up notes, and the verification pack exist
- `reviewer -> memory-keeper` after the route can preserve its `decision`, `audit_event`, and `provenance_thread` without turning transient startup noise into canon
- `reviewer or memory-keeper -> architect` when the route must return to the last viable startup or blocker anchor before another pass

## Fallback and rollback posture

Fallback mode is `safe_stop`.

Pause or stop when:

- the startup canon is still unclear
- the preview seam is skipped without a named reason
- the bring-up attempt widens into unrelated cleanup
- the blocker remains too broad for one bounded fix
- the verification pack is weaker than the claimed diagnosis result

If canon, blocker scope, or verification integrity is lost, return to the last valid `startup_canon_map`, `blocker_list`, or `verification_pack` anchor before continuing.
If those anchors are no longer trustworthy, stop with a bounded blocker report instead of simulating progress.

## Expected evidence posture

The route should finish with visible evidence for:

- which startup or dependency docs were treated as canonical
- what the preview seam did and did not prove
- what bounded bring-up or repair actually happened
- which blockers remain and why
- what verification ran after the diagnosis step
- which artifact anchor governed any return or safe stop

## Expected artifacts

- `startup_canon_map`
- `preview_evidence`
- `blocker_list`
- `verification_pack`
- `shareable_summary`

## Eval anchors

- `aoa-verification-honesty`
- `aoa-tool-trajectory-discipline`

Use `aoa-verification-honesty` to check that the route reports bring-up and verification truthfully.
Use `aoa-tool-trajectory-discipline` to check that diagnosis steps stayed reviewable and bounded instead of becoming terminal folklore.

## Memory writeback

- the main diagnosis or next-step decision may survive as a `decision`
- the closing blocker or verification record may survive as an `audit_event`
- the route handoff trail may survive as a `provenance_thread`
- the startup canon map, preview evidence, and blocker list remain route artifacts unless a later memo pass promotes them explicitly

## Canonical route

1. Use `aoa-source-of-truth-check` to locate the authoritative startup and dependency docs.
2. Use `aoa-dry-run-first` when a bounded preview exists for reset, startup, or migration steps.
3. Use `aoa-local-stack-bringup` to attempt the smallest viable bring-up.
4. If the blocker is now isolated, use `aoa-change-protocol` for one bounded repair.
5. Use `aoa-contract-test` when a boundary check will strengthen trust around the failing path.
6. Use `aoa-sanitized-share` to prepare a concise blocker or recovery summary when the result must travel.
7. If canon, blocker scope, or verification integrity is lost, return to the last artifact anchor and re-enter through `previous_phase` or `safe_stop`.
