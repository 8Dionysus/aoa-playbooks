#!/usr/bin/env python3
"""Validate the package-local RPG mechanic package."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from scripts.mechanic_package_validator import validate_mechanic_package


REQUIRED_ROOT_PATHS = (
    "mechanics/rpg/parts/party-template-model/docs/party-template-model.md",
    "mechanics/rpg/parts/build-synergy-posture/docs/build-synergy-posture.md",
    "mechanics/rpg/parts/party-template-readout/schemas/party_template_catalog.schema.json",
    "generated/party_template_cards.min.example.json",
)


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    return validate_mechanic_package(
        repo_root=repo_root,
        slug="rpg",
        required_paths=REQUIRED_ROOT_PATHS,
        required_text={
            "PARTS.md": ("Payloads moved into package-local parts", "package-local", "party-template"),
            "PROVENANCE.md": ("Mechanic payload moved into package-local parts", "package-local", "accepted-input"),
        },
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    issues = validate(args.repo_root)
    if issues:
        print("RPG package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("RPG package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
