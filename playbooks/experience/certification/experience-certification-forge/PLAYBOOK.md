---
id: AOA-P-0047
name: experience-certification-forge
status: experimental
summary: Coordinates an experience-derived assistant/service patch through regression, rollback, and operator-review certification gates without granting Codex certification authority.
scenario: experience_certification_forge
trigger: reviewed_experience_patch_ready_for_release_candidate
prerequisites:
  - reviewed_experience_candidate
  - release_candidate_named
  - regression_pack_named
  - rollback_drill_named
  - operator_review_authority_named
participating_agents:
  - architect
  - coder
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - boundary-shaping
  - change-protocol
  - contract-test
  - evaluation
  - memory-curation
required_skills:
  - aoa-bounded-context-map
  - aoa-change-protocol
  - aoa-contract-test
  - aoa-source-of-truth-check
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: safe_stop
expected_artifacts:
  - release_candidate
  - regression_pack
  - certification_gate_result
  - rollback_drill_result
  - operator_review_request
return_posture: review_anchor
return_anchor_artifacts:
  - certification_gate_result
  - rollback_drill_result
return_reentry_modes:
  - review_gate
  - safe_stop
eval_anchors:
  - aoa-experience-certification-gate-integrity
memo_recall_modes:
  - episodic
  - semantic
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_then_expand
memo_checkpoint_posture: required
memo_source_route_policy: required
---

# experience-certification-forge

## Intent

Use this playbook when a reviewed experience patch is ready to become a release
candidate and the route must prove regression coverage, rollback readiness, and
authorized operator review before any versioned assistant/service release.

The playbook coordinates the v0.4 certification forge. It does not deploy the
release and it does not certify anything by itself.

## Trigger boundary

Use this playbook when:

- the Wave 1 experience candidate has a reviewed verdict
- a release candidate can be named without hidden projection
- regression and rollback evidence can be produced before approval
- the operator/reviewer authority is explicit

Do not use this playbook when:

- Codex is being asked to certify
- there is no rollback drill path
- the patch needs runtime deployment or rollout-ring promotion
- the task is only a stats dashboard or routing hint

## Prerequisites

- the reviewed experience candidate is named
- the release candidate is named
- the regression pack is named
- the rollback drill is named
- the operator review authority is named

## Participating agents

- `architect` keeps the release boundary, certification authority, and
  recharter path explicit
- `coder` repairs bounded regression or rollback fixture gaps when review asks
  for them
- `reviewer` checks that the packet does not imply Codex certification or
  release approval
- `evaluator` runs the bounded certification-gate proof surface
- `memory-keeper` preserves only review-approved revision or retention notes

## Required skills

- `aoa-bounded-context-map`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-source-of-truth-check`

## Decision points

1. Confirm the reviewed experience candidate and release candidate.
2. Bind the regression pack and golden cases.
3. Run the certification-gate proof bundle.
4. Prove rollback drill evidence before operator review.
5. Route to authorized operator review or safe-stop.

## Handoffs

- `architect -> evaluator` after the release candidate and authority boundary
  are named
- `evaluator -> coder` when regression or rollback fixture gaps need repair
- `coder -> reviewer` after evidence artifacts exist
- `reviewer -> memory-keeper` only after a memory gate allows revision ledger
  writeback
- `reviewer -> architect` when the route needs recharter

## Fallback and rollback posture

Fallback mode is `safe_stop`.

Stop when:

- certification authority is missing
- regression coverage is missing
- rollback drill evidence is missing
- compatibility requires recharter
- any step asks Codex to certify or approve release

## Expected evidence posture

The route should finish with visible evidence for:

- release candidate shape
- regression pack coverage
- certification gate verdict
- rollback drill result
- operator review request or denial

## Expected artifacts

- `release_candidate`
- `regression_pack`
- `certification_gate_result`
- `rollback_drill_result`
- `operator_review_request`

## Eval anchors

- `aoa-experience-certification-gate-integrity`

This eval anchor remains a draft and review-only surface, so it helps bound the
certification-gate claim without turning the playbook into proof or release
authority.

## Memory writeback

- the certification gate result may survive only after review
- rollback drill evidence may survive as a bounded audit or revision note
- retention watch follow-up remains a route artifact unless a later memo gate
  promotes it explicitly
- no memory writeback may certify, approve release, or authorize deployment

## Canonical route

1. Name the reviewed candidate and release candidate.
2. Bind the regression pack.
3. Run the bounded certification gate.
4. Prove rollback drill evidence.
5. Request authorized operator review.
6. Record retention-watch follow-up only after approval.
