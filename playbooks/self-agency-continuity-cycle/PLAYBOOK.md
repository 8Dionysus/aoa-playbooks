---
id: AOA-P-0029
name: self-agency-continuity-cycle
status: experimental
summary: Coordinates bounded self-agency continuity across reviewed anchors, revision windows, explicit reanchor decisions, bounded memo relaunch aids, derived continuity refresh, and proof without turning continuity into hidden runtime autonomy.
scenario: self_agency_continuity_cycle
trigger: reviewed_anchor_needing_bounded_continuity_across_revision_windows_and_reanchor
prerequisites:
  - reviewed_anchor_artifact_named
  - continuity_thread_and_revision_window_named
  - reanchor_boundary_named
  - memo_relaunch_and_stats_surfaces_named
  - proof_boundary_named
  - defer_or_safe_stop_line_named
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
  - aoa-checkpoint-closeout-bridge
  - aoa-session-route-forks
  - aoa-session-self-diagnose
  - aoa-session-self-repair
  - aoa-session-progression-lift
  - aoa-source-of-truth-check
  - aoa-bounded-context-map
  - aoa-approval-gate-check
  - aoa-dry-run-first
  - aoa-change-protocol
  - aoa-contract-test
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - continuity_window
  - reflective_revision_decision
  - reanchor_decision
  - anchor_trace
  - continuity_writeback_record
  - continuity_summary_refresh_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - continuity_window
  - reanchor_decision
  - anchor_trace
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
eval_anchors:
  - aoa-continuity-anchor-integrity
  - aoa-reflective-revision-boundedness
  - aoa-self-reanchor-correctness
memo_recall_modes:
  - working
  - episodic
  - semantic
  - lineage
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_capsule_then_expand
memo_checkpoint_posture: not_needed
memo_source_route_policy: required
memo_contract_refs:
  - examples/recall_contract.router.lineage.json
  - examples/recall_contract.object.working.phase-alpha.json
  - examples/checkpoint_to_memory_contract.example.json
  - examples/provenance_thread.example.json
memo_writeback_targets:
  - decision
  - audit_event
  - state_capsule
  - provenance_thread
---

# self-agency-continuity-cycle

## Intent

Use this playbook when the honest route has outgrown one owner follow-through
move, one rollout window, or one reviewed growth cycle step, and now needs to
preserve bounded continuity across more than one reviewed anchor.

The route keeps six things explicit:
- which reviewed anchor artifact still governs continuity now
- which `continuity_ref` and `revision_window_ref` define the current bounded
  window rather than the whole session residue
- when reflective revision is honest and when the route must stop revising and
  issue one explicit `reanchor_decision`
- which memo-side relaunch aids are allowed without becoming continuity truth
- which derived continuity summaries may refresh and what they remain
  subordinate to
- what anchor survives if boundedness, owner fit, or verification posture is
  lost

This playbook is wider than `AOA-P-0023` once the route is no longer one
reviewed closeout handoff plus one owner move, but a longer continuity lane
across several bounded windows.
It is distinct from `AOA-P-0025` because the route anchor is not candidate
lineage through harvest, seed staging, owner landing, and proof, but
continuity across reviewed anchors, reflective revision, and explicit
reanchor.
It is distinct from `AOA-P-0028` because the route is not a shared-root Codex
rollout campaign with drift, rollback, and checked-in rollout history.

## Trigger boundary

Use this playbook when:
- a reviewed anchor already exists and the route must keep continuity across
  more than one bounded revision window
- reflective revision is required, but only inside a named
  `revision_window_ref`
- the route may need explicit reanchor rather than unbounded forward motion
- memo-side relaunch, derived continuity refresh, and bounded proof all matter
  in one reviewable route

Do not use this playbook when:
- there is no reviewed anchor artifact yet
- the route is only one owner follow-through move or one closeout continuity
  handoff
- the route is really a candidate-to-seed-to-owner growth cycle, which belongs
  in `AOA-P-0025`
- the route is really a shared-root rollout operations campaign, which belongs
  in `AOA-P-0028`
- the continuity claim is being narrated from vague chat residue or hidden
  runtime retries

## Prerequisites

- the current reviewed anchor artifact is named before mutation begins
- the `continuity_ref` and bounded `revision_window_ref` are explicit enough to
  keep the route inspectable
- the reanchor boundary is explicit enough to say what event would require
  return now
- memo relaunch and stats-summary surfaces are named before any derived refresh
  begins
- proof stays bounded to continuity integrity, revision boundedness, or
  reanchor correctness rather than broad autonomy claims
- the route can say when it must defer or safe-stop instead of widening context

## Participating agents

- `architect` maps the current anchor artifact, continuity thread, revision
  boundary, and stop-lines before mutation begins
- `coder` applies the smallest honest continuity or reanchor move once the
  current anchor and boundary are explicit
- `reviewer` checks that continuity, memo aids, stats summaries, and proof stay
  in their owning layers
- `evaluator` checks that anchor integrity, reflective revision boundedness,
  and reanchor correctness claims match the evidence posture
- `memory-keeper` preserves bounded relaunch aids without letting memory become
  continuity truth

## Required skills

- `aoa-checkpoint-closeout-bridge`
- `aoa-session-route-forks`
- `aoa-session-self-diagnose`
- `aoa-session-self-repair`
- `aoa-session-progression-lift`
- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`

## Decision points

1. Decide whether the current reviewed anchor is still strong enough to govern
   another bounded continuity window.
2. Decide whether the next honest move is bounded reflective revision, explicit
   reanchor, or safe stop.
3. Decide which artifact remains the last valid `anchor_artifact_ref` if the
   route loses boundedness.
4. Decide whether diagnosis or repair is needed before another continuity
   window can stay honest.
5. Decide which memo-side relaunch aids are earned without letting memory
   overrule owner truth.
6. Decide whether a derived continuity summary may refresh without outranking
   reviewed anchors.
7. Decide which bounded proof question is actually live now:
   continuity integrity, revision boundedness, or reanchor correctness.
8. Decide whether the route closes as continued continuity, reanchored
   continuity, defer, or safe stop.

## Handoffs

- `architect -> coder` after the current anchor artifact, revision window, and
  reanchor boundary are explicit
- `coder -> reviewer` after the current continuity artifacts exist, whether the
  move was revision, reanchor, or bounded refresh
- `reviewer -> evaluator` after anchor integrity, boundedness, and proof
  posture are explicit enough to support proceed, defer, or stop
- `reviewer or evaluator -> architect` when continuity drift, owner drift, or
  proof drift forces return to the last valid anchor
- `evaluator -> memory-keeper` after the route can preserve one bounded relaunch
  aid without turning memo into continuity sovereign
- `memory-keeper -> architect` only when the surviving writeback or residual
  handoff proves another governed continuity window still remains

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the current `anchor_artifact_ref` is missing, contradictory, or weaker than
  the claimed continuity posture
- the `revision_window_ref` has widened into generic session residue
- memo or stats are being asked to replace reviewed anchor truth
- reflective revision keeps moving but no explicit reanchor criterion survives
- the route starts acting like hidden autonomy rather than bounded continuity

If anchor integrity, boundedness, or verification posture is lost, return to
the last valid `continuity_window`, `reanchor_decision`, or `anchor_trace`
anchor before further mutation.
If no honest anchor remains, stop and defer rather than narrate self-agency by
inertia.

## Expected evidence posture

The route should finish with visible evidence for:
- which reviewed anchor artifact governed the route
- what `continuity_ref`, `revision_window_ref`, and `reanchor_ref` were active
- what reflective revision stayed inside the bounded window
- whether and why the route had to reanchor
- what memo writeback was earned and why it stayed subordinate to anchor truth
- what continuity summary refreshed and which reviewed anchors it remained
  downstream of

## Expected artifacts

- `continuity_window`
- `reflective_revision_decision`
- `reanchor_decision`
- `anchor_trace`
- `continuity_writeback_record`
- `continuity_summary_refresh_record`

## Eval anchors

- `aoa-continuity-anchor-integrity`
- `aoa-reflective-revision-boundedness`
- `aoa-self-reanchor-correctness`

Use `aoa-continuity-anchor-integrity` when the route needs to prove that the
current continuity window still resolves to one inspectable anchor chain.
Use `aoa-reflective-revision-boundedness` when the route needs to prove that
reflective revision stayed inside the named revision window instead of widening
by convenience.
Use `aoa-self-reanchor-correctness` when the route needs to prove that reanchor
returned to the last valid artifact rather than to remembered chat continuity.
All three eval anchors are still draft and review-only surfaces, so they keep
claim limits visible and do not turn the playbook into proof authority.

## Memory writeback

- the surviving anchor choice may persist as an `anchor`
- one explicit continuity or reanchor branch choice may persist as a `decision`
- one bounded continuity drift or defer trail may persist as an `audit_event`
- one relaunch-ready continuity state may persist as a `state_capsule`
- one explicit continuity lineage may persist as a `provenance_thread`
- `continuity_window`, `reflective_revision_decision`, `reanchor_decision`,
  `anchor_trace`, and `continuity_summary_refresh_record` remain route
  artifacts or cited evidence rather than memo kinds

This playbook does not invent a new continuity memory family and does not move
continuity truth, proof truth, or stats truth into the playbook layer.

## Canonical route

1. Start from one reviewed anchor artifact and use
   `aoa-checkpoint-closeout-bridge`, `aoa-source-of-truth-check`, and
   `aoa-bounded-context-map` to name the current `continuity_ref`,
   `revision_window_ref`, and `anchor_artifact_ref` before mutation begins.
2. Use `aoa-session-route-forks` to choose whether the next honest move is
   bounded reflective revision, explicit reanchor, or safe stop instead of
   drifting by convenience.
3. If boundedness, owner fit, or verification posture is weak, use
   `aoa-session-self-diagnose`, `aoa-session-self-repair`, and
   `aoa-session-progression-lift` only as far as the current continuity route
   actually requires.
4. Use `aoa-approval-gate-check` and `aoa-dry-run-first` before any mutation
   that would widen the continuity window, shift the anchor, or refresh a
   derived summary.
5. Land the smallest honest continuity or reanchor artifact through
   `aoa-change-protocol`, and tighten any touched boundary with
   `aoa-contract-test` so the next anchor remains inspectable.
6. Refresh memo-side relaunch aids and derived continuity summaries only after
   the current reviewed anchor and route artifacts are explicit, and keep both
   subordinate to those anchors.
7. Run only the narrow proof bundle that matches the current question, and do
   not let proof widen into a total self-agency verdict.
8. Close with continued continuity, reanchored continuity, defer, or safe
   stop; if anchor integrity or boundedness is lost, return through
   `previous_phase`, `review_gate`, `rollback_gate`, or `safe_stop` before
   claiming continuity.
