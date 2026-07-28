# Move Scenario Composition Builder Into Mechanics Package

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0007
- Original date: 2026-05-31
- Surface classes: mechanic package, mechanic part, generated/readout, config/source, validation guard, legacy/provenance, decision record
- Playbook routes: composition gates
- Mechanic parents: scenario-composition
- Guard families: package route, generated/read-model, legacy/provenance, validation guard, sibling-owner boundary, release/tooling
- Posture: accepted scenario-composition package

## Context

After the activation package proved the package-local implementation plus root
compatibility wrapper pattern, the next local package candidate was
`scenario-composition`.

Scenario composition already had a dedicated builder, root source config,
root-published generated read models, source docs, focused tests, and a
sibling-owner dependency on `aoa-skills` handoff contracts.

## Options Considered

1. Leave the composition builder in root `scripts/` until source config and
   generated outputs can move together.
2. Move generated composition outputs and source config into the package
   immediately.
3. Move the builder implementation into `mechanics/scenario-composition/` and
   keep root source config, root generated outputs, and root command path as
   public compatibility surfaces.

## Decision

Choose option 3.

Create `mechanics/scenario-composition/` with:

- package `AGENTS.md`, `README.md`, `PARTS.md`, and `PROVENANCE.md`;
- `parts/composition-surfaces/` for the active builder implementation;
- package-local `legacy/` index and distillation log for the former root
  script path;
- `mechanics/scenario-composition/scripts/validate_scenario_composition_package.py`;
- root `scripts/generate_playbook_composition_surfaces.py` as a compatibility
  wrapper.

## Rationale

The active mechanic belongs in `mechanics/scenario-composition/` because the
builder exists only to protect scenario-level handoff, failure, subagent,
automation, and manifest projections.

The root generated outputs remain root-published because downstream readers
consume their current paths.

The composition config is package-owned because generated source-of-truth fields
and operator docs should point at the package-local mechanic source.

## Consequences

- Positive: `scenario-composition` is now an operational local mechanics
  package.
- Positive: package-local provenance records the former root script path.
- Positive: root generated outputs and root command compatibility are preserved.
- Positive: composition docs, config, examples, and recurrence manifests now
  live in the package-local composition surface.
- Follow-up: promote `federation-closure` or split `review-gate` from
  `real-run-harvest`.

## Current Applicability

As of 2026-07-28:

- Still valid: scenario-composition builder implementation and source payloads
  are package-local.
- Changed: `mechanics/LOCAL_MECHANICS.md` marks `scenario-composition` as
  `package-active`.
- Changed: the former sibling dependency on
  `aoa-skills/generated/skill_handoff_contracts.json` is superseded by typed
  node IDs and ABI data from `aoa-skills/generated/capability_graph.json`.
  The `required_skills` field name remains only as a compatibility surface; its
  entries are capability graph IDs, not promises that every node is a callable
  skill.
- Superseded by: none.

## Review Log

### 2026-07-28 - Follow the semantic capability graph

- Observed mismatch: `aoa-skills` retired the 57-object skill handoff catalog
  when it adopted the semantic capability ecosystem, while this package still
  required the deleted generated file and legacy skill names.
- Correction: resolve composition and plan-contour requirements against exact
  capability graph node IDs, derive input/output tags from each node's typed
  ABI, and fail when a referenced node is absent, retired, non-actionable, or
  lacks ABI, binding, or owner data.
- Compatibility: retain the existing playbook `required_skills` and generated
  handoff field names during this correction. They carry typed capability IDs;
  a separately versioned playbook ABI decision is required before renaming
  those public fields.
- Boundary: `aoa-skills` continues to own capability meaning. `aoa-playbooks`
  owns scenario composition only, while `aoa-sdk` resolves and compiles those
  references without copying their semantics.

### 2026-05-31 - Scenario-composition implementation move

- Previous assumption: scenario-composition was candidate-only in the local
  roster.
- New reality: scenario-composition has a package card, part map, provenance
  bridge, moved builder implementation, compatibility wrapper, package
  validator, and focused tests.
- Reason: scenario composition is the next smallest local package after
  activation that can move implementation without moving public generated
  outputs.
- Source surfaces updated: `mechanics/scenario-composition/`,
  `scripts/generate_playbook_composition_surfaces.py`,
  `scripts/release_check.py`, root design/readme surfaces, and package tests.
- Validation: the owning executable validator, generated-freshness checks, relevant tests, and repository release gate.

## Boundaries

- This decision does not move authored playbooks.
- This decision does not move root generated composition read models.
- This decision does not move root composition source config.
- This decision does not move skill meaning from `aoa-skills`.
- This decision does not make root script compatibility the active
  implementation.

## Source Surfaces

- `mechanics/scenario-composition/AGENTS.md`
- `mechanics/scenario-composition/README.md`
- `mechanics/scenario-composition/PARTS.md`
- `mechanics/scenario-composition/PROVENANCE.md`
- `mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py`
- `mechanics/scenario-composition/scripts/validate_scenario_composition_package.py`
- `scripts/generate_playbook_composition_surfaces.py`
- `scripts/release_check.py`
- `tests/test_scenario_composition_mechanics_package.py`

## Follow-Up Route

Promote `federation-closure` with the same active implementation plus
root-public readout compatibility pattern, or split review evidence from
review readout before moving review-gate payloads.

## Verification

Verification is owned by the corresponding executable validators and the repository release gate; focused invocation lives in the nearest `AGENTS.md`.
