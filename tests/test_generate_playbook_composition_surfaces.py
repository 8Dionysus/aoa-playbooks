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
                "closeout-owner-follow-through-continuity",
                "source-truth-then-share",
                "atm10-bounded-change",
                "split-wave-cross-repo-rollout",
            ],
        )

    def test_multiline_decision_and_handoff_items_are_preserved(self) -> None:
        outputs = builder.build_outputs()
        payload = outputs[builder.PLAYBOOK_HANDOFF_CONTRACTS_PATH]
        playbook = next(
            item
            for item in payload["playbooks"]
            if item["name"] == "closeout-owner-follow-through-continuity"
        )

        self.assertIn(
            "Decide whether a bounded candidate should stay a harvest draft or close through quest promotion.",
            playbook["decision_points"],
        )
        self.assertIn(
            "`architect -> coder` after the reviewed source, owner handoff, owner repo, and next-surface boundary are explicit",
            playbook["handoffs"],
        )

    def test_recipe_and_seed_refs_resolve_to_known_playbooks_and_capabilities(self) -> None:
        outputs = builder.build_outputs()
        handoff_payload = outputs[builder.PLAYBOOK_HANDOFF_CONTRACTS_PATH]
        recipe_payload = outputs[builder.PLAYBOOK_SUBAGENT_RECIPES_PATH]
        automation_payload = outputs[builder.PLAYBOOK_AUTOMATION_SEEDS_PATH]
        capabilities = builder.load_capabilities_by_id()

        playbook_names = {item["name"] for item in handoff_payload["playbooks"]}
        capability_ids = set(capabilities)

        for recipe in recipe_payload["recipes"]:
            self.assertIn(recipe["playbook"], playbook_names)
            for role in recipe["roles"]:
                self.assertTrue(set(role["skills"]).issubset(capability_ids))

        for seed in automation_payload["seeds"]:
            self.assertIn(seed["playbook"], playbook_names)
            self.assertTrue(
                set(builder.normalize_handles(seed["skill_handles"])).issubset(
                    capability_ids
                )
            )

    def test_handoff_refs_resolve_to_capability_graph_nodes(self) -> None:
        outputs = builder.build_outputs()
        handoff_payload = outputs[builder.PLAYBOOK_HANDOFF_CONTRACTS_PATH]
        capabilities = builder.load_capabilities_by_id()

        for playbook in handoff_payload["playbooks"]:
            for handoff in playbook["upstream_skill_handoffs"]:
                capability_id = handoff["name"]
                self.assertIn(capability_id, capabilities)
                self.assertEqual(
                    handoff["ref"],
                    "../aoa-skills/generated/capability_graph.json"
                    f"#nodes/{capability_id}",
                )

    def test_projection_capability_requires_actionable_typed_node(self) -> None:
        capability = {
            "kind": "workflow",
            "contract_level": "executable",
            "abi": {},
            "binding": {},
            "owner": {},
            "lifecycle": {"state": "active"},
        }

        self.assertIsNone(builder.capability_projection_error(capability))

        for field in ("abi", "binding", "owner", "lifecycle"):
            invalid = dict(capability)
            invalid.pop(field)
            self.assertIsNotNone(builder.capability_projection_error(invalid))

        retired = dict(capability)
        retired["lifecycle"] = {"state": "retired"}
        self.assertEqual(
            builder.capability_projection_error(retired),
            "node is retired",
        )

        lifecycle_without_state = dict(capability)
        lifecycle_without_state["lifecycle"] = {}
        self.assertEqual(
            builder.capability_projection_error(lifecycle_without_state),
            "node lacks a lifecycle state",
        )

        non_actionable = dict(capability)
        non_actionable["kind"] = "concept"
        self.assertEqual(
            builder.capability_projection_error(non_actionable),
            "node kind is not actionable",
        )

    def test_recipe_only_capability_must_be_projectable(self) -> None:
        overrides = builder.load_composition_overrides()
        registry_by_name = builder.load_registry_by_name()
        frontmatter_by_name, _ = builder.load_authored_playbooks()
        capabilities = builder.load_capabilities_by_id()
        capability_id = "test.recipe-only-retired"
        retired = {
            "id": capability_id,
            "kind": "workflow",
            "contract_level": "executable",
            "abi": {},
            "binding": {},
            "owner": {},
            "lifecycle": {"state": "retired"},
        }
        capabilities[capability_id] = retired
        recipes = overrides["subagent_recipes"]
        self.assertIsInstance(recipes, list)
        recipe = next(
            item
            for item in recipes
            if item["name"] == "boundary-contract-split"
        )
        recipe["roles"][0]["skills"].append(capability_id)

        with self.assertRaisesRegex(
            builder.BuilderError,
            "subagent recipe 'boundary-contract-split'.*test.recipe-only-retired.*retired",
        ):
            builder.validate_overrides(
                overrides,
                registry_by_name=registry_by_name,
                frontmatter_by_name=frontmatter_by_name,
                capabilities_by_id=capabilities,
            )


if __name__ == "__main__":
    unittest.main()
