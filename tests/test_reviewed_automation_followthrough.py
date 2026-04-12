from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATED_ROOT = REPO_ROOT / "generated"
DOCS_ROOT = REPO_ROOT / "docs"


def load_generated(name: str):
    return json.loads((GENERATED_ROOT / name).read_text(encoding="utf-8"))


def test_reviewed_automation_followthrough_docs_and_examples_stay_discoverable() -> None:
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    docs_map = (DOCS_ROOT / "README.md").read_text(encoding="utf-8")
    operational_family = (DOCS_ROOT / "PLAYBOOK_OPERATIONAL_FAMILY.md").read_text(encoding="utf-8")
    portfolio = (DOCS_ROOT / "PLAYBOOK_PORTFOLIO.md").read_text(encoding="utf-8")
    gap_matrix = (DOCS_ROOT / "PLAYBOOK_GAP_MATRIX.md").read_text(encoding="utf-8")
    execution_seam = (DOCS_ROOT / "PLAYBOOK_EXECUTION_SEAM.md").read_text(encoding="utf-8")
    automation_doc = (DOCS_ROOT / "AUTOMATION_SEEDS.md").read_text(encoding="utf-8")
    example = (
        REPO_ROOT / "examples" / "automations" / "reviewed-automation-followthrough.md"
    ).read_text(encoding="utf-8")

    for text in (readme, docs_map, operational_family, portfolio, gap_matrix, execution_seam):
        assert "AOA-P-0027" in text

    assert "playbooks/reviewed-automation-followthrough/PLAYBOOK.md" in readme
    assert "playbooks/reviewed-automation-followthrough/PLAYBOOK.md" in docs_map
    assert "examples/automations/reviewed-automation-followthrough.md" in automation_doc
    assert "outside `config/playbook_composition_overrides.json`" in automation_doc
    assert "not yet a composition-owned automation" in example


def test_reviewed_automation_followthrough_stays_out_of_composition_until_gate_review() -> None:
    activation = load_generated("playbook_activation_surfaces.min.json")
    federation = load_generated("playbook_federation_surfaces.min.json")
    review_packets = load_generated("playbook_review_packet_contracts.min.json")
    landing = load_generated("playbook_landing_governance.min.json")
    automation = load_generated("playbook_automation_seeds.json")
    manifest = load_generated("playbook_composition_manifest.json")

    activation_by_id = {entry["playbook_id"]: entry for entry in activation}
    federation_by_id = {entry["playbook_id"]: entry for entry in federation}
    review_packets_by_id = {entry["playbook_id"]: entry for entry in review_packets["playbooks"]}
    landing_by_id = {entry["playbook_id"]: entry for entry in landing["playbooks"]}

    assert "AOA-P-0027" in activation_by_id
    assert "AOA-P-0027" in federation_by_id
    assert review_packets_by_id["AOA-P-0027"]["source_review_refs"] == [
        "playbooks/reviewed-automation-followthrough/PLAYBOOK.md"
    ]
    assert review_packets_by_id["AOA-P-0027"]["gate_verdict"] is None
    assert landing_by_id["AOA-P-0027"]["in_review_status"] is False
    assert landing_by_id["AOA-P-0027"]["in_composition_manifest"] is False
    assert landing_by_id["AOA-P-0027"]["gate_verdict"] is None
    assert "reviewed-automation-followthrough" not in manifest["managed_playbooks"]
    assert all(seed["playbook"] != "reviewed-automation-followthrough" for seed in automation["seeds"])
