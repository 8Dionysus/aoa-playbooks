# Move Real-Run Harvest Evidence Into Package Parts

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0010
- Original date: 2026-05-31
- Surface classes: mechanic package, docs route, validation guard, evidence boundary, decision record, package-local payload
- Playbook routes: none
- Mechanic parents: real-run-harvest
- Guard families: package route, source topology, evidence boundary, validation guard, sibling-owner boundary, generated/read-model
- Posture: accepted package-local evidence store

## Context

The review-gate split made one boundary explicit: readout builders belong to the
review-gate mechanic, while reviewed-run evidence and harvest templates belong
to the real-run-harvest mechanic.

The source evidence paths were historically scattered under root docs, examples,
and config:

- `docs/real-runs/`
- `docs/gate-reviews/`
- `examples/harvests/`
- `examples/alpha_harvests/`
- `docs/alpha-readiness/`
- `docs/alpha-reviewed-runs/`
- `config/phase_alpha_curated_core.json`

These are not root-layer doctrine. They are mechanic-owned evidence stores and
source templates, so their active home is package-local.

## Options Considered

1. Keep evidence directories under root and only document their route.
2. Leave real-run harvest as a candidate-only roster row.
3. Move evidence, templates, alpha readiness notes, and Phase Alpha config into
   `mechanics/real-run-harvest/parts/...`, then update generators, validators,
   generated refs, provenance, and tests.

## Decision

Choose option 3.

Create `mechanics/real-run-harvest/` with package route files, provenance, and a
package validator. Move the active payloads into:

- `parts/reviewed-run-source-store/docs/real-runs/`
- `parts/reviewed-run-source-store/docs/gate-reviews/`
- `parts/reviewed-run-source-store/docs/playbook-real-run-workflow.md`
- `parts/harvest-template-source-store/docs/playbook-real-run-harvest.md`
- `parts/harvest-template-source-store/examples/harvests/`
- `parts/harvest-template-source-store/examples/alpha_harvests/`
- `parts/phase-alpha-evidence-store/docs/alpha-readiness/`
- `parts/phase-alpha-evidence-store/docs/alpha-reviewed-runs/`
- `parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json`

Generated read models remain under root `generated/` because that is the public
readout plane. Root command wrappers may remain in `scripts/` as compatibility
entrypoints to package implementations.

## Rationale

The refactor follows the operation-map rule: role, input, output, owner, next
route, and validation should be explicit. Real-run harvest owns evidence
templates and reviewed-run source stores; review-gate owns status/packet/readout
projection; root `generated/` owns public read models.

Keeping mechanic payloads in root made the owner map ambiguous. Moving them into
package parts makes the source of truth match the architecture.

## Consequences

- Positive: real-run evidence, harvest templates, alpha readiness notes, and
  Phase Alpha config now have a package-local owner.
- Positive: generated refs can point to package-local source paths without
  pretending root docs/examples/config are the mechanic home.
- Positive: `real-run-harvest` is no longer an ambiguous candidate row.
- Tradeoff: downstream readers that assumed old root paths must follow updated
  generated source refs or compatibility wrappers.
- Follow-up: keep evidence-template validation strict enough to prevent the
  package from becoming proof storage, raw runtime trace storage, or memo truth.

## Current Applicability

As of 2026-05-31:

- Valid: real-run-harvest owns package-local evidence/source-store payloads.
- Valid: review-gate owns generated review/readiness builders and root public
  readouts.
- Superseded by: none.

## Review Log

### 2026-05-31 - Package-local evidence landing

- Previous assumption: evidence paths could be treated as root public source
  paths.
- New reality: the evidence and harvest source payloads moved under
  `mechanics/real-run-harvest/parts/...`.
- Source surfaces updated: `mechanics/real-run-harvest/`,
  `mechanics/review-gate/parts/*/scripts/`, `scripts/validate_playbooks.py`,
  generated review/Phase Alpha readouts, placement audit, release check, and
  focused tests.
- Validation:
  `python mechanics/real-run-harvest/scripts/validate_real_run_harvest_package.py`,
  review-status builder `--check`, Phase Alpha builder `--check`,
  `python scripts/validate_mechanics_skeleton.py`, decision index check,
  `python scripts/validate_playbooks.py`, and focused pytest.

## Boundaries

- This decision does not move authored playbooks.
- This decision does not move generated public read models out of `generated/`.
- This decision does not claim proof verdicts, raw runtime trace storage, memo
  truth, eval acceptance, or review-gate builder ownership.
- This decision does not create a root `legacy/` directory.

## Source Surfaces

- `mechanics/real-run-harvest/AGENTS.md`
- `mechanics/real-run-harvest/README.md`
- `mechanics/real-run-harvest/PARTS.md`
- `mechanics/real-run-harvest/PROVENANCE.md`
- `mechanics/real-run-harvest/scripts/validate_real_run_harvest_package.py`
- `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`
- `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`
- `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests/`
- `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/alpha_harvests/`
- `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-readiness/`
- `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-reviewed-runs/`
- `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json`
- `scripts/release_check.py`
- `tests/test_real_run_harvest_mechanics_package.py`

## Verification

```bash
python mechanics/real-run-harvest/scripts/validate_real_run_harvest_package.py
python mechanics/review-gate/parts/review-status/scripts/generate_playbook_review_status.py --check
python mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py --check
python scripts/validate_mechanics_skeleton.py
python scripts/generate_decision_indexes.py --check
python scripts/validate_playbooks.py
```
