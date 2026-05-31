#!/usr/bin/env python3
"""Validate root design spine surfaces for aoa-playbooks."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

DESIGN_REQUIRED_TOKENS = (
    "scenario and composition layer",
    "source-authored playbook canon",
    "Generated readers",
    "A playbook coordinates neighboring layers",
    "mechanics/",
    "docs/decisions/",
    "This file does not override local owner truth",
)

DESIGN_AGENTS_REQUIRED_TOKENS = (
    "agent-facing guidance",
    "route mesh",
    "Root card",
    "District cards",
    "Future mechanic cards",
    "Operational Map Shape",
    "| role |",
    "nearest nested `AGENTS.md`",
    "closeout",
)

ROOT_ENTRYPOINT_REQUIRED_TOKENS: dict[str, tuple[str, ...]] = {
    "AGENTS.md": ("DESIGN.md", "DESIGN.AGENTS.md"),
    "README.md": ("DESIGN.md", "DESIGN.AGENTS.md"),
    "docs/README.md": ("DESIGN.md", "DESIGN.AGENTS.md"),
    "ROADMAP.md": ("DESIGN.md", "DESIGN.AGENTS.md"),
}

FORBIDDEN_ROOT_TOKENS = ("DESGIN.md", "DESGIN.AGENTS.md")


@dataclass(frozen=True)
class ValidationResult:
    issues: tuple[str, ...]


class ValidationError(RuntimeError):
    pass


def require_file_tokens(
    repo_root: Path,
    relative_path: str,
    tokens: tuple[str, ...],
    issues: list[str],
) -> str:
    path = repo_root / relative_path
    if not path.is_file():
        issues.append(f"{relative_path}: file is missing")
        return ""
    text = path.read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            issues.append(f"{relative_path}: missing required token {token!r}")
    for forbidden in FORBIDDEN_ROOT_TOKENS:
        if forbidden in text:
            issues.append(f"{relative_path}: contains forbidden typo token {forbidden!r}")
    return text


def validate(repo_root: Path = REPO_ROOT) -> ValidationResult:
    repo_root = repo_root.resolve()
    issues: list[str] = []

    require_file_tokens(repo_root, "DESIGN.md", DESIGN_REQUIRED_TOKENS, issues)
    require_file_tokens(
        repo_root,
        "DESIGN.AGENTS.md",
        DESIGN_AGENTS_REQUIRED_TOKENS,
        issues,
    )
    for relative_path, tokens in ROOT_ENTRYPOINT_REQUIRED_TOKENS.items():
        require_file_tokens(repo_root, relative_path, tokens, issues)

    return ValidationResult(tuple(issues))


def validate_root_design_surfaces(repo_root: Path = REPO_ROOT) -> None:
    result = validate(repo_root)
    if result.issues:
        raise ValidationError("; ".join(result.issues))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)

    result = validate(args.repo_root)
    if result.issues:
        print("Root design validation failed.")
        for issue in result.issues:
            print(f"- {issue}")
        return 1
    print("Root design validation passed for aoa-playbooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
