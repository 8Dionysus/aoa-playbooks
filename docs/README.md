# Documentation Map

This file is the human-first entrypoint for the `docs/` surface of `aoa-playbooks`.

Use it when you want to understand the AoA playbook layer rather than the broader federation as a whole.

## Start here

- Read [CHARTER](../CHARTER.md) for the role and boundaries of the playbook layer.
- Read [DESIGN](../DESIGN.md) for the system form of the playbook layer.
- Read [DESIGN.AGENTS](../DESIGN.AGENTS.md) for the agent-facing route mesh form.
- Read [mechanics](../mechanics/README.md),
  [activation mechanic](../mechanics/activation/README.md),
  [scenario composition mechanic](../mechanics/scenario-composition/README.md),
  [federation closure mechanic](../mechanics/federation-closure/README.md),
  [review gate mechanic](../mechanics/review-gate/README.md),
  [real-run harvest mechanic](../mechanics/real-run-harvest/README.md),
  [antifragility mechanic](../mechanics/antifragility/README.md),
  [Agon mechanic](../mechanics/agon/README.md),
  [recurrence mechanic](../mechanics/recurrence/README.md),
  [checkpoint mechanic](../mechanics/checkpoint/README.md),
  [Experience mechanic](../mechanics/experience/README.md),
  [release-support mechanic](../mechanics/release-support/README.md),
  [questbook mechanic](../mechanics/questbook/README.md),
  [RPG mechanic](../mechanics/rpg/README.md),
  [Titan mechanic](../mechanics/titan/README.md),
  and [portfolio governance mechanic](../mechanics/portfolio-governance/README.md)
  when repeatable operation topology is the question.
- Read [PLAYBOOK_MODEL](../mechanics/portfolio-governance/parts/model-spine/docs/playbook-model.md) for the conceptual model.
- Read [BOUNDARIES](BOUNDARIES.md) for ownership discipline relative to neighboring AoA layers.
- Read [PLAYBOOK_BUNDLE_CONTRACT](../mechanics/activation/parts/activation-surface/docs/playbook-bundle-contract.md) for the authored bundle contract.
- Read [PLAYBOOK_EXECUTION_SEAM](../mechanics/activation/parts/activation-surface/docs/playbook-execution-seam.md) for the derived runtime-readable activation seam.
- Read [PLAYBOOK_OPERATIONAL_FAMILY](../mechanics/portfolio-governance/parts/operational-family/docs/playbook-operational-family.md) for chooser discipline across the operational playbook family.
- Read [HANDOFF_CONTRACTS](../mechanics/scenario-composition/parts/composition-surfaces/docs/handoff-contracts.md) for the bounded playbook-to-skill handoff bridge.
- Read [FAILURE_RECOVERY](../mechanics/scenario-composition/parts/composition-surfaces/docs/failure-recovery.md) for the shared failure catalog posture.
- Read [SUBAGENT_PATTERNS](../mechanics/scenario-composition/parts/composition-surfaces/docs/subagent-patterns.md) for explicit subagent recipe doctrine.
- Read [AUTOMATION_SEEDS](../mechanics/scenario-composition/parts/composition-surfaces/docs/automation-seeds.md) for example-only automation seed posture.
- Read [PLAYBOOK_RECURRENCE_DISCIPLINE](../mechanics/recurrence/parts/recurrence-discipline/docs/playbook-recurrence-discipline.md) for scenario-level recurrence posture.
- Read [PLAYBOOK_LIFECYCLE](../mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-lifecycle.md) for graduation and lifecycle doctrine.
- Read [PLAYBOOK_PORTFOLIO](../mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-portfolio.md) for coverage matrix and portfolio guidance.
- Read [PLAYBOOK_REAL_RUN_WORKFLOW](../mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/playbook-real-run-workflow.md) for the repo-first chooser -> run -> review -> gate workflow.
- Read [PLAYBOOK_REAL_RUN_HARVEST](../mechanics/real-run-harvest/parts/harvest-template-source-store/docs/playbook-real-run-harvest.md) for reviewable evidence scaffolding for future real runs.
- Read [CHECKPOINT_DISTILLATION_CLOSED_LOOP_PILOT](../mechanics/checkpoint/parts/distillation-closed-loop/docs/checkpoint-distillation-closed-loop-pilot.md) for the bounded checkpoint-distillation pilot-runbook route.
- Read [Codex-plane rollout cycle](../mechanics/release-support/parts/promotion-and-retention/docs/codex-plane-rollout-cycle.md) for the shared-root deployment continuity companion under `AOA-P-0028`.
- Read [trusted rollout campaign cadence](../mechanics/release-support/parts/promotion-and-retention/docs/trusted-rollout-campaign-cadence.md) for the bounded cadence adjunct that stays under `AOA-P-0028` without minting a second playbook.
- Read [stress lanes](../mechanics/antifragility/parts/stress-lanes/docs/playbook-stress-lanes.md) for additive degraded-lane doctrine inside recurring scenarios.
- Read [stress harvest](../mechanics/antifragility/parts/stress-harvest/docs/playbook-stress-harvest.md) for bounded harvest and re-entry posture for stressed runs.
- Read [runtime chaos wave 1](../mechanics/antifragility/parts/runtime-chaos-wave1/docs/playbook-stress-chaos-wave1.md) for the bounded runtime-chaos degraded-lane and re-entry landing.
- Read the [Agon mechanic](../mechanics/agon/README.md), [trial playbooks part](../mechanics/agon/parts/trial-playbooks/docs/agon-trial-playbooks.md), [mechanical trial model](../mechanics/agon/parts/trial-playbooks/docs/agon-mechanical-trial-model.md), [trial choreography boundary](../mechanics/agon/parts/trial-playbooks/docs/agon-trial-choreography-boundary.md), [assistant service boundary](../mechanics/agon/parts/trial-playbooks/docs/agon-trial-assistant-service-boundary.md), [owner handoffs](../mechanics/agon/parts/trial-playbooks/docs/agon-trial-owner-handoffs.md), and [Wave VI landing](../mechanics/agon/parts/trial-playbooks/docs/agon-wave6-playbook-landing.md) for the Wave VI pre-protocol Agon trial family.
- Read [PLAYBOOK_COMPOSITION_GATES](../mechanics/scenario-composition/parts/composition-surfaces/docs/playbook-composition-gates.md) for the composition promotion gate surface.
- Read [PLAYBOOK_GAP_MATRIX](../mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-gap-matrix.md) for the current prioritized lifecycle posture of the portfolio.
- Read [decisions](decisions/README.md) when a route, topology, owner split, or generated-index choice needs durable rationale.
- Read [RELEASING](RELEASING.md) for the bounded repo-level release flow.
- Open [../playbooks/continuity/checkpoint/self-agent-checkpoint-rollout/PLAYBOOK.md](../playbooks/continuity/checkpoint/self-agent-checkpoint-rollout/PLAYBOOK.md) for the first real playbook object, [../playbooks/continuity/session-growth/session-growth-cycle/PLAYBOOK.md](../playbooks/continuity/session-growth/session-growth-cycle/PLAYBOOK.md) for the recurring lineage-aware growth route, [../playbooks/continuity/session-growth/owner-followthrough-campaign/PLAYBOOK.md](../playbooks/continuity/session-growth/owner-followthrough-campaign/PLAYBOOK.md) for the narrower post-candidate owner follow-through route, [AOA-P-0027 reviewed-automation-followthrough](../playbooks/operations/release/reviewed-automation-followthrough/PLAYBOOK.md) for the automation-specific bridge between a reviewed route and any broader playbook-owned seed claim, [AOA-P-0028 trusted-rollout-operations](../playbooks/operations/release/trusted-rollout-operations/PLAYBOOK.md) for the sovereign shared-root Codex rollout operations route, [AOA-P-0029 self-agency-continuity-cycle](../playbooks/continuity/session-growth/self-agency-continuity-cycle/PLAYBOOK.md) for the long-arc continuity route with bounded revision and explicit reanchor, [AOA-P-0030 component-refresh-cycle](../playbooks/continuity/session-growth/component-refresh-cycle/PLAYBOOK.md) for the owner-law internal refresh route with bounded follow-through, [AOA-P-0031 a2a-summon-return-checkpoint](../playbooks/continuity/checkpoint/a2a-summon-return-checkpoint/PLAYBOOK.md) for the reviewed summon child-return checkpoint route, [AOA-P-0032 runtime-chaos-recovery](../playbooks/operations/recovery/runtime-chaos-recovery/PLAYBOOK.md) for the bounded degraded-lane and re-entry route, [AOA-P-0033 agon-broken-trace-trial](../playbooks/agon/trials/agon-broken-trace-trial/PLAYBOOK.md) and [AOA-P-0039 agon-expensive-summon-intent-trial](../playbooks/agon/trials/agon-expensive-summon-intent-trial/PLAYBOOK.md) for the first bounded Agon trial choreography family, and [AOA-PB-D-0001](decisions/AOA-PB-D-0001-trusted-rollout-operations-extraction.md) for one neighboring sovereign-boundary example.
- Read [ROADMAP](../ROADMAP.md) for the current direction.

## Docs in this repository

- [PLAYBOOK_MODEL](../mechanics/portfolio-governance/parts/model-spine/docs/playbook-model.md) - what the playbook layer is for
- [../DESIGN](../DESIGN.md) - the system form of the playbook layer
- [../DESIGN.AGENTS](../DESIGN.AGENTS.md) - the design form of the agent-facing route mesh
- [../mechanics](../mechanics/README.md) - the mechanics atlas for head-fed and
  local playbook mechanics, placement rules, legacy naming posture, and active
  package routes under `mechanics/*/`
- [BOUNDARIES](BOUNDARIES.md) - what the playbook layer owns and must not absorb
- [PLAYBOOK_BUNDLE_CONTRACT](../mechanics/activation/parts/activation-surface/docs/playbook-bundle-contract.md) - how authored `PLAYBOOK.md` bundles stay compact, registry-aligned, and federation-checkable where needed
- [PLAYBOOK_EXECUTION_SEAM](../mechanics/activation/parts/activation-surface/docs/playbook-execution-seam.md) - how derived activation, federation, and composition surfaces stay readable without becoming second authored sources
- [PLAYBOOK_OPERATIONAL_FAMILY](../mechanics/portfolio-governance/parts/operational-family/docs/playbook-operational-family.md) - how the operational playbook family stays differentiated instead of semantically overlapping
- [HANDOFF_CONTRACTS](../mechanics/scenario-composition/parts/composition-surfaces/docs/handoff-contracts.md) - how derived playbook handoff packets point to `aoa-skills` without absorbing skill meaning
- [FAILURE_RECOVERY](../mechanics/scenario-composition/parts/composition-surfaces/docs/failure-recovery.md) - how a shared failure catalog stays scenario-owned without becoming a persisted run engine
- [SUBAGENT_PATTERNS](../mechanics/scenario-composition/parts/composition-surfaces/docs/subagent-patterns.md) - how explicit subagent recipes stay bounded and example-shaped
- [AUTOMATION_SEEDS](../mechanics/scenario-composition/parts/composition-surfaces/docs/automation-seeds.md) - how automation prompt seeds stay illustrative rather than authoritative schedules
- [PLAYBOOK_RECURRENCE_DISCIPLINE](../mechanics/recurrence/parts/recurrence-discipline/docs/playbook-recurrence-discipline.md) - how scenario routes return to valid anchors without turning the playbook layer into runtime machinery
- [PLAYBOOK_LIFECYCLE](../mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-lifecycle.md) - how playbooks graduate from registry rows to authored and federation-checked forms
- [PLAYBOOK_PORTFOLIO](../mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-portfolio.md) - how the playbook layer stays broad enough across scenario families without overfitting
- [PLAYBOOK_REAL_RUN_WORKFLOW](../mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/playbook-real-run-workflow.md) - how real operational runs become reviewed summaries and explicit gate verdicts without creating a runtime log layer
- [PLAYBOOK_REAL_RUN_HARVEST](../mechanics/real-run-harvest/parts/harvest-template-source-store/docs/playbook-real-run-harvest.md) - how reviewable real-run evidence stays distinct from runtime state and from composition promotion itself
- [Codex-plane rollout cycle](../mechanics/release-support/parts/promotion-and-retention/docs/codex-plane-rollout-cycle.md) - how the shared-root Codex-plane deployment continuity lane stays a companion route under `AOA-P-0028`
- [Trusted rollout campaign cadence](../mechanics/release-support/parts/promotion-and-retention/docs/trusted-rollout-campaign-cadence.md) - how grouped rollout campaign cadence stays an adjunct under `AOA-P-0028` instead of a new sovereign playbook
- [stress lanes](../mechanics/antifragility/parts/stress-lanes/docs/playbook-stress-lanes.md) - how recurring playbooks expose a weaker, reviewable degraded lane without replacing source-owned receipts or proof
- [stress harvest](../mechanics/antifragility/parts/stress-harvest/docs/playbook-stress-harvest.md) - how stressed runs harvest bounded evidence and explicit re-entry gates without seizing ownership of what happened
- [runtime chaos wave 1](../mechanics/antifragility/parts/runtime-chaos-wave1/docs/playbook-stress-chaos-wave1.md) - how the runtime-chaos degraded-lane wave lands bounded stress lanes and gates without absorbing runtime, KAG, or eval ownership
- [Agon mechanic](../mechanics/agon/README.md) - how Agon trial, kernel-binding, campaign, adoption, and recurrence-adapter payloads stay package-local while source playbooks stay in `playbooks/`
- [Agon trial playbooks](../mechanics/agon/parts/trial-playbooks/docs/agon-trial-playbooks.md) - how the Wave VI Agon trial family stays playbook-owned, recurring, and pre-protocol
- [Agon mechanical trial model](../mechanics/agon/parts/trial-playbooks/docs/agon-mechanical-trial-model.md) - how mechanical trial rehearsal differs from live arena protocol
- [Agon trial choreography boundary](../mechanics/agon/parts/trial-playbooks/docs/agon-trial-choreography-boundary.md) - how trial choreography stays below arena sovereignty
- [Agon trial assistant service boundary](../mechanics/agon/parts/trial-playbooks/docs/agon-trial-assistant-service-boundary.md) - how assistants may support trials without becoming hidden contestants
- [Agon trial owner handoffs](../mechanics/agon/parts/trial-playbooks/docs/agon-trial-owner-handoffs.md) - how future eval, memo, routing, stats, skill, and technique handoffs stay explicit
- [Agon Wave VI landing](../mechanics/agon/parts/trial-playbooks/docs/agon-wave6-playbook-landing.md) - the bounded Wave VI landing order and verify path
- [PLAYBOOK_COMPOSITION_GATES](../mechanics/scenario-composition/parts/composition-surfaces/docs/playbook-composition-gates.md) - how `AOA-P-0017`, `AOA-P-0018`, `AOA-P-0019`, `AOA-P-0020`, `AOA-P-0021`, `AOA-P-0023`, `AOA-P-0024`, and `AOA-P-0028` use explicit gate review before composition grows
- [PLAYBOOK_GAP_MATRIX](../mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-gap-matrix.md) - the current prioritized lifecycle matrix and next bounded portfolio moves
- [decisions](decisions/README.md) - durable rationale and generated lookup indexes for playbook route choices
- [RELEASING](RELEASING.md) - how repo-level releases stay small, validated, and honest about remaining evidence gaps

## Notes

This repository should stay bounded.
Reviewed summaries may enter this repository under `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`, but composition changes still require explicit gate review under `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`.
If a document starts trying to become a technique corpus, workflow corpus, proof corpus, memory store, or routing surface, it probably belongs in a neighboring AoA repository instead.
