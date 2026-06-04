#!/usr/bin/env python3
"""Validate the package-local recurrence mechanic package."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from scripts.mechanic_package_validator import validate_mechanic_package


REQUIRED_ROOT_PATHS = (
    "mechanics/recurrence/parts/recurrence-discipline/docs/playbook-recurrence-discipline.md",
    "mechanics/recurrence/parts/observation-producers/docs/recurrence-live-observation-producers.md",
    "mechanics/recurrence/parts/review-decision-closure/docs/recurrence-review-decision-closure.md",
    "playbooks/continuity/session-growth/self-agency-continuity-cycle/PLAYBOOK.md",
    "playbooks/continuity/session-growth/component-refresh-cycle/PLAYBOOK.md",
    "mechanics/agon/parts/recurrence-adapter/manifests/component.agon.trial-playbook-surfaces.json",
    "mechanics/scenario-composition/parts/composition-surfaces/manifests/component.playbooks.scenario-composition-beacons.json",
)


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    return validate_mechanic_package(
        repo_root=repo_root,
        slug="recurrence",
        required_paths=REQUIRED_ROOT_PATHS,
        required_globs=(
            "mechanics/agon/parts/*/manifests/*.json",
            "mechanics/scenario-composition/parts/*/manifests/*.json",
        ),
        required_text={
            "PARTS.md": ("Payloads moved into package-local parts", "package-local", "source-playbook"),
            "PROVENANCE.md": ("Mechanic payload moved into package-local parts", "package-local", "accepted-input"),
        },
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    issues = validate(args.repo_root)
    if issues:
        print("Recurrence package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Recurrence package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
