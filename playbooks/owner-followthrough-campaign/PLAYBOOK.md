---
id: AOA-P-0026
name: owner-followthrough-campaign
status: experimental
summary: Carries a reviewed candidate or staged seed through the next honest owner move, including owner-status landing, reanchor, merge, defer, or drop, without confusing tracked status surfaces for final owner truth.
scenario: owner_followthrough_campaign
trigger: reviewed_candidate_or_seed_needing_honest_next_owner_move
prerequisites:
  - reviewed_candidate_identity_named
  - owner_repo_and_owner_shape_named
  - nearest_wrong_target_named
  - route_followthrough_surface_named
  - seed_or_direct_landing_posture_named
  - proof_and_prune_boundary_named_if_needed
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
required_skills:
  - aoa-session-route-forks
  - aoa-session-self-diagnose
  - aoa-session-self-repair
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
  - route_followthrough_decision
  - reviewed_owner_landing_bundle
  - seed_owner_landing_trace
  - proof_packet
  - prune_writeback_note
  - stats_refresh_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - route_followthrough_decision
  - reviewed_owner_landing_bundle
  - seed_owner_landing_trace
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
eval_anchors:
  - aoa-candidate-lineage-integrity
  - aoa-owner-fit-routing-quality
  - aoa-repair-boundedness
memo_recall_modes:
  - episodic
  - lineage
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_capsule_then_expand
memo_checkpoint_posture: not_needed
memo_source_route_policy: required
memo_contract_refs:
  - examples/recall_contract.router.lineage.json
  - examples/checkpoint_to_memory_contract.example.json
  - examples/provenance_thread.example.json
memo_writeback_targets:
  - decision
  - audit_event
  - provenance_thread
---

# owner-followthrough-campaign

## Intent

Use this playbook when the route already has a reviewed `candidate_ref` or a
staged `seed_ref`, and the honest question is no longer whether the candidate
exists but what the next owner move should be.

The route keeps six things explicit:
- which reviewed candidate or staged seed the campaign is carrying
- which owner repo, owner shape, and nearest-wrong target keep the move honest
- whether the next move is direct owner-status landing, seed trace, reanchor,
  proof-first, merge, defer, or drop
- when thin-evidence landing is still useful and when it stops being honest
- when prune should be made visible instead of left implicit
- what anchor survives if the campaign loses owner fit, proof fit, or route legibility

This playbook is narrower than `AOA-P-0025` because it starts after candidate
identity exists and does not own checkpoint carry, reviewed harvest, bounded
writeback, or stats refresh as a recurring cycle.
It is narrower than `AOA-P-0021` because the main route is not broader rollout
and post-landing hardening.
It is distinct from `AOA-P-0023` because the route anchor is not a reviewed
closeout handoff but the already-named candidate or staged seed itself.

## Trigger boundary

Use this playbook when:
- a reviewed candidate or staged seed already exists and the main question is
  the next honest owner move
- the route may legitimately end in owner-status landing, reanchor, merge,
  defer, or drop
- seed staging may help but should not be narrated as completion
- the scenario is bigger than one ordinary repo edit but smaller than the full
  recurring `session-growth-cycle`

Do not use this playbook when:
- the route still needs checkpoint carry, reviewed harvest, proof, bounded
  writeback, and stats refresh as one recurring cycle
- the real work is owner-first rollout and post-landing hardening across
  neighboring repos
- the route anchor is still a reviewed closeout continuity handoff rather than
  the candidate or seed itself
- the candidate is too weak for any honest next owner move and should return to
  diagnosis, repair, or reviewed harvest instead

## Prerequisites

- the reviewed `candidate_ref` or staged `seed_ref` is named before mutation begins
- the owner repo, owner shape, and nearest-wrong target are explicit before
  owner follow-through starts
- the route-followthrough surface is named before branch selection begins
- the route can say whether direct landing, seed staging, prove-first,
  reanchor, merge, defer, or drop is the current honest branch
- proof and prune boundaries are named before they are cited as reasons to stop
  or continue
- the route can say what artifact anchors return if owner fit or evidence fit is lost

## Participating agents

- `architect` maps the candidate or seed to its owner boundary, nearest-wrong
  target, and stop conditions before mutation begins
- `coder` applies the smallest honest owner follow-through move once the branch
  decision is explicit
- `reviewer` checks that owner-status landing, seed staging, and prune stay
  weaker than final owner truth
- `evaluator` checks that proof-first, merge, defer, or drop claims match the
  actual evidence posture
- `memory-keeper` preserves only the surviving decision or prune trail without
  inventing new lineage identities

## Required skills

- `aoa-session-route-forks`
- `aoa-session-self-diagnose`
- `aoa-session-self-repair`
- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`

## Decision points

1. Decide whether the next honest move is direct owner-status landing, seed
   staging, proof-first, reanchor, merge, defer, or drop.
2. Decide whether seed staging adds real owner legibility or only delays honest
   landing.
3. Decide whether a thin-evidence owner-status landing is still useful or
   whether the route should stay provisional.
4. Decide whether diagnosis or repair is needed before another owner move is honest.
5. Decide whether prune should happen now and be made explicit.
6. Decide whether proof narrows the route or widens it beyond this campaign.
7. Decide whether the route closes with landing, reanchor, merge, defer, or drop,
   or leaves one bounded residual handoff.

## Handoffs

- `architect -> coder` after the candidate or seed, owner boundary, and branch
  options are explicit
- `coder -> reviewer` after the current owner follow-through artifact exists,
  whether that is `route_followthrough_decision`,
  `reviewed_owner_landing_bundle`, or `seed_owner_landing_trace`
- `reviewer -> evaluator` after landing, proof, merge, defer, or prune posture
  is explicit enough to support proceed or stop
- `reviewer or evaluator -> architect` when owner fit, branch choice, or prune
  honesty drifts enough that the route must return to the last valid anchor
- `evaluator -> memory-keeper` only when one bounded decision or prune trail
  should survive as subordinate writeback

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- owner boundary becomes unclear enough that convenience landing would replace
  honest owner fit
- seed staging starts masquerading as completion
- drop or defer is being claimed without an explicit reason
- proof widens beyond one bounded packet
- the route silently widens into full rollout/hardening or the full
  `session-growth-cycle`

If owner fit, branch clarity, or prune honesty is lost, return to the last
valid `route_followthrough_decision`, `reviewed_owner_landing_bundle`, or
`seed_owner_landing_trace` anchor before further mutation.
If no honest anchor remains, stop and defer rather than narrate movement by inertia.

## Expected evidence posture

The route should finish with visible evidence for:
- which reviewed candidate or staged seed the campaign carried
- which owner repo and nearest-wrong target kept the route honest
- why the branch became direct landing, seed stage, reanchor, merge, defer, or drop
- whether proof narrowed the move or blocked it
- whether prune became explicit and why
- what residual handoff, if any, still survives the current wave

## Expected artifacts

- `route_followthrough_decision`
- `reviewed_owner_landing_bundle`
- `seed_owner_landing_trace`
- `proof_packet`
- `prune_writeback_note`
- `stats_refresh_record`

## Eval anchors

- `aoa-candidate-lineage-integrity`
- `aoa-owner-fit-routing-quality`
- `aoa-repair-boundedness`

Use `aoa-candidate-lineage-integrity` when the route needs to prove that the
candidate or seed still belongs to one honest lineage chain.
Use `aoa-owner-fit-routing-quality` when the route needs to prove that the
current owner move really fits the named owner repo and nearest-wrong target.
Use `aoa-repair-boundedness` when diagnosis or repair becomes the active branch
before another owner move is honest.
All three eval anchors are still draft and review-only surfaces, so they keep
claim limits visible and do not turn owner follow-through into proof by
association.

## Memory writeback

- the surviving branch choice may persist as a `decision`
- one explicit prune, merge, or defer trail may persist as an `audit_event`
- one bounded lineage-aware residual handoff may persist as a `provenance_thread`
- `route_followthrough_decision`, `reviewed_owner_landing_bundle`,
  `seed_owner_landing_trace`, and `proof_packet` remain route artifacts or cited
  evidence rather than memo kinds

This playbook does not mint lineage identities and does not move owner truth,
proof truth, or memo truth into the playbook layer.

## Canonical route

1. Start from the reviewed candidate or staged seed and confirm the owner repo,
   owner shape, and nearest-wrong target with `aoa-source-of-truth-check` and
   `aoa-bounded-context-map`.
2. Use `aoa-session-route-forks` to choose the next honest owner move instead
   of letting follow-through drift by convenience.
3. If owner fit or evidence fit is weak, use `aoa-session-self-diagnose` and
   `aoa-session-self-repair` to reduce ambiguity before another owner move.
4. Use `aoa-approval-gate-check` and `aoa-dry-run-first` before any seed or
   owner-layer mutation so the campaign stays reviewable.
5. Land direct owner-status surfaces through `aoa-change-protocol` and tighten
   the touched interface with `aoa-contract-test` when the owner move is now honest.
6. Emit `seed_owner_landing_trace` only when seed staging really clarifies the
   route; otherwise keep the route smaller.
7. If proof is required, keep it bounded and subordinate to the current owner
   move rather than letting proof become a new sovereign route.
8. Close with one explicit landing, reanchor, merge, defer, or drop outcome,
   and preserve only the smallest honest residual handoff.
