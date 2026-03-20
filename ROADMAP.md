# AoA Playbooks Roadmap

This roadmap tracks the bootstrap and early shaping of the AoA playbook layer.

## Current phase

`aoa-playbooks` is in bootstrap.
The current goal is not to build a giant orchestration engine immediately.
The goal is to define what the playbook layer is for, what it owns, and what it must not silently absorb.

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

## Phase 3: posture and fallback surfaces

Goals:
- make trigger posture explicit
- make prerequisite posture explicit
- make fallback and rollback posture explicit
- make expected artifact posture explicit

## Phase 4: composition discipline

Goals:
- define bounded multi-surface composition hints
- clarify when a playbook is mainly skill-driven, agent-driven, or proof-heavy
- avoid turning the playbook layer into hidden orchestration runtime too early

## Phase 5: federation integration

Goals:
- connect `aoa-playbooks` cleanly to `aoa-skills`
- connect participating role posture to `aoa-agents`
- connect expected proof posture to `aoa-evals`
- connect expected memory posture to `aoa-memo`
- preserve clear boundaries relative to `aoa-routing`

## Standing discipline

Across all phases:
- keep scenarios explicit
- keep playbooks compact
- keep fallback posture reviewable
- do not confuse scenario composition with execution, proof, memory, or routing
