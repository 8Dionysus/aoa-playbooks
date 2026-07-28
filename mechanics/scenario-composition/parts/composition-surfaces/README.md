# Composition Surfaces Part

## Role

This part owns the implementation that builds the root composition read models:

- `generated/playbook_handoff_contracts.json`
- `generated/playbook_failure_catalog.json`
- `generated/playbook_subagent_recipes.json`
- `generated/playbook_automation_seeds.json`
- `generated/playbook_composition_manifest.json`

## Source surfaces

- `playbooks/*/*/*/PLAYBOOK.md`
- `generated/playbook_registry.min.json`
- `mechanics/scenario-composition/parts/composition-surfaces/config/playbook_composition_overrides.json`
- `../aoa-skills/generated/capability_graph.json`
- root command wrapper `mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py`

## Boundary

The generated outputs remain root-published. This part owns the builder
implementation, not the public output paths.

## Validation

The part-local builder and package validator are the executable owners. Their
focused order lives in the nearest `AGENTS.md`.
