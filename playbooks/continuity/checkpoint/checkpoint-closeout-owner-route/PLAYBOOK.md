---
id: AOA-P-0050
name: checkpoint-closeout-owner-route
status: experimental
summary: Routes a reviewed checkpoint closeout with multiple surviving candidates into owner-specific follow-through without promoting one mechanical bridge into skill, memo, eval, or playbook truth.
scenario: checkpoint_closeout_owner_route
trigger: reviewed_checkpoint_closeout_with_multiple_owner_candidates_and_keep_open_quest_verdict
prerequisites:
  - reviewed_checkpoint_closeout_pack_named
  - session_memory_or_raw_trace_anchor_named
  - accepted_candidate_set_named
  - owner_repo_and_nearest_wrong_targets_named
  - quest_or_defer_verdict_named
  - stronger_owner_stop_lines_named
participating_agents:
  - architect
  - coder
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - source-of-truth
  - change-protocol
  - review
  - evaluation
  - memory-curation
required_skills:
  - aoa-checkpoint-closeout-bridge
  - aoa-session-donor-harvest
  - aoa-session-progression-lift
  - aoa-quest-harvest
  - aoa-session-route-forks
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
  - reviewed_checkpoint_closeout_pack
  - owner_route_matrix
  - quest_followthrough_decision
  - stronger_owner_handoff_notes
  - proof_or_defer_packet
  - residual_handoff_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - reviewed_checkpoint_closeout_pack
  - owner_route_matrix
  - quest_followthrough_decision
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
eval_anchors:
  - aoa-owner-fit-routing-quality
  - aoa-candidate-lineage-integrity
  - aoa-verification-honesty
memo_recall_modes:
  - episodic
  - semantic
  - lineage
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_capsule_then_expand
memo_checkpoint_posture: preferred
memo_source_route_policy: required
memo_contract_refs:
  - examples/recall/recall_contract.router.lineage.json
  - mechanics/checkpoint/parts/checkpoint-to-memory-mapping/examples/checkpoint_to_memory_contract.example.json
  - examples/support-objects/provenance_thread.example.json
memo_writeback_targets:
  - decision
  - audit_event
  - provenance_thread
---

# checkpoint-closeout-owner-route

## Intent

Use this playbook when a reviewed checkpoint closeout has already produced a
bounded evidence packet, but the closeout still contains more than one surviving
owner candidate and the honest verdict is route, reanchor, keep-open quest,
prove-first, or defer rather than immediate promotion.

The route keeps six things explicit:

- what reviewed checkpoint closeout pack is being used
- what session-memory or raw-trace anchor keeps the closeout reviewable
- which candidates survived the reread and which were dropped or deferred
- which owner repo owns each surviving candidate
- which nearest-wrong target would create false topology
- what artifact survives if the route remains an open quest instead of landing

This playbook is narrower than `AOA-P-0023` when the main pressure is the
checkpoint-closeout owner-routing step itself. Use `AOA-P-0023` after one owner
handoff has been chosen and the work becomes bounded owner-layer authorship.
Use `AOA-P-0026` when the route starts from one already named candidate or seed
and no longer needs checkpoint-closeout carry.

## Trigger boundary

Use this playbook when:

- a reviewed checkpoint closeout exists and has a named closeout execution
  report or equivalent reviewed artifact
- the closeout accepted more than one candidate, owner, or next surface
- at least one candidate is route-shaped and should remain in `aoa-playbooks`
  instead of becoming a premature skill
- at least one candidate points to a stronger owner such as `aoa-skills`,
  `aoa-memo`, `aoa-evals`, `aoa-techniques`, or `aoa-stats`
- the current honest verdict is keep-open quest, reanchor, prove-first, defer,
  or owner-routed landing

Do not use this playbook when:

- there is no reviewed closeout pack or raw/session anchor
- the remaining work is one obvious bounded skill implementation
- the closeout already selected one owner artifact and the route is now normal
  owner-follow-through continuity
- the claim would promote one mechanical bridge artifact into final owner truth
- the route needs live automation, hidden scheduler behavior, MCP authority, or
  runtime dispatch

## Prerequisites

- the reviewed checkpoint closeout pack is named before mutation begins
- the session-memory archive, raw trace, or reviewed artifact anchor is named
  without replacing raw evidence
- the accepted candidate set is visible enough to review as a set
- each surviving candidate has an owner repo, owner shape, and nearest-wrong
  target before follow-through starts
- the quest, promote, defer, prove-first, or drop verdict is explicit before
  any owner artifact is authored
- stronger-owner stop lines are named before playbooks writes anything about
  skills, memo, evals, techniques, stats, routing, or runtime

## Participating agents

- `architect` maps the closeout pack, candidate set, owner route, and stop
  lines before mutation begins
- `coder` writes only the smallest owner-route artifact or quest carry after
  the route matrix is explicit
- `reviewer` checks that owner routing, nearest-wrong targets, and keep-open
  quest posture remain honest
- `evaluator` checks whether proof, defer, drop, or owner landing is supported
  by the reviewed evidence
- `memory-keeper` preserves bounded decisions and provenance without promoting
  closeout summaries into memory truth

## Required skills

- `aoa-checkpoint-closeout-bridge`
- `aoa-session-donor-harvest`
- `aoa-session-progression-lift`
- `aoa-quest-harvest`
- `aoa-session-route-forks`
- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`

## Decision points

1. Decide whether the closeout pack is strong enough for owner-route work.
2. Decide which surviving candidates are route, skill, memo, proof, technique,
   stats, or runtime shaped.
3. Decide which nearest-wrong target would create false topology for each
   candidate.
4. Decide whether the route should keep an open quest, author a playbook-owned
   route artifact, hand off to a stronger owner, prove first, defer, or drop.
5. Decide whether the checkpoint-closeout family has enough recurrence for a
   new playbook route or should remain under an existing continuity playbook.
6. Decide what residual handoff survives if the route remains open.

## Handoffs

- `architect -> coder` after the closeout pack, owner route matrix, and stop
  lines are explicit
- `coder -> reviewer` after the quest carry, route artifact, or owner handoff
  note exists
- `reviewer -> evaluator` after owner-route and nearest-wrong-target claims are
  readable enough to judge
- `reviewer or evaluator -> architect` when a candidate starts drifting toward
  the nearest convenient owner instead of the truthful owner
- `evaluator -> memory-keeper` only after one bounded decision, defer, drop,
  or residual handoff is ready to preserve

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:

- the closeout artifact is mechanical-only and no agent-led review has checked
  the owner route
- owner ambiguity remains high enough that landing would be convenience, not
  truth
- a route-shaped candidate is being flattened into a skill or tool
- a skill-shaped candidate is being inflated into a playbook
- memo, eval, technique, stats, routing, or runtime truth is being absorbed by
  `aoa-playbooks`
- the route depends on hidden automation, daemon behavior, or unreviewed MCP
  authority

If owner fit, proof fit, or quest posture is lost, return to the last valid
`reviewed_checkpoint_closeout_pack`, `owner_route_matrix`, or
`quest_followthrough_decision`. If no honest anchor remains, stop and defer.

## Expected evidence posture

The route should finish with visible evidence for:

- which checkpoint closeout pack was read
- which raw, session-memory, or reviewed artifact anchor preserved provenance
- which candidates survived and which were deferred or dropped
- why each surviving candidate belongs to its owner repo
- why the route chose keep-open quest, reanchor, prove-first, defer, drop, or
  owner landing
- what residual handoff remains for the next pass

## Expected artifacts

- `reviewed_checkpoint_closeout_pack`
- `owner_route_matrix`
- `quest_followthrough_decision`
- `stronger_owner_handoff_notes`
- `proof_or_defer_packet`
- `residual_handoff_record`

## Eval anchors

- `aoa-owner-fit-routing-quality`
- `aoa-candidate-lineage-integrity`
- `aoa-verification-honesty`

Use `aoa-owner-fit-routing-quality` to check that route-shaped, skill-shaped,
memo-shaped, and proof-shaped candidates leave through the right owner.
Use `aoa-candidate-lineage-integrity` to check that candidates did not mutate
identity while moving from checkpoint closeout to owner follow-through.
Use `aoa-verification-honesty` to check that mechanical bridge artifacts are
not narrated as final reviewed truth.

All three eval anchors are draft and review-only surfaces here. They guide
owner-fit and lineage review, but they do not prove promotion, write owner
truth, or grant runtime authority.

## Memory writeback

- the selected owner-route verdict may survive as a `decision`
- a keep-open quest, defer, drop, or proof-first outcome may survive as an
  `audit_event`
- the residual handoff may survive as a `provenance_thread`
- the closeout pack, route matrix, and owner handoff notes remain route
  artifacts unless a later memo pass promotes them explicitly

This playbook does not write memo truth, skill truth, eval proof, technique
doctrine, stats posture, routing authority, or runtime state.

## Canonical route

1. Name the reviewed checkpoint closeout pack and provenance anchor.
2. Build the owner route matrix from the surviving candidates, owner repos,
   owner shapes, and nearest-wrong targets.
3. Run source-of-truth and bounded-context checks before any owner artifact is
   written.
4. Classify each candidate as route, skill, memo, proof, technique, stats, or
   runtime shaped.
5. Choose keep-open quest, reanchor, prove-first, defer, drop, or bounded owner
   landing for the current pass.
6. Preserve the route artifact, stronger-owner handoff note, and residual
   handoff without promoting mechanical closeout output into final truth.
