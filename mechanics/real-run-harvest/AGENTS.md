# AGENTS.md

## Applies to

This card applies to `mechanics/real-run-harvest/`.

## Role

`real-run-harvest/` is the local mechanic for keeping reviewed run evidence,
harvest templates, and Phase Alpha reviewed-run/readiness packets bounded as
source evidence surfaces.

It is class `local`. It validates the posture of package-local evidence
paths and hands readout generation to `mechanics/review-gate/`.

## Route by task

- Reviewed-run source or gate note: use the real-run workflow and exact
  evidence path.
- Harvest template: use the real-run harvest contract and exact example.
- Readout builder: follow the matching `mechanics/review-gate/` part and its
  source map.
- Package topology or evidence-store placement: use `README.md`.

## Boundaries

- Do not move `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`,
  `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-readiness/`, `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-reviewed-runs/`,
  `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests/`, or `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/alpha_harvests/` without a new
  compatibility decision.
- Do not turn evidence summaries into proof verdicts.
- Do not claim runtime, memo, eval, or source playbook authority.

## Validation

Run:

```bash
python mechanics/real-run-harvest/scripts/validate_real_run_harvest_package.py
python mechanics/review-gate/parts/review-status/scripts/generate_playbook_review_status.py --check
python mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py --check
python scripts/validate_playbooks.py
```

## Closeout

Report which evidence/source-store paths changed, whether any root path moved,
and whether review-gate generated surfaces were rechecked.
