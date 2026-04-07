---
id: AOA-P-0022
name: project-foundation-workspace-landing
status: experimental
summary: Coordinates sibling-workspace landing through shared foundation install, explicit root guidance, ingress and mutation-gate verification, and portable bootstrap posture.
scenario: project_foundation_workspace_landing
trigger: sibling_workspace_needing_foundation_install_root_posture_and_portable_bootstrap
prerequisites:
  - workspace_root_named
  - sibling_repo_set_bounded
  - foundation_profile_surface_named
  - install_and_verify_surfaces_named
  - root_guidance_surface_named
  - portability_scope_bounded
participating_agents:
  - architect
  - coder
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - source-of-truth
  - approval-gate
  - preview
  - change-protocol
  - local-bringup
  - review
required_skills:
  - aoa-source-of-truth-check
  - aoa-bounded-context-map
  - aoa-approval-gate-check
  - aoa-dry-run-first
  - aoa-change-protocol
  - aoa-local-stack-bringup
  - aoa-adr-write
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - workspace_layout_map
  - foundation_install_report
  - root_guidance_record
  - ingress_guard_verification_pack
  - portability_bootstrap_pack
  - handoff_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - workspace_layout_map
  - foundation_install_report
  - ingress_guard_verification_pack
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
eval_anchors:
  - aoa-approval-boundary-adherence
  - aoa-verification-honesty
  - aoa-tool-trajectory-discipline
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

# project-foundation-workspace-landing

## Intent

Use this playbook when one bounded campaign must turn a sibling workspace into a truthful project workspace with shared foundation install, explicit root guidance, and a portable route for non-default roots.

The route keeps six things explicit:
- which directory is the workspace root and which sibling repositories are actually in scope
- which foundation profile is the canonical shared install layer
- what root guidance belongs in the workspace entrypoint versus owner-repo canon
- what ingress and mutation-gate route the operator or agent should use after landing
- what verification proves the install and workspace posture honestly
- what portability story survives when the same project must land outside the current root

This playbook is wider than a single repository change and narrower than a generic multi-repo rollout once the real route is specifically workspace landing.
Use `AOA-P-0010` when the task is a generic cross-repo source-of-truth change without a shared workspace landing anchor.
Use `AOA-P-0014` when the real problem is bounded local startup diagnosis rather than workspace foundation landing.
Use `AOA-P-0015` when the remaining work is documentation authority cleanup or sharing rather than install and posture landing.
Use `AOA-P-0021` when the route is landing a reviewed capability into an owner repo before later workspace rollout.

## Trigger boundary

Use this playbook when:
- a sibling workspace needs one shared foundation install at the root rather than ad hoc per-repo skill drift
- root-level session posture must become explicit through canonical guidance and ingress or mutation-gate commands
- the route needs install verification plus bounded portability for future non-default workspace roots
- the scenario spans more than one owner repo even if the final install target is the shared workspace root

Do not use this playbook when:
- only one repository needs bounded bootstrap or local cleanup
- the route is really generic multi-repo sequencing without workspace landing as the main anchor
- the task is only to document authority or outward sharing after canon is already settled
- the only remaining work is a single explicit skill activation rather than a scenario route
- no bounded sibling workspace can be named

## Prerequisites

- the workspace root is named before mutation begins
- the sibling repositories in scope are explicit enough to keep the route reviewable
- the canonical foundation profile and install target are known before changes begin
- the verify surface for the shared install and post-landing posture is named
- the root guidance surface is named before it is edited or created
- portability beyond the current root is bounded enough to avoid widening into broad ecosystem rollout

## Participating agents

- `architect` maps the workspace root, sibling repo set, and authority split between root guidance and owner-repo canon
- `coder` applies the smallest bounded install, guidance, and bootstrap changes once the workspace boundary is explicit
- `reviewer` checks that shared install, root guidance, and portability claims stay honest and do not absorb unrelated repo cleanup
- `evaluator` checks that install verification and ingress or guard posture are strong enough to support closure or defer
- `memory-keeper` preserves the surviving landing decision, audit trail, and provenance-safe handoff without inventing a new workspace-memory taxonomy

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-local-stack-bringup`
- `aoa-adr-write`

## Decision points

1. Decide which directory is the workspace root and which sibling repositories belong to the bounded landing wave.
2. Decide whether `repo-project-foundation` is the exact shared install layer or whether the route should stop before forcing a different baseline.
3. Decide what belongs in root guidance versus the owner repos that define canon for install, bootstrap, or session posture.
4. Decide whether repo-local `.agents/skills` rollout belongs in the current wave or should remain deferred.
5. Decide what verify path proves shared install, ingress posture, and mutation-gate behavior strongly enough to close the route.
6. Decide whether portability beyond the current root needs a bounded bootstrap path now or can remain future work.
7. Decide whether the route closes with a verified workspace landing or hands off to a later owner-specific rollout or documentation pass.

## Handoffs

- `architect -> coder` after the workspace boundary, install target, and authority split are explicit
- `coder -> reviewer` after the foundation install report, root guidance record, and bootstrap pack exist
- `reviewer -> evaluator` after the ingress and mutation-gate verification pack is explicit enough to support closure or defer
- `reviewer or evaluator -> architect` when workspace boundary, authority split, or portability posture drifts enough that the route must return to the last valid anchor
- `evaluator -> memory-keeper` after the landing decision and residual handoff are explicit enough to survive the route
- `memory-keeper -> architect` only when the handoff record proves another governed route still remains

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the workspace root or sibling repo set remains ambiguous
- the shared foundation profile drifts away from the named kernel, outer ring, and risk ring baseline
- root guidance starts replacing owner-repo canon instead of pointing back to it
- overlays or unrelated repo-local extras begin to leak into the shared install layer
- portability work widens into unbounded repo-local rollout or environment-specific cleanup
- the verification pack is weaker than the claimed workspace landing result

If workspace boundary, install truth, or verification integrity is lost, return to the last valid `workspace_layout_map`, `foundation_install_report`, or `ingress_guard_verification_pack` anchor before further mutation.
If no honest anchor remains, stop and defer rather than claim a landed workspace that still depends on hidden operator memory.

## Expected evidence posture

The route should finish with visible evidence for:
- which sibling repositories and root-level surfaces were in scope
- which foundation profile landed at the workspace root and what stayed out of baseline
- what root guidance or session-start posture was declared authoritative
- what ingress and mutation-gate behavior the route actually verified
- what portable bootstrap route exists for future non-default workspace roots
- what work stayed deferred for later repo-local or owner-specific follow-on

## Expected artifacts

- `workspace_layout_map`
- `foundation_install_report`
- `root_guidance_record`
- `ingress_guard_verification_pack`
- `portability_bootstrap_pack`
- `handoff_record`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-verification-honesty`
- `aoa-tool-trajectory-discipline`

Use `aoa-approval-boundary-adherence` to check that root-level install and guidance respected workspace and owner-repo authority boundaries.
Use `aoa-verification-honesty` to check that install, verify, and ingress or mutation-gate claims match what actually ran.
Use `aoa-tool-trajectory-discipline` to check that workspace landing stayed reviewable and bounded instead of turning into terminal folklore or manual ritual.

## Memory writeback

- the main landing or portability decision may survive as a `decision`
- the install and verification closeout may survive as an `audit_event`
- the route handoff may survive as a `provenance_thread`
- the `workspace_layout_map`, `root_guidance_record`, and `portability_bootstrap_pack` remain route artifacts unless a later memo pass promotes them explicitly

The playbook does not move install canon, bootstrap authority, or skill semantics out of their owner repos.

## Canonical route

1. Use `aoa-source-of-truth-check` and `aoa-bounded-context-map` to name the workspace root, sibling repo set, and the owner-repo canon that governs install and session posture.
2. Use `aoa-approval-gate-check` and `aoa-dry-run-first` to bound which root directories, symlinks, and guidance surfaces may change before mutation begins.
3. Land or refresh the shared foundation install at the workspace root and keep overlays or repo-local extras out of the baseline unless the route explicitly widens later.
4. Record or repair the root guidance surface so session-start posture points to canonical install docs and ingress or mutation-gate commands instead of duplicating owner canon.
5. Use `aoa-change-protocol` for the bounded repo and workspace changes that make the landing real, and use `aoa-adr-write` when the route introduces a durable workspace install or guidance decision.
6. Use `aoa-local-stack-bringup` only as far as needed to verify that the workspace can actually enter through ingress and guard surfaces after landing.
7. If the same project must land outside the current root, add the smallest bounded bootstrap route that preserves sibling-workspace layout without widening into generic ecosystem rollout.
8. Close with the install report, verification pack, and handoff record; if authority, baseline integrity, or verification honesty is lost, return through `previous_phase`, `review_gate`, `rollback_gate`, or `safe_stop` before claiming the workspace landed.
