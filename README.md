# aoa-playbooks

`aoa-playbooks` is the scenario and composition layer of the AoA ecosystem.

It exists to make recurring operational recipes explicit, reviewable, and reusable. A playbook is not a skill. A skill is a bounded workflow. A playbook coordinates multiple surfaces, handoffs, fallbacks, and evidence expectations across a recurring scenario.

## Start here

Use the shortest route by need:

- role, boundaries, and conceptual model: [CHARTER](CHARTER.md), [docs/PLAYBOOK_MODEL](docs/PLAYBOOK_MODEL.md), and [docs/BOUNDARIES](docs/BOUNDARIES.md)
- authored bundle and activation seam: [docs/PLAYBOOK_BUNDLE_CONTRACT](docs/PLAYBOOK_BUNDLE_CONTRACT.md), [docs/PLAYBOOK_EXECUTION_SEAM](docs/PLAYBOOK_EXECUTION_SEAM.md), [docs/PLAYBOOK_OPERATIONAL_FAMILY](docs/PLAYBOOK_OPERATIONAL_FAMILY.md), [docs/PLAYBOOK_RECURRENCE_DISCIPLINE](docs/PLAYBOOK_RECURRENCE_DISCIPLINE.md), [docs/PLAYBOOK_LIFECYCLE](docs/PLAYBOOK_LIFECYCLE.md), and [docs/PLAYBOOK_PORTFOLIO](docs/PLAYBOOK_PORTFOLIO.md)
- evidence, gates, and release posture: [docs/PLAYBOOK_REAL_RUN_WORKFLOW](docs/PLAYBOOK_REAL_RUN_WORKFLOW.md), [docs/PLAYBOOK_REAL_RUN_HARVEST](docs/PLAYBOOK_REAL_RUN_HARVEST.md), [docs/PLAYBOOK_COMPOSITION_GATES](docs/PLAYBOOK_COMPOSITION_GATES.md), [docs/PLAYBOOK_GAP_MATRIX](docs/PLAYBOOK_GAP_MATRIX.md), and [docs/RELEASING](docs/RELEASING.md)
- adjunct outline seam: [docs/QUESTLINE_AND_CAMPAIGN_MODEL](docs/QUESTLINE_AND_CAMPAIGN_MODEL.md)
- live authored examples: [playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md](playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md), [playbooks/witness-to-compost-pilot/PLAYBOOK.md](playbooks/witness-to-compost-pilot/PLAYBOOK.md), and the wider `playbooks/*/PLAYBOOK.md` family
- current direction: [ROADMAP](ROADMAP.md)

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

- root registry: `generated/playbook_registry.min.json`
- authored bundles under `playbooks/*/PLAYBOOK.md`
- derived activation, federation, and review-status surfaces such as `generated/playbook_activation_surfaces.min.json`, `generated/playbook_federation_surfaces.min.json`, and `generated/playbook_review_status.min.json`
- playbook-owned composition adjuncts such as `generated/playbook_handoff_contracts.json`, `generated/playbook_failure_catalog.json`, `generated/playbook_subagent_recipes.json`, `generated/playbook_automation_seeds.json`, and `generated/playbook_composition_manifest.json`

Real-run harvest templates under `examples/harvests/` and review notes under `docs/real-runs/` and `docs/gate-reviews/` stay bounded evidence surfaces. They do not turn this repository into a runtime log substrate.

## Go here when...

- you need a single bounded execution unit: [`aoa-skills`](https://github.com/8Dionysus/aoa-skills)
- you need role and handoff contracts: [`aoa-agents`](https://github.com/8Dionysus/aoa-agents)
- you need proof surfaces or evidence framing: [`aoa-evals`](https://github.com/8Dionysus/aoa-evals)
- you need explicit memory objects or recall posture: [`aoa-memo`](https://github.com/8Dionysus/aoa-memo)
- you need the smallest next object or dispatch hint: [`aoa-routing`](https://github.com/8Dionysus/aoa-routing)
- you need the ecosystem center and boundary doctrine: [`Agents-of-Abyss`](https://github.com/8Dionysus/Agents-of-Abyss)

## Build and validate

To validate the current playbook-layer surface locally, run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_playbook_activation_surfaces.py --check
python scripts/generate_playbook_federation_surfaces.py --check
python scripts/generate_playbook_review_status.py --check
python scripts/generate_playbook_composition_surfaces.py --check
python scripts/validate_playbooks.py
```

The validator auto-discovers authored bundles under `playbooks/*/PLAYBOOK.md`, checks registry alignment, resolves federation-facing references into neighboring repositories, and validates the local guidance surfaces at `playbooks/AGENTS.md` and `generated/AGENTS.md`.

## Current contour

`aoa-playbooks` has reached its `v0.1.0` public baseline. The current honest move is evidence-led maturation rather than bootstrap growth for its own sake.

The runtime-facing extension stays intentionally bounded: selected playbooks may publish explicit memo-read defaults and activation-readable surfaces, but memo truth, routing ownership, and source skill meaning remain in their owning repositories.

Questline and campaign reflection also remains adjunct-only. It is a reviewed outline seam, not a runtime ledger or quest authority surface.

## License

Apache-2.0
