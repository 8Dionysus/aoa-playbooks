# Playbook Model

This document defines the conceptual model of the AoA playbook layer.

## Why a playbook layer exists

AoA needs more than reusable practice, bounded execution, bounded proof, memory, routing, and explicit agents.
It also needs reusable scenario-level operating forms.

The playbook layer exists to make recurring scenario recipes explicit rather than leaving them scattered across notes, prompts, and one-off orchestration behavior.

## What counts as a playbook here

Within `aoa-playbooks`, a playbook should mean a reusable scenario-level composition described through surfaces such as:
- scenario contract
- trigger posture
- prerequisites
- participating agent roles
- required skill families
- evaluation posture
- memory posture
- fallback or rollback posture
- expected artifact posture

## Playbook classes

The first useful distinction is between scenario archetypes such as:

### Repo bootstrap

A playbook for establishing a new repository layer or project surface with bounded scaffolding, docs, validation, and contributor guidance.

### Safe change rollout

A playbook for bounded changes where validation, handoff, rollback, and review posture matter.

### Bounded research pass

A playbook for constrained exploration where questions, synthesis, and next-step artifacts should stay explicit.

### Release prep

A playbook for preparing a repository or layer for merge or release with clear checks and outputs.

### Memory curation pass

A playbook for turning scattered memory inputs into bounded curated memory outputs without confusing curation with proof.

## What a playbook must not do

A playbook profile should not silently become:
- a single skill bundle
- a proof surface
- a routing layer
- a memory store

A playbook may coordinate all of those layers, but does not replace them.

## Playbook posture

A good playbook should make it easier to answer:
- what recurring situation is this for?
- when should it trigger?
- who participates?
- what skills are usually composed?
- what evidence or evaluation posture is expected?
- what fallback path exists if the scenario goes wrong?
- what artifacts should exist at the end?

## Relationship to neighboring layers

- `aoa-techniques` stores reusable practice
- `aoa-skills` stores bounded execution
- `aoa-evals` stores bounded proof
- `aoa-routing` stores navigation and dispatch
- `aoa-memo` stores memory and recall surfaces
- `aoa-agents` stores reusable role-bearing actors
- `aoa-playbooks` stores reusable scenario-level compositions

## Compact principle

The playbook layer should make recurring scenarios explicit without turning operations into theater.
