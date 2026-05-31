# Review Gate Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `review-status` | build review status from reviewed-run notes and gate verdicts | `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`, `generated/playbook_registry.min.json` | `python mechanics/review-gate/parts/review-status/scripts/generate_playbook_review_status.py --check` | active |
| `review-packet-contracts` | join registry, activation, federation, review status, and eval template availability into packet contracts | `generated/playbook_registry.min.json`, activation/federation generated outputs, `generated/playbook_review_status.min.json`, `repo:aoa-evals/.../runtime_candidate_template_index.min.json` | `python mechanics/review-gate/parts/review-packet-contracts/scripts/generate_playbook_review_packet_contracts.py --check` | active |
| `review-intake` | derive accepted packets, gate targets, and reviewed-run targets for review intake | `generated/playbook_review_packet_contracts.min.json`, `generated/playbook_review_status.min.json`, `mechanics/activation/parts/activation-surface/examples/playbook_activation.*.example.json` | `python mechanics/review-gate/parts/review-intake/scripts/generate_playbook_review_intake.py --check` | active |
| `landing-governance` | expose review-track blockers before a playbook can be considered landed | review packet contracts, review intake, review status, composition manifest | `python mechanics/review-gate/parts/landing-governance/scripts/generate_playbook_landing_governance.py --check` | active |
| `phase-alpha-readiness` | project curated alpha review packets and run matrix | `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json`, alpha harvest/readiness/reviewed-run paths | `python mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py --check` | active |

## Boundary payloads

- Review schemas live in their review-gate package parts.
- Evidence notes live in `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`,
  `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-readiness/`, and `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-reviewed-runs/`.
- Harvest examples live under `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests/` and
  `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/alpha_harvests/`.
- Generated read models remain under root `generated/`.

## Part growth rule

A part can absorb more payload only when its validator proves:

- root public read-model compatibility is preserved or intentionally removed by
  decision;
- generated outputs remain byte-for-byte equivalent under `--check`;
- evidence/source-store paths are not silently moved;
- stronger owner boundaries stay visible in package docs.
