#!/usr/bin/env python3
"""Validate the package-local release-support mechanic package."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from scripts.mechanic_package_validator import validate_mechanic_package


REQUIRED_ROOT_PATHS = (
    "docs/RELEASING.md",
    "mechanics/release-support/parts/promotion-and-retention/docs/first-release-runbook.md",
    "mechanics/release-support/parts/promotion-and-retention/docs/release-candidate-promotion.md",
    "mechanics/release-support/parts/deployment-and-installation/docs/deployment-runbook.md",
    "mechanics/release-support/parts/deployment-and-installation/docs/installation-runbook.md",
    "mechanics/release-support/parts/promotion-and-retention/docs/post-release-retention-playbook.md",
    "mechanics/release-support/parts/rollback-and-regression/docs/regression-pack-runbook.md",
    "mechanics/release-support/parts/rollback-and-regression/docs/rollback-drill-runbook.md",
    "mechanics/release-support/parts/rollback-and-regression/docs/rollback-drill-playbook.md",
    "mechanics/release-support/parts/rollback-and-regression/docs/safe-rollback-playbook.md",
    "mechanics/release-support/parts/promotion-and-retention/docs/ring-promotion-playbook.md",
    "mechanics/release-support/parts/promotion-and-retention/docs/retirement-revocation-playbook.md",
    "mechanics/release-support/parts/promotion-and-retention/docs/appeal-review-playbook.md",
    "mechanics/release-support/parts/promotion-and-retention/docs/appeal-expiry-playbook.md",
    "mechanics/release-support/parts/rollback-and-regression/docs/veto-and-stay-order-playbook.md",
    "mechanics/release-support/parts/rollback-and-regression/docs/stay-order-enforcement-playbook.md",
    "scripts/release_check.py",
    "mechanics/release-support/parts/promotion-and-retention/schemas/release_candidate_promotion_plan_v1.json",
    "mechanics/release-support/parts/promotion-and-retention/examples/release_candidate_promotion_plan.example.json",
    "mechanics/release-support/parts/deployment-and-installation/schemas/deployment_runbook_step_v1.json",
    "mechanics/release-support/parts/deployment-and-installation/examples/deployment_runbook_step.example.json",
    "mechanics/release-support/parts/deployment-and-installation/schemas/installation_runbook_record_v1.json",
    "mechanics/release-support/parts/deployment-and-installation/examples/installation_runbook_record_v1.example.json",
    "mechanics/release-support/parts/rollback-and-regression/schemas/regression_pack_manifest_v1.json",
    "mechanics/release-support/parts/rollback-and-regression/examples/regression_pack_manifest.example.json",
    "mechanics/release-support/parts/rollback-and-regression/schemas/rollback_drill_plan_v1.json",
    "mechanics/release-support/parts/rollback-and-regression/examples/rollback_drill_plan.example.json",
    "mechanics/release-support/parts/rollback-and-regression/schemas/rollback_drill_runbook_record_v1.json",
    "mechanics/release-support/parts/rollback-and-regression/examples/rollback_drill_runbook_record_v1.example.json",
    "mechanics/release-support/parts/rollback-and-regression/schemas/rollback_playbook_run_v1.json",
    "mechanics/release-support/parts/rollback-and-regression/examples/rollback_playbook_run.example.json",
    "mechanics/release-support/parts/promotion-and-retention/schemas/retirement_playbook_run_v1.json",
    "mechanics/release-support/parts/promotion-and-retention/examples/retirement_playbook_run.example.json",
    "mechanics/release-support/parts/rollback-and-regression/schemas/veto_playbook_run_v1.json",
    "mechanics/release-support/parts/rollback-and-regression/examples/veto_playbook_run.example.json",
)


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    return validate_mechanic_package(
        repo_root=repo_root,
        slug="release-support",
        required_paths=REQUIRED_ROOT_PATHS,
        allow_compact=True,
        required_text={
            "AGENTS.md": (
                "Do not move `scripts/release_check.py`",
                "Do not claim GitHub/CI authority",
                "Do not move release schemas/examples",
            ),
            "README.md": (
                "Payloads moved into package-local parts",
                "Mechanic payload moved into package-local parts",
                "package-local",
                "repo-release-gate",
                "deployment-and-installation",
                "rollback-and-regression",
                "promotion-and-retention",
                "accepted-input",
            ),
        },
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    issues = validate(args.repo_root)
    if issues:
        print("Release-support package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Release-support package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
