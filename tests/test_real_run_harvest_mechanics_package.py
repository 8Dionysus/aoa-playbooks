from __future__ import annotations

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = (
    REPO_ROOT / "mechanics" / "real-run-harvest" / "scripts" / "validate_real_run_harvest_package.py"
)
SPEC = importlib.util.spec_from_file_location("validate_real_run_harvest_package", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(validator)


def test_real_run_harvest_package_validates() -> None:
    assert validator.validate(validator.REPO_ROOT) == []


def test_real_run_harvest_has_no_legacy_directory_without_moved_payload() -> None:
    assert not (REPO_ROOT / "mechanics" / "real-run-harvest" / "legacy").exists()
