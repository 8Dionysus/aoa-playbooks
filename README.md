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
5. Read [docs/PLAYBOOK_EXECUTION_SEAM](docs/PLAYBOOK_EXECUTION_SEAM.md) for the derived runtime-readable activation seam.
6. Read [docs/PLAYBOOK_OPERATIONAL_FAMILY](docs/PLAYBOOK_OPERATIONAL_FAMILY.md) for chooser rules across the operational playbook family.
7. Read [docs/PLAYBOOK_RECURRENCE_DISCIPLINE](docs/PLAYBOOK_RECURRENCE_DISCIPLINE.md) for scenario-level recurrence posture.
8. Read [docs/PLAYBOOK_LIFECYCLE](docs/PLAYBOOK_LIFECYCLE.md) for the playbook graduation path.
9. Read [docs/PLAYBOOK_PORTFOLIO](docs/PLAYBOOK_PORTFOLIO.md) for coverage and portfolio guidance.
10. Read [docs/PLAYBOOK_REAL_RUN_WORKFLOW](docs/PLAYBOOK_REAL_RUN_WORKFLOW.md) for the repo-first chooser -> run -> review -> gate workflow.
11. Read [docs/PLAYBOOK_REAL_RUN_HARVEST](docs/PLAYBOOK_REAL_RUN_HARVEST.md) for evidence-first real-run harvest doctrine.
12. Read [docs/PLAYBOOK_COMPOSITION_GATES](docs/PLAYBOOK_COMPOSITION_GATES.md) for promotion rules before any new adjunct reaches composition.
13. Read [docs/PLAYBOOK_GAP_MATRIX](docs/PLAYBOOK_GAP_MATRIX.md) for the current lifecycle posture and next bounded move.
14. Open [playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md](playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md) for the first checkpoint-method playbook object.
15. Open [playbooks/witness-to-compost-pilot/PLAYBOOK.md](playbooks/witness-to-compost-pilot/PLAYBOOK.md) for the witness/compost pilot route.
16. Read [ROADMAP](ROADMAP.md) for the current direction.

## What this repository is for

`aoa-playbooks` should own playbook-layer meaning about:
- recurring operational scenarios
- multi-step compositions of skills
- scenario-level methods once a route spans skills, roles, memory posture, and proof posture
- role-aware handoff patterns
- decision points and fallback paths
- governed return posture when scenario routes lose axis, boundary, or restart integrity
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
- `playbooks/long-horizon-model-tier-orchestra/PLAYBOOK.md`
- `playbooks/restartable-inquiry-loop/PLAYBOOK.md`
- `playbooks/cross-repo-boundary-rollout/PLAYBOOK.md`
- `playbooks/bounded-change-safe/PLAYBOOK.md`
- `playbooks/infra-change-guarded/PLAYBOOK.md`
- `playbooks/invariants-first-refactor/PLAYBOOK.md`
- `playbooks/local-stack-diagnosis/PLAYBOOK.md`
- `playbooks/source-truth-then-share/PLAYBOOK.md`
- `playbooks/atm10-bounded-change/PLAYBOOK.md`
- `playbooks/split-wave-cross-repo-rollout/PLAYBOOK.md`
- `playbooks/validation-driven-remediation/PLAYBOOK.md`
- `playbooks/release-migration-cutover/PLAYBOOK.md`
- `playbooks/incident-recovery-routing/PLAYBOOK.md`

The validator auto-discovers authored bundles under `playbooks/*/PLAYBOOK.md` and checks that each one stays aligned with the registry surface.
For the long-horizon experimental seam, it also checks that participating agents resolve in `aoa-agents`, model-tier artifact contracts stay aligned where applicable, and referenced eval anchors exist in `aoa-evals`.
It now also validates the derived activation surface used to make selected playbooks runtime-readable without changing bundle authorship.
For the current federation-checked cohort, it also resolves exact skills in `aoa-skills` and memo contracts in `aoa-memo` without moving ownership out of those repositories.
For the runtime-facing activation cohort, it now also projects flat memo recall defaults so a downstream runtime can derive bounded `inspect`, `capsule`, and `expand` posture from playbook-owned surfaces without inventing memo search or ranking here.
It now also validates derived composition surfaces for handoff contracts, failure catalogs, subagent recipes, automation seeds, and a composition manifest without turning the playbook layer into a runtime engine.
It now also requires the local guidance surfaces at `playbooks/AGENTS.md` and `generated/AGENTS.md` to stay present and aligned with the authored-vs-derived split of this layer.
It now also validates the shipped real-run harvest templates under `examples/harvests/` so evidence scaffolding stays reviewable without becoming a runtime log substrate.
It now also validates the repo-first real-run workflow surfaces under `docs/real-runs/` and `docs/gate-reviews/` without turning this repository into a runtime evidence store.
Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.
`AOA-P-0016 atm10-bounded-change` remains activation-readable and composition-managed, and is now back in the federation cohort because its ATM10 overlay skills reconcile as `project_overlay_federation_ready` in `aoa-skills` without introducing a governance lane there.

Derived playbook surfaces live at:
- `schemas/playbook-activation-surface.schema.json`
- `schemas/playbook-federation-surface.schema.json`
- `generated/playbook_activation_surfaces.min.json`
- `generated/playbook_federation_surfaces.min.json`
- `generated/playbook_handoff_contracts.json`
- `generated/playbook_failure_catalog.json`
- `generated/playbook_subagent_recipes.json`
- `generated/playbook_automation_seeds.json`
- `generated/playbook_composition_manifest.json`
- `examples/playbook_activation.long-horizon-model-tier-orchestra.example.json`
- `examples/playbook_activation.restartable-inquiry-loop.example.json`
- `examples/playbook_activation.cross-repo-boundary-rollout.example.json`
- `examples/playbook_activation.split-wave-cross-repo-rollout.example.json`
- `examples/playbook_activation.validation-driven-remediation.example.json`
- `examples/playbook_activation.release-migration-cutover.example.json`
- `examples/playbook_activation.incident-recovery-routing.example.json`

To validate the current playbook-layer surface locally, run:

```bash
python scripts/generate_playbook_activation_surfaces.py --check
python scripts/generate_playbook_federation_surfaces.py --check
python scripts/generate_playbook_composition_surfaces.py --check
python scripts/validate_playbooks.py
```

## Current status

`aoa-playbooks` is in bootstrap with authored playbook bundles for checkpoint work, witness/compost flow, model-tier orchestration, restartable inquiry, cross-repo boundary rollout, split-wave cross-repo rollout, validation-driven remediation, release-migration cutover, incident-recovery routing, bounded change safety, guarded infra changes, invariants-first refactors, local stack diagnosis, source-truth sharing, and ATM10 overlay change work.
The current goal is to keep the playbook layer compact while giving scenario-level method one real source-owned home plus a bounded derived composition surface.
The current closure step is to keep federation-checked scenario routes machine-checkable against `aoa-skills` and `aoa-memo` without blurring boundaries or introducing a persisted run engine here.
The current runtime-facing extension is to let a bounded activation cohort publish explicit memo-read defaults while leaving actual memo recall truth, search posture, and routing ownership in `aoa-memo` and `aoa-routing`.

## Principles

- recurring scenarios should be explicit rather than folkloric
- playbooks should stay bounded and reviewable
- fallback and rollback posture should be named, not implied
- return posture should be explicit when a recurring route can lose axis, ownership boundary, or restart integrity
- evaluation posture should be visible, not retrofitted later
- the playbook layer should not swallow neighboring AoA layers

## License

Apache-2.0
