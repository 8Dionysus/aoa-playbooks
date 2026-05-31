#!/usr/bin/env python3
"""Validate the package-local portfolio-governance mechanic package."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from scripts.mechanic_package_validator import validate_mechanic_package


REQUIRED_ROOT_PATHS = (
    "mechanics/portfolio-governance/parts/model-spine/docs/playbook-model.md",
    "mechanics/portfolio-governance/parts/operational-family/docs/playbook-operational-family.md",
    "mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-lifecycle.md",
    "mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-portfolio.md",
    "mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-gap-matrix.md",
)


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    return validate_mechanic_package(
        repo_root=repo_root,
        slug="portfolio-governance",
        required_paths=REQUIRED_ROOT_PATHS,
        required_text={
            "PARTS.md": ("Payloads moved into package-local parts", "package-local", "model-spine"),
            "PROVENANCE.md": ("Mechanic payload moved into package-local parts", "package-local", "accepted-input"),
        },
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    issues = validate(args.repo_root)
    if issues:
        print("Portfolio-governance package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Portfolio-governance package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
