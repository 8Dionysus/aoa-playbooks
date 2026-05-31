# Scenario Composition Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `composition-surfaces` | derive root composition read models from playbooks, source overrides, and skill handoff contracts | `playbooks/*/PLAYBOOK.md`, `mechanics/scenario-composition/parts/composition-surfaces/config/playbook_composition_overrides.json`, `../aoa-skills/generated/skill_handoff_contracts.json`, root generated composition outputs | `python mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py --check` | active |

## Boundary payloads

| Payload | Current route | Reason |
| --- | --- | --- |
| composition source config | `mechanics/scenario-composition/parts/composition-surfaces/config/playbook_composition_overrides.json` | package-local source config cited by generated source-of-truth fields |
| composition docs | `mechanics/scenario-composition/parts/composition-surfaces/docs/handoff-contracts.md`, `mechanics/scenario-composition/parts/composition-surfaces/docs/failure-recovery.md`, `mechanics/scenario-composition/parts/composition-surfaces/docs/subagent-patterns.md`, `mechanics/scenario-composition/parts/composition-surfaces/docs/automation-seeds.md`, `mechanics/scenario-composition/parts/composition-surfaces/docs/playbook-composition-gates.md` | package-local public model and gate surfaces |
| composition generated outputs | `generated/playbook_handoff_contracts.json`, `generated/playbook_failure_catalog.json`, `generated/playbook_subagent_recipes.json`, `generated/playbook_automation_seeds.json`, `generated/playbook_composition_manifest.json` | root-published read models consumed by downstream readers |
| composition tests | `tests/test_generate_playbook_composition_surfaces.py` | root tests protect repo release gate and root command compatibility |

## Part growth rule

Move only public generated read models if source-of-truth fields, public links,
and downstream generated path refs can remain explicit and validated.
