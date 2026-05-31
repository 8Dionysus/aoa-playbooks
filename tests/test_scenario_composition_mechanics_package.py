from __future__ import annotations

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = (
    REPO_ROOT
    / "mechanics"
    / "scenario-composition"
    / "scripts"
    / "validate_scenario_composition_package.py"
)
SPEC = importlib.util.spec_from_file_location("validate_scenario_composition_package", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def test_scenario_composition_package_validates() -> None:
    assert validator.validate(validator.REPO_ROOT) == []


def test_root_composition_command_is_compatibility_wrapper() -> None:
    wrapper = REPO_ROOT / "scripts" / "generate_playbook_composition_surfaces.py"
    text = wrapper.read_text(encoding="utf-8")

    assert "mechanics" in text
    assert "composition-surfaces" in text
    assert "globals()[_name] = getattr(_impl, _name)" in text
