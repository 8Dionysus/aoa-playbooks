#!/usr/bin/env python3
from __future__ import annotations

import argparse
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


def default_aoa_skills_root() -> Path:
    deps_root = REPO_ROOT / ".deps" / "aoa-skills"
    if deps_root.exists():
        return deps_root.resolve()
    return (REPO_ROOT.parent / "aoa-skills").resolve()


AOA_SKILLS_ROOT = repo_root_from_env("AOA_SKILLS_ROOT", default_aoa_skills_root())
REGISTRY_PATH = REPO_ROOT / "generated" / "playbook_registry.min.json"
PLAYBOOK_ROOT = REPO_ROOT / "playbooks"
COMPOSITION_OVERRIDES_PATH = REPO_ROOT / "config" / "playbook_composition_overrides.json"
SKILL_HANDOFF_PATH = AOA_SKILLS_ROOT / "generated" / "skill_handoff_contracts.json"

PLAYBOOK_HANDOFF_CONTRACTS_PATH = REPO_ROOT / "generated" / "playbook_handoff_contracts.json"
PLAYBOOK_FAILURE_CATALOG_PATH = REPO_ROOT / "generated" / "playbook_failure_catalog.json"
PLAYBOOK_SUBAGENT_RECIPES_PATH = REPO_ROOT / "generated" / "playbook_subagent_recipes.json"
PLAYBOOK_AUTOMATION_SEEDS_PATH = REPO_ROOT / "generated" / "playbook_automation_seeds.json"
PLAYBOOK_COMPOSITION_MANIFEST_PATH = REPO_ROOT / "generated" / "playbook_composition_manifest.json"

GENERATED_OUTPUTS = (
    PLAYBOOK_HANDOFF_CONTRACTS_PATH,
    PLAYBOOK_FAILURE_CATALOG_PATH,
    PLAYBOOK_SUBAGENT_RECIPES_PATH,
    PLAYBOOK_AUTOMATION_SEEDS_PATH,
    PLAYBOOK_COMPOSITION_MANIFEST_PATH,
)


class BuilderError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise BuilderError(message)


def display_path(path: Path) -> str:
    for root in (REPO_ROOT, AOA_SKILLS_ROOT):
        try:
            return path.relative_to(root).as_posix()
        except ValueError:
            continue
    return path.as_posix()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing required file: {display_path(path)}")


def read_json(path: Path) -> object:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {display_path(path)}: {exc}")


def parse_scalar(value: str) -> str:
    scalar = value.strip()
    if len(scalar) >= 2 and scalar[0] in {"'", '"'} and scalar[-1] == scalar[0]:
        return scalar[1:-1]
    return scalar


def parse_frontmatter(text: str, path: Path) -> tuple[dict[str, object], str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        fail(f"{display_path(path)} must start with YAML frontmatter")

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
                fail(f"{display_path(path)} has a list item without a key in frontmatter")
            frontmatter.setdefault(current_key, [])
            assert isinstance(frontmatter[current_key], list)
            frontmatter[current_key].append(parse_scalar(line.split("-", 1)[1]))
            continue
        if ":" not in line:
            fail(f"{display_path(path)} has an invalid frontmatter line: {line}")
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
        fail(f"{display_path(path)} is missing the closing YAML frontmatter boundary")

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


def extract_list_items(section_text: str) -> list[str]:
    items: list[str] = []
    for raw_line in section_text.splitlines():
        line = raw_line.strip()
        if line.startswith("- "):
            items.append(line[2:].strip())
            continue
        if ". " in line:
            prefix, rest = line.split(". ", 1)
            if prefix.isdigit() and rest.strip():
                items.append(rest.strip())
    return items


def load_registry_by_name() -> dict[str, dict[str, object]]:
    payload = read_json(REGISTRY_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("playbooks"), list):
        fail("generated/playbook_registry.min.json must contain a 'playbooks' list")

    registry_by_name: dict[str, dict[str, object]] = {}
    for item in payload["playbooks"]:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if isinstance(name, str):
            registry_by_name[name] = item
    if not registry_by_name:
        fail("generated/playbook_registry.min.json must list at least one playbook")
    return registry_by_name


def authored_bundle_paths() -> list[Path]:
    if not PLAYBOOK_ROOT.exists():
        return []
    return sorted(path for path in PLAYBOOK_ROOT.rglob("PLAYBOOK.md") if path.is_file())


def load_authored_playbooks() -> tuple[dict[str, dict[str, object]], dict[str, dict[str, str]]]:
    frontmatter_by_name: dict[str, dict[str, object]] = {}
    sections_by_name: dict[str, dict[str, str]] = {}

    for bundle_path in authored_bundle_paths():
        frontmatter, body = parse_frontmatter(read_text(bundle_path), bundle_path)
        name = frontmatter.get("name")
        if not isinstance(name, str) or not name:
            fail(f"{display_path(bundle_path)} is missing a non-empty 'name' frontmatter")
        frontmatter_by_name[name] = frontmatter
        sections_by_name[name] = markdown_sections(body)

    return frontmatter_by_name, sections_by_name


def load_skill_handoff_by_name() -> dict[str, dict[str, object]]:
    payload = read_json(SKILL_HANDOFF_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("skills"), list):
        fail("aoa-skills/generated/skill_handoff_contracts.json must contain a 'skills' list")

    skill_handoff_by_name: dict[str, dict[str, object]] = {}
    for item in payload["skills"]:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if isinstance(name, str):
            skill_handoff_by_name[name] = item
    if not skill_handoff_by_name:
        fail("aoa-skills/generated/skill_handoff_contracts.json must list at least one skill")
    return skill_handoff_by_name


def load_composition_overrides() -> dict[str, object]:
    payload = read_json(COMPOSITION_OVERRIDES_PATH)
    if not isinstance(payload, dict):
        fail("config/playbook_composition_overrides.json must be a JSON object")
    if payload.get("schema_version") != 1:
        fail("config/playbook_composition_overrides.json must declare schema_version 1")
    if not isinstance(payload.get("profile"), str) or len(str(payload["profile"])) < 3:
        fail("config/playbook_composition_overrides.json must declare a non-empty profile")
    if not isinstance(payload.get("playbooks"), dict) or not payload["playbooks"]:
        fail("config/playbook_composition_overrides.json must declare a non-empty playbooks map")
    return payload


def skill_ref(skill_name: str) -> str:
    return f"../aoa-skills/generated/skill_handoff_contracts.json#{skill_name}"


def normalize_handles(handles: list[object]) -> list[str]:
    normalized: list[str] = []
    for handle in handles:
        if not isinstance(handle, str) or not handle.startswith("$") or len(handle) < 2:
            fail("automation skill_handles must contain explicit $skill handles")
        normalized.append(handle[1:])
    return normalized


def validate_overrides(
    overrides: dict[str, object],
    *,
    registry_by_name: dict[str, dict[str, object]],
    frontmatter_by_name: dict[str, dict[str, object]],
    skill_handoff_by_name: dict[str, dict[str, object]],
) -> None:
    playbook_overrides = overrides["playbooks"]
    assert isinstance(playbook_overrides, dict)

    failure_catalog = overrides.get("failure_catalog")
    if not isinstance(failure_catalog, list) or not failure_catalog:
        fail("config/playbook_composition_overrides.json must declare a non-empty failure_catalog list")
    failure_codes = {
        item.get("code")
        for item in failure_catalog
        if isinstance(item, dict) and isinstance(item.get("code"), str)
    }
    if len(failure_codes) != len(failure_catalog):
        fail("config/playbook_composition_overrides.json failure_catalog codes must be unique strings")

    subagent_recipes = overrides.get("subagent_recipes")
    if not isinstance(subagent_recipes, list):
        fail("config/playbook_composition_overrides.json must declare subagent_recipes as a list")
    recipe_names = {
        item.get("name")
        for item in subagent_recipes
        if isinstance(item, dict) and isinstance(item.get("name"), str)
    }
    if len(recipe_names) != len(subagent_recipes):
        fail("config/playbook_composition_overrides.json subagent recipe names must be unique strings")

    automation_seeds = overrides.get("automation_seeds")
    if not isinstance(automation_seeds, list):
        fail("config/playbook_composition_overrides.json must declare automation_seeds as a list")
    automation_names = {
        item.get("name")
        for item in automation_seeds
        if isinstance(item, dict) and isinstance(item.get("name"), str)
    }
    if len(automation_names) != len(automation_seeds):
        fail("config/playbook_composition_overrides.json automation seed names must be unique strings")

    for playbook_name, item in playbook_overrides.items():
        if playbook_name not in registry_by_name:
            fail(f"playbook composition override references unknown playbook: {playbook_name}")
        if playbook_name not in frontmatter_by_name:
            fail(f"playbook composition override requires an authored bundle: {playbook_name}")
        if not isinstance(item, dict):
            fail(f"playbook composition override for {playbook_name} must be an object")

        failure_refs = item.get("failure_codes")
        if not isinstance(failure_refs, list) or not failure_refs:
            fail(f"playbook composition override for {playbook_name} must list failure_codes")
        for failure_code in failure_refs:
            if not isinstance(failure_code, str) or failure_code not in failure_codes:
                fail(f"playbook composition override for {playbook_name} references unknown failure code '{failure_code}'")

        followup_playbooks = item.get("followup_playbooks")
        if not isinstance(followup_playbooks, list):
            fail(f"playbook composition override for {playbook_name} must list followup_playbooks")
        for followup_name in followup_playbooks:
            if not isinstance(followup_name, str) or followup_name not in registry_by_name:
                fail(f"playbook composition override for {playbook_name} references unknown followup playbook '{followup_name}'")

        handoff_skill_refs = item.get("handoff_skill_refs")
        if not isinstance(handoff_skill_refs, list) or not handoff_skill_refs:
            fail(f"playbook composition override for {playbook_name} must list handoff_skill_refs")
        required_skills = frontmatter_by_name[playbook_name].get("required_skills")
        if not isinstance(required_skills, list):
            fail(f"authored playbook {playbook_name} must expose required_skills")
        for skill_name in handoff_skill_refs:
            if not isinstance(skill_name, str) or skill_name not in skill_handoff_by_name:
                fail(f"playbook composition override for {playbook_name} references unknown skill handoff '{skill_name}'")
            if skill_name not in required_skills:
                fail(f"playbook composition override for {playbook_name} references handoff skill '{skill_name}' outside required_skills")

        recipe_refs = item.get("subagent_recipes")
        if not isinstance(recipe_refs, list):
            fail(f"playbook composition override for {playbook_name} must list subagent_recipes")
        for recipe_name in recipe_refs:
            if not isinstance(recipe_name, str) or recipe_name not in recipe_names:
                fail(f"playbook composition override for {playbook_name} references unknown subagent recipe '{recipe_name}'")

        automation_refs = item.get("automation_seeds")
        if not isinstance(automation_refs, list):
            fail(f"playbook composition override for {playbook_name} must list automation_seeds")
        for seed_name in automation_refs:
            if not isinstance(seed_name, str) or seed_name not in automation_names:
                fail(f"playbook composition override for {playbook_name} references unknown automation seed '{seed_name}'")

    for recipe in subagent_recipes:
        assert isinstance(recipe, dict)
        playbook_name = recipe.get("playbook")
        if not isinstance(playbook_name, str) or playbook_name not in playbook_overrides:
            fail(f"subagent recipe '{recipe.get('name')}' must point at a managed playbook")
        roles = recipe.get("roles")
        if not isinstance(roles, list) or not roles:
            fail(f"subagent recipe '{recipe.get('name')}' must list roles")
        for role in roles:
            if not isinstance(role, dict):
                fail(f"subagent recipe '{recipe.get('name')}' contains an invalid role entry")
            skills = role.get("skills")
            if not isinstance(skills, list) or not skills:
                fail(f"subagent recipe '{recipe.get('name')}' roles must list skills")
            for skill_name in skills:
                if not isinstance(skill_name, str) or skill_name not in skill_handoff_by_name:
                    fail(f"subagent recipe '{recipe.get('name')}' references unknown skill '{skill_name}'")

    for seed in automation_seeds:
        assert isinstance(seed, dict)
        playbook_name = seed.get("playbook")
        if not isinstance(playbook_name, str) or playbook_name not in playbook_overrides:
            fail(f"automation seed '{seed.get('name')}' must point at a managed playbook")
        skill_handles = seed.get("skill_handles")
        if not isinstance(skill_handles, list) or not skill_handles:
            fail(f"automation seed '{seed.get('name')}' must list skill_handles")
        for skill_name in normalize_handles(skill_handles):
            if skill_name not in skill_handoff_by_name:
                fail(f"automation seed '{seed.get('name')}' references unknown skill handle '${skill_name}'")


def build_playbook_handoff_contracts(
    *,
    overrides: dict[str, object],
    frontmatter_by_name: dict[str, dict[str, object]],
    sections_by_name: dict[str, dict[str, str]],
    skill_handoff_by_name: dict[str, dict[str, object]],
) -> dict[str, object]:
    playbook_entries: list[dict[str, object]] = []
    playbook_overrides = overrides["playbooks"]
    assert isinstance(playbook_overrides, dict)

    for playbook_name in playbook_overrides:
        frontmatter = frontmatter_by_name[playbook_name]
        sections = sections_by_name[playbook_name]
        override = playbook_overrides[playbook_name]
        assert isinstance(override, dict)
        required_skills = frontmatter["required_skills"]
        assert isinstance(required_skills, list)
        expected_artifacts = frontmatter["expected_artifacts"]
        assert isinstance(expected_artifacts, list)
        handoff_skill_refs = override["handoff_skill_refs"]
        assert isinstance(handoff_skill_refs, list)

        upstream_skill_handoffs = []
        for skill_name in handoff_skill_refs:
            assert isinstance(skill_name, str)
            skill_handoff = skill_handoff_by_name[skill_name]
            upstream_skill_handoffs.append(
                {
                    "name": skill_name,
                    "ref": skill_ref(skill_name),
                    "consumes_artifact_tags": skill_handoff.get("consumes_artifact_tags", []),
                    "provides_artifact_tags": skill_handoff.get("provides_artifact_tags", []),
                }
            )

        playbook_entries.append(
            {
                "playbook_id": frontmatter["id"],
                "name": playbook_name,
                "required_skills": required_skills,
                "upstream_skill_handoffs": upstream_skill_handoffs,
                "decision_points": extract_list_items(sections.get("Decision points", "")),
                "handoffs": extract_list_items(sections.get("Handoffs", "")),
                "expected_artifacts": expected_artifacts,
                "return_anchor_artifacts": frontmatter.get("return_anchor_artifacts", []),
                "handoff_packet_template": {
                    "from_playbook": playbook_name,
                    "carried_artifacts": expected_artifacts,
                    "required_skill_handoffs": handoff_skill_refs,
                    "failure_codes": override.get("failure_codes", []),
                    "next_followups": override.get("followup_playbooks", []),
                },
            }
        )

    return {
        "schema_version": 1,
        "layer": "aoa-playbooks",
        "profile": overrides["profile"],
        "source_of_truth": {
            "registry": "generated/playbook_registry.min.json",
            "bundles": "playbooks/*/PLAYBOOK.md",
            "composition_overrides": "config/playbook_composition_overrides.json",
            "skill_handoff_contracts": "../aoa-skills/generated/skill_handoff_contracts.json",
        },
        "playbooks": playbook_entries,
    }


def build_failure_catalog(overrides: dict[str, object]) -> dict[str, object]:
    playbook_overrides = overrides["playbooks"]
    failure_catalog = overrides["failure_catalog"]
    assert isinstance(playbook_overrides, dict)
    assert isinstance(failure_catalog, list)

    used_by: dict[str, list[str]] = {}
    for playbook_name, item in playbook_overrides.items():
        assert isinstance(item, dict)
        for failure_code in item.get("failure_codes", []):
            if isinstance(failure_code, str):
                used_by.setdefault(failure_code, []).append(playbook_name)

    failures: list[dict[str, object]] = []
    for item in failure_catalog:
        assert isinstance(item, dict)
        entry = dict(item)
        entry["used_by_playbooks"] = sorted(used_by.get(str(item["code"]), []))
        failures.append(entry)

    return {
        "schema_version": 1,
        "layer": "aoa-playbooks",
        "profile": overrides["profile"],
        "failures": failures,
    }


def build_subagent_recipes(overrides: dict[str, object]) -> dict[str, object]:
    return {
        "schema_version": 1,
        "layer": "aoa-playbooks",
        "profile": overrides["profile"],
        "recipes": overrides["subagent_recipes"],
    }


def build_automation_seeds(overrides: dict[str, object]) -> dict[str, object]:
    return {
        "schema_version": 1,
        "layer": "aoa-playbooks",
        "profile": overrides["profile"],
        "seeds": overrides["automation_seeds"],
    }


def build_composition_manifest(
    *,
    overrides: dict[str, object],
    registry_by_name: dict[str, dict[str, object]],
) -> dict[str, object]:
    playbook_overrides = overrides["playbooks"]
    assert isinstance(playbook_overrides, dict)
    managed_playbooks = list(playbook_overrides)
    return {
        "schema_version": 1,
        "layer": "aoa-playbooks",
        "profile": overrides["profile"],
        "source_of_truth": {
            "registry": "generated/playbook_registry.min.json",
            "bundles": "playbooks/*/PLAYBOOK.md",
            "composition_overrides": "config/playbook_composition_overrides.json",
            "skill_handoff_contracts": "../aoa-skills/generated/skill_handoff_contracts.json",
        },
        "generated_files": [path.relative_to(REPO_ROOT).as_posix() for path in GENERATED_OUTPUTS],
        "managed_playbooks": managed_playbooks,
        "composition_playbook_count": len(managed_playbooks),
        "total_playbook_count": len(registry_by_name),
    }


def build_outputs() -> dict[Path, object]:
    registry_by_name = load_registry_by_name()
    frontmatter_by_name, sections_by_name = load_authored_playbooks()
    skill_handoff_by_name = load_skill_handoff_by_name()
    overrides = load_composition_overrides()

    validate_overrides(
        overrides,
        registry_by_name=registry_by_name,
        frontmatter_by_name=frontmatter_by_name,
        skill_handoff_by_name=skill_handoff_by_name,
    )

    return {
        PLAYBOOK_HANDOFF_CONTRACTS_PATH: build_playbook_handoff_contracts(
            overrides=overrides,
            frontmatter_by_name=frontmatter_by_name,
            sections_by_name=sections_by_name,
            skill_handoff_by_name=skill_handoff_by_name,
        ),
        PLAYBOOK_FAILURE_CATALOG_PATH: build_failure_catalog(overrides),
        PLAYBOOK_SUBAGENT_RECIPES_PATH: build_subagent_recipes(overrides),
        PLAYBOOK_AUTOMATION_SEEDS_PATH: build_automation_seeds(overrides),
        PLAYBOOK_COMPOSITION_MANIFEST_PATH: build_composition_manifest(
            overrides=overrides,
            registry_by_name=registry_by_name,
        ),
    }


def render_json(payload: object) -> str:
    return json.dumps(payload, indent=2) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate derived playbook composition surfaces.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the generated outputs without writing files.",
    )
    args = parser.parse_args(argv)

    try:
        outputs = build_outputs()
    except BuilderError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    for path, payload in outputs.items():
        rendered = render_json(payload)
        if args.check:
            try:
                existing = path.read_text(encoding="utf-8")
            except FileNotFoundError:
                print(f"[error] missing required file: {display_path(path)}", file=sys.stderr)
                return 1
            if existing != rendered:
                print(
                    f"[error] {display_path(path)} is out of date; "
                    "run scripts/generate_playbook_composition_surfaces.py",
                    file=sys.stderr,
                )
                return 1
        else:
            path.write_text(rendered, encoding="utf-8")

    print("[ok] derived playbook composition surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
