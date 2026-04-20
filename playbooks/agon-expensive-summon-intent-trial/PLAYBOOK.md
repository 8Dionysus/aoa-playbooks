---
id: AOA-P-0039
name: agon-expensive-summon-intent-trial
status: experimental
summary: Coordinates a pre-protocol trial for reviewing summon intent as a costly, visible request rather than a panic button or hidden orchestration shortcut.
scenario: agon_mechanical_expensive_summon_intent_trial
trigger: summon_intent_requires_review_before_any_future_summon_authority_exists
prerequisites:
- summon_intent_named
- reason_local_form_is_insufficient_named
- requested_summon_class_named
- cost_or_budget_boundary_named
- forbidden_hidden_or_runtime_summon_named
participating_agents:
- architect
- reviewer
- evaluator
- memory-keeper
assistant_support:
- steward
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
- summon_intent_receipt
- summon_cost_note
- local_insufficiency_note
- owner_review_ticket
return_posture: artifact_anchor
return_anchor_artifacts:
- summon_intent_receipt
- summon_cost_note
- local_insufficiency_note
return_reentry_modes:
- previous_phase
- review_gate
- safe_stop
agon_trial_id: agon.trial.mechanical.expensive_summon_intent
agon_wave: VI
agon_pre_protocol: true
live_protocol: false
runtime_effect: none
lawful_moves:
- request_summon_intent
- request_witness
- challenge_claim
- request_evidence
- defer_with_cost
- flag_scope_breach
gate_triggers:
- summon_intent_requires_review
- repeated_failure_without_delta
- novelty_above_service_threshold
terminal_pre_protocol_outcomes:
- summon_intent_denied_pre_protocol
- summon_intent_deferred_with_cost
- owner_review_required
- safe_stop
eval_anchors:
- aoa-summon-intent-cost
- aoa-evidence-before-summon
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
# agon-expensive-summon-intent-trial

## Intent

Force every summon-shaped desire to name its purpose, cost, limits, and owner review before summon becomes arena authority.

This is a Wave VI pre-protocol mechanical trial. It choreographs a repeatable test and prepares owner-review artifacts. It does not open an arena session and does not issue verdicts.

## Trigger boundary

Use this playbook when `summon_intent_requires_review_before_any_future_summon_authority_exists` appears and the route needs a recurring trial shape instead of ad hoc narration.

Do not use this playbook when:

- the route needs a live arena session;
- the route needs a verdict;
- the route needs durable scar storage;
- the route needs retention scheduling;
- the route is really one bounded skill workflow;
- an assistant is trying to become a hidden contestant.

## Prerequisites

- `summon_intent_named`
- `reason_local_form_is_insufficient_named`
- `requested_summon_class_named`
- `cost_or_budget_boundary_named`
- `forbidden_hidden_or_runtime_summon_named`

## Participating agents

- `architect`
- `reviewer`
- `evaluator`
- `memory-keeper`

Assistant support may be provided by:

- `steward`
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

1. Decide whether the request is utility, adversarial, perspective, witness, or not yet legal.
2. Decide whether local evidence or skill work should happen before summon intent review.
3. Decide whether the request should be denied, deferred, or handed to owner review.
4. Decide what assistant support may package without initiating summon.

## Handoffs

- `steward assistant -> reviewer with budget and cost receipt`
- `reviewer -> evaluator when summon intent could mask weak evidence`
- `evaluator -> architect when summon classes or boundaries need recharter`
- `reviewer/evaluator -> memory-keeper only for bounded summon-intent audit candidate`

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

- `summon intent receipt`
- `local insufficiency claim`
- `requested summon class`
- `cost boundary`
- `forbidden hidden summon acknowledgment`

## Expected artifacts

- `summon_intent_receipt`
- `summon_cost_note`
- `local_insufficiency_note`
- `owner_review_ticket`

## Eval anchors

- `aoa-summon-intent-cost`
- `aoa-evidence-before-summon`

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

- `summon_intent_denied_pre_protocol`
- `summon_intent_deferred_with_cost`
- `owner_review_required`
- `safe_stop`
