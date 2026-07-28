from pathlib import Path
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def test_agon_trial_playbook_registry_build_check():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_agon_trial_playbook_registry.py"), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr + result.stdout

def test_agon_trial_playbooks_are_pre_protocol():
    source = json.loads(
        (
            ROOT
            / "mechanics"
            / "agon"
            / "parts"
            / "trial-playbooks"
            / "config"
            / "agon_trial_playbooks.seed.json"
        ).read_text(encoding="utf-8")
    )
    data = json.loads((ROOT / "generated" / "agon_trial_playbook_registry.min.json").read_text(encoding="utf-8"))
    assert source["gate_trigger_source"].startswith(
        "aoa-sdk/src/aoa_sdk/control_plane/routing/"
    )
    assert "aoa-routing" not in source["gate_trigger_source"]
    assert source["lawful_move_source"].startswith(
        "Agents-of-Abyss/mechanics/agon/parts/lawful-move-grammar/"
    )
    assert data["wave"] == "VI"
    assert data["live_protocol"] is False
    assert data["runtime_effect"] == "none"
    assert data["trial_count"] >= 5
    assert "contestant_seat" in data["assistant_forbidden_authority"]
    for trial in data["trials"]:
        assert trial["live_protocol"] is False
        assert trial["runtime_effect"] == "none"
        assert (ROOT / trial["playbook_path"]).exists()
        assert trial["lawful_moves"]
        assert trial["gate_triggers"]


def test_agon_trial_playbook_validator_passes():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_agon_trial_playbooks.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_agon_trial_playbook_validator_rejects_incomplete_explicit_sdk_root(
    tmp_path,
):
    sdk_root = tmp_path / "aoa-sdk"
    sdk_root.mkdir()
    env = os.environ.copy()
    env["AOA_SDK_ROOT"] = str(sdk_root)

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_agon_trial_playbooks.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env=env,
    )

    assert result.returncode == 1
    assert (
        "explicit AOA_SDK_ROOT does not provide required Agon routing registry"
        in result.stderr
    )


def test_agon_trial_playbook_validator_rejects_incomplete_explicit_center_root(
    tmp_path,
):
    center_root = tmp_path / "Agents-of-Abyss"
    center_root.mkdir()
    env = os.environ.copy()
    env["AOA_CENTER_ROOT"] = str(center_root)

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_agon_trial_playbooks.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env=env,
    )

    assert result.returncode == 1
    assert (
        "explicit AOA_CENTER_ROOT does not provide required lawful-move registry"
        in result.stderr
    )
