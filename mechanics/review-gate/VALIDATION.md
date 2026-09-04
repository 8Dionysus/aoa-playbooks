# Validation routes

```bash
python mechanics/review-gate/scripts/validate_review_gate_package.py
python mechanics/review-gate/parts/review-status/scripts/generate_playbook_review_status.py --check
python mechanics/review-gate/parts/review-packet-contracts/scripts/generate_playbook_review_packet_contracts.py --check
python mechanics/review-gate/parts/review-intake/scripts/generate_playbook_review_intake.py --check
python mechanics/review-gate/parts/landing-governance/scripts/generate_playbook_landing_governance.py --check
python mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py --check
```
