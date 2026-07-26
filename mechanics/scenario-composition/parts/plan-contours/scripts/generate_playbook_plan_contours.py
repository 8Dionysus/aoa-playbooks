#!/usr/bin/env python3
"""Generate the runtime-neutral playbook plan-contour projection."""
from __future__ import annotations

import argparse
from copy import deepcopy
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
import yaml


REPO_ROOT = Path(__file__).resolve().parents[5]
PART_ROOT = REPO_ROOT / "mechanics" / "scenario-composition" / "parts" / "plan-contours"
CONFIG_PATH = PART_ROOT / "config" / "playbook_plan_contours.json"
SCHEMA_PATH = PART_ROOT / "schemas" / "playbook-plan-contours.schema.json"
OUTPUT_PATH = REPO_ROOT / "generated" / "playbook_plan_contours.min.json"

CONFIG_REF = CONFIG_PATH.relative_to(REPO_ROOT).as_posix()
SCHEMA_REF = SCHEMA_PATH.relative_to(REPO_ROOT).as_posix()
PLAYBOOK_GLOB = "playbooks/*/*/*/PLAYBOOK.md"
ABI_ID = "aoa_playbook_plan_contour_v1"
ABI_VERSION = "aoa_playbook_plan_contour_v1"
SOURCE_SCHEMA_VERSION = "aoa_playbook_plan_contour_source_v1"
OUTPUT_SCHEMA_VERSION = "aoa_playbook_plan_contours_v1"
REQUIRED_CONTOUR_IDS = frozenset({"AOA-P-0011", "AOA-P-0031", "AOA-P-0032"})
FORBIDDEN_EXECUTABLE_KEYS = frozenset(
    {
        "args",
        "argv",
        "command",
        "commands",
        "mcp",
        "model",
        "prompt",
        "prompts",
        "script",
        "shell",
        "tool",
        "tool_args",
        "tools",
        "transport",
    }
)


class BuilderError(RuntimeError):
    """Raised when a plan-contour source violates the owner contract."""


def fail(message: str) -> None:
    raise BuilderError(message)


def display_path(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {display_path(path)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {display_path(path)}: {exc}")


def load_source_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    payload = read_json(path)
    if not isinstance(payload, dict):
        fail(f"{display_path(path)} must contain a JSON object")
    return payload


def _read_frontmatter(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing source playbook: {display_path(path)}")

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        fail(f"{display_path(path)} must start with YAML frontmatter")
    try:
        boundary = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        fail(f"{display_path(path)} is missing the closing YAML frontmatter boundary")

    try:
        payload = yaml.safe_load("\n".join(lines[1:boundary]))
    except yaml.YAMLError as exc:
        fail(f"invalid YAML frontmatter in {display_path(path)}: {exc}")
    if not isinstance(payload, dict):
        fail(f"{display_path(path)} frontmatter must contain a mapping")
    return payload


def _require_string(value: Any, *, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{location} must be a non-empty string")
    return value


def _require_string_list(value: Any, *, location: str) -> list[str]:
    if not isinstance(value, list):
        fail(f"{location} must be a list")
    result: list[str] = []
    for index, item in enumerate(value):
        result.append(_require_string(item, location=f"{location}[{index}]"))
    if len(result) != len(set(result)):
        fail(f"{location} must not contain duplicates")
    return result


def _require_object_list(value: Any, *, location: str, nonempty: bool = True) -> list[dict[str, Any]]:
    if not isinstance(value, list) or (nonempty and not value):
        qualifier = "a non-empty" if nonempty else "a"
        fail(f"{location} must be {qualifier} list")
    result: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            fail(f"{location}[{index}] must be an object")
        result.append(item)
    return result


def _require_unique(items: list[dict[str, Any]], key: str, *, location: str) -> list[str]:
    values = [
        _require_string(item.get(key), location=f"{location}[{index}].{key}")
        for index, item in enumerate(items)
    ]
    if len(values) != len(set(values)):
        fail(f"{location}.{key} values must be unique")
    return values


def _normalized_key(key: str) -> str:
    return key.strip().casefold().replace("-", "_")


def _reject_executable_keys(value: Any, *, location: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if not isinstance(key, str):
                fail(f"{location} contains a non-string object key")
            if _normalized_key(key) in FORBIDDEN_EXECUTABLE_KEYS:
                fail(f"{location}.{key} is forbidden in runtime-neutral plan contours")
            _reject_executable_keys(child, location=f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _reject_executable_keys(child, location=f"{location}[{index}]")


def _validate_scenario_conditions(
    contour: dict[str, Any],
    *,
    location: str,
) -> set[str]:
    conditions = _require_object_list(
        contour.get("scenario_conditions"),
        location=f"{location}.scenario_conditions",
        nonempty=False,
    )
    condition_ids = set(
        _require_unique(
            conditions,
            "condition_id",
            location=f"{location}.scenario_conditions",
        )
    )
    for index, condition in enumerate(conditions):
        if condition.get("binding") != "reviewed_boolean":
            fail(
                f"{location}.scenario_conditions[{index}].binding "
                "must be reviewed_boolean"
            )
    return condition_ids


def _validate_guard_condition(
    value: Any,
    *,
    location: str,
    condition_ids: set[str],
) -> str | None:
    if value is None:
        return None
    condition_id = _require_string(value, location=location)
    if condition_id not in condition_ids:
        fail(f"{location} references unknown scenario condition {condition_id!r}")
    return condition_id


def _validate_step_graph(
    contour: dict[str, Any],
    *,
    location: str,
    required_agents: set[str],
    required_capabilities: set[str],
    expected_artifacts: set[str],
    input_artifacts: set[str],
    condition_ids: set[str],
) -> tuple[
    set[str],
    dict[str, set[str]],
    dict[str, set[str]],
    dict[str, str | None],
]:
    steps = _require_object_list(contour.get("steps"), location=f"{location}.steps")
    step_ids = _require_unique(steps, "step_id", location=f"{location}.steps")
    seen: set[str] = set()
    output_owner: dict[str, str] = {}
    outputs_by_step: dict[str, set[str]] = {}
    inputs_by_step: dict[str, set[str]] = {}
    guards_by_step: dict[str, str | None] = {}
    consumed_inputs: set[str] = set()
    used_conditions: set[str] = set()
    output_artifacts = expected_artifacts - input_artifacts

    for index, (step, step_id) in enumerate(zip(steps, step_ids, strict=True)):
        step_location = f"{location}.steps[{index}]"
        dependencies = _require_string_list(
            step.get("depends_on"),
            location=f"{step_location}.depends_on",
        )
        unknown_or_forward = sorted(set(dependencies) - seen)
        if unknown_or_forward:
            fail(
                f"{step_location}.depends_on must reference earlier steps only; "
                f"invalid={unknown_or_forward}"
            )

        guard_condition_id = _validate_guard_condition(
            step.get("guard_condition_id"),
            location=f"{step_location}.guard_condition_id",
            condition_ids=condition_ids,
        )
        guards_by_step[step_id] = guard_condition_id
        if guard_condition_id is not None:
            used_conditions.add(guard_condition_id)

        agents = set(
            _require_string_list(step.get("agent_ids"), location=f"{step_location}.agent_ids")
        )
        unknown_agents = sorted(agents - required_agents)
        if unknown_agents:
            fail(f"{step_location}.agent_ids are outside required_agent_ids: {unknown_agents}")

        capabilities = set(
            _require_string_list(
                step.get("capability_ids"),
                location=f"{step_location}.capability_ids",
            )
        )
        unknown_capabilities = sorted(capabilities - required_capabilities)
        if unknown_capabilities:
            fail(
                f"{step_location}.capability_ids are outside required_capability_ids: "
                f"{unknown_capabilities}"
            )

        inputs = set(
            _require_string_list(
                step.get("input_artifact_kinds"),
                location=f"{step_location}.input_artifact_kinds",
            )
        )
        unknown_inputs = sorted(inputs - input_artifacts)
        if unknown_inputs:
            fail(
                f"{step_location}.input_artifact_kinds are outside "
                f"input_artifact_kinds: {unknown_inputs}"
            )
        if inputs and step.get("input_binding") != "all_scenario_inputs":
            fail(
                f"{step_location}.input_binding must be all_scenario_inputs "
                "when input_artifact_kinds are bound"
            )
        inputs_by_step[step_id] = inputs
        consumed_inputs.update(inputs)

        outputs = set(
            _require_string_list(
                step.get("expected_output_kinds"),
                location=f"{step_location}.expected_output_kinds",
            )
        )
        unknown_outputs = sorted(outputs - output_artifacts)
        if unknown_outputs:
            fail(
                f"{step_location}.expected_output_kinds are outside produced artifacts: "
                f"{unknown_outputs}"
            )
        for output in outputs:
            if output in output_owner:
                fail(
                    f"{location} produces artifact kind {output!r} more than once "
                    f"({output_owner[output]!r}, {step_id!r})"
                )
            output_owner[output] = step_id
        outputs_by_step[step_id] = outputs
        seen.add(step_id)

    produced = set(output_owner)
    if produced != output_artifacts:
        fail(
            f"{location}.steps must produce every non-input expected artifact exactly once; "
            f"missing={sorted(output_artifacts - produced)}, "
            f"unexpected={sorted(produced - output_artifacts)}"
        )
    if consumed_inputs != input_artifacts:
        fail(
            f"{location}.steps must bind every input artifact at least once; "
            f"missing={sorted(input_artifacts - consumed_inputs)}"
        )
    if used_conditions != condition_ids:
        fail(
            f"{location}.steps must use every declared scenario condition; "
            f"unused={sorted(condition_ids - used_conditions)}"
        )
    return set(step_ids), outputs_by_step, inputs_by_step, guards_by_step


def _validate_evidence(
    contour: dict[str, Any],
    *,
    location: str,
    step_ids: set[str],
    outputs_by_step: dict[str, set[str]],
    inputs_by_step: dict[str, set[str]],
    guards_by_step: dict[str, str | None],
    expected_artifacts: set[str],
    input_artifacts: set[str],
    condition_ids: set[str],
) -> tuple[set[str], dict[str, str | None]]:
    requirements = _require_object_list(
        contour.get("evidence_requirements"),
        location=f"{location}.evidence_requirements",
    )
    requirement_ids = set(
        _require_unique(
            requirements,
            "requirement_id",
            location=f"{location}.evidence_requirements",
        )
    )
    artifact_kinds: list[str] = []
    guards_by_requirement: dict[str, str | None] = {}
    for index, requirement in enumerate(requirements):
        item_location = f"{location}.evidence_requirements[{index}]"
        requirement_id = _require_string(
            requirement.get("requirement_id"),
            location=f"{item_location}.requirement_id",
        )
        artifact_kind = _require_string(
            requirement.get("artifact_kind"),
            location=f"{item_location}.artifact_kind",
        )
        artifact_kinds.append(artifact_kind)
        step_id = requirement.get("required_after_step_id")
        if not isinstance(step_id, str) or step_id not in step_ids:
            fail(f"{item_location}.required_after_step_id must reference a plan step")
        expected_binding = (
            "scenario_input" if artifact_kind in input_artifacts else "step_output"
        )
        if requirement.get("artifact_binding") != expected_binding:
            fail(
                f"{item_location}.artifact_binding must be {expected_binding!r} "
                f"for {artifact_kind!r}"
            )
        bound_artifacts = (
            inputs_by_step[step_id]
            if expected_binding == "scenario_input"
            else outputs_by_step[step_id]
        )
        if artifact_kind not in bound_artifacts:
            fail(
                f"{item_location} binds artifact {artifact_kind!r} to step {step_id!r}, "
                f"but that step does not bind it as {expected_binding}"
            )
        guard_condition_id = _validate_guard_condition(
            requirement.get("guard_condition_id"),
            location=f"{item_location}.guard_condition_id",
            condition_ids=condition_ids,
        )
        if guard_condition_id != guards_by_step[step_id]:
            fail(
                f"{item_location}.guard_condition_id must match step "
                f"{step_id!r}"
            )
        if guard_condition_id is not None and requirement.get("terminal_required") is not False:
            fail(f"{item_location}.terminal_required must be false for guarded evidence")
        guards_by_requirement[requirement_id] = guard_condition_id

    if len(artifact_kinds) != len(set(artifact_kinds)):
        fail(f"{location}.evidence_requirements must bind each artifact kind once")
    if set(artifact_kinds) != expected_artifacts:
        fail(
            f"{location}.evidence_requirements must cover expected_artifact_kinds exactly; "
            f"missing={sorted(expected_artifacts - set(artifact_kinds))}, "
            f"unexpected={sorted(set(artifact_kinds) - expected_artifacts)}"
        )
    return requirement_ids, guards_by_requirement


def _validate_eval_requirements(
    contour: dict[str, Any],
    *,
    location: str,
    frontmatter: dict[str, Any],
    evidence_ids: set[str],
    evidence_guards: dict[str, str | None],
    condition_ids: set[str],
) -> None:
    requirements = _require_object_list(
        contour.get("eval_requirements"),
        location=f"{location}.eval_requirements",
    )
    _require_unique(
        requirements,
        "requirement_id",
        location=f"{location}.eval_requirements",
    )
    configured_eval_anchors = set(
        _require_unique(
            requirements,
            "eval_anchor",
            location=f"{location}.eval_requirements",
        )
    )
    eval_anchors = set(
        _require_string_list(
            frontmatter.get("eval_anchors"),
            location=f"{location}.source_playbook.eval_anchors",
        )
    )
    if configured_eval_anchors != eval_anchors:
        fail(
            f"{location}.eval_requirements must cover source playbook eval_anchors exactly; "
            f"missing={sorted(eval_anchors - configured_eval_anchors)}, "
            f"unexpected={sorted(configured_eval_anchors - eval_anchors)}"
        )
    for index, requirement in enumerate(requirements):
        item_location = f"{location}.eval_requirements[{index}]"
        eval_anchor = _require_string(
            requirement.get("eval_anchor"),
            location=f"{item_location}.eval_anchor",
        )
        if eval_anchor not in eval_anchors:
            fail(f"{item_location}.eval_anchor is not declared by the source playbook")
        input_ref = requirement.get("input_ref")
        if not isinstance(input_ref, dict):
            fail(f"{item_location}.input_ref must be an object")
        if input_ref.get("owner_repo") != "aoa-evals":
            fail(f"{item_location}.input_ref.owner_repo must be aoa-evals")
        artifact_ref = _require_string(
            input_ref.get("artifact_ref"),
            location=f"{item_location}.input_ref.artifact_ref",
        )
        if artifact_ref != "generated/eval_catalog.min.json":
            fail(
                f"{item_location}.input_ref.artifact_ref must bind the aoa-evals "
                "generated catalog; eval_anchor selects the exact named entry"
            )
        required_evidence_ids = set(
            _require_string_list(
                requirement.get("required_evidence_ids"),
                location=f"{item_location}.required_evidence_ids",
            )
        )
        unknown_evidence = sorted(required_evidence_ids - evidence_ids)
        if unknown_evidence:
            fail(
                f"{item_location}.required_evidence_ids reference unknown requirements: "
                f"{unknown_evidence}"
            )
        guard_condition_id = _validate_guard_condition(
            requirement.get("guard_condition_id"),
            location=f"{item_location}.guard_condition_id",
            condition_ids=condition_ids,
        )
        incompatible_evidence = sorted(
            evidence_id
            for evidence_id in required_evidence_ids
            if evidence_guards[evidence_id] not in {None, guard_condition_id}
        )
        if incompatible_evidence:
            fail(
                f"{item_location}.required_evidence_ids contain evidence unavailable "
                f"under guard {guard_condition_id!r}: {incompatible_evidence}"
            )
        if guard_condition_id is not None and requirement.get(
            "verdict_required_for_closeout"
        ) is not False:
            fail(
                f"{item_location}.verdict_required_for_closeout must be false "
                "for guarded eval requirements"
            )


def _validate_retention_requirements(
    contour: dict[str, Any],
    *,
    location: str,
    frontmatter: dict[str, Any],
    condition_ids: set[str],
) -> None:
    requirements = _require_object_list(
        contour.get("retention_requirements"),
        location=f"{location}.retention_requirements",
    )
    _require_unique(
        requirements,
        "requirement_id",
        location=f"{location}.retention_requirements",
    )
    memo_contract_refs = set(
        _require_string_list(
            frontmatter.get("memo_contract_refs"),
            location=f"{location}.source_playbook.memo_contract_refs",
        )
    )
    for index, requirement in enumerate(requirements):
        item_location = f"{location}.retention_requirements[{index}]"
        input_ref = requirement.get("input_ref")
        if not isinstance(input_ref, dict):
            fail(f"{item_location}.input_ref must be an object")
        if input_ref.get("owner_repo") != "aoa-memo":
            fail(f"{item_location}.input_ref.owner_repo must be aoa-memo")
        artifact_ref = _require_string(
            input_ref.get("artifact_ref"),
            location=f"{item_location}.input_ref.artifact_ref",
        )
        if artifact_ref not in memo_contract_refs:
            fail(f"{item_location}.input_ref.artifact_ref is not declared by the source playbook")
        guard_condition_id = _validate_guard_condition(
            requirement.get("guard_condition_id"),
            location=f"{item_location}.guard_condition_id",
            condition_ids=condition_ids,
        )
        if guard_condition_id is not None and requirement.get(
            "receipt_required_for_closeout"
        ) is not True:
            fail(
                f"{item_location}.receipt_required_for_closeout must be true "
                "inside its guarded branch"
            )


def _validate_closeout_requirements(
    contour: dict[str, Any],
    *,
    location: str,
    expected_artifacts: set[str],
    artifact_guards: dict[str, str | None],
) -> None:
    requirements = _require_object_list(
        contour.get("closeout_requirements"),
        location=f"{location}.closeout_requirements",
    )
    _require_unique(
        requirements,
        "requirement_id",
        location=f"{location}.closeout_requirements",
    )
    for index, requirement in enumerate(requirements):
        item_location = f"{location}.closeout_requirements[{index}]"
        required_refs = set(
            _require_string_list(
                requirement.get("required_ref_kinds"),
                location=f"{item_location}.required_ref_kinds",
            )
        )
        unknown_refs = sorted(required_refs - expected_artifacts)
        if unknown_refs:
            fail(f"{item_location}.required_ref_kinds are not expected artifacts: {unknown_refs}")
        guarded_refs = sorted(
            artifact_kind
            for artifact_kind in required_refs
            if artifact_guards[artifact_kind] is not None
        )
        if guarded_refs:
            fail(
                f"{item_location}.required_ref_kinds cannot require guarded artifacts: "
                f"{guarded_refs}"
            )


def _validate_contour(contour: dict[str, Any], *, index: int, repo_root: Path) -> None:
    location = f"contours[{index}]"
    source_ref = _require_string(
        contour.get("source_playbook_ref"),
        location=f"{location}.source_playbook_ref",
    )
    source_path = (repo_root / source_ref).resolve()
    playbook_root = (repo_root / "playbooks").resolve()
    try:
        source_path.relative_to(playbook_root)
    except ValueError:
        fail(f"{location}.source_playbook_ref must stay under playbooks/")
    if source_path.name != "PLAYBOOK.md":
        fail(f"{location}.source_playbook_ref must end with PLAYBOOK.md")
    frontmatter = _read_frontmatter(source_path)

    exact_fields = {
        "playbook_id": "id",
        "playbook_name": "name",
        "scenario": "scenario",
        "required_agent_ids": "participating_agents",
        "required_capability_ids": "required_skills",
        "expected_artifact_kinds": "expected_artifacts",
    }
    for contour_field, frontmatter_field in exact_fields.items():
        if contour.get(contour_field) != frontmatter.get(frontmatter_field):
            fail(
                f"{location}.{contour_field} must exactly match "
                f"{source_ref} frontmatter.{frontmatter_field}"
            )

    required_agents = set(
        _require_string_list(
            contour.get("required_agent_ids"),
            location=f"{location}.required_agent_ids",
        )
    )
    required_capabilities = set(
        _require_string_list(
            contour.get("required_capability_ids"),
            location=f"{location}.required_capability_ids",
        )
    )
    expected_artifacts = set(
        _require_string_list(
            contour.get("expected_artifact_kinds"),
            location=f"{location}.expected_artifact_kinds",
        )
    )
    input_artifacts = set(
        _require_string_list(
            contour.get("input_artifact_kinds"),
            location=f"{location}.input_artifact_kinds",
        )
    )
    unknown_input_artifacts = sorted(input_artifacts - expected_artifacts)
    if unknown_input_artifacts:
        fail(
            f"{location}.input_artifact_kinds are outside expected_artifact_kinds: "
            f"{unknown_input_artifacts}"
        )
    condition_ids = _validate_scenario_conditions(contour, location=location)
    (
        step_ids,
        outputs_by_step,
        inputs_by_step,
        guards_by_step,
    ) = _validate_step_graph(
        contour,
        location=location,
        required_agents=required_agents,
        required_capabilities=required_capabilities,
        expected_artifacts=expected_artifacts,
        input_artifacts=input_artifacts,
        condition_ids=condition_ids,
    )

    checkpoint = contour.get("checkpoint_policy")
    if not isinstance(checkpoint, dict):
        fail(f"{location}.checkpoint_policy must be an object")
    checkpoint_steps = set(
        _require_string_list(
            checkpoint.get("required_after_step_ids"),
            location=f"{location}.checkpoint_policy.required_after_step_ids",
        )
    )
    unknown_checkpoint_steps = sorted(checkpoint_steps - step_ids)
    if unknown_checkpoint_steps:
        fail(
            f"{location}.checkpoint_policy.required_after_step_ids reference unknown steps: "
            f"{unknown_checkpoint_steps}"
        )

    rollback = contour.get("rollback_policy")
    if not isinstance(rollback, dict):
        fail(f"{location}.rollback_policy must be an object")
    rollback_ref_present = rollback.get("rollback_artifact_input_ref") is not None
    if rollback.get("required") is not rollback_ref_present:
        fail(
            f"{location}.rollback_policy.required must be true exactly when "
            "rollback_artifact_input_ref is present"
        )

    evidence_ids, evidence_guards = _validate_evidence(
        contour,
        location=location,
        step_ids=step_ids,
        outputs_by_step=outputs_by_step,
        inputs_by_step=inputs_by_step,
        guards_by_step=guards_by_step,
        expected_artifacts=expected_artifacts,
        input_artifacts=input_artifacts,
        condition_ids=condition_ids,
    )
    _validate_eval_requirements(
        contour,
        location=location,
        frontmatter=frontmatter,
        evidence_ids=evidence_ids,
        evidence_guards=evidence_guards,
        condition_ids=condition_ids,
    )
    _validate_retention_requirements(
        contour,
        location=location,
        frontmatter=frontmatter,
        condition_ids=condition_ids,
    )
    artifact_guards = {artifact_kind: None for artifact_kind in input_artifacts}
    for step_id, outputs in outputs_by_step.items():
        for artifact_kind in outputs:
            artifact_guards[artifact_kind] = guards_by_step[step_id]
    _validate_closeout_requirements(
        contour,
        location=location,
        expected_artifacts=expected_artifacts,
        artifact_guards=artifact_guards,
    )


def _output_payload(source: dict[str, Any]) -> dict[str, Any]:
    contours = source.get("contours")
    assert isinstance(contours, list)
    return {
        "schema_version": OUTPUT_SCHEMA_VERSION,
        "layer": "aoa-playbooks",
        "abi": {
            "abi_id": ABI_ID,
            "abi_version": ABI_VERSION,
            "owner_repo": "aoa-playbooks",
            "schema_ref": SCHEMA_REF,
        },
        "source_of_truth": {
            "config": CONFIG_REF,
            "playbooks": PLAYBOOK_GLOB,
            "schema": SCHEMA_REF,
        },
        "contours": sorted(deepcopy(contours), key=lambda item: item["playbook_id"]),
    }


def _validate_output(payload: dict[str, Any]) -> None:
    schema = read_json(SCHEMA_PATH)
    if not isinstance(schema, dict):
        fail(f"{SCHEMA_REF} must contain a JSON object")
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(payload),
        key=lambda item: item.json_path,
    )
    if errors:
        error = errors[0]
        fail(f"generated projection violates {SCHEMA_REF} at {error.json_path}: {error.message}")


def validate_source_config(
    source: dict[str, Any],
    *,
    repo_root: Path = REPO_ROOT,
) -> None:
    _reject_executable_keys(source)
    if source.get("schema_version") != SOURCE_SCHEMA_VERSION:
        fail(f"{CONFIG_REF} must declare schema_version {SOURCE_SCHEMA_VERSION!r}")
    abi = source.get("abi")
    if not isinstance(abi, dict):
        fail(f"{CONFIG_REF}.abi must be an object")
    if abi.get("abi_id") != ABI_ID or abi.get("abi_version") != ABI_VERSION:
        fail(f"{CONFIG_REF}.abi must declare the stable {ABI_VERSION} ABI")

    contours = _require_object_list(source.get("contours"), location="contours")
    contour_ids = _require_unique(contours, "playbook_id", location="contours")
    _require_unique(contours, "playbook_name", location="contours")
    _require_unique(contours, "scenario", location="contours")
    _require_unique(contours, "source_playbook_ref", location="contours")
    if set(contour_ids) != REQUIRED_CONTOUR_IDS:
        fail(
            "contours must publish exactly the three C2 golden scenarios; "
            f"missing={sorted(REQUIRED_CONTOUR_IDS - set(contour_ids))}, "
            f"unexpected={sorted(set(contour_ids) - REQUIRED_CONTOUR_IDS)}"
        )

    for index, contour in enumerate(contours):
        _validate_contour(contour, index=index, repo_root=repo_root)

    _validate_output(_output_payload(source))


def build_output(source: dict[str, Any] | None = None) -> dict[str, Any]:
    loaded = load_source_config() if source is None else deepcopy(source)
    validate_source_config(loaded)
    return _output_payload(loaded)


def render_json(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when the committed generated projection differs from canonical inputs",
    )
    args = parser.parse_args(argv)

    try:
        rendered = render_json(build_output())
    except BuilderError as exc:
        print(f"error: {exc}")
        return 1

    if args.check:
        try:
            current = OUTPUT_PATH.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"error: missing generated output: {display_path(OUTPUT_PATH)}")
            return 1
        if current != rendered:
            print(
                "error: generated projection is out of date; run "
                f"{display_path(Path(__file__))}"
            )
            return 1
        print(f"OK: {display_path(OUTPUT_PATH)} is current")
        return 0

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    print(f"wrote {display_path(OUTPUT_PATH)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
