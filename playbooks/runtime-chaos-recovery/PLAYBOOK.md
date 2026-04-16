---
id: AOA-P-0032
name: runtime-chaos-recovery
status: experimental
summary: Coordinates one reviewed runtime stress receipt through a bounded degraded lane, explicit re-entry gate, source-first regrounding when derived retrieval fails, proof-facing handoff, and safe stop lines without turning playbooks into runtime repair or verdict authority.
scenario: runtime_chaos_recovery
trigger: reviewed_runtime_stress_receipt_needing_bounded_degraded_lane_and_reentry_gate
prerequisites:
  - owner_local_runtime_receipt_named
  - degraded_continuation_or_hold_boundary_named
  - source_first_regrounding_surface_named_when_derivation_fails
  - reentry_gate_named
  - proof_handoff_boundary_named
  - blocked_widening_or_safe_stop_line_named
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
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - runtime_stress_lane
  - runtime_reentry_gate
  - owner_runtime_receipt
  - runtime_closeout_receipt
  - regrounding_ticket_ref
  - proof_handoff_candidate
return_posture: artifact_anchor
return_anchor_artifacts:
  - runtime_stress_lane
  - runtime_reentry_gate
  - owner_runtime_receipt
return_reentry_modes:
  - previous_phase
  - review_gate
  - safe_stop
eval_anchors:
  - aoa-diagnosis-cause-discipline
  - aoa-repair-boundedness
  - aoa-stress-recovery-window
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

# runtime-chaos-recovery

## Intent

Use this playbook when a reviewed runtime stress receipt already exists, the
next honest move is a bounded degraded lane plus explicit re-entry gate, and
the route must stay source-first instead of inflating playbook prose into
runtime repair authority, KAG health truth, or eval verdict logic.

The route keeps six things explicit:
- which owner-local `owner_runtime_receipt` actually names the runtime stress
  family now
- which `runtime_stress_lane` allows only a weaker reviewed continuation
- which `runtime_reentry_gate` decides `resume_degraded`, `hold`, or
  `retire_route`
- which `regrounding_ticket_ref` keeps derived-surface recovery source-first
  when retrieval continuity is unavailable
- which `proof_handoff_candidate` may later enter `aoa-evals` without moving
  verdict meaning into `aoa-playbooks`
- which stop-lines still block widening, hidden mutation, or decorative
  re-entry

When the route also emits one bounded public witness sidecar for the proof
handoff, `aoa-witness-trace-integrity` may read that sidecar as adjacent proof
support. It stays narrower than owner-local runtime receipts,
`aoa-stress-recovery-window`, and reviewer judgment.

The seeded example degraded lanes live in
`examples/playbook_stress_lane.runtime-timeout-chaos.example.json` and
`examples/playbook_stress_lane.retrieval-outage-honesty.example.json`.
The matching re-entry gates live in
`examples/playbook_reentry_gate.runtime-timeout-chaos.example.json` and
`examples/playbook_reentry_gate.retrieval-outage-honesty.example.json`.
The retrieval-outage lane keeps its source-first recovery anchored to
`aoa-kag:regrounding_ticket_v1` rather than inventing repair authority inside
the playbook layer.

This playbook is narrower than `AOA-P-0020` because it does not own the whole
live incident stabilization route across downstream consumers. It is distinct
from `AOA-P-0028` because the route is not a shared-root rollout campaign with
checked-in rollout history, drift windows, and rollback windows. It is also
distinct from `AOA-P-0030` because the anchor is not one owner-law component
refresh decision but one reviewed runtime stress receipt plus one bounded
degraded lane and re-entry gate.

## Trigger boundary

Use this playbook when:
- one reviewed owner-local runtime receipt already names the active stress
  family
- the honest near-term move is degraded continuation, hold, or bounded retire,
  not full-service recovery theater
- the route needs an explicit re-entry gate before any broader reopening
- derived retrieval or projection recovery may need source-first regrounding
  through `aoa-kag`
- proof-facing follow-through matters, but remains weaker than owner receipts
  and reviewer judgment

Do not use this playbook when:
- the runtime receipt is still missing, vague, or unreviewed
- the route is really a live cross-boundary incident and still belongs in
  `AOA-P-0020`
- the route is really a shared-root rollout or rollback campaign and belongs
  in `AOA-P-0028`
- the route is really one owner-local component refresh decision and belongs in
  `AOA-P-0030`
- someone is trying to move runtime repair implementation, KAG health truth,
  or eval verdict meaning into playbook prose

## Prerequisites

- the active owner-local runtime receipt is reviewed before further mutation
- the degraded continuation or hold boundary is explicit before the lane opens
- the source-first regrounding surface is named before any derived recovery
  claim
- the re-entry gate is named before any broader reopen claim
- the proof handoff boundary is named before any eval-facing artifact is
  prepared
- blocked widening, blocked mutation, and safe-stop lines are explicit before
  the route continues

## Participating agents

- `architect` maps the runtime receipt, degraded lane, re-entry gate, and
  source-first boundary before any route widening
- `coder` lands only bounded source-owned changes or example surfaces after the
  route is explicit
- `reviewer` checks that degraded continuation, hold posture, and re-entry stay
  honest and bounded
- `evaluator` checks that any proof-facing handoff stays evidence-led and does
  not become playbook-owned verdict logic
- `memory-keeper` preserves only bounded recovery context that stays weaker
  than owner receipts and reviewer decisions

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`

## Decision points

1. Decide whether the reviewed runtime receipt is strong enough to justify a
   bounded degraded lane now.
2. Decide whether the honest posture is `resume_degraded`, `hold`, or
   `retire_route`.
3. Decide whether any derived-surface follow-through must stay source-first
   through a regrounding ticket.
4. Decide which re-entry gate checks must pass before any broader reopening.
5. Decide whether a proof-facing artifact is honestly earned or should remain
   absent.
6. Decide whether any memo writeback is bounded enough to keep.
7. Decide whether the route closes as `resume_degraded`, `hold`, `retire_route`,
   or `safe_stop`.

## Handoffs

- `architect -> coder` after the runtime receipt, degraded lane, re-entry gate,
  and stop-lines are explicit
- `coder -> reviewer` after source-owned changes and example artifacts exist
- `reviewer -> evaluator` after the route can show which evidence, if any,
  supports a proof-facing handoff candidate
- `reviewer or evaluator -> architect` when the route loses owner clarity,
  boundedness, or source-first regrounding posture
- `evaluator -> memory-keeper` only after a bounded decision or audit witness
  is explicit enough to preserve without outranking owner receipts

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the owner-local runtime receipt is weaker than the claimed degraded lane
- the route cannot name what remains blocked
- derived continuity is being implied without a source-first regrounding plan
- the re-entry gate is decorative rather than decision-bearing
- proof-facing language starts acting like runtime verdict authority
- the route starts requiring hidden mutation, unrelated restarts, or broader
  repair theater

If owner fit, degraded boundedness, or source-first posture is lost, return to
the latest valid `runtime_stress_lane`, `runtime_reentry_gate`, or
`owner_runtime_receipt` anchor before further mutation. If no honest anchor
remains, safe-stop instead of narrating recovery that the evidence does not
support.

## Expected evidence posture

The route should finish with visible evidence for:
- which owner-local runtime receipt governed the route
- which degraded lane stayed open and what it still blocked
- which re-entry gate decided `resume_degraded`, `hold`, or `retire_route`
- which regrounding ticket, if any, kept derived follow-through source-first
- which proof-facing handoff candidate remained subordinate to owner truth
- whether any memo writeback stayed bounded and optional

## Eval anchors

- `aoa-diagnosis-cause-discipline` checks that the named runtime stress family
  actually matches the receipt trail rather than a vaguer recovery story.
- `aoa-repair-boundedness` checks that degraded continuation and repair claims
  stay inside one bounded lane and do not silently widen.
- `aoa-stress-recovery-window` checks that re-entry timing and recovery claims
  stay anchored to explicit evidence windows rather than mood.
- `aoa-witness-trace-integrity` may read one bounded witness sidecar attached to
  the proof handoff candidate when the route needs reviewable trace context.
- These eval anchors are still draft, remain review-only, and stay subordinate
  to owner-local runtime receipts, `aoa-kag` health artifacts, and reviewer
  decisions.

## Memory writeback

- `decision` is allowed only for a bounded re-entry or hold decision worth
  preserving.
- `audit_event` is allowed only for a bounded runtime witness that helps later
  review.
- `provenance_thread` is allowed only when the route needs one bounded replay
  thread across receipt, lane, gate, and regrounding.
- No memo writeback target may replace owner-local runtime receipts, KAG-owned
  health artifacts, or review decisions.

## Canonical route

1. Start from one reviewed owner-local runtime receipt.
2. Name one bounded degraded lane and one blocked-widening posture.
3. Name the re-entry gate before any broader reopen claim.
4. Route any derived-surface recovery through one source-first regrounding
   ticket when needed.
5. Prepare one proof-facing handoff candidate only if the evidence is already
   stronger than the story.
6. Close with `resume_degraded`, `hold`, `retire_route`, or `safe_stop`.

## Expected artifacts

- `runtime_stress_lane`
- `runtime_reentry_gate`
- `owner_runtime_receipt`
- `runtime_closeout_receipt`
- `regrounding_ticket_ref`
- `proof_handoff_candidate`
