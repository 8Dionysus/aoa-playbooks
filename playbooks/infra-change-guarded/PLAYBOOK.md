---
id: AOA-P-0012
name: infra-change-guarded
status: experimental
summary: Coordinates a guarded infrastructure or configuration change through approval, preview-first discipline, rollback posture, and bounded verification.
scenario: infra_change_guarded
trigger: infrastructure_or_configuration_change_needing_preview
prerequisites:
  - approval_boundary_named
  - canonical_runbook_surface_known
  - rollback_or_recovery_path_named
  - verification_boundary_named
participating_agents:
  - architect
  - coder
  - reviewer
  - memory-keeper
required_skill_families:
  - approval-gate
  - source-of-truth
  - preview
  - safe-infra
  - verification
required_skills:
  - aoa-approval-gate-check
  - aoa-source-of-truth-check
  - aoa-dry-run-first
  - aoa-safe-infra-change
  - aoa-local-stack-bringup
  - aoa-contract-test
  - aoa-adr-write
  - aoa-sanitized-share
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - approval_record
  - canonical_runbook_map
  - preview_evidence
  - rollback_plan
  - infra_change_set
  - verification_pack
return_posture: artifact_anchor
return_anchor_artifacts:
  - approval_record
  - preview_evidence
  - rollback_plan
return_reentry_modes:
  - previous_phase
  - rollback_gate
  - safe_stop
eval_anchors:
  - aoa-approval-boundary-adherence
  - aoa-verification-honesty
memo_contract_refs:
  - examples/checkpoint_to_memory_contract.example.json
  - examples/provenance_thread.example.json
memo_writeback_targets:
  - decision
  - audit_event
  - provenance_thread
---

# infra-change-guarded

## Intent

Use this playbook when services, configuration, startup surfaces, or operational topology need a bounded change path that stays preview-first and rollback-aware.

The route keeps explicit:

- whether authority to mutate already exists
- which runbooks and config docs are canonical
- what the preview seam proved before mutation
- what rollback or recovery path exists
- what bounded verification closes the route

Use `AOA-P-0014` when the real work is local-only diagnosis and blocker isolation.
Use `AOA-P-0020` when a live cross-boundary incident already exists and the route must stabilize or degrade with explicit recovery handoff.

## Trigger boundary

Use this playbook when:

- the route changes infrastructure, service configuration, environment setup, or operational startup surfaces
- a preview seam exists and should happen before mutation
- rollback posture matters as much as the direct apply step
- the result should leave bounded operational evidence, not ad hoc terminal folklore

Do not use this playbook when:

- the task is purely a docs cleanup or domain refactor with no runtime implications
- one bounded skill is enough and no explicit preview or rollback seam is needed
- the route is really `AOA-P-0014 local-stack-diagnosis` or `AOA-P-0020 incident-recovery-routing`
- the change is really routing, agent taxonomy, or memory-object work
- the route cannot name a rollback or safe-stop posture at all

## Prerequisites

- the approval boundary is explicit before the route mutates
- canonical runbooks, startup docs, or config surfaces are known
- a rollback or recovery path is named
- the verification boundary is explicit before execution starts

## Participating agents

- `architect` names the runbook surface, approval boundary, and rollback posture
- `coder` executes only the smallest bounded infra change once the preview seam is explicit
- `reviewer` checks that preview evidence, rollback notes, and verification remain honest
- `memory-keeper` preserves the decision, audit, and provenance artifacts that survive the route

## Required skills

- `aoa-approval-gate-check`
- `aoa-source-of-truth-check`
- `aoa-dry-run-first`
- `aoa-safe-infra-change`
- `aoa-local-stack-bringup`
- `aoa-contract-test`
- `aoa-adr-write`
- `aoa-sanitized-share`

## Decision points

1. Decide whether approval is explicit enough to proceed beyond preview.
2. Decide which runbook or startup surface is actually canonical.
3. Decide what the preview proved and what still remains unproven.
4. Decide whether rollback posture is strong enough to justify mutation.
5. Decide whether local bring-up or a contract check is the right bounded verifier.
6. Decide whether the route should proceed, return to preview, or stop for review.

## Handoffs

- `architect -> coder` after authority, runbook canon, and rollback posture are explicit
- `coder -> reviewer` after preview evidence, infra change notes, and verification outputs exist
- `reviewer -> memory-keeper` after the route can preserve its decision, audit event, and provenance trail without leaking unsafe operational detail
- `reviewer or memory-keeper -> architect` when the route must return to the last preview or rollback anchor before another pass

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:

- approval is still unresolved
- the canonical runbook surface is unclear
- the preview seam was skipped or does not support the next step
- rollback posture is weaker than the proposed mutation
- the verification pack depends on an unstable local environment with no clear blocker report

If preview, rollback, or verification integrity is lost, return to the last valid `preview_evidence` or `rollback_plan` anchor before any further mutation.
If no honest rollback anchor remains, stop for review instead of widening the route.

## Expected evidence posture

The route should finish with visible evidence for:

- how authority was classified
- which runbook or config surface constrained the change
- what the preview seam proved
- what rollback or recovery path remained available
- what exact infra change was applied
- what bounded verification closed the route

## Expected artifacts

- `approval_record`
- `canonical_runbook_map`
- `preview_evidence`
- `rollback_plan`
- `infra_change_set`
- `verification_pack`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-verification-honesty`

Use `aoa-approval-boundary-adherence` to check that preview and mutation respected explicit authority boundaries.
Use `aoa-verification-honesty` to check that preview and post-change verification are reported truthfully.

## Memory writeback

- the controlling infra decision may survive as a `decision`
- the meaningful verification and rollback closeout may survive as an `audit_event`
- the route handoff trail may survive as a `provenance_thread`
- the canonical runbook map, preview evidence, and infra change set remain route artifacts unless a later memo pass promotes them explicitly

## Canonical route

1. Use `aoa-approval-gate-check` to classify authority before mutation.
2. Use `aoa-source-of-truth-check` to identify the canonical runbook or startup surface.
3. Use `aoa-dry-run-first` to capture preview evidence before the real infra change.
4. Use `aoa-safe-infra-change` to apply the smallest reversible operational change.
5. Verify with `aoa-local-stack-bringup` or `aoa-contract-test`, depending on the bounded verification seam.
6. Record any durable operational decision through `aoa-adr-write` and prepare a safe outbound summary through `aoa-sanitized-share`.
7. If preview, rollback, or verification integrity is lost, return to the last artifact anchor and re-enter through `previous_phase`, `rollback_gate`, or `safe_stop`.
