from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


def _load_json(relative_path: str) -> object:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def _load_playbook_frontmatter(relative_path: str) -> dict[str, object]:
    text = (ROOT / relative_path).read_text(encoding="utf-8")
    start = text.index("---\n") + 4
    end = text.index("\n---\n", start)
    import yaml

    return yaml.safe_load(text[start:end])


def test_checkpoint_distillation_pilot_activation_surface_validates() -> None:
    schema = _load_json("schemas/playbook-activation-surface.schema.json")
    example = _load_json(
        "examples/playbook_activation.checkpoint-distillation-closed-loop-pilot.example.json"
    )
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(example)


def test_checkpoint_distillation_pilot_frontmatter_matches_example() -> None:
    frontmatter = _load_playbook_frontmatter(
        "playbooks/checkpoint-distillation-closed-loop-pilot/PLAYBOOK.md"
    )
    example = _load_json(
        "examples/playbook_activation.checkpoint-distillation-closed-loop-pilot.example.json"
    )

    assert frontmatter["id"] == "AOA-P-0046"
    assert frontmatter["name"] == example["name"]
    assert frontmatter["scenario"] == example["scenario"]
    assert frontmatter["trigger"] == example["trigger"]
    assert frontmatter["expected_artifacts"] == example["expected_artifacts"]


def test_checkpoint_distillation_runbook_doc_mentions_playbook() -> None:
    docs = (ROOT / "docs" / "CHECKPOINT_DISTILLATION_CLOSED_LOOP_PILOT.md").read_text(
        encoding="utf-8"
    )
    assert "checkpoint-distillation-closed-loop-pilot" in docs
