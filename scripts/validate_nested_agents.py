#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_NESTED_AGENTS = {
    REPO_ROOT / "playbooks" / "AGENTS.md": {
        "min_lines": 20,
        "required_tokens": (
            "playbooks/*/PLAYBOOK.md",
            "docs/PLAYBOOK_BUNDLE_CONTRACT.md",
            "generated/playbook_registry.min.json",
            "scripts/validate_playbooks.py",
            "A playbook is not a skill",
        ),
    },
    REPO_ROOT / "generated" / "AGENTS.md": {
        "min_lines": 20,
        "required_tokens": (
            "playbook_registry.min.json",
            "playbook_activation_surfaces.min.json",
            "playbook_federation_surfaces.min.json",
            "scripts/generate_playbook_activation_surfaces.py",
            "scripts/generate_playbook_federation_surfaces.py",
            "source-authored",
            "Do not hand-edit",
        ),
    },
}


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def display_path(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing required nested AGENTS doc: {display_path(path)}")


def validate_nested_agents_docs() -> None:
    for path, contract in REQUIRED_NESTED_AGENTS.items():
        text = read_text(path)
        stripped = text.strip()
        if not stripped.startswith("# AGENTS.md"):
            fail(f"{display_path(path)} must start with a '# AGENTS.md' heading")

        lines = stripped.splitlines()
        min_lines = int(contract["min_lines"])
        if len(lines) < min_lines:
            fail(f"{display_path(path)} must contain at least {min_lines} lines of guidance")

        for token in contract["required_tokens"]:
            if token not in text:
                fail(f"{display_path(path)} must mention '{token}' explicitly")


def main() -> int:
    try:
        validate_nested_agents_docs()
    except ValidationError as exc:
        print(f"[error] {exc}")
        return 1

    print("[ok] validated nested AGENTS docs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
