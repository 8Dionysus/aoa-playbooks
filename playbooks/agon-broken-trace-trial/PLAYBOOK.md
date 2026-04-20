---
id: AOA-P-0033
name: agon-broken-trace-trial
status: experimental
summary: Coordinates a pre-protocol mechanical trial for detecting trace gaps, refusing false closure, and preserving owner review without creating arena verdict authority.
scenario: agon_mechanical_broken_trace_trial
trigger: broken_trace_or_trace_gap_with_closure_pressure
prerequisites:
- one_candidate_trace_claim_named
- one_missing_or_disputed_trace_segment_named
- closure_pressure_named
- witness_or_receipt_surface_available
- owner_review_boundary_named
participating_agents:
- architect
- reviewer
- evaluator
- memory-keeper
assistant_support:
- notary
- monitor
- steward
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
- trace_gap_note
- closure_denial_note
- witness_request_candidate
- owner_review_ticket
return_posture: artifact_anchor
return_anchor_artifacts:
- trace_gap_note
- closure_denial_note
- witness_request_candidate
return_reentry_modes:
- previous_phase
- review_gate
- safe_stop
agon_trial_id: agon.trial.mechanical.broken_trace
agon_wave: VI
agon_pre_protocol: true
live_protocol: false
runtime_effect: none
lawful_moves:
- probe_trace
- deny_trace_closure
- request_evidence
- request_witness
- deny_closure
- defer_with_cost
gate_triggers:
- broken_trace_or_trace_gap
- contested_closure
- evidence_floor_collapse
terminal_pre_protocol_outcomes:
- trial_passed_pre_protocol
- trial_deferred_with_cost
- owner_review_required
- quarantine_hint
eval_anchors:
- aoa-witness-trace-integrity
- aoa-closure-discipline
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
# agon-broken-trace-trial

## Intent

Force the route to prove trace continuity or stop honestly before closure language hardens into a false win.

This is a Wave VI pre-protocol mechanical trial. It choreographs a repeatable test and prepares owner-review artifacts. It does not open an arena session and does not issue verdicts.

## Trigger boundary

Use this playbook when `broken_trace_or_trace_gap_with_closure_pressure` appears and the route needs a recurring trial shape instead of ad hoc narration.

Do not use this playbook when:

- the route needs a live arena session;
- the route needs a verdict;
- the route needs durable scar storage;
- the route needs retention scheduling;
- the route is really one bounded skill workflow;
- an assistant is trying to become a hidden contestant.

## Prerequisites

- `one_candidate_trace_claim_named`
- `one_missing_or_disputed_trace_segment_named`
- `closure_pressure_named`
- `witness_or_receipt_surface_available`
- `owner_review_boundary_named`

## Participating agents

- `architect`
- `reviewer`
- `evaluator`
- `memory-keeper`

Assistant support may be provided by:

- `notary`
- `monitor`
- `steward`

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

1. Decide whether the trace claim can be probed without inventing runtime state.
2. Decide whether the disputed segment blocks closure or only narrows confidence.
3. Decide whether a witness request is required before any continuation.
4. Decide whether the route must end as defer_with_cost or owner_review_required.

## Handoffs

- `architect -> reviewer after the disputed trace segment is named`
- `reviewer -> evaluator when trace adequacy needs proof-facing review`
- `reviewer/evaluator -> memory-keeper only for a bounded chronicle candidate, not a scar write`
- `any actor -> steward assistant for receipt packaging only`

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

- `named trace claim`
- `named gap or continuity dispute`
- `closure pressure receipt`
- `witness request or reason it is not yet legal`
- `explicit stop or defer posture`

## Expected artifacts

- `trace_gap_note`
- `closure_denial_note`
- `witness_request_candidate`
- `owner_review_ticket`

## Eval anchors

- `aoa-witness-trace-integrity`
- `aoa-closure-discipline`

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

- `trial_passed_pre_protocol`
- `trial_deferred_with_cost`
- `owner_review_required`
- `quarantine_hint`
