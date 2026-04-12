---
id: AOA-P-0028
name: trusted-rollout-operations
status: experimental
summary: Coordinates a bounded shared-root Codex rollout campaign through trust checks, drift observation, bounded repair, rollback windows, checked-in receipt publication, derived summary refresh, and bounded memo writeback without moving rollout truth out of owner repos.
scenario: trusted_rollout_operations
trigger: trusted_shared_root_codex_rollout_needing_bounded_drift_and_rollback_followthrough
prerequisites:
  - rollout_scope_and_workspace_root_named
  - trust_doctor_and_smoke_posture_named
  - bounded_activation_boundary_named
  - drift_window_and_rollback_posture_named
  - checked_in_receipt_publication_surface_named
  - stats_and_memo_followthrough_surfaces_named
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
  - aoa-source-of-truth-check
  - aoa-bounded-context-map
  - aoa-approval-gate-check
  - aoa-dry-run-first
  - aoa-change-protocol
  - aoa-contract-test
  - aoa-session-self-diagnose
  - aoa-session-self-repair
  - aoa-adr-write
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - rollout_decision
  - doctor_report_ref
  - smoke_report_ref
  - deploy_receipt_ref
  - drift_window_ref
  - rollback_window_ref
  - stats_refresh_ref
  - memo_writeback_ref
return_posture: artifact_anchor
return_anchor_artifacts:
  - rollout_decision
  - deploy_receipt_ref
  - stats_refresh_ref
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
eval_anchors:
  - aoa-diagnosis-cause-discipline
  - aoa-repair-boundedness
  - aoa-stress-recovery-window
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

# trusted-rollout-operations

## Intent

Use this playbook when the route is a real shared-root Codex rollout campaign,
not just one deploy-local receipt or one generic infra mutation, and the honest
work now spans trust, doctor, smoke, drift, bounded repair, rollback,
publication, derived stats, and bounded memo follow-through.

The route keeps nine things explicit:
- which shared-root Codex rollout scope is being activated
- what trust, doctor, and smoke evidence exists before the rollout widens
- what stop-lines still block activation or continued monitoring
- when a drift window is quiet, watch-shaped, material, or rollback-bound
- when bounded repair is honest and when rollback must open
- which checked-in owner repo records become the durable rollout history
- which derived stats may refresh and what they remain subordinate to
- when memo writeback is earned as bounded lesson or recovery context
- what anchor survives if trust, drift, rollback, or publication posture is lost

This playbook is narrower than `AOA-P-0010` because the route is not a generic
cross-repo rollout but one specific shared-root Codex rollout operations cycle.
It is narrower than `AOA-P-0012` because the route is no longer just previewed
infra mutation; it already spans bounded rollout activation, drift observation,
and checked-in follow-through.
It is distinct from `AOA-P-0020` because the route is still a governed rollout
campaign rather than an unplanned incident.
It is distinct from `AOA-P-0025` because the route anchor is rollout,
drift, rollback, and checked-in operational continuity rather than checkpoint
carry, reviewed harvest, seed staging, proof, and recurring growth closure.
The shared-root Codex-plane continuity lane keeps its companion route card in
`docs/CODEX_PLANE_ROLLOUT_CYCLE.md` plus
`examples/codex_plane_rollout_lane.example.json`, but that companion stays
subordinate to this sovereign playbook rather than acting like a second
playbook or hidden runner.
When repeated maintenance needs one grouped cadence layer above checked-in
rollout history, the adjunct lives in
`docs/TRUSTED_ROLLOUT_CAMPAIGN_CADENCE.md`; it stays under this playbook
instead of minting a second sovereign playbook, activation surface, or
scheduler.

## Trigger boundary

Use this playbook when:
- a shared-root Codex rollout campaign is real and bounded
- trust, doctor, smoke, drift, rollback, stats, and memo posture all matter in
  one reviewable route
- checked-in rollout history must survive in an owner repo after the live
  deploy-local step
- the route needs explicit distinction between bounded repair and rollback

Do not use this playbook when:
- the route is only one preview-first infra mutation without rollout follow-through
- the route is already an unplanned incident, which belongs in `AOA-P-0020`
- the route is really a broader recurring session-growth chain, which belongs
  in `AOA-P-0025`
- the route tries to let stats, memo, or sdk status speak stronger than
  checked-in rollout history
- the route would become a hidden scheduler or runtime authority instead of a
  reviewable scenario

## Prerequisites

- the rollout scope and shared-root workspace boundary are named before mutation begins
- trust, doctor, and smoke posture are explicit before activation begins
- the bounded activation boundary is explicit before drift monitoring widens
- drift-window and rollback posture are named before repair or rollback begins
- checked-in receipt publication surfaces are named before follow-through starts
- stats and memo follow-through surfaces are named before derived refresh begins

## Participating agents

- `architect` maps rollout scope, trust boundary, drift window, and rollback
  stop-lines before mutation begins
- `coder` applies only the smallest honest rollout, repair, or rollback move
  once the current boundary is explicit
- `reviewer` checks that checked-in rollout history, derived stats, and memo
  writeback stay in their owner layers
- `evaluator` checks that diagnosis, repair, rollback, and closure claims match
  the evidence posture
- `memory-keeper` preserves bounded lessons and recovery patterns without
  replacing rollout truth or proof

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-session-self-diagnose`
- `aoa-session-self-repair`
- `aoa-adr-write`

## Decision points

1. Decide whether trust, doctor, and smoke posture are strong enough to open a
   bounded rollout campaign now.
2. Decide whether the drift window is still quiet, watch-shaped, material, or
   already rollback-bound.
3. Decide whether one bounded repair is honest or whether rollback must open now.
4. Decide which checked-in rollout records must survive as durable owner history.
5. Decide which derived stats may refresh without overrunning owner truth.
6. Decide whether memo writeback earned a failure lesson, a recovery pattern,
   or no durable writeback at all.
7. Decide whether the route closed as `stabilized`, `rolled_back`, `abandoned`,
   or one review stop requiring return to the last honest anchor.

## Handoffs

- `architect -> coder` after rollout scope, stop-lines, drift boundary, and
  rollback posture are explicit
- `coder -> reviewer` after the current rollout, repair, rollback, or
  publication artifacts exist
- `reviewer -> evaluator` after checked-in history, derived stats, and
  stop-line posture are explicit enough to support proceed, rollback, or stop
- `reviewer or evaluator -> architect` when trust, drift, rollback, or
  publication posture drifts enough that the route must return to the last
  valid rollout anchor
- `evaluator -> memory-keeper` after a bounded lesson or recovery pattern is
  explicit enough to survive as subordinate memo writeback

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- project trust or shared-root boundary posture is ambiguous
- doctor or smoke evidence is weaker than the claimed rollout posture
- startup, hook, MCP, or shared-root loading drift becomes material without
  one honest repair or rollback boundary
- checked-in rollout history is missing or contradictory
- derived summaries start outranking checked-in owner history
- memo writeback starts acting like rollout proof

If trust posture, drift posture, rollback closure, or publication posture is
lost, return to the last valid `rollout_decision`, `deploy_receipt_ref`, or
`stats_refresh_ref` anchor before further mutation.
If no honest anchor remains, stop and defer rather than narrate the campaign as
stable by inertia.

## Expected evidence posture

The route should finish with visible evidence for:
- which shared-root rollout scope and trust boundary were active before apply
- what doctor and smoke signals justified bounded activation or stopped it
- whether the drift window stayed quiet, watch-shaped, material, or rollback-bound
- whether one bounded repair was honest or rollback had to open
- which checked-in rollout campaign and rollback records became durable owner history
- which derived stats and memo surfaces refreshed without outranking owner truth
- what closure class survived after the route ended

## Expected artifacts

- `rollout_decision`
- `doctor_report_ref`
- `smoke_report_ref`
- `deploy_receipt_ref`
- `drift_window_ref`
- `rollback_window_ref`
- `stats_refresh_ref`
- `memo_writeback_ref`

## Eval anchors

- `aoa-diagnosis-cause-discipline`
- `aoa-repair-boundedness`
- `aoa-stress-recovery-window`

Use `aoa-diagnosis-cause-discipline` when the route needs to prove that drift,
doctor, or smoke claims still point to the real cause rather than to a
convenient story.
Use `aoa-repair-boundedness` when one repair branch is being considered and the
route must show why that repair stayed smaller and more honest than either
continued rollout optimism or premature rollback.
Use `aoa-stress-recovery-window` when the route needs to show that activation,
drift, rollback, and recovery timing stayed explicit enough to support the
closure claim.
All three eval anchors remain draft and review-only surfaces, so they help
bound claims without turning the playbook into proof authority.

## Memory writeback

- the surviving rollout branch choice may persist as a `decision`
- one explicit rollback or recovery trail may persist as an `audit_event`
- one bounded rollout provenance chain may persist as a `provenance_thread`
- `rollout_decision`, `deploy_receipt_ref`, `drift_window_ref`,
  `rollback_window_ref`, and `stats_refresh_ref` remain route artifacts or
  cited evidence rather than memo kinds

This playbook does not move rollout truth out of checked-in owner history and
does not let memo writeback overrule trust, receipt, or rollback evidence.

## Canonical route

1. Start from the named shared-root rollout scope and confirm the active owner
   truth surfaces with `aoa-source-of-truth-check` and `aoa-bounded-context-map`.
2. Use `aoa-approval-gate-check` and `aoa-dry-run-first` to keep the route
   bounded before any live rollout activation widens.
3. Apply only the smallest honest rollout move through `aoa-change-protocol`,
   keeping doctor and smoke posture explicit before calling the route healthy.
4. If trust, startup, hooks, or runtime behavior drift, use
   `aoa-session-self-diagnose` and `aoa-session-self-repair` to decide whether
   one bounded repair is honest or whether rollback must open now.
5. Tighten any touched operational seam with `aoa-contract-test` so the route
   leaves behind a smaller verification gap than it found.
6. Publish the durable rollout, drift, and rollback record in the owner repo
   before derived stats or memo writeback try to summarize the route.
7. Refresh bounded stats and memo surfaces only after checked-in rollout
   history exists, and keep both subordinate to owner truth.
8. Close as `stabilized`, `rolled_back`, `abandoned`, or one explicit review
   stop, preserving only the smallest honest anchor for re-entry.
