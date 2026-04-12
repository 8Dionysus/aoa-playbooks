---
id: AOA-P-0025
name: session-growth-cycle
status: experimental
summary: Coordinates the recurring session-growth route from provisional checkpoint carry through reviewed harvest, seed staging, owner landing, proof, bounded writeback, and derived funnel refresh without letting playbook composition outrank owner truth.
scenario: session_growth_cycle
trigger: reviewed_session_route_needing_lineage_bound_growth_follow_through
prerequisites:
  - reviewed_session_artifact_named
  - checkpoint_carry_or_closeout_context_named
  - owner_boundary_and_nearest_wrong_target_named
  - lineage_and_seed_stage_surfaces_named
  - proof_and_writeback_surfaces_named
  - stats_refresh_boundary_named
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
  - aoa-session-donor-harvest
  - aoa-session-self-diagnose
  - aoa-session-self-repair
  - aoa-session-progression-lift
  - aoa-quest-harvest
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
  - checkpoint_carry_bundle
  - reviewed_closeout_context
  - candidate_harvest_packet
  - route_follow_through_decision
  - seed_trace
  - owner_landing_bundle
  - proof_packet
  - writeback_record
  - stats_refresh_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - reviewed_closeout_context
  - candidate_harvest_packet
  - route_follow_through_decision
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
  - semantic
  - lineage
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_capsule_then_expand
memo_checkpoint_posture: not_needed
memo_source_route_policy: required
memo_contract_refs:
  - examples/recall_contract.router.semantic.json
  - examples/recall_contract.router.lineage.json
  - examples/checkpoint_to_memory_contract.example.json
  - examples/provenance_thread.example.json
memo_writeback_targets:
  - audit_event
  - provenance_thread
---

# session-growth-cycle

## Intent

Use this playbook when the honest recurring route is no longer a one-off
landing, continuity handoff, or remediation wave, but a full session-growth
cycle across already-landed lineage seams.

The route keeps nine things explicit:
- which reviewed session artifact and checkpoint carry started the cycle
- where provisional `cluster_ref` carry stops and reviewed `candidate_ref`
  meaning begins
- when the route needs diagnosis, repair, progression, or quest follow-through
  rather than immediate staging
- when a reviewed candidate should stage a `seed_ref` in `Dionysus`
- which owner repo, owner shape, and nearest-wrong target keep landing honest
- what proof bundle is needed before the route can claim more than owner-local
  authorship
- when memory writeback is earned as bounded failure or recovery context
- when derived stats may refresh and what evidence they remain subordinate to
- what anchor the route returns to if lineage, ownership, or proof posture is
  lost

This playbook is wider than `AOA-P-0021` once the route already spans reviewed
harvest, seed staging, owner landing, proof, writeback, and stats refresh.
It is wider than `AOA-P-0023` once the main question is not one persistent
owner follow-through move but the recurring cycle itself.
Use `AOA-P-0027` when the current route is specifically a reviewed automation
follow-through candidate needing one playbook-seed decision and one real-run
gate rather than the full recurring cycle.
It is narrower than generic ecosystem rollout because it only coordinates the
session-growth path that the landed lineage seams already make possible.
The shared-root Codex-plane deployment continuity lane lives in
`docs/CODEX_PLANE_ROLLOUT_CYCLE.md` plus
`examples/codex_plane_rollout_lane.example.json` as a companion route card.
It stays inside `AOA-P-0025` rather than becoming a second playbook or a
hidden rollout runner.

## Trigger boundary

Use this playbook when:
- a reviewed session artifact already exists and the route is to carry it
  through the recurring growth cycle rather than stop at closeout
- checkpoint carry, reviewed harvest, seed staging, owner landing, proof,
  writeback, and stats refresh may all matter in one bounded route
- the main risk is that derived layers will overstate owner truth unless the
  whole cycle stays explicit
- the route needs scenario-level coordination across more than one owner layer

Do not use this playbook when:
- no reviewed session artifact exists yet and the route should stop at
  checkpoint carry or reviewed closeout
- the truthful next move is only one owner-first landing campaign, one
  continuity handoff, or one bounded remediation wave
- the current question is one reviewed automation follow-through candidate and
  one real-run gate rather than the full recurring cycle, which belongs in
  `AOA-P-0027`
- proof, memory, or stats are being asked to invent owner truth that does not
  exist in reviewed owner-local artifacts
- the route would become a hidden runner instead of a reviewable scenario

## Prerequisites

- the reviewed session artifact is named before mutation begins
- checkpoint carry or closeout context is explicit enough to keep provisional
  lineage weaker than reviewed lineage
- the owner boundary and nearest-wrong-target posture are named before owner
  landing starts
- seed-stage and proof surfaces are named before the route widens beyond
  reviewed harvest
- writeback and stats-refresh surfaces are named before derived layers are
  refreshed
- the route can say what condition forces return, defer, or safe stop

## Participating agents

- `architect` maps the reviewed session artifact, lineage axis, owner boundary,
  and stop conditions before mutation begins
- `coder` applies the smallest honest route move after the current stage and
  owner boundary are explicit
- `reviewer` checks that checkpoint carry, reviewed candidate identity, seed
  staging, owner landing, proof, memory, and stats remain in their owning
  layers
- `evaluator` checks that proof, owner evidence, and derived refresh really
  support proceed, defer, or stop
- `memory-keeper` preserves bounded failure and recovery context without
  replacing owner truth, proof truth, or stats truth

## Required skills

- `aoa-checkpoint-closeout-bridge`
- `aoa-session-donor-harvest`
- `aoa-session-self-diagnose`
- `aoa-session-self-repair`
- `aoa-session-progression-lift`
- `aoa-quest-harvest`
- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`

## Decision points

1. Decide whether the reviewed session artifact is strong enough to continue
   past reviewed closeout or should stop there.
2. Decide whether the next honest move is donor harvest, diagnosis, repair,
   progression, quest follow-through, or defer.
3. Decide whether a reviewed candidate should stay candidate-only, stage a
   seed, or land directly in an owner repo.
4. Decide which owner repo, owner shape, and nearest-wrong target keep the
   route honest for the current candidate.
5. Decide whether the route needs proof now, and which proof surface is narrow
   enough to read the current move honestly.
6. Decide whether a failure or recovery pattern is stable enough for bounded
   writeback.
7. Decide whether derived stats can refresh from reviewed receipts without
   outrunning owner truth.
8. Decide whether the route closes as bounded growth follow-through, leaves a
   residual handoff, or returns to the last valid reviewed anchor.

## Handoffs

- `architect -> coder` after the reviewed session artifact, lineage boundary,
  and current owner boundary are explicit
- `coder -> reviewer` after the current stage artifacts exist, whether that is
  harvest, seed trace, owner landing, proof, or bounded refresh
- `reviewer -> evaluator` after owner evidence, proof posture, and derived
  refresh posture are explicit enough to support proceed, defer, or stop
- `reviewer or evaluator -> architect` when lineage order, owner fit, or repair
  boundedness drifts enough that the route must return to the last valid
  reviewed anchor
- `evaluator -> memory-keeper` after a bounded failure or recovery context is
  explicit enough to survive as writeback
- `memory-keeper -> architect` only when the writeback or residual handoff
  proves another governed route still remains

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- checkpoint carry is being treated as reviewed candidate truth
- a `candidate_ref` is missing but the route is trying to stage a seed or land
  an owner object
- owner fit is still ambiguous enough that `aoa-routing` or `aoa-kag` would
  become the convenience first author
- proof, memory, or stats are being asked to outrank reviewed owner evidence
- a repair move widens scope instead of reducing ambiguity
- the route starts acting like a hidden runner instead of a reviewable cycle

If lineage order, owner boundary, or proof posture is lost, return to the last
valid `reviewed_closeout_context`, `candidate_harvest_packet`, or
`route_follow_through_decision` anchor before further mutation.
If no honest reviewed anchor remains, stop and defer rather than narrate the
cycle as healthy by inertia.

## Expected evidence posture

The route should finish with visible evidence for:
- what checkpoint carry entered the route and how it stayed provisional
- what reviewed harvest kept, dropped, or superseded
- what route decision chose diagnosis, repair, progression, quest, seed stage,
  or owner landing next
- what seed trace, owner landing, and proof artifacts actually exist
- what writeback was earned and why it stayed subordinate to owner truth and
  proof
- what stats refresh happened and which reviewed receipts it remained
  downstream of

## Expected artifacts

- `checkpoint_carry_bundle`
- `reviewed_closeout_context`
- `candidate_harvest_packet`
- `route_follow_through_decision`
- `seed_trace`
- `owner_landing_bundle`
- `proof_packet`
- `writeback_record`
- `stats_refresh_record`

## Eval anchors

- `aoa-candidate-lineage-integrity`
- `aoa-owner-fit-routing-quality`
- `aoa-repair-boundedness`

Use `aoa-candidate-lineage-integrity` when the route needs to prove that
checkpoint carry, reviewed candidate, seed trace, and owner artifact still form
one honest bounded chain.
Use `aoa-owner-fit-routing-quality` when the route needs to prove that one
reviewed candidate is landing in the right owner layer with an honest
nearest-wrong target.
Use `aoa-repair-boundedness` when diagnosis or repair becomes the active route
branch and the main question is whether the repair stayed bounded.
All three eval anchors are still draft and review-only surfaces, so they keep
claim limits visible and do not upgrade this route into canonical proof by
association.

## Memory writeback

- `audit_event` is appropriate when the route leaves one reviewed closure,
  defer, or bounded failure record that later sessions should recall without
  replacing owner truth or proof
- `provenance_thread` is appropriate when the route needs one explicit lineage
  trail across reviewed closeout, seed trace, owner landing, proof, and later
  memo-layer follow-through
- `checkpoint_carry_bundle`, `reviewed_closeout_context`,
  `candidate_harvest_packet`, `seed_trace`, `owner_landing_bundle`,
  `proof_packet`, and `stats_refresh_record` remain route artifacts or cited
  evidence rather than memo writeback kinds
- later owner-local memo objects such as `failure_lesson` or
  `recovery_pattern` still belong in `aoa-memo` and remain subordinate to the
  strongest available lineage refs

The playbook does not create a new memory taxonomy and does not move memo,
proof, or stats authority into the playbook layer.

## Canonical route

1. Start from one reviewed session artifact, keep checkpoint carry explicit, and
   use `aoa-checkpoint-closeout-bridge`, `aoa-source-of-truth-check`, and
   `aoa-bounded-context-map` to name the current lineage boundary before
   mutation begins.
2. Use `aoa-session-donor-harvest` to decide whether the route yields a bounded
   reviewed candidate, a dropped branch, or a superseded branch, and do not let
   `candidate_ref` appear before reviewed harvest exists.
3. Decide whether the next honest move is diagnosis, repair, progression, or
   quest follow-through, and use `aoa-session-self-diagnose`,
   `aoa-session-self-repair`, `aoa-session-progression-lift`, or
   `aoa-quest-harvest` only as far as the current reviewed route actually
   requires.
4. Use `aoa-approval-gate-check` and `aoa-dry-run-first` before any seed-stage
   or owner-layer mutation so the route does not widen by convenience.
5. Stage `seed_trace` in `Dionysus` only when the reviewed candidate survives
   and seed staging is the honest next owner move; otherwise keep the route
   smaller.
6. Land the current owner artifact with `aoa-change-protocol` and
   `aoa-contract-test` only in the owner repo that the reviewed route actually
   supports.
7. Run proof only where the route needs it, keep memory writeback subordinate to
   the strongest available lineage refs, and refresh stats only from reviewed
   owner-local receipts.
8. Close with the smallest honest `route_follow_through_decision`; if lineage
   order, owner fit, proof posture, or boundedness is lost, return through
   `previous_phase`, `review_gate`, `rollback_gate`, or `safe_stop` before
   claiming a completed growth cycle.
