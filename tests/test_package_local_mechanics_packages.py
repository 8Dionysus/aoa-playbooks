from __future__ import annotations

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGES = (
    ("recurrence", "validate_recurrence_package.py"),
    ("checkpoint", "validate_checkpoint_package.py"),
    ("experience", "validate_experience_package.py"),
    ("release-support", "validate_release_support_package.py"),
    ("questbook", "validate_questbook_package.py"),
    ("rpg", "validate_rpg_package.py"),
    ("titan", "validate_titan_package.py"),
    ("portfolio-governance", "validate_portfolio_governance_package.py"),
)


def load_validator(slug: str, filename: str):
    path = REPO_ROOT / "mechanics" / slug / "scripts" / filename
    spec = importlib.util.spec_from_file_location(f"validate_{slug.replace('-', '_')}_package", path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_package_local_mechanics_packages_validate() -> None:
    for slug, filename in PACKAGES:
        validator = load_validator(slug, filename)
        assert validator.validate(validator.REPO_ROOT) == []


def test_package_local_mechanics_packages_do_not_open_legacy_without_moved_payload() -> None:
    for slug, _filename in PACKAGES:
        assert not (REPO_ROOT / "mechanics" / slug / "legacy").exists()
