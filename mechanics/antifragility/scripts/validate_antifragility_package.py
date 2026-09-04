#!/usr/bin/env python3
"""Validate the antifragility mechanic package."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from scripts.playbook_source_home import playbook_path_for_name

PACKAGE_ROOT = REPO_ROOT / "mechanics" / "antifragility"

STRESS_LANE_SCHEMA_REL = Path("parts/stress-lanes/schemas/playbook_stress_lane_v1.json")
REENTRY_GATE_SCHEMA_REL = Path("parts/reentry-gates/schemas/playbook_reentry_gate_v1.json")
STRESS_LANE_EXAMPLE_RELS = (
    Path("parts/stress-lanes/examples/playbook_stress_lane.example.json"),
    Path("parts/stress-lanes/examples/playbook_stress_lane.runtime-timeout-chaos.example.json"),
    Path("parts/stress-lanes/examples/playbook_stress_lane.retrieval-outage-honesty.example.json"),
)
REENTRY_GATE_EXAMPLE_RELS = (
    Path("parts/reentry-gates/examples/playbook_reentry_gate.example.json"),
    Path("parts/reentry-gates/examples/playbook_reentry_gate.runtime-timeout-chaos.example.json"),
    Path("parts/reentry-gates/examples/playbook_reentry_gate.retrieval-outage-honesty.example.json"),
)
STRESS_LANE_SCHEMA = PACKAGE_ROOT / STRESS_LANE_SCHEMA_REL
REENTRY_GATE_SCHEMA = PACKAGE_ROOT / REENTRY_GATE_SCHEMA_REL
STRESS_LANE_EXAMPLES = (
    *(PACKAGE_ROOT / relative_path for relative_path in STRESS_LANE_EXAMPLE_RELS),
)
REENTRY_GATE_EXAMPLES = (
    *(PACKAGE_ROOT / relative_path for relative_path in REENTRY_GATE_EXAMPLE_RELS),
)

REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "PARTS.md",
    "PROVENANCE.md",
    "parts/AGENTS.md",
    "parts/README.md",
    "parts/stress-lanes/README.md",
    "parts/reentry-gates/README.md",
    "parts/stress-harvest/README.md",
    "parts/runtime-chaos-wave1/README.md",
    "parts/via-negativa/README.md",
    "parts/stress-lanes/docs/playbook-stress-lanes.md",
    "parts/stress-harvest/docs/playbook-stress-harvest.md",
    "parts/runtime-chaos-wave1/docs/playbook-stress-chaos-wave1.md",
    "parts/via-negativa/docs/via-negativa-checklist.md",
    "parts/stress-lanes/schemas/playbook_stress_lane_v1.json",
    "parts/reentry-gates/schemas/playbook_reentry_gate_v1.json",
    "scripts/validate_antifragility_package.py",
)

REQUIRED_TEXT = {
    "README.md": (
        "## Mechanic card",
        "class | head-fed/local",
        "stress-lane",
        "re-entry",
    ),
    "PARTS.md": (
        "stress-lanes",
        "reentry-gates",
        "runtime-chaos-wave1",
        "via-negativa",
    ),
    "PROVENANCE.md": (
        "mechanics/antifragility/parts/stress-lanes/docs/playbook-stress-lanes.md",
        "mechanics/antifragility/parts/stress-lanes/schemas/playbook_stress_lane_v1.json",
        "examples/playbook_reentry_gate*.json",
        "moved into antifragility package",
    ),
    "legacy/INDEX.md": (
        "Former root path",
        "mechanics/antifragility/parts/stress-lanes/docs/playbook-stress-lanes.md",
        "mechanics/antifragility/parts/reentry-gates/schemas/playbook_reentry_gate_v1.json",
    ),
    "parts/stress-lanes/docs/playbook-stress-lanes.md": (
        "do not let playbooks replace source-owned receipts",
        "do not confuse scenario composition with proof or source meaning",
        "It is a named branch of the same recurring scenario.",
    ),
    "parts/stress-harvest/docs/playbook-stress-harvest.md": (
        "do not let playbook harvest become the only record of what happened",
        "That decision should cite evidence, not mood.",
        "one machine-readable re-entry gate family",
    ),
    "parts/runtime-chaos-wave1/docs/playbook-stress-chaos-wave1.md": (
        "structured degraded lanes and explicit re-entry gates",
        "AOA-P-0032 runtime-chaos-recovery",
        "runtime repair implementation",
    ),
    "parts/via-negativa/docs/via-negativa-checklist.md": (
        "explicit fallback paths and re-entry gates",
        "stress lanes that add no distinct threshold or fallback meaning",
    ),
}

OLD_ROOT_PATHS = (
    "docs/PLAYBOOK_STRESS_LANES.md",
    "docs/PLAYBOOK_STRESS_HARVEST.md",
    "docs/PLAYBOOK_STRESS_CHAOS_WAVE1.md",
    "docs/VIA_NEGATIVA_CHECKLIST.md",
    "schemas/playbook_stress_lane_v1.json",
    "schemas/playbook_reentry_gate_v1.json",
    "examples/playbook_stress_lane.example.json",
    "examples/playbook_stress_lane.runtime-timeout-chaos.example.json",
    "examples/playbook_stress_lane.retrieval-outage-honesty.example.json",
    "examples/playbook_reentry_gate.example.json",
    "examples/playbook_reentry_gate.runtime-timeout-chaos.example.json",
    "examples/playbook_reentry_gate.retrieval-outage-honesty.example.json",
)


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def display_path(path: Path, repo_root: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def validate_examples(repo_root: Path, schema_path: Path, example_paths: tuple[Path, ...], issues: list[str]) -> None:
    try:
        schema = read_json(schema_path)
    except Exception as exc:
        issues.append(f"{display_path(schema_path, repo_root)}: invalid JSON: {exc}")
        return
    if not isinstance(schema, dict):
        issues.append(f"{display_path(schema_path, repo_root)}: must be a JSON object")
        return
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        issues.append(f"{display_path(schema_path, repo_root)}: invalid schema: {exc}")
        return
    validator = Draft202012Validator(schema)
    for example_path in example_paths:
        try:
            payload = read_json(example_path)
        except Exception as exc:
            issues.append(f"{display_path(example_path, repo_root)}: invalid JSON: {exc}")
            continue
        errors = sorted(
            validator.iter_errors(payload),
            key=lambda error: (list(error.absolute_path), error.message),
        )
        if errors:
            first = errors[0]
            location = ".".join(str(part) for part in first.absolute_path)
            if location:
                issues.append(f"{display_path(example_path, repo_root)}: schema error at {location}: {first.message}")
            else:
                issues.append(f"{display_path(example_path, repo_root)}: schema error: {first.message}")
        if isinstance(payload, dict):
            playbook_ref = payload.get("playbook_id")
            if isinstance(playbook_ref, str) and not (repo_root / playbook_ref).is_file():
                issues.append(f"{display_path(example_path, repo_root)}: playbook_id target is missing: {playbook_ref}")


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    repo_root = repo_root.resolve()
    package_root = repo_root / "mechanics" / "antifragility"
    issues: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (package_root / relative_path).is_file():
            issues.append(f"mechanics/antifragility/{relative_path}: missing required file")

    for relative_path, tokens in REQUIRED_TEXT.items():
        path = package_root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                issues.append(f"mechanics/antifragility/{relative_path}: missing token {token!r}")

    for relative_path in OLD_ROOT_PATHS:
        if (repo_root / relative_path).exists():
            issues.append(f"{relative_path}: old root antifragility payload should be package-local")

    if not playbook_path_for_name("runtime-chaos-recovery", repo_root).is_file():
        issues.append("runtime-chaos-recovery: source playbook canon is missing")

    validate_examples(
        repo_root,
        package_root / STRESS_LANE_SCHEMA_REL,
        tuple(package_root / relative_path for relative_path in STRESS_LANE_EXAMPLE_RELS),
        issues,
    )
    validate_examples(
        repo_root,
        package_root / REENTRY_GATE_SCHEMA_REL,
        tuple(package_root / relative_path for relative_path in REENTRY_GATE_EXAMPLE_RELS),
        issues,
    )

    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)

    issues = validate(args.repo_root.resolve())
    if issues:
        print("Antifragility package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Antifragility package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
