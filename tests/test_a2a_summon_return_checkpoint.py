from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATED_ROOT = REPO_ROOT / "generated"
DOCS_ROOT = REPO_ROOT / "docs"


def load_generated(name: str):
    return json.loads((GENERATED_ROOT / name).read_text(encoding="utf-8"))


def test_a2a_summon_return_checkpoint_docs_stay_discoverable() -> None:
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    docs_map = (DOCS_ROOT / "README.md").read_text(encoding="utf-8")
    operational_family = (DOCS_ROOT / "PLAYBOOK_OPERATIONAL_FAMILY.md").read_text(
        encoding="utf-8"
    )
    portfolio = (DOCS_ROOT / "PLAYBOOK_PORTFOLIO.md").read_text(encoding="utf-8")
    gap_matrix = (DOCS_ROOT / "PLAYBOOK_GAP_MATRIX.md").read_text(encoding="utf-8")
    execution_seam = (DOCS_ROOT / "PLAYBOOK_EXECUTION_SEAM.md").read_text(encoding="utf-8")
    roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")

    for text in (
        readme,
        docs_map,
        operational_family,
        portfolio,
        gap_matrix,
        execution_seam,
        roadmap,
    ):
        assert "AOA-P-0031" in text

    assert "playbooks/a2a-summon-return-checkpoint/PLAYBOOK.md" in readme
    assert "a2a-summon-return-checkpoint" in docs_map
    assert "hidden child automation" in readme
    assert "runtime dry-run receipt" in execution_seam


def test_a2a_summon_return_checkpoint_stays_out_of_composition_until_reviewed_run() -> None:
    activation = load_generated("playbook_activation_surfaces.min.json")
    federation = load_generated("playbook_federation_surfaces.min.json")
    review_packets = load_generated("playbook_review_packet_contracts.min.json")
    landing = load_generated("playbook_landing_governance.min.json")
    manifest = load_generated("playbook_composition_manifest.json")

    activation_by_id = {entry["playbook_id"]: entry for entry in activation}
    federation_by_id = {entry["playbook_id"]: entry for entry in federation}
    review_packets_by_id = {entry["playbook_id"]: entry for entry in review_packets["playbooks"]}
    landing_by_id = {entry["playbook_id"]: entry for entry in landing["playbooks"]}

    assert activation_by_id["AOA-P-0031"]["return_posture"] == "checkpoint_anchor"
    assert federation_by_id["AOA-P-0031"]["memo_checkpoint_posture"] == "required"
    assert review_packets_by_id["AOA-P-0031"]["source_review_refs"] == [
        "playbooks/a2a-summon-return-checkpoint/PLAYBOOK.md"
    ]
    assert review_packets_by_id["AOA-P-0031"]["gate_verdict"] is None
    assert landing_by_id["AOA-P-0031"]["in_review_status"] is False
    assert landing_by_id["AOA-P-0031"]["in_composition_manifest"] is False
    assert landing_by_id["AOA-P-0031"]["gate_verdict"] is None
    assert "a2a-summon-return-checkpoint" not in manifest["managed_playbooks"]
