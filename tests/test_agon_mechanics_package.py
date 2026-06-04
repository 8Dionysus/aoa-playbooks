from __future__ import annotations

import importlib.util
from pathlib import Path

from scripts.playbook_source_home import playbook_path_for_name


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "mechanics" / "agon" / "scripts" / "validate_agon_package.py"
SPEC = importlib.util.spec_from_file_location("validate_agon_package", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(validator)


def test_agon_package_validates() -> None:
    assert validator.validate(validator.REPO_ROOT) == []


def test_agon_source_playbooks_stay_in_playbooks() -> None:
    assert playbook_path_for_name("agon-broken-trace-trial", REPO_ROOT).is_file()
    assert playbook_path_for_name("agon-expensive-summon-intent-trial", REPO_ROOT).is_file()
    assert not (REPO_ROOT / "mechanics" / "agon" / "playbooks").exists()
