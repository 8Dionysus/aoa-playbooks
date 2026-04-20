---
id: AOA-P-0037
name: agon-assistant-escalation-trial
status: experimental
summary: Coordinates a pre-protocol trial for service actors that must flag scope breach, preserve receipt clarity, and escalate without becoming hidden contestants.
scenario: agon_mechanical_assistant_escalation_trial
trigger: assistant_scope_breach_or_anti_drift_alarm_needing_agonic_escalation
prerequisites:
- assistant_variant_named
- service_contract_or_scope_boundary_named
- scope_breach_or_anti_drift_alarm_named
- target_agonic_actor_or_owner_review_boundary_named
participating_agents:
- architect
- reviewer
- evaluator
- memory-keeper
assistant_support:
- concierge
- notary
- monitor
- steward
- librarian
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
- assistant_scope_breach_receipt
- agonic_escalation_candidate
- anti_drift_note
- owner_review_ticket
return_posture: artifact_anchor
return_anchor_artifacts:
- assistant_scope_breach_receipt
- agonic_escalation_candidate
- anti_drift_note
return_reentry_modes:
- previous_phase
- review_gate
- safe_stop
agon_trial_id: agon.trial.mechanical.assistant_escalation
agon_wave: VI
agon_pre_protocol: true
live_protocol: false
runtime_effect: none
lawful_moves:
- flag_scope_breach
- escalate_to_agon_gate
- request_witness
- request_evidence
- defer_with_cost
gate_triggers:
- assistant_scope_breach
- assistant_anti_drift_alarm
- actor_kind_mismatch
- novelty_above_service_threshold
terminal_pre_protocol_outcomes:
- service_resolved_with_receipt
- agon_gate_candidate_prepared
- owner_review_required
- safe_stop
eval_anchors:
- aoa-assistant-anti-drift-boundary
- aoa-scope-discipline
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
# agon-assistant-escalation-trial

## Intent

Prove that assistants can serve boundary clarity and escalation while refusing any hidden drift into arena authority.

This is a Wave VI pre-protocol mechanical trial. It choreographs a repeatable test and prepares owner-review artifacts. It does not open an arena session and does not issue verdicts.

## Trigger boundary

Use this playbook when `assistant_scope_breach_or_anti_drift_alarm_needing_agonic_escalation` appears and the route needs a recurring trial shape instead of ad hoc narration.

Do not use this playbook when:

- the route needs a live arena session;
- the route needs a verdict;
- the route needs durable scar storage;
- the route needs retention scheduling;
- the route is really one bounded skill workflow;
- an assistant is trying to become a hidden contestant.

## Prerequisites

- `assistant_variant_named`
- `service_contract_or_scope_boundary_named`
- `scope_breach_or_anti_drift_alarm_named`
- `target_agonic_actor_or_owner_review_boundary_named`

## Participating agents

- `architect`
- `reviewer`
- `evaluator`
- `memory-keeper`

Assistant support may be provided by:

- `concierge`
- `notary`
- `monitor`
- `steward`
- `librarian`

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

1. Decide whether the service actor can resolve the issue inside its contract.
2. Decide whether escalation to an agonic actor is required.
3. Decide which assistant actions are forbidden before handoff.
4. Decide whether the output should be a receipt, gate hint, or owner review ticket.

## Handoffs

- `assistant -> reviewer with receipt, not argument`
- `reviewer -> architect when actor-kind mismatch must be mapped`
- `reviewer -> evaluator when anti-drift boundary needs review`
- `evaluator -> memory-keeper only for bounded audit-event candidate`

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

- `assistant variant identity`
- `service contract boundary`
- `scope breach or anti-drift alarm note`
- `handoff receipt`
- `explicit forbidden actions retained`

## Expected artifacts

- `assistant_scope_breach_receipt`
- `agonic_escalation_candidate`
- `anti_drift_note`
- `owner_review_ticket`

## Eval anchors

- `aoa-assistant-anti-drift-boundary`
- `aoa-scope-discipline`

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

- `service_resolved_with_receipt`
- `agon_gate_candidate_prepared`
- `owner_review_required`
- `safe_stop`
