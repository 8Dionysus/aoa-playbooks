from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = REPO_ROOT / "scripts" / "generate_playbook_composition_surfaces.py"
BUILDER_SPEC = importlib.util.spec_from_file_location("generate_playbook_composition_surfaces", BUILDER_PATH)
if BUILDER_SPEC is None or BUILDER_SPEC.loader is None:
    raise RuntimeError(f"unable to load composition builder module from {BUILDER_PATH}")
builder = importlib.util.module_from_spec(BUILDER_SPEC)
BUILDER_SPEC.loader.exec_module(builder)


class GeneratePlaybookCompositionSurfacesTests(unittest.TestCase):
    def test_outputs_cover_expected_generated_files(self) -> None:
        outputs = builder.build_outputs()
        rendered_paths = {path.relative_to(REPO_ROOT).as_posix() for path in outputs}

        self.assertEqual(
            rendered_paths,
            {
                "generated/playbook_handoff_contracts.json",
                "generated/playbook_failure_catalog.json",
                "generated/playbook_subagent_recipes.json",
                "generated/playbook_automation_seeds.json",
                "generated/playbook_composition_manifest.json",
            },
        )

    def test_handoff_contracts_cover_managed_playbooks_only(self) -> None:
        outputs = builder.build_outputs()
        payload = outputs[builder.PLAYBOOK_HANDOFF_CONTRACTS_PATH]
        self.assertIsInstance(payload, dict)
        playbooks = payload["playbooks"]

        self.assertEqual(
            [item["name"] for item in playbooks],
            [
                "bounded-change-safe",
                "infra-change-guarded",
                "invariants-first-refactor",
                "local-stack-diagnosis",
                "owner-first-capability-landing",
                "project-foundation-workspace-landing",
                "source-truth-then-share",
                "atm10-bounded-change",
                "split-wave-cross-repo-rollout",
            ],
        )

    def test_recipe_and_seed_refs_resolve_to_known_playbooks_and_skills(self) -> None:
        outputs = builder.build_outputs()
        handoff_payload = outputs[builder.PLAYBOOK_HANDOFF_CONTRACTS_PATH]
        recipe_payload = outputs[builder.PLAYBOOK_SUBAGENT_RECIPES_PATH]
        automation_payload = outputs[builder.PLAYBOOK_AUTOMATION_SEEDS_PATH]
        skill_handoffs = builder.load_skill_handoff_by_name()

        playbook_names = {item["name"] for item in handoff_payload["playbooks"]}
        skill_names = set(skill_handoffs)

        for recipe in recipe_payload["recipes"]:
            self.assertIn(recipe["playbook"], playbook_names)
            for role in recipe["roles"]:
                self.assertTrue(set(role["skills"]).issubset(skill_names))

        for seed in automation_payload["seeds"]:
            self.assertIn(seed["playbook"], playbook_names)
            self.assertTrue(set(builder.normalize_handles(seed["skill_handles"])).issubset(skill_names))


if __name__ == "__main__":
    unittest.main()
