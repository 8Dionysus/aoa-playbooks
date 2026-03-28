# AoA Playbooks Roadmap

This roadmap tracks the bootstrap and early shaping of the AoA playbook layer.

## Current phase

`aoa-playbooks` has reached its `v0.1.0` public baseline.
The immediate goal is no longer to prove that the repository can exist.
The next goal is to keep the layer honest through evidence-led maturation:
- preserve the current authored, activation, federation, and composition seams without widening them casually
- wait for real cutover evidence for `AOA-P-0019`
- wait for live incident evidence for `AOA-P-0020`
- prefer steady-state maintenance over catalog expansion unless a clearly distinct scenario family appears

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
