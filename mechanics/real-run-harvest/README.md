# Real-Run Harvest Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | local, not head-fed |
| role | keep real-run and alpha-run evidence reviewable without turning this repo into runtime storage or proof authority |
| trigger | new reviewed-run summaries, harvest templates, alpha reviewed-run notes, readiness notes, or Phase Alpha config refs |
| playbooks owns | source-store posture, section/route expectations, and package-local evidence boundary |
| stronger owner split | runtime owns raw run artifacts; evals own proof verdicts; memo owns recall truth; review-gate owns generated readouts |
| inputs | `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/playbook-real-run-workflow.md`, `mechanics/real-run-harvest/parts/harvest-template-source-store/docs/playbook-real-run-harvest.md`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`, `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests/`, alpha readiness and reviewed-run paths |
| outputs | checked package-local evidence posture and handoff to review-gate readout builders |
| must not claim | proof verdict, runtime trace storage, memo truth, eval acceptance, or ownership of raw runtime evidence |
| validation | `python mechanics/real-run-harvest/scripts/validate_real_run_harvest_package.py` plus review-status and Phase Alpha builder `--check` commands |
| next route | package-local evidence note, harvest template, `mechanics/review-gate/`, or stronger owner repo |

## Active route

This package is active as a package-local evidence posture package.

Evidence directories are package-local. Generated review contracts, docs, and
operator workflows now cite those package-local paths.

## Functioning parts

- `reviewed-run-source-store`: `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/` and
  `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`.
- `harvest-template-source-store`: `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests/` and
  `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/alpha_harvests/`.
- `phase-alpha-evidence-store`: `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-readiness/`,
  `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-reviewed-runs/`, and `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json`.

## Source surfaces

- `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/playbook-real-run-workflow.md`
- `mechanics/real-run-harvest/parts/harvest-template-source-store/docs/playbook-real-run-harvest.md`
- `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`
- `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`
- `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests/`
- `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/alpha_harvests/`
- `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-readiness/`
- `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-reviewed-runs/`
- `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json`

## Owner boundary

This mechanic owns evidence posture and package-local routing. It does not own
the readout builders; those live in `mechanics/review-gate/`.

## Growth posture

The next safe growth is stricter evidence template validation around the
package-local evidence directories.
