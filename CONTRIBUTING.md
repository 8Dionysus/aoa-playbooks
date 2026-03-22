# Contributing to aoa-playbooks

Thank you for helping shape the AoA playbook layer.

This repository is the scenario and composition layer of AoA.
Contributions here should improve the clarity, coherence, and usefulness of recurring scenario recipes rather than turning this repository into a pile of prompts or orchestration folklore.

## What belongs here

Good contributions include:
- playbook layer definitions
- reusable scenario recipes
- trigger and prerequisite guidance
- fallback and rollback posture guidance
- expected artifact posture
- compact playbook registries, schemas, and validation
- clearer boundaries between scenario composition, execution, proof, memory, and routing

## What usually does not belong here

Do not use this repository as the default home for:
- new technique bundles
- new skill bundles
- new eval bundles
- routing surfaces
- memory objects
- infrastructure implementation details
- giant prompt payloads with no reusable scenario contract

If a change mainly defines reusable practice, bounded execution, or bounded proof, prefer the specialized neighboring repository first.

## Source-of-truth discipline

When contributing, preserve this rule:
- `aoa-playbooks` owns scenario-level composition meaning
- neighboring AoA repositories still own their own meaning

Examples:
- `aoa-techniques` owns practice meaning
- `aoa-skills` owns execution meaning
- `aoa-evals` owns proof meaning
- `aoa-routing` owns navigation surfaces
- `aoa-memo` owns memory meaning
- `aoa-agents` owns role and persona meaning

## How to decide where a change belongs

Ask these questions in order:

1. Is this change mainly about a recurring scenario recipe, fallback path, or scenario-level composition?
   - If yes, it may belong here.
2. Is this change mainly about reusable practice?
   - If yes, it probably belongs in `aoa-techniques`.
3. Is this change mainly about bounded execution?
   - If yes, it probably belongs in `aoa-skills`.
4. Is this change mainly about bounded proof?
   - If yes, it probably belongs in `aoa-evals`.
5. Is this change mainly about memory objects or recall truth?
   - If yes, it probably belongs in `aoa-memo`.
6. Is this change mainly about actor roles or posture?
   - If yes, it probably belongs in `aoa-agents`.
7. Is this change mainly about dispatch across repos?
   - If yes, it probably belongs in `aoa-routing`.

## Pull request shape

A strong pull request in this repository should explain:
- what playbook-layer surface changed
- why the change belongs in `aoa-playbooks`
- what neighboring AoA layers are affected
- what was intentionally not absorbed into this repository

## Style guidance

Prefer:
- compactness over scenario sprawl
- explicit fallback over magical recovery
- reviewable playbooks over hidden orchestration scripts
- bounded scenario contracts over overloaded operational mythology
