# aoa-playbooks

`aoa-playbooks` is the scenario and composition layer of the AoA ecosystem.

It exists to make recurring operational recipes explicit, reviewable, and reusable. A playbook is not a skill. A skill is a bounded workflow. A playbook coordinates multiple surfaces, handoffs, fallbacks, and evidence expectations across a recurring scenario.

> Current release: `v0.3.3`. See [CHANGELOG](CHANGELOG.md) for release notes.

## Start here

Use the shortest route by need:

- docs map: [docs/README](docs/README.md)
- role, boundaries, and conceptual model: [CHARTER](CHARTER.md), [playbook model](mechanics/portfolio-governance/parts/model-spine/docs/playbook-model.md), and [docs/BOUNDARIES](docs/BOUNDARIES.md)
- root system and agent-route design: [DESIGN](DESIGN.md) and [DESIGN.AGENTS](DESIGN.AGENTS.md)
- playbook-local statistical questions and reference packets: [stats port](stats/README.md)
- repeatable operation topology: [mechanics atlas](mechanics/README.md),
  [activation mechanic](mechanics/activation/README.md),
  [scenario composition mechanic](mechanics/scenario-composition/README.md),
  [federation closure mechanic](mechanics/federation-closure/README.md),
  [review gate mechanic](mechanics/review-gate/README.md),
  [real-run harvest mechanic](mechanics/real-run-harvest/README.md),
  [antifragility mechanic](mechanics/antifragility/README.md),
  [Agon mechanic](mechanics/agon/README.md),
  [recurrence mechanic](mechanics/recurrence/README.md),
  [checkpoint mechanic](mechanics/checkpoint/README.md),
  [Experience mechanic](mechanics/experience/README.md),
  [release-support mechanic](mechanics/release-support/README.md),
  [questbook mechanic](mechanics/questbook/README.md),
  [RPG mechanic](mechanics/rpg/README.md),
  [Titan mechanic](mechanics/titan/README.md),
  and [portfolio governance mechanic](mechanics/portfolio-governance/README.md)
- authored bundle and activation seam: [activation bundle contract](mechanics/activation/parts/activation-surface/docs/playbook-bundle-contract.md), [activation execution seam](mechanics/activation/parts/activation-surface/docs/playbook-execution-seam.md), [operational family](mechanics/portfolio-governance/parts/operational-family/docs/playbook-operational-family.md), [recurrence discipline](mechanics/recurrence/parts/recurrence-discipline/docs/playbook-recurrence-discipline.md), [playbook lifecycle](mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-lifecycle.md), and [playbook portfolio](mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-portfolio.md)
- evidence, gates, and release posture: [real-run workflow](mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/playbook-real-run-workflow.md), [real-run harvest](mechanics/real-run-harvest/parts/harvest-template-source-store/docs/playbook-real-run-harvest.md), [composition gates](mechanics/scenario-composition/parts/composition-surfaces/docs/playbook-composition-gates.md), [gap matrix](mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-gap-matrix.md), and [docs/RELEASING](docs/RELEASING.md)
- sovereign shared-root rollout route plus companion lane: [playbooks/operations/release/trusted-rollout-operations/PLAYBOOK.md](playbooks/operations/release/trusted-rollout-operations/PLAYBOOK.md), [codex-plane rollout cycle](mechanics/release-support/parts/promotion-and-retention/docs/codex-plane-rollout-cycle.md), [trusted rollout cadence](mechanics/release-support/parts/promotion-and-retention/docs/trusted-rollout-campaign-cadence.md), and [mechanics/release-support/parts/promotion-and-retention/examples/codex_plane_rollout_lane.example.json](mechanics/release-support/parts/promotion-and-retention/examples/codex_plane_rollout_lane.example.json)
- long-arc continuity and explicit reanchor route: [AOA-P-0029 self-agency-continuity-cycle](playbooks/continuity/session-growth/self-agency-continuity-cycle/PLAYBOOK.md)
- owner-law component refresh route without scheduler authority: [AOA-P-0030 component-refresh-cycle](playbooks/continuity/session-growth/component-refresh-cycle/PLAYBOOK.md)
- A2A summon return checkpoint route without hidden child automation: [AOA-P-0031 a2a-summon-return-checkpoint](playbooks/continuity/checkpoint/a2a-summon-return-checkpoint/PLAYBOOK.md)
- runtime-chaos degraded lane and re-entry route: [AOA-P-0032 runtime-chaos-recovery](playbooks/operations/recovery/runtime-chaos-recovery/PLAYBOOK.md), [runtime chaos wave 1 part](mechanics/antifragility/parts/runtime-chaos-wave1/docs/playbook-stress-chaos-wave1.md), and [runtime timeout stress-lane example](mechanics/antifragility/parts/stress-lanes/examples/playbook_stress_lane.runtime-timeout-chaos.example.json)
- Agon pre-protocol mechanical trial family: [trial playbooks part](mechanics/agon/parts/trial-playbooks/docs/agon-trial-playbooks.md), [mechanical trial model](mechanics/agon/parts/trial-playbooks/docs/agon-mechanical-trial-model.md), [AOA-P-0033 agon-broken-trace-trial](playbooks/agon/trials/agon-broken-trace-trial/PLAYBOOK.md), [AOA-P-0039 agon-expensive-summon-intent-trial](playbooks/agon/trials/agon-expensive-summon-intent-trial/PLAYBOOK.md), and [generated/agon_trial_playbook_registry.min.json](generated/agon_trial_playbook_registry.min.json)
- additive stress-lane and re-entry doctrine: [stress lanes](mechanics/antifragility/parts/stress-lanes/docs/playbook-stress-lanes.md), [stress harvest](mechanics/antifragility/parts/stress-harvest/docs/playbook-stress-harvest.md), and [runtime chaos wave 1](mechanics/antifragility/parts/runtime-chaos-wave1/docs/playbook-stress-chaos-wave1.md)
- adjunct outline seam: [questline and campaign model](mechanics/questbook/parts/questline-outline/docs/questline-and-campaign-model.md)
- checkpoint distillation and closed-loop pilot: [checkpoint distillation closed-loop pilot](mechanics/checkpoint/parts/distillation-closed-loop/docs/checkpoint-distillation-closed-loop-pilot.md)
- checkpoint closeout owner routing: [AOA-P-0050 checkpoint-closeout-owner-route](playbooks/continuity/checkpoint/checkpoint-closeout-owner-route/PLAYBOOK.md)
- Titan live session drill and route ecology: [Titan live session drill route](mechanics/titan/parts/drill-and-ecology/docs/titan-live-session-drill-route.md) and [Titan route ecology playbook](mechanics/titan/parts/drill-and-ecology/docs/titan-route-ecology-playbook.md)
- live authored examples: [playbooks/continuity/checkpoint/self-agent-checkpoint-rollout/PLAYBOOK.md](playbooks/continuity/checkpoint/self-agent-checkpoint-rollout/PLAYBOOK.md), [playbooks/continuity/session-growth/witness-to-compost-pilot/PLAYBOOK.md](playbooks/continuity/session-growth/witness-to-compost-pilot/PLAYBOOK.md), [playbooks/continuity/session-growth/session-growth-cycle/PLAYBOOK.md](playbooks/continuity/session-growth/session-growth-cycle/PLAYBOOK.md), [playbooks/continuity/session-growth/owner-followthrough-campaign/PLAYBOOK.md](playbooks/continuity/session-growth/owner-followthrough-campaign/PLAYBOOK.md), [AOA-P-0027 reviewed-automation-followthrough](playbooks/operations/release/reviewed-automation-followthrough/PLAYBOOK.md), [AOA-P-0028 trusted-rollout-operations](playbooks/operations/release/trusted-rollout-operations/PLAYBOOK.md), [AOA-P-0029 self-agency-continuity-cycle](playbooks/continuity/session-growth/self-agency-continuity-cycle/PLAYBOOK.md), [AOA-P-0030 component-refresh-cycle](playbooks/continuity/session-growth/component-refresh-cycle/PLAYBOOK.md), [AOA-P-0031 a2a-summon-return-checkpoint](playbooks/continuity/checkpoint/a2a-summon-return-checkpoint/PLAYBOOK.md), [AOA-P-0032 runtime-chaos-recovery](playbooks/operations/recovery/runtime-chaos-recovery/PLAYBOOK.md), and the Wave VI Agon cohort under `playbooks/agon/*/agon-*/PLAYBOOK.md`
- current direction: [ROADMAP](ROADMAP.md)

## Route by need

- source-authored playbook truth: `playbooks/*/*/*/PLAYBOOK.md` for scenario routes and `generated/playbook_registry.min.json` for compact registry metadata
- root system design and agent-facing route mesh: `DESIGN.md`, `DESIGN.AGENTS.md`, `AGENTS.md`, and the nearest nested `AGENTS.md`
- playbook-local statistical questions and evidence-linked reference packets: `stats/README.md` and `stats/port.manifest.json`; shared measurement grammar and cross-owner composition remain in `aoa-stats`
- mechanics atlas and package routes: `mechanics/README.md`, `mechanics/AGENTS.md`, and active package READMEs under `mechanics/*/README.md`
- activation, federation, and review-governed landing surfaces: `generated/playbook_activation_surfaces.min.json`, `generated/playbook_federation_surfaces.min.json`, `generated/playbook_review_status.min.json`, `generated/playbook_review_intake.min.json`, `generated/playbook_review_packet_contracts.min.json`, and `generated/playbook_landing_governance.min.json`
- shared-root rollout operations route and companion lane: `playbooks/operations/release/trusted-rollout-operations/PLAYBOOK.md`, `mechanics/release-support/parts/promotion-and-retention/docs/codex-plane-rollout-cycle.md`, `mechanics/release-support/parts/promotion-and-retention/docs/trusted-rollout-campaign-cadence.md`, and `mechanics/release-support/parts/promotion-and-retention/examples/codex_plane_rollout_lane.example.json`
- long-arc continuity and explicit reanchor route: `playbooks/continuity/session-growth/self-agency-continuity-cycle/PLAYBOOK.md`
- owner-law component refresh route: `playbooks/continuity/session-growth/component-refresh-cycle/PLAYBOOK.md`
- A2A summon return checkpoint route: `playbooks/continuity/checkpoint/a2a-summon-return-checkpoint/PLAYBOOK.md`
- runtime-chaos degraded lane and re-entry route: `playbooks/operations/recovery/runtime-chaos-recovery/PLAYBOOK.md`, `mechanics/antifragility/parts/runtime-chaos-wave1/docs/playbook-stress-chaos-wave1.md`, and `mechanics/antifragility/parts/stress-lanes/examples/playbook_stress_lane.runtime-timeout-chaos.example.json`
- Titan live drill route and route ecology: `mechanics/titan/parts/drill-and-ecology/docs/titan-live-session-drill-route.md` and `mechanics/titan/parts/drill-and-ecology/docs/titan-route-ecology-playbook.md`
- Agon pre-protocol mechanical trial family: `mechanics/agon/README.md`, `mechanics/agon/parts/trial-playbooks/docs/agon-trial-playbooks.md`, `mechanics/agon/parts/trial-playbooks/docs/agon-mechanical-trial-model.md`, `mechanics/agon/parts/trial-playbooks/docs/agon-trial-choreography-boundary.md`, `mechanics/agon/parts/trial-playbooks/docs/agon-trial-assistant-service-boundary.md`, `mechanics/agon/parts/trial-playbooks/docs/agon-trial-owner-handoffs.md`, `mechanics/agon/parts/trial-playbooks/docs/agon-wave6-playbook-landing.md`, `playbooks/agon/*/agon-*/PLAYBOOK.md`, and `generated/agon_trial_playbook_registry.min.json`
- handoff, failure, automation, and subagent adjuncts: `generated/playbook_handoff_contracts.json`, `generated/playbook_failure_catalog.json`, `generated/playbook_automation_seeds.json`, `generated/playbook_subagent_recipes.json`, [handoff contracts](mechanics/scenario-composition/parts/composition-surfaces/docs/handoff-contracts.md), [failure recovery](mechanics/scenario-composition/parts/composition-surfaces/docs/failure-recovery.md), [automation seeds](mechanics/scenario-composition/parts/composition-surfaces/docs/automation-seeds.md), and [subagent patterns](mechanics/scenario-composition/parts/composition-surfaces/docs/subagent-patterns.md)
- additive stress-lane adjuncts: `mechanics/antifragility/parts/stress-lanes/schemas/playbook_stress_lane_v1.json`, `mechanics/antifragility/parts/reentry-gates/schemas/playbook_reentry_gate_v1.json`, `mechanics/antifragility/parts/stress-lanes/examples/playbook_stress_lane.example.json`, `mechanics/antifragility/parts/reentry-gates/examples/playbook_reentry_gate.example.json`, [stress lanes](mechanics/antifragility/parts/stress-lanes/docs/playbook-stress-lanes.md), and [stress harvest](mechanics/antifragility/parts/stress-harvest/docs/playbook-stress-harvest.md)
- via negativa pruning checklist: [via negativa part](mechanics/antifragility/parts/via-negativa/docs/via-negativa-checklist.md)
- real-run and gate-review evidence: `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`, `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests/`, [real-run workflow](mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/playbook-real-run-workflow.md), and [composition gates](mechanics/scenario-composition/parts/composition-surfaces/docs/playbook-composition-gates.md)
- owner-local live receipt publication for closeout/stats integration: `scripts/publish_live_receipts.py` and `.aoa/live_receipts/playbook-receipts.jsonl`
- live authored bundles and activation examples: `playbooks/*/*/*/PLAYBOOK.md` and `mechanics/activation/parts/activation-surface/examples/playbook_activation.*.example.json`
- full non-mutating verify path: the executable repository gate owned by
  `scripts/release_check.py`; focused routes live in the nearest `AGENTS.md`

## What `aoa-playbooks` owns

This repository is the source of truth for:

- recurring operational scenarios
- multi-step compositions across skills, roles, memory posture, and proof posture
- scenario-level handoff, fallback, rollback, and return posture
- expected evidence and validation posture for recurring routes
- compact playbook registries and derived playbook-owned composition surfaces

## What it does not own

Do not treat this repository as the main home for:

- reusable techniques
- single bounded skill bundles
- proof doctrine or verdict logic
- routing surfaces
- primary memory objects
- infrastructure implementation details
- giant prompt scripts pretending to be operations

When a route is really one bounded workflow, keep it in `aoa-skills` instead of inflating it into a playbook.

## Current public surfaces

The committed public surfaces group into four families:

- source-authored playbook canon: `playbooks/*/*/*/PLAYBOOK.md` for route meaning and `generated/playbook_registry.min.json` for compact registry metadata
- OS Abyss registry artifact identity: `generated/playbook_registry.min.json#/artifact_identity` and `docs/artifact-bundles/playbook_registry.bundle.json` define the ABI+SLSA bundle consumed by registry/latest readers
- Wave VI Agon trial registry and doctrine: `generated/agon_trial_playbook_registry.min.json`, `generated/agon_trial_kernel_binding_registry.min.json`, `generated/agon_campaign_playbook_registry.min.json`, and the package-local docs under `mechanics/agon/parts/`
- derived activation, federation, review-status, review-packet, review-intake, and landing-governance surfaces such as `generated/playbook_activation_surfaces.min.json`, `generated/playbook_federation_surfaces.min.json`, `generated/playbook_review_status.min.json`, `generated/playbook_review_packet_contracts.min.json`, `generated/playbook_review_intake.min.json`, and `generated/playbook_landing_governance.min.json`
- playbook-owned composition adjuncts such as `generated/playbook_handoff_contracts.json`, `generated/playbook_failure_catalog.json`, `generated/playbook_subagent_recipes.json`, `generated/playbook_automation_seeds.json`, and `generated/playbook_composition_manifest.json`
- bounded evidence and readiness adjuncts under `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`, `generated/phase_alpha_review_packets.min.json`, `generated/phase_alpha_run_matrix.min.json`, and `QUESTBOOK.md`

Real-run harvest templates under `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests/` and review notes under `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/` and `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/` stay bounded evidence surfaces. They do not turn this repository into a runtime log substrate.

## Go here when...

- you need a single bounded execution unit: [`aoa-skills`](https://github.com/8Dionysus/aoa-skills)
- you need role and handoff contracts: [`aoa-agents`](https://github.com/8Dionysus/aoa-agents)
- you need proof surfaces or evidence framing: [`aoa-evals`](https://github.com/8Dionysus/aoa-evals)
- you need explicit memory objects or recall posture: [`aoa-memo`](https://github.com/8Dionysus/aoa-memo)
- you need the smallest next object or dispatch hint: [`aoa-routing`](https://github.com/8Dionysus/aoa-routing)
- you need the ecosystem center and boundary doctrine: [`Agents-of-Abyss`](https://github.com/8Dionysus/Agents-of-Abyss)

## Build and validate

The executable repository-wide route is `scripts/release_check.py`. Focused
checks and their ordering live in the nearest `AGENTS.md`, so this public front
door does not duplicate command authority.

The validator auto-discovers authored bundles under `playbooks/*/*/*/PLAYBOOK.md`, checks registry alignment, resolves federation-facing references into neighboring repositories, and validates the review-governed experimental landing layer, the Wave VI Agon trial family, Phase Alpha, questbook, and local guidance surfaces including `playbooks/AGENTS.md` and `generated/AGENTS.md`.

## Current contour

`aoa-playbooks` is currently at `v0.3.3` and has moved beyond its initial public baseline. The current honest move is evidence-led maturation across reviewed continuity, Titan drills, Experience follow-through, and Agon trial/campaign surfaces while keeping mechanical trials experimental, pre-protocol, and choreography-only. Root design is now split between `DESIGN.md` for the playbook-layer system form and `DESIGN.AGENTS.md` for the agent-facing route mesh. The first `mechanics/` skeleton now separates head-fed mechanics from `Agents-of-Abyss` and local playbook-native mechanics, with placement/legacy gates and active packages proving package-local builder moves, payload moves, stronger-owner handoffs, and public generated/readout boundaries while preserving the right root entrypoints.

The runtime-facing extension stays intentionally bounded: selected playbooks may publish explicit memo-read defaults and activation-readable surfaces, but memo truth, routing ownership, and source skill meaning remain in their owning repositories.

Questline and campaign reflection also remains adjunct-only. It is a reviewed outline seam, not a runtime ledger or quest authority surface.

## License

Apache-2.0
