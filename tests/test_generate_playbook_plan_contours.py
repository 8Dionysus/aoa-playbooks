from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
from typing import Any

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = (
    REPO_ROOT
    / "mechanics"
    / "scenario-composition"
    / "parts"
    / "plan-contours"
    / "scripts"
    / "generate_playbook_plan_contours.py"
)
SPEC = importlib.util.spec_from_file_location("generate_playbook_plan_contours", GENERATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
generator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generator)


def _walk_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(generator._normalized_key(key))
            keys.update(_walk_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(_walk_keys(child))
    return keys


def test_generated_plan_contours_match_canonical_inputs() -> None:
    committed = json.loads(generator.OUTPUT_PATH.read_text(encoding="utf-8"))

    assert committed == generator.build_output()


def test_plan_contours_reference_exact_capability_graph_node_ids() -> None:
    source = generator.load_source_config()
    graph_ids = set(generator.load_capabilities_by_id())

    referenced = {
        capability_id
        for contour in source["contours"]
        for capability_id in (
            *contour["required_capability_ids"],
            *(
                capability_id
                for step in contour["steps"]
                for capability_id in step["capability_ids"]
            ),
        )
    }

    assert referenced
    assert referenced.issubset(graph_ids)


def test_golden_contours_are_complete_and_runtime_neutral() -> None:
    output = generator.build_output()

    assert {item["playbook_id"] for item in output["contours"]} == set(
        generator.REQUIRED_CONTOUR_IDS
    )
    assert _walk_keys(output).isdisjoint(generator.FORBIDDEN_EXECUTABLE_KEYS)
    for contour in output["contours"]:
        produced = [
            artifact
            for step in contour["steps"]
            for artifact in step["expected_output_kinds"]
        ]
        inputs = contour["input_artifact_kinds"]
        assert sorted((*inputs, *produced)) == sorted(contour["expected_artifact_kinds"])
        assert set(inputs).isdisjoint(produced)
        assert len(produced) == len(set(produced))


def test_executable_fields_are_rejected_recursively() -> None:
    source = deepcopy(generator.load_source_config())
    source["contours"][0]["steps"][0]["command"] = "git status"

    with pytest.raises(generator.BuilderError, match="forbidden"):
        generator.validate_source_config(source)


def test_frontmatter_alignment_is_required() -> None:
    source = deepcopy(generator.load_source_config())
    source["contours"][0]["required_agent_ids"][0] = "invented-agent"

    with pytest.raises(generator.BuilderError, match="must exactly match"):
        generator.validate_source_config(source)


def test_eval_requirements_cover_source_anchors_exactly() -> None:
    source = deepcopy(generator.load_source_config())
    source["contours"][0]["eval_requirements"].pop()

    with pytest.raises(generator.BuilderError, match="must cover source playbook eval_anchors exactly"):
        generator.validate_source_config(source)


def test_dry_run_a2a_contour_has_no_dispatchable_effect() -> None:
    source = generator.load_source_config()
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == "AOA-P-0031"
    )
    target_step = next(
        step for step in contour["steps"] if "codex_local_target" in step["expected_output_kinds"]
    )

    assert target_step["step_id"] == "inspect-child-target"
    assert target_step["operation_kind"] == "inspect"
    assert target_step["effect_class"] == "read_only"
    assert target_step["input_binding"] == "selected_scenario_inputs"
    assert target_step["input_artifact_kinds"] == [
        "summon_request",
        "summon_decision",
    ]


def test_bounded_change_preview_and_mutation_bind_requested_inputs() -> None:
    source = generator.load_source_config()
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == "AOA-P-0011"
    )
    steps = {step["step_id"]: step for step in contour["steps"]}

    assert steps["preview"]["input_binding"] == "all_scenario_inputs"
    assert steps["mutate"]["input_binding"] == "all_scenario_inputs"


def test_dry_run_a2a_review_binds_preexisting_child_result() -> None:
    source = generator.load_source_config()
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == "AOA-P-0031"
    )
    review_step = next(
        step for step in contour["steps"] if step["step_id"] == "review-return"
    )

    assert "child_task_result" in contour["input_artifact_kinds"]
    assert "child_task_result" in review_step["input_artifact_kinds"]
    assert "child_task_result" not in review_step["expected_output_kinds"]
    assert review_step["step_id"] == "review-return"
    assert review_step["input_binding"] == "selected_scenario_inputs"


def test_reviewed_runtime_receipt_is_an_input_not_a_step_output() -> None:
    source = generator.load_source_config()
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == "AOA-P-0032"
    )
    inspect_step = next(
        step for step in contour["steps"] if step["step_id"] == "inspect-runtime-receipt"
    )
    evidence = next(
        requirement
        for requirement in contour["evidence_requirements"]
        if requirement["artifact_kind"] == "owner_runtime_receipt"
    )

    assert contour["input_artifact_kinds"] == ["owner_runtime_receipt"]
    assert inspect_step["input_artifact_kinds"] == ["owner_runtime_receipt"]
    assert inspect_step["expected_output_kinds"] == []
    assert evidence["artifact_binding"] == "scenario_input"
    validate_step = next(
        step for step in contour["steps"] if step["step_id"] == "validate-degraded-lane"
    )
    assert validate_step["input_binding"] == "selected_scenario_inputs"
    assert validate_step["input_artifact_kinds"] == ["owner_runtime_receipt"]


def test_input_artifact_cannot_be_reproduced_by_a_step() -> None:
    source = deepcopy(generator.load_source_config())
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == "AOA-P-0031"
    )
    review_step = next(
        step for step in contour["steps"] if step["step_id"] == "review-return"
    )
    review_step["expected_output_kinds"].append("child_task_result")

    with pytest.raises(generator.BuilderError, match="outside produced artifacts"):
        generator.validate_source_config(source)


def test_every_input_artifact_must_be_bound_by_a_step() -> None:
    source = deepcopy(generator.load_source_config())
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == "AOA-P-0031"
    )
    review_step = next(
        step for step in contour["steps"] if step["step_id"] == "review-return"
    )
    review_step["input_artifact_kinds"].remove("child_task_result")
    review_step["input_binding"] = "none"

    with pytest.raises(generator.BuilderError, match="must bind every input artifact"):
        generator.validate_source_config(source)


@pytest.mark.parametrize(
    ("playbook_id", "step_id"),
    [
        ("AOA-P-0011", "orient"),
        ("AOA-P-0011", "mutate"),
        ("AOA-P-0031", "inspect-child-target"),
        ("AOA-P-0032", "validate-degraded-lane"),
    ],
)
def test_output_step_requires_input_provenance(
    playbook_id: str,
    step_id: str,
) -> None:
    source = deepcopy(generator.load_source_config())
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == playbook_id
    )
    step = next(item for item in contour["steps"] if item["step_id"] == step_id)
    step["input_binding"] = "none"
    step["input_artifact_kinds"] = []

    with pytest.raises(generator.BuilderError, match="without input provenance"):
        generator.validate_source_config(source)


def test_typed_inputs_require_kind_selected_binding() -> None:
    source = deepcopy(generator.load_source_config())
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == "AOA-P-0031"
    )
    step = next(
        item for item in contour["steps"] if item["step_id"] == "inspect-child-target"
    )
    step["input_binding"] = "all_scenario_inputs"

    with pytest.raises(
        generator.BuilderError,
        match="must be selected_scenario_inputs",
    ):
        generator.validate_source_config(source)


def test_selected_input_binding_requires_typed_artifact_kinds() -> None:
    source = deepcopy(generator.load_source_config())
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == "AOA-P-0011"
    )
    step = next(item for item in contour["steps"] if item["step_id"] == "orient")
    step["input_binding"] = "selected_scenario_inputs"

    with pytest.raises(
        generator.BuilderError,
        match="requires at least one input_artifact_kind",
    ):
        generator.validate_source_config(source)


def test_runtime_optional_paths_have_reviewed_guards() -> None:
    source = generator.load_source_config()
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == "AOA-P-0032"
    )
    conditions = {
        condition["condition_id"]: condition["binding"]
        for condition in contour["scenario_conditions"]
    }
    steps = {step["step_id"]: step for step in contour["steps"]}

    assert conditions == {
        "derived_surface_recovery_required": "reviewed_boolean",
        "proof_handoff_earned": "reviewed_boolean",
    }
    assert (
        steps["reground-source"]["guard_condition_id"]
        == "derived_surface_recovery_required"
    )
    assert steps["evaluate-reentry"]["guard_condition_id"] == "proof_handoff_earned"
    assert steps["closeout-recovery"]["guard_condition_id"] is None


def test_unknown_guard_condition_is_rejected() -> None:
    source = deepcopy(generator.load_source_config())
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == "AOA-P-0032"
    )
    contour["steps"][2]["guard_condition_id"] = "invented_condition"

    with pytest.raises(generator.BuilderError, match="unknown scenario condition"):
        generator.validate_source_config(source)


def test_guarded_artifact_cannot_be_terminally_required() -> None:
    source = deepcopy(generator.load_source_config())
    contour = next(
        item for item in source["contours"] if item["playbook_id"] == "AOA-P-0032"
    )
    requirement = next(
        item
        for item in contour["evidence_requirements"]
        if item["artifact_kind"] == "regrounding_ticket_ref"
    )
    requirement["terminal_required"] = True

    with pytest.raises(generator.BuilderError, match="must be false for guarded evidence"):
        generator.validate_source_config(source)
