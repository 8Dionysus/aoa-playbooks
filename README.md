# aoa-playbooks

`aoa-playbooks` is the scenario and composition layer of the AoA ecosystem.

It exists to make recurring operational recipes explicit, reviewable, and reusable.

This repository is not the main home of reusable techniques, skill bundles, proof bundles, or memory objects.
Its role is different: it should define scenario-shaped operating recipes that compose skills, agents, evaluation posture, memory posture, and fallback paths for recurring situations.

## Start here

If you are new to this repository, use this path:

1. Read [CHARTER](CHARTER.md) for the role and boundaries of the playbook layer.
2. Read [docs/PLAYBOOK_MODEL](docs/PLAYBOOK_MODEL.md) for the conceptual model.
3. Read [docs/BOUNDARIES](docs/BOUNDARIES.md) for ownership rules.
4. Read [docs/PLAYBOOK_BUNDLE_CONTRACT](docs/PLAYBOOK_BUNDLE_CONTRACT.md) for the authored bundle contract.
5. Open [playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md](playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md) for the first checkpoint-method playbook object.
6. Open [playbooks/witness-to-compost-pilot/PLAYBOOK.md](playbooks/witness-to-compost-pilot/PLAYBOOK.md) for the witness/compost pilot route.
7. Read [ROADMAP](ROADMAP.md) for the current direction.

## What this repository is for

`aoa-playbooks` should own playbook-layer meaning about:
- recurring operational scenarios
- multi-step compositions of skills
- scenario-level methods once a route spans skills, roles, memory posture, and proof posture
- role-aware handoff patterns
- decision points and fallback paths
- expected evidence and validation posture
- compact playbook registries and validation

## What this repository is not for

This repository should not become the main home for:
- reusable techniques
- single bounded skill bundles
- eval bundles
- routing surfaces
- memory objects
- infrastructure implementation details
- giant prompt scripts pretending to be operations

A playbook is not a skill.
A skill is a bounded workflow.
A playbook is a higher-level scenario recipe that coordinates multiple surfaces.

When a route becomes a recurring cross-layer method, it belongs here rather than being smeared across skills, notes, and ad hoc orchestration.

## Relationship to the AoA federation

Within AoA:
- `aoa-techniques` owns practice meaning
- `aoa-skills` owns execution meaning
- `aoa-evals` owns bounded proof meaning
- `aoa-routing` should own dispatch and navigation surfaces
- `aoa-memo` should own memory and recall meaning
- `aoa-agents` should own role and persona meaning
- `aoa-playbooks` should own scenario-level compositions

## Local validation

This repository includes a compact machine-readable playbook-layer registry at:
- `generated/playbook_registry.min.json`

It now also includes authored playbook bundles at:
- `playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md`
- `playbooks/witness-to-compost-pilot/PLAYBOOK.md`

The validator auto-discovers authored bundles under `playbooks/*/PLAYBOOK.md` and checks that each one stays aligned with the registry surface.

To validate the current playbook-layer surface locally, run:

```bash
python scripts/validate_playbooks.py
```

## Current status

`aoa-playbooks` is in bootstrap with authored playbook bundles for checkpoint work and the witness/compost pilot.
The current goal is to keep the playbook layer compact while giving scenario-level method one real source-owned home.

## Principles

- recurring scenarios should be explicit rather than folkloric
- playbooks should stay bounded and reviewable
- fallback and rollback posture should be named, not implied
- evaluation posture should be visible, not retrofitted later
- the playbook layer should not swallow neighboring AoA layers

## License

Apache-2.0
