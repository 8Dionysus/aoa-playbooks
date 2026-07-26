# AGENTS.md

## Applies to

This card applies to `mechanics/scenario-composition/` until a nearer
`AGENTS.md` narrows the lane.

## Role

`mechanics/scenario-composition/` owns the local mechanic that derives compact
handoff, failure, subagent, automation, composition manifest, and
runtime-neutral plan-contour read models from authored playbooks and
source-owned configs.

## Read before editing

Read:

1. root `AGENTS.md`
2. `DESIGN.md`
3. `DESIGN.AGENTS.md`
4. `mechanics/AGENTS.md`
5. `mechanics/README.md`
6. `mechanics/scenario-composition/README.md`
7. `mechanics/scenario-composition/PARTS.md`
8. `mechanics/scenario-composition/parts/composition-surfaces/docs/handoff-contracts.md`
9. `mechanics/scenario-composition/parts/composition-surfaces/docs/failure-recovery.md`
10. `mechanics/scenario-composition/parts/composition-surfaces/docs/subagent-patterns.md`
11. `mechanics/scenario-composition/parts/composition-surfaces/docs/automation-seeds.md`
12. `mechanics/scenario-composition/parts/composition-surfaces/config/playbook_composition_overrides.json`
13. `mechanics/scenario-composition/parts/plan-contours/README.md`
14. `mechanics/scenario-composition/parts/plan-contours/docs/playbook-plan-contour-contract.md`
15. `mechanics/scenario-composition/parts/plan-contours/config/playbook_plan_contours.json`

## Boundaries

- Scenario composition is class `local`.
- Source playbook truth stays in `playbooks/*/*/*/PLAYBOOK.md`.
- Source composition overrides stay in root `config/` until compatibility and
  validators support a move.
- Generated composition outputs stay root-published read models.
- Generated plan contours stay root-published read models; their abstract
  source, schema, and generator stay in `parts/plan-contours/`.
- Root `mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py` stays a
  compatibility command wrapper.
- Do not encode runtime state, scheduler authority, router policy, skill
  meaning, proof verdicts, or memory truth in composition outputs.
- Do not encode commands, prompts, tools, arguments, MCP, transport, models,
  shell, scripts, or consumer-owned binding provenance in plan contours.

## Validation

Run:

```bash
python mechanics/scenario-composition/scripts/validate_scenario_composition_package.py
python mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py --check
python mechanics/scenario-composition/parts/plan-contours/scripts/generate_playbook_plan_contours.py --check
python scripts/validate_mechanics_skeleton.py
python scripts/validate_playbooks.py
```

For release-bound changes, run:

```bash
python scripts/release_check.py
```

## Closeout

Report whether source playbooks or composition/plan-contour configs changed,
whether root generated outputs changed, whether the package implementation or
root wrapper changed, and which validation proved generated parity.
