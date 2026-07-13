# Add Mechanics Placement Audit And Legacy Naming Gate

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0005
- Original date: 2026-05-31
- Surface classes: mechanic package, docs route, validation guard, legacy/provenance, decision record
- Playbook routes: none
- Mechanic parents: cross-mechanic
- Guard families: package route, legacy/provenance, source topology, validation guard, sibling-owner boundary
- Posture: accepted placement audit

## Context

The first `mechanics/` landing created an atlas, head-fed roster, local roster,
and package template, but it intentionally did not move payloads.

The next mechanics-refactor pressure is broader: root, docs, config, schemas,
examples, generated, scripts, tests, manifests, playbooks, questbook, and
decision surfaces all contain mechanics-related names. Moving by filename would
break owner boundaries because some root paths are public compatibility routes,
some generated outputs are repo-wide read models, some source stores must stay
root-owned, and authored `playbooks/*/*/*/PLAYBOOK.md` must remain the playbook
canon.

Sibling repositories show the safer pattern: active package first, package
part map second, package `PROVENANCE.md` as the active bridge to former paths,
and package-local `legacy/` only when real moved-path or raw receipt accounting
exists. A root `legacy/` directory would make history look like an alternate
active route.

## Options Considered

1. Move every filename that matches a mechanic term into a matching package.
2. Create a root `legacy/` map before package landings.
3. Add a mechanics placement audit and legacy naming gate, then move payloads
   only through package-specific owner splits and validators.

## Decision

Choose option 3.

Add:

- `mechanics/PLACEMENT_AUDIT.md` as the cross-package placement matrix;
- `mechanics/LEGACY_NAMING.md` as the posture guide for old names, wave names,
  compatibility names, generated projections, root-public paths, and
  stronger-owner vocabulary;
- validation that rejects a repository-root `legacy/` directory for mechanics
  accounting.

## Rationale

This keeps the refactor evidence-first.

The placement audit gives each mechanics-related payload family an explicit
current decision: move target, root exception if any, legacy-name posture,
consumer risk, validation hook, and status. That prevents package creation from
becoming a topic-bucket sweep.

The legacy naming gate protects the active route. Old names become historical,
accepted-input, generated-projection, root-public, candidate-only,
provenance-bridge, or stronger-owner names. They do not become active routes
just because they are familiar.

## Consequences

- Positive: later payload moves now have a checked placement matrix.
- Positive: root `legacy/` is forbidden before it can become a false route.
- Positive: package-local `PROVENANCE.md` remains the only bridge into former
  paths once a package moves real payloads.
- Tradeoff: this adds one more control surface before large moves.
- Follow-up: land the first package with moved implementation payload and
  package-local provenance, starting with a small local package such as
  `activation` or `scenario-composition`.

## Current Applicability

As of 2026-05-31:

- Still valid: the mechanics layer is not complete until every placement row is
  either moved with package validation or intentionally retained with a root,
  playbook, generated, source-store, public, decision, or compatibility reason.
- Changed: package landings moved active payloads into package parts, and
  AOA-PB-D-0014 folded the placement and legacy rules into
  `mechanics/README.md`.
- Superseded by: AOA-PB-D-0014 for root mechanics file shape; still valid for
  package-local provenance, legacy-name posture, and no root `legacy/`.

## Review Log

### 2026-05-31 - Placement audit landing

- Previous assumption: the mechanics skeleton alone was enough before package
  movement.
- New reality: package movement needs an explicit payload matrix and old-name
  classification gate.
- Reason: `aoa-playbooks` contains mechanics pressure across root payload
  districts, but not every mechanics-related path should move.
- Source surfaces updated: `mechanics/PLACEMENT_AUDIT.md`,
  `mechanics/LEGACY_NAMING.md`, `mechanics/README.md`,
  `mechanics/AGENTS.md`, `scripts/validate_mechanics_skeleton.py`, and
  `tests/test_mechanics_skeleton.py`.
- Validation: the owning executable validator, generated-freshness checks, relevant tests, and repository release gate.

## Boundaries

- This decision does not create operational child mechanic packages.
- This decision does not move authored playbooks.
- This decision does not move generated outputs, examples, configs, schemas,
  scripts, tests, or manifests by itself.
- This decision does not make candidate-only roster rows operational.
- This decision does not move sibling-owner truth into `aoa-playbooks`.

## Source Surfaces

- `mechanics/README.md`
- `mechanics/AGENTS.md`
- `scripts/validate_mechanics_skeleton.py`
- `tests/test_mechanics_skeleton.py`
- `docs/decisions/AOA-PB-D-0014-collapse-mechanics-root-entrypoints.md`

## Follow-Up Route

Promote the first child package only with package cards, part map, package
`PROVENANCE.md`, moved payload or explicit root-retention route, and focused
validation.

## Verification

Verification is owned by the corresponding executable validators and the repository release gate; focused invocation lives in the nearest `AGENTS.md`.
