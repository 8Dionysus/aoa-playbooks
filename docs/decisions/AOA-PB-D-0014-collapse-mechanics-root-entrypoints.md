# Collapse Mechanics Root Entrypoints

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0014
- Original date: 2026-05-31
- Surface classes: mechanic package, docs route, validation guard, source topology, decision record
- Playbook routes: none
- Mechanic parents: cross-mechanic
- Guard families: package route, source topology, validation guard, legacy/provenance, AGENTS/mesh
- Posture: accepted mechanics root entrypoint collapse

## Context

The package-moving landings made `mechanics/` real, but the root of that
directory still carried several control documents: roster, audit, template, and
legacy-accounting surfaces. Those files explained the migration, but they also
made the first screen look like a holding shelf instead of a package directory.

The stronger route is the one used across the refactored AoA repos: a small
root entrypoint, package-local cards for active function, local provenance for
former names, and validators that prevent a new loose lane from appearing.

## Decision

Keep only two root markdown files in `mechanics/`:

- `mechanics/README.md`
- `mechanics/AGENTS.md`

Fold the durable operational rules into those two files:

- head-fed versus local mechanic routing;
- placement rules;
- legacy-name posture;
- package shape;
- validation and closeout route law.

Active mechanic detail belongs under `mechanics/<package>/`. Historical
rationale belongs in `docs/decisions/`. Former-path accounting belongs in the
owning package `PROVENANCE.md` and package-local `legacy/` when the active route
needs it. A root `_meta/`, root `legacy/`, root notes lane, or root migration
lane is not an acceptable substitute.

## Rationale

Modern agent-facing repo maps work best when the first route gives role, input,
output, owner, next route, tools, and validation without forcing an agent
through migration prose. This also preserves the center/local split: head-fed
mechanics can arrive from `Agents-of-Abyss`, but `aoa-playbooks` only owns the
playbook-local operation and its package route.

The collapse keeps the mechanics layer visible while removing the root clutter
that would otherwise compete with package cards.

## Consequences

- Positive: `mechanics/` now reads as a package directory on the first screen.
- Positive: root mechanics markdown is validator-guarded.
- Positive: old-name and placement rules remain active, but no longer require
  separate root files.
- Tradeoff: older decision records may mention previous migration files as
  history; those records are rationale, not active routes.
- Follow-up: future mechanics growth must land in a package with validation, not
  in a root holding file.

## Current Applicability

As of 2026-05-31:

- Valid: root mechanics files are limited to `README.md` and `AGENTS.md`.
- Valid: active mechanics live in package routes under `mechanics/<package>/`.
- Valid: package provenance may preserve former names.
- Superseded by: none.

## Review Log

### 2026-05-31 - Root mechanics collapse

- Previous assumption: root mechanics could keep separate control documents
  while packages grew.
- New reality: those documents distracted from the package-directory function.
- Reason: package routes are active; root migration scaffolding is no longer the
  right first screen.
- Source surfaces updated: root docs, mechanics root cards, validators, tests,
  and generated decision indexes.
- Validation: the owning executable validator, generated-freshness checks, relevant tests, and repository release gate.

## Boundaries

- This decision does not move source playbooks out of `playbooks/`.
- This decision does not move generated public read models out of `generated/`.
- This decision does not delete package-local provenance.
- This decision does not claim center mechanics, runtime authority, proof
  verdicts, memory truth, routing authority, role authority, or KAG promotion.
- This decision does not make decision history an active route.

## Source Surfaces

- `mechanics/README.md`
- `mechanics/AGENTS.md`
- `scripts/validate_mechanics_skeleton.py`
- `tests/test_mechanics_skeleton.py`
- `README.md`
- `docs/README.md`
- `DESIGN.md`
- `DESIGN.AGENTS.md`

## Follow-Up Route

New mechanic pressure routes to the owning package. If no package owns it yet,
create the package route and validator in the same slice.

## Verification

Verification is owned by the corresponding executable validators and the repository release gate; focused invocation lives in the nearest `AGENTS.md`.
