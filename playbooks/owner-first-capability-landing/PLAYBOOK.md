---
id: AOA-P-0021
name: owner-first-capability-landing
status: experimental
summary: Coordinates a reviewed capability candidate through staged lineage intake, owner-first landing, optional lineage decomposition, bounded rollout, and post-landing hardening across neighboring AoA layers.
scenario: owner_first_capability_landing
trigger: reviewed_capability_candidate_requiring_owner_first_landing_then_bounded_rollout
prerequisites:
  - reviewed_candidate_or_seed_pack_named
  - owner_repo_candidate_named
  - neighboring_lineage_surfaces_mapped
  - rollout_scope_bounded
  - verification_and_hardening_surfaces_named
  - scaffold_or_defer_posture_named
participating_agents:
  - architect
  - coder
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - source-of-truth
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
  - aoa-adr-write
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - candidate_lineage_pack
  - owner_landing_bundle
  - landing_decision
  - rollout_pack
  - validation_pack
  - hardening_record
  - handoff_record
return_posture: artifact_anchor
return_anchor_artifacts:
  - owner_landing_bundle
  - landing_decision
  - validation_pack
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
eval_anchors:
  - aoa-approval-boundary-adherence
  - aoa-scope-drift-detection
  - aoa-verification-honesty
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

# owner-first-capability-landing

## Intent

Use this playbook when a reviewed capability candidate already looks real enough to land, but the honest route still needs one owner-first campaign from staged lineage intake to bounded rollout and post-landing hardening.

The route keeps seven things explicit:
- what reviewed packet, staged seed, or lineage pack justified landing now
- which repository owns the first truthful landing
- whether the owner landing is scaffold, pinned lineage, or direct canonical bundle
- whether decomposition or lineage pinning must happen before wider rollout
- what rollout order keeps downstream repos and `/srv` honest
- what validation and live hardening must run before the route can close
- what durable decision and handoff survive the campaign

This playbook is narrower than generic cross-repo rollout once owner truth already exists, and wider than a single repository change.
Use `AOA-P-0010` when the source-owned change already lives in the owner repo and the main problem is generic multi-repo sequencing.
Use `AOA-P-0017` when ordered upstream bridge publication and downstream revalidation against updated upstream `main` are the route anchor.
Use `AOA-P-0018` when a failed validator or seam break is already the route anchor.
Use `AOA-P-0015` when the remaining work is documentation authority cleanup or sanitized reporting rather than capability landing.

## Trigger boundary

Use this playbook when:
- a reviewed capability candidate or staged seed has enough evidence that the main work is landing, not deciding whether it exists
- one owner repo must absorb the first truthful version before wider rollout
- the scenario may include scaffold posture, lineage pinning, downstream sync, and bounded live hardening
- the route is larger than one bounded skill or one ordinary single-repo change

Do not use this playbook when:
- the candidate still needs owner-layer routing or final promotion verdict through `aoa-session-donor-harvest` or `aoa-quest-harvest`
- source-owned truth already lives in the owner repo and the remaining work is just `AOA-P-0010` or `AOA-P-0017`
- the task is mainly documentation authority cleanup or sanitized outward sharing, which belongs in `AOA-P-0015`
- a validator failure or live incident is already the route anchor, which belongs in `AOA-P-0018` or `AOA-P-0020`

## Prerequisites

- the reviewed candidate, staged seed, or lineage pack is named before landing begins
- the candidate owner repo is explicit enough to keep the first landing honest
- neighboring lineage surfaces are mapped before mutation begins
- the rollout scope is bounded before downstream repos or `/srv` are touched
- the validation and live hardening surfaces are named before the first merge closes
- the route can say whether scaffold, defer, or direct canonical landing is the honest first posture

## Participating agents

- `architect` maps the candidate to its owner repo, neighboring lineage surfaces, and rollout order before mutation begins
- `coder` applies the smallest owner-first landing bundle and later bounded rollout slices once the route boundary is explicit
- `reviewer` checks that scaffold posture, lineage pinning, and downstream sync stay honest rather than getting narrated as canon too early
- `evaluator` checks that validation and live hardening actually support proceed, defer, or follow-on route closure
- `memory-keeper` preserves the landing decision, audit trail, and provenance-safe handoff without inventing a new memo taxonomy

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-adr-write`

## Decision points

1. Decide whether the reviewed candidate is strong enough to land now or must stay staged.
2. Decide which repo owns the first truthful landing and which neighboring repos must wait.
3. Decide whether the owner landing should be scaffold, pinned lineage, or direct canonical bundle.
4. Decide whether decomposition or lineage pinning must happen before downstream rollout can stay honest.
5. Decide whether the rollout can remain one bounded wave or must hand off later to `AOA-P-0017`.
6. Decide what exact validation pack is required before downstream repos and `/srv` can be updated.
7. Decide whether live hardening exposes only a local seam repair or forces return to the last valid owner anchor.
8. Decide whether the route closes cleanly or hands off to later rollout, remediation, or documentation cleanup.

## Handoffs

- `architect -> coder` after the candidate lineage pack, owner boundary, landing mode, and stop conditions are explicit
- `coder -> reviewer` after the owner landing bundle, rollout pack, and validation notes exist
- `reviewer -> evaluator` after the landing decision, validation pack, and hardening record are explicit enough to support closure or defer
- `reviewer or evaluator -> architect` when lineage pinning, rollout order, or hardening integrity drift enough that the route must return to the last valid landing anchor
- `evaluator -> memory-keeper` after the route can name merge, defer, or follow-on posture with bounded evidence
- `memory-keeper -> architect` only when the handoff record proves that another governed route still remains

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the reviewed candidate is weaker than the claimed landing posture
- the owner repo remains ambiguous across neighboring layers
- scaffold posture starts being narrated as finished canon
- decomposition or lineage pinning debt must land before rollout but still remains unresolved
- downstream rollout or `/srv` install outruns owner validation
- live hardening reveals a seam whose repair would widen the route beyond the named campaign

If owner truth, validation closure, or hardening integrity is lost, return to the last valid `owner_landing_bundle`, `landing_decision`, or `validation_pack` anchor before further mutation.
If the candidate no longer warrants landing, return it to staged lineage rather than force a rollout by inertia.
If repair work becomes the new route anchor, stop and hand off to `AOA-P-0018` instead of widening this playbook past bounded landing.

## Expected evidence posture

The route should finish with visible evidence for:
- why the candidate warranted landing now
- why the chosen owner repo was the first truthful landing surface
- what landed as scaffold, pinned lineage, or direct canon
- whether decomposition or lineage pinning happened before wider rollout
- what validations ran in the owner repo, downstream roots, and `/srv`
- what live hardening proved, repaired, or deferred
- what handoff remains for later rollout, remediation, or reporting

## Expected artifacts

- `candidate_lineage_pack`
- `owner_landing_bundle`
- `landing_decision`
- `rollout_pack`
- `validation_pack`
- `hardening_record`
- `handoff_record`

## Eval anchors

- `aoa-approval-boundary-adherence`
- `aoa-scope-drift-detection`
- `aoa-verification-honesty`

Use `aoa-approval-boundary-adherence` to check that the route respected owner-first boundaries instead of landing meaning in the nearest convenient repo.
Use `aoa-scope-drift-detection` to check that the campaign did not silently widen from bounded landing into unrelated ecosystem cleanup.
Use `aoa-verification-honesty` to check that rollout, `/srv` install, and live hardening claims match what actually ran.

## Memory writeback

- `landing_decision` should survive as a `decision`
- `validation_pack` or `hardening_record` may survive as an `audit_event` when they record actual closure or deferred seam posture
- `handoff_record` should survive as a `provenance_thread`
- `candidate_lineage_pack`, `owner_landing_bundle`, and `rollout_pack` remain route artifacts or referenced artifacts rather than memo writeback kinds

The playbook does not create a new memory-object kind and does not move skill, technique, or stats ownership into the playbook layer.

## Canonical route

1. Start from the reviewed candidate pack or staged seed and confirm the owner repo plus neighboring boundaries with `aoa-source-of-truth-check` and `aoa-bounded-context-map`.
2. Record whether the honest first landing is scaffold, pinned lineage, or direct canon, and keep unlanded variants staged rather than leaking them downstream.
3. Use `aoa-approval-gate-check` and `aoa-dry-run-first` to make write scope, install surfaces, and stop conditions explicit before mutation begins.
4. Land the capability in the owner repo through `aoa-change-protocol` and capture any durable boundary or lineage decision through `aoa-adr-write`.
5. If the owner landing introduces pending lineage debt, complete the smallest required decomposition or pinning step before wider rollout.
6. Build the `validation_pack` for the owner repo and tighten interface or install parity with `aoa-contract-test` before the route widens.
7. Roll out to dependent repos and `/srv` only after owner truth is explicit, and keep the `rollout_pack` reviewable enough to defer or stop without losing the route.
8. Run one bounded live hardening pass; if seams appear, return to the last valid owner anchor and re-enter through `previous_phase`, `review_gate`, `rollback_gate`, or `safe_stop` before closing with the `landing_decision`, `hardening_record`, and `handoff_record`.
