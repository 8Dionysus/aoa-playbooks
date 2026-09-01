#!/usr/bin/env python3
"""Validate nested AGENTS.md guidance for aoa-playbooks."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_NAME = "aoa-playbooks"

REQUIRED_AGENTS_DOCS: dict[str, tuple[str, ...]] = {
    ".github/AGENTS.md": ("GitHub platform surface", "Repo Validation"),
    "Spark/AGENTS.md": ("fast-loop lane", "Local done signal"),
    "playbooks/AGENTS.md": ("playbooks/<branch>/<family>/<slug>/PLAYBOOK.md", "A playbook is not a skill"),
    "generated/AGENTS.md": ("playbook_registry.min.json", "mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py"),
    "config/AGENTS.md": ("playbook_composition_overrides.json", "source-owned composition overrides"),
    "examples/AGENTS.md": ("Examples must demonstrate contracts without becoming canon", "activation posture"),
    "schemas/AGENTS.md": ("Schema changes are contract changes", "playbook-owned adjuncts"),
    "scripts/AGENTS.md": ("generate_* --check", "repo-relative"),
    "tests/AGENTS.md": ("scenario boundaries", "generated alignment"),
    "memo/AGENTS.md": ("local memory port", "reviewed landing"),
    "stats/AGENTS.md": ("playbook-local statistical questions", "aoa-stats"),
    "docs/decisions/AGENTS.md": ("Decision ID: AOA-PB-D-####", "generated lookup read models"),
    "evals/AGENTS.md": ("skeleton port", "aoa-evals"),
    "kag/AGENTS.md": ("local KAG provider home", "kag/manifest.json"),
    "mechanics/AGENTS.md": ("head-fed", "local", "Do not add root-level"),
}
ADVISORY_AGENT_DIRS: tuple[str, ...] = ("Spark", "docs", "manifests/recurrence", "quests")
HEADING_PREFIXES = ("# AGENTS.md", "# AGENTS")
IGNORED_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache", ".mypy_cache"}
MARKDOWN_HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")
MANDATORY_READ_SECTION_RE = re.compile(
    r"\b(read\s+before(?:\s+editing|\s+changing)?|reading\s+order|"
    r"read\s+first|required\s+reading|start\s+here)\b",
    re.IGNORECASE,
)
MANDATORY_README_LINE_RE = re.compile(
    r"(?:\b(?:read|must|required|before)\b.*\bREADME\.md\b|"
    r"\bREADME\.md\b.*\b(?:before|required|must)\b)",
    re.IGNORECASE,
)
NEGATED_READ_RE = re.compile(
    r"\b(do\s+not|don't|not\s+required|optional)\b",
    re.IGNORECASE,
)
README_TASK_CONDITION_RE = re.compile(
    r"(?:\b(?:when|if|where)\b|"
    r"\bonly\s+(?:when|if|for)\b|"
    r"\b(?:as|when|if)\s+needed\b|"
    r"\bfor\s+(?!(?:all|any|every|each|editing|work|tasks?)\b)|"
    r"\b(?:relevant|selected|target|named)\s+(?:[^\n]*\s)?README\.md\b)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ValidationResult:
    issues: tuple[str, ...]
    warnings: tuple[str, ...]


class ValidationError(RuntimeError):
    pass


def _normalize(text: str) -> str:
    return " ".join(text.lower().split())


def _has_agents_heading(text: str) -> bool:
    stripped = text.lstrip()
    return any(stripped.startswith(prefix) for prefix in HEADING_PREFIXES)


def _mandatory_readme_lines(text: str) -> tuple[int, ...]:
    lines: list[int] = []
    mandatory_section_level: int | None = None
    for line_number, line in enumerate(text.splitlines(), start=1):
        heading = MARKDOWN_HEADING_RE.match(line.strip())
        if heading:
            level = len(heading.group("marks"))
            if mandatory_section_level is not None and level <= mandatory_section_level:
                mandatory_section_level = None
            if MANDATORY_READ_SECTION_RE.search(heading.group("title")):
                mandatory_section_level = level
        if "README.md" not in line or NEGATED_READ_RE.search(line):
            continue
        if README_TASK_CONDITION_RE.search(line):
            continue
        if mandatory_section_level is not None or MANDATORY_README_LINE_RE.search(line):
            lines.append(line_number)
    return tuple(lines)


def _relative(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError:
        return path.as_posix()


def _is_ignored(path: Path, repo_root: Path) -> bool:
    try:
        parts = path.relative_to(repo_root).parts
    except ValueError:
        return False
    return any(part in IGNORED_DIRS for part in parts)


def discover_nested_agents(repo_root: Path) -> set[str]:
    found: set[str] = set()
    for path in repo_root.rglob("AGENTS.md"):
        if _is_ignored(path, repo_root):
            continue
        rel = _relative(path, repo_root)
        if rel != "AGENTS.md":
            found.add(rel)
    return found


def discover_mechanics_agents(repo_root: Path) -> set[str]:
    mechanics_root = repo_root / "mechanics"
    if not mechanics_root.is_dir():
        return set()
    found: set[str] = set()
    for path in mechanics_root.glob("*/AGENTS.md"):
        found.add(_relative(path, repo_root))
    for path in mechanics_root.glob("*/parts/AGENTS.md"):
        found.add(_relative(path, repo_root))
    return found


def validate(
    repo_root: Path = REPO_ROOT,
    *,
    strict_advisory: bool = False,
    fail_on_untracked: bool = False,
) -> ValidationResult:
    repo_root = repo_root.resolve()
    issues: list[str] = []
    warnings: list[str] = []

    root_agents = repo_root / "AGENTS.md"
    if not root_agents.is_file():
        issues.append("AGENTS.md: root guidance file is missing")
    else:
        root_text = root_agents.read_text(encoding="utf-8")
        if not _has_agents_heading(root_text):
            issues.append("AGENTS.md: missing AGENTS heading")
        mandatory_lines = _mandatory_readme_lines(root_text)
        if mandatory_lines:
            issues.append(
                "AGENTS.md: README.md must stay task-conditioned; "
                f"mandatory line(s): {', '.join(map(str, mandatory_lines))}"
            )

    for rel_path, snippets in REQUIRED_AGENTS_DOCS.items():
        path = repo_root / rel_path
        if not path.is_file():
            issues.append(f"{rel_path}: required nested AGENTS.md is missing")
            continue
        text = path.read_text(encoding="utf-8")
        if not _has_agents_heading(text):
            issues.append(f"{rel_path}: missing AGENTS heading")
        mandatory_lines = _mandatory_readme_lines(text)
        if mandatory_lines:
            issues.append(
                f"{rel_path}: README.md must stay task-conditioned; "
                f"mandatory line(s): {', '.join(map(str, mandatory_lines))}"
            )
        normalized = _normalize(text)
        for snippet in snippets:
            if _normalize(snippet) not in normalized:
                issues.append(f"{rel_path}: missing required snippet {snippet!r}")

    dynamic_mechanics_agents = discover_mechanics_agents(repo_root)
    for rel_path in sorted(dynamic_mechanics_agents):
        path = repo_root / rel_path
        text = path.read_text(encoding="utf-8")
        if not _has_agents_heading(text):
            issues.append(f"{rel_path}: missing AGENTS heading")
        mandatory_lines = _mandatory_readme_lines(text)
        if mandatory_lines:
            issues.append(
                f"{rel_path}: README.md must stay task-conditioned; "
                f"mandatory line(s): {', '.join(map(str, mandatory_lines))}"
            )
        if "Validation" not in text:
            issues.append(f"{rel_path}: missing Validation section")

    required = set(REQUIRED_AGENTS_DOCS)
    required.update(dynamic_mechanics_agents)
    actual = discover_nested_agents(repo_root)
    untracked = sorted(actual - required)
    if untracked:
        message = "untracked nested AGENTS.md not yet in validator map: " + ", ".join(untracked)
        warnings.append(message)
        if fail_on_untracked:
            issues.append(message)

    for rel_dir in ADVISORY_AGENT_DIRS:
        dir_path = repo_root / rel_dir
        agent_path = f"{rel_dir.rstrip('/')}/AGENTS.md"
        if not dir_path.is_dir():
            continue
        if agent_path in required or agent_path in actual:
            continue
        warnings.append(f"{rel_dir}: high-risk directory has no local AGENTS.md yet")

    if strict_advisory:
        issues.extend(warnings)

    return ValidationResult(tuple(issues), tuple(warnings))


def validate_nested_agents_docs(repo_root: Path = REPO_ROOT) -> None:
    """Compatibility entrypoint used by scripts/validate_playbooks.py."""
    result = validate(repo_root)
    if result.issues:
        raise ValidationError("; ".join(result.issues))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--strict-advisory", action="store_true")
    parser.add_argument("--fail-on-untracked", action="store_true")
    args = parser.parse_args(argv)

    result = validate(
        args.repo_root,
        strict_advisory=args.strict_advisory,
        fail_on_untracked=args.fail_on_untracked,
    )
    if result.issues:
        print(f"Nested AGENTS validation failed for {REPOSITORY_NAME}.")
        for issue in result.issues:
            print(f"- {issue}")
        return 1
    print(
        f"Nested AGENTS validation passed for {REPOSITORY_NAME}: "
        f"{len(REQUIRED_AGENTS_DOCS)} required nested document(s)."
    )
    for warning in result.warnings:
        print(f"[advisory] {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
