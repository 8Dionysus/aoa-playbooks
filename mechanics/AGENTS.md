# AGENTS.md

## Applies To

This card applies to `mechanics/` and every nested path until a nearer
`AGENTS.md` narrows the lane.

## Role

`mechanics/` is the package directory for repeatable playbook-layer mechanics.
It routes head-fed and local operation pressure without turning mechanics into
source playbook truth, proof verdicts, memory truth, role authority, routing
policy, or runtime implementation.

## Read Before Editing

1. root `AGENTS.md`
2. `DESIGN.md`
3. `DESIGN.AGENTS.md`
4. `mechanics/README.md`
5. target package `AGENTS.md`, `README.md`, `PARTS.md`, and `PROVENANCE.md`
6. target source playbook, generated builder, review note, config, schema, or
   decision record that owns the active claim

## Boundaries

- Mechanics are operations, not topic buckets.
- `mechanics/` root has only two docs: `README.md` and `AGENTS.md`.
- Do not add root-level roster, audit, template, backlog, legacy, notes,
  scratch, migration, or `_meta/` holding surfaces.
- Source-authored scenario meaning stays in `playbooks/*/*/*/PLAYBOOK.md`.
- Generated readers stay weaker than source and builders.
- Real-run and gate-review evidence stay evidence surfaces, not proof verdicts.
- Head-fed mechanics from `Agents-of-Abyss` become playbook-local only when the
  playbook layer has its own operation, owner split, stop-lines, and validation.
- Local mechanics do not become center-wide law merely because this repo names
  them.
- Former-path accounting belongs in package `PROVENANCE.md` and package-local
  `legacy/`; repository-root `legacy/` is forbidden.

## Package Growth Rule

A new `mechanics/<slug>/` package should appear only when it has:

- repeatable operation pressure;
- source surfaces and payload classes;
- owner split and stop-lines;
- local validation;
- class: `head-fed`, `local`, or both.

Use the package shape in `mechanics/README.md`. Do not create a child package as
a parking lot for unresolved docs.

## Validation

For mechanics root changes, run:

```bash
python scripts/validate_mechanics_skeleton.py
python scripts/validate_root_design.py
python scripts/generate_decision_indexes.py --check
python scripts/validate_playbooks.py
```

For package-local work, run the package validator named by the nearest package
card before the broader release lane.

## Closeout

Report which mechanic package changed, whether pressure was `head-fed` or
`local`, whether any payload moved, which validator ran, and which
stronger-owner boundary stayed intact.
