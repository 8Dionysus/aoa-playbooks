#!/usr/bin/env python3
"""Validate the package-local Experience mechanic package."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from scripts.mechanic_package_validator import validate_mechanic_package


REQUIRED_ROOT_PATHS = (
    "mechanics/experience/parts/adoption-and-retention/docs/adoption-runbook.md",
    "mechanics/experience/parts/adoption-and-retention/docs/adoption-retention-playbook.md",
    "mechanics/experience/parts/adoption-and-retention/docs/adoption-rollback-playbook.md",
    "mechanics/experience/parts/certification-and-governance/docs/assistant-adoption-certification-playbook.md",
    "mechanics/experience/parts/certification-and-governance/docs/experience-certification-runbook.md",
    "mechanics/experience/parts/certification-and-governance/docs/federation-harvest-runbook.md",
    "mechanics/experience/parts/certification-and-governance/docs/kag-promotion-dossier-runbook.md",
    "mechanics/experience/parts/certification-and-governance/docs/owner-adoption-quest-playbook.md",
    "mechanics/experience/parts/certification-and-governance/docs/pattern-merge-split-playbook.md",
    "mechanics/experience/parts/adoption-and-retention/docs/playbook-pattern-adoption.md",
    "mechanics/experience/parts/adoption-and-retention/docs/shadow-adoption-playbook.md",
    "mechanics/experience/parts/adoption-and-retention/docs/shared-pattern-review-playbook.md",
    "mechanics/experience/parts/certification-and-governance/docs/governance-council-runbook.md",
    "mechanics/experience/parts/service-and-office/docs/service-mesh-incident-response.md",
    "mechanics/experience/parts/service-and-office/docs/watchtower-incident-response.md",
    "mechanics/experience/parts/service-and-office/docs/office-bootstrap-runbook.md",
    "mechanics/experience/parts/service-and-office/docs/operator-console-runbook.md",
    "mechanics/experience/parts/adoption-and-retention/schemas/adoption_playbook_run_v1.json",
    "mechanics/experience/parts/adoption-and-retention/examples/adoption_playbook_run.example.json",
    "mechanics/experience/parts/adoption-and-retention/schemas/adoption_retention_playbook_run_v1.json",
    "mechanics/experience/parts/adoption-and-retention/examples/adoption_retention_playbook_run.example.json",
    "mechanics/experience/parts/adoption-and-retention/schemas/adoption_rollback_playbook_run_v1.json",
    "mechanics/experience/parts/adoption-and-retention/examples/adoption_rollback_playbook_run.example.json",
    "mechanics/experience/parts/certification-and-governance/schemas/assistant_adoption_certification_run_v1.json",
    "mechanics/experience/parts/certification-and-governance/examples/assistant_adoption_certification_run.example.json",
    "mechanics/experience/parts/certification-and-governance/schemas/federation_harvest_run_v1.json",
    "mechanics/experience/parts/certification-and-governance/examples/federation_harvest_run.example.json",
    "mechanics/experience/parts/certification-and-governance/schemas/kag_dossier_run_v1.json",
    "mechanics/experience/parts/certification-and-governance/examples/kag_dossier_run.example.json",
    "mechanics/experience/parts/certification-and-governance/schemas/owner_adoption_quest_run_v1.json",
    "mechanics/experience/parts/certification-and-governance/examples/owner_adoption_quest_run.example.json",
    "mechanics/experience/parts/certification-and-governance/schemas/pattern_merge_split_run_v1.json",
    "mechanics/experience/parts/certification-and-governance/examples/pattern_merge_split_run.example.json",
    "mechanics/experience/parts/adoption-and-retention/schemas/playbook_pattern_adoption_patch_v1.json",
    "mechanics/experience/parts/adoption-and-retention/examples/playbook_pattern_adoption_patch.example.json",
    "mechanics/experience/parts/adoption-and-retention/schemas/shadow_adoption_playbook_run_v1.json",
    "mechanics/experience/parts/adoption-and-retention/examples/shadow_adoption_playbook_run.example.json",
    "mechanics/experience/parts/adoption-and-retention/schemas/shared_pattern_review_run_v1.json",
    "mechanics/experience/parts/adoption-and-retention/examples/shared_pattern_review_run.example.json",
    "mechanics/experience/parts/certification-and-governance/schemas/tos_dossier_review_run_v1.json",
    "mechanics/experience/parts/certification-and-governance/examples/tos_dossier_review_run.example.json",
)

TRANSFERRED_PATHS = (
    "mechanics/agon/parts/adoption/schemas/agonic_trial_adoption_run_v1.json",
    "mechanics/agon/parts/adoption/examples/agonic_trial_adoption_run.example.json",
)


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    return validate_mechanic_package(
        repo_root=repo_root,
        slug="experience",
        required_paths=REQUIRED_ROOT_PATHS,
        transferred_paths=TRANSFERRED_PATHS,
        required_text={
            "PARTS.md": ("Payloads moved into package-local parts", "package-local", "transferred-to-agon"),
            "PROVENANCE.md": ("Mechanic payload moved into package-local parts", "package-local", "accepted-input"),
        },
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    issues = validate(args.repo_root)
    if issues:
        print("Experience package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Experience package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
