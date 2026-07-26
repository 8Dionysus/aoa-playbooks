from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = (
    REPO_ROOT
    / "mechanics"
    / "scenario-composition"
    / "scripts"
    / "validate_scenario_composition_package.py"
)
SPEC = importlib.util.spec_from_file_location("validate_scenario_composition_package", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def test_scenario_composition_package_validates() -> None:
    assert validator.validate(validator.REPO_ROOT) == []


def test_root_composition_command_is_compatibility_wrapper() -> None:
    wrapper = REPO_ROOT / "scripts" / "generate_playbook_composition_surfaces.py"
    text = wrapper.read_text(encoding="utf-8")

    assert "mechanics" in text
    assert "composition-surfaces" in text
    assert "globals()[_name] = getattr(_impl, _name)" in text


def test_validator_loads_plan_projection_from_requested_repo_root(
    tmp_path: Path,
    monkeypatch,
) -> None:
    staged_root = tmp_path / "staged"
    plan_part = (
        REPO_ROOT
        / "mechanics"
        / "scenario-composition"
        / "parts"
        / "plan-contours"
    )
    shutil.copytree(
        plan_part,
        staged_root
        / "mechanics"
        / "scenario-composition"
        / "parts"
        / "plan-contours",
    )
    source = json.loads(
        (
            plan_part / "config" / "playbook_plan_contours.json"
        ).read_text(encoding="utf-8")
    )
    for contour in source["contours"]:
        source_playbook = Path(contour["source_playbook_ref"])
        target = staged_root / source_playbook
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO_ROOT / source_playbook, target)

    generated = staged_root / "generated" / "playbook_plan_contours.min.json"
    generated.parent.mkdir(parents=True, exist_ok=True)
    generated.write_text("{}\n", encoding="utf-8")
    wrapper = staged_root / "scripts" / "generate_playbook_composition_surfaces.py"
    wrapper.parent.mkdir(parents=True, exist_ok=True)
    wrapper.write_text("# mechanics composition-surfaces\n", encoding="utf-8")

    class FakeCompositionBuilder:
        @staticmethod
        def build_outputs() -> dict[Path, object]:
            return {}

    monkeypatch.setattr(validator, "REQUIRED_FILES", ())
    monkeypatch.setattr(validator, "REQUIRED_TEXT", {})
    monkeypatch.setattr(validator, "load_impl", lambda repo_root: FakeCompositionBuilder)

    issues = validator.validate(staged_root)

    assert any(
        issue == "generated/playbook_plan_contours.min.json is out of date"
        for issue in issues
    )
