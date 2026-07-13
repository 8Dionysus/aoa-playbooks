# Add Mechanics Skeleton With Head-Fed And Local Lanes

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0004
- Original date: 2026-05-31
- Surface classes: root/topology, mechanic package, agent route, docs route, validation guard, decision record
- Playbook routes: none
- Mechanic parents: cross-mechanic
- Guard families: source topology, package route, AGENTS/mesh, decision index/read-model, validation guard
- Posture: accepted mechanics skeleton

## Context

After adding the root design spine, `aoa-playbooks` needed a first
`mechanics/` topology that can carry two different kinds of pressure:

- common AoA mechanics that start in `Agents-of-Abyss` and then land in owner
  repos through a local owner split;
- playbook-native mechanics that are born inside `aoa-playbooks` from
  activation, federation closure, review gates, scenario composition, real-run
  harvest, and portfolio governance.

Sibling repositories already show the pattern: mechanics are operation
atlases, not topic buckets. A mechanic becomes real when it has source
surfaces, owner split, inputs, outputs, stop-lines, and validation.

## Options Considered

1. Create many empty `mechanics/<slug>/` child packages immediately.
2. Create only a root `mechanics/README.md` with no checked distinction between
   head-fed and local mechanics.
3. Create a checked skeleton with root route law, head-fed roster, local
   roster, and package template, then add child packages later only when a
   package has real source surfaces and validation.

## Decision

Choose option 3.

Create `mechanics/` as a skeleton atlas with:

- `mechanics/AGENTS.md` for route law;
- `mechanics/README.md` for atlas shape;
- `mechanics/HEAD_MECHANICS.md` for center-fed mechanics from
  `Agents-of-Abyss`;
- `mechanics/LOCAL_MECHANICS.md` for playbook-native mechanics;
- `mechanics/PACKAGE_TEMPLATE.md` for future package creation;
- validation that keeps these surfaces present and rejects typo drift around
  `DESGIN`.

No existing playbook, docs, generated, config, schema, example, review, or
memo payload moves in this slice.

## Rationale

This gives future mechanics work a safe landing route without creating false
operational packages.

The head-fed/local split matters because `Agents-of-Abyss` is the center
mechanics head, but owner repos still need local acceptance: source surfaces,
stop-lines, validation, and owner-specific meaning. A center mechanic does not
become playbook-owned just because it is named.

Local playbook mechanics also need a route, because activation, review gates,
federation closure, and composition readers are already recurring operations
inside this repository. They should not be scattered forever across root docs,
but they should not move into package homes before validation and owner split
are explicit.

## Consequences

- Positive: `mechanics/` now exists as a checked skeleton.
- Positive: future work can distinguish `head-fed` and `local` mechanics before
  creating packages.
- Positive: package creation now has a template and validation route.
- Tradeoff: this creates route surfaces before moving payloads.
- Follow-up: promote the first local package only when the source surface and
  validation route are ready, likely `activation`, `review-gate`, or
  `scenario-composition`.

## Current Applicability

As of 2026-05-31:

- Still valid: this decision created the mechanics atlas and head/local roster
  split.
- Changed: later decisions promoted package-local mechanics and collapsed root
  mechanics control documents into `mechanics/README.md` and
  `mechanics/AGENTS.md`.
- Superseded by: AOA-PB-D-0014 for root mechanics file shape; still valid for
  the head-fed/local distinction and package-validation posture.

## Review Log

### 2026-05-31 - Initial skeleton

- Previous assumption: root design spine was enough before package movement.
- New reality: mechanics needs its own route skeleton before package
  promotion.
- Reason: common center-fed mechanics and local playbook-native mechanics need
  different acceptance rules.
- Source surfaces updated: `mechanics/`, root entrypoints, validators, and
  release checks.
- Validation: the owning executable validator, generated-freshness checks, relevant tests, and repository release gate.

## Boundaries

- This decision does not create operational child mechanic packages.
- This decision does not move flat docs into mechanics.
- This decision does not move authored playbooks.
- This decision does not make center mechanics playbook-owned.
- This decision does not make local playbook mechanics center-wide law.
- This decision does not move skill, technique, eval, memo, agent, routing,
  stats, KAG, runtime, or center truth into `aoa-playbooks`.

## Source Surfaces

- `mechanics/AGENTS.md`
- `mechanics/README.md`
- `scripts/validate_mechanics_skeleton.py`
- `scripts/release_check.py`
- `docs/decisions/AOA-PB-D-0014-collapse-mechanics-root-entrypoints.md`

## Follow-Up Route

Use this skeleton before creating any `mechanics/<slug>/` package. The first
real package should land with package-specific validation and a narrow owner
split, not as an empty directory.

## Verification

Verification is owned by the corresponding executable validators and the repository release gate; focused invocation lives in the nearest `AGENTS.md`.
