---
id: AOA-P-0034
name: agon-fallback-honor-trial
status: experimental
summary: Coordinates a pre-protocol trial for honest degradation when evidence, retrieval, tools, or context are weakened, without letting smooth language masquerade as completion.
scenario: agon_mechanical_fallback_honor_trial
trigger: degraded_lane_with_risk_of_false_completion
prerequisites:
- degradation_family_named
- weakened_capability_or_missing_evidence_named
- blocked_completion_claim_named
- safe_stop_or_degraded_continuation_boundary_named
participating_agents:
- architect
- reviewer
- evaluator
- memory-keeper
assistant_support:
- monitor
- notary
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
- degradation_honor_note
- blocked_claims_receipt
- degraded_continuation_boundary
- owner_review_ticket
return_posture: artifact_anchor
return_anchor_artifacts:
- degradation_honor_note
- blocked_claims_receipt
- degraded_continuation_boundary
return_reentry_modes:
- previous_phase
- review_gate
- safe_stop
agon_trial_id: agon.trial.mechanical.fallback_honor
agon_wave: VI
agon_pre_protocol: true
live_protocol: false
runtime_effect: none
lawful_moves:
- flag_scope_breach
- request_evidence
- stand_fast
- defer_with_cost
- deny_closure
- request_witness
gate_triggers:
- evidence_floor_collapse
- repeated_failure_without_delta
- novelty_above_service_threshold
terminal_pre_protocol_outcomes:
- trial_passed_pre_protocol
- failed_honorably_pre_protocol
- owner_review_required
- safe_stop
eval_anchors:
- aoa-stress-recovery-window
- aoa-repair-boundedness
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
# agon-fallback-honor-trial

## Intent

Make degraded operation legible, bounded, and honorable instead of allowing fallback prose to impersonate success.

This is a Wave VI pre-protocol mechanical trial. It choreographs a repeatable test and prepares owner-review artifacts. It does not open an arena session and does not issue verdicts.

## Trigger boundary

Use this playbook when `degraded_lane_with_risk_of_false_completion` appears and the route needs a recurring trial shape instead of ad hoc narration.

Do not use this playbook when:

- the route needs a live arena session;
- the route needs a verdict;
- the route needs durable scar storage;
- the route needs retention scheduling;
- the route is really one bounded skill workflow;
- an assistant is trying to become a hidden contestant.

## Prerequisites

- `degradation_family_named`
- `weakened_capability_or_missing_evidence_named`
- `blocked_completion_claim_named`
- `safe_stop_or_degraded_continuation_boundary_named`

## Participating agents

- `architect`
- `reviewer`
- `evaluator`
- `memory-keeper`

Assistant support may be provided by:

- `monitor`
- `notary`
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

1. Decide whether the route may continue in a weaker mode.
2. Decide which completion claims are now illegal.
3. Decide what evidence would be required to reopen full closure.
4. Decide whether assistant receipt support is enough or agonic review is needed.

## Handoffs

- `monitor assistant -> reviewer when degradation could hide false completion`
- `reviewer -> evaluator when proof posture must distinguish weak continuation from closure`
- `evaluator -> memory-keeper only for bounded lesson candidate after owner review`
- `architect -> steward assistant to preserve blocked actions and budgets`

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

- `degradation family receipt`
- `weakened capability list`
- `blocked completion claims`
- `safe-stop or degraded continuation note`

## Expected artifacts

- `degradation_honor_note`
- `blocked_claims_receipt`
- `degraded_continuation_boundary`
- `owner_review_ticket`

## Eval anchors

- `aoa-stress-recovery-window`
- `aoa-repair-boundedness`

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
- `failed_honorably_pre_protocol`
- `owner_review_required`
- `safe_stop`
