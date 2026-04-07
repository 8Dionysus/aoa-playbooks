#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "generated" / "playbook_registry.min.json"
REVIEW_PACKET_CONTRACTS_PATH = REPO_ROOT / "generated" / "playbook_review_packet_contracts.min.json"
REVIEW_INTAKE_PATH = REPO_ROOT / "generated" / "playbook_review_intake.min.json"
REVIEW_STATUS_PATH = REPO_ROOT / "generated" / "playbook_review_status.min.json"
COMPOSITION_MANIFEST_PATH = REPO_ROOT / "generated" / "playbook_composition_manifest.json"
OUTPUT_PATH = REPO_ROOT / "generated" / "playbook_landing_governance.min.json"


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


def _load_registry_by_id() -> dict[str, dict[str, object]]:
    payload = read_json(REGISTRY_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("playbooks"), list):
        raise SystemExit("[error] generated/playbook_registry.min.json must contain a playbooks list")
    return {
        item["id"]: item
        for item in payload["playbooks"]
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }


def _load_playbooks_by_id(path: Path) -> dict[str, dict[str, object]]:
    payload = read_json(path)
    if not isinstance(payload, dict) or not isinstance(payload.get("playbooks"), list):
        raise SystemExit(f"[error] {path.relative_to(REPO_ROOT).as_posix()} must contain a playbooks list")
    return {
        item["playbook_id"]: item
        for item in payload["playbooks"]
        if isinstance(item, dict) and isinstance(item.get("playbook_id"), str)
    }


def _managed_playbook_names() -> set[str]:
    payload = read_json(COMPOSITION_MANIFEST_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("managed_playbooks"), list):
        raise SystemExit("[error] generated/playbook_composition_manifest.json must contain managed_playbooks")
    return {
        item
        for item in payload["managed_playbooks"]
        if isinstance(item, str)
    }


def build_playbook_landing_governance_payload() -> dict[str, object]:
    registry_by_id = _load_registry_by_id()
    packet_by_id = _load_playbooks_by_id(REVIEW_PACKET_CONTRACTS_PATH)
    intake_by_id = _load_playbooks_by_id(REVIEW_INTAKE_PATH)
    review_status_by_id = _load_playbooks_by_id(REVIEW_STATUS_PATH)
    managed_playbook_names = _managed_playbook_names()

    scoped_ids = sorted(set(packet_by_id) & set(intake_by_id))
    entries: list[dict[str, object]] = []
    for playbook_id in scoped_ids:
        registry_entry = registry_by_id.get(playbook_id)
        packet_entry = packet_by_id.get(playbook_id)
        intake_entry = intake_by_id.get(playbook_id)
        review_status_entry = review_status_by_id.get(playbook_id)

        playbook_name = None
        if isinstance(registry_entry, dict) and isinstance(registry_entry.get("name"), str):
            playbook_name = registry_entry["name"]
        elif isinstance(packet_entry, dict) and isinstance(packet_entry.get("playbook_name"), str):
            playbook_name = packet_entry["playbook_name"]
        elif isinstance(intake_entry, dict) and isinstance(intake_entry.get("playbook_name"), str):
            playbook_name = intake_entry["playbook_name"]

        registry_status = registry_entry.get("status") if isinstance(registry_entry, dict) else None
        gate_verdict = review_status_entry.get("gate_verdict") if isinstance(review_status_entry, dict) else None
        if not isinstance(gate_verdict, str):
            gate_verdict = None

        blockers: list[str] = []
        if registry_entry is None:
            blockers.append("missing_registry_entry")
        elif registry_status != "experimental":
            blockers.append("registry_status_not_experimental")
        if packet_entry is None:
            blockers.append("missing_review_packet_contract")
        elif not packet_entry:
            blockers.append("empty_review_packet_contract")
        if intake_entry is None:
            blockers.append("missing_review_intake")
        elif not intake_entry:
            blockers.append("empty_review_intake")
        if (
            isinstance(packet_entry, dict)
            and isinstance(intake_entry, dict)
            and packet_entry.get("playbook_name") != intake_entry.get("playbook_name")
        ):
            blockers.append("packet_intake_name_mismatch")
        if (
            isinstance(packet_entry, dict)
            and isinstance(intake_entry, dict)
            and packet_entry.get("scenario") != intake_entry.get("scenario")
        ):
            blockers.append("packet_intake_scenario_mismatch")
        if gate_verdict is not None and gate_verdict not in {"composition-landed", "hold"}:
            blockers.append("unsupported_gate_verdict")
        in_composition_manifest = isinstance(playbook_name, str) and playbook_name in managed_playbook_names
        if gate_verdict == "composition-landed" and not in_composition_manifest:
            blockers.append("composition_landed_missing_manifest_membership")

        entries.append(
            {
                "playbook_id": playbook_id,
                "playbook_name": playbook_name,
                "registry_status": registry_status,
                "in_registry": registry_entry is not None,
                "in_review_packet_contracts": packet_entry is not None,
                "in_review_intake": intake_entry is not None,
                "in_review_status": review_status_entry is not None,
                "in_composition_manifest": in_composition_manifest,
                "gate_verdict": gate_verdict,
                "landing_passed": not blockers,
                "blockers": blockers,
            }
        )

    return {
        "schema_version": 1,
        "layer": "aoa-playbooks",
        "scope": "review-track",
        "source_of_truth": {
            "registry": "generated/playbook_registry.min.json",
            "review_packet_contracts": "generated/playbook_review_packet_contracts.min.json",
            "review_intake": "generated/playbook_review_intake.min.json",
            "review_status": "generated/playbook_review_status.min.json",
            "composition_manifest": "generated/playbook_composition_manifest.json",
        },
        "playbooks": entries,
    }


def write_output(payload: dict[str, object]) -> None:
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate compact playbook landing governance surface.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the generated output without writing files.",
    )
    args = parser.parse_args(argv)

    payload = build_playbook_landing_governance_payload()
    if args.check:
        current = read_json(OUTPUT_PATH)
        if current != payload:
            raise SystemExit(
                "[error] generated/playbook_landing_governance.min.json is out of date; "
                "run scripts/generate_playbook_landing_governance.py"
            )
        print("[ok] generated/playbook_landing_governance.min.json is current")
        return 0

    write_output(payload)
    print("[ok] wrote generated/playbook_landing_governance.min.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
