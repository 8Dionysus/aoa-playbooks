#!/usr/bin/env python3
"""Validate the package-local Titan mechanic package."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from scripts.mechanic_package_validator import validate_mechanic_package


REQUIRED_ROOT_PATHS = (
    "mechanics/titan/parts/drill-and-ecology/docs/titan-live-session-drill-route.md",
    "mechanics/titan/parts/drill-and-ecology/docs/titan-route-ecology-playbook.md",
    "mechanics/titan/parts/memory-and-closeout/docs/titan-closeout-playbook.md",
    "mechanics/titan/parts/runtime-bridges/docs/titan-appserver-bridge-playbook.md",
    "mechanics/titan/parts/runtime-bridges/docs/titan-runtime-harness-playbook.md",
    "mechanics/titan/parts/memory-and-closeout/docs/titan-memory-loom-playbook.md",
    "mechanics/titan/parts/runtime-bridges/docs/titan-operator-console-playbook.md",
    "mechanics/titan/parts/runtime-bridges/docs/titan-service-cohort-playbook.md",
    "mechanics/titan/parts/memory-and-closeout/docs/titan-swarm-audit-playbook.md",
)


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    return validate_mechanic_package(
        repo_root=repo_root,
        slug="titan",
        required_paths=REQUIRED_ROOT_PATHS,
        required_text={
            "PARTS.md": ("Payloads moved into package-local parts", "package-local", "drill-and-ecology"),
            "PROVENANCE.md": ("Mechanic payload moved into package-local parts", "package-local", "accepted-input"),
        },
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    issues = validate(args.repo_root)
    if issues:
        print("Titan package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Titan package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
