from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATED_ROOT = REPO_ROOT / "generated"
DOCS_ROOT = REPO_ROOT / "docs"


def load_generated(name: str):
    return json.loads((GENERATED_ROOT / name).read_text(encoding="utf-8"))


def test_trusted_rollout_operations_docs_and_routes_stay_discoverable() -> None:
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    docs_map = (DOCS_ROOT / "README.md").read_text(encoding="utf-8")
    operational_family = (DOCS_ROOT / "PLAYBOOK_OPERATIONAL_FAMILY.md").read_text(encoding="utf-8")
    portfolio = (DOCS_ROOT / "PLAYBOOK_PORTFOLIO.md").read_text(encoding="utf-8")
    gap_matrix = (DOCS_ROOT / "PLAYBOOK_GAP_MATRIX.md").read_text(encoding="utf-8")
    execution_seam = (DOCS_ROOT / "PLAYBOOK_EXECUTION_SEAM.md").read_text(encoding="utf-8")
    workflow = (DOCS_ROOT / "PLAYBOOK_REAL_RUN_WORKFLOW.md").read_text(encoding="utf-8")
    cycle_doc = (DOCS_ROOT / "CODEX_PLANE_ROLLOUT_CYCLE.md").read_text(encoding="utf-8")
    real_runs_home = (DOCS_ROOT / "real-runs" / "README.md").read_text(encoding="utf-8")
    gate_review = (DOCS_ROOT / "gate-reviews" / "trusted-rollout-operations.md").read_text(encoding="utf-8")
    reviewed_run_initial = (
        DOCS_ROOT / "real-runs" / "2026-04-11.trusted-rollout-operations.initial-stable-regen.md"
    ).read_text(encoding="utf-8")
    reviewed_run = (DOCS_ROOT / "real-runs" / "2026-04-11.trusted-rollout-operations.md").read_text(
        encoding="utf-8"
    )
    decision_note = (
        DOCS_ROOT / "decisions" / "2026-04-11-trusted-rollout-operations-extraction.md"
    ).read_text(encoding="utf-8")

    for text in (
        readme,
        docs_map,
        operational_family,
        portfolio,
        gap_matrix,
        execution_seam,
        workflow,
        cycle_doc,
        real_runs_home,
        gate_review,
        reviewed_run_initial,
        reviewed_run,
    ):
        assert "AOA-P-0028" in text

    assert "playbooks/trusted-rollout-operations/PLAYBOOK.md" in readme
    assert "playbooks/trusted-rollout-operations/PLAYBOOK.md" in docs_map
    assert "examples/codex_plane_rollout_lane.example.json" in readme
    assert "trusted-rollout-operations.harvest-template.md" in workflow
    assert "docs/gate-reviews/trusted-rollout-operations.md" in reviewed_run_initial
    assert "docs/gate-reviews/trusted-rollout-operations.md" in reviewed_run
    assert "docs/real-runs/2026-04-11.trusted-rollout-operations.md" in gate_review
    assert "AOA-P-0028" in decision_note


def test_trusted_rollout_operations_stays_out_of_composition_after_two_reviewed_runs() -> None:
    activation = load_generated("playbook_activation_surfaces.min.json")
    federation = load_generated("playbook_federation_surfaces.min.json")
    review_status = load_generated("playbook_review_status.min.json")
    review_packets = load_generated("playbook_review_packet_contracts.min.json")
    review_intake = load_generated("playbook_review_intake.min.json")
    landing = load_generated("playbook_landing_governance.min.json")
    manifest = load_generated("playbook_composition_manifest.json")

    activation_by_id = {entry["playbook_id"]: entry for entry in activation}
    federation_by_id = {entry["playbook_id"]: entry for entry in federation}
    review_status_by_id = {entry["playbook_id"]: entry for entry in review_status["playbooks"]}
    review_packets_by_id = {entry["playbook_id"]: entry for entry in review_packets["playbooks"]}
    review_intake_by_id = {entry["playbook_id"]: entry for entry in review_intake["playbooks"]}
    landing_by_id = {entry["playbook_id"]: entry for entry in landing["playbooks"]}

    assert "AOA-P-0028" in activation_by_id
    assert "AOA-P-0028" in federation_by_id
    assert review_status_by_id["AOA-P-0028"]["reviewed_run_count"] == 2
    assert review_status_by_id["AOA-P-0028"]["reviewed_run_refs"] == [
        "docs/real-runs/2026-04-11.trusted-rollout-operations.initial-stable-regen.md",
        "docs/real-runs/2026-04-11.trusted-rollout-operations.md",
    ]
    assert review_status_by_id["AOA-P-0028"]["latest_reviewed_run_ref"] == (
        "docs/real-runs/2026-04-11.trusted-rollout-operations.md"
    )
    assert review_status_by_id["AOA-P-0028"]["gate_review_ref"] == "docs/gate-reviews/trusted-rollout-operations.md"
    assert review_status_by_id["AOA-P-0028"]["gate_verdict"] == "hold"
    assert review_packets_by_id["AOA-P-0028"]["source_review_refs"] == [
        "playbooks/trusted-rollout-operations/PLAYBOOK.md",
        "docs/gate-reviews/trusted-rollout-operations.md",
        "docs/real-runs/2026-04-11.trusted-rollout-operations.initial-stable-regen.md",
        "docs/real-runs/2026-04-11.trusted-rollout-operations.md",
    ]
    assert review_packets_by_id["AOA-P-0028"]["gate_verdict"] == "hold"
    assert review_intake_by_id["AOA-P-0028"]["gate_review_ref"] == "docs/gate-reviews/trusted-rollout-operations.md"
    assert review_intake_by_id["AOA-P-0028"]["composition_posture"] == "held-after-review"
    assert landing_by_id["AOA-P-0028"]["in_review_status"] is True
    assert landing_by_id["AOA-P-0028"]["in_composition_manifest"] is False
    assert landing_by_id["AOA-P-0028"]["gate_verdict"] == "hold"
    assert "trusted-rollout-operations" not in manifest["managed_playbooks"]
