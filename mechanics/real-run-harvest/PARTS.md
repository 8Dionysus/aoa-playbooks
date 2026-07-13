# Real-Run Harvest Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `reviewed-run-source-store` | keep reviewed-run summaries and gate verdicts bounded as package-local evidence | `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/` | `mechanics/real-run-harvest/scripts/validate_real_run_harvest_package.py` | package-local |
| `harvest-template-source-store` | keep harvest templates public and source-linked | `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests/`, `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/alpha_harvests/` | package validator plus review builders | package-local |
| `phase-alpha-evidence-store` | keep alpha readiness and reviewed-run refs explicit | `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json`, `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-readiness/`, `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-reviewed-runs/` | package validator plus `mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py` | package-local |

## Deferred payloads

Payloads moved into package-local parts in this package landing.

Package-local evidence paths are the active source-store paths and stay there
until a decision changes public compatibility.

## Part growth rule

A future part-local payload can be added only if it is a validator, contract,
or helper that strengthens package-local evidence posture without moving source
evidence out of root.
