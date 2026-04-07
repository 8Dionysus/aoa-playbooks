---
id: AOA-P-0023
name: closeout-owner-follow-through-continuity
status: experimental
summary: Coordinates reviewed closeout through persistent owner handoff, bounded owner-layer authorship, and merged follow-through so strong harvests do not lose the next honest move between sessions.
scenario: closeout_owner_follow_through_continuity
trigger: reviewed_closeout_with_owner_handoff_needing_bounded_owner_layer_authorship_and_merge
prerequisites:
  - reviewed_source_or_closeout_pack_named
  - owner_handoff_surface_named
  - next_owner_surface_named
  - owner_repo_boundary_named
  - validation_and_merge_posture_named
  - residual_handoff_or_stop_posture_named
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
  - memory-curation
required_skills:
  - aoa-session-donor-harvest
  - aoa-quest-harvest
  - aoa-source-of-truth-check
  - aoa-bounded-context-map
  - aoa-approval-gate-check
  - aoa-dry-run-first
  - aoa-change-protocol
  - aoa-adr-write
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - reviewed_closeout_pack
  - owner_handoff_bundle
  - owner_authorship_bundle
  - validation_pack
  - merge_record
  - residual_handoff_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - owner_handoff_bundle
  - owner_authorship_bundle
  - validation_pack
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
eval_anchors:
  - aoa-approval-boundary-adherence
  - aoa-verification-honesty
  - aoa-tool-trajectory-discipline
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

# closeout-owner-follow-through-continuity

## Intent

Use this playbook when a reviewed closeout is strong enough to name the next
owner-layer move, and the honest route is to keep that move alive through a
persistent handoff, bounded owner authorship, and merge closure rather than
letting it dissolve into session memory.

The route keeps six things explicit:
- what reviewed source or closeout justified follow-through now
- what owner handoff bundle names the next truthful owner repo and surface
- whether the next move is draft-owner-artifact or author-owner-artifact
- what bounded authoring wave lands the owner artifact honestly
- what validation and merge evidence proves the route really closed
- what residual handoff remains if the current wave cannot fully finish

This playbook is narrower than generic owner-first landing once the main problem
is continuity across sessions, and wider than one ordinary single-repo edit.
Use `AOA-P-0021` when the main route is capability landing across owner-first
lineage and rollout stages.
Use `AOA-P-0022` when the route anchor is workspace-foundation landing itself.
Use `AOA-P-0015` when the remaining work is only source-of-truth cleanup or
sharing rather than owner-follow-through continuity.

## Trigger boundary

Use this playbook when:
- a reviewed source or reviewed closeout already contains enough evidence that
  owner-layer follow-through should happen now
- the route depends on one persistent owner handoff rather than on operator
  memory or chat recap
- the next honest move spans closeout, owner-repo selection, bounded authorship,
  validation, and merge closure
- the route may cross more than one repository even if the final authored
  artifact lives in only one owner repo

Do not use this playbook when:
- the source is still too raw for `aoa-session-donor-harvest` or
  `aoa-quest-harvest` to close honestly
- the task is already one obvious single-repo authoring move and there is no
  real cross-session continuity risk
- the route is really capability landing, workspace landing, or remediation,
  which belong in sibling playbooks
- the remaining work is only to write a memo or note without owner-layer
  artifact authorship

## Prerequisites

- the reviewed source or closeout pack is named before further mutation begins
- the owner handoff surface is explicit enough to keep follow-through reviewable
- the next owner surface is named before authorship begins
- the owner repo boundary is explicit enough to prevent convenience landing in
  the wrong layer
- the validation and merge posture is named before the authoring wave starts
- the route can say whether it closes fully now or must leave a residual handoff

## Participating agents

- `architect` maps the reviewed source, owner repo, next surface, and stop
  conditions before mutation begins
- `coder` applies the smallest bounded owner-layer authoring wave once the
  handoff boundary is explicit
- `reviewer` checks that persistent handoff, owner selection, and authored
  closure stay honest rather than drifting into vague “we should do this later”
- `evaluator` checks that validation and merge evidence really support closure
  or honest defer
- `memory-keeper` preserves the surviving decision, audit trail, and residual
  handoff without inventing a new memory taxonomy

## Required skills

- `aoa-session-donor-harvest`
- `aoa-quest-harvest`
- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-adr-write`

## Decision points

1. Decide whether the reviewed source is strong enough for donor-harvest now.
2. Decide whether a bounded candidate should stay a harvest draft or close
   through quest promotion.
3. Decide which owner repo and next surface are the truthful follow-through
   target.
4. Decide whether the current wave can author the owner artifact now or should
   stop at persistent handoff.
5. Decide what validation pack proves the authored owner artifact is merge-ready.
6. Decide whether merge closes the route or leaves a residual handoff for later.
7. Decide whether the authored wave itself warrants a new harvest pass.

## Handoffs

- `architect -> coder` after the reviewed source, owner handoff, owner repo, and
  next-surface boundary are explicit
- `coder -> reviewer` after the owner authorship bundle and validation notes
  exist
- `reviewer -> evaluator` after merge, defer, or residual handoff posture is
  explicit enough to support closure
- `reviewer or evaluator -> architect` when owner selection, next-surface
  naming, or closure integrity drifts enough that the route must return to the
  last valid handoff anchor
- `evaluator -> memory-keeper` after the route can name merge, defer, or
  residual handoff with bounded evidence
- `memory-keeper -> architect` only when the residual handoff proves that
  another governed route still remains

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the reviewed source is weaker than the claimed follow-through posture
- the owner repo or next surface remains ambiguous
- the owner handoff bundle is missing, unreadable, or no longer matches the
  intended authoring move
- the authoring wave widens into unrelated repo cleanup or broad rollout
- merge or validation evidence is weaker than the claimed closure
- the residual handoff is unclear enough that the next move would again depend
  on operator memory

If owner selection, handoff integrity, or merge closure is lost, return to the
last valid `reviewed_closeout_pack`, `owner_handoff_bundle`, or `validation_pack`
anchor before further mutation.
If no honest owner move remains, stop and defer rather than narrate continuity
that is still memory-bound.

## Expected evidence posture

The route should finish with visible evidence for:
- what reviewed source or closeout justified owner-layer follow-through now
- what owner handoff named the next repo and surface
- what owner artifact was authored and why that surface was truthful
- what validations and merge evidence proved the route really moved forward
- what residual handoff remains, if any

## Expected artifacts

- `reviewed_closeout_pack`
- `owner_handoff_bundle`
- `owner_authorship_bundle`
- `validation_pack`
- `merge_record`
- `residual_handoff_record`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-verification-honesty`
- `aoa-tool-trajectory-discipline`

Use `aoa-approval-boundary-adherence` to check that owner-layer authorship
respected the right owner repo and did not land meaning in the nearest
convenient surface.
Use `aoa-verification-honesty` to check that closeout, authoring, and merge
claims match what actually happened.
Use `aoa-tool-trajectory-discipline` to check that the route stayed a reviewable
continuity campaign instead of reverting to terminal folklore or manual memory.

## Memory writeback

- the closure or defer decision may survive as a `decision`
- the validation and merge outcome may survive as an `audit_event`
- the residual handoff may survive as a `provenance_thread`
- the `owner_handoff_bundle` and `owner_authorship_bundle` remain route
  artifacts unless a later memo pass promotes them explicitly

The playbook does not move source truth for skills, techniques, playbooks, or
closeout control-plane semantics out of their owner repos.

## Canonical route

1. Start from one reviewed source or reviewed closeout pack and confirm the
   owner boundary plus next-surface truth with `aoa-source-of-truth-check` and
   `aoa-bounded-context-map`.
2. Use `aoa-session-donor-harvest` to keep only bounded reusable candidates from
   the reviewed source and defer weak or supporting seams.
3. Use `aoa-quest-harvest` when the leading candidate already looks owner-shaped
   enough for closed promotion.
4. Run reviewed closeout so the owner follow-through bundle becomes a persistent
   handoff instead of a chat-memory reminder.
5. Use `aoa-approval-gate-check` and `aoa-dry-run-first` to bound the owner
   authoring wave before mutation begins.
6. Use `aoa-change-protocol` to author the owner-layer artifact at the named
   `next_surface`, and use `aoa-adr-write` if the wave introduces a durable
   decision that should remain discoverable.
7. Validate and merge the owner artifact, then either close with a `merge_record`
   or emit one honest `residual_handoff_record` if the next move still remains.
8. If the authored wave itself produces another surviving route, run a new
   reviewed harvest instead of leaving the next authoring move implicit.
