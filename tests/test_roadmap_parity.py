from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class RoadmapParityTestCase(unittest.TestCase):
    def test_roadmap_matches_current_portfolio_and_generated_surfaces(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        portfolio = (REPO_ROOT / "docs" / "PLAYBOOK_PORTFOLIO.md").read_text(
            encoding="utf-8"
        )
        registry = json.loads(
            (REPO_ROOT / "generated" / "playbook_registry.min.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertIn("v0.3.1", readme)
        self.assertIn("v0.3.1", roadmap)

        registry_ids = {playbook["id"] for playbook in registry["playbooks"]}
        for playbook_id in (
            "AOA-P-0001",
            "AOA-P-0002",
            "AOA-P-0003",
            "AOA-P-0004",
            "AOA-P-0005",
            "AOA-P-0025",
            "AOA-P-0026",
            "AOA-P-0027",
            "AOA-P-0028",
            "AOA-P-0029",
            "AOA-P-0030",
        ):
            self.assertIn(playbook_id, registry_ids)

        self.assertIn("AOA-P-0001", roadmap)
        self.assertIn("AOA-P-0005", roadmap)
        for playbook_id in (
            "AOA-P-0025",
            "AOA-P-0026",
            "AOA-P-0027",
            "AOA-P-0028",
            "AOA-P-0029",
            "AOA-P-0030",
        ):
            self.assertIn(playbook_id, roadmap)

        for surface_name in (
            "playbook_activation_surfaces.min.json",
            "playbook_federation_surfaces.min.json",
            "playbook_review_status.min.json",
            "playbook_review_intake.min.json",
            "playbook_review_packet_contracts.min.json",
            "playbook_landing_governance.min.json",
            "playbook_handoff_contracts.json",
            "playbook_failure_catalog.json",
            "playbook_automation_seeds.json",
            "playbook_subagent_recipes.json",
        ):
            self.assertTrue((REPO_ROOT / "generated" / surface_name).is_file())
            self.assertIn(surface_name, roadmap)

        self.assertIn("AOA-P-0025", portfolio)
        self.assertIn("AOA-P-0026", portfolio)
        self.assertIn("AOA-P-0027", portfolio)
        self.assertIn("AOA-P-0028", portfolio)
        self.assertIn("AOA-P-0029", portfolio)
        self.assertIn("AOA-P-0030", portfolio)
        self.assertIn("docs/CODEX_PLANE_ROLLOUT_CYCLE.md", readme)
        self.assertIn("docs/CODEX_PLANE_ROLLOUT_CYCLE.md", roadmap)
        self.assertIn("QUESTBOOK.md", readme)
        self.assertIn("QUESTBOOK.md", roadmap)


if __name__ == "__main__":
    unittest.main()
