#!/usr/bin/env python3
"""Validate the package-local questbook mechanic package."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from scripts.mechanic_package_validator import validate_mechanic_package


REQUIRED_ROOT_PATHS = (
    "QUESTBOOK.md",
    "quests",
    "generated/quest_catalog.min.json",
    "generated/quest_dispatch.min.json",
    "mechanics/questbook/parts/questline-outline/docs/questline-and-campaign-model.md",
    "mechanics/questbook/parts/harvest-reanchor/docs/quest-harvest-and-reanchor.md",
    "mechanics/questbook/parts/questline-outline/schemas/questline_outline.schema.json",
    "mechanics/questbook/parts/questline-outline/examples/questline_outline.example.yaml",
)


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    return validate_mechanic_package(
        repo_root=repo_root,
        slug="questbook",
        required_paths=REQUIRED_ROOT_PATHS,
        required_globs=("quests/*.yaml",),
        required_text={
            "PARTS.md": ("Payloads moved into package-local parts", "package-local", "generated-projection"),
            "PROVENANCE.md": ("Mechanic payload moved into package-local parts", "package-local", "accepted-input"),
        },
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    issues = validate(args.repo_root)
    if issues:
        print("Questbook package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Questbook package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
