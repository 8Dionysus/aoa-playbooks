# Move Antifragility Payloads Into Mechanics Package

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0011
- Original date: 2026-05-31
- Surface classes: mechanic package, mechanic part, docs route, schema/example, validation guard, legacy/provenance, decision record
- Playbook routes: runtime-chaos-recovery
- Mechanic parents: antifragility
- Guard families: package route, source topology, legacy/provenance, validation guard, sibling-owner boundary, playbook source boundary
- Posture: accepted antifragility package

## Context

Antifragility pressure in `aoa-playbooks` was already larger than a docs note.
It had:

- stress-lane doctrine;
- stress-harvest doctrine;
- runtime-chaos wave posture;
- via negativa checklist;
- stress-lane and re-entry gate schemas;
- stress-lane and re-entry gate examples;
- focused tests and validator hooks;
- the source playbook `playbooks/operations/recovery/runtime-chaos-recovery/PLAYBOOK.md`.

Sibling repositories already treat `antifragility` as a center-fed mechanic
with owner-local packages. The playbook-local form should own degraded-lane and
re-entry choreography, not runtime repair or proof verdicts.

## Options Considered

1. Leave antifragility payloads scattered across root `docs/`, `schemas/`, and
   `examples/`.
2. Move the source `runtime-chaos-recovery` playbook into mechanics.
3. Move antifragility docs, schemas, and examples into
   `mechanics/antifragility/parts/`, keep the source playbook in `playbooks/`,
   and update validators/tests/docs to the package route.

## Decision

Choose option 3.

Create `mechanics/antifragility/` with:

- package `AGENTS.md`, `README.md`, `PARTS.md`, and `PROVENANCE.md`;
- parts for stress lanes, re-entry gates, stress harvest, runtime chaos wave 1,
  and via negativa;
- package-local `legacy/` index and distillation log for former root paths;
- `mechanics/antifragility/scripts/validate_antifragility_package.py`;
- focused test and release-check wiring.

## Rationale

Antifragility payloads are repeatable mechanics, not root docs sprawl.

Moving docs, schemas, and examples into package parts makes the operation map
visible: stress input, degraded lane, re-entry gate, harvest, owner handoff,
and validation.

The source playbook stays in `playbooks/` because authored scenario canon is
not a mechanics payload.

## Consequences

- Positive: antifragility is now the first package-active head-fed mechanic in
  `aoa-playbooks`.
- Positive: stress-lane and re-entry schemas/examples are part-local and
  validated.
- Positive: former root paths are recorded through package provenance and
  legacy index.
- Tradeoff: public docs/examples/schema paths changed from root to package
  routes.
- Follow-up: continue the placement audit with the larger `agon` package only
  after its owner split is explicit.

## Current Applicability

As of 2026-05-31:

- Still valid: `mechanics/antifragility/` owns playbook-local stress and
  re-entry payloads.
- Changed: `mechanics/HEAD_MECHANICS.md` marks `antifragility` as
  `package-active`.
- Superseded by: none.

## Review Log

### 2026-05-31 - Antifragility package landing

- Previous assumption: antifragility was ready-for-package but still scattered
  across root docs, schemas, and examples.
- New reality: antifragility has package cards, part map, provenance bridge,
  moved docs/schemas/examples, package validator, focused tests, and
  release-check wiring.
- Reason: stress-lane and re-entry posture are repeatable playbook-layer
  mechanics with clear stronger-owner boundaries.
- Source surfaces updated: `mechanics/antifragility/`, `README.md`,
  `docs/README.md`, `DESIGN.md`, `DESIGN.AGENTS.md`, `ROADMAP.md`,
  `scripts/validate_playbooks.py`, `scripts/release_check.py`, source playbook
  refs, and focused tests.
- Validation:
  `python mechanics/antifragility/scripts/validate_antifragility_package.py`,
  `python scripts/validate_playbooks.py`, and focused pytest.

## Boundaries

- This decision does not move authored playbook canon out of `playbooks/`.
- This decision does not claim runtime repair authority.
- This decision does not claim proof verdicts, memory truth, KAG health truth,
  route dispatch, or role authority.
- This decision does not create a root `legacy/` directory.

## Source Surfaces

- `mechanics/antifragility/AGENTS.md`
- `mechanics/antifragility/README.md`
- `mechanics/antifragility/PARTS.md`
- `mechanics/antifragility/PROVENANCE.md`
- `mechanics/antifragility/parts/stress-lanes/docs/playbook-stress-lanes.md`
- `mechanics/antifragility/parts/stress-lanes/schemas/playbook_stress_lane_v1.json`
- `mechanics/antifragility/parts/stress-lanes/examples/`
- `mechanics/antifragility/parts/reentry-gates/schemas/playbook_reentry_gate_v1.json`
- `mechanics/antifragility/parts/reentry-gates/examples/`
- `mechanics/antifragility/parts/stress-harvest/docs/playbook-stress-harvest.md`
- `mechanics/antifragility/parts/runtime-chaos-wave1/docs/playbook-stress-chaos-wave1.md`
- `mechanics/antifragility/parts/via-negativa/docs/via-negativa-checklist.md`
- `mechanics/antifragility/scripts/validate_antifragility_package.py`
- `playbooks/operations/recovery/runtime-chaos-recovery/PLAYBOOK.md`
- `tests/test_antifragility_mechanics_package.py`
- `tests/test_antifragility_public_surface.py`
- `tests/test_runtime_chaos_recovery.py`

## Follow-Up Route

Continue with `agon` only after mapping trial, campaign, recurrence-manifest,
quest, playbook-source, generated-registry, schema/example, and builder
ownership separately.

## Verification

```bash
python mechanics/antifragility/scripts/validate_antifragility_package.py
python scripts/validate_mechanics_skeleton.py
python scripts/generate_decision_indexes.py --check
python scripts/validate_playbooks.py
python -m pytest -q tests/test_antifragility_mechanics_package.py tests/test_antifragility_public_surface.py tests/test_runtime_chaos_recovery.py
```
