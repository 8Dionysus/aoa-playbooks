#!/usr/bin/env python3
"""Compatibility command for the Agon trial-playbook validator."""
from __future__ import annotations

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
IMPL_PATH = (
    REPO_ROOT
    / "mechanics"
    / "agon"
    / "parts"
    / "trial-playbooks"
    / "scripts"
    / "validate_agon_trial_playbooks.py"
)

SPEC = importlib.util.spec_from_file_location("agon_trial_playbook_validator", IMPL_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"unable to load Agon trial-playbook validator from {IMPL_PATH}")
_impl = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(_impl)


def _sync_impl_globals() -> None:
    for _name, _value in list(globals().items()):
        if _name in {"_impl", "_sync_impl_globals", "_wrap_impl_function"}:
            continue
        if _name.startswith("__") and _name.endswith("__"):
            continue
        if hasattr(_impl, _name) and not callable(_value):
            setattr(_impl, _name, _value)


def _wrap_impl_function(_function_name: str):
    def _wrapped(*args, **kwargs):
        _sync_impl_globals()
        return getattr(_impl, _function_name)(*args, **kwargs)

    _wrapped.__name__ = _function_name
    _wrapped.__doc__ = getattr(_impl, _function_name).__doc__
    return _wrapped


for _name in dir(_impl):
    if _name.startswith("__") and _name.endswith("__"):
        continue
    _value = getattr(_impl, _name)
    if callable(_value) and getattr(_value, "__module__", None) == _impl.__name__:
        globals()[_name] = _wrap_impl_function(_name)
    else:
        globals()[_name] = _value


if __name__ == "__main__":
    raise SystemExit(main())
