from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "validate_playbooks.py"
SPEC = importlib.util.spec_from_file_location("validate_playbooks", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"unable to load validator module from {MODULE_PATH}")
validate_playbooks = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_playbooks)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class ValidatePlaybooksReturnContractTests(unittest.TestCase):
    def make_registry_entry(self) -> dict[str, object]:
        return {
            "id": "AOA-P-0008",
            "name": "long-horizon-model-tier-orchestra",
            "status": "experimental",
            "summary": "Coordinates a long-horizon route through explicit model-tier handoffs and guarded return posture.",
            "scenario": "model_tier_orchestration",
            "trigger": "long_horizon_or_high_cost_route",
            "prerequisites": ["tier_registry_defined"],
            "participating_agents": ["architect", "reviewer"],
            "required_skill_families": ["change-protocol", "review"],
            "evaluation_posture": "strict",
            "memory_posture": "bounded_recall",
            "fallback_mode": "handoff",
            "expected_artifacts": ["route_decision", "bounded_plan"],
            "return_posture": "artifact_anchor",
            "return_anchor_artifacts": ["route_decision", "bounded_plan"],
            "return_reentry_modes": ["previous_phase", "safe_stop"],
        }

    def test_valid_return_configuration_passes(self) -> None:
        payload = self.make_registry_entry()

        validate_playbooks.validate_return_configuration(payload, location="playbooks[0]")

    def test_missing_anchor_artifacts_fails(self) -> None:
        payload = self.make_registry_entry()
        payload.pop("return_anchor_artifacts")

        with self.assertRaisesRegex(
            validate_playbooks.ValidationError,
            "return_anchor_artifacts must be a non-empty list",
        ):
            validate_playbooks.validate_return_configuration(payload, location="playbooks[0]")

    def test_missing_reentry_modes_fails(self) -> None:
        payload = self.make_registry_entry()
        payload.pop("return_reentry_modes")

        with self.assertRaisesRegex(
            validate_playbooks.ValidationError,
            "return_reentry_modes must be a non-empty list",
        ):
            validate_playbooks.validate_return_configuration(payload, location="playbooks[0]")

    def test_invalid_reentry_mode_member_fails(self) -> None:
        payload = self.make_registry_entry()
        payload["return_reentry_modes"] = ["previous_phase", "invalid_mode"]

        with self.assertRaisesRegex(
            validate_playbooks.ValidationError,
            "return_reentry_modes contains an invalid entry: invalid_mode",
        ):
            validate_playbooks.validate_return_configuration(payload, location="playbooks[0]")

    def test_activation_surface_passthrough_keeps_return_fields(self) -> None:
        payload = self.make_registry_entry()

        surface = validate_playbooks.activation_surface_for_playbook("AOA-P-0008", payload)

        self.assertEqual(surface["return_posture"], "artifact_anchor")
        self.assertEqual(surface["return_anchor_artifacts"], ["route_decision", "bounded_plan"])
        self.assertEqual(surface["return_reentry_modes"], ["previous_phase", "safe_stop"])

    def test_playbooks_without_return_posture_stay_unchanged(self) -> None:
        payload = self.make_registry_entry()
        payload.pop("return_posture")
        payload.pop("return_anchor_artifacts")
        payload.pop("return_reentry_modes")

        validate_playbooks.validate_return_configuration(payload, location="playbooks[0]")
        surface = validate_playbooks.activation_surface_for_playbook("AOA-P-0008", payload)

        self.assertNotIn("return_posture", surface)
        self.assertNotIn("return_anchor_artifacts", surface)
        self.assertNotIn("return_reentry_modes", surface)


class ValidatePlaybooksFederationEligibilityTests(unittest.TestCase):
    def test_project_overlay_federation_ready_counts_as_full_federation_readiness(self) -> None:
        skill = {
            "lineage_state": "published",
            "readiness_reconciliation": "project_overlay_federation_ready",
        }

        self.assertTrue(
            validate_playbooks.skill_is_federation_eligible(skill, playbook_status="active")
        )

    def test_experimental_playbooks_may_use_published_governance_blocked_skills(self) -> None:
        skill = {
            "lineage_state": "published",
            "readiness_reconciliation": "eval_ready_but_governance_blocked",
        }

        self.assertTrue(
            validate_playbooks.skill_is_federation_eligible(skill, playbook_status="experimental")
        )

    def test_nonexperimental_playbooks_require_full_federation_readiness(self) -> None:
        skill = {
            "lineage_state": "published",
            "readiness_reconciliation": "eval_ready_but_governance_blocked",
        }

        self.assertFalse(
            validate_playbooks.skill_is_federation_eligible(skill, playbook_status="active")
        )


class ValidatePlaybooksQuestbookSurfaceTests(unittest.TestCase):
    def write_valid_surface(self, repo_root: Path) -> None:
        write_text(
            repo_root / "QUESTBOOK.md",
            "\n".join(
                (
                    "# QUESTBOOK",
                    "",
                    "## Frontier",
                    "- none yet",
                    "",
                    "## Near",
                    "- none yet",
                    "",
                    "## Blocked / reanchor",
                    "- `AOA-PB-Q-0002` Define harvest thresholds and promotion destinations without promoting one reviewed lane into fake recurrence.",
                    "",
                    "## Harvest candidates",
                    "- none yet",
                    "",
                    "Read `docs/QUEST_HARVEST_AND_REANCHOR.md` for the bounded note.",
                    "",
                )
            ),
        )
        write_text(
            repo_root / "docs" / "QUEST_HARVEST_AND_REANCHOR.md",
            "\n".join(
                (
                    "# Playbook Harvest and Reanchor",
                    "",
                    "This note lands the recurrence posture from `docs/PLAYBOOK_RECURRENCE_DISCIPLINE.md`.",
                    "",
                    "## Core rule",
                    "",
                    "Harvest is evidence-first selection. Reanchor is governed return to a named anchor.",
                    "reanchor is not retry.",
                    "",
                    "## What harvest is",
                    "",
                    "Harvest selects reviewable evidence without turning the playbook layer into runtime state.",
                    "",
                    "## What harvest is not",
                    "",
                    "Harvest is not a runtime ledger or a shortcut around boundary review.",
                    "",
                    "## What reanchor is",
                    "",
                    "Reanchor returns a route to a valid anchor after drift or boundary loss.",
                    "",
                    "## What reanchor is not",
                    "",
                    "reanchor is not retry.",
                    "",
                    "## Harvest thresholds",
                    "",
                    "- If a route has no valid anchor, do not harvest it.",
                    "- If a route loses anchor integrity twice, stop rather than simulate continuity.",
                    "",
                    "## Valid anchor classes",
                    "",
                    "- artifact anchors",
                    "- checkpoint anchors",
                    "- review anchors",
                    "",
                    "## Named promotion destinations",
                    "",
                    "- `docs/real-runs/` for reviewed summaries",
                    "- `docs/gate-reviews/` for gate-review notes",
                    "",
                    "## Anti-patterns",
                    "",
                    "- treating reanchor as retry",
                    "- promoting harvest into runtime state",
                    "",
                )
            ),
        )
        for quest_id in validate_playbooks.QUESTBOOK_QUEST_IDS:
            write_text(
                repo_root / "quests" / f"{quest_id}.yaml",
                "\n".join(
                    (
                        "schema_version: work_quest_v1",
                        f"id: {quest_id}",
                        "title: Questbook foundation rollout",
                        "summary: ''",
                        "repo: aoa-playbooks",
                        "owner_surface: docs/QUEST_HARVEST_AND_REANCHOR.md",
                        "theme_ref: ''",
                        "milestone_ref: ''",
                        "kind: doctrine" if quest_id == "AOA-PB-Q-0001" else "kind: seam",
                        "state: done" if quest_id == "AOA-PB-Q-0001" else "state: reanchor",
                        "band: frontier" if quest_id == "AOA-PB-Q-0001" else "band: near",
                        "difficulty: d4_architecture" if quest_id == "AOA-PB-Q-0001" else "difficulty: d3_seam",
                        "risk: r2_contract" if quest_id == "AOA-PB-Q-0001" else "risk: r1_repo_local",
                        "control_mode: human_codex_copilot" if quest_id == "AOA-PB-Q-0001" else "control_mode: codex_supervised",
                        "delegate_tier: conductor" if quest_id == "AOA-PB-Q-0001" else "delegate_tier: planner",
                        "fallback_tier: verifier" if quest_id == "AOA-PB-Q-0001" else "fallback_tier: verifier",
                        "wrapper_class: codex_primary",
                        "write_scope: docs_only",
                        "split_required: true",
                        "complexity_basis:",
                        "  scope: 2",
                        "  ambiguity: 2",
                        "  boundary: 2",
                        "  verification: 2",
                        "parent: null",
                        "depends_on: []" if quest_id == "AOA-PB-Q-0001" else "depends_on:\n  - AOA-PB-Q-0001",
                        "activation:",
                        "  mode: immediate" if quest_id == "AOA-PB-Q-0001" else "  mode: on_review_of",
                        "" if quest_id == "AOA-PB-Q-0001" else "  ref: AOA-PB-Q-0001",
                        "anchor_ref:",
                        "  artifact: recurrence_discipline" if quest_id == "AOA-PB-Q-0001" else "  artifact: harvest_reanchor_note",
                        "  ref: docs/PLAYBOOK_RECURRENCE_DISCIPLINE.md" if quest_id == "AOA-PB-Q-0001" else "  ref: docs/QUEST_HARVEST_AND_REANCHOR.md",
                        "handoff_role: playbook-maintainer",
                        "evidence:",
                        "  - recurrence and return stay scenario-owned" if quest_id == "AOA-PB-Q-0001" else "  - harvest thresholds are named",
                        "  - reanchor is not retry" if quest_id == "AOA-PB-Q-0001" else "  - named promotion destinations stay reviewable",
                        "  - harvest stays evidence-first" if quest_id == "AOA-PB-Q-0001" else "  - valid anchor classes stay compact",
                        "harvest:",
                        "  target: playbook",
                        "opened_at: '2026-03-31'",
                        "touched_at: '2026-03-31'",
                        "tags:",
                        "  - playbooks",
                        "  - recurrence" if quest_id == "AOA-PB-Q-0001" else "  - harvest",
                        "  - reanchor" if quest_id == "AOA-PB-Q-0001" else "  - evidence",
                        "notes: ''",
                        "public_safe: true",
                        "",
                    )
                ),
            )

        catalog = validate_playbooks.build_quest_catalog_projection(repo_root)
        dispatch = validate_playbooks.build_quest_dispatch_projection(repo_root)
        write_text(
            repo_root / "generated" / "quest_catalog.min.json",
            json.dumps(catalog, separators=(",", ":")) + "\n",
        )
        write_text(
            repo_root / "generated" / "quest_catalog.min.example.json",
            json.dumps(catalog, indent=2) + "\n",
        )
        write_text(
            repo_root / "generated" / "quest_dispatch.min.json",
            json.dumps(dispatch, separators=(",", ":")) + "\n",
        )
        write_text(
            repo_root / "generated" / "quest_dispatch.min.example.json",
            json.dumps(dispatch, indent=2) + "\n",
        )

    def test_valid_questbook_surface_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            self.write_valid_surface(repo_root)

            validate_playbooks.validate_questbook_surface(repo_root)

    def test_additive_questbook_quest_passes_when_referenced(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            self.write_valid_surface(repo_root)
            write_text(
                repo_root / "quests" / "AOA-PB-Q-0003.yaml",
                "\n".join(
                    (
                        "schema_version: work_quest_v1",
                        "id: AOA-PB-Q-0003",
                        "title: Adjunct campaign outline",
                        "summary: ''",
                        "repo: aoa-playbooks",
                        "owner_surface: docs/QUESTLINE_AND_CAMPAIGN_MODEL.md",
                        "theme_ref: ''",
                        "milestone_ref: ''",
                        "kind: seam",
                        "state: captured",
                        "band: frontier",
                        "difficulty: d3_seam",
                        "risk: r1_repo_local",
                        "control_mode: human_codex_copilot",
                        "delegate_tier: planner",
                        "fallback_tier: verifier",
                        "wrapper_class: codex_primary",
                        "write_scope: repo_local",
                        "split_required: true",
                        "complexity_basis:",
                        "  scope: 2",
                        "  ambiguity: 2",
                        "  boundary: 2",
                        "  verification: 1",
                        "parent: null",
                        "depends_on: []",
                        "activation:",
                        "  mode: manual",
                        "anchor_ref:",
                        "  artifact: questline_campaign_model",
                        "  ref: docs/QUESTLINE_AND_CAMPAIGN_MODEL.md",
                        "handoff_role: playbook-maintainer",
                        "evidence:",
                        "  - outline stays bounded",
                        "  - reanchor stays governed return",
                        "  - runtime ledger posture stays excluded",
                        "harvest:",
                        "  target: playbook",
                        "opened_at: '2026-04-01'",
                        "touched_at: '2026-04-01'",
                        "tags:",
                        "  - questline",
                        "  - campaign",
                        "notes: ''",
                        "public_safe: true",
                        "",
                    )
                ),
            )
            write_text(
                repo_root / "QUESTBOOK.md",
                (repo_root / "QUESTBOOK.md").read_text(encoding="utf-8").replace(
                    "- none yet",
                    "- `AOA-PB-Q-0003` Adjunct campaign outline surface.",
                    1,
                ),
            )
            catalog = validate_playbooks.build_quest_catalog_projection(repo_root)
            dispatch = validate_playbooks.build_quest_dispatch_projection(repo_root)
            write_text(
                repo_root / "generated" / "quest_catalog.min.json",
                json.dumps(catalog, separators=(",", ":")) + "\n",
            )
            write_text(
                repo_root / "generated" / "quest_catalog.min.example.json",
                json.dumps(catalog, indent=2) + "\n",
            )
            write_text(
                repo_root / "generated" / "quest_dispatch.min.json",
                json.dumps(dispatch, separators=(",", ":")) + "\n",
            )
            write_text(
                repo_root / "generated" / "quest_dispatch.min.example.json",
                json.dumps(dispatch, indent=2) + "\n",
            )

            validate_playbooks.validate_questbook_surface(repo_root)

    def test_missing_questbook_file_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            self.write_valid_surface(repo_root)
            (repo_root / "QUESTBOOK.md").unlink()

            with self.assertRaisesRegex(validate_playbooks.ValidationError, "missing required file"):
                validate_playbooks.validate_questbook_surface(repo_root)

    def test_missing_foundation_quest_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            self.write_valid_surface(repo_root)
            (repo_root / "quests" / "AOA-PB-Q-0001.yaml").unlink()

            with self.assertRaisesRegex(
                validate_playbooks.ValidationError,
                "foundation quest ids: AOA-PB-Q-0001",
            ):
                validate_playbooks.validate_questbook_surface(repo_root)

    def test_quest_id_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            self.write_valid_surface(repo_root)
            write_text(
                repo_root / "quests" / "AOA-PB-Q-0002.yaml",
                "\n".join(
                    (
                        "schema_version: work_quest_v1",
                        "id: AOA-PB-Q-9999",
                        "title: Questbook foundation rollout",
                        "summary: ''",
                        "repo: aoa-playbooks",
                        "owner_surface: docs/QUEST_HARVEST_AND_REANCHOR.md",
                        "theme_ref: ''",
                        "milestone_ref: ''",
                        "kind: seam",
                        "state: triaged",
                        "band: near",
                        "difficulty: d3_seam",
                        "risk: r1_repo_local",
                        "control_mode: codex_supervised",
                        "delegate_tier: planner",
                        "fallback_tier: verifier",
                        "wrapper_class: codex_primary",
                        "write_scope: docs_only",
                        "split_required: true",
                        "complexity_basis:",
                        "  scope: 2",
                        "  ambiguity: 2",
                        "  boundary: 2",
                        "  verification: 2",
                        "parent: null",
                        "depends_on:",
                        "  - AOA-PB-Q-0001",
                        "activation:",
                        "  mode: on_review_of",
                        "  ref: AOA-PB-Q-0001",
                        "anchor_ref:",
                        "  artifact: harvest_reanchor_note",
                        "  ref: docs/QUEST_HARVEST_AND_REANCHOR.md",
                        "handoff_role: playbook-maintainer",
                        "evidence:",
                        "  - harvest thresholds are named",
                        "  - named promotion destinations stay reviewable",
                        "  - valid anchor classes stay compact",
                        "harvest:",
                        "  target: playbook",
                        "opened_at: '2026-03-31'",
                        "touched_at: '2026-03-31'",
                        "tags:",
                        "  - playbooks",
                        "  - harvest",
                        "  - evidence",
                        "notes: ''",
                        "public_safe: true",
                        "",
                    )
                ),
            )

            with self.assertRaisesRegex(validate_playbooks.ValidationError, "must declare id 'AOA-PB-Q-0002'"):
                validate_playbooks.validate_questbook_surface(repo_root)

    def test_missing_reanchor_phrase_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            self.write_valid_surface(repo_root)
            doc_path = repo_root / "docs" / "QUEST_HARVEST_AND_REANCHOR.md"
            write_text(
                doc_path,
                doc_path.read_text(encoding="utf-8").replace("reanchor is not retry.\n", ""),
            )

            with self.assertRaisesRegex(
                validate_playbooks.ValidationError,
                "must mention 'reanchor is not retry'",
            ):
                validate_playbooks.validate_questbook_surface(repo_root)


class ValidatePlaybookReviewStatusSurfaceTests(unittest.TestCase):
    def test_review_status_surface_passes_for_current_repo(self) -> None:
        playbooks_by_id = validate_playbooks.validate_registry()
        validate_playbooks.validate_real_run_workflow_surfaces()
        validate_playbooks.validate_playbook_review_status_surface(playbooks_by_id)

    def test_review_status_surface_rejects_verdict_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            repo_root.mkdir(parents=True, exist_ok=True)
            generated_dir = repo_root / "generated"
            generated_dir.mkdir(parents=True, exist_ok=True)

            source_path = REPO_ROOT / "generated" / "playbook_review_status.min.json"
            payload = source_path.read_text(encoding="utf-8").replace("composition-landed", "hold", 1)
            write_text(generated_dir / "playbook_review_status.min.json", payload)

            with self.assertRaisesRegex(
                validate_playbooks.ValidationError,
                "generated/playbook_review_status.min.json is out of date",
            ):
                original_repo_root = validate_playbooks.REPO_ROOT
                original_review_path = validate_playbooks.PLAYBOOK_REVIEW_STATUS_PATH
                original_run_dir = validate_playbooks.REAL_RUN_SUMMARY_DIR
                original_gate_dir = validate_playbooks.GATE_REVIEW_DIR
                try:
                    validate_playbooks.REPO_ROOT = REPO_ROOT
                    validate_playbooks.PLAYBOOK_REVIEW_STATUS_PATH = generated_dir / "playbook_review_status.min.json"
                    validate_playbooks.REAL_RUN_SUMMARY_DIR = REPO_ROOT / "docs" / "real-runs"
                    validate_playbooks.GATE_REVIEW_DIR = REPO_ROOT / "docs" / "gate-reviews"
                    playbooks_by_id = validate_playbooks.validate_registry()
                    validate_playbooks.validate_playbook_review_status_surface(playbooks_by_id)
                finally:
                    validate_playbooks.REPO_ROOT = original_repo_root
                    validate_playbooks.PLAYBOOK_REVIEW_STATUS_PATH = original_review_path
                    validate_playbooks.REAL_RUN_SUMMARY_DIR = original_run_dir
                    validate_playbooks.GATE_REVIEW_DIR = original_gate_dir


class ValidatePlaybookReviewPacketContractsSurfaceTests(unittest.TestCase):
    def test_review_packet_contracts_surface_passes_for_current_repo(self) -> None:
        playbooks_by_id = validate_playbooks.validate_registry()
        validate_playbooks.validate_playbook_review_packet_contracts_surface(playbooks_by_id)

    def test_review_packet_contracts_surface_reports_builder_system_exit(self) -> None:
        class FailingBuilder:
            def build_review_packet_contracts_payload(self) -> dict[str, object]:
                raise SystemExit("builder-exit")

        with patch.object(
            validate_playbooks,
            "load_review_packet_contract_builder_module",
            return_value=FailingBuilder(),
        ):
            with self.assertRaisesRegex(validate_playbooks.ValidationError, "builder-exit"):
                playbooks_by_id = validate_playbooks.validate_registry()
                validate_playbooks.validate_playbook_review_packet_contracts_surface(playbooks_by_id)

    def test_review_packet_contracts_surface_rejects_packet_kind_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            repo_root.mkdir(parents=True, exist_ok=True)
            generated_dir = repo_root / "generated"
            generated_dir.mkdir(parents=True, exist_ok=True)

            source_path = REPO_ROOT / "generated" / "playbook_review_packet_contracts.min.json"
            payload = source_path.read_text(encoding="utf-8").replace(
                "\"artifact_hook_candidate\"",
                "\"unexpected_packet_kind\"",
                1,
            )
            write_text(generated_dir / "playbook_review_packet_contracts.min.json", payload)

            with self.assertRaisesRegex(
                validate_playbooks.ValidationError,
                "generated/playbook_review_packet_contracts.min.json is out of date",
            ):
                original_packet_path = validate_playbooks.PLAYBOOK_REVIEW_PACKET_CONTRACTS_PATH
                try:
                    validate_playbooks.PLAYBOOK_REVIEW_PACKET_CONTRACTS_PATH = (
                        generated_dir / "playbook_review_packet_contracts.min.json"
                    )
                    playbooks_by_id = validate_playbooks.validate_registry()
                    validate_playbooks.validate_playbook_review_packet_contracts_surface(playbooks_by_id)
                finally:
                    validate_playbooks.PLAYBOOK_REVIEW_PACKET_CONTRACTS_PATH = original_packet_path


class ValidatePlaybookReviewIntakeSurfaceTests(unittest.TestCase):
    def test_review_intake_surface_passes_for_current_repo(self) -> None:
        validate_playbooks.validate_playbook_review_intake_surface()

    def test_review_intake_surface_rejects_accepted_packet_kind_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            repo_root.mkdir(parents=True, exist_ok=True)
            generated_dir = repo_root / "generated"
            generated_dir.mkdir(parents=True, exist_ok=True)

            payload = json.loads(
                (REPO_ROOT / "generated" / "playbook_review_intake.min.json").read_text(encoding="utf-8")
            )
            for entry in payload["playbooks"]:
                if entry["playbook_id"] == "AOA-P-0011":
                    entry["accepted_packet_kinds"] = ["unexpected_packet_kind"]
                    break
            write_text(
                generated_dir / "playbook_review_intake.min.json",
                json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
            )

            with self.assertRaisesRegex(
                validate_playbooks.ValidationError,
                "generated/playbook_review_intake.min.json is out of date",
            ):
                original_intake_path = validate_playbooks.PLAYBOOK_REVIEW_INTAKE_PATH
                try:
                    validate_playbooks.PLAYBOOK_REVIEW_INTAKE_PATH = (
                        generated_dir / "playbook_review_intake.min.json"
                    )
                    validate_playbooks.validate_playbook_review_intake_surface()
                finally:
                    validate_playbooks.PLAYBOOK_REVIEW_INTAKE_PATH = original_intake_path

    def test_review_intake_surface_rejects_gate_review_ref_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            repo_root.mkdir(parents=True, exist_ok=True)
            generated_dir = repo_root / "generated"
            generated_dir.mkdir(parents=True, exist_ok=True)

            payload = json.loads(
                (REPO_ROOT / "generated" / "playbook_review_intake.min.json").read_text(encoding="utf-8")
            )
            for entry in payload["playbooks"]:
                if entry["playbook_id"] == "AOA-P-0017":
                    entry["gate_review_ref"] = "docs/gate-reviews/drifted.md"
                    break
            write_text(
                generated_dir / "playbook_review_intake.min.json",
                json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
            )

            with self.assertRaisesRegex(
                validate_playbooks.ValidationError,
                "generated/playbook_review_intake.min.json is out of date",
            ):
                original_intake_path = validate_playbooks.PLAYBOOK_REVIEW_INTAKE_PATH
                try:
                    validate_playbooks.PLAYBOOK_REVIEW_INTAKE_PATH = (
                        generated_dir / "playbook_review_intake.min.json"
                    )
                    validate_playbooks.validate_playbook_review_intake_surface()
                finally:
                    validate_playbooks.PLAYBOOK_REVIEW_INTAKE_PATH = original_intake_path

class ValidatePlaybookReviewPacketContractRegressionTests(unittest.TestCase):
    def test_review_packet_contracts_surface_rejects_missing_source_review_refs_for_review_required_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "aoa-playbooks"
            repo_root.mkdir(parents=True, exist_ok=True)
            generated_dir = repo_root / "generated"
            generated_dir.mkdir(parents=True, exist_ok=True)

            payload = json.loads(
                (REPO_ROOT / "generated" / "playbook_review_packet_contracts.min.json").read_text(encoding="utf-8")
            )
            for entry in payload["playbooks"]:
                if entry["playbook_id"] == "AOA-P-0011":
                    entry["source_review_refs"] = []
                    break
            write_text(
                generated_dir / "playbook_review_packet_contracts.min.json",
                json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
            )

            with self.assertRaisesRegex(
                validate_playbooks.ValidationError,
                "generated/playbook_review_packet_contracts.min.json is out of date",
            ):
                original_packet_path = validate_playbooks.PLAYBOOK_REVIEW_PACKET_CONTRACTS_PATH
                try:
                    validate_playbooks.PLAYBOOK_REVIEW_PACKET_CONTRACTS_PATH = (
                        generated_dir / "playbook_review_packet_contracts.min.json"
                    )
                    playbooks_by_id = validate_playbooks.validate_registry()
                    validate_playbooks.validate_playbook_review_packet_contracts_surface(playbooks_by_id)
                finally:
                    validate_playbooks.PLAYBOOK_REVIEW_PACKET_CONTRACTS_PATH = original_packet_path


if __name__ == "__main__":
    unittest.main()
