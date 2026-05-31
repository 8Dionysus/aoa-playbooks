#!/usr/bin/env python3
"""Compatibility command for the federation-closure mechanic builder."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
IMPL_PATH = (
    REPO_ROOT
    / "mechanics"
    / "federation-closure"
    / "parts"
    / "federation-surfaces"
    / "scripts"
    / "generate_playbook_federation_surfaces.py"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

SPEC = importlib.util.spec_from_file_location("federation_closure_builder", IMPL_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"unable to load federation closure builder from {IMPL_PATH}")
_impl = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(_impl)

for _name in dir(_impl):
    if not _name.startswith("_"):
        globals()[_name] = getattr(_impl, _name)


if __name__ == "__main__":
    raise SystemExit(main())
