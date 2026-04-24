---
id: AOA-P-0048
name: titan-closeout-audit
status: experimental
summary: Coordinates a Titan-backed session closeout through visible swarm ledger review, narrow Sentinel/Delta posture, grade attribution, memory-candidate triage, and owner-routed follow-through.
scenario: titan_closeout_audit
trigger: titan_backed_session_or_wave_needs_structured_closeout_review
prerequisites:
  - titan_swarm_ledger_named
  - visible_session_or_receipt_evidence_named
  - owner_route_boundaries_named
  - mutation_and_judgment_gates_respected
participating_agents:
  - architect
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - source-of-truth
  - change-protocol
  - review
  - evaluation
  - memory-curation
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - titan_swarm_ledger
  - titan_agent_reports
  - titan_closeout_audit
  - memory_candidate_triage
  - owner_followthrough_notes
eval_anchors:
  - aoa-bounded-change-quality
  - aoa-verification-honesty
return_posture: artifact_anchor
return_anchor_artifacts:
  - titan_swarm_ledger
  - titan_closeout_audit
  - owner_followthrough_notes
return_reentry_modes:
  - previous_phase
  - review_gate
  - safe_stop
memo_recall_modes:
  - episodic
  - semantic
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_then_expand
memo_checkpoint_posture: preferred
memo_source_route_policy: required
---

# Titan Closeout Audit

## Intent

Use this playbook when a Titan-backed session, planting wave, or compact review needs one visible closeout path from task contracts and agent reports to bounded follow-through.

The playbook coordinates the scenario. It does not spawn Titans, grade them as a sovereign authority, or turn reports into memory.

## Trigger boundary

Use when a visible Titan swarm ledger or equivalent receipt set exists and the session needs structured review of task scope, findings, grades, timeout pressure, and memory candidates.

Do not use it for ordinary single-agent work, hidden child automation, or situations where Forge or Delta gates were bypassed.

## Prerequisites

- A visible Titan swarm ledger or receipt bundle is named.
- Source refs for task contracts, reports, findings, grades, and timeouts are available.
- Owner routes for SDK, role, memo, eval, stats, and playbook surfaces are explicit.
- Forge mutation and Delta judgment gates were respected when those Titans participated.

## Participating agents

- `architect` frames owner routes and boundary risk.
- `reviewer` checks narrow evidence and overclaim risk.
- `evaluator` judges bounded residual risk after evidence is assembled.
- `memory-keeper` separates memory candidates from proof and owner truth.

When using named Titans directly, keep the live summon posture explicit: Atlas and Mneme early, Sentinel late and narrow, Delta last and bounded, and Forge only through mutation gate.

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-invariant-coverage-audit`

These skills support reviewable closeout work. They do not create hidden runtime authority.

## Decision points

- Is the ledger complete enough to close, or does it need another report?
- Are low grades caused by Titan quality, orchestration, prompt width, tooling, timeout, or stale source state?
- Which findings are validated, rejected, stale, or only memory candidates?
- Which owner repository should receive each surviving follow-up?

## Handoffs

- SDK behavior and CLI issues route to `aoa-sdk`.
- Role, summon discipline, and report-boundary wording route to `aoa-agents`.
- Scenario ordering and repeatable closeout route shape stay in `aoa-playbooks`.
- Canary proof routes to `aoa-evals`.
- Memory-candidate policy routes to `aoa-memo`.
- Derived pressure summaries route to `aoa-stats`.
- Seed lineage and planting trace route to `Dionysus`.

## Fallback and rollback posture

If evidence is incomplete, stop at a review-required closeout note and do not promote memory candidates.

If an owner route is ambiguous, record the ambiguity in the closeout audit and reanchor before editing downstream docs or generated surfaces.

If a mutation gate was bypassed, mark the closeout as blocked and route the fix through the owning repository before grading the Titan as failed.

## Expected evidence posture

Evidence should include direct ledger paths, visible session or receipt refs, source file refs, and any diff excerpts used by Sentinel.

Compaction-recovered evidence may support review only when chronology confidence and tool-trace availability are named.

## Expected artifacts

- `titan_swarm_ledger`
- `titan_agent_reports`
- `titan_closeout_audit`
- `memory_candidate_triage`
- `owner_followthrough_notes`

## Eval anchors

- `aoa-bounded-change-quality`
- `aoa-verification-honesty`

Titan-specific canaries may support this route, but they remain canaries until promoted into eval-owned bundle contracts.

## Memory writeback

Memory writeback is candidate-only. A report or finding becomes a memory candidate only when source refs, closeout context, and owner route are present.

Do not treat memory candidates as proof, current truth, or authorization for future summons.

## Canonical route

1. Inspect the ledger and visible source refs.
2. Confirm each Titan task had a bounded task contract.
3. Review reports and finding lifecycle states.
4. Attribute grades and timeout pressure without collapsing orchestration fault into Titan fault.
5. Create closeout audit and memory-candidate triage.
6. Route surviving follow-through to owner repositories.
7. Refresh derived stats only after owner evidence exists.
