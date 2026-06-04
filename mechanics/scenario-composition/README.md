# Scenario Composition Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | local |
| role | derive scenario-level handoff, failure, subagent, automation, and manifest read models |
| trigger | a managed playbook, composition override, upstream skill handoff contract, or generated composition output changes |
| playbooks owns | scenario-level composition projection shape and source config alignment |
| stronger owner split | `aoa-skills` owns skill execution and skill handoff meaning; routing/runtime owners own dispatch and execution |
| inputs | `playbooks/*/*/*/PLAYBOOK.md`, `generated/playbook_registry.min.json`, `mechanics/scenario-composition/parts/composition-surfaces/config/playbook_composition_overrides.json`, `../aoa-skills/generated/skill_handoff_contracts.json` |
| outputs | root-published `generated/playbook_handoff_contracts.json`, `generated/playbook_failure_catalog.json`, `generated/playbook_subagent_recipes.json`, `generated/playbook_automation_seeds.json`, and `generated/playbook_composition_manifest.json` |
| must not claim | runtime state, scheduler authority, route dispatch, skill semantics, proof verdicts, or memory truth |
| validation | `python mechanics/scenario-composition/scripts/validate_scenario_composition_package.py` and `python mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py --check` |
| next route | `parts/composition-surfaces/`, composition source docs, root generated read models, or `aoa-skills` for skill-owned meaning |

## Active route

The active builder implementation lives under
`parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py`.

The root command `scripts/generate_playbook_composition_surfaces.py` remains as
an operator-facing compatibility wrapper because README, release checks, and
tests already use that command path.

## Functioning parts

- `composition-surfaces`: builds and validates the compact composition read
  models from authored playbooks, root source config, and skill handoff
  contracts.

## Source surfaces

- `playbooks/*/*/*/PLAYBOOK.md`
- `generated/playbook_registry.min.json`
- `mechanics/scenario-composition/parts/composition-surfaces/config/playbook_composition_overrides.json`
- `../aoa-skills/generated/skill_handoff_contracts.json`
- root generated composition outputs
- `mechanics/scenario-composition/parts/composition-surfaces/docs/handoff-contracts.md`
- `mechanics/scenario-composition/parts/composition-surfaces/docs/failure-recovery.md`
- `mechanics/scenario-composition/parts/composition-surfaces/docs/subagent-patterns.md`
- `mechanics/scenario-composition/parts/composition-surfaces/docs/automation-seeds.md`
- `mechanics/scenario-composition/parts/composition-surfaces/docs/playbook-composition-gates.md`

## Owner boundary

Composition outputs are derived readers. They are weaker than authored
playbooks, root source config, and upstream skill contracts.

This mechanic may project handoff, failure, subagent, and automation metadata
that is already source-backed. It must not invent runtime execution behavior
or skill semantics.

## Growth posture

The next safe growth is part-local config or docs movement only after root
public links and generated output source-of-truth fields can preserve their
compatibility semantics.
