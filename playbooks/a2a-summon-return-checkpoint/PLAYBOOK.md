---
id: AOA-P-0031
name: a2a-summon-return-checkpoint
status: experimental
summary: Coordinates one reviewed aoa-summon child route through sdk.a2a decision, Codex-local target selection, reviewed child return, checkpoint bridge, proof hook, memo writeback, and runtime dry-run without turning child execution into hidden automation authority.
scenario: a2a_summon_return_checkpoint
trigger: reviewed_summon_child_route_needing_return_checkpoint_bridge
prerequisites:
  - summon_contract_available
  - quest_passport_reviewed
  - sdk_a2a_decision_available
  - codex_projection_manifest_available
  - child_return_artifacts_reviewed
  - checkpoint_bridge_boundary_named
  - eval_and_memo_surfaces_named
  - runtime_dry_run_only
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
  - aoa-checkpoint-closeout-bridge
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: review_required
expected_artifacts:
  - summon_request
  - summon_decision
  - codex_local_target
  - child_task_result
  - return_plan
  - checkpoint_bridge_plan
  - a2a_return_eval_packet
  - memo_writeback_ref
  - runtime_closeout_dry_run_receipt
return_posture: checkpoint_anchor
return_anchor_artifacts:
  - return_plan
  - checkpoint_bridge_plan
  - child_task_result
return_reentry_modes:
  - checkpoint_relaunch
  - review_gate
  - safe_stop
eval_anchors:
  - aoa-a2a-summon-return-checkpoint
  - aoa-return-anchor-integrity
memo_recall_modes:
  - episodic
  - semantic
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_capsule_then_expand
memo_checkpoint_posture: required
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

# a2a-summon-return-checkpoint

## Intent

Use this playbook when a reviewed parent route has already chosen the
`aoa-summon` contract as the narrow child-route boundary, `aoa-sdk` has a
bounded `sdk.a2a` decision or closeout request to carry, and the next honest
move is a reviewed child return into one checkpoint bridge, not live
automation.

The route keeps eight things explicit:
- which `summon_request` carried the parent anchor, quest-passport posture,
  expected outputs, and child-role intent
- which `summon_decision` chose or blocked the child route
- which `codex_local_target` came from the `aoa-agents` projection manifest
  rather than improvised role lore
- which `child_task_result` is reviewed before it can shape parent closeout
- which `return_plan` and `checkpoint_bridge_plan` drive re-entry
- which `a2a_return_eval_packet` can be judged by `aoa-evals`
- which `memo_writeback_ref` stays subordinate to reviewed artifacts
- which `runtime_closeout_dry_run_receipt` proves only adapter assembly, not
  live runtime execution

The current canonical full-chain example is the SDK-owned fixture
`repo:aoa-sdk/examples/a2a/summon_return_checkpoint_e2e.fixture.json`. This
playbook may cite it as a route walkthrough, but the fixture remains a
control-plane example rather than playbook authority or runtime execution.

This playbook is narrower than `AOA-P-0025` because it does not attempt the
whole session-growth route. It is narrower than `AOA-P-0027` because the route
is not deciding whether automation should become a playbook-owned candidate.
It is also distinct from `AOA-P-0030` because the anchor is a reviewed
summon-return contract, not an owner-law component refresh.

## Trigger boundary

Use this playbook when:
- a parent route already has a reviewed anchor and named child outputs
- the `aoa-summon` v3 request and result schemas are the child-route contract
- `aoa-sdk` has planned a Codex-local A2A target or reviewed closeout request
- the child result is reviewed before the checkpoint bridge runs
- memo, eval, routing, and runtime surfaces are named but stay owner-owned
- the runtime side is dry-run only

Do not use this playbook when:
- the parent anchor or expected child outputs are still vague
- the child route is `d3+` and still needs a split before summon
- someone is using summon language to bypass approval, proof, or closeout
- the runtime is expected to execute live automation
- the main task is only a generic cross-repo remediation route, which belongs
  in `AOA-P-0018`
- the main task is only owner-local component refresh, which belongs in
  `AOA-P-0030`

## Prerequisites

- the `summon_request` and `summon_decision` are available for review
- the quest passport or equivalent parent route posture is named
- the `sdk.a2a` decision or closeout request is available in `aoa-sdk`
- the Codex-local target cites the `aoa-agents` projection manifest when one is
  used
- the child result is reviewed before it becomes checkpoint input
- the checkpoint bridge boundary names donor harvest, progression lift, and
  quest harvest as reviewed-closeout follow-through, not hidden execution
- the eval hook and memo writeback seam are named before runtime dry-run
  receipt assembly
- the runtime path is explicitly dry-run and may only assemble a receipt
  candidate

## Participating agents

- `architect` maps parent anchor, summon contract, SDK control-plane boundary,
  and owner repos before mutation begins
- `coder` lands only bounded contract, docs, adapter, or generated-surface
  changes after the route is explicit
- `reviewer` checks that summon, SDK, routing, memo, eval, and runtime surfaces
  stay in their owning layers
- `evaluator` checks that the return claim is supported by reviewed artifacts
  and not by automation rhetoric
- `memory-keeper` records only bounded replay aids and refuses to turn child
  traces into memo truth

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-approval-gate-check`
- `aoa-dry-run-first`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-checkpoint-closeout-bridge`

`aoa-summon` is the named child-route contract input for this playbook, but it
is not yet declared as a federation-required skill here while that skill remains
below federation-ready governance posture. Once the skill is ready, this
playbook can be tightened to require it directly.

## Decision points

1. Decide whether the parent anchor and expected child outputs are explicit
   enough to allow a child summon route.
2. Decide whether the `summon_decision` allows, narrows, blocks, or splits the
   child route.
3. Decide whether the `codex_local_target` is sufficient or whether the route
   needs human review before child execution.
4. Decide whether the reviewed `child_task_result` supports return, safe stop,
   or re-split.
5. Decide whether the `checkpoint_bridge_plan` can run through reviewed
   closeout without turning checkpoint notes into final authority.
6. Decide whether `a2a_return_eval_packet` and `memo_writeback_ref` are
   honestly earned.
7. Decide whether the runtime dry-run receipt proves only adapter assembly or
   is overclaiming live execution.
8. Decide whether the route closes as `return_ready`, `split_required`,
   `human_gate_required`, or `safe_stop`.

## Handoffs

- `architect -> coder` after parent anchor, summon contract, SDK control-plane
  boundary, stop-lines, and dry-run posture are explicit
- `coder -> reviewer` after source-owned changes and generated surfaces exist
  and before any claim of runtime readiness
- `reviewer -> evaluator` after the return packet, checkpoint bridge plan, and
  dry-run receipt are inspectable
- `reviewer or evaluator -> architect` when the route loses owner clarity,
  child-result review, or checkpoint bridge posture
- `evaluator -> memory-keeper` only after a bounded decision, audit event, or
  provenance thread is supported by reviewed artifacts

## Fallback and rollback posture

Fallback mode is `review_required`.

Pause or stop when:
- the parent anchor is missing
- the `summon_request` or `summon_decision` is not reviewable
- the child route should split before summon but proceeds anyway
- Codex-local targeting relies on role lore instead of the projection manifest
  or a reviewed fallback
- the child result is not reviewed
- the checkpoint bridge starts treating checkpoint notes as final harvest,
  progression, or quest authority
- memo writeback starts acting like proof
- eval proof starts acting like runtime execution
- the runtime dry-run receipt is described as live automation

If owner fit, child-result review, or checkpoint bridge posture is lost, return
to the latest valid `return_plan`, `checkpoint_bridge_plan`, or
`child_task_result` anchor before further mutation. If no honest anchor remains,
safe-stop and require a new reviewed parent route instead of inventing
continuity.

## Expected evidence posture

The route should finish with visible evidence for:
- which SDK-owned E2E fixture, if any, connected the full dry-run route
- which parent route and `summon_request` governed the child task
- which `summon_decision` allowed, narrowed, blocked, or split the route
- which Codex-local target was selected and what owner role source supported it
- which child result was reviewed before return
- which checkpoint bridge plan governed re-entry
- which eval packet and memo writeback references stayed subordinate to owner
  truth
- which runtime dry-run receipt was assembled without live automation

## Eval anchors

- `aoa-a2a-summon-return-checkpoint` checks that the summon request, SDK A2A
  decision, Codex-local target, reviewed child result, checkpoint bridge,
  memo writeback, and dry-run runtime receipt stay in one bounded contract.
- `aoa-return-anchor-integrity` checks that return and re-entry preserve a real
  anchor instead of relying on hidden continuity.
- These eval anchors are draft, review-only, and subordinate to source-owned
  contracts in `aoa-skills`, `aoa-sdk`, `aoa-memo`, `aoa-routing`, and
  `abyss-stack`.

## Memory writeback

- `decision` is allowed only for a bounded `summon_decision`, return decision,
  or bridge decision that shaped later re-entry.
- `audit_event` is allowed only for a reviewed child return, bridge execution
  boundary, or dry-run runtime receipt worth preserving as an operational
  witness.
- `provenance_thread` is allowed only when the route needs one bounded replay
  thread across summon request, SDK decision, child result, checkpoint bridge,
  eval packet, memo reference, and runtime dry-run receipt.
- No memo writeback target may outrank the reviewed `child_task_result`, the
  `return_plan`, the `checkpoint_bridge_plan`, or the owning SDK/eval/runtime
  surfaces.

## Canonical route

1. Start from one reviewed parent anchor and one `summon_request`.
2. Inspect one `summon_decision` and stop if it blocks, splits, or requires a
   human gate.
3. Inspect or assemble one `codex_local_target` through the SDK A2A seam.
4. Require one reviewed `child_task_result`.
5. Build one `return_plan` and one `checkpoint_bridge_plan`.
6. Attach one `a2a_return_eval_packet` and one bounded `memo_writeback_ref`
   only if they are earned.
7. Assemble one `runtime_closeout_dry_run_receipt` that remains dry-run only.
8. Close as return-ready, split-required, human-gated, or safe-stop.

When using the current fixture, confirm its `routing_reentry.primary_action`
returns to `aoa-playbooks/generated/playbook_registry.min.json` with
`target_value=AOA-P-0031`; routing must not become the source of playbook
meaning.

## Expected artifacts

- `summon_request`
- `summon_decision`
- `codex_local_target`
- `child_task_result`
- `return_plan`
- `checkpoint_bridge_plan`
- `a2a_return_eval_packet`
- `memo_writeback_ref`
- `runtime_closeout_dry_run_receipt`
