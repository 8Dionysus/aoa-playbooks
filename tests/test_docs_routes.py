from __future__ import annotations

import re
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
EXECUTABLE_MARKDOWN_PREFIXES = (".agents/skills/",)
SHELL_FENCE_PATTERN = re.compile(
    r"^ {0,3}```(?:bash|console|sh|shell|zsh)(?:\s+.*)?$",
    re.IGNORECASE | re.MULTILINE,
)
REPO_COMMAND_LINE_PATTERN = re.compile(
    r"^[ \t]*(?:[-*][ \t]+)?`?(?:"
    r"python3?(?:[ \t]+-m)?[ \t]+|pytest(?=[ \t])|"
    r"uv[ \t]+run[ \t]+pytest\b|pip3?[ \t]+|"
    r"git[ \t]+(?:status|diff|commit|push|fetch|checkout|switch|merge|tag)\b|"
    r"aoa[ \t]+(?:release|compatibility|skills|surfaces|checkpoint|playbooks|workspace)\b|"
    r"ruff[ \t]+(?:check|format)\b|mypy(?=[ \t]))",
    re.MULTILINE,
)
INLINE_REPO_COMMAND_PATTERN = re.compile(
    r"(?<!`)`(?!``)(?:python3?(?:\s+-m)?\s+|pytest(?=\s)|"
    r"uv\s+run\s+pytest\b|pip3?\s+|"
    r"git\s+(?:status|diff|commit|push|fetch|checkout|switch|merge|tag)\b|"
    r"aoa\s+(?:release|compatibility|skills|surfaces|checkpoint|playbooks|workspace)\b|"
    r"ruff\s+(?:check|format)\b|mypy(?=\s))[^`\n]+`(?!`)"
)
FENCE_OPEN_PATTERN = re.compile(r"^ {0,3}```")
COMMAND_BLOCK_LINE_PATTERN = re.compile(
    r"^[ \t]*(?:\$[ \t]+)?(?:python3?|pytest|uv|pip3?|aoa|git|ruff|mypy|"
    r"make|tox|hatch|poetry)(?:[ \t]+(?![=:])\S+)"
)


def tracked_markdown_paths() -> tuple[Path, ...]:
    completed = subprocess.run(
        ("git", "ls-files", "--cached", "--others", "--exclude-standard", "--", "*.md"),
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return tuple(Path(line) for line in completed.stdout.splitlines() if line)


def fenced_command_block_present(content: str) -> bool:
    in_fence = False
    for line in content.splitlines():
        if not in_fence and FENCE_OPEN_PATTERN.match(line):
            in_fence = True
            continue
        if in_fence and line.strip() == "```":
            in_fence = False
            continue
        if in_fence and COMMAND_BLOCK_LINE_PATTERN.match(line):
            return True
    return False


def markdown_command_violations(content: str) -> set[str]:
    violations: set[str] = set()
    if SHELL_FENCE_PATTERN.search(content):
        violations.add("shell command block")
    elif fenced_command_block_present(content):
        violations.add("command block")
    if REPO_COMMAND_LINE_PATTERN.search(content):
        violations.add("repo command line")
    if INLINE_REPO_COMMAND_PATTERN.search(content):
        violations.add("inline repo command")
    return violations


def test_non_owner_markdown_routes_runnable_commands_to_command_owners() -> None:
    offenders: list[str] = []
    for relative_path in tracked_markdown_paths():
        route = relative_path.as_posix()
        if route.startswith(EXECUTABLE_MARKDOWN_PREFIXES):
            continue
        if relative_path.name in {"AGENTS.md", "VALIDATION.md"}:
            continue
        content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        for violation in sorted(markdown_command_violations(content)):
            offenders.append(f"{route}: {violation}")

    assert offenders == []


def test_markdown_command_guard_rejects_scattered_command_forms() -> None:
    content = """# Drift

```bash
python scripts/validate_playbooks.py
```

- `python -m pytest -q`
- git status -sb
"""

    assert markdown_command_violations(content) == {
        "inline repo command",
        "repo command line",
        "shell command block",
    }
    assert markdown_command_violations("```text\naoa recur agents spawn\n```\n") == {
        "command block"
    }
    assert markdown_command_violations("```python\nfrom pathlib import Path\n```\n") == set()
