# AGENTS.md

## Applies to

This card applies to `mechanics/review-gate/` and every nested path until a
nearer `AGENTS.md` narrows the lane.

## Role

`review-gate/` is the local mechanic for converting bounded playbook review
evidence into root-published review, intake, packet-contract, landing, and
Phase Alpha readiness read models.

It is local, not head-fed. It protects the review operation inside
`aoa-playbooks` without owning runtime proof, memory truth, eval verdicts, or
source playbook canon.

## Read before editing

Read:

1. root `AGENTS.md`
2. `DESIGN.md`
3. `mechanics/AGENTS.md`
4. `mechanics/LOCAL_MECHANICS.md`
5. `mechanics/PLACEMENT_AUDIT.md`
6. this package `README.md`
7. `PARTS.md`
8. the part-local builder being changed
9. root evidence/source surfaces referenced by that builder

## Boundaries

- Source-authored playbooks stay in `playbooks/*/PLAYBOOK.md`.
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

```bash
python mechanics/review-gate/scripts/validate_review_gate_package.py
python mechanics/review-gate/parts/review-status/scripts/generate_playbook_review_status.py --check
python mechanics/review-gate/parts/review-packet-contracts/scripts/generate_playbook_review_packet_contracts.py --check
python mechanics/review-gate/parts/review-intake/scripts/generate_playbook_review_intake.py --check
python mechanics/review-gate/parts/landing-governance/scripts/generate_playbook_landing_governance.py --check
python mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py --check
python scripts/validate_playbooks.py
```

## Closeout

Report which review builder moved or changed, which root source paths were
retained, which generated read models were checked, and whether the
`real-run-harvest` boundary stayed intact.
