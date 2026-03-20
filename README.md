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
4. Read [ROADMAP](ROADMAP.md) for the current direction.

For the shortest next route by intent:
- if you need the ecosystem center and layer map, go to [`Agents-of-Abyss`](https://github.com/8Dionysus/Agents-of-Abyss)
- if you need bounded execution workflows rather than scenario compositions, go to [`aoa-skills`](https://github.com/8Dionysus/aoa-skills)
- if you need portable proof surfaces rather than operating recipes, go to [`aoa-evals`](https://github.com/8Dionysus/aoa-evals)
- if you need explicit role contracts and handoff posture, go to [`aoa-agents`](https://github.com/8Dionysus/aoa-agents)
- if you need memory and recall meaning, go to [`aoa-memo`](https://github.com/8Dionysus/aoa-memo)

## Quick route table

| repository | owns | go here when |
|---|---|---|
| `aoa-playbooks` | recurring operational scenarios, multi-step compositions, fallback paths, expected evidence posture | you need scenario recipes that coordinate multiple surfaces |
| `Agents-of-Abyss` | ecosystem identity, layer map, federation rules, program-level direction | you need the center and the constitutional view of AoA |
| `aoa-skills` | bounded agent-facing execution workflows | you need one workflow rather than a higher-level scenario composition |
| `aoa-evals` | portable proof surfaces for bounded claims | you need evaluation and quality checks rather than operating recipes |
| `aoa-agents` | role contracts, persona boundaries, handoff posture | you need actor-level contracts within or around a playbook |
| `aoa-memo` | memory objects, recall surfaces, provenance threads | you need memory-layer meaning rather than scenario composition |

## What this repository is for

`aoa-playbooks` should own playbook-layer meaning about:
- recurring operational scenarios
- multi-step compositions of skills
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
- giant script archives pretending to be operations

A playbook is not a skill.
A skill is a bounded workflow.
A playbook is a higher-level scenario recipe that coordinates multiple surfaces.

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

To validate the current playbook-layer surface locally, run:

```bash
python scripts/validate_playbooks.py
```

## Current status

`aoa-playbooks` is in bootstrap.
The goal of this first public baseline is to define the role, boundaries, and first machine-readable playbook-layer surface without overbuilding orchestration too early.

## Principles

- recurring scenarios should be explicit rather than folkloric
- playbooks should stay bounded and reviewable
- fallback and rollback posture should be named, not implied
- evaluation posture should be visible, not retrofitted later
- the playbook layer should not swallow neighboring AoA layers

## License

Apache-2.0
