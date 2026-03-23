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
REGISTRY_PATH = REPO_ROOT / "generated" / "playbook_registry.min.json"
SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook-registry.schema.json"
PLAYBOOK_ROOT = REPO_ROOT / "playbooks"
AGENT_REGISTRY_PATH = AOA_AGENTS_ROOT / "generated" / "agent_registry.min.json"
MODEL_TIER_REGISTRY_PATH = AOA_AGENTS_ROOT / "generated" / "model_tier_registry.json"
EVAL_CATALOG_PATH = AOA_EVALS_ROOT / "generated" / "eval_catalog.min.json"
ACTIVATION_SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook-activation-surface.schema.json"
ACTIVATION_EXAMPLE_PATHS = {
    "AOA-P-0008": REPO_ROOT / "examples" / "playbook_activation.long-horizon-model-tier-orchestra.example.json",
    "AOA-P-0009": REPO_ROOT / "examples" / "playbook_activation.restartable-inquiry-loop.example.json",
}

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
        },
    },
    "AOA-P-0009": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-long-horizon-depth",
            ),
        },
    },
}


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def display_path(path: Path) -> str:
    for root in (REPO_ROOT, AOA_AGENTS_ROOT, AOA_EVALS_ROOT):
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
) -> None:
    seen_bundle_ids: set[str] = set()
    seen_bundle_names: set[str] = set()

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

    missing_semantic_check_bundles = sorted(set(BUNDLE_SEMANTIC_CHECKS) - seen_bundle_ids)
    if missing_semantic_check_bundles:
        fail(
            "authored bundle validation expected bundle ids that were not discovered: "
            + ", ".join(missing_semantic_check_bundles)
        )


def validate_activation_examples(
    playbooks_by_id: dict[str, dict[str, object]],
    *,
    agent_names: set[str],
    model_tier_artifacts: set[str],
    evals_by_name: dict[str, dict[str, object]],
) -> None:
    shared_keys = (
        "name",
        "scenario",
        "trigger",
        "participating_agents",
        "required_skill_families",
        "expected_artifacts",
        "evaluation_posture",
        "memory_posture",
        "fallback_mode",
        "eval_anchors",
    )

    for playbook_id, example_path in ACTIVATION_EXAMPLE_PATHS.items():
        payload = read_json(example_path)
        location = example_path.relative_to(REPO_ROOT).as_posix()
        if not isinstance(payload, dict):
            fail(f"{location} must contain a JSON object")

        for key in (
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
        ):
            if key not in payload:
                fail(f"{location} is missing required key '{key}'")

        if payload["surface_type"] != "playbook_activation_surface":
            fail(f"{location}.surface_type must equal 'playbook_activation_surface'")
        if payload["playbook_id"] != playbook_id:
            fail(f"{location}.playbook_id must equal '{playbook_id}'")
        if playbook_id not in playbooks_by_id:
            fail(f"{location} references playbook_id '{playbook_id}' that is missing from the registry")

        registry_entry = playbooks_by_id[playbook_id]
        if payload["name"] != registry_entry["name"]:
            fail(f"{location}.name does not match generated/playbook_registry.min.json")

        for key in shared_keys:
            registry_value = registry_entry.get(key)
            payload_value = payload.get(key)
            if payload_value != registry_value:
                fail(f"{location}.{key} does not match generated/playbook_registry.min.json")

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
        playbooks_by_id = validate_registry()
        agent_names = load_agent_names()
        model_tier_artifacts = load_model_tier_artifacts()
        evals_by_name = load_eval_catalog()
        validate_authored_bundles(
            playbooks_by_id,
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
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
    print("[ok] validated generated/playbook_registry.min.json")
    print("[ok] validated authored playbook bundles")
    print("[ok] validated playbook activation examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
