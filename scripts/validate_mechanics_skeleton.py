#!/usr/bin/env python3
"""Validate the aoa-playbooks mechanics skeleton."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

MECHANICS_ROOT = Path("mechanics")
ALLOWED_ROOT_MARKDOWN = {"README.md", "AGENTS.md"}
FORBIDDEN_ROOT_DIR_NAMES = {"_meta", "legacy", "notes", "scratch", "migration", "migrations"}

REQUIRED_ROOT_FILES: dict[str, tuple[str, ...]] = {
    "mechanics/AGENTS.md": (
        "head-fed",
        "local",
        "Do not add root-level",
        "python scripts/validate_mechanics_skeleton.py",
    ),
    "mechanics/README.md": (
        "Playbook Mechanics",
        "Root Files Rule",
        "Package Directory",
        "Head-Fed Mechanics",
        "Local Mechanics",
        "Placement Rules",
        "Legacy Rules",
        "Package Shape",
        "No source playbook has moved",
    ),
}

ROOT_ENTRYPOINT_REQUIRED_TOKENS: dict[str, tuple[str, ...]] = {
    "AGENTS.md": ("mechanics/README.md", "mechanics/AGENTS.md"),
    "README.md": ("mechanics/README.md", "mechanics/AGENTS.md", "mechanics/*/README.md"),
    "docs/README.md": ("../mechanics/README.md", "../mechanics/activation/README.md", "../mechanics/agon/README.md"),
    "DESIGN.md": ("mechanics/README.md", "mechanics/AGENTS.md", "head-fed", "local"),
    "DESIGN.AGENTS.md": ("mechanics/AGENTS.md", "mechanics/README.md"),
}

PACKAGE_REQUIRED_FILES = ("AGENTS.md", "README.md", "PARTS.md", "PROVENANCE.md")
PACKAGE_README_TOKENS = ("## Mechanic card", "head-fed", "local", "validation")
FORBIDDEN_TOKENS = ("DESGIN.md", "DESGIN.AGENTS.md")
IGNORED_DIR_NAMES = {"__pycache__"}


@dataclass(frozen=True)
class ValidationResult:
    issues: tuple[str, ...]


class ValidationError(RuntimeError):
    pass


def require_tokens(repo_root: Path, relative_path: str, tokens: tuple[str, ...], issues: list[str]) -> str:
    path = repo_root / relative_path
    if not path.is_file():
        issues.append(f"{relative_path}: file is missing")
        return ""
    text = path.read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            issues.append(f"{relative_path}: missing required token {token!r}")
    for forbidden in FORBIDDEN_TOKENS:
        if forbidden in text:
            issues.append(f"{relative_path}: contains forbidden typo token {forbidden!r}")
    return text


def iter_child_package_dirs(repo_root: Path) -> tuple[Path, ...]:
    mechanics_root = repo_root / MECHANICS_ROOT
    if not mechanics_root.is_dir():
        return ()
    packages: list[Path] = []
    for path in mechanics_root.iterdir():
        if not path.is_dir():
            continue
        if path.name in IGNORED_DIR_NAMES:
            continue
        packages.append(path)
    return tuple(sorted(packages))


def validate_child_packages(repo_root: Path, issues: list[str]) -> None:
    for package_dir in iter_child_package_dirs(repo_root):
        rel_dir = package_dir.relative_to(repo_root).as_posix()
        for filename in PACKAGE_REQUIRED_FILES:
            path = package_dir / filename
            if not path.is_file():
                issues.append(f"{rel_dir}: child package missing {filename}")
        readme = package_dir / "README.md"
        if readme.is_file():
            text = readme.read_text(encoding="utf-8")
            for token in PACKAGE_README_TOKENS:
                if token not in text:
                    issues.append(f"{rel_dir}/README.md: missing package card token {token!r}")


def validate(repo_root: Path = REPO_ROOT) -> ValidationResult:
    repo_root = repo_root.resolve()
    issues: list[str] = []

    mechanics_root = repo_root / MECHANICS_ROOT
    if not mechanics_root.is_dir():
        issues.append("mechanics/: directory is missing")
    else:
        for path in sorted(mechanics_root.glob("*.md")):
            if path.name not in ALLOWED_ROOT_MARKDOWN:
                rel = path.relative_to(repo_root).as_posix()
                issues.append(f"{rel}: root mechanics markdown is forbidden")
        for path in sorted(mechanics_root.iterdir()):
            if path.is_dir() and path.name in FORBIDDEN_ROOT_DIR_NAMES:
                rel = path.relative_to(repo_root).as_posix()
                issues.append(f"{rel}/: root mechanics holding directory is forbidden")

    for relative_path, tokens in REQUIRED_ROOT_FILES.items():
        require_tokens(repo_root, relative_path, tokens, issues)

    for relative_path, tokens in ROOT_ENTRYPOINT_REQUIRED_TOKENS.items():
        require_tokens(repo_root, relative_path, tokens, issues)

    if (repo_root / "legacy").exists():
        issues.append("legacy/: root legacy directory is forbidden for mechanics accounting")

    validate_child_packages(repo_root, issues)

    return ValidationResult(tuple(issues))


def validate_mechanics_skeleton(repo_root: Path = REPO_ROOT) -> None:
    result = validate(repo_root)
    if result.issues:
        raise ValidationError("; ".join(result.issues))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)

    result = validate(args.repo_root)
    if result.issues:
        print("Mechanics skeleton validation failed.")
        for issue in result.issues:
            print(f"- {issue}")
        return 1
    print("Mechanics skeleton validation passed for aoa-playbooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
