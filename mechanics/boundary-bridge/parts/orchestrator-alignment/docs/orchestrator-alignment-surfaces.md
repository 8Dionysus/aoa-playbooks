# Orchestrator Alignment Surfaces

## Purpose

This note defines how orchestrator-facing quest families align with `aoa-playbooks` without turning playbooks into class identity or runtime state.

Orchestrator class identity lives in `aoa-agents`.
This repository only names which playbook families and route artifacts each class may consume.

## Router

The `router` class may consume:

- activation surfaces from `generated/playbook_activation_surfaces.min.json`
- federation and advisory selection surfaces from `generated/playbook_federation_surfaces.min.json`
- bounded route-selection notes that help choose the next source of truth

Router alignment stays selection-shaped.
It does not mutate route canon and does not become a hidden playbook runner.

## Review

The `review` class may consume:

- reviewed-run packet contracts from `generated/playbook_review_packet_contracts.min.json`
- readiness and review-status surfaces from `generated/playbook_review_status.min.json`
- real-run and readiness summaries that close a route honestly

Review alignment stays closure-shaped.
It does not replace proof surfaces from `aoa-evals`.

## Bounded execution

The `bounded_execution` class may consume:

- bounded route cards from `generated/playbook_registry.min.json`
- artifact intake and route handoff surfaces from `generated/playbook_review_intake.min.json`
- explicit route artifact lists and stop conditions

Bounded execution alignment stays smallest-step-shaped.
It does not widen a route beyond the named playbook contract.

## Boundary rule

Playbooks remain route canon.
Quests may point at playbook families, but they must not redefine orchestrator identity or turn playbook evidence into runtime state.
