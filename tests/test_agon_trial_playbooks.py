from pathlib import Path
import json
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
    data = json.loads((ROOT / "generated" / "agon_trial_playbook_registry.min.json").read_text(encoding="utf-8"))
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
