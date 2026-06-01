#!/usr/bin/env python3
"""Validate the aoa-playbooks mechanics skeleton."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re


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
PACKAGE_README_TOKENS = ("## Mechanic card", "| class |", "| role |", "| validation |", "| next route |")
ALLOWED_PACKAGE_CLASSES = {"head-fed", "local", "head-fed/local"}
FORBIDDEN_TOKENS = ("DESGIN.md", "DESGIN.AGENTS.md")
IGNORED_DIR_NAMES = {"__pycache__"}
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PACKAGE_CLASS_RE = re.compile(r"^\|\s*class\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)
ROOT_PACKAGE_ROW_RE = re.compile(r"^\|\s*`([^`/]+)/`\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)


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
            package_class = parse_package_class(text)
            if package_class is None:
                issues.append(f"{rel_dir}/README.md: missing package class")
            elif package_class not in ALLOWED_PACKAGE_CLASSES:
                issues.append(
                    f"{rel_dir}/README.md: invalid package class {package_class!r}; "
                    f"expected one of {sorted(ALLOWED_PACKAGE_CLASSES)!r}"
                )


def parse_package_class(text: str) -> str | None:
    match = PACKAGE_CLASS_RE.search(text)
    if match is None:
        return None
    return normalize_package_class(match.group(1))


def normalize_package_class(value: str) -> str:
    return " ".join(value.strip().lower().split())


def parse_root_package_classes(readme_text: str) -> dict[str, str]:
    classes: dict[str, str] = {}
    for package_name, package_class in ROOT_PACKAGE_ROW_RE.findall(readme_text):
        classes[package_name] = normalize_package_class(package_class)
    return classes


def validate_package_class_alignment(repo_root: Path, issues: list[str]) -> None:
    root_readme_path = repo_root / MECHANICS_ROOT / "README.md"
    if not root_readme_path.is_file():
        return
    root_classes = parse_root_package_classes(root_readme_path.read_text(encoding="utf-8"))
    if not root_classes:
        return

    package_dirs = iter_child_package_dirs(repo_root)
    package_names = {path.name for path in package_dirs}
    for package_dir in package_dirs:
        rel_dir = package_dir.relative_to(repo_root).as_posix()
        root_class = root_classes.get(package_dir.name)
        if root_class is None:
            issues.append(f"{rel_dir}: missing package row in mechanics/README.md")
            continue
        readme = package_dir / "README.md"
        if not readme.is_file():
            continue
        package_class = parse_package_class(readme.read_text(encoding="utf-8"))
        if package_class is not None and root_class != package_class:
            issues.append(
                f"{rel_dir}/README.md: package class {package_class!r} does not match "
                f"mechanics/README.md class {root_class!r}"
            )

    for package_name in sorted(root_classes):
        if package_name not in package_names:
            issues.append(f"mechanics/README.md: package row {package_name!r} has no child package")


def validate_mechanics_markdown_links(repo_root: Path, issues: list[str]) -> None:
    mechanics_root = repo_root / MECHANICS_ROOT
    if not mechanics_root.is_dir():
        return

    for markdown_path in sorted(mechanics_root.rglob("*.md")):
        text = markdown_path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip()
            if not target:
                continue
            if target.startswith(("#", "repo:", "mailto:")) or "://" in target:
                continue
            target_path = target.split("#", 1)[0].strip()
            if not target_path:
                continue
            resolved = (markdown_path.parent / target_path).resolve()
            try:
                resolved.relative_to(repo_root)
            except ValueError:
                continue
            if not resolved.exists():
                rel = markdown_path.relative_to(repo_root).as_posix()
                issues.append(f"{rel}: markdown link target is missing: {target!r}")


def validate_release_check_covers_package_validators(repo_root: Path, issues: list[str]) -> None:
    release_check = repo_root / "scripts" / "release_check.py"
    if not release_check.is_file():
        return
    release_text = release_check.read_text(encoding="utf-8")

    for package_dir in iter_child_package_dirs(repo_root):
        for validator_path in sorted((package_dir / "scripts").glob("validate_*_package.py")):
            rel = validator_path.relative_to(repo_root).as_posix()
            if rel not in release_text:
                issues.append(f"scripts/release_check.py: missing package validator {rel}")


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
    validate_package_class_alignment(repo_root, issues)
    validate_mechanics_markdown_links(repo_root, issues)
    validate_release_check_covers_package_validators(repo_root, issues)

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
