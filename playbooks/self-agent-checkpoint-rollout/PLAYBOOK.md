---
id: AOA-P-0006
name: self-agent-checkpoint-rollout
status: experimental
summary: Coordinates a bounded self-agent or policy-sensitive change through approval, rollback, health checks, and an improvement log.
scenario: self_agent_checkpoint
trigger: self_change_or_policy_sensitive_change
prerequisites:
  - constitution_or_source_of_truth_check_defined
  - approval_gate_defined
  - rollback_marker_available
  - health_check_defined
participating_agents:
  - architect
  - coder
  - reviewer
  - memory-keeper
required_skill_families:
  - source-of-truth
  - approval-gate
  - change-protocol
  - memory-curation
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: rollback
expected_artifacts:
  - approval_record
  - rollback_marker
  - health_check
  - improvement_log
eval_anchors:
  - aoa-approval-boundary-adherence
  - aoa-bounded-change-quality
---

# self-agent-checkpoint-rollout

## Intent

Use this playbook when a bounded self-agent or policy-sensitive change needs a real scenario-level method rather than a loose pile of skills, notes, and warnings.

The playbook keeps five things explicit:
- constitution or source-of-truth fit
- approval gate
- rollback readiness
- post-change health
- improvement-log writeback

## Trigger boundary

Use this playbook when:
- a change can reshape important AoA surfaces
- the route crosses policy, role, memory, or governance boundaries
- a normal bounded change flow is not enough by itself because checkpoint posture matters

Do not use this playbook when:
- the change is ordinary and already fits a normal bounded change workflow
- no explicit approval or rollback boundary exists
- the task is primarily a proof surface, memory curation pass, or role-definition task rather than a scenario-level route

## Prerequisites

- a constitution or source-of-truth check can be named
- an approval gate exists and is readable
- a rollback marker can be attached before mutation
- a post-change health check is defined

## Participating agents

- `architect` initiates the route, checks constitutional fit, and keeps the scope bounded before execution begins
- `coder` executes the bounded change path only after the gate is clear
- `reviewer` checks approval posture, health posture, and final boundedness
- `memory-keeper` keeps provenance and the improvement log legible after the route completes

## Required skills

- `aoa-source-of-truth-check`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`

## Decision points

1. Decide whether the target surface passes a constitution or source-of-truth check.
2. Decide whether the route is approved, deferred, or refused.
3. Decide whether rollback posture is explicit enough to proceed.
4. Decide whether the post-change health check supports continue, rollback, or handoff.
5. Decide whether the route lost approval, rollback, or health clarity badly enough that it must return to the last explicit checkpoint before any second mutation.
6. Decide whether the improvement log is explicit enough to preserve the route as reviewable history.

## Handoffs

- `architect -> coder` after constitutional fit and route scope are explicit
- `coder -> reviewer` after the bounded change path and health evidence exist
- `reviewer -> memory-keeper` after the route outcome and remaining risks are explicit
- `memory-keeper -> architect` only if the improvement log reveals a follow-up design issue rather than a one-run operational issue

## Fallback and rollback posture

Fallback mode is `rollback`.

The playbook should pause or reverse when:
- approval remains unclear
- a dry-run or inspect-first pass reveals unbounded risk
- the rollback marker is missing or weak
- the post-change health check fails or remains ambiguous

If approval posture, rollback readiness, or health interpretation becomes unclear after a first pass, do not continue by inertia.
Return to the last explicit approval or rollback anchor and require review before another mutation attempt.

Review is required before trying a second mutation pass if the first pass already crossed a checkpoint boundary.

## Expected evidence posture

The route should finish with visible evidence for:
- why the route was in-bounds or approved
- what changed and how the change stayed bounded
- what rollback marker existed before mutation
- what the post-change health result actually was
- why the route returned, if it returned, and which checkpoint anchor governed the re-entry or stop decision
- what the improvement log says should be reinforced, repeated, or avoided next time

## Expected artifacts

- `approval_record`
- `rollback_marker`
- `health_check`
- `improvement_log`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-bounded-change-quality`

## Memory writeback

- `approval_record` should survive as a `decision`
- `rollback_marker` may survive as a referenced artifact or bounded state marker rather than a new memory taxonomy
- `health_check` should survive as an `episode` or `audit_event`
- `improvement_log` should survive as a `provenance_thread`

## Canonical route

1. Run a constitution or source-of-truth check on the target surface.
2. Run the approval gate and classify proceed, defer, or stop.
3. Define the rollback marker before any mutation.
4. Use `aoa-dry-run-first` if the route still has unbounded risk.
5. Execute the bounded change path with `aoa-change-protocol`.
6. Record the post-change health check.
7. If the route loses checkpoint clarity, return to the last valid approval or rollback anchor before any further mutation.
8. Append the improvement log through a provenance-backed writeback.
