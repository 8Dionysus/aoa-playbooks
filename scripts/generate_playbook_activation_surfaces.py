#!/usr/bin/env python3
"""Compatibility command for the activation mechanic surface builder."""
from __future__ import annotations

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
IMPL_PATH = (
    REPO_ROOT
    / "mechanics"
    / "activation"
    / "parts"
    / "activation-surface"
    / "scripts"
    / "generate_playbook_activation_surfaces.py"
)

SPEC = importlib.util.spec_from_file_location("activation_surface_builder", IMPL_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"unable to load activation surface builder from {IMPL_PATH}")
_impl = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(_impl)

ACTIVATION_PLAYBOOK_IDS = _impl.ACTIVATION_PLAYBOOK_IDS
OPTIONAL_MEMO_SPEC_FIELDS = _impl.OPTIONAL_MEMO_SPEC_FIELDS
OPTIONAL_RETURN_FIELDS = _impl.OPTIONAL_RETURN_FIELDS
OUTPUT_PATH = _impl.OUTPUT_PATH
REGISTRY_PATH = _impl.REGISTRY_PATH

build_activation_surface = _impl.build_activation_surface
build_activation_surfaces = _impl.build_activation_surfaces
main = _impl.main
read_registry = _impl.read_registry
write_output = _impl.write_output


if __name__ == "__main__":
    raise SystemExit(main())
