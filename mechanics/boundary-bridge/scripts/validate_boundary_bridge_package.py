#!/usr/bin/env python3
"""Validate the boundary-bridge mechanic package."""
from __future__ import annotations

import argparse
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "boundary-bridge"

REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "PARTS.md",
    "PROVENANCE.md",
    "legacy/README.md",
    "legacy/INDEX.md",
    "legacy/DISTILLATION_LOG.md",
    "parts/README.md",
    "parts/handoff-drill/README.md",
    "parts/handoff-drill/docs/handoff-drill-runbook.md",
    "parts/handoff-drill/schemas/handoff_drill_runbook_v1.json",
    "parts/handoff-drill/examples/handoff_drill_runbook_v1.example.json",
    "parts/orchestrator-alignment/README.md",
    "parts/orchestrator-alignment/docs/orchestrator-alignment-surfaces.md",
    "scripts/validate_boundary_bridge_package.py",
)

OLD_ROOT_PAYLOADS = (
    "docs/HANDOFF_DRILL_RUNBOOK.md",
    "schemas/handoff_drill_runbook_v1.json",
    "examples/handoff_drill_runbook_v1.example.json",
    "docs/ORCHESTRATOR_ALIGNMENT_SURFACES.md",
)


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    repo_root = repo_root.resolve()
    package_root = repo_root / "mechanics" / "boundary-bridge"
    issues: list[str] = []
    for relative_path in REQUIRED_FILES:
        if not (package_root / relative_path).is_file():
            issues.append(f"mechanics/boundary-bridge/{relative_path}: missing required file")
    readme = package_root / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        for token in ("## Mechanic card", "class | head-fed/local", "| validation |", "| next route |"):
            if token not in text:
                issues.append(f"mechanics/boundary-bridge/README.md: missing token {token!r}")
    for relative_path in OLD_ROOT_PAYLOADS:
        if (repo_root / relative_path).exists():
            issues.append(f"{relative_path}: old boundary-bridge payload should be package-local")
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    issues = validate(args.repo_root)
    if issues:
        print("Boundary-bridge package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Boundary-bridge package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
