---
id: AOA-P-0038
name: agon-prediction-trial
status: experimental
summary: Coordinates a pre-protocol trial for making an actor state its model of another actor before any future arena reveal can reward or break that prediction.
scenario: agon_mechanical_prediction_trial
trigger: model_divergence_or_future_contestant_readiness_needs_prediction_discipline
prerequisites:
- actor_subjectivity_surface_named
- other_actor_or_role_named
- prediction_claim_named
- evidence_or_uncertainty_floor_named
- revision_condition_named
participating_agents:
- architect
- reviewer
- evaluator
- memory-keeper
assistant_support:
- notary
- monitor
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
evaluation_posture: strict_pre_protocol_review
memory_posture: bounded_chronicle_candidate_only
fallback_mode: review_required
expected_artifacts:
- prediction_rehearsal_receipt
- model_divergence_note
- revision_condition_note
- future_commit_candidate
return_posture: artifact_anchor
return_anchor_artifacts:
- prediction_rehearsal_receipt
- model_divergence_note
- revision_condition_note
return_reentry_modes:
- previous_phase
- review_gate
- safe_stop
agon_trial_id: agon.trial.mechanical.prediction
agon_wave: VI
agon_pre_protocol: true
live_protocol: false
runtime_effect: none
lawful_moves:
- assert_position
- challenge_claim
- request_evidence
- stand_fast
- revise_position
- defer_with_cost
gate_triggers:
- model_divergence_above_threshold
- repeated_failure_without_delta
- canonical_risk
terminal_pre_protocol_outcomes:
- prediction_rehearsed
- model_divergence_named
- owner_review_required
- deferred_with_cost
eval_anchors:
- aoa-prediction-boundedness
- aoa-model-divergence-discipline
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
# agon-prediction-trial

## Intent

Prepare future sealed-commit discipline by making model-of-other claims visible before a protocol session exists.

This is a Wave VI pre-protocol mechanical trial. It choreographs a repeatable test and prepares owner-review artifacts. It does not open an arena session and does not issue verdicts.

## Trigger boundary

Use this playbook when `model_divergence_or_future_contestant_readiness_needs_prediction_discipline` appears and the route needs a recurring trial shape instead of ad hoc narration.

Do not use this playbook when:

- the route needs a live arena session;
- the route needs a verdict;
- the route needs durable scar storage;
- the route needs retention scheduling;
- the route is really one bounded skill workflow;
- an assistant is trying to become a hidden contestant.

## Prerequisites

- `actor_subjectivity_surface_named`
- `other_actor_or_role_named`
- `prediction_claim_named`
- `evidence_or_uncertainty_floor_named`
- `revision_condition_named`

## Participating agents

- `architect`
- `reviewer`
- `evaluator`
- `memory-keeper`

Assistant support may be provided by:

- `notary`
- `monitor`

Assistants may package receipts, preserve boundaries, and hand off. They may not claim contestant, judge, closer, summon initiator, scar writer, rank mutator, or ToS promoter authority.

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`

These skill references are choreography hints. Skill truth remains in `aoa-skills`.

## Decision points

1. Decide whether the prediction is bounded enough to record as pre-protocol evidence.
2. Decide whether the prediction exposes model divergence or only missing context.
3. Decide whether revise_position is warranted without future sealed commit machinery.
4. Decide whether the result should become an owner review note or remain a rehearsal receipt.

## Handoffs

- `architect -> reviewer after prediction claim and boundary are explicit`
- `reviewer -> evaluator when the prediction affects future contestant readiness`
- `notary assistant -> memory-keeper for receipt packaging only`
- `memory-keeper preserves only bounded rehearsal context, not durable scar`

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or safe-stop when:

- required evidence is absent;
- a lawful move is being used as runtime execution;
- the playbook starts acting like eval or arena protocol;
- an assistant crosses the service boundary;
- closure language appears before trace, contradiction, and evidence posture are honest.

## Expected evidence posture

The route should finish with visible evidence for:

- `actor subjectivity surface ref`
- `target actor or role`
- `prediction claim`
- `uncertainty floor`
- `revision condition`

## Expected artifacts

- `prediction_rehearsal_receipt`
- `model_divergence_note`
- `revision_condition_note`
- `future_commit_candidate`

## Eval anchors

- `aoa-prediction-boundedness`
- `aoa-model-divergence-discipline`

These are future eval-owner requests. They are not verdicts.

## Memory writeback

Allowed memo targets are:

- `decision`
- `audit_event`
- `provenance_thread`

These are chronicle candidates only. They are not durable scars and do not schedule retention.

## Canonical route

1. Name the trigger and the owner boundary.
2. Confirm the required actor and assistant roles.
3. Name the relevant lawful moves without executing an arena session.
4. Gather expected evidence.
5. Choose one terminal pre-protocol outcome.
6. Prepare owner-review artifacts.
7. Stop before verdict, scar, retention, rank mutation, or ToS promotion.

## Terminal pre-protocol outcomes

- `prediction_rehearsed`
- `model_divergence_named`
- `owner_review_required`
- `deferred_with_cost`
