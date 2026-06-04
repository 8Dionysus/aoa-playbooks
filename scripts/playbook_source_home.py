#!/usr/bin/env python3
"""Helpers for the authored playbook source home."""
from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK_ROOT = REPO_ROOT / "playbooks"
SOURCE_HOME_MANIFEST_PATH = PLAYBOOK_ROOT / "source_home.manifest.json"


def read_source_home_manifest(repo_root: Path = REPO_ROOT) -> dict[str, object]:
    path = repo_root / "playbooks" / "source_home.manifest.json"
    return json.loads(path.read_text(encoding="utf-8"))


def iter_manifest_entries(repo_root: Path = REPO_ROOT) -> list[dict[str, str]]:
    manifest = read_source_home_manifest(repo_root)
    entries: list[dict[str, str]] = []
    branches = manifest.get("branches")
    if not isinstance(branches, list):
        return entries
    for branch in branches:
        if not isinstance(branch, dict) or not isinstance(branch.get("id"), str):
            continue
        branch_id = branch["id"]
        families = branch.get("families")
        if not isinstance(families, list):
            continue
        for family in families:
            if not isinstance(family, dict) or not isinstance(family.get("id"), str):
                continue
            family_id = family["id"]
            playbooks = family.get("playbooks")
            if not isinstance(playbooks, list):
                continue
            for playbook_name in playbooks:
                if not isinstance(playbook_name, str):
                    continue
                entries.append(
                    {
                        "branch": branch_id,
                        "family": family_id,
                        "name": playbook_name,
                        "path": f"playbooks/{branch_id}/{family_id}/{playbook_name}/PLAYBOOK.md",
                    }
                )
    return entries


def manifest_entries_by_name(repo_root: Path = REPO_ROOT) -> dict[str, dict[str, str]]:
    return {entry["name"]: entry for entry in iter_manifest_entries(repo_root)}


def authored_bundle_paths(repo_root: Path = REPO_ROOT) -> list[Path]:
    root = repo_root / "playbooks"
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("PLAYBOOK.md") if path.is_file())


def playbook_path_for_name(playbook_name: str, repo_root: Path = REPO_ROOT) -> Path:
    entry = manifest_entries_by_name(repo_root).get(playbook_name)
    if entry is not None:
        return repo_root / entry["path"]

    matches = [path for path in authored_bundle_paths(repo_root) if path.parent.name == playbook_name]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise KeyError(f"unknown playbook source path: {playbook_name}")
    raise KeyError(f"ambiguous playbook source path: {playbook_name}")


def playbook_ref_for_name(playbook_name: str, repo_root: Path = REPO_ROOT) -> str:
    return playbook_path_for_name(playbook_name, repo_root).relative_to(repo_root).as_posix()


def validate_source_home_manifest(repo_root: Path = REPO_ROOT) -> list[str]:
    repo_root = repo_root.resolve()
    issues: list[str] = []
    manifest_path = repo_root / "playbooks" / "source_home.manifest.json"
    if not manifest_path.is_file():
        return ["playbooks/source_home.manifest.json: missing source-home manifest"]
    try:
        manifest = read_source_home_manifest(repo_root)
    except Exception as exc:
        return [f"playbooks/source_home.manifest.json: invalid JSON: {exc}"]

    if manifest.get("path_template") != "playbooks/<branch>/<family>/<slug>/PLAYBOOK.md":
        issues.append("playbooks/source_home.manifest.json: path_template must name the trunk/family/slug contract")

    entries = iter_manifest_entries(repo_root)
    if not entries:
        issues.append("playbooks/source_home.manifest.json: must list at least one playbook")
        return issues

    names_seen: set[str] = set()
    paths_seen: set[str] = set()
    for entry in entries:
        name = entry["name"]
        path = entry["path"]
        expected_path = f"playbooks/{entry['branch']}/{entry['family']}/{name}/PLAYBOOK.md"
        if path != expected_path:
            issues.append(f"playbooks/source_home.manifest.json: {name} path must be {expected_path}")
        if name in names_seen:
            issues.append(f"playbooks/source_home.manifest.json: duplicate playbook name {name!r}")
        names_seen.add(name)
        if path in paths_seen:
            issues.append(f"playbooks/source_home.manifest.json: duplicate playbook path {path!r}")
        paths_seen.add(path)
        source_path = repo_root / path
        if not source_path.is_file():
            issues.append(f"{path}: manifest source path is missing")

    actual_paths = {
        path.relative_to(repo_root).as_posix()
        for path in authored_bundle_paths(repo_root)
    }
    for path in sorted(actual_paths - paths_seen):
        issues.append(f"{path}: authored playbook is missing from source_home.manifest.json")
    for path in sorted(paths_seen - actual_paths):
        issues.append(f"{path}: source_home.manifest.json path has no authored playbook")

    for path in sorted((repo_root / "playbooks").glob("*/PLAYBOOK.md")):
        issues.append(f"{path.relative_to(repo_root).as_posix()}: flat playbook source path is forbidden")

    return issues
