---
id: AOA-P-0041
name: agon-campaign-bifurcation-survival
status: experimental
summary: Repeated branch tests after honest split rather than forced agreement.
scenario: agon_campaign_bifurcation_survival
trigger: reviewed_wave16_campaign_candidate
prerequisites:
  - wave16_campaign_candidate_named
  - allowed_trial_sources_named
  - owner_review_scope_named
  - candidate_only_stop_lines_accepted
participating_agents:
  - architect
  - coder
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - change-protocol
  - boundary-checks
  - evaluation
  - memory-curation
  - review
required_skills:
  - aoa-source-of-truth-check
  - aoa-bounded-context-map
  - aoa-approval-gate-check
  - aoa-dry-run-first
  - aoa-change-protocol
  - aoa-contract-test
evaluation_posture: strict
memory_posture: bounded_chronicle_candidate_only
fallback_mode: review_required
expected_artifacts:
  - campaign_episode_candidate
  - lineage_episode_candidate
  - campaign_handoff_record
eval_anchors:
  - aoa-approval-boundary-adherence
  - aoa-scope-drift-detection
  - aoa-verification-honesty
return_posture: artifact_anchor
return_anchor_artifacts:
  - campaign_episode_candidate
  - lineage_episode_candidate
  - campaign_handoff_record
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
memo_recall_modes:
  - episodic
  - semantic
  - lineage
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_capsule_then_expand
memo_checkpoint_posture: preferred
memo_source_route_policy: required
agon_pre_protocol: true
live_protocol: false
runtime_effect: none
---

# agon-campaign-bifurcation-survival

## Intent

Repeated branch tests after honest split rather than forced agreement. The route keeps the campaign as reviewed choreography only: it can collect candidate episodes, lineage hints, and owner handoff records, but it cannot open a live arena or decide canon.

## Trigger boundary

Use this playbook when repeated Agon trial material needs one named campaign frame before owner review.

Do not use this playbook to grant verdict authority, write scars, mutate rank or trust, promote to KAG or Tree of Sophia, or let a school, lineage, or campaign become authority by narration.

## Prerequisites

- `wave16_campaign_candidate_named`
- `allowed_trial_sources_named`
- `owner_review_scope_named`
- `candidate_only_stop_lines_accepted`
- allowed source surfaces are named before the campaign starts
- `Wave XIII mechanical trials` stays evidence input, not live protocol authority
- `Wave XV epistemic Agon` stays evidence input, not live protocol authority

## Participating agents

- `architect` keeps the campaign boundary, owner handoff path, and source-of-truth route explicit
- `coder` applies only bounded documentation, registry, or validation updates requested by the campaign route
- `reviewer` checks that candidate choreography does not become verdict, scar, rank, KAG, or ToS authority
- `evaluator` reviews evidence shape and eval anchors without issuing a live verdict
- `memory-keeper` preserves candidate chronicle and lineage references without canonizing them

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`

## Decision points

1. Decide whether the repeated material is strong enough to name a campaign candidate.
2. Decide which owner surfaces must review the campaign before any follow-through.
3. Decide which trial episodes are allowed sources and which must stay out of scope.
4. Decide whether lineage hints survive as candidates or must be dropped as unsupported.
5. Decide whether the campaign can close as a candidate packet or must hand off to a later owner route.

## Handoffs

- `architect -> reviewer` after campaign scope, source inputs, and stop-lines are explicit
- `reviewer -> evaluator` after the candidate evidence packet is stable enough for review-only checks
- `evaluator -> memory-keeper` after the route can name what should be preserved as candidate chronicle
- `memory-keeper -> architect` only when owner follow-through remains unresolved and needs a new bounded route

## Fallback and rollback posture

Fallback mode is `review_required`. Stop if campaign language starts acting like live arena state, if a lineage hint is treated as canon, if school affiliation is used as authority, or if assistant posture drifts toward contestant rights. Return to the last valid source packet and keep unsupported fragments out of the campaign.

## Expected evidence posture

Evidence must stay candidate-only and source-linked. The campaign should leave enough reviewable material to explain source inputs, owner boundaries, stop-line adherence, surviving lineage hints, dropped claims, and remaining handoff needs.

## Expected artifacts

- `campaign_episode_candidate`
- `lineage_episode_candidate`
- `campaign_handoff_record`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-scope-drift-detection`
- `aoa-verification-honesty`

These anchors review boundary adherence, scope drift, and verification honesty. They do not issue live verdicts and do not promote a campaign, school, or lineage into canon.

## Memory writeback

`campaign_episode_candidate` and `lineage_episode_candidate` may be preserved as candidate chronicle references. `campaign_handoff_record` may preserve owner follow-through needs. Memory writeback must not create durable scars, retention schedules, rank mutations, KAG promotion, or Tree of Sophia branches.

## Canonical route

1. Name the campaign candidate and confirm the allowed source surfaces.
2. Reconfirm the Wave XVI stop-lines before any mutation or generated-surface update.
3. Gather candidate episodes and owner handoff refs without opening a live arena.
4. Apply review-only eval anchors and record what survives, what drops, and what needs owner follow-through.
5. Preserve only candidate chronicle and handoff artifacts, then close or hand off through a later bounded route.

Stop-lines carried by this campaign:

- `no_live_verdict_authority`
- `no_durable_scar_write`
- `no_retention_execution`
- `no_rank_or_trust_mutation`
- `no_tree_of_sophia_promotion`
- `no_kag_promotion`
- `no_hidden_scheduler_action`
- `no_assistant_contestant_drift`
- `no_auto_doctrine_rewrite`
- `no_school_as_authority`
- `no_lineage_as_canon`
- `no_campaign_as_live_arena`
- `no_center_takeover_of_owner_truth`
