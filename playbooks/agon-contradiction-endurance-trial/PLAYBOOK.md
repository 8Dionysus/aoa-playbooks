---
id: AOA-P-0035
name: agon-contradiction-endurance-trial
status: experimental
summary: Coordinates a pre-protocol trial that prevents closure over an open material contradiction and forces localization, deferment, or review.
scenario: agon_mechanical_contradiction_endurance_trial
trigger: open_material_contradiction_with_pressure_to_resolve_by_language
prerequisites:
- two_incompatible_claims_named
- materiality_reason_named
- closure_pressure_or_routing_pressure_named
- localization_candidate_or_missing_context_named
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
- contradiction_marker
- localization_note
- closure_denial_note
- agon_gate_hint_candidate
return_posture: artifact_anchor
return_anchor_artifacts:
- contradiction_marker
- localization_note
- closure_denial_note
return_reentry_modes:
- previous_phase
- review_gate
- safe_stop
agon_trial_id: agon.trial.mechanical.contradiction_endurance
agon_wave: VI
agon_pre_protocol: true
live_protocol: false
runtime_effect: none
lawful_moves:
- mark_contradiction
- localize_contradiction
- challenge_claim
- request_evidence
- deny_closure
- defer_with_cost
gate_triggers:
- open_material_contradiction
- contested_closure
- model_divergence_above_threshold
terminal_pre_protocol_outcomes:
- localized_pre_protocol
- deferred_with_cost
- owner_review_required
- quarantine_hint
eval_anchors:
- aoa-contradiction-localization
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
# agon-contradiction-endurance-trial

## Intent

Make the system endure an unresolved contradiction long enough to name its locus instead of laundering it into consensus.

This is a Wave VI pre-protocol mechanical trial. It choreographs a repeatable test and prepares owner-review artifacts. It does not open an arena session and does not issue verdicts.

## Trigger boundary

Use this playbook when `open_material_contradiction_with_pressure_to_resolve_by_language` appears and the route needs a recurring trial shape instead of ad hoc narration.

Do not use this playbook when:

- the route needs a live arena session;
- the route needs a verdict;
- the route needs durable scar storage;
- the route needs retention scheduling;
- the route is really one bounded skill workflow;
- an assistant is trying to become a hidden contestant.

## Prerequisites

- `two_incompatible_claims_named`
- `materiality_reason_named`
- `closure_pressure_or_routing_pressure_named`
- `localization_candidate_or_missing_context_named`

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

1. Decide whether the contradiction is material or only wording noise.
2. Decide whether it can be localized without arena verdict authority.
3. Decide whether closure must be denied.
4. Decide whether owner review or future arena gate is the honest next hop.

## Handoffs

- `reviewer -> evaluator when materiality must be checked`
- `evaluator -> reviewer when proof posture is too weak for localization`
- `notary assistant -> memory-keeper for contradiction receipt packaging only`
- `architect -> routing owner when the contradiction should become a gate hint`

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

- `two incompatible claims`
- `materiality note`
- `localization attempt or reason absent`
- `closure denial or defer-with-cost posture`

## Expected artifacts

- `contradiction_marker`
- `localization_note`
- `closure_denial_note`
- `agon_gate_hint_candidate`

## Eval anchors

- `aoa-contradiction-localization`
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

- `localized_pre_protocol`
- `deferred_with_cost`
- `owner_review_required`
- `quarantine_hint`
