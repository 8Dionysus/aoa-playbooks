from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_nested_agents.py"
SPEC = importlib.util.spec_from_file_location("validate_nested_agents", SCRIPT_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

EXPECTED_PACK3_DOCS = {
    ".github/AGENTS.md",
    "Spark/AGENTS.md",
    "config/AGENTS.md",
    "examples/AGENTS.md",
    "schemas/AGENTS.md",
    "scripts/AGENTS.md",
    "tests/AGENTS.md",
    "stats/AGENTS.md",
    "mechanics/AGENTS.md",
    "evals/AGENTS.md",
    "kag/AGENTS.md",
}


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_minimal_required_tree(repo_root: Path) -> None:
    _write(repo_root / "AGENTS.md", "# AGENTS.md\nRoot guidance.\n")
    for rel_path, snippets in validator.REQUIRED_AGENTS_DOCS.items():
        _write(repo_root / rel_path, "# AGENTS.md\n" + "\n".join(snippets) + "\n")


class ValidateNestedAgentsTests(unittest.TestCase):
    def test_pack3_surface_map_is_required(self) -> None:
        self.assertTrue(EXPECTED_PACK3_DOCS.issubset(set(validator.REQUIRED_AGENTS_DOCS)))

    def test_minimal_required_tree_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            result = validator.validate(repo_root)
            self.assertEqual((), result.issues)

    def test_missing_root_agents_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = validator.validate(Path(tmp))
            self.assertIn("AGENTS.md: root guidance file is missing", result.issues)

    def test_missing_required_doc_fails(self) -> None:
        first_rel = next(iter(validator.REQUIRED_AGENTS_DOCS))
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            (repo_root / first_rel).unlink()
            result = validator.validate(repo_root)
            self.assertTrue(any(first_rel in issue for issue in result.issues))

    def test_missing_required_snippet_fails(self) -> None:
        first_rel = next(iter(validator.REQUIRED_AGENTS_DOCS))
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(repo_root / first_rel, "# AGENTS.md\nToo thin.\n")
            result = validator.validate(repo_root)
            self.assertTrue(any(first_rel in issue and "missing required snippet" in issue for issue in result.issues))

    def test_untracked_nested_agents_can_be_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(repo_root / "extra" / "AGENTS.md", "# AGENTS.md\nExtra.\n")
            result = validator.validate(repo_root, fail_on_untracked=True)
            self.assertTrue(any("untracked nested AGENTS.md" in issue for issue in result.issues))

    def test_mandatory_readme_route_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(
                repo_root / "AGENTS.md",
                "# AGENTS.md\n\n## Read before editing\n\n1. `README.md`\n",
            )

            result = validator.validate(repo_root)

            self.assertTrue(
                any("README.md must stay task-conditioned" in issue for issue in result.issues)
            )

    def test_unconditional_readme_directive_fails_without_legacy_heading(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(repo_root / "AGENTS.md", "# AGENTS.md\n\nRead `README.md` before editing.\n")

            result = validator.validate(repo_root)

            self.assertTrue(
                any("README.md must stay task-conditioned" in issue for issue in result.issues)
            )

    def test_task_conditioned_readme_route_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(
                repo_root / "AGENTS.md",
                "# AGENTS.md\n\n## Read before editing\n\n"
                "When public orientation changes, read `README.md`.\n",
            )

            result = validator.validate(repo_root)

            self.assertEqual((), result.issues)

    def test_bare_for_readme_scope_is_not_treated_as_task_conditioned(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            _write(
                repo_root / "AGENTS.md",
                "# AGENTS.md\n\n"
                "Read `README.md` for every task.\n"
                "Read `README.md` for setup.\n",
            )

            result = validator.validate(repo_root)

            self.assertIn(
                "AGENTS.md: README.md must stay task-conditioned; mandatory line(s): 3, 4",
                result.issues,
            )

    def test_advisory_can_become_strict(self) -> None:
        if not validator.ADVISORY_AGENT_DIRS:
            self.skipTest("repository has no advisory AGENTS.md candidates")
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            _write_minimal_required_tree(repo_root)
            (repo_root / validator.ADVISORY_AGENT_DIRS[0]).mkdir(parents=True, exist_ok=True)
            result = validator.validate(repo_root, strict_advisory=True)
            self.assertTrue(any("high-risk directory" in issue for issue in result.issues))


if __name__ == "__main__":
    unittest.main()
