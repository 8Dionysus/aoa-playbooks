from __future__ import annotations

import importlib.util
from pathlib import Path

from scripts.mechanic_package_validator import validate_mechanic_package


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


def test_shared_validator_accepts_semantic_compact_package(tmp_path: Path) -> None:
    package = tmp_path / "mechanics" / "sample"
    package.mkdir(parents=True)
    (package / "AGENTS.md").write_text("# AGENTS.md\n", encoding="utf-8")
    (package / "README.md").write_text(
        "\n".join(
            (
                "## Mechanic card",
                "| class | local |",
                "| role | sample |",
                "| validation | sample check |",
                "| next route | sample owner |",
                "## Parts",
                "sample part",
                "## Provenance",
                "sample source",
            )
        ),
        encoding="utf-8",
    )
    assert validate_mechanic_package(repo_root=tmp_path, slug="sample", required_paths=()) == []


def test_shared_validator_rejects_incomplete_companion_pair(tmp_path: Path) -> None:
    package = tmp_path / "mechanics" / "sample"
    package.mkdir(parents=True)
    (package / "AGENTS.md").write_text("# AGENTS.md\n", encoding="utf-8")
    (package / "README.md").write_text(
        "\n".join(
            (
                "## Mechanic card",
                "| class | local |",
                "| role | sample |",
                "| validation | sample check |",
                "| next route | sample owner |",
            )
        ),
        encoding="utf-8",
    )
    (package / "PARTS.md").write_text("# Parts\n", encoding="utf-8")
    issues = validate_mechanic_package(repo_root=tmp_path, slug="sample", required_paths=())
    assert "mechanics/sample: package companions must include both PARTS.md and PROVENANCE.md" in issues


def _write_release_support_fixture(repo_root: Path, validator) -> None:
    for relative_path in validator.REQUIRED_ROOT_PATHS:
        path = repo_root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("", encoding="utf-8")
    package = repo_root / "mechanics" / "release-support"
    package.mkdir(parents=True, exist_ok=True)
    for filename in ("AGENTS.md", "README.md"):
        (package / filename).write_text(
            (REPO_ROOT / "mechanics" / "release-support" / filename).read_text(encoding="utf-8"),
            encoding="utf-8",
        )


def test_release_support_compact_contract_rejects_semantic_loss(tmp_path: Path) -> None:
    validator = load_validator("release-support", "validate_release_support_package.py")
    readme_tokens = (
        "accepted-input",
        "repo-release-gate",
        "deployment-and-installation",
        "rollback-and-regression",
        "promotion-and-retention",
    )
    agent_tokens = (
        "Do not move `scripts/release_check.py`",
        "Do not claim GitHub/CI authority",
        "Do not move release schemas/examples",
    )

    for index, token in enumerate(readme_tokens):
        repo_root = tmp_path / f"readme-{index}"
        _write_release_support_fixture(repo_root, validator)
        readme = repo_root / "mechanics" / "release-support" / "README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8").replace(token, "removed"),
            encoding="utf-8",
        )
        assert f"mechanics/release-support/README.md: missing token {token!r}" in validator.validate(repo_root)

    for index, token in enumerate(agent_tokens):
        repo_root = tmp_path / f"agents-{index}"
        _write_release_support_fixture(repo_root, validator)
        agents = repo_root / "mechanics" / "release-support" / "AGENTS.md"
        agents.write_text(
            agents.read_text(encoding="utf-8").replace(token, "removed", 1),
            encoding="utf-8",
        )
        assert f"mechanics/release-support/AGENTS.md: missing token {token!r}" in validator.validate(repo_root)
