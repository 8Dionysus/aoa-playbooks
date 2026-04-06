from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "publish_live_receipts.py"


def load_module():
    spec = importlib.util.spec_from_file_location("publish_live_receipts", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


def build_receipt(event_kind: str = "playbook_review_harvest_receipt") -> dict:
    return {
        "event_kind": event_kind,
        "event_id": "evt-playbook-001",
        "observed_at": "2026-04-06T20:00:00Z",
        "run_ref": "run-playbook-001",
        "session_ref": "session:test-playbook-closeout",
        "actor_ref": "aoa-playbooks:owner-first-capability-landing",
        "object_ref": {
            "repo": "aoa-playbooks",
            "kind": "playbook",
            "id": "AOA-P-0021",
            "version": "main",
        },
        "evidence_refs": [
            {
                "kind": "reviewed_run",
                "ref": "repo:aoa-playbooks/docs/real-runs/2026-04-06.owner-first-capability-landing.md",
            }
        ],
        "payload": {
            "gate_verdict": "composition-landed",
            "reviewed_run_ref": "docs/real-runs/2026-04-06.owner-first-capability-landing.md",
        },
    }


def test_publish_live_receipts_appends_once_and_skips_duplicates(tmp_path: Path) -> None:
    module = load_module()
    input_path = tmp_path / "receipt.json"
    log_path = tmp_path / "playbook-receipts.jsonl"
    input_path.write_text(json.dumps(build_receipt(), indent=2) + "\n", encoding="utf-8")

    receipts = module.load_receipts([input_path])
    appended, skipped = module.append_new_receipts(log_path=log_path, receipts=receipts)
    assert appended == 1
    assert skipped == 0

    appended, skipped = module.append_new_receipts(log_path=log_path, receipts=receipts)
    assert appended == 0
    assert skipped == 1


def test_publish_live_receipts_rejects_unsupported_event_kind(tmp_path: Path) -> None:
    module = load_module()
    input_path = tmp_path / "receipt.json"
    input_path.write_text(
        json.dumps(build_receipt(event_kind="automation_candidate_receipt"), indent=2) + "\n",
        encoding="utf-8",
    )

    with pytest.raises(module.ReceiptPublishError):
        module.load_receipts([input_path])
