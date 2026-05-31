#!/usr/bin/env python3
"""Shared checks for mechanics packages."""
from __future__ import annotations

from pathlib import Path


PACKAGE_FILES = (
    "AGENTS.md",
    "README.md",
    "PARTS.md",
    "PROVENANCE.md",
)

PACKAGE_README_TOKENS = (
    "## Mechanic card",
    "head-fed",
    "local",
    "validation",
)


def validate_mechanic_package(
    *,
    repo_root: Path,
    slug: str,
    required_paths: tuple[str, ...],
    required_globs: tuple[str, ...] = (),
    transferred_paths: tuple[str, ...] = (),
    required_text: dict[str, tuple[str, ...]] | None = None,
) -> list[str]:
    repo_root = repo_root.resolve()
    package_root = repo_root / "mechanics" / slug
    issues: list[str] = []

    for relative_path in PACKAGE_FILES:
        if not (package_root / relative_path).is_file():
            issues.append(f"mechanics/{slug}/{relative_path}: missing required file")

    readme = package_root / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        for token in PACKAGE_README_TOKENS:
            if token not in text:
                issues.append(f"mechanics/{slug}/README.md: missing token {token!r}")

    package_text = required_text or {}
    for relative_path, tokens in package_text.items():
        path = package_root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                issues.append(f"mechanics/{slug}/{relative_path}: missing token {token!r}")

    if (package_root / "legacy").exists():
        issues.append(f"mechanics/{slug}/legacy/: should not exist without moved payloads")

    for relative_path in required_paths:
        path = repo_root / relative_path
        if not path.exists():
            issues.append(f"{relative_path}: required package/source path is missing")

    for pattern in required_globs:
        if not tuple(repo_root.glob(pattern)):
            issues.append(f"{pattern}: required package/source glob has no matches")

    for relative_path in transferred_paths:
        if not (repo_root / relative_path).exists():
            issues.append(f"{relative_path}: transferred package path is missing")

    return issues
