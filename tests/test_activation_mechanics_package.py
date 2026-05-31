from __future__ import annotations

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "mechanics" / "activation" / "scripts" / "validate_activation_package.py"
SPEC = importlib.util.spec_from_file_location("validate_activation_package", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(validator)


def test_activation_package_validates() -> None:
    assert validator.validate(validator.REPO_ROOT) == []


def test_root_activation_command_is_compatibility_wrapper() -> None:
    wrapper = REPO_ROOT / "scripts" / "generate_playbook_activation_surfaces.py"
    text = wrapper.read_text(encoding="utf-8")

    assert "mechanics" in text
    assert "activation-surface" in text
    assert "build_activation_surfaces = _impl.build_activation_surfaces" in text
