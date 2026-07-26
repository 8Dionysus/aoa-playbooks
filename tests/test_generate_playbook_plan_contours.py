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
        assert sorted(produced) == sorted(contour["expected_artifact_kinds"])
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
        step for step in contour["steps"] if "child_task_result" in step["expected_output_kinds"]
    )

    assert review_step["step_id"] == "review-return"
    assert review_step["input_binding"] == "all_scenario_inputs"
