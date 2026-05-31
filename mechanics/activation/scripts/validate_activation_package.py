#!/usr/bin/env python3
"""Validate the activation mechanic package."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "activation"
IMPL_PATH = (
    PACKAGE_ROOT
    / "parts"
    / "activation-surface"
    / "scripts"
    / "generate_playbook_activation_surfaces.py"
)
ROOT_WRAPPER_PATH = REPO_ROOT / "scripts" / "generate_playbook_activation_surfaces.py"
OUTPUT_PATH = REPO_ROOT / "generated" / "playbook_activation_surfaces.min.json"

REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "PARTS.md",
    "PROVENANCE.md",
    "legacy/README.md",
    "legacy/INDEX.md",
    "legacy/DISTILLATION_LOG.md",
    "parts/AGENTS.md",
    "parts/README.md",
    "parts/activation-surface/README.md",
    "parts/activation-surface/scripts/generate_playbook_activation_surfaces.py",
)

REQUIRED_TEXT = {
    "README.md": (
        "## Mechanic card",
        "class | local, not head-fed",
        "generated/playbook_activation_surfaces.min.json",
    ),
    "PARTS.md": (
        "activation-surface",
        "Boundary payloads",
        "mechanics/activation/parts/activation-surface/examples/playbook_activation.*.example.json",
    ),
    "PROVENANCE.md": (
        "mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py",
        "accepted-input",
        "implementation moved into activation package",
    ),
    "legacy/INDEX.md": (
        "Former root path",
        "mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py",
    ),
}


def load_impl():
    spec = importlib.util.spec_from_file_location("activation_package_builder", IMPL_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load activation package builder from {IMPL_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    issues: list[str] = []
    package_root = repo_root / "mechanics" / "activation"

    for relative_path in REQUIRED_FILES:
        if not (package_root / relative_path).is_file():
            issues.append(f"mechanics/activation/{relative_path}: missing required file")

    for relative_path, tokens in REQUIRED_TEXT.items():
        path = package_root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                issues.append(f"mechanics/activation/{relative_path}: missing token {token!r}")

    if not ROOT_WRAPPER_PATH.is_file():
        issues.append("scripts/generate_playbook_activation_surfaces.py: missing compatibility wrapper")
    else:
        wrapper_text = ROOT_WRAPPER_PATH.read_text(encoding="utf-8")
        if "mechanics" not in wrapper_text or "activation-surface" not in wrapper_text:
            issues.append("scripts/generate_playbook_activation_surfaces.py: wrapper must route to activation package")

    try:
        builder = load_impl()
        registry = builder.read_registry()
        expected = builder.build_activation_surfaces(registry)
        current = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        if current != expected:
            issues.append("generated/playbook_activation_surfaces.min.json is out of date")
    except Exception as exc:  # pragma: no cover - reported as validator issue
        issues.append(f"activation builder validation failed: {exc}")

    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)

    issues = validate(args.repo_root.resolve())
    if issues:
        print("Activation package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Activation package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
