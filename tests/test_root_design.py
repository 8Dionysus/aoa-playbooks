from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_root_design.py"
SPEC = importlib.util.spec_from_file_location("validate_root_design", SCRIPT_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_minimal_required_tree(repo_root: Path) -> None:
    _write(repo_root / "DESIGN.md", "\n".join(validator.DESIGN_REQUIRED_TOKENS))
    _write(
        repo_root / "DESIGN.AGENTS.md",
        "\n".join(validator.DESIGN_AGENTS_REQUIRED_TOKENS),
    )
    for relative_path, tokens in validator.ROOT_ENTRYPOINT_REQUIRED_TOKENS.items():
        _write(repo_root / relative_path, "\n".join(tokens))


class RootDesignValidationTests(unittest.TestCase):
    def test_current_root_design_surfaces_pass(self) -> None:
        result = validator.validate(validator.REPO_ROOT)
        self.assertEqual((), result.issues)

    def test_minimal_required_tree_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            result = validator.validate(repo_root)
            self.assertEqual((), result.issues)

    def test_missing_design_file_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            (repo_root / "DESIGN.md").unlink()
            result = validator.validate(repo_root)
            self.assertIn("DESIGN.md: file is missing", result.issues)

    def test_root_entrypoint_must_route_to_design_surfaces(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(repo_root / "README.md", "DESIGN.md\n")
            result = validator.validate(repo_root)
            self.assertIn(
                "README.md: missing required token 'DESIGN.AGENTS.md'",
                result.issues,
            )

    def test_desgin_typo_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(repo_root / "ROADMAP.md", "DESIGN.md\nDESIGN.AGENTS.md\nDESGIN.md\n")
            result = validator.validate(repo_root)
            self.assertIn(
                "ROADMAP.md: contains forbidden typo token 'DESGIN.md'",
                result.issues,
            )


if __name__ == "__main__":
    unittest.main()
