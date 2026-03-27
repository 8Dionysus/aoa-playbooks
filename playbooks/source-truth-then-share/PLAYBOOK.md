---
id: AOA-P-0015
name: source-truth-then-share
status: experimental
summary: Coordinates documentation authority cleanup through explicit canon mapping, decision capture, and sanitized outward sharing.
scenario: source_truth_then_share
trigger: documentation_authority_drift_or_share_request
prerequisites:
  - affected_doc_surface_named
  - authority_question_explicit
  - share_boundary_named
participating_agents:
  - architect
  - coder
  - reviewer
  - memory-keeper
required_skill_families:
  - source-of-truth
  - decision-docs
  - sharing
  - review
required_skills:
  - aoa-source-of-truth-check
  - aoa-adr-write
  - aoa-sanitized-share
evaluation_posture: required
memory_posture: light_recall
fallback_mode: handoff
expected_artifacts:
  - authority_map
  - overlap_notes
  - documentation_decision
  - shareable_summary
return_posture: artifact_anchor
return_anchor_artifacts:
  - authority_map
  - documentation_decision
  - shareable_summary
return_reentry_modes:
  - previous_phase
  - review_gate
  - safe_stop
eval_anchors:
  - aoa-ambiguity-handling
  - aoa-artifact-review-rubric
memo_contract_refs:
  - examples/checkpoint_to_memory_contract.example.json
  - examples/provenance_thread.example.json
memo_writeback_targets:
  - decision
  - audit_event
  - provenance_thread
---

# source-truth-then-share

## Intent

Use this playbook when the real work is to clarify authority first, then prepare an outward-facing summary that reflects canon instead of replacing it.

The route keeps explicit:

- which files are authoritative
- which docs are summary-only or overlapping
- what documentation decision should survive the cleanup
- what redaction or sanitization boundary applies before sharing

## Trigger boundary

Use this playbook when:

- top-level or summary docs are drifting away from canon
- a human-facing explanation is needed after authority is clarified
- the route needs both a canon decision and a public-safe report
- the work is larger than one isolated doc tweak but smaller than a broad rollout

Do not use this playbook when:

- the task is mainly operational mutation or infrastructure work
- the route is really a multi-repo rollout that needs broader sequencing
- no share boundary exists and the task is fully internal
- a single skill can finish the work without meaningful handoffs

## Prerequisites

- the affected doc or guidance surface is named
- the main authority question is explicit before edits begin
- the share boundary is clear enough to know what must be sanitized

## Participating agents

- `architect` maps the authority question and the canonical file set
- `coder` applies the smallest documentation change once the canon is explicit
- `reviewer` checks that the summary reflects authority rather than redefining it
- `memory-keeper` preserves the surviving `decision`, `audit_event`, and `provenance_thread` without turning the route into memo taxonomy design

## Required skills

- `aoa-source-of-truth-check`
- `aoa-adr-write`
- `aoa-sanitized-share`

## Decision points

1. Decide which file is authoritative for the target concern.
2. Decide which summaries should shrink into link-driven entrypoints rather than duplicate canon.
3. Decide whether the change needs a durable documentation decision through `aoa-adr-write`.
4. Decide what must be redacted before the result can travel.
5. Decide whether the route closes with a publishable summary or should hand off for later review.

## Handoffs

- `architect -> coder` after the authority map and summary-vs-canon split are explicit
- `coder -> reviewer` after the documentation decision and shareable summary draft exist
- `reviewer -> memory-keeper` after the route can preserve its `decision`, `audit_event`, and `provenance_thread` without treating summary text as canon
- `reviewer or memory-keeper -> architect` when canon is still ambiguous enough that the route must return to the last authority anchor

## Fallback and rollback posture

Fallback mode is `handoff`.

Pause or hand off when:

- authority remains ambiguous
- the summary starts trying to replace canon
- the documentation decision is still fuzzy
- redaction needs are stronger than the current summary supports
- the route widens into unrelated repo cleanup

If authority or redaction posture is lost, return to the last valid `authority_map`, `documentation_decision`, or `shareable_summary` anchor before continuing.
If no honest anchor remains, hand the route off for review rather than forcing a summary that outruns canon.

## Expected evidence posture

The route should finish with visible evidence for:

- which files were declared authoritative
- which overlaps or summary drift were found
- what durable documentation decision was made
- what sanitization boundary governed the outward-facing report
- which artifact anchor supports return, review, or safe stop

## Expected artifacts

- `authority_map`
- `overlap_notes`
- `documentation_decision`
- `shareable_summary`

## Eval anchors

- `aoa-ambiguity-handling`
- `aoa-artifact-review-rubric`

Use `aoa-ambiguity-handling` to check that the route handled authority ambiguity explicitly instead of guessing.
Use `aoa-artifact-review-rubric` to check that the resulting shareable summary is reviewably strong on the visible task surface.

## Memory writeback

- the authority or documentation decision may survive as a `decision`
- the closeout review record may survive as an `audit_event`
- the handoff trail may survive as a `provenance_thread`
- the authority map, overlap notes, and shareable summary remain route artifacts unless a later memo pass promotes them explicitly

## Canonical route

1. Use `aoa-source-of-truth-check` to identify the authoritative files and the summary surfaces that should point back to them.
2. Apply the smallest bounded documentation change that makes the authority map legible.
3. Use `aoa-adr-write` when the route introduces a durable documentation or workflow decision.
4. Use `aoa-sanitized-share` to prepare a clean outward-facing summary that reflects the canon review.
5. If canon or redaction posture becomes unclear, return to the last artifact anchor and re-enter through `previous_phase`, `review_gate`, or `safe_stop`.
