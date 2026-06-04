# AGENTS.md

## Applies to

This card applies to `mechanics/scenario-composition/` until a nearer
`AGENTS.md` narrows the lane.

## Role

`mechanics/scenario-composition/` owns the local mechanic that derives compact
handoff, failure, subagent, automation, and composition manifest read models
from authored playbooks and source-owned composition overrides.

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

## Boundaries

- Scenario composition is class `local`.
- Source playbook truth stays in `playbooks/*/*/*/PLAYBOOK.md`.
- Source composition overrides stay in root `config/` until compatibility and
  validators support a move.
- Generated composition outputs stay root-published read models.
- Root `mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py` stays a
  compatibility command wrapper.
- Do not encode runtime state, scheduler authority, router policy, skill
  meaning, proof verdicts, or memory truth in composition outputs.

## Validation

Run:

```bash
python mechanics/scenario-composition/scripts/validate_scenario_composition_package.py
python mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py --check
python scripts/validate_mechanics_skeleton.py
python scripts/validate_playbooks.py
```

For release-bound changes, run:

```bash
python scripts/release_check.py
```

## Closeout

Report whether source playbooks or composition overrides changed, whether root
generated outputs changed, whether the package implementation or root wrapper
changed, and which validation proved generated parity.
