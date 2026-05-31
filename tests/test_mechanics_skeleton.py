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

    def test_missing_head_roster_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            (repo_root / "mechanics" / "HEAD_MECHANICS.md").unlink()
            result = validator.validate(repo_root)
            self.assertIn("mechanics/HEAD_MECHANICS.md: file is missing", result.issues)

    def test_entrypoints_must_route_to_mechanics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(repo_root / "README.md", "mechanics/README.md\n")
            result = validator.validate(repo_root)
            self.assertIn(
                "README.md: missing required token 'mechanics/HEAD_MECHANICS.md'",
                result.issues,
            )

    def test_future_child_package_requires_package_shape(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            package = repo_root / "mechanics" / "activation"
            _write(package / "README.md", "## Mechanic card\nhead-fed\nlocal\nvalidation\n")
            result = validator.validate(repo_root)
            self.assertIn("mechanics/activation: child package missing AGENTS.md", result.issues)
            self.assertIn("mechanics/activation: child package missing PARTS.md", result.issues)
            self.assertIn("mechanics/activation: child package missing PROVENANCE.md", result.issues)

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
