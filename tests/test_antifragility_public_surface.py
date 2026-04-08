from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_json(relative_path: str) -> object:
    return json.loads((REPO_ROOT / relative_path).read_text(encoding="utf-8"))


class AntifragilityPublicSurfaceTests(unittest.TestCase):
    def test_stress_lane_examples_validate(self) -> None:
        surfaces = (
            (
                "schemas/playbook_stress_lane_v1.json",
                "examples/playbook_stress_lane.example.json",
            ),
            (
                "schemas/playbook_reentry_gate_v1.json",
                "examples/playbook_reentry_gate.example.json",
            ),
        )

        for schema_path, example_path in surfaces:
            with self.subTest(schema=schema_path, example=example_path):
                schema = load_json(schema_path)
                example = load_json(example_path)
                self.assertIsInstance(schema, dict)
                Draft202012Validator.check_schema(schema)
                Draft202012Validator(schema).validate(example)

    def test_stress_lane_surfaces_are_discoverable_and_bounded(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        lanes = (REPO_ROOT / "docs" / "PLAYBOOK_STRESS_LANES.md").read_text(encoding="utf-8")
        harvest = (REPO_ROOT / "docs" / "PLAYBOOK_STRESS_HARVEST.md").read_text(encoding="utf-8")

        self.assertIn("docs/PLAYBOOK_STRESS_LANES.md", readme)
        self.assertIn("docs/PLAYBOOK_STRESS_HARVEST.md", readme)
        self.assertIn("PLAYBOOK_STRESS_LANES", docs_readme)
        self.assertIn("PLAYBOOK_STRESS_HARVEST", docs_readme)

        for token in (
            "do not let playbooks replace source-owned receipts",
            "do not confuse scenario composition with proof or source meaning",
            "It is a named branch of the same recurring scenario.",
        ):
            self.assertIn(token, lanes)

        for token in (
            "do not let playbook harvest become the only record of what happened",
            "That decision should cite evidence, not mood.",
            "one machine-readable re-entry gate family",
        ):
            self.assertIn(token, harvest)

    def test_examples_target_existing_playbook(self) -> None:
        for example_path in (
            "examples/playbook_stress_lane.example.json",
            "examples/playbook_reentry_gate.example.json",
        ):
            with self.subTest(example=example_path):
                payload = load_json(example_path)
                assert isinstance(payload, dict)
                target = REPO_ROOT / payload["playbook_id"]
                self.assertTrue(target.is_file())


if __name__ == "__main__":
    unittest.main()
