#!/usr/bin/env python3
"""Validate the scenario-composition mechanic package."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "scenario-composition"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "PARTS.md",
    "PROVENANCE.md",
    "parts/AGENTS.md",
    "parts/README.md",
    "parts/composition-surfaces/README.md",
    "parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py",
    "parts/plan-contours/README.md",
    "parts/plan-contours/config/playbook_plan_contours.json",
    "parts/plan-contours/docs/playbook-plan-contour-contract.md",
    "parts/plan-contours/schemas/playbook-plan-contours.schema.json",
    "parts/plan-contours/scripts/generate_playbook_plan_contours.py",
)

REQUIRED_TEXT = {
    "README.md": (
        "## Mechanic card",
        "class | local",
        "generated/playbook_handoff_contracts.json",
        "generated/playbook_plan_contours.min.json",
    ),
    "PARTS.md": (
        "composition-surfaces",
        "Boundary payloads",
        "mechanics/scenario-composition/parts/composition-surfaces/config/playbook_composition_overrides.json",
        "plan-contours",
    ),
    "PROVENANCE.md": (
        "mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py",
        "accepted-input",
        "implementation moved into scenario-composition package",
        "generated/playbook_plan_contours.min.json",
    ),
    "parts/README.md": (
        "composition-surfaces",
        "plan-contours",
    ),
    "parts/plan-contours/README.md": (
        "aoa_playbook_plan_contour_v1",
        "generated/playbook_plan_contours.min.json",
        "does not",
    ),
}


def load_impl(repo_root: Path = REPO_ROOT):
    impl_path = (
        repo_root
        / "mechanics"
        / "scenario-composition"
        / "parts"
        / "composition-surfaces"
        / "scripts"
        / "generate_playbook_composition_surfaces.py"
    )
    spec = importlib.util.spec_from_file_location("scenario_composition_package_builder", impl_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load scenario-composition package builder from {impl_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_plan_impl(repo_root: Path = REPO_ROOT):
    plan_impl_path = (
        repo_root
        / "mechanics"
        / "scenario-composition"
        / "parts"
        / "plan-contours"
        / "scripts"
        / "generate_playbook_plan_contours.py"
    )
    spec = importlib.util.spec_from_file_location(
        "scenario_composition_plan_contour_builder",
        plan_impl_path,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(
            f"unable to load scenario-composition plan-contour builder from {plan_impl_path}"
        )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    issues: list[str] = []
    repo_root = repo_root.resolve()
    package_root = repo_root / "mechanics" / "scenario-composition"
    root_wrapper_path = repo_root / "scripts" / "generate_playbook_composition_surfaces.py"

    for relative_path in REQUIRED_FILES:
        if not (package_root / relative_path).is_file():
            issues.append(f"mechanics/scenario-composition/{relative_path}: missing required file")

    for relative_path, tokens in REQUIRED_TEXT.items():
        path = package_root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                issues.append(f"mechanics/scenario-composition/{relative_path}: missing token {token!r}")

    if not root_wrapper_path.is_file():
        issues.append("scripts/generate_playbook_composition_surfaces.py: missing compatibility wrapper")
    else:
        wrapper_text = root_wrapper_path.read_text(encoding="utf-8")
        if "mechanics" not in wrapper_text or "composition-surfaces" not in wrapper_text:
            issues.append("scripts/generate_playbook_composition_surfaces.py: wrapper must route to scenario-composition package")

    try:
        builder = load_impl(repo_root)
        outputs = builder.build_outputs()
        for path, payload in outputs.items():
            current = json.loads(path.read_text(encoding="utf-8"))
            if current != payload:
                issues.append(f"{builder.display_path(path)} is out of date")
    except Exception as exc:  # pragma: no cover - reported as validator issue
        issues.append(f"scenario-composition builder validation failed: {exc}")

    try:
        plan_builder = load_plan_impl(repo_root)
        expected = plan_builder.build_output()
        current = json.loads(plan_builder.OUTPUT_PATH.read_text(encoding="utf-8"))
        if current != expected:
            issues.append(f"{plan_builder.display_path(plan_builder.OUTPUT_PATH)} is out of date")
    except Exception as exc:  # pragma: no cover - reported as validator issue
        issues.append(f"scenario-composition plan-contour validation failed: {exc}")

    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)

    issues = validate(args.repo_root.resolve())
    if issues:
        print("Scenario-composition package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Scenario-composition package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
