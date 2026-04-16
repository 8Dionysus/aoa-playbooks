# AoA Playbooks Roadmap

This roadmap tracks the playbook layer from its public baseline into its
current `v0.3.1` portfolio-hardening phase.

## Current phase

`aoa-playbooks` established its `v0.3.1` public contour and has moved well
beyond the bootstrap question.
The immediate goal is no longer to prove that the repository can exist.
The next goal is to keep the current portfolio honest through boundary repair,
reviewed evidence, and maintenance discipline:
- preserve the current authored, activation, federation, review-status, landing-governance, and composition seams without widening them casually
- keep `AOA-P-0025 session-growth-cycle`, `AOA-P-0026 owner-followthrough-campaign`, `AOA-P-0027 reviewed-automation-followthrough`, `AOA-P-0028 trusted-rollout-operations`, `AOA-P-0029 self-agency-continuity-cycle`, `AOA-P-0030 component-refresh-cycle`, `AOA-P-0031 a2a-summon-return-checkpoint`, and `AOA-P-0032 runtime-chaos-recovery` aligned with their authored docs, generated surfaces, and reviewed evidence
- keep `docs/CODEX_PLANE_ROLLOUT_CYCLE.md` as the companion lane to `AOA-P-0028` rather than a second sovereign playbook
- keep questline, campaign, and `QUESTBOOK.md` adjunct posture evidence-first and bounded
- treat `AOA-P-0019` and `AOA-P-0020` as evidence-gated operational routes rather than the sole frontier of the repository
- prefer steady-state maintenance, portfolio hardening, and reviewed evidence over catalog expansion unless a clearly distinct scenario family appears

## Current published contour

The currently published playbook canon already includes:
- baseline public routes `AOA-P-0001` through `AOA-P-0005`
- the current growth, follow-through, shared-root rollout, continuity, component-refresh, A2A summon-return, and runtime-chaos routes `AOA-P-0025 session-growth-cycle`, `AOA-P-0026 owner-followthrough-campaign`, `AOA-P-0027 reviewed-automation-followthrough`, `AOA-P-0028 trusted-rollout-operations`, `AOA-P-0029 self-agency-continuity-cycle`, `AOA-P-0030 component-refresh-cycle`, `AOA-P-0031 a2a-summon-return-checkpoint`, and `AOA-P-0032 runtime-chaos-recovery`
- generated coordination surfaces such as `generated/playbook_activation_surfaces.min.json`, `generated/playbook_federation_surfaces.min.json`, `generated/playbook_review_status.min.json`, `generated/playbook_review_intake.min.json`, `generated/playbook_review_packet_contracts.min.json`, and `generated/playbook_landing_governance.min.json`
- generated composition adjuncts such as `generated/playbook_handoff_contracts.json`, `generated/playbook_failure_catalog.json`, `generated/playbook_automation_seeds.json`, and `generated/playbook_subagent_recipes.json`

The near-term roadmap should therefore read the repository as a portfolio
hardening pass, not as an early shaping pass waiting only on cutover or
incident proof.

## Phase 1: playbook layer definition

Goals:
- define `aoa-playbooks` as the canonical scenario and composition layer within AoA
- make the distinction between playbook, skill, proof, memory, routing, and agent explicit
- establish a compact playbook registry and a minimal validator

Exit signals:
- the repository role is clear
- playbook-layer boundaries are documented
- a compact machine-readable registry exists

## Phase 2: first playbook discipline

Goals:
- define the first public shape for playbook profiles
- distinguish recurring scenarios such as repo bootstrap, safe change rollout, bounded research pass, release prep, and memory curation
- keep playbook forms compact enough to review
- introduce the first authored `PLAYBOOK.md` without turning the layer into a workflow dump

## Phase 3: posture and fallback surfaces

Goals:
- make trigger posture explicit
- make prerequisite posture explicit
- make fallback and rollback posture explicit
- make return posture explicit for long-horizon, restartable, and cross-boundary scenarios
- make expected artifact posture explicit

## Phase 4: composition discipline

Goals:
- define bounded multi-surface composition hints
- clarify when a playbook is mainly skill-driven, agent-driven, or proof-heavy
- avoid turning the playbook layer into hidden orchestration runtime too early
- keep recurrence compact and scenario-owned without growing a hidden orchestration engine
- make scenario-level method readable as an authored object rather than only a registry row

## Phase 5: federation integration

Goals:
- connect `aoa-playbooks` cleanly to `aoa-skills`
- connect participating role posture to `aoa-agents`
- connect expected proof posture to `aoa-evals`
- connect expected memory posture to `aoa-memo`
- preserve clear boundaries relative to `aoa-routing`
- let the runtime-facing cohort publish flat memo-read defaults without turning the playbook layer into recall search or routing ownership

## Phase 6: growth governance

Goals:
- define the playbook lifecycle from registry-only to federation-checked
- define when a scenario deserves an authored `PLAYBOOK.md`
- define when a scenario deserves a derived activation surface
- keep a visible portfolio matrix so new playbooks add distinct scenario coverage
- prevent the playbook layer from overfitting to one route family

Exit signals:
- lifecycle and graduation doctrine is documented
- portfolio coverage guidance is documented
- the repo can explain why a scenario is added, refined, or left in registry-only form

## Standing discipline

Across all phases:
- keep scenarios explicit
- keep playbooks compact
- keep fallback posture reviewable
- do not confuse scenario composition with execution, proof, memory, or routing
