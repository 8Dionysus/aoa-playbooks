# Playbook Mechanics Atlas

`mechanics/` is the operation atlas for repeatable playbook-layer mechanics in
`aoa-playbooks`.

It does not replace source playbooks under `playbooks/`, public explanation
under `docs/`, source config under `config/`, schemas under `schemas/`,
examples under `examples/`, generated readers under `generated/`, or decisions
under `docs/decisions/`.

It names the operations that repeatedly move pressure across those surfaces and
keeps owner boundaries visible.

This first skeleton creates the route. The placement audit and legacy naming
gate now define how payloads can move without creating a root archive lane or
blurring source playbooks with mechanic packages.

## Operating Card

| Field | Route |
| --- | --- |
| role | atlas for repeatable playbook-layer operations |
| entry | choose `head-fed` when pressure starts from `Agents-of-Abyss`; choose `local` when pressure starts from playbook-owned scenario machinery |
| input | recurring scenario-operation pressure, owner-request pressure, generated-reader drift, review-gate drift, package-boundary pressure, or topology movement |
| output | lane route, package-growth candidate, validator route, source-owner route, or stronger-owner handoff |
| owner | `mechanics/AGENTS.md`, this atlas, `HEAD_MECHANICS.md`, `LOCAL_MECHANICS.md`, and future package cards |
| next route | target source playbook, generated builder, review/gate source, decision record, or stronger owner repo |
| validation | `python scripts/validate_mechanics_skeleton.py` and the nearest future package card |

## Mechanics Classes

### Head-fed mechanics

Head-fed mechanics start at `Agents-of-Abyss` as center mechanics and land in
owner repos only through a local owner split.

They answer:

- what center mechanic is pressing on the playbook layer;
- what the center owns;
- what `aoa-playbooks` may own locally;
- what remains with another owner repo;
- what must be validated before the local landing can claim more than a route.

The current roster lives in [HEAD_MECHANICS](HEAD_MECHANICS.md).

### Local mechanics

Local mechanics start inside `aoa-playbooks`.

They answer:

- what repeatable playbook-layer operation keeps recurring;
- which playbook source, generated reader, review gate, or config surface owns
  the active claim;
- what may become package-local later;
- what must remain in playbook source, generated readers, docs, or sibling
  owners.

The current roster lives in [LOCAL_MECHANICS](LOCAL_MECHANICS.md).

## Skeleton Route

Use this skeleton before creating child packages:

1. Name the pressure.
2. Decide whether it is `head-fed` or `local`.
3. Check the matching roster.
4. Identify the source surface and stronger owner split.
5. Decide whether the operation already needs a child package or only a route
   note.
6. Check [PLACEMENT_AUDIT](PLACEMENT_AUDIT.md) and
   [LEGACY_NAMING](LEGACY_NAMING.md) for current placement and old-name
   posture.
7. If a package is needed, start from [PACKAGE_TEMPLATE](PACKAGE_TEMPLATE.md)
   and add validation in the same slice.

## Package Route Standard

Future `mechanics/<slug>/` packages should use this minimum surface set:

| Surface | Use for |
| --- | --- |
| `AGENTS.md` | package-local route law, validation, and closeout |
| `README.md` | mechanic card and entry route |
| `PARTS.md` | active functioning parts and deferred payload map |
| `PROVENANCE.md` | active-first bridge to center source, prior path, or sibling evidence |
| `docs/` | mechanic-owned doctrine only after package validation exists |
| `parts/` | part-local contracts and payload homes after part validation exists |

Do not create these files as empty ceremony. A child package must have at least
one source surface, owner split, stop-line, and validation route.

## Head And Local Split

| Class | Source of pressure | Local acceptance requirement | Must not claim |
| --- | --- | --- | --- |
| `head-fed` | center mechanics in `Agents-of-Abyss` | playbook-local operation, source surface, stop-line, and validator route | center authority, owner acceptance, or sibling truth |
| `local` | recurring playbook-layer operation | source playbook, generated builder, review surface, config, schema, or decision route | center law, runtime execution, proof verdict, memory truth, role authority, or routing policy |

## Current Status

Status: `package-growth`.

`mechanics/activation/`, `mechanics/scenario-composition/`,
`mechanics/federation-closure/`, `mechanics/review-gate/`, and
`mechanics/real-run-harvest/` are operational local packages.
`mechanics/antifragility/`, `mechanics/agon/`, `mechanics/recurrence/`,
`mechanics/checkpoint/`, `mechanics/experience/`,
`mechanics/release-support/`, `mechanics/questbook/`, `mechanics/rpg/`, and
`mechanics/titan/` are package-active head-fed/local routes.
`mechanics/portfolio-governance/` is a package-active package-local local
route.
No source playbook has moved.
The active result is a checked route map, placement audit, legacy-name gate,
package-local implementation moves that keep root command wrappers, and a
package-local evidence posture for real-run harvest paths.

## Validation

Run:

```bash
python scripts/validate_mechanics_skeleton.py
python mechanics/review-gate/scripts/validate_review_gate_package.py
python mechanics/real-run-harvest/scripts/validate_real_run_harvest_package.py
python mechanics/antifragility/scripts/validate_antifragility_package.py
python mechanics/agon/scripts/validate_agon_package.py
python mechanics/recurrence/scripts/validate_recurrence_package.py
python mechanics/checkpoint/scripts/validate_checkpoint_package.py
python mechanics/experience/scripts/validate_experience_package.py
python mechanics/release-support/scripts/validate_release_support_package.py
python mechanics/questbook/scripts/validate_questbook_package.py
python mechanics/rpg/scripts/validate_rpg_package.py
python mechanics/titan/scripts/validate_titan_package.py
python mechanics/portfolio-governance/scripts/validate_portfolio_governance_package.py
python scripts/validate_playbooks.py
```

For release-bound changes, run:

```bash
python scripts/release_check.py
```
