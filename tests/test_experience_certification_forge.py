from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK = ROOT / "playbooks" / "experience-certification-forge" / "PLAYBOOK.md"


def test_experience_certification_forge_names_stop_lines() -> None:
    text = PLAYBOOK.read_text(encoding="utf-8")
    for token in (
        "does not deploy",
        "does not certify",
        "Codex is being asked to certify",
        "rollback drill",
        "operator review",
        "safe_stop",
    ):
        assert token in text


def test_experience_certification_forge_keeps_eval_anchor_bounded() -> None:
    text = PLAYBOOK.read_text(encoding="utf-8")
    assert "aoa-experience-certification-gate-integrity" in text
    assert "rollout-ring promotion" in text
