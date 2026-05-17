from __future__ import annotations

import os
from pathlib import Path


def repo_root_from_env(env_name: str, default: Path) -> Path:
    override = os.environ.get(env_name)
    if not override:
        return default.resolve()
    return Path(override).expanduser().resolve()


def default_dependency_root(repo_root: Path, repo_name: str) -> Path:
    candidates = [
        repo_root / ".deps" / repo_name,
        repo_root.parent / repo_name,
    ]
    candidates.extend(parent / repo_name for parent in repo_root.parents)

    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()

    return (repo_root.parent / repo_name).resolve()
