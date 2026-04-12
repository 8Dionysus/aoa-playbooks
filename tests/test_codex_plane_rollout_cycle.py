from __future__ import annotations

import importlib.util
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "validate_playbooks.py"
SPEC = importlib.util.spec_from_file_location("validate_playbooks", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"unable to load validator module from {MODULE_PATH}")
validate_playbooks = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_playbooks)


def load_generated(name: str):
    return json.loads((REPO_ROOT / "generated" / name).read_text(encoding="utf-8"))


def test_codex_plane_rollout_cycle_companion_stays_discoverable_and_aligned() -> None:
    validate_playbooks.validate_codex_plane_rollout_cycle_companion()


def test_codex_plane_rollout_cycle_stays_companion_to_trusted_rollout_operations() -> None:
    registry = load_generated("playbook_registry.min.json")
    activation = load_generated("playbook_activation_surfaces.min.json")
    federation = load_generated("playbook_federation_surfaces.min.json")

    registry_names = {entry["name"] for entry in registry["playbooks"]}
    activation_names = {entry["name"] for entry in activation}
    federation_names = {entry["name"] for entry in federation}

    assert "trusted-rollout-operations" in registry_names
    assert "trusted-rollout-operations" in activation_names
    assert "trusted-rollout-operations" in federation_names
    assert "codex-plane-rollout-cycle" not in registry_names
    assert "codex-plane-rollout-cycle" not in activation_names
    assert "codex-plane-rollout-cycle" not in federation_names
    assert "trusted-rollout-campaign-cadence" not in registry_names
    assert "trusted-rollout-campaign-cadence" not in activation_names
    assert "trusted-rollout-campaign-cadence" not in federation_names
