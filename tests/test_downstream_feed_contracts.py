from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATED_ROOT = REPO_ROOT / "generated"
DOCS_ROOT = REPO_ROOT / "docs"


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
review_status_builder = load_module("generate_playbook_review_status.py")
review_packet_contract_builder = load_module("generate_playbook_review_packet_contracts.py")
review_intake_builder = load_module("generate_playbook_review_intake.py")
landing_governance_builder = load_module("generate_playbook_landing_governance.py")


def load_generated(name: str):
    return json.loads((GENERATED_ROOT / name).read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


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

    def test_review_status_surface_is_deterministic_and_keeps_live_verdicts(self) -> None:
        expected = review_status_builder.build_review_status_payload()
        current = load_generated("playbook_review_status.min.json")

        self.assertEqual(current, expected)
        self.assertEqual(
            set(current.keys()),
            {"schema_version", "layer", "source_of_truth", "playbooks"},
        )
        self.assertEqual(current["schema_version"], 1)
        self.assertEqual(current["layer"], "aoa-playbooks")
        self.assertEqual(
            current["source_of_truth"],
            {"reviewed_runs_dir": "docs/real-runs", "gate_reviews_dir": "docs/gate-reviews"},
        )

        by_id = {entry["playbook_id"]: entry for entry in current["playbooks"]}
        self.assertEqual(by_id["AOA-P-0017"]["gate_verdict"], "composition-landed")
        self.assertEqual(by_id["AOA-P-0017"]["reviewed_run_count"], 3)
        self.assertEqual(by_id["AOA-P-0021"]["gate_verdict"], "composition-landed")
        self.assertEqual(by_id["AOA-P-0021"]["reviewed_run_count"], 3)
        self.assertEqual(by_id["AOA-P-0023"]["gate_verdict"], "composition-landed")
        self.assertEqual(by_id["AOA-P-0023"]["reviewed_run_count"], 6)
        self.assertEqual(by_id["AOA-P-0024"]["gate_verdict"], "hold")
        self.assertEqual(by_id["AOA-P-0024"]["reviewed_run_count"], 1)
        self.assertEqual(by_id["AOA-P-0019"]["gate_verdict"], "hold")
        self.assertEqual(by_id["AOA-P-0019"]["reviewed_run_count"], 0)
        self.assertEqual(by_id["AOA-P-0020"]["gate_verdict"], "hold")
        self.assertEqual(by_id["AOA-P-0020"]["reviewed_run_count"], 0)

    def test_review_status_builder_rejects_stale_gate_review_refs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            generated_dir = repo_root / "generated"
            real_runs_dir = repo_root / "docs" / "real-runs"
            gate_reviews_dir = repo_root / "docs" / "gate-reviews"
            generated_dir.mkdir(parents=True, exist_ok=True)
            real_runs_dir.mkdir(parents=True, exist_ok=True)
            gate_reviews_dir.mkdir(parents=True, exist_ok=True)

            (generated_dir / "playbook_registry.min.json").write_text(
                json.dumps(
                    {
                        "version": 1,
                        "layer": "aoa-playbooks",
                        "playbooks": [
                            {
                                "id": "AOA-P-9999",
                                "name": "stale-review-status-example",
                                "scenario": "stale_review_status_example",
                            }
                        ],
                    },
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            (real_runs_dir / "2026-04-09.stale-review-status-example.md").write_text(
                "\n".join(
                    [
                        "## Run Header",
                        "AOA-P-9999",
                        "",
                        "## Entry Signal",
                        "signal",
                        "",
                        "## Boundary Summary",
                        "boundary",
                        "",
                        "## Required Artifacts",
                        "- artifact",
                        "",
                        "## Closure Class",
                        "closure",
                        "",
                        "## Follow-On Route",
                        "route",
                        "",
                        "## Composition Signals",
                        "- signal one",
                        "- signal two",
                        "",
                        "## Residual Risk",
                        "risk",
                        "",
                        "## Evidence Links",
                        "- evidence",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            (gate_reviews_dir / "stale-review-status-example.md").write_text(
                "\n".join(
                    [
                        "## Gate Header",
                        "AOA-P-9999",
                        "",
                        "## Minimum Evidence Threshold",
                        "- one reviewed run",
                        "",
                        "## Latest Reviewed Run",
                        "- docs/real-runs/2026-04-09.stale-review-status-example.md",
                        "- docs/real-runs/2026-04-08.stale-review-status-example.md",
                        "",
                        "## Dual Signal Check",
                        "- failure or follow-up",
                        "- adjunct candidate",
                        "",
                        "## Current Verdict",
                        "hold",
                        "",
                        "## Next Trigger",
                        "trigger",
                        "",
                    ]
                ),
                encoding="utf-8",
            )

            with (
                patch.object(review_status_builder, "REPO_ROOT", repo_root),
                patch.object(review_status_builder, "REGISTRY_PATH", generated_dir / "playbook_registry.min.json"),
                patch.object(review_status_builder, "REAL_RUN_SUMMARY_DIR", real_runs_dir),
                patch.object(review_status_builder, "GATE_REVIEW_DIR", gate_reviews_dir),
                self.assertRaisesRegex(
                    SystemExit,
                    "unexpected reviewed runs: docs/real-runs/2026-04-08.stale-review-status-example.md",
                ),
            ):
                review_status_builder.build_review_status_payload()

    def test_review_packet_contract_surface_is_deterministic_and_keeps_packet_posture(self) -> None:
        expected = review_packet_contract_builder.build_review_packet_contracts_payload()
        current = load_generated("playbook_review_packet_contracts.min.json")

        self.assertEqual(current, expected)
        self.assertEqual(
            set(current.keys()),
            {"schema_version", "layer", "source_of_truth", "playbooks"},
        )
        self.assertEqual(current["schema_version"], 1)
        self.assertEqual(current["layer"], "aoa-playbooks")

        by_id = {entry["playbook_id"]: entry for entry in current["playbooks"]}
        self.assertIn("AOA-P-0011", by_id)
        self.assertEqual(
            by_id["AOA-P-0011"]["candidate_packet_kinds"],
            [
                "memo_candidate",
                "runtime_evidence_selection_candidate",
                "artifact_hook_candidate",
            ],
        )
        self.assertEqual(by_id["AOA-P-0011"]["memo_runtime_surfaces"], ["approval_record"])
        self.assertEqual(
            by_id["AOA-P-0011"]["source_review_refs"],
            ["playbooks/bounded-change-safe/PLAYBOOK.md"],
        )
        self.assertIsNone(by_id["AOA-P-0011"]["gate_verdict"])

        self.assertEqual(by_id["AOA-P-0018"]["gate_verdict"], "hold")
        self.assertEqual(
            by_id["AOA-P-0018"]["source_review_refs"],
            [
                "playbooks/validation-driven-remediation/PLAYBOOK.md",
                "docs/gate-reviews/validation-driven-remediation.md",
                "docs/real-runs/2026-04-05.validation-driven-remediation.md",
            ],
        )
        self.assertEqual(by_id["AOA-P-0017"]["gate_verdict"], "composition-landed")
        self.assertEqual(
            by_id["AOA-P-0017"]["source_review_refs"],
            [
                "playbooks/split-wave-cross-repo-rollout/PLAYBOOK.md",
                "docs/gate-reviews/split-wave-cross-repo-rollout.md",
                "docs/real-runs/2026-03-21.split-wave-cross-repo-rollout.md",
                "docs/real-runs/2026-03-28.split-wave-cross-repo-rollout.md",
                "docs/real-runs/2026-04-07.split-wave-cross-repo-rollout.md",
            ],
        )
        self.assertEqual(by_id["AOA-P-0019"]["gate_verdict"], "hold")
        self.assertEqual(
            by_id["AOA-P-0019"]["source_review_refs"],
            [
                "playbooks/release-migration-cutover/PLAYBOOK.md",
                "docs/gate-reviews/release-migration-cutover.md",
            ],
        )
        self.assertEqual(by_id["AOA-P-0020"]["gate_verdict"], "hold")
        self.assertEqual(
            by_id["AOA-P-0020"]["source_review_refs"],
            [
                "playbooks/incident-recovery-routing/PLAYBOOK.md",
                "docs/gate-reviews/incident-recovery-routing.md",
            ],
        )
        self.assertEqual(by_id["AOA-P-0021"]["gate_verdict"], "composition-landed")
        self.assertEqual(
            by_id["AOA-P-0021"]["source_review_refs"],
            [
                "playbooks/owner-first-capability-landing/PLAYBOOK.md",
                "docs/gate-reviews/owner-first-capability-landing.md",
                "docs/real-runs/2026-04-07.owner-first-capability-landing.md",
                "docs/real-runs/2026-04-08.owner-first-capability-landing.md",
                "docs/real-runs/2026-04-08.owner-first-capability-landing.tos-graph-curation.md",
            ],
        )
        self.assertEqual(by_id["AOA-P-0023"]["gate_verdict"], "composition-landed")
        self.assertEqual(
            by_id["AOA-P-0023"]["source_review_refs"],
            [
                "playbooks/closeout-owner-follow-through-continuity/PLAYBOOK.md",
                "docs/gate-reviews/closeout-owner-follow-through-continuity.md",
                "docs/real-runs/2026-04-08.closeout-owner-follow-through-continuity.md",
                "docs/real-runs/2026-04-09.closeout-owner-follow-through-continuity.workspace-checkpoint-growth.md",
                "docs/real-runs/2026-04-13.closeout-owner-follow-through-continuity.aoa-kag-owner-followthrough.md",
                "docs/real-runs/2026-04-19.closeout-owner-follow-through-continuity.live-codex-finding-repair.md",
                "docs/real-runs/2026-04-20.closeout-owner-follow-through-continuity.aoa-evals-proof-gates.md",
                "docs/real-runs/2026-04-20.closeout-owner-follow-through-continuity.release-wave-closeout.md",
            ],
        )
        self.assertEqual(by_id["AOA-P-0024"]["gate_verdict"], "hold")
        self.assertEqual(
            by_id["AOA-P-0024"]["source_review_refs"],
            [
                "playbooks/federated-live-publisher-activation/PLAYBOOK.md",
                "docs/gate-reviews/federated-live-publisher-activation.md",
                "docs/real-runs/2026-04-07.federated-live-publisher-activation.md",
            ],
        )
        self.assertEqual(
            current["source_of_truth"],
            {
                "registry": "generated/playbook_registry.min.json",
                "activation": "generated/playbook_activation_surfaces.min.json",
                "federation": "generated/playbook_federation_surfaces.min.json",
                "review_status": "generated/playbook_review_status.min.json",
                "runtime_template_index": "repo:aoa-evals/generated/runtime_candidate_template_index.min.json",
            },
        )

    def test_review_track_docs_cover_all_live_review_status_playbooks(self) -> None:
        review_status = load_generated("playbook_review_status.min.json")
        review_ids = [entry["playbook_id"] for entry in review_status["playbooks"]]

        docs_by_path = {
            "docs/README.md": read_text(DOCS_ROOT / "README.md"),
            "docs/PLAYBOOK_OPERATIONAL_FAMILY.md": read_text(DOCS_ROOT / "PLAYBOOK_OPERATIONAL_FAMILY.md"),
            "docs/PLAYBOOK_PORTFOLIO.md": read_text(DOCS_ROOT / "PLAYBOOK_PORTFOLIO.md"),
            "docs/PLAYBOOK_GAP_MATRIX.md": read_text(DOCS_ROOT / "PLAYBOOK_GAP_MATRIX.md"),
        }

        for path_label, text in docs_by_path.items():
            for playbook_id in review_ids:
                self.assertIn(
                    playbook_id,
                    text,
                    msg=(
                        f"{path_label} must mention {playbook_id} while it remains live in "
                        "generated/playbook_review_status.min.json"
                    ),
                )

    def test_review_packet_contract_builder_rejects_missing_runtime_template_index(self) -> None:
        with self.assertRaisesRegex(
            SystemExit,
            "missing required file: generated/runtime_candidate_template_index.min.json",
        ):
            with patch.object(review_packet_contract_builder, "AOA_EVALS_ROOT", REPO_ROOT / ".missing-aoa-evals"):
                review_packet_contract_builder.build_review_packet_contracts_payload()

    def test_review_packet_contract_builder_rejects_missing_runtime_template_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            evals_root = Path(tmpdir) / "aoa-evals"
            template_index_path = evals_root / "generated" / "runtime_candidate_template_index.min.json"
            template_index_path.parent.mkdir(parents=True, exist_ok=True)
            template_index_path.write_text(
                json.dumps(
                    {
                        "templates": [
                            {
                                "eval_anchor": "runtime_evidence_selection.demo",
                                "source_example_ref": "examples/runtime_evidence_selection.demo.example.json",
                            }
                        ]
                    }
                )
                + "\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                SystemExit,
                "runtime candidate template source is unavailable: examples/runtime_evidence_selection.demo.example.json",
            ):
                with patch.object(review_packet_contract_builder, "AOA_EVALS_ROOT", evals_root):
                    review_packet_contract_builder.build_review_packet_contracts_payload()

    def test_review_intake_surface_is_deterministic_and_keeps_live_review_alignment(self) -> None:
        expected = review_intake_builder.build_review_intake_payload()
        current = load_generated("playbook_review_intake.min.json")

        self.assertEqual(current, expected)
        self.assertEqual(
            set(current.keys()),
            {"schema_version", "layer", "source_of_truth", "playbooks"},
        )
        self.assertEqual(current["schema_version"], 1)
        self.assertEqual(current["layer"], "aoa-playbooks")

        by_id = {entry["playbook_id"]: entry for entry in current["playbooks"]}
        self.assertEqual(by_id["AOA-P-0018"]["gate_verdict"], "hold")
        self.assertEqual(
            by_id["AOA-P-0018"]["review_outcome_targets"]["real_runs"],
            ["docs/real-runs/2026-04-05.validation-driven-remediation.md"],
        )
        self.assertEqual(
            by_id["AOA-P-0018"]["review_outcome_targets"]["gate_reviews"],
            ["docs/gate-reviews/validation-driven-remediation.md"],
        )
        self.assertEqual(by_id["AOA-P-0018"]["composition_posture"], "held-after-review")
        self.assertEqual(by_id["AOA-P-0017"]["gate_verdict"], "composition-landed")
        self.assertEqual(
            by_id["AOA-P-0017"]["review_outcome_targets"]["real_runs"],
            [
                "docs/real-runs/2026-03-21.split-wave-cross-repo-rollout.md",
                "docs/real-runs/2026-03-28.split-wave-cross-repo-rollout.md",
                "docs/real-runs/2026-04-07.split-wave-cross-repo-rollout.md",
            ],
        )
        self.assertEqual(
            by_id["AOA-P-0017"]["review_outcome_targets"]["gate_reviews"],
            ["docs/gate-reviews/split-wave-cross-repo-rollout.md"],
        )
        self.assertEqual(by_id["AOA-P-0017"]["composition_posture"], "landed")
        self.assertEqual(by_id["AOA-P-0021"]["gate_verdict"], "composition-landed")
        self.assertEqual(
            by_id["AOA-P-0021"]["review_outcome_targets"]["real_runs"],
            [
                "docs/real-runs/2026-04-07.owner-first-capability-landing.md",
                "docs/real-runs/2026-04-08.owner-first-capability-landing.md",
                "docs/real-runs/2026-04-08.owner-first-capability-landing.tos-graph-curation.md",
            ],
        )
        self.assertEqual(
            by_id["AOA-P-0021"]["review_outcome_targets"]["gate_reviews"],
            ["docs/gate-reviews/owner-first-capability-landing.md"],
        )
        self.assertEqual(by_id["AOA-P-0021"]["composition_posture"], "landed")
        self.assertEqual(by_id["AOA-P-0023"]["gate_verdict"], "composition-landed")
        self.assertEqual(
            by_id["AOA-P-0023"]["review_outcome_targets"]["real_runs"],
            [
                "docs/real-runs/2026-04-08.closeout-owner-follow-through-continuity.md",
                "docs/real-runs/2026-04-09.closeout-owner-follow-through-continuity.workspace-checkpoint-growth.md",
                "docs/real-runs/2026-04-13.closeout-owner-follow-through-continuity.aoa-kag-owner-followthrough.md",
                "docs/real-runs/2026-04-19.closeout-owner-follow-through-continuity.live-codex-finding-repair.md",
                "docs/real-runs/2026-04-20.closeout-owner-follow-through-continuity.aoa-evals-proof-gates.md",
                "docs/real-runs/2026-04-20.closeout-owner-follow-through-continuity.release-wave-closeout.md",
            ],
        )
        self.assertEqual(
            by_id["AOA-P-0023"]["review_outcome_targets"]["gate_reviews"],
            ["docs/gate-reviews/closeout-owner-follow-through-continuity.md"],
        )
        self.assertEqual(by_id["AOA-P-0023"]["composition_posture"], "landed")
        self.assertEqual(by_id["AOA-P-0024"]["gate_verdict"], "hold")
        self.assertEqual(
            by_id["AOA-P-0024"]["review_outcome_targets"]["real_runs"],
            ["docs/real-runs/2026-04-07.federated-live-publisher-activation.md"],
        )
        self.assertEqual(
            by_id["AOA-P-0024"]["review_outcome_targets"]["gate_reviews"],
            ["docs/gate-reviews/federated-live-publisher-activation.md"],
        )
        self.assertEqual(by_id["AOA-P-0024"]["composition_posture"], "held-after-review")
        self.assertEqual(by_id["AOA-P-0019"]["gate_verdict"], "hold")
        self.assertEqual(by_id["AOA-P-0019"]["composition_posture"], "awaiting-reviewed-run")
        self.assertEqual(by_id["AOA-P-0020"]["gate_verdict"], "hold")
        self.assertEqual(by_id["AOA-P-0020"]["composition_posture"], "awaiting-reviewed-run")

    def test_landing_governance_surface_is_deterministic_and_review_track_scoped(self) -> None:
        expected = landing_governance_builder.build_playbook_landing_governance_payload()
        current = load_generated("playbook_landing_governance.min.json")

        self.assertEqual(current, expected)
        self.assertEqual(
            set(current.keys()),
            {"schema_version", "layer", "scope", "source_of_truth", "playbooks"},
        )
        self.assertEqual(current["schema_version"], 1)
        self.assertEqual(current["layer"], "aoa-playbooks")
        self.assertEqual(current["scope"], "review-track")

        by_id = {entry["playbook_id"]: entry for entry in current["playbooks"]}
        self.assertNotIn("AOA-P-0001", by_id)
        self.assertTrue(by_id["AOA-P-0017"]["landing_passed"])
        self.assertEqual(by_id["AOA-P-0017"]["gate_verdict"], "composition-landed")
        self.assertTrue(by_id["AOA-P-0017"]["in_composition_manifest"])
        self.assertEqual(by_id["AOA-P-0017"]["registry_status"], "experimental")
        self.assertTrue(by_id["AOA-P-0021"]["landing_passed"])
        self.assertEqual(by_id["AOA-P-0021"]["gate_verdict"], "composition-landed")
        self.assertTrue(by_id["AOA-P-0021"]["in_composition_manifest"])
        self.assertEqual(by_id["AOA-P-0021"]["registry_status"], "experimental")
        self.assertTrue(by_id["AOA-P-0023"]["landing_passed"])
        self.assertEqual(by_id["AOA-P-0023"]["gate_verdict"], "composition-landed")
        self.assertTrue(by_id["AOA-P-0023"]["in_composition_manifest"])
        self.assertEqual(by_id["AOA-P-0023"]["registry_status"], "experimental")
        self.assertTrue(by_id["AOA-P-0024"]["landing_passed"])
        self.assertEqual(by_id["AOA-P-0024"]["gate_verdict"], "hold")
        self.assertFalse(by_id["AOA-P-0024"]["in_composition_manifest"])
        self.assertEqual(by_id["AOA-P-0024"]["registry_status"], "experimental")
        self.assertTrue(by_id["AOA-P-0018"]["landing_passed"])
        self.assertEqual(by_id["AOA-P-0018"]["gate_verdict"], "hold")
        self.assertFalse(by_id["AOA-P-0018"]["in_composition_manifest"])
        self.assertTrue(all(entry["landing_passed"] for entry in current["playbooks"]))
        self.assertTrue(all(entry["registry_status"] == "experimental" for entry in current["playbooks"]))
        self.assertTrue(all(entry["in_review_packet_contracts"] for entry in current["playbooks"]))
        self.assertTrue(all(entry["in_review_intake"] for entry in current["playbooks"]))


if __name__ == "__main__":
    unittest.main()
