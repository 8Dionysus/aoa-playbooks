# AGENTS.md

## Applies to

This card applies to `mechanics/scenario-composition/` until a nearer
`AGENTS.md` narrows the lane.

## Role

`mechanics/scenario-composition/` owns the local mechanic that derives compact
handoff, failure, subagent, automation, composition manifest, and
runtime-neutral plan-contour read models from authored playbooks and
source-owned configs.

## Route by task

- Composition readout: use the exact handoff, failure, subagent, or automation
  contract, `playbook_composition_overrides.json`, and its builder.
- Plan contour: use the part README, contour contract, source config, schema,
  and builder.
- Package topology or provenance: use `README.md`, `PARTS.md`, and
  `PROVENANCE.md`.
- Repository or agent-route shape: use `DESIGN.md` or `DESIGN.AGENTS.md`
  respectively.

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
