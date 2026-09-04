#!/usr/bin/env python3
"""Validate the federation-closure mechanic package."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "federation-closure"
IMPL_PATH = (
    PACKAGE_ROOT
    / "parts"
    / "federation-surfaces"
    / "scripts"
    / "generate_playbook_federation_surfaces.py"
)
ROOT_WRAPPER_PATH = REPO_ROOT / "scripts" / "generate_playbook_federation_surfaces.py"
OUTPUT_PATH = REPO_ROOT / "generated" / "playbook_federation_surfaces.min.json"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "PARTS.md",
    "PROVENANCE.md",
    "parts/AGENTS.md",
    "parts/README.md",
    "parts/federation-surfaces/README.md",
    "parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py",
)

REQUIRED_TEXT = {
    "README.md": (
        "## Mechanic card",
        "class | local",
        "generated/playbook_federation_surfaces.min.json",
    ),
    "PARTS.md": (
        "federation-surfaces",
        "Boundary payloads",
        "mechanics/federation-closure/parts/federation-surfaces/schemas/playbook-federation-surface.schema.json",
    ),
    "PROVENANCE.md": (
        "mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py",
        "accepted-input",
        "implementation moved into federation-closure package",
    ),
    "legacy/INDEX.md": (
        "Former root path",
        "mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py",
    ),
}


def load_impl():
    spec = importlib.util.spec_from_file_location("federation_closure_package_builder", IMPL_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load federation-closure package builder from {IMPL_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    issues: list[str] = []
    package_root = repo_root / "mechanics" / "federation-closure"

    for relative_path in REQUIRED_FILES:
        if not (package_root / relative_path).is_file():
            issues.append(f"mechanics/federation-closure/{relative_path}: missing required file")

    for relative_path, tokens in REQUIRED_TEXT.items():
        path = package_root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                issues.append(f"mechanics/federation-closure/{relative_path}: missing token {token!r}")

    if not ROOT_WRAPPER_PATH.is_file():
        issues.append("scripts/generate_playbook_federation_surfaces.py: missing compatibility wrapper")
    else:
        wrapper_text = ROOT_WRAPPER_PATH.read_text(encoding="utf-8")
        if "mechanics" not in wrapper_text or "federation-surfaces" not in wrapper_text:
            issues.append("scripts/generate_playbook_federation_surfaces.py: wrapper must route to federation-closure package")

    try:
        builder = load_impl()
        expected = builder.build_federation_surfaces()
        current = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        if current != expected:
            issues.append("generated/playbook_federation_surfaces.min.json is out of date")
    except Exception as exc:  # pragma: no cover - reported as validator issue
        issues.append(f"federation-closure builder validation failed: {exc}")

    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)

    issues = validate(args.repo_root.resolve())
    if issues:
        print("Federation-closure package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Federation-closure package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
