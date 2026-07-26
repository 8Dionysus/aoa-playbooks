from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_mechanics_skeleton.py"
SPEC = importlib.util.spec_from_file_location("validate_mechanics_skeleton", SCRIPT_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_minimal_required_tree(repo_root: Path) -> None:
    for relative_path, tokens in validator.REQUIRED_ROOT_FILES.items():
        _write(repo_root / relative_path, "\n".join(tokens))
    for relative_path, tokens in validator.ROOT_ENTRYPOINT_REQUIRED_TOKENS.items():
        _write(repo_root / relative_path, "\n".join(tokens))


def _write_minimal_package(repo_root: Path, package_name: str = "activation", package_class: str = "local") -> Path:
    package = repo_root / "mechanics" / package_name
    _write(package / "AGENTS.md", "# AGENTS.md\n")
    _write(
        package / "README.md",
        "\n".join(
            (
                "## Mechanic card",
                f"| class | {package_class} |",
                "| role | test package |",
                "| validation | test validator |",
                "| next route | test route |",
            )
        ),
    )
    _write(package / "PARTS.md", "# Parts\n")
    _write(package / "PROVENANCE.md", "# Provenance\n")
    return package


class MechanicsSkeletonValidationTests(unittest.TestCase):
    def test_current_mechanics_skeleton_passes(self) -> None:
        result = validator.validate(validator.REPO_ROOT)
        self.assertEqual((), result.issues)

    def test_minimal_required_tree_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            result = validator.validate(repo_root)
            self.assertEqual((), result.issues)

    def test_extra_root_mechanics_markdown_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(repo_root / "mechanics" / "NOTES.md", "old root note\n")
            result = validator.validate(repo_root)
            self.assertIn("mechanics/NOTES.md: root mechanics markdown is forbidden", result.issues)

    def test_extra_root_mechanics_non_markdown_file_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(repo_root / "mechanics" / "NOTES.txt", "old root note\n")
            result = validator.validate(repo_root)
            self.assertIn("mechanics/NOTES.txt: root mechanics file is forbidden", result.issues)

    def test_entrypoints_must_route_to_mechanics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(repo_root / "README.md", "mechanics/README.md\n")
            result = validator.validate(repo_root)
            self.assertIn(
                "README.md: missing required token 'mechanics/AGENTS.md'",
                result.issues,
            )

    def test_root_holding_directory_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            (repo_root / "mechanics" / "_meta").mkdir()
            result = validator.validate(repo_root)
            self.assertIn("mechanics/_meta/: root mechanics holding directory is forbidden", result.issues)

    def test_future_child_package_requires_package_shape(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            package = repo_root / "mechanics" / "activation"
            _write(
                package / "README.md",
                "## Mechanic card\n| class | local |\n| role | test package |\n| validation | test validator |\n| next route | test route |\n",
            )
            result = validator.validate(repo_root)
            self.assertIn("mechanics/activation: child package missing AGENTS.md", result.issues)
            self.assertIn(
                "mechanics/activation: child package missing PARTS.md",
                result.issues,
            )
            self.assertIn(
                "mechanics/activation: child package missing PROVENANCE.md",
                result.issues,
            )

    def test_release_support_compact_package_embeds_parts_and_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            package = _write_minimal_package(repo_root, "release-support", "head-fed/local")
            (package / "PARTS.md").unlink()
            (package / "PROVENANCE.md").unlink()
            _write(
                package / "README.md",
                (package / "README.md").read_text(encoding="utf-8")
                + "\n## Parts\n\npart route\n\n## Provenance\n\nsource route\n",
            )
            result = validator.validate(repo_root)
            self.assertEqual((), result.issues)

    def test_other_packages_cannot_adopt_compact_tier_without_owner_proof(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            package = _write_minimal_package(repo_root, "activation", "local")
            (package / "PARTS.md").unlink()
            (package / "PROVENANCE.md").unlink()
            _write(
                package / "README.md",
                (package / "README.md").read_text(encoding="utf-8")
                + "\n## Parts\n\npart route\n\n## Provenance\n\nsource route\n",
            )
            result = validator.validate(repo_root)
            self.assertIn("mechanics/activation: child package missing PARTS.md", result.issues)
            self.assertIn("mechanics/activation: child package missing PROVENANCE.md", result.issues)

    def test_package_companions_must_be_a_pair(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            package = _write_minimal_package(repo_root, "activation", "local")
            (package / "PROVENANCE.md").unlink()
            result = validator.validate(repo_root)
            self.assertIn(
                "mechanics/activation: package companions must include both PARTS.md and PROVENANCE.md",
                result.issues,
            )

    def test_package_class_must_match_root_table(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(
                repo_root / "mechanics" / "README.md",
                "\n".join(validator.REQUIRED_ROOT_FILES["mechanics/README.md"])
                + "\n| Package | Class | Role |\n| --- | --- | --- |\n| `activation/` | head-fed/local | test |\n",
            )
            _write_minimal_package(repo_root, "activation", "local")
            result = validator.validate(repo_root)
            self.assertIn(
                "mechanics/activation/README.md: package class 'local' does not match mechanics/README.md class 'head-fed/local'",
                result.issues,
            )

    def test_mechanics_markdown_links_must_resolve(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            package = _write_minimal_package(repo_root, "activation", "local")
            _write(
                package / "README.md",
                (package / "README.md").read_text(encoding="utf-8") + "\n[missing](missing.md)\n",
            )
            result = validator.validate(repo_root)
            self.assertIn(
                "mechanics/activation/README.md: markdown link target is missing: 'missing.md'",
                result.issues,
            )

    def test_release_check_must_cover_package_validators(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            package = _write_minimal_package(repo_root, "activation", "local")
            _write(package / "scripts" / "validate_activation_package.py", "print('ok')\n")
            _write(repo_root / "scripts" / "release_check.py", "COMMANDS = []\n")
            result = validator.validate(repo_root)
            self.assertIn(
                "scripts/release_check.py: missing package validator mechanics/activation/scripts/validate_activation_package.py",
                result.issues,
            )

    def test_desgin_typo_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(
                repo_root / "mechanics" / "README.md",
                "\n".join(validator.REQUIRED_ROOT_FILES["mechanics/README.md"]) + "\nDESGIN.md\n",
            )
            result = validator.validate(repo_root)
            self.assertIn(
                "mechanics/README.md: contains forbidden typo token 'DESGIN.md'",
                result.issues,
            )

    def test_root_legacy_directory_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            (repo_root / "legacy").mkdir()
            result = validator.validate(repo_root)
            self.assertIn(
                "legacy/: root legacy directory is forbidden for mechanics accounting",
                result.issues,
            )


if __name__ == "__main__":
    unittest.main()
