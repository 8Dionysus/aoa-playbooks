from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[1]
ANTIFRAGILITY_ROOT = REPO_ROOT / "mechanics" / "antifragility"
STRESS_LANE_SCHEMA = "mechanics/antifragility/parts/stress-lanes/schemas/playbook_stress_lane_v1.json"
REENTRY_GATE_SCHEMA = "mechanics/antifragility/parts/reentry-gates/schemas/playbook_reentry_gate_v1.json"
STRESS_LANE_DOC = ANTIFRAGILITY_ROOT / "parts" / "stress-lanes" / "docs" / "playbook-stress-lanes.md"
STRESS_HARVEST_DOC = ANTIFRAGILITY_ROOT / "parts" / "stress-harvest" / "docs" / "playbook-stress-harvest.md"
RUNTIME_CHAOS_DOC = (
    ANTIFRAGILITY_ROOT / "parts" / "runtime-chaos-wave1" / "docs" / "playbook-stress-chaos-wave1.md"
)


def load_json(relative_path: str) -> object:
    return json.loads((REPO_ROOT / relative_path).read_text(encoding="utf-8"))


class AntifragilityPublicSurfaceTests(unittest.TestCase):
    def test_stress_lane_examples_validate(self) -> None:
        surfaces = (
            (
                STRESS_LANE_SCHEMA,
                "mechanics/antifragility/parts/stress-lanes/examples/playbook_stress_lane.example.json",
            ),
            (
                REENTRY_GATE_SCHEMA,
                "mechanics/antifragility/parts/reentry-gates/examples/playbook_reentry_gate.example.json",
            ),
            (
                STRESS_LANE_SCHEMA,
                "mechanics/antifragility/parts/stress-lanes/examples/playbook_stress_lane.runtime-timeout-chaos.example.json",
            ),
            (
                REENTRY_GATE_SCHEMA,
                "mechanics/antifragility/parts/reentry-gates/examples/playbook_reentry_gate.runtime-timeout-chaos.example.json",
            ),
            (
                STRESS_LANE_SCHEMA,
                "mechanics/antifragility/parts/stress-lanes/examples/playbook_stress_lane.retrieval-outage-honesty.example.json",
            ),
            (
                REENTRY_GATE_SCHEMA,
                "mechanics/antifragility/parts/reentry-gates/examples/playbook_reentry_gate.retrieval-outage-honesty.example.json",
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
        lanes = STRESS_LANE_DOC.read_text(encoding="utf-8")
        harvest = STRESS_HARVEST_DOC.read_text(encoding="utf-8")
        chaos = RUNTIME_CHAOS_DOC.read_text(encoding="utf-8")

        self.assertIn("mechanics/antifragility/parts/stress-lanes/docs/playbook-stress-lanes.md", readme)
        self.assertIn("mechanics/antifragility/parts/stress-harvest/docs/playbook-stress-harvest.md", readme)
        self.assertIn("mechanics/antifragility/parts/runtime-chaos-wave1/docs/playbook-stress-chaos-wave1.md", readme)
        self.assertIn("antifragility/parts/stress-lanes", docs_readme)
        self.assertIn("antifragility/parts/stress-harvest", docs_readme)
        self.assertIn("antifragility/parts/runtime-chaos-wave1", docs_readme)

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

        for token in (
            "structured degraded lanes and explicit re-entry gates",
            "AOA-P-0032 runtime-chaos-recovery",
            "runtime repair implementation",
        ):
            self.assertIn(token, chaos)

    def test_examples_target_existing_playbook(self) -> None:
        for example_path in (
            "mechanics/antifragility/parts/stress-lanes/examples/playbook_stress_lane.example.json",
            "mechanics/antifragility/parts/reentry-gates/examples/playbook_reentry_gate.example.json",
            "mechanics/antifragility/parts/stress-lanes/examples/playbook_stress_lane.runtime-timeout-chaos.example.json",
            "mechanics/antifragility/parts/reentry-gates/examples/playbook_reentry_gate.runtime-timeout-chaos.example.json",
            "mechanics/antifragility/parts/stress-lanes/examples/playbook_stress_lane.retrieval-outage-honesty.example.json",
            "mechanics/antifragility/parts/reentry-gates/examples/playbook_reentry_gate.retrieval-outage-honesty.example.json",
        ):
            with self.subTest(example=example_path):
                payload = load_json(example_path)
                assert isinstance(payload, dict)
                target = REPO_ROOT / payload["playbook_id"]
                self.assertTrue(target.is_file())


if __name__ == "__main__":
    unittest.main()
