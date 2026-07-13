# Move Activation Builder Into Mechanics Package

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0006
- Original date: 2026-05-31
- Surface classes: mechanic package, mechanic part, generated/readout, validation guard, legacy/provenance, decision record
- Playbook routes: none
- Mechanic parents: activation
- Guard families: package route, generated/read-model, legacy/provenance, validation guard, release/tooling
- Posture: accepted activation package

## Context

The placement audit identified `activation` as the safest first package
landing. It is local, has one dedicated builder, has a root-published generated
output, and already has clear source surfaces:

- `generated/playbook_registry.min.json`;
- authored `playbooks/*/*/*/PLAYBOOK.md`;
- root generated output `generated/playbook_activation_surfaces.min.json`;
- root command path `scripts/generate_playbook_activation_surfaces.py`.

The package needed to prove the package-local move pattern without breaking
operator commands, README verification routes, release checks, or downstream
tests that import the root script path.

## Options Considered

1. Leave the activation builder in root `scripts/` until every activation
   schema and example can move.
2. Move the root generated output into `mechanics/activation/` immediately.
3. Move the builder implementation, schema, docs, and examples into
   `mechanics/activation/` while keeping root generated output and root command
   path as public compatibility surfaces.

## Decision

Choose option 3.

Create `mechanics/activation/` with:

- package `AGENTS.md`, `README.md`, `PARTS.md`, and `PROVENANCE.md`;
- `parts/activation-surface/` for the active builder implementation;
- package-local `legacy/` index and distillation log for the former root
  script path;
- `mechanics/activation/scripts/validate_activation_package.py`;
- root `scripts/generate_playbook_activation_surfaces.py` as a compatibility
  wrapper.

## Rationale

The active mechanic belongs in `mechanics/activation/` because the builder
exists only to protect the activation projection.

The output remains root-published because downstream readers and validation
contracts consume `generated/playbook_activation_surfaces.min.json`.

The root command remains because operator docs and release checks should not
break while the implementation moves. That root command is a compatibility
wrapper, not an alternate source of truth.

## Consequences

- Positive: `activation` is now the first operational local mechanics package.
- Positive: package-local provenance records the former root script path.
- Positive: root generated output and root command compatibility are preserved.
- Positive: activation schema, docs, and examples now live in the package-local
  activation surface.
- Follow-up: use the same package-local implementation plus root-wrapper
  pattern for `scenario-composition` or `federation-closure`.

## Current Applicability

As of 2026-05-31:

- Still valid: activation builder implementation and source payloads are
  package-local.
- Changed: `mechanics/LOCAL_MECHANICS.md` marks `activation` as
  `package-active`.
- Superseded by: none.

## Review Log

### 2026-05-31 - Activation implementation move

- Previous assumption: activation was candidate-only in the local roster.
- New reality: activation has a package card, part map, provenance bridge,
  moved builder implementation, compatibility wrapper, package validator, and
  focused tests.
- Reason: activation is the smallest safe proof of the mechanics package move
  pattern.
- Source surfaces updated: `mechanics/activation/`,
  `scripts/generate_playbook_activation_surfaces.py`,
  `scripts/release_check.py`, root design/readme surfaces, and package tests.
- Validation: the owning executable validator, generated-freshness checks, relevant tests, and repository release gate.

## Boundaries

- This decision does not move authored playbooks.
- This decision does not move the root generated activation read model.
- This decision does not move activation examples or schema contracts.
- This decision does not make activation a runtime owner.
- This decision does not make root script compatibility the active
  implementation.

## Source Surfaces

- `mechanics/activation/AGENTS.md`
- `mechanics/activation/README.md`
- `mechanics/activation/PARTS.md`
- `mechanics/activation/PROVENANCE.md`
- `mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py`
- `mechanics/activation/scripts/validate_activation_package.py`
- `scripts/generate_playbook_activation_surfaces.py`
- `scripts/release_check.py`
- `tests/test_activation_mechanics_package.py`

## Follow-Up Route

Promote the next small local package, likely `scenario-composition` or
`federation-closure`, using the same active implementation plus root-public
readout compatibility pattern.

## Verification

Verification is owned by the corresponding executable validators and the repository release gate; focused invocation lives in the nearest `AGENTS.md`.
