from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "validate_playbooks.py"
SPEC = importlib.util.spec_from_file_location("validate_playbooks", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"unable to load validator module from {MODULE_PATH}")
validate_playbooks = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_playbooks)


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


if __name__ == "__main__":
    unittest.main()
