from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class CurrentDirectionRoutesTestCase(unittest.TestCase):
    def test_root_entrypoints_route_to_roadmap(self) -> None:
        roadmap_path = REPO_ROOT / "ROADMAP.md"
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertTrue(roadmap_path.is_file())
        self.assertIn("ROADMAP.md", readme)
        self.assertIn("ROADMAP.md", agents)

    def test_root_entrypoints_route_to_design_spine(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        docs_map = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")

        for text in (readme, agents, docs_map, roadmap):
            self.assertIn("DESIGN.md", text)
            self.assertIn("DESIGN.AGENTS.md", text)


if __name__ == "__main__":
    unittest.main()
