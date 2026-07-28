# Scenario Composition Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `composition-surfaces` | derive root composition read models from playbooks, source overrides, and typed capability nodes | `playbooks/*/*/*/PLAYBOOK.md`, `mechanics/scenario-composition/parts/composition-surfaces/config/playbook_composition_overrides.json`, `../aoa-skills/generated/capability_graph.json`, root generated composition outputs | `mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py` | active |
| `plan-contours` | derive a closed runtime-neutral plan-contour ABI for selected playbook routes | three named `PLAYBOOK.md` bundles and `mechanics/scenario-composition/parts/plan-contours/config/playbook_plan_contours.json` | `mechanics/scenario-composition/parts/plan-contours/scripts/generate_playbook_plan_contours.py` | active |

## Boundary payloads

| Payload | Current route | Reason |
| --- | --- | --- |
| composition source config | `mechanics/scenario-composition/parts/composition-surfaces/config/playbook_composition_overrides.json` | package-local source config cited by generated source-of-truth fields |
| composition docs | `mechanics/scenario-composition/parts/composition-surfaces/docs/handoff-contracts.md`, `mechanics/scenario-composition/parts/composition-surfaces/docs/failure-recovery.md`, `mechanics/scenario-composition/parts/composition-surfaces/docs/subagent-patterns.md`, `mechanics/scenario-composition/parts/composition-surfaces/docs/automation-seeds.md`, `mechanics/scenario-composition/parts/composition-surfaces/docs/playbook-composition-gates.md` | package-local public model and gate surfaces |
| composition generated outputs | `generated/playbook_handoff_contracts.json`, `generated/playbook_failure_catalog.json`, `generated/playbook_subagent_recipes.json`, `generated/playbook_automation_seeds.json`, `generated/playbook_composition_manifest.json` | root-published read models consumed by downstream readers |
| composition tests | `tests/test_generate_playbook_composition_surfaces.py` | root tests protect repo release gate and root command compatibility |
| plan-contour source and schema | `mechanics/scenario-composition/parts/plan-contours/config/playbook_plan_contours.json`, `mechanics/scenario-composition/parts/plan-contours/schemas/playbook-plan-contours.schema.json` | owner-authored abstract contour and closed public ABI |
| plan-contour generated output | `generated/playbook_plan_contours.min.json` | root-published runtime-neutral read model for pinned downstream compilation |
| plan-contour tests | `tests/test_generate_playbook_plan_contours.py` | exact playbook alignment, deterministic parity, input/output role partition, guarded-branch integrity, and executable-field rejection |

## Part growth rule

Move only public generated read models if source-of-truth fields, public links,
and downstream generated path refs can remain explicit and validated.

Plan contours must remain abstract. A part may add operation/effect classes,
reviewed input/output roles, owner-named boolean guards, and owner-qualified
requirements, but never concrete condition values, commands, prompts, tools,
arguments, transport, model choice, scheduler logic, or mutable execution
state.
