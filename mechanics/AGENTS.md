# AGENTS.md

## Applies To

This card applies to `mechanics/` and every nested path until a nearer
`AGENTS.md` narrows the lane.

## Role

`mechanics/` is the package directory for repeatable playbook-layer mechanics.
It routes head-fed and local operation pressure without turning mechanics into
source playbook truth, proof verdicts, memory truth, role authority, routing
policy, or runtime implementation.

## Route by task

The inherited root and mechanics cards already supply the common law. Add only
the sources needed by the change:

- package-local work: the nearest package card and exact source, builder,
  config, schema, evidence note, or playbook that owns the claim
- public package topology, class, or placement: `mechanics/README.md` and the
  target package README
- part placement or former-path accounting: the target `PARTS.md` and
  `PROVENANCE.md`
- repository/source topology: `DESIGN.md`
- agent-card shape: `DESIGN.AGENTS.md`

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
- Former-path accounting belongs in the package `README.md` provenance section
  or its `PROVENANCE.md` companion and package-local `legacy/`;
  repository-root `legacy/` is forbidden.

## Package Growth Rule

A new `mechanics/<slug>/` package should appear only when it has:

- repeatable operation pressure;
- source surfaces and payload classes;
- owner split and stop-lines;
- local validation;
- class: `head-fed`, `local`, or both.

Every package starts with `AGENTS.md` and `README.md`. A compact package keeps
its parts and provenance sections in `README.md`; a larger package may split
both into the `PARTS.md` and `PROVENANCE.md` companion pair. Use the package
shape in `mechanics/README.md`. Do not create a child package as a parking lot
for unresolved docs.

## Validation

For mechanics root changes, run:

Run the [Mechanics](../VALIDATION.md#mechanics) lane in the root validation map
on demand.

For package-local work, run the package validator named by the nearest package
card before the broader release lane.

## Closeout

Report which mechanic package changed, whether pressure was `head-fed` or
`local`, whether any payload moved, which validator ran, and which
stronger-owner boundary stayed intact.
