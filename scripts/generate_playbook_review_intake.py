#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_STATUS_PATH = REPO_ROOT / "generated" / "playbook_review_status.min.json"
REVIEW_PACKET_CONTRACTS_PATH = REPO_ROOT / "generated" / "playbook_review_packet_contracts.min.json"
OUTPUT_PATH = REPO_ROOT / "generated" / "playbook_review_intake.min.json"
EXAMPLES_ROOT = REPO_ROOT / "examples"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"[error] missing required file: {path.relative_to(REPO_ROOT).as_posix()}")


def read_json(path: Path) -> object:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"[error] invalid JSON in {path.relative_to(REPO_ROOT).as_posix()}: {exc}")


def _load_review_status_by_id() -> dict[str, dict[str, object]]:
    payload = read_json(REVIEW_STATUS_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("playbooks"), list):
        raise SystemExit("[error] generated/playbook_review_status.min.json must contain a playbooks list")
    return {
        item["playbook_id"]: item
        for item in payload["playbooks"]
        if isinstance(item, dict) and isinstance(item.get("playbook_id"), str)
    }


def _load_review_packet_contracts() -> list[dict[str, object]]:
    payload = read_json(REVIEW_PACKET_CONTRACTS_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("playbooks"), list):
        raise SystemExit("[error] generated/playbook_review_packet_contracts.min.json must contain a playbooks list")
    return [item for item in payload["playbooks"] if isinstance(item, dict)]


def _activation_example_ref(playbook_name: str) -> str | None:
    candidate = EXAMPLES_ROOT / f"playbook_activation.{playbook_name}.example.json"
    if candidate.is_file():
        return candidate.relative_to(REPO_ROOT).as_posix()
    return None


def _composition_posture(*, gate_verdict: str | None, reviewed_run_count: int) -> str:
    if gate_verdict == "composition-landed":
        return "landed"
    if gate_verdict == "ready-for-composition-review":
        return "ready-for-composition-review"
    if gate_verdict == "hold" and reviewed_run_count > 0:
        return "held-after-review"
    if gate_verdict == "hold":
        return "awaiting-reviewed-run"
    return "ungated"


def build_review_intake_payload() -> dict[str, object]:
    review_status_by_id = _load_review_status_by_id()
    review_packet_contracts = _load_review_packet_contracts()

    entries: list[dict[str, object]] = []
    for contract in review_packet_contracts:
        playbook_id = contract.get("playbook_id")
        playbook_name = contract.get("playbook_name")
        scenario = contract.get("scenario")
        if not isinstance(playbook_id, str) or not isinstance(playbook_name, str) or not isinstance(scenario, str):
            continue

        review_status = review_status_by_id.get(playbook_id)
        gate_review_ref = review_status.get("gate_review_ref") if isinstance(review_status, dict) else None
        if not isinstance(gate_review_ref, str):
            gate_review_ref = None

        reviewed_run_refs = (
            [item for item in review_status.get("reviewed_run_refs", []) if isinstance(item, str)]
            if isinstance(review_status, dict)
            else []
        )
        gate_verdict = review_status.get("gate_verdict") if isinstance(review_status, dict) else contract.get("gate_verdict")
        if not isinstance(gate_verdict, str):
            gate_verdict = None

        entries.append(
            {
                "playbook_id": playbook_id,
                "playbook_name": playbook_name,
                "scenario": scenario,
                "gate_verdict": gate_verdict,
                "gate_review_ref": gate_review_ref,
                "real_run_template_ref": _activation_example_ref(playbook_name),
                "required_artifact_set": [
                    item for item in contract.get("expected_artifacts", []) if isinstance(item, str)
                ],
                "accepted_packet_kinds": [
                    item for item in contract.get("candidate_packet_kinds", []) if isinstance(item, str)
                ],
                "source_review_refs": [
                    item for item in contract.get("source_review_refs", []) if isinstance(item, str)
                ],
                "review_outcome_targets": {
                    "real_runs": reviewed_run_refs,
                    "gate_reviews": [gate_review_ref] if gate_review_ref else [],
                },
                "composition_posture": _composition_posture(
                    gate_verdict=gate_verdict,
                    reviewed_run_count=len(reviewed_run_refs),
                ),
            }
        )

    entries.sort(key=lambda item: item["playbook_id"])
    return {
        "schema_version": 1,
        "layer": "aoa-playbooks",
        "source_of_truth": {
            "review_packet_contracts": "generated/playbook_review_packet_contracts.min.json",
            "review_status": "generated/playbook_review_status.min.json",
            "activation_examples": "examples/playbook_activation.*.example.json",
            "gate_reviews_dir": "docs/gate-reviews",
            "reviewed_runs_dir": "docs/real-runs",
        },
        "playbooks": entries,
    }


def write_output(payload: dict[str, object]) -> None:
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate compact playbook review intake surface.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the generated output without writing files.",
    )
    args = parser.parse_args(argv)

    payload = build_review_intake_payload()
    if args.check:
        current = read_json(OUTPUT_PATH)
        if current != payload:
            raise SystemExit(
                "[error] generated/playbook_review_intake.min.json is out of date; "
                "run scripts/generate_playbook_review_intake.py"
            )
        print("[ok] generated/playbook_review_intake.min.json is current")
        return 0

    write_output(payload)
    print("[ok] wrote generated/playbook_review_intake.min.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
