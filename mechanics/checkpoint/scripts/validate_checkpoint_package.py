#!/usr/bin/env python3
"""Validate the package-local checkpoint mechanic package."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from scripts.mechanic_package_validator import validate_mechanic_package


REQUIRED_ROOT_PATHS = (
    "mechanics/checkpoint/parts/distillation-closed-loop/docs/checkpoint-distillation-closed-loop-pilot.md",
    "playbooks/continuity/checkpoint/a2a-summon-return-checkpoint/PLAYBOOK.md",
    "playbooks/continuity/checkpoint/checkpoint-closeout-owner-route/PLAYBOOK.md",
    "playbooks/continuity/checkpoint/checkpoint-distillation-closed-loop-pilot/PLAYBOOK.md",
    "mechanics/activation/parts/activation-surface/examples/playbook_activation.checkpoint-distillation-closed-loop-pilot.example.json",
)


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    return validate_mechanic_package(
        repo_root=repo_root,
        slug="checkpoint",
        required_paths=REQUIRED_ROOT_PATHS,
        required_text={
            "PARTS.md": ("Payloads moved into package-local parts", "stronger-owner", "source-playbook"),
            "PROVENANCE.md": ("Mechanic payload moved into package-local parts", "package-local", "accepted-input"),
        },
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    issues = validate(args.repo_root)
    if issues:
        print("Checkpoint package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Checkpoint package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
