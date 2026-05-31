from __future__ import annotations

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "mechanics" / "review-gate" / "scripts" / "validate_review_gate_package.py"
SPEC = importlib.util.spec_from_file_location("validate_review_gate_package", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(validator)


def test_review_gate_package_validates() -> None:
    assert validator.validate(validator.REPO_ROOT) == []


def test_root_review_gate_commands_are_compatibility_wrappers() -> None:
    wrappers = (
        ("mechanics/review-gate/parts/review-status/scripts/generate_playbook_review_status.py", "review-status"),
        ("mechanics/review-gate/parts/review-packet-contracts/scripts/generate_playbook_review_packet_contracts.py", "review-packet-contracts"),
        ("mechanics/review-gate/parts/review-intake/scripts/generate_playbook_review_intake.py", "review-intake"),
        ("mechanics/review-gate/parts/landing-governance/scripts/generate_playbook_landing_governance.py", "landing-governance"),
        ("mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py", "phase-alpha-readiness"),
    )

    for relative_path, part_name in wrappers:
        text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        assert "mechanics" in text
        assert "review-gate" in text
        assert part_name in text
