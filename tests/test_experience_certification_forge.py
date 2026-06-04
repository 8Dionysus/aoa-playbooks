from __future__ import annotations

from pathlib import Path

from scripts.playbook_source_home import playbook_path_for_name


ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK = playbook_path_for_name("experience-certification-forge", ROOT)


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
