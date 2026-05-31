# Move Review Gate Builders Into Mechanics Package

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0009
- Original date: 2026-05-31
- Surface classes: mechanic package, mechanic part, generated/readout, validation guard, legacy/provenance, decision record
- Playbook routes: none
- Mechanic parents: review-gate
- Guard families: package route, generated/read-model, legacy/provenance, validation guard, evidence boundary, release/tooling
- Posture: accepted review-gate package

## Context

Review-gate pressure was mixed across root scripts, root generated outputs,
review evidence directories, Phase Alpha config, and real-run harvest docs.

The old flat placement made it hard to see which layer owned what:

- reviewed-run and gate-review notes are source evidence;
- Phase Alpha config and readiness notes are source readiness surfaces;
- generated review, intake, packet, landing, and alpha outputs are root
  read models;
- root commands are public operator entrypoints;
- the builder implementations are repeatable mechanics.

## Options Considered

1. Leave every review builder in root `scripts/`.
2. Move evidence directories and generated outputs under `mechanics/review-gate/`.
3. Move review-gate builder implementations into package parts, keep root
   commands as compatibility wrappers, and keep evidence/config/generated paths
   root-public.

## Decision

Choose option 3.

Create `mechanics/review-gate/` with:

- package `AGENTS.md`, `README.md`, `PARTS.md`, and `PROVENANCE.md`;
- part-local builder implementations for review status, review packet
  contracts, review intake, landing governance, and Phase Alpha readiness;
- package-local `legacy/` index and distillation log for former root builder
  paths;
- `mechanics/review-gate/scripts/validate_review_gate_package.py`;
- root `scripts/generate_*` compatibility wrappers for the moved builders.

## Rationale

This follows the mechanics package pattern without breaking public root
contracts.

The active mechanic is the repeatable computation from source evidence and
config into generated read models. That belongs in `mechanics/review-gate/`.

The generated outputs remain root-public because downstream readers cite those
paths as read models. Evidence/source-store paths belong to
`mechanics/real-run-harvest/parts/...` and feed review-gate builders from there.

## Consequences

- Positive: review-gate is now an operational local mechanics package.
- Positive: package-local provenance records former root builder paths.
- Positive: root command compatibility and generated output paths are
  preserved.
- Positive: Phase Alpha readiness builder has an explicit package part.
- Positive: review schemas now live in review-gate package parts.
- Follow-up: tighten real-run-harvest posture and then continue with the next
  package candidate such as antifragility.

## Current Applicability

As of 2026-05-31:

- Still valid: review-gate owns builder implementation routes, not evidence or
  proof truth.
- Changed: `mechanics/LOCAL_MECHANICS.md` marks `review-gate` as
  `package-active`.
- Superseded by: none.

## Review Log

### 2026-05-31 - Review-gate implementation move

- Previous assumption: review-gate was candidate-only and mixed with
  real-run-harvest evidence.
- New reality: review-gate has a package card, part map, provenance bridge,
  moved builder implementations, compatibility wrappers, package validator,
  focused tests, and release-check wiring.
- Reason: review readout computation is a bounded local mechanic with clear
  source inputs and generated outputs.
- Source surfaces updated: `mechanics/review-gate/`,
  root `scripts/generate_playbook_review_*.py`,
  `scripts/generate_playbook_landing_governance.py`,
  `scripts/generate_phase_alpha_surfaces.py`, `scripts/release_check.py`,
  root design/readme surfaces, and package tests.
- Validation:
  `python mechanics/review-gate/scripts/validate_review_gate_package.py`,
  review builder `--check` commands, Phase Alpha builder `--check`,
  `python scripts/validate_mechanics_skeleton.py`, and focused pytest.

## Boundaries

- This decision does not move authored playbooks.
- This decision does not make review-gate the evidence owner; package-local
  evidence stores belong to real-run-harvest.
- This decision does not move root generated review or Phase Alpha outputs.
- This decision does not make root script compatibility the active
  implementation.
- This decision does not claim eval proof, memo truth, runtime execution, or
  sibling-owner authority.

## Source Surfaces

- `mechanics/review-gate/AGENTS.md`
- `mechanics/review-gate/README.md`
- `mechanics/review-gate/PARTS.md`
- `mechanics/review-gate/PROVENANCE.md`
- `mechanics/review-gate/parts/review-status/scripts/generate_playbook_review_status.py`
- `mechanics/review-gate/parts/review-packet-contracts/scripts/generate_playbook_review_packet_contracts.py`
- `mechanics/review-gate/parts/review-intake/scripts/generate_playbook_review_intake.py`
- `mechanics/review-gate/parts/landing-governance/scripts/generate_playbook_landing_governance.py`
- `mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py`
- `mechanics/review-gate/scripts/validate_review_gate_package.py`
- root compatibility wrappers under `scripts/`
- `scripts/release_check.py`
- `tests/test_review_gate_mechanics_package.py`

## Follow-Up Route

Keep `real-run-harvest` as the package-local evidence owner, then promote the
next bounded package candidate only after owner split and validator evidence.

## Verification

```bash
python mechanics/review-gate/scripts/validate_review_gate_package.py
python scripts/generate_playbook_review_status.py --check
python scripts/generate_playbook_review_packet_contracts.py --check
python scripts/generate_playbook_review_intake.py --check
python scripts/generate_playbook_landing_governance.py --check
python scripts/generate_phase_alpha_surfaces.py --check
python scripts/validate_mechanics_skeleton.py
python scripts/generate_decision_indexes.py --check
python scripts/validate_playbooks.py
```
