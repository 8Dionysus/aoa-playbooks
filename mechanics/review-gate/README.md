# Review Gate Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | local |
| role | turn bounded review evidence and review contracts into root-published playbook review read models |
| trigger | reviewed-run notes, gate-review verdicts, activation/federation outputs, Phase Alpha readiness config, or composition manifest posture changes |
| playbooks owns | review-status parsing, review packet contract projection, review intake projection, landing-governance readout, and Phase Alpha readiness readouts |
| stronger owner split | runtime owns live execution; evals own proof verdicts; memo owns memory truth; agents own agent-route authority; composition owns source composition manifest |
| inputs | `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`, `generated/playbook_activation_surfaces.min.json`, `generated/playbook_federation_surfaces.min.json`, `generated/playbook_composition_manifest.json`, `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json`, and root playbook registry |
| outputs | root-published `generated/playbook_review_status.min.json`, `generated/playbook_review_packet_contracts.min.json`, `generated/playbook_review_intake.min.json`, `generated/playbook_landing_governance.min.json`, `generated/phase_alpha_review_packets.min.json`, and `generated/phase_alpha_run_matrix.min.json` |
| must not claim | proof, runtime execution, eval acceptance, memory recall truth, source playbook authorship, or evidence-store relocation |
| validation | package executable owners; focused order in `AGENTS.md` |
| next route | part-local builder, root evidence/source store, `mechanics/real-run-harvest/`, generated read model, or stronger owner repo |

## Active route

The active builder implementations live under this package:

- `parts/review-status/scripts/generate_playbook_review_status.py`
- `parts/review-packet-contracts/scripts/generate_playbook_review_packet_contracts.py`
- `parts/review-intake/scripts/generate_playbook_review_intake.py`
- `parts/landing-governance/scripts/generate_playbook_landing_governance.py`
- `parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py`

The root commands in `scripts/` remain compatibility wrappers because README,
release checks, validators, and downstream operators already use those paths.

## Functioning parts

- `review-status`: parses reviewed-run and gate-review notes into the compact
  review status surface.
- `review-packet-contracts`: joins registry, activation, federation, review
  status, and eval template availability into review packet contracts.
- `review-intake`: converts packet contracts and status into intake targets.
- `landing-governance`: checks review-track landing posture against registry
  and composition membership.
- `phase-alpha-readiness`: projects curated Phase Alpha readiness packets and
  run matrix.

## Source surfaces

- `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`
- `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`
- `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-readiness/`
- `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-reviewed-runs/`
- `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests/`
- `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/alpha_harvests/`
- `mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json`
- root `generated/` review and Phase Alpha outputs
- root `scripts/generate_playbook_review_*.py`
- `mechanics/review-gate/parts/landing-governance/scripts/generate_playbook_landing_governance.py`
- `mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py`

## Owner boundary

Review gate surfaces are derived readers. They are weaker than authored
playbooks, evidence notes, source configs, and sibling-owner proof systems.

This package owns how the review read models are computed. It does not own the
truth of a real run, the proof status of evidence, or runtime behavior.

## Growth posture

The next safe growth is tightening package-local validators and only then
deciding whether schemas or examples can move without breaking the root-public
generated contracts.
