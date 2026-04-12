---
id: AOA-P-0027
name: reviewed-automation-followthrough
status: experimental
summary: Carries a reviewed automation candidate through one explicit playbook-seed decision, one real-run review gate, and bounded follow-through summaries without granting scheduler authority.
scenario: reviewed_automation_followthrough
trigger: reviewed_route_with_serious_automation_candidate_but_no_scheduler_truth
prerequisites:
  - reviewed_route_or_candidate_named
  - closeout_followthrough_signal_named
  - automation_candidate_packet_named
  - checkpoint_approval_and_rollback_posture_named
  - real_run_review_boundary_named
  - defer_or_stop_line_named
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
required_skills:
  - aoa-automation-opportunity-scan
  - aoa-session-route-forks
  - aoa-session-self-diagnose
  - aoa-session-self-repair
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
  - closeout_followthrough_decision
  - automation_candidate_packet
  - reviewed_automation_route_decision
  - playbook_seed_candidate
  - real_run_review_note
  - followthrough_summary
return_posture: artifact_anchor
return_anchor_artifacts:
  - closeout_followthrough_decision
  - automation_candidate_packet
  - reviewed_automation_route_decision
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
  - lineage
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_capsule_then_expand
memo_checkpoint_posture: not_needed
memo_source_route_policy: required
memo_contract_refs:
  - examples/recall_contract.router.lineage.json
  - examples/checkpoint_to_memory_contract.example.json
  - examples/provenance_thread.example.json
memo_writeback_targets:
  - decision
  - audit_event
  - provenance_thread
---

# reviewed-automation-followthrough

## Intent

Use this playbook when a reviewed route already makes automation a serious
candidate, but the next honest move is still one bounded playbook-seed
decision plus one reviewed real-run gate rather than scheduler truth.

The route keeps six things explicit:
- which reviewed route, closeout signal, or candidate-aware packet started the
  automation question
- which checkpoint, approval, and rollback boundaries still constrain the
  route
- whether the next honest move is a playbook-seed candidate, defer, or safe
  stop
- what real-run review note must exist before any broader automation claim can
  stay honest
- what anchor survives if diagnosis or repair becomes necessary
- what stop line keeps the playbook from smuggling in schedule authority

This playbook is narrower than `AOA-P-0025` because it does not own checkpoint
carry, reviewed harvest, seed staging, owner landing, proof, writeback, or
stats refresh as one recurring cycle.
It is narrower than `AOA-P-0026` because the main question is not any next
owner move but whether reviewed automation follow-through deserves one explicit
playbook home.
It is distinct from `AOA-P-0023` because the continuity handoff already exists
and the live question is now scenario-level automation follow-through rather
than generic owner continuity.

## Trigger boundary

Use this playbook when:
- a reviewed route, closeout signal, or candidate-aware packet already exists
  and automation readiness is a serious candidate
- the next honest move is to decide whether a playbook-seed candidate is
  warranted now, not to grant schedule authority
- checkpoint, approval, rollback, and real-run review posture all need to stay
  explicit in one bounded scenario
- the route needs scenario-level coordination across `aoa-sdk`,
  `aoa-skills`, and `aoa-playbooks` without widening into the full recurring
  session-growth cycle

Do not use this playbook when:
- the route still needs first-pass donor harvest or reviewed closeout
  assembly, which belongs earlier in the line
- the route is already just one direct owner move with no live automation
  question, which belongs in `AOA-P-0026`
- the route already spans recurring seed, owner, proof, writeback, and stats
  work, which belongs in `AOA-P-0025`
- someone is trying to narrate a live schedule, hidden runner, or scheduler
  right instead of a reviewable playbook seed candidate

## Prerequisites

- the reviewed route or candidate-aware packet is named before mutation begins
- the closeout followthrough signal is explicit enough to keep reviewed
  automation follow-through subordinate to owner truth
- the automation candidate packet is explicit enough to show owner target,
  defer line, and rollback posture
- checkpoint, approval, and rollback posture are explicit before any playbook
  seed candidate is written
- the route can say where the first reviewed real-run note would live
- the route can say what condition forces defer or safe stop

## Participating agents

- `architect` maps the reviewed route, automation boundary, and stop line
  before mutation begins
- `coder` applies the smallest honest playbook-layer change after the route
  anchor and approval posture are explicit
- `reviewer` checks that the playbook seed candidate remains weaker than any
  schedule authority, owner truth, or real-run proof
- `evaluator` checks that diagnosis, repair, defer, or proceed claims match
  the actual evidence posture
- `memory-keeper` preserves only bounded decision or audit context without
  turning the playbook into a run ledger

## Required skills

- `aoa-automation-opportunity-scan`
- `aoa-session-route-forks`
- `aoa-session-self-diagnose`
- `aoa-session-self-repair`
- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`

## Decision points

1. Decide whether automation is still only a hint or already a serious
   reviewed candidate.
2. Decide whether the next honest move is a playbook-seed candidate, a defer,
   or a safe stop.
3. Decide whether diagnosis or repair is needed before any playbook-seed
   candidate is honest.
4. Decide what checkpoint, approval, rollback, and real-run review posture
   must remain explicit in the route.
5. Decide whether the current route still fits `AOA-P-0027` or has widened
   into `AOA-P-0025`.
6. Decide which artifact anchor survives if scheduler drift, owner drift, or
   proof drift appears.

## Handoffs

- `architect -> coder` after the reviewed route anchor, automation boundary,
  and stop line are explicit
- `coder -> reviewer` after the current playbook-layer artifacts exist,
  whether that is a route decision, playbook-seed candidate, or explicit defer
- `reviewer -> evaluator` after checkpoint, approval, rollback, and real-run
  review posture are explicit enough to support proceed, defer, or stop
- `reviewer or evaluator -> architect` when diagnosis, repair, or scheduler
  drift forces return to the last valid artifact anchor
- `evaluator -> memory-keeper` only when one bounded decision or audit trail
  should survive as subordinate writeback

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the route still needs first-pass donor harvest or reviewed closeout assembly
- a playbook-seed candidate starts masquerading as a live schedule
- rollback posture is missing or too weak to keep the route bounded
- the real-run review boundary is missing but the route is already claiming
  more than candidacy
- the route widens into the full recurring `AOA-P-0025 session-growth-cycle`

If automation fit, rollback posture, or stop-line clarity is lost, return to
the last valid `closeout_followthrough_decision`,
`automation_candidate_packet`, or `reviewed_automation_route_decision` anchor
before further mutation.
If no honest anchor remains, stop and defer rather than narrate schedule
readiness by inertia.

## Expected evidence posture

The route should finish with visible evidence for:
- which reviewed route or candidate-aware packet entered the playbook
- why automation was treated as serious, deferred, or stopped
- what checkpoint, approval, and rollback posture remained explicit
- whether the route wrote one bounded playbook-seed candidate or refused to
  do so
- what real-run review note is still required before any broader automation
  claim can survive
- what residual handoff, if any, still survives after the current pass

## Expected artifacts

- `closeout_followthrough_decision`
- `automation_candidate_packet`
- `reviewed_automation_route_decision`
- `playbook_seed_candidate`
- `real_run_review_note`
- `followthrough_summary`

## Eval anchors

- `aoa-candidate-lineage-integrity`
- `aoa-owner-fit-routing-quality`
- `aoa-repair-boundedness`

Use `aoa-candidate-lineage-integrity` when the route needs to prove that the
automation question still belongs to one honest reviewed lineage chain.
Use `aoa-owner-fit-routing-quality` when the route needs to prove that
`aoa-playbooks` really is the best next home for this follow-through move.
Use `aoa-repair-boundedness` when diagnosis or repair becomes the active
branch before any playbook-seed candidate is honest.
All three eval anchors are still draft and review-only surfaces, so they keep
claim limits visible and do not turn reviewed automation follow-through into
proof by association.

## Memory writeback

- the surviving branch choice may persist as a `decision`
- one explicit stop, defer, or rollback trail may persist as an `audit_event`
- one bounded residual handoff may persist as a `provenance_thread`
- `playbook_seed_candidate` and `real_run_review_note` remain route artifacts
  or cited evidence rather than memo kinds

This playbook does not grant scheduler authority and does not move owner truth,
proof truth, or memo truth into the playbook layer.

## Canonical route

1. Start from the reviewed route anchor and confirm the automation boundary,
   owner target, and stop line with `aoa-source-of-truth-check` and
   `aoa-bounded-context-map`.
2. Use `aoa-automation-opportunity-scan` and `aoa-session-route-forks` to
   decide whether a playbook-seed candidate is honest now or should defer.
3. If blockers remain, use `aoa-session-self-diagnose` and
   `aoa-session-self-repair` to keep the route bounded instead of narrating
   readiness.
4. If the route stays bounded and recommendation-only, write one explicit
   `playbook_seed_candidate` and keep its real-run review gate visible.
5. Stop at the first honest closure: bounded candidate, explicit defer, or
   safe stop. Widen into `AOA-P-0025` only when the route genuinely becomes a
   recurring cycle.
