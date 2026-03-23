---
id: AOA-P-0007
name: witness-to-compost-pilot
status: experimental
summary: Routes a nontrivial run through witness capture, bounded memory writeback, and compost promotion into a note or principle candidate.
scenario: witness_compost_pilot
trigger: nontrivial_run_needs_reviewable_trace
prerequisites:
  - trace_boundary_defined
  - redaction_posture_defined
  - reviewable_summary_defined
  - compost_target_defined
participating_agents:
  - architect
  - coder
  - reviewer
  - memory-keeper
required_skill_families:
  - source-of-truth
  - change-protocol
  - memory-curation
  - review
evaluation_posture: strict
memory_posture: deep_recall
fallback_mode: handoff
expected_artifacts:
  - witness_trace_json
  - witness_summary_md
  - compost_note
  - principle_candidate
  - canon_bundle
eval_anchors:
  - aoa-witness-trace-integrity
  - aoa-compost-provenance-preservation
---

# witness-to-compost-pilot

## Intent

Use this playbook when a nontrivial run needs a reviewable witness first and a bounded path toward ToS-facing compost second.

The route keeps five things explicit:
- what the run was trying to do
- what witness artifact survives the run
- how memory writeback stays inside the current memo taxonomy
- how a compost note or principle candidate is formed
- what proof surfaces check trace integrity and provenance preservation

## Trigger boundary

Use this playbook when:
- a run is substantial enough that a witness should survive it
- the output may later become a note, synthesis seed, or principle candidate
- the route crosses memory, review, and ToS-facing digestion boundaries

Do not use this playbook when:
- the task is trivial and no durable witness is needed
- the route is only a memory cleanup pass with no witness-producing run
- the route would require full runtime instrumentation rather than a contract-first public pilot

## Prerequisites

- a trace boundary is named before the run is reviewed
- a redaction posture exists for tool inputs, outputs, and side-effect notes
- a human-readable summary format is defined
- a compost target such as note or principle candidate is named

## Participating agents

- `architect` names the witness boundary and keeps the route bounded before evidence is accepted
- `coder` carries the nontrivial run and its reviewable witness artifact
- `reviewer` checks trace completeness, redaction posture, and whether compost promotion is in-bounds
- `memory-keeper` writes the surviving route into memo-facing objects and prepares the compost note or principle candidate

## Required skills

- `aoa-source-of-truth-check`
- `aoa-change-protocol`

The route may use narrower local memory or review helpers later, but this pilot keeps the public skill surface compact.

## Decision points

1. Decide whether the run is substantial enough to require a witness artifact.
2. Decide whether the witness trace is complete enough to survive review.
3. Decide whether redaction is strong enough for public-safe preservation.
4. Decide whether the witness should stop at note level or move toward a principle candidate.
5. Decide whether a canon bundle is warranted now or should remain deferred.

## Handoffs

- `architect -> coder` after the witness boundary and target run scope are explicit
- `coder -> reviewer` after the witness trace and summary exist
- `reviewer -> memory-keeper` after trace integrity and redaction posture are accepted
- `memory-keeper -> architect` if compost promotion reveals an unresolved design issue or a later canon decision

## Fallback and rollback posture

Fallback mode is `handoff`.

The route should pause or narrow when:
- the witness trace is incomplete
- tool visibility is weak or ambiguous
- redaction posture is missing
- provenance would be severed by pushing directly to principle or canon

When the witness is useful but compost promotion is not ready, preserve the note-level output and hand off the deeper digestion rather than forcing promotion.

## Expected evidence posture

The route should finish with visible evidence for:
- what run was witnessed
- what external effects or state deltas were visible
- how redaction was preserved
- what memo-layer writeback survived
- why the compost result stopped at note, principle candidate, or canon bundle

## Expected artifacts

- `witness_trace_json`
- `witness_summary_md`
- `compost_note`
- optional `principle_candidate`
- optional `canon_bundle`

## Eval anchors

- `aoa-witness-trace-integrity`
- `aoa-compost-provenance-preservation`

Both anchors are draft, review-only pilot anchors in this wave.
They exist to keep witness and compost posture inspectable without pretending the route is production-ready or fully instrumented.

## Memory writeback

- the run-level trace event should survive as an `episode`
- explicit gate or review outcomes may survive as `decision` objects when present
- the route history should survive as a `provenance_thread`
- lifecycle transitions or failure states may survive as `audit_event` objects

The playbook does not introduce a new memory-object kind.

## Canonical route

1. Bound the run and state why a witness artifact is needed.
2. Produce a reviewable witness trace plus a human-readable summary.
3. Review the trace for completeness, tool visibility, redaction, and state-delta clarity.
4. Write the surviving route into memo-layer objects without changing the current taxonomy.
5. Distill the witness into a compost note.
6. Promote to a principle candidate only if provenance, limits, and review posture remain visible.
7. Emit a canon bundle only when the route is already clear enough for bounded reuse.
