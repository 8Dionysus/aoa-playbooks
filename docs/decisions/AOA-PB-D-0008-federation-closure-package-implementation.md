# Move Federation Closure Builder Into Mechanics Package

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0008
- Original date: 2026-05-31
- Surface classes: mechanic package, mechanic part, generated/readout, validation guard, legacy/provenance, decision record
- Playbook routes: none
- Mechanic parents: federation-closure
- Guard families: package route, generated/read-model, legacy/provenance, validation guard, sibling-owner boundary, release/tooling
- Posture: accepted federation-closure package

## Context

After activation and scenario-composition proved the package-local
implementation plus root compatibility wrapper pattern, `federation-closure`
was the next small local package candidate.

It had one dedicated builder, a root-published generated output, and a clear
stronger-owner boundary: it checks cross-repo closure without owning skill,
eval, memo, agent, routing, or runtime truth.

## Options Considered

1. Leave the federation builder in root `scripts/` until schema movement is
   ready.
2. Move the root generated output and schema into `mechanics/federation-closure/`.
3. Move the builder implementation and schema into
   `mechanics/federation-closure/`, while keeping root generated output and root
   command path as public compatibility surfaces.

## Decision

Choose option 3.

Create `mechanics/federation-closure/` with:

- package `AGENTS.md`, `README.md`, `PARTS.md`, and `PROVENANCE.md`;
- `parts/federation-surfaces/` for the active builder implementation;
- package-local `legacy/` index and distillation log for the former root
  script path;
- `mechanics/federation-closure/scripts/validate_federation_closure_package.py`;
- root `scripts/generate_playbook_federation_surfaces.py` as a compatibility
  wrapper.

## Rationale

The active mechanic belongs in `mechanics/federation-closure/` because the
builder exists only to protect the federation closure projection.

The generated output remains root-published because downstream readers and
validators consume `generated/playbook_federation_surfaces.min.json`.

The root command remains because operator docs and release checks should not
break while the implementation moves.

## Consequences

- Positive: `federation-closure` is now an operational local mechanics
  package.
- Positive: package-local provenance records the former root script path.
- Positive: root generated output, schema path, and command compatibility are
  preserved.
- Tradeoff: federation schema remains a root path for now.
- Follow-up: split `review-gate` from `real-run-harvest`, or promote
  `antifragility` stress-lane contracts.

## Current Applicability

As of 2026-05-31:

- Still valid: federation-closure builder implementation is package-local.
- Changed: `mechanics/LOCAL_MECHANICS.md` marks `federation-closure` as
  `package-active`.
- Superseded by: none.

## Review Log

### 2026-05-31 - Federation-closure implementation move

- Previous assumption: federation-closure was candidate-only in the local
  roster.
- New reality: federation-closure has a package card, part map, provenance
  bridge, moved builder implementation, compatibility wrapper, package
  validator, and focused tests.
- Reason: federation closure is a bounded local package with clear
  stronger-owner stop-lines.
- Source surfaces updated: `mechanics/federation-closure/`,
  `scripts/generate_playbook_federation_surfaces.py`,
  `scripts/release_check.py`, root design/readme surfaces, and package tests.
- Validation: the owning executable validator, generated-freshness checks, relevant tests, and repository release gate.

## Boundaries

- This decision does not move authored playbooks.
- This decision does not move the root generated federation read model.
- This decision does not move the root federation schema.
- This decision does not move sibling-owner truth into `aoa-playbooks`.
- This decision does not make root script compatibility the active
  implementation.

## Source Surfaces

- `mechanics/federation-closure/AGENTS.md`
- `mechanics/federation-closure/README.md`
- `mechanics/federation-closure/PARTS.md`
- `mechanics/federation-closure/PROVENANCE.md`
- `mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py`
- `mechanics/federation-closure/scripts/validate_federation_closure_package.py`
- `scripts/generate_playbook_federation_surfaces.py`
- `scripts/release_check.py`
- `tests/test_federation_closure_mechanics_package.py`

## Follow-Up Route

Split `review-gate` from `real-run-harvest`, or promote `antifragility` with
stress-lane and re-entry contract validation.

## Verification

Verification is owned by the corresponding executable validators and the repository release gate; focused invocation lives in the nearest `AGENTS.md`.
