# AGENTS.md

## Applies to

This card applies to `mechanics/` and every nested path until a nearer
`AGENTS.md` narrows the lane.

## Role

`mechanics/` is the operation atlas for repeatable playbook-layer mechanics.

It routes recurring operation pressure around playbook activation, federation
closure, review gates, real-run harvest, scenario composition, portfolio
governance, and head-fed AoA mechanics without turning those operations into
source playbook truth, proof verdicts, memory truth, role authority, routing
policy, or runtime implementation.

## Operating Card

| Field | Route |
| --- | --- |
| role | operation atlas for repeatable playbook-layer mechanics |
| input | recurring operation pressure, package-boundary changes, route-card drift, validation-route changes, or head-fed owner pressure from `Agents-of-Abyss` |
| output | mechanic lane route, package-growth decision, validator route, playbook source route, or stronger-owner handoff |
| owner | `mechanics/README.md` for atlas shape; `mechanics/HEAD_MECHANICS.md` and `mechanics/LOCAL_MECHANICS.md` for skeleton rosters; `mechanics/PLACEMENT_AUDIT.md` for cross-package placement status; `mechanics/LEGACY_NAMING.md` for old-name posture; future package cards for child package route law |
| next route | `DESIGN.md`, `DESIGN.AGENTS.md`, target playbook source, generated reader builder, decision record, or stronger owner repo |
| tools | `scripts/validate_mechanics_skeleton.py`, `scripts/validate_root_design.py`, generated-surface builders, decision-index builder |
| validation | this card's `Validation` section plus future package-specific checks when packages exist |

## Route Stack

- Above: root `AGENTS.md` owns repo identity, owner boundaries, broad
  verification, and GitHub landing workflow.
- Design: `DESIGN.md` owns the system split between playbook canon, mechanics,
  docs, generated readers, review evidence, and sibling owners.
- Agent design: `DESIGN.AGENTS.md` owns the desired form of route cards.
- Here: `mechanics/README.md` owns the mechanics atlas.
- Roster: `HEAD_MECHANICS.md` names center-fed mechanics from
  `Agents-of-Abyss`; `LOCAL_MECHANICS.md` names playbook-native mechanics.
- Audit: `PLACEMENT_AUDIT.md` records move targets, package-local reasons, and
  validation coverage before payloads move.
- Legacy: `LEGACY_NAMING.md` classifies old names and keeps archive accounting
  package-local.
- Decisions: `docs/decisions/` owns why mechanics topology changes.

## Read before editing

Read:

1. root `AGENTS.md`
2. `DESIGN.md`
3. `DESIGN.AGENTS.md`
4. `mechanics/README.md`
5. `mechanics/HEAD_MECHANICS.md` when a mechanic pressure comes from
   `Agents-of-Abyss`
6. `mechanics/LOCAL_MECHANICS.md` when a mechanic pressure is born inside
   `aoa-playbooks`
7. `mechanics/PLACEMENT_AUDIT.md` before moving or retaining a payload
8. `mechanics/LEGACY_NAMING.md` before preserving old names or former paths
9. `mechanics/PACKAGE_TEMPLATE.md` before creating a child package
10. target source playbook, generated builder, review note, config, schema, or
   decision record that owns the active claim

## Boundaries

- Mechanics name repeatable operations; they are not topic buckets.
- Source-authored scenario meaning stays in `playbooks/*/PLAYBOOK.md`.
- Generated readers stay weaker than source and builders.
- Real-run and gate-review evidence stay evidence surfaces, not proof verdicts.
- Head-fed mechanics from `Agents-of-Abyss` become playbook-local only when the
  playbook layer has its own operation, owner split, stop-lines, and
  validation route.
- Local mechanics do not become center-wide law merely because this repo names
  them.
- Runtime autonomy, proof verdicts, durable memory truth, routing policy,
  role authority, KAG substrate, stats truth, and infrastructure
  implementation route to their owning repositories.
- This skeleton does not move existing flat docs or playbook bundles.
- Do not create a repository-root `legacy/` directory. Former-path accounting
  belongs in package `PROVENANCE.md` and package-local `legacy/` only after the
  active route exists.

## Package growth rule

A new `mechanics/<slug>/` package should appear only when it has:

- a repeatable operation, not only a theme;
- source surfaces and payload classes;
- owner split and stop-lines;
- validation route;
- decision or explicit route note when it changes topology;
- clear class: `head-fed` or `local`.

Use `PACKAGE_TEMPLATE.md` for the first package card. Do not create a child
package as a parking lot for unresolved docs.

## Validation

For mechanics skeleton changes, run:

```bash
python scripts/validate_mechanics_skeleton.py
python scripts/validate_root_design.py
python scripts/generate_decision_indexes.py --check
python scripts/validate_playbooks.py
```

For package-local work added later, run the package validator named by the
nearest package card before the broader release lane.

## Closeout

Report which mechanic lane changed, whether the pressure was `head-fed` or
`local`, whether any payload moved, which validator ran, which package remains
candidate-only, and which stronger-owner boundary stayed intact.
