from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATED_ROOT = REPO_ROOT / "generated"


def load_module(script_name: str):
    path = REPO_ROOT / "scripts" / script_name
    spec = importlib.util.spec_from_file_location(script_name.replace(".py", ""), path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


activation_builder = load_module("generate_playbook_activation_surfaces.py")
federation_builder = load_module("generate_playbook_federation_surfaces.py")
composition_builder = load_module("generate_playbook_composition_surfaces.py")


def load_generated(name: str):
    return json.loads((GENERATED_ROOT / name).read_text(encoding="utf-8"))


class PlaybookDownstreamFeedContractsTests(unittest.TestCase):
    def test_registry_surface_keeps_expected_contract(self) -> None:
        payload = load_generated("playbook_registry.min.json")

        self.assertEqual(set(payload.keys()), {"version", "layer", "playbooks"})
        self.assertEqual(payload["version"], 1)
        self.assertEqual(payload["layer"], "aoa-playbooks")
        self.assertIsInstance(payload["playbooks"], list)
        self.assertTrue(payload["playbooks"])

        ids = [item["id"] for item in payload["playbooks"]]
        self.assertEqual(ids, sorted(ids))
        self.assertEqual(len(ids), len(set(ids)))

        expected_keys = {
            "id",
            "name",
            "status",
            "summary",
            "scenario",
            "trigger",
            "prerequisites",
            "participating_agents",
            "required_skill_families",
            "evaluation_posture",
            "memory_posture",
            "fallback_mode",
            "expected_artifacts",
        }
        for item in payload["playbooks"]:
            self.assertTrue(expected_keys.issubset(item))

    def test_activation_surface_is_deterministic_list_contract(self) -> None:
        registry = activation_builder.read_registry()
        expected = activation_builder.build_activation_surfaces(registry)
        current = load_generated("playbook_activation_surfaces.min.json")

        self.assertEqual(current, expected)
        self.assertIsInstance(current, list)
        self.assertEqual(
            [item["playbook_id"] for item in current],
            list(activation_builder.ACTIVATION_PLAYBOOK_IDS),
        )

        base_keys = {
            "surface_type",
            "playbook_id",
            "name",
            "scenario",
            "trigger",
            "participating_agents",
            "required_skill_families",
            "expected_artifacts",
            "evaluation_posture",
            "memory_posture",
            "fallback_mode",
        }
        optional_keys = {
            "eval_anchors",
            "return_posture",
            "return_anchor_artifacts",
            "return_reentry_modes",
            "memo_recall_modes",
            "memo_scope_default",
            "memo_scope_ceiling",
            "memo_read_path",
            "memo_checkpoint_posture",
            "memo_source_route_policy",
        }
        for item in current:
            self.assertEqual(item["surface_type"], "playbook_activation_surface")
            self.assertTrue(base_keys.issubset(item))
            self.assertTrue(set(item).issubset(base_keys | optional_keys))

    def test_federation_surface_is_deterministic_list_contract(self) -> None:
        expected = federation_builder.build_federation_surfaces()
        current = load_generated("playbook_federation_surfaces.min.json")

        self.assertEqual(current, expected)
        self.assertIsInstance(current, list)
        self.assertEqual(
            [item["playbook_id"] for item in current],
            list(federation_builder.FEDERATION_PLAYBOOK_IDS),
        )

        base_keys = {
            "surface_type",
            "playbook_id",
            "name",
            "participating_agents",
            "memory_posture",
            "required_skills",
            "memo_contract_refs",
            "memo_writeback_targets",
        }
        optional_keys = {
            "eval_anchors",
            "memo_recall_modes",
            "memo_scope_default",
            "memo_scope_ceiling",
            "memo_read_path",
            "memo_checkpoint_posture",
            "memo_source_route_policy",
        }
        for item in current:
            self.assertEqual(item["surface_type"], "playbook_federation_surface")
            self.assertTrue(base_keys.issubset(item))
            self.assertTrue(set(item).issubset(base_keys | optional_keys))

    def test_composition_surfaces_match_builder_outputs(self) -> None:
        outputs = composition_builder.build_outputs()

        expected_paths = {
            "playbook_handoff_contracts.json",
            "playbook_failure_catalog.json",
            "playbook_subagent_recipes.json",
            "playbook_automation_seeds.json",
            "playbook_composition_manifest.json",
        }
        self.assertEqual({path.name for path in outputs}, expected_paths)

        for path, payload in outputs.items():
            current = load_generated(path.name)
            self.assertEqual(current, payload)

    def test_composition_surface_top_level_contracts_stay_stable(self) -> None:
        handoffs = load_generated("playbook_handoff_contracts.json")
        failures = load_generated("playbook_failure_catalog.json")
        recipes = load_generated("playbook_subagent_recipes.json")
        automation = load_generated("playbook_automation_seeds.json")
        manifest = load_generated("playbook_composition_manifest.json")

        self.assertEqual(
            set(handoffs.keys()),
            {"schema_version", "layer", "profile", "source_of_truth", "playbooks"},
        )
        self.assertEqual(
            set(failures.keys()),
            {"schema_version", "layer", "profile", "failures"},
        )
        self.assertEqual(
            set(recipes.keys()),
            {"schema_version", "layer", "profile", "recipes"},
        )
        self.assertEqual(
            set(automation.keys()),
            {"schema_version", "layer", "profile", "seeds"},
        )
        self.assertEqual(
            set(manifest.keys()),
            {
                "schema_version",
                "layer",
                "profile",
                "source_of_truth",
                "generated_files",
                "managed_playbooks",
                "composition_playbook_count",
                "total_playbook_count",
            },
        )

        self.assertEqual(handoffs["schema_version"], 1)
        self.assertEqual(failures["schema_version"], 1)
        self.assertEqual(recipes["schema_version"], 1)
        self.assertEqual(automation["schema_version"], 1)
        self.assertEqual(manifest["schema_version"], 1)

        self.assertEqual(
            manifest["generated_files"],
            [
                "generated/playbook_handoff_contracts.json",
                "generated/playbook_failure_catalog.json",
                "generated/playbook_subagent_recipes.json",
                "generated/playbook_automation_seeds.json",
                "generated/playbook_composition_manifest.json",
            ],
        )


if __name__ == "__main__":
    unittest.main()
