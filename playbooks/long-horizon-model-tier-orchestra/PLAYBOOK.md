---
id: AOA-P-0008
name: long-horizon-model-tier-orchestra
status: experimental
summary: Coordinates a long-horizon route through explicit model-tier handoffs, deep escalation gates, and distillation posture.
scenario: model_tier_orchestration
trigger: long_horizon_or_high_cost_route
prerequisites:
  - tier_registry_defined
  - bounded_route_goal_defined
  - verification_boundary_defined
  - distillation_target_defined
participating_agents:
  - architect
  - coder
  - reviewer
  - memory-keeper
required_skill_families:
  - change-protocol
  - review
  - memory-curation
  - research
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: handoff
expected_artifacts:
  - route_decision
  - bounded_plan
  - verification_result
  - transition_decision
  - distillation_pack
eval_anchors:
  - aoa-long-horizon-depth
  - aoa-tool-trajectory-discipline
---

# long-horizon-model-tier-orchestra

## Intent

Use this playbook when a route is large enough that one tier should not quietly absorb routing, planning, execution, verification, deep arbitration, and distillation at the same time.

The goal is to keep the long-horizon route explicit:
- route first
- plan second
- execute in bounded slices
- verify before deep escalation
- distill after non-trivial motion

## Trigger boundary

Use this playbook when:
- the route is multi-step and likely to span more than one bounded pass
- the cost of error is high enough that verification and escalation need named gates
- deep synthesis may be needed, but should not run by default
- the route should leave a reviewable distillation pack at the end

Do not use this playbook when:
- one bounded workflow can complete the task without tier choreography
- the route is so vague that no bounded plan can be named
- the real need is a human role contract rather than a scenario route
- distillation or checkpoint posture does not matter

## Prerequisites

- a tier registry exists and names `router`, `planner`, `executor`, `verifier`, `conductor`, `deep`, and `archivist`
- the route goal is bounded enough to plan
- verification posture is explicit before execution starts
- the route has a named distillation target before work expands

## Participating agents

- `architect` keeps the route goal, boundaries, and orchestration fit explicit
- `coder` executes bounded slices once the current tier decision is clear
- `reviewer` checks that verification posture and escalation posture stay reviewable
- `memory-keeper` receives the final distillation pack and preserves bounded writeback posture

## Required skills

- `aoa-change-protocol`
- `aoa-source-of-truth-check`
- `aoa-dry-run-first`
- `aoa-bounded-context-map`

## Decision points

1. Decide whether the route can stay in the ordinary `route -> plan -> do -> verify` loop.
2. Decide whether the `conductor` should keep the route local, escalate, or pause.
3. Decide whether the current contradiction or cost-of-error surface justifies `deep`.
4. Decide whether the run is complete enough to distill.
5. Decide whether the distillation pack should stay operational-only or become bounded memo writeback.

## Handoffs

- `router -> planner` after task shape and risk are explicit
- `planner -> executor` after the bounded slice and checks are explicit
- `executor -> verifier` after the bounded slice completes
- `verifier -> conductor` when the route should continue, escalate, or pause
- `conductor -> deep` only when the deep trigger is named explicitly
- `conductor or verifier -> archivist` when the route has enough material to distill
- `archivist -> memory-keeper` when the distillation pack needs bounded writeback review

## Fallback and rollback posture

Fallback mode is `handoff`.

Pause or hand off when:
- the next tier is unclear
- the current slice lost its verification boundary
- the route is trying to use `deep` as a default instead of a trigger-based intervention
- the distillation target is still vague

If the route crosses a high-cost boundary without a clear next tier, stop and re-route instead of continuing by inertia.

## Expected evidence posture

The route should finish with visible evidence for:
- why the chosen tier sequence was justified
- whether `deep` was triggered or avoided and why
- how verification constrained the next move
- what the distillation pack includes
- what remains operational-only versus memo-surviving

## Expected artifacts

- `route_decision`
- `bounded_plan`
- `verification_result`
- `transition_decision`
- `distillation_pack`

## Eval anchors

- `aoa-long-horizon-depth`
- `aoa-tool-trajectory-discipline`

## Memory writeback

- tier-local execution notes should usually stay operational-only
- `transition_decision` may survive as a `decision` when it changes later routing posture
- the `distillation_pack` should nominate summaries, decisions, and memory candidates without pretending to be source-authored canon
- contradiction notes should remain explicit rather than being smoothed away for neatness

## Canonical route

1. Let `router` classify the task and name the next tier.
2. Let `planner` shape the current bounded slice and verification posture.
3. Let `executor` perform the slice and leave explicit state deltas.
4. Let `verifier` judge whether the slice supports continue, stop, or escalate.
5. Let `conductor` decide whether the route should continue, call `deep`, or pause.
6. Use `deep` only when the escalation trigger is explicit.
7. Distill the run through `archivist` and hand the result to `memory-keeper` for bounded writeback review.
