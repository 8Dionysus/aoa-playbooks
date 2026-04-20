---
id: AOA-P-0036
name: agon-costly-closure-trial
status: experimental
summary: Coordinates a pre-protocol closure review trial that treats finalization as earned jurisdiction, not a default exit.
scenario: agon_mechanical_costly_closure_trial
trigger: closure_requested_with_unproven_jurisdiction_or_missing_evidence
prerequisites:
- closure_request_named
- claimed_closure_basis_named
- evidence_floor_named
- trace_and_contradiction_status_named
- closer_jurisdiction_absent_or_unearned_named
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
- closure_review_note
- closure_denial_receipt
- evidence_floor_gap_note
- owner_review_ticket
return_posture: artifact_anchor
return_anchor_artifacts:
- closure_review_note
- closure_denial_receipt
- evidence_floor_gap_note
return_reentry_modes:
- previous_phase
- review_gate
- safe_stop
agon_trial_id: agon.trial.mechanical.costly_closure
agon_wave: VI
agon_pre_protocol: true
live_protocol: false
runtime_effect: none
lawful_moves:
- request_closure_review
- deny_closure
- probe_trace
- request_evidence
- mark_contradiction
- defer_with_cost
gate_triggers:
- contested_closure
- broken_trace_or_trace_gap
- open_material_contradiction
- evidence_floor_collapse
terminal_pre_protocol_outcomes:
- closure_denied_pre_protocol
- deferred_with_cost
- owner_review_required
- safe_stop
eval_anchors:
- aoa-closure-discipline
- aoa-witness-trace-integrity
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
# agon-costly-closure-trial

## Intent

Make closure expensive enough that the system cannot end a route by smoothness, fatigue, or authority drift.

This is a Wave VI pre-protocol mechanical trial. It choreographs a repeatable test and prepares owner-review artifacts. It does not open an arena session and does not issue verdicts.

## Trigger boundary

Use this playbook when `closure_requested_with_unproven_jurisdiction_or_missing_evidence` appears and the route needs a recurring trial shape instead of ad hoc narration.

Do not use this playbook when:

- the route needs a live arena session;
- the route needs a verdict;
- the route needs durable scar storage;
- the route needs retention scheduling;
- the route is really one bounded skill workflow;
- an assistant is trying to become a hidden contestant.

## Prerequisites

- `closure_request_named`
- `claimed_closure_basis_named`
- `evidence_floor_named`
- `trace_and_contradiction_status_named`
- `closer_jurisdiction_absent_or_unearned_named`

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

1. Decide whether closure review is legal before a future arena protocol exists.
2. Decide which missing evidence or open contradiction blocks closure.
3. Decide whether the outcome is closure denied, defer-with-cost, or owner review.
4. Decide whether a future closer jurisdiction candidate should remain absent.

## Handoffs

- `steward assistant -> reviewer with closure request receipt`
- `reviewer -> evaluator for closure legality review`
- `evaluator -> architect when closure policy boundaries need recharter`
- `reviewer/evaluator -> memory-keeper for bounded closure denial chronicle candidate only`

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

- `closure request receipt`
- `evidence floor note`
- `trace status note`
- `contradiction status note`
- `closure denial or deferred posture`

## Expected artifacts

- `closure_review_note`
- `closure_denial_receipt`
- `evidence_floor_gap_note`
- `owner_review_ticket`

## Eval anchors

- `aoa-closure-discipline`
- `aoa-witness-trace-integrity`

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

- `closure_denied_pre_protocol`
- `deferred_with_cost`
- `owner_review_required`
- `safe_stop`
