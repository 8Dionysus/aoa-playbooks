#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def repo_root_from_env(env_name: str, default: Path) -> Path:
    override = os.environ.get(env_name)
    if not override:
        return default
    return Path(override).expanduser().resolve()


AOA_AGENTS_ROOT = repo_root_from_env("AOA_AGENTS_ROOT", REPO_ROOT.parent / "aoa-agents")
AOA_EVALS_ROOT = repo_root_from_env("AOA_EVALS_ROOT", REPO_ROOT.parent / "aoa-evals")
AOA_SKILLS_ROOT = repo_root_from_env("AOA_SKILLS_ROOT", REPO_ROOT.parent / "aoa-skills")
AOA_MEMO_ROOT = repo_root_from_env("AOA_MEMO_ROOT", REPO_ROOT.parent / "aoa-memo")
REGISTRY_PATH = REPO_ROOT / "generated" / "playbook_registry.min.json"
ACTIVATION_COLLECTION_PATH = REPO_ROOT / "generated" / "playbook_activation_surfaces.min.json"
FEDERATION_COLLECTION_PATH = REPO_ROOT / "generated" / "playbook_federation_surfaces.min.json"
SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook-registry.schema.json"
PLAYBOOK_ROOT = REPO_ROOT / "playbooks"
AGENT_REGISTRY_PATH = AOA_AGENTS_ROOT / "generated" / "agent_registry.min.json"
MODEL_TIER_REGISTRY_PATH = AOA_AGENTS_ROOT / "generated" / "model_tier_registry.json"
EVAL_CATALOG_PATH = AOA_EVALS_ROOT / "generated" / "eval_catalog.min.json"
SKILL_GOVERNANCE_PATH = AOA_SKILLS_ROOT / "generated" / "governance_backlog.json"
ACTIVATION_SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook-activation-surface.schema.json"
FEDERATION_SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook-federation-surface.schema.json"
ACTIVATION_EXAMPLE_PATHS = {
    "AOA-P-0008": REPO_ROOT / "examples" / "playbook_activation.long-horizon-model-tier-orchestra.example.json",
    "AOA-P-0009": REPO_ROOT / "examples" / "playbook_activation.restartable-inquiry-loop.example.json",
    "AOA-P-0010": REPO_ROOT / "examples" / "playbook_activation.cross-repo-boundary-rollout.example.json",
}
ACTIVATION_COLLECTION_PLAYBOOK_IDS = ("AOA-P-0008", "AOA-P-0009", "AOA-P-0010")
FEDERATION_COLLECTION_PLAYBOOK_IDS = ("AOA-P-0007", "AOA-P-0008", "AOA-P-0009", "AOA-P-0010")
FEDERATION_REQUIRED_FRONTMATTER_KEYS = ("required_skills", "memo_contract_refs", "memo_writeback_targets")

ALLOWED_STATUS = {"active", "planned", "experimental", "deprecated"}
ALLOWED_MEMORY_POSTURE = {"none", "light_recall", "bounded_recall", "deep_recall"}
ALLOWED_EVAL_POSTURE = {"minimal", "required", "strict", "paired_eval"}
ALLOWED_FALLBACK = {"none", "handoff", "rollback", "safe_stop", "review_required"}
TIER_ARTIFACT_PLAYBOOKS = {"AOA-P-0008"}
REQUIRED_BUNDLE_SECTIONS = {
    "Intent",
    "Trigger boundary",
    "Prerequisites",
    "Participating agents",
    "Required skills",
    "Decision points",
    "Handoffs",
    "Fallback and rollback posture",
    "Expected evidence posture",
    "Expected artifacts",
    "Eval anchors",
    "Memory writeback",
    "Canonical route",
}
BUNDLE_SEMANTIC_CHECKS = {
    "AOA-P-0006": {
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-approval-gate-check",
            "aoa-dry-run-first",
            "aoa-change-protocol",
            "aoa-approval-boundary-adherence",
            "aoa-bounded-change-quality",
            "architect",
            "coder",
            "reviewer",
            "memory-keeper",
        ),
    },
    "AOA-P-0007": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-witness-trace-integrity",
                "aoa-compost-provenance-preservation",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-change-protocol",
            ),
            "memo_contract_refs": (
                "examples/recall_contract.router.semantic.json",
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "episode",
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-change-protocol",
            "aoa-witness-trace-integrity",
            "aoa-compost-provenance-preservation",
            "architect",
            "coder",
            "reviewer",
            "memory-keeper",
        ),
    },
    "AOA-P-0008": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-long-horizon-depth",
                "aoa-tool-trajectory-discipline",
            ),
            "required_skills": (
                "aoa-change-protocol",
                "aoa-source-of-truth-check",
                "aoa-dry-run-first",
                "aoa-bounded-context-map",
            ),
            "memo_contract_refs": (
                "examples/checkpoint_to_memory_contract.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "claim",
                "pattern",
            ),
        },
        "text_tokens": (
            "aoa-change-protocol",
            "aoa-source-of-truth-check",
            "aoa-dry-run-first",
            "aoa-bounded-context-map",
            "decision",
            "claim",
            "pattern",
        ),
    },
    "AOA-P-0009": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-long-horizon-depth",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-change-protocol",
                "aoa-dry-run-first",
                "aoa-bounded-context-map",
            ),
            "memo_contract_refs": (
                "examples/checkpoint_to_memory_contract.example.json",
            ),
            "memo_writeback_targets": (
                "state_capsule",
                "decision",
            ),
        },
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-change-protocol",
            "aoa-dry-run-first",
            "aoa-bounded-context-map",
            "state_capsule",
            "decision",
        ),
    },
    "AOA-P-0010": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-approval-boundary-adherence",
                "aoa-scope-drift-detection",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-bounded-context-map",
                "aoa-approval-gate-check",
                "aoa-dry-run-first",
                "aoa-change-protocol",
            ),
            "memo_contract_refs": (
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-bounded-context-map",
            "aoa-approval-gate-check",
            "aoa-dry-run-first",
            "aoa-change-protocol",
            "aoa-approval-boundary-adherence",
            "aoa-scope-drift-detection",
            "architect",
            "coder",
            "reviewer",
            "evaluator",
            "memory-keeper",
        ),
    },
}


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def display_path(path: Path) -> str:
    for root in (REPO_ROOT, AOA_AGENTS_ROOT, AOA_EVALS_ROOT, AOA_SKILLS_ROOT, AOA_MEMO_ROOT):
        try:
            return path.relative_to(root).as_posix()
        except ValueError:
            continue
    return path.as_posix()


def read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {display_path(path)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {display_path(path)}: {exc}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing required file: {display_path(path)}")


def parse_scalar(value: str) -> str:
    scalar = value.strip()
    if len(scalar) >= 2 and scalar[0] in {"'", '"'} and scalar[-1] == scalar[0]:
        return scalar[1:-1]
    return scalar


def parse_frontmatter(text: str, path: Path) -> tuple[dict[str, object], str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        fail(f"{path.relative_to(REPO_ROOT).as_posix()} must start with YAML frontmatter")

    frontmatter: dict[str, object] = {}
    current_key: str | None = None
    body_start = 0

    for index in range(1, len(lines)):
        line = lines[index]
        if line.strip() == "---":
            body_start = index + 1
            break
        if not line.strip():
            continue
        if line.startswith("  - ") or line.startswith("- "):
            if current_key is None:
                fail(f"{path.relative_to(REPO_ROOT).as_posix()} has a list item without a key in frontmatter")
            frontmatter.setdefault(current_key, [])
            assert isinstance(frontmatter[current_key], list)
            frontmatter[current_key].append(parse_scalar(line.split("-", 1)[1]))
            continue
        if ":" not in line:
            fail(f"{path.relative_to(REPO_ROOT).as_posix()} has an invalid frontmatter line: {line}")
        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if not value:
            frontmatter[key] = []
            current_key = key
            continue
        frontmatter[key] = parse_scalar(value)
        current_key = key
    else:
        fail(f"{path.relative_to(REPO_ROOT).as_posix()} is missing the closing YAML frontmatter boundary")

    return frontmatter, "\n".join(lines[body_start:])


def markdown_sections(body: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current_heading: str | None = None
    current_lines: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            if current_heading is not None:
                sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = line[3:].strip()
            current_lines = []
            continue
        if current_heading is not None:
            current_lines.append(line)
    if current_heading is not None:
        sections[current_heading] = "\n".join(current_lines).strip()
    return sections


def authored_bundle_paths() -> list[Path]:
    if not PLAYBOOK_ROOT.exists():
        return []
    return sorted(path for path in PLAYBOOK_ROOT.rglob("PLAYBOOK.md") if path.is_file())


def validate_schema_surface() -> None:
    schema = read_json(SCHEMA_PATH)
    if not isinstance(schema, dict):
        fail("schema file must contain a JSON object")
    required_top_level = {"$schema", "$id", "title", "type", "properties", "required"}
    missing = sorted(required_top_level - set(schema))
    if missing:
        fail(f"schema is missing required top-level keys: {', '.join(missing)}")


def validate_activation_schema_surface() -> dict[str, object]:
    schema = read_json(ACTIVATION_SCHEMA_PATH)
    if not isinstance(schema, dict):
        fail("playbook activation schema file must contain a JSON object")
    required_top_level = {"$schema", "$id", "title", "type", "properties", "required"}
    missing = sorted(required_top_level - set(schema))
    if missing:
        fail(f"playbook activation schema is missing required top-level keys: {', '.join(missing)}")
    if schema.get("type") != "object":
        fail("playbook activation schema must declare type 'object'")
    properties = schema.get("properties")
    if not isinstance(properties, dict) or "surface_type" not in properties:
        fail("playbook activation schema must expose a surface_type property")
    surface_type = properties["surface_type"]
    if not isinstance(surface_type, dict) or surface_type.get("const") != "playbook_activation_surface":
        fail("playbook activation schema must pin surface_type.const to 'playbook_activation_surface'")
    return schema


def validate_federation_schema_surface() -> dict[str, object]:
    schema = read_json(FEDERATION_SCHEMA_PATH)
    if not isinstance(schema, dict):
        fail("playbook federation schema file must contain a JSON object")
    required_top_level = {"$schema", "$id", "title", "type", "properties", "required"}
    missing = sorted(required_top_level - set(schema))
    if missing:
        fail(f"playbook federation schema is missing required top-level keys: {', '.join(missing)}")
    if schema.get("type") != "object":
        fail("playbook federation schema must declare type 'object'")
    properties = schema.get("properties")
    if not isinstance(properties, dict) or "surface_type" not in properties:
        fail("playbook federation schema must expose a surface_type property")
    surface_type = properties["surface_type"]
    if not isinstance(surface_type, dict) or surface_type.get("const") != "playbook_federation_surface":
        fail("playbook federation schema must pin surface_type.const to 'playbook_federation_surface'")
    return schema


def validate_registry() -> dict[str, dict[str, object]]:
    payload = read_json(REGISTRY_PATH)
    if not isinstance(payload, dict):
        fail("playbook registry must be a JSON object")

    for key in ("version", "layer", "playbooks"):
        if key not in payload:
            fail(f"playbook registry is missing required key '{key}'")

    if not isinstance(payload["version"], int) or payload["version"] < 1:
        fail("registry 'version' must be an integer >= 1")
    if payload["layer"] != "aoa-playbooks":
        fail("registry 'layer' must equal 'aoa-playbooks'")

    playbooks = payload["playbooks"]
    if not isinstance(playbooks, list) or not playbooks:
        fail("registry 'playbooks' must be a non-empty list")

    seen_ids: set[str] = set()
    required_seed = {"repo-bootstrap", "safe-change-rollout", "bounded-research-pass", "release-prep", "memory-curation-pass"}
    seen_names: set[str] = set()
    playbooks_by_id: dict[str, dict[str, object]] = {}

    for index, playbook in enumerate(playbooks):
        location = f"playbooks[{index}]"
        if not isinstance(playbook, dict):
            fail(f"{location} must be an object")

        for key in (
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
        ):
            if key not in playbook:
                fail(f"{location} is missing required key '{key}'")

        playbook_id = playbook["id"]
        name = playbook["name"]
        status = playbook["status"]
        summary = playbook["summary"]
        scenario = playbook["scenario"]
        trigger = playbook["trigger"]
        prerequisites = playbook["prerequisites"]
        participating_agents = playbook["participating_agents"]
        required_skill_families = playbook["required_skill_families"]
        evaluation_posture = playbook["evaluation_posture"]
        memory_posture = playbook["memory_posture"]
        fallback_mode = playbook["fallback_mode"]
        expected_artifacts = playbook["expected_artifacts"]

        if not isinstance(playbook_id, str) or len(playbook_id) < 3:
            fail(f"{location}.id must be a string of length >= 3")
        if playbook_id in seen_ids:
            fail(f"duplicate playbook id in registry: '{playbook_id}'")
        seen_ids.add(playbook_id)
        playbooks_by_id[playbook_id] = playbook

        if not isinstance(name, str) or len(name) < 3:
            fail(f"{location}.name must be a string of length >= 3")
        if name in seen_names:
            fail(f"duplicate playbook name in registry: '{name}'")
        seen_names.add(name)
        if status not in ALLOWED_STATUS:
            fail(f"{location}.status '{status}' is not allowed")
        if not isinstance(summary, str) or len(summary) < 10:
            fail(f"{location}.summary must be a string of length >= 10")
        if not isinstance(scenario, str) or len(scenario) < 3:
            fail(f"{location}.scenario must be a string of length >= 3")
        if not isinstance(trigger, str) or len(trigger) < 3:
            fail(f"{location}.trigger must be a string of length >= 3")

        for array_name, value in (
            ("prerequisites", prerequisites),
            ("participating_agents", participating_agents),
            ("required_skill_families", required_skill_families),
            ("expected_artifacts", expected_artifacts),
        ):
            if not isinstance(value, list) or not value:
                fail(f"{location}.{array_name} must be a non-empty list")
            for item in value:
                if not isinstance(item, str) or len(item) < 2:
                    fail(f"{location}.{array_name} contains an invalid entry")

        eval_anchors = playbook.get("eval_anchors")
        if eval_anchors is not None:
            if not isinstance(eval_anchors, list) or not eval_anchors:
                fail(f"{location}.eval_anchors must be a non-empty list when present")
            for anchor in eval_anchors:
                if not isinstance(anchor, str) or len(anchor) < 3:
                    fail(f"{location}.eval_anchors contains an invalid entry")

        if evaluation_posture not in ALLOWED_EVAL_POSTURE:
            fail(f"{location}.evaluation_posture '{evaluation_posture}' is not allowed")
        if memory_posture not in ALLOWED_MEMORY_POSTURE:
            fail(f"{location}.memory_posture '{memory_posture}' is not allowed")
        if fallback_mode not in ALLOWED_FALLBACK:
            fail(f"{location}.fallback_mode '{fallback_mode}' is not allowed")

    missing_seed = sorted(required_seed - seen_names)
    if missing_seed:
        fail(f"playbook registry is missing required seed playbooks: {', '.join(missing_seed)}")
    return playbooks_by_id


def load_agent_names() -> set[str]:
    payload = read_json(AGENT_REGISTRY_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("agents"), list):
        fail("aoa-agents/generated/agent_registry.min.json must contain an 'agents' list")
    agent_names = {
        item["name"]
        for item in payload["agents"]
        if isinstance(item, dict) and isinstance(item.get("name"), str)
    }
    if not agent_names:
        fail("aoa-agents/generated/agent_registry.min.json must list at least one agent")
    return agent_names


def load_model_tier_artifacts() -> set[str]:
    payload = read_json(MODEL_TIER_REGISTRY_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("model_tiers"), list):
        fail("aoa-agents/generated/model_tier_registry.json must contain a 'model_tiers' list")
    artifacts = {
        item["artifact_requirement"]
        for item in payload["model_tiers"]
        if isinstance(item, dict) and isinstance(item.get("artifact_requirement"), str)
    }
    if not artifacts:
        fail("aoa-agents/generated/model_tier_registry.json must list at least one artifact requirement")
    return artifacts


def load_eval_catalog() -> dict[str, dict[str, object]]:
    payload = read_json(EVAL_CATALOG_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("evals"), list):
        fail("aoa-evals/generated/eval_catalog.min.json must contain an 'evals' list")
    evals_by_name: dict[str, dict[str, object]] = {}
    for item in payload["evals"]:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if isinstance(name, str):
            evals_by_name[name] = item
    if not evals_by_name:
        fail("aoa-evals/generated/eval_catalog.min.json must list at least one eval")
    return evals_by_name


def load_skill_catalog() -> dict[str, dict[str, object]]:
    payload = read_json(SKILL_GOVERNANCE_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("skills"), list):
        fail("aoa-skills/generated/governance_backlog.json must contain a 'skills' list")
    skills_by_name: dict[str, dict[str, object]] = {}
    for item in payload["skills"]:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if isinstance(name, str):
            skills_by_name[name] = item
    if not skills_by_name:
        fail("aoa-skills/generated/governance_backlog.json must list at least one skill")
    return skills_by_name


def collect_string_field_values(payload: object, field_name: str) -> set[str]:
    values: set[str] = set()
    if isinstance(payload, dict):
        for key, value in payload.items():
            if key == field_name and isinstance(value, str):
                values.add(value)
            values.update(collect_string_field_values(value, field_name))
    elif isinstance(payload, list):
        for item in payload:
            values.update(collect_string_field_values(item, field_name))
    return values


def memo_contract_path(contract_ref: str) -> Path:
    return AOA_MEMO_ROOT / contract_ref


def memo_kinds_for_contract(contract_ref: str) -> set[str]:
    path = memo_contract_path(contract_ref)
    payload = read_json(path)
    kinds = collect_string_field_values(payload, "kind")
    kinds.update(collect_string_field_values(payload, "target_kind"))
    if isinstance(payload, dict) and "memory_object_ids" in payload and "timeline" in payload:
        kinds.add("provenance_thread")
    return kinds


def validate_projection_refs(
    *,
    location: str,
    participating_agents: object,
    expected_artifacts: object,
    eval_anchors: object,
    agent_names: set[str],
    model_tier_artifacts: set[str],
    evals_by_name: dict[str, dict[str, object]],
) -> None:
    if not isinstance(participating_agents, list) or not participating_agents:
        fail(f"{location} must expose a non-empty participating_agents list")
    missing_agents = [
        item for item in participating_agents if not isinstance(item, str) or item not in agent_names
    ]
    if missing_agents:
        fail(
            f"{location} references participating_agents that do not resolve in aoa-agents: "
            + ", ".join(str(item) for item in missing_agents)
        )

    if not isinstance(expected_artifacts, list) or not expected_artifacts:
        fail(f"{location} must expose a non-empty expected_artifacts list")
    if location.endswith("AOA-P-0008"):
        unknown_artifacts = [
            item
            for item in expected_artifacts
            if not isinstance(item, str) or item not in model_tier_artifacts
        ]
        if unknown_artifacts:
            fail(
                f"{location} expected_artifacts do not resolve against aoa-agents model-tier artifacts: "
                + ", ".join(str(item) for item in unknown_artifacts)
            )

    if eval_anchors is None:
        return
    if not isinstance(eval_anchors, list) or not eval_anchors:
        fail(f"{location} must expose a non-empty eval_anchors list when present")
    missing_eval_anchors = [
        anchor for anchor in eval_anchors if not isinstance(anchor, str) or anchor not in evals_by_name
    ]
    if missing_eval_anchors:
        fail(
            f"{location} references eval_anchors that do not resolve in aoa-evals: "
            + ", ".join(str(item) for item in missing_eval_anchors)
        )


def activation_surface_for_playbook(playbook_id: str, registry_entry: dict[str, object]) -> dict[str, object]:
    payload: dict[str, object] = {
        "surface_type": "playbook_activation_surface",
        "playbook_id": playbook_id,
        "name": registry_entry["name"],
        "scenario": registry_entry["scenario"],
        "trigger": registry_entry["trigger"],
        "participating_agents": registry_entry["participating_agents"],
        "required_skill_families": registry_entry["required_skill_families"],
        "expected_artifacts": registry_entry["expected_artifacts"],
        "evaluation_posture": registry_entry["evaluation_posture"],
        "memory_posture": registry_entry["memory_posture"],
        "fallback_mode": registry_entry["fallback_mode"],
    }
    if "eval_anchors" in registry_entry:
        payload["eval_anchors"] = registry_entry["eval_anchors"]
    return payload


def activation_surfaces_for_playbooks(
    playbooks_by_id: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    surfaces: list[dict[str, object]] = []
    for playbook_id in ACTIVATION_COLLECTION_PLAYBOOK_IDS:
        if playbook_id not in playbooks_by_id:
            fail(f"playbook registry is missing required activation target '{playbook_id}'")
        surfaces.append(activation_surface_for_playbook(playbook_id, playbooks_by_id[playbook_id]))
    return surfaces


def validate_activation_collection(
    playbooks_by_id: dict[str, dict[str, object]],
    *,
    agent_names: set[str],
    model_tier_artifacts: set[str],
    evals_by_name: dict[str, dict[str, object]],
) -> None:
    payload = read_json(ACTIVATION_COLLECTION_PATH)
    if not isinstance(payload, list):
        fail("generated/playbook_activation_surfaces.min.json must be a JSON array")

    expected = activation_surfaces_for_playbooks(playbooks_by_id)
    if payload != expected:
        fail(
            "generated/playbook_activation_surfaces.min.json is out of date; "
            "run scripts/generate_playbook_activation_surfaces.py"
        )

    for index, surface in enumerate(payload):
        if not isinstance(surface, dict):
            fail(f"generated/playbook_activation_surfaces.min.json[{index}] must be an object")
        playbook_id = surface.get("playbook_id")
        if not isinstance(playbook_id, str):
            fail(f"generated/playbook_activation_surfaces.min.json[{index}] is missing a string playbook_id")
        validate_projection_refs(
            location=f"generated/playbook_activation_surfaces.min.json[{index}]:{playbook_id}",
            participating_agents=surface.get("participating_agents"),
            expected_artifacts=surface.get("expected_artifacts"),
            eval_anchors=surface.get("eval_anchors"),
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
        )


def federation_surface_for_frontmatter(frontmatter: dict[str, object]) -> dict[str, object]:
    payload: dict[str, object] = {
        "surface_type": "playbook_federation_surface",
        "playbook_id": frontmatter["id"],
        "name": frontmatter["name"],
        "participating_agents": frontmatter["participating_agents"],
        "memory_posture": frontmatter["memory_posture"],
        "required_skills": frontmatter["required_skills"],
        "memo_contract_refs": frontmatter["memo_contract_refs"],
        "memo_writeback_targets": frontmatter["memo_writeback_targets"],
    }
    if "eval_anchors" in frontmatter:
        payload["eval_anchors"] = frontmatter["eval_anchors"]
    return payload


def validate_federation_bundle(
    *,
    bundle_path: Path,
    frontmatter: dict[str, object],
    sections: dict[str, str],
    skills_by_name: dict[str, dict[str, object]],
) -> None:
    bundle_location = bundle_path.relative_to(REPO_ROOT).as_posix()

    for key in FEDERATION_REQUIRED_FRONTMATTER_KEYS:
        if key not in frontmatter:
            fail(f"{bundle_location} is missing required federation frontmatter '{key}'")

    required_skills = frontmatter["required_skills"]
    memo_contract_refs = frontmatter["memo_contract_refs"]
    memo_writeback_targets = frontmatter["memo_writeback_targets"]
    participating_agents = frontmatter.get("participating_agents")
    eval_anchors = frontmatter.get("eval_anchors")

    for field_name, value in (
        ("required_skills", required_skills),
        ("memo_contract_refs", memo_contract_refs),
        ("memo_writeback_targets", memo_writeback_targets),
    ):
        if not isinstance(value, list) or not value:
            fail(f"{bundle_location} federation field '{field_name}' must be a non-empty list")
        for item in value:
            if not isinstance(item, str) or len(item) < 3:
                fail(f"{bundle_location} federation field '{field_name}' contains an invalid entry")

    if not isinstance(eval_anchors, list) or not eval_anchors:
        fail(f"{bundle_location} federation-checked playbooks must expose non-empty 'eval_anchors'")

    if not isinstance(participating_agents, list) or "memory-keeper" not in participating_agents:
        fail(
            f"{bundle_location} federation-checked playbooks with memo writeback targets must include "
            "'memory-keeper' in participating_agents"
        )

    missing_skills: list[str] = []
    invalid_skill_readiness: list[str] = []
    for skill_name in required_skills:
        skill = skills_by_name.get(skill_name)
        if skill is None:
            missing_skills.append(skill_name)
            continue
        if skill.get("lineage_state") != "published" or skill.get("readiness_reconciliation") != "governance_and_eval_ready":
            invalid_skill_readiness.append(skill_name)
    if missing_skills:
        fail(
            f"{bundle_location} required_skills do not resolve in aoa-skills/generated/governance_backlog.json: "
            + ", ".join(missing_skills)
        )
    if invalid_skill_readiness:
        fail(
            f"{bundle_location} required_skills are not federation-ready in aoa-skills/generated/governance_backlog.json: "
            + ", ".join(invalid_skill_readiness)
        )

    allowed_memo_kinds: set[str] = set()
    missing_memo_contract_refs: list[str] = []
    for contract_ref in memo_contract_refs:
        contract_path = memo_contract_path(contract_ref)
        if not contract_path.exists():
            missing_memo_contract_refs.append(contract_ref)
            continue
        allowed_memo_kinds.update(memo_kinds_for_contract(contract_ref))
    if missing_memo_contract_refs:
        fail(
            f"{bundle_location} memo_contract_refs do not resolve in aoa-memo: "
            + ", ".join(missing_memo_contract_refs)
        )

    invalid_targets = [target for target in memo_writeback_targets if target not in allowed_memo_kinds]
    if invalid_targets:
        allowed_list = ", ".join(sorted(allowed_memo_kinds)) if allowed_memo_kinds else "none"
        fail(
            f"{bundle_location} memo_writeback_targets are not supported by the referenced aoa-memo contracts: "
            + ", ".join(invalid_targets)
            + f" (allowed: {allowed_list})"
        )

    memory_writeback_section = sections.get("Memory writeback", "")
    for target in memo_writeback_targets:
        if target not in memory_writeback_section:
            fail(
                f"{bundle_location} Memory writeback section must mention federation target '{target}' explicitly"
            )


def federation_surfaces_for_bundles(
    frontmatter_by_id: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    surfaces: list[dict[str, object]] = []
    for playbook_id in FEDERATION_COLLECTION_PLAYBOOK_IDS:
        if playbook_id not in frontmatter_by_id:
            fail(f"authored bundles are missing required federation target '{playbook_id}'")
        surfaces.append(federation_surface_for_frontmatter(frontmatter_by_id[playbook_id]))
    return surfaces


def validate_federation_collection(
    frontmatter_by_id: dict[str, dict[str, object]],
    *,
    agent_names: set[str],
    evals_by_name: dict[str, dict[str, object]],
    skills_by_name: dict[str, dict[str, object]],
) -> None:
    payload = read_json(FEDERATION_COLLECTION_PATH)
    if not isinstance(payload, list):
        fail("generated/playbook_federation_surfaces.min.json must be a JSON array")

    expected = federation_surfaces_for_bundles(frontmatter_by_id)
    if payload != expected:
        fail(
            "generated/playbook_federation_surfaces.min.json is out of date; "
            "run scripts/generate_playbook_federation_surfaces.py"
        )

    for index, surface in enumerate(payload):
        if not isinstance(surface, dict):
            fail(f"generated/playbook_federation_surfaces.min.json[{index}] must be an object")
        playbook_id = surface.get("playbook_id")
        if not isinstance(playbook_id, str):
            fail(f"generated/playbook_federation_surfaces.min.json[{index}] is missing a string playbook_id")

        participating_agents = surface.get("participating_agents")
        if not isinstance(participating_agents, list) or not participating_agents:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must expose a non-empty "
                "participating_agents list"
            )
        if "memory-keeper" not in participating_agents:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must include 'memory-keeper' in "
                "participating_agents"
            )
        missing_agents = [
            item for item in participating_agents if not isinstance(item, str) or item not in agent_names
        ]
        if missing_agents:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] references participating_agents "
                f"that do not resolve in aoa-agents: {', '.join(str(item) for item in missing_agents)}"
            )

        eval_anchors = surface.get("eval_anchors")
        if not isinstance(eval_anchors, list) or not eval_anchors:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must expose a non-empty eval_anchors list"
            )
        missing_eval_anchors = [
            anchor for anchor in eval_anchors if not isinstance(anchor, str) or anchor not in evals_by_name
        ]
        if missing_eval_anchors:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] references eval_anchors that do not "
                f"resolve in aoa-evals: {', '.join(str(item) for item in missing_eval_anchors)}"
            )

        required_skills = surface.get("required_skills")
        if not isinstance(required_skills, list) or not required_skills:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must expose a non-empty required_skills list"
            )
        unresolved_skills = [skill for skill in required_skills if not isinstance(skill, str) or skill not in skills_by_name]
        if unresolved_skills:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] references required_skills that do not "
                f"resolve in aoa-skills: {', '.join(str(item) for item in unresolved_skills)}"
            )
        invalid_skill_readiness = [
            skill
            for skill in required_skills
            if isinstance(skill, str)
            and skill in skills_by_name
            and (
                skills_by_name[skill].get("lineage_state") != "published"
                or skills_by_name[skill].get("readiness_reconciliation") != "governance_and_eval_ready"
            )
        ]
        if invalid_skill_readiness:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] references required_skills that are "
                f"not federation-ready in aoa-skills: {', '.join(invalid_skill_readiness)}"
            )

        memo_contract_refs = surface.get("memo_contract_refs")
        if not isinstance(memo_contract_refs, list) or not memo_contract_refs:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must expose a non-empty "
                "memo_contract_refs list"
            )
        allowed_memo_kinds: set[str] = set()
        missing_contracts: list[str] = []
        for contract_ref in memo_contract_refs:
            if not isinstance(contract_ref, str):
                missing_contracts.append(str(contract_ref))
                continue
            contract_path = memo_contract_path(contract_ref)
            if not contract_path.exists():
                missing_contracts.append(contract_ref)
                continue
            allowed_memo_kinds.update(memo_kinds_for_contract(contract_ref))
        if missing_contracts:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] references memo_contract_refs that do "
                f"not resolve in aoa-memo: {', '.join(missing_contracts)}"
            )

        memo_writeback_targets = surface.get("memo_writeback_targets")
        if not isinstance(memo_writeback_targets, list) or not memo_writeback_targets:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must expose a non-empty "
                "memo_writeback_targets list"
            )
        invalid_targets = [
            target
            for target in memo_writeback_targets
            if not isinstance(target, str) or target not in allowed_memo_kinds
        ]
        if invalid_targets:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] exposes memo_writeback_targets that are "
                f"not supported by the referenced aoa-memo contracts: {', '.join(str(item) for item in invalid_targets)}"
            )


def validate_cross_repo_bundle(
    *,
    bundle_path: Path,
    frontmatter: dict[str, object],
    sections: dict[str, str],
    agent_names: set[str],
    model_tier_artifacts: set[str],
    evals_by_name: dict[str, dict[str, object]],
) -> None:
    bundle_location = bundle_path.relative_to(REPO_ROOT).as_posix()

    participating_agents = frontmatter.get("participating_agents")
    if not isinstance(participating_agents, list):
        fail(f"{bundle_location} is missing required list frontmatter 'participating_agents'")
    missing_agents = [
        item for item in participating_agents if not isinstance(item, str) or item not in agent_names
    ]
    if missing_agents:
        fail(
            f"{bundle_location} references participating_agents that do not resolve in aoa-agents: "
            + ", ".join(str(item) for item in missing_agents)
        )

    playbook_id = frontmatter.get("id")
    validate_projection_refs(
        location=f"{bundle_location}:{playbook_id}",
        participating_agents=participating_agents,
        expected_artifacts=frontmatter.get("expected_artifacts"),
        eval_anchors=frontmatter.get("eval_anchors"),
        agent_names=agent_names,
        model_tier_artifacts=model_tier_artifacts,
        evals_by_name=evals_by_name,
    )

    eval_anchors = frontmatter.get("eval_anchors")
    if eval_anchors is None:
        return
    draft_eval_anchors = [
        anchor
        for anchor in eval_anchors
        if isinstance(anchor, str) and evals_by_name[anchor].get("status") == "draft"
    ]
    if draft_eval_anchors:
        if frontmatter.get("status") != "experimental":
            fail(
                f"{bundle_location} uses draft eval_anchors and must remain experimental: "
                + ", ".join(draft_eval_anchors)
            )
        eval_anchor_section = sections.get("Eval anchors", "").lower()
        if "draft" not in eval_anchor_section or "review-only" not in eval_anchor_section:
            fail(
                f"{bundle_location} must state that draft eval_anchors are draft and review-only in the "
                "'Eval anchors' section"
            )


def validate_authored_bundles(
    playbooks_by_id: dict[str, dict[str, object]],
    *,
    agent_names: set[str],
    model_tier_artifacts: set[str],
    evals_by_name: dict[str, dict[str, object]],
    skills_by_name: dict[str, dict[str, object]],
) -> dict[str, dict[str, object]]:
    seen_bundle_ids: set[str] = set()
    seen_bundle_names: set[str] = set()
    frontmatter_by_id: dict[str, dict[str, object]] = {}

    for bundle_path in authored_bundle_paths():
        text = read_text(bundle_path)
        frontmatter, body = parse_frontmatter(text, bundle_path)
        sections = markdown_sections(body)

        playbook_id = frontmatter.get("id")
        if not isinstance(playbook_id, str) or not playbook_id:
            fail(f"{bundle_path.relative_to(REPO_ROOT).as_posix()} is missing a non-empty frontmatter 'id'")
        if playbook_id in seen_bundle_ids:
            fail(f"duplicate authored bundle id discovered: '{playbook_id}'")
        seen_bundle_ids.add(playbook_id)
        frontmatter_by_id[playbook_id] = frontmatter

        if playbook_id not in playbooks_by_id:
            fail(f"{bundle_path.relative_to(REPO_ROOT).as_posix()} has no registry entry for '{playbook_id}'")
        registry_entry = playbooks_by_id[playbook_id]

        bundle_name = frontmatter.get("name")
        if not isinstance(bundle_name, str) or not bundle_name:
            fail(f"{bundle_path.relative_to(REPO_ROOT).as_posix()} is missing a non-empty frontmatter 'name'")
        if bundle_name in seen_bundle_names:
            fail(f"duplicate authored bundle name discovered: '{bundle_name}'")
        seen_bundle_names.add(bundle_name)

        expected_path = PLAYBOOK_ROOT / bundle_name / "PLAYBOOK.md"
        if bundle_path != expected_path:
            fail(
                f"{bundle_path.relative_to(REPO_ROOT).as_posix()} must live at "
                f"{expected_path.relative_to(REPO_ROOT).as_posix()} to match its bundle name"
            )

        for key in (
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
        ):
            if key not in frontmatter:
                fail(f"{bundle_path.relative_to(REPO_ROOT).as_posix()} is missing frontmatter key '{key}'")
            if frontmatter[key] != registry_entry[key]:
                fail(
                    f"{bundle_path.relative_to(REPO_ROOT).as_posix()} frontmatter '{key}' does not match "
                    f"generated/playbook_registry.min.json"
                )
        if "eval_anchors" in registry_entry:
            if frontmatter.get("eval_anchors") != registry_entry["eval_anchors"]:
                fail(
                    f"{bundle_path.relative_to(REPO_ROOT).as_posix()} frontmatter 'eval_anchors' does not match "
                    f"generated/playbook_registry.min.json"
                )

        missing_sections = sorted(REQUIRED_BUNDLE_SECTIONS - set(sections))
        if missing_sections:
            fail(
                f"{bundle_path.relative_to(REPO_ROOT).as_posix()} is missing required sections: "
                f"{', '.join(missing_sections)}"
            )

        semantic_checks = BUNDLE_SEMANTIC_CHECKS.get(playbook_id, {})

        for field_name, expected_items in semantic_checks.get("frontmatter_lists", {}).items():
            value = frontmatter.get(field_name)
            if not isinstance(value, list):
                fail(
                    f"{bundle_path.relative_to(REPO_ROOT).as_posix()} is missing required list frontmatter "
                    f"'{field_name}'"
                )
            actual_items = tuple(item for item in value if isinstance(item, str))
            if actual_items != expected_items:
                fail(
                    f"{bundle_path.relative_to(REPO_ROOT).as_posix()} frontmatter '{field_name}' must equal "
                    f"{list(expected_items)}"
                )

        for token in semantic_checks.get("text_tokens", ()):
            if token not in text:
                fail(f"{bundle_path.relative_to(REPO_ROOT).as_posix()} must mention '{token}' explicitly")

        validate_cross_repo_bundle(
            bundle_path=bundle_path,
            frontmatter=frontmatter,
            sections=sections,
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
        )
        if playbook_id in FEDERATION_COLLECTION_PLAYBOOK_IDS:
            validate_federation_bundle(
                bundle_path=bundle_path,
                frontmatter=frontmatter,
                sections=sections,
                skills_by_name=skills_by_name,
            )

    missing_semantic_check_bundles = sorted(set(BUNDLE_SEMANTIC_CHECKS) - seen_bundle_ids)
    if missing_semantic_check_bundles:
        fail(
            "authored bundle validation expected bundle ids that were not discovered: "
            + ", ".join(missing_semantic_check_bundles)
        )
    return frontmatter_by_id


def validate_activation_examples(
    playbooks_by_id: dict[str, dict[str, object]],
    *,
    agent_names: set[str],
    model_tier_artifacts: set[str],
    evals_by_name: dict[str, dict[str, object]],
) -> None:
    for playbook_id, example_path in ACTIVATION_EXAMPLE_PATHS.items():
        payload = read_json(example_path)
        location = example_path.relative_to(REPO_ROOT).as_posix()
        if not isinstance(payload, dict):
            fail(f"{location} must contain a JSON object")

        if playbook_id not in playbooks_by_id:
            fail(f"{location} references playbook_id '{playbook_id}' that is missing from the registry")

        registry_entry = playbooks_by_id[playbook_id]
        expected = activation_surface_for_playbook(playbook_id, registry_entry)
        if payload != expected:
            fail(f"{location} does not match generated/playbook_activation_surfaces.min.json")

        validate_projection_refs(
            location=f"{location}:{playbook_id}",
            participating_agents=payload.get("participating_agents"),
            expected_artifacts=payload.get("expected_artifacts"),
            eval_anchors=payload.get("eval_anchors"),
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
        )


def main() -> int:
    try:
        validate_schema_surface()
        validate_activation_schema_surface()
        validate_federation_schema_surface()
        playbooks_by_id = validate_registry()
        agent_names = load_agent_names()
        model_tier_artifacts = load_model_tier_artifacts()
        evals_by_name = load_eval_catalog()
        skills_by_name = load_skill_catalog()
        validate_activation_collection(
            playbooks_by_id,
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
        )
        frontmatter_by_id = validate_authored_bundles(
            playbooks_by_id,
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
            skills_by_name=skills_by_name,
        )
        validate_federation_collection(
            frontmatter_by_id,
            agent_names=agent_names,
            evals_by_name=evals_by_name,
            skills_by_name=skills_by_name,
        )
        validate_activation_examples(
            playbooks_by_id,
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
        )
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    print("[ok] validated playbook registry schema surface")
    print("[ok] validated playbook activation schema surface")
    print("[ok] validated playbook federation schema surface")
    print("[ok] validated generated/playbook_registry.min.json")
    print("[ok] validated generated/playbook_activation_surfaces.min.json")
    print("[ok] validated authored playbook bundles")
    print("[ok] validated generated/playbook_federation_surfaces.min.json")
    print("[ok] validated playbook activation examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
