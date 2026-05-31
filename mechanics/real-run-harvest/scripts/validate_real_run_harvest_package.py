#!/usr/bin/env python3
"""Validate the real-run-harvest mechanic package."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "real-run-harvest"

REQUIRED_PACKAGE_FILES = (
    "AGENTS.md",
    "README.md",
    "PARTS.md",
    "PROVENANCE.md",
    "scripts/validate_real_run_harvest_package.py",
)

REQUIRED_PACKAGE_TEXT = {
    "README.md": (
        "## Mechanic card",
        "class | local, not head-fed",
        "mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/",
        "mechanics/real-run-harvest/parts/harvest-template-source-store/examples/alpha_harvests/",
    ),
    "PARTS.md": (
        "reviewed-run-source-store",
        "harvest-template-source-store",
        "phase-alpha-evidence-store",
        "Payloads moved into package-local parts",
    ),
    "PROVENANCE.md": (
        "Mechanic payload moved into package-local parts",
        "package-local",
        "accepted-input",
    ),
}

REQUIRED_ROOT_PATHS = (
    "mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/playbook-real-run-workflow.md",
    "mechanics/real-run-harvest/parts/harvest-template-source-store/docs/playbook-real-run-harvest.md",
    "mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs",
    "mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews",
    "mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests",
    "mechanics/real-run-harvest/parts/harvest-template-source-store/examples/alpha_harvests",
    "mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-readiness",
    "mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-reviewed-runs",
    "mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json",
)

LOCAL_REF_PREFIXES = (
    "docs/",
    "examples/",
    "config/",
    "schemas/",
    "generated/",
    "playbooks/",
    "mechanics/",
)


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def is_local_ref(value: object) -> bool:
    return isinstance(value, str) and value.startswith(LOCAL_REF_PREFIXES)


def validate_phase_alpha_refs(repo_root: Path, issues: list[str]) -> None:
    config_path = (
        repo_root
        / "mechanics"
        / "real-run-harvest"
        / "parts"
        / "phase-alpha-evidence-store"
        / "config"
        / "phase_alpha_curated_core.json"
    )
    try:
        payload = read_json(config_path)
    except Exception as exc:
        issues.append(f"mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json: invalid JSON: {exc}")
        return
    if not isinstance(payload, dict):
        issues.append("mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json: must contain an object")
        return

    playbooks = payload.get("playbooks")
    if not isinstance(playbooks, list):
        issues.append("mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json: playbooks must stay a list")
        return

    for index, entry in enumerate(playbooks):
        if not isinstance(entry, dict):
            issues.append(f"mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json: playbooks[{index}] must be an object")
            continue
        for field_name in ("harvest_template_ref", "reviewed_run_ref", "readiness_review_ref"):
            ref = entry.get(field_name)
            if is_local_ref(ref) and not (repo_root / str(ref)).is_file():
                issues.append(f"mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json: missing {field_name} {ref}")
        source_review_refs = entry.get("source_review_refs")
        if isinstance(source_review_refs, list):
            for ref in source_review_refs:
                if is_local_ref(ref) and not (repo_root / str(ref)).is_file():
                    issues.append(f"mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json: missing source_review_ref {ref}")

    final_rerun = payload.get("final_rerun")
    if isinstance(final_rerun, dict):
        run_ref = final_rerun.get("run_ref")
        if is_local_ref(run_ref) and not (repo_root / str(run_ref)).is_file():
            issues.append(f"mechanics/real-run-harvest/parts/phase-alpha-evidence-store/config/phase_alpha_curated_core.json: missing final_rerun run_ref {run_ref}")


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    repo_root = repo_root.resolve()
    issues: list[str] = []
    package_root = repo_root / "mechanics" / "real-run-harvest"

    for relative_path in REQUIRED_PACKAGE_FILES:
        if not (package_root / relative_path).is_file():
            issues.append(f"mechanics/real-run-harvest/{relative_path}: missing required file")

    for relative_path, tokens in REQUIRED_PACKAGE_TEXT.items():
        path = package_root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                issues.append(f"mechanics/real-run-harvest/{relative_path}: missing token {token!r}")

    if (package_root / "legacy").exists():
        issues.append("mechanics/real-run-harvest/legacy/: should not exist without moved legacy payload")

    for relative_path in REQUIRED_ROOT_PATHS:
        path = repo_root / relative_path
        if not path.exists():
            issues.append(f"{relative_path}: missing package-local evidence/source path")

    for relative_path in ("mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/playbook-real-run-workflow.md", "mechanics/real-run-harvest/parts/harvest-template-source-store/docs/playbook-real-run-harvest.md"):
        path = repo_root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in ("mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/", "mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/", "Evidence Links"):
            if token not in text:
                issues.append(f"{relative_path}: missing evidence route token {token!r}")

    for relative_dir, pattern in (
        ("mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs", "*.md"),
        ("mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews", "*.md"),
        ("mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests", "*.md"),
        ("mechanics/real-run-harvest/parts/harvest-template-source-store/examples/alpha_harvests", "*.md"),
        ("mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-readiness", "*.md"),
        ("mechanics/real-run-harvest/parts/phase-alpha-evidence-store/docs/alpha-reviewed-runs", "*.md"),
    ):
        path = repo_root / relative_dir
        if path.is_dir() and not any(path.glob(pattern)):
            issues.append(f"{relative_dir}: must contain at least one {pattern} evidence/template file")

    validate_phase_alpha_refs(repo_root, issues)
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)

    issues = validate(args.repo_root.resolve())
    if issues:
        print("Real-run-harvest package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Real-run-harvest package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
