# AGENTS.md

## Applies to

This card applies to `mechanics/review-gate/` and every nested path until a
nearer `AGENTS.md` narrows the lane.

## Role

`review-gate/` is the local mechanic for converting bounded playbook review
evidence into root-published review, intake, packet-contract, landing, and
Phase Alpha readiness read models.

It is class `local`. It protects the review operation inside
`aoa-playbooks` without owning runtime proof, memory truth, eval verdicts, or
source playbook canon.

## Route by task

- Readout change: use the exact part-local builder, its schema/config, and the
  root evidence/source surfaces it consumes.
- Package topology or provenance: use `README.md`, `PARTS.md`, and
  `PROVENANCE.md`.
- Repository topology or authority change: use `DESIGN.md`.

## Boundaries

- Source-authored playbooks stay in `playbooks/*/*/*/PLAYBOOK.md`.
- Reviewed run notes stay under `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`.
- Gate verdict notes stay under `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`.
- Phase Alpha evidence stays under `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-readiness/`,
  `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-reviewed-runs/`, `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/alpha_harvests/`, and
  `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json`.
- Generated review read models stay root-published under `generated/`.
- Root `scripts/generate_*` commands remain operator-facing compatibility
  wrappers.
- This package must not claim proof, runtime execution, memo recall, eval
  acceptance, sibling-owner truth, or composition source ownership.

## Validation

Run:

Run `VALIDATION.md` in this directory, then the common mechanics route in the root `VALIDATION.md`.

## Closeout

Report which review builder moved or changed, which root source paths were
retained, which generated read models were checked, and whether the
`real-run-harvest` boundary stayed intact.
