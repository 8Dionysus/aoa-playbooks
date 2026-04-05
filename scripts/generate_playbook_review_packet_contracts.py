#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "generated" / "playbook_registry.min.json"
ACTIVATION_PATH = REPO_ROOT / "generated" / "playbook_activation_surfaces.min.json"
FEDERATION_PATH = REPO_ROOT / "generated" / "playbook_federation_surfaces.min.json"
REVIEW_STATUS_PATH = REPO_ROOT / "generated" / "playbook_review_status.min.json"
OUTPUT_PATH = REPO_ROOT / "generated" / "playbook_review_packet_contracts.min.json"

KNOWN_MEMO_RUNTIME_SURFACES = (
    "checkpoint_export",
    "approval_record",
    "transition_record",
    "execution_trace",
    "review_trace",
    "distillation_claim_candidate",
    "distillation_pattern_candidate",
    "distillation_bridge_candidate",
)
CANDIDATE_PACKET_KIND_ORDER = (
    "memo_candidate",
    "runtime_evidence_selection_candidate",
    "artifact_hook_candidate",
)


def _resolve_aoa_evals_root() -> Path:
    configured = os.environ.get("AOA_EVALS_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()

    for candidate in (REPO_ROOT.parent / "aoa-evals", REPO_ROOT / ".deps" / "aoa-evals"):
        if candidate.exists():
            return candidate.resolve()

    return (REPO_ROOT.parent / "aoa-evals").resolve()


AOA_EVALS_ROOT = _resolve_aoa_evals_root()


def describe_path(path: Path, *, root: Path = REPO_ROOT) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def runtime_template_index_path() -> Path:
    return AOA_EVALS_ROOT / "generated" / "runtime_candidate_template_index.min.json"


def read_text(path: Path, *, root: Path = REPO_ROOT) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"[error] missing required file: {describe_path(path, root=root)}")


def read_json(path: Path, *, root: Path = REPO_ROOT) -> object:
    try:
        return json.loads(read_text(path, root=root))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"[error] invalid JSON in {describe_path(path, root=root)}: {exc}")


def _load_registry_by_id() -> dict[str, dict[str, object]]:
    payload = read_json(REGISTRY_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("playbooks"), list):
        raise SystemExit("[error] generated/playbook_registry.min.json must contain a 'playbooks' list")

    registry_by_id: dict[str, dict[str, object]] = {}
    for item in payload["playbooks"]:
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            registry_by_id[item["id"]] = item
    if not registry_by_id:
        raise SystemExit("[error] generated/playbook_registry.min.json must list at least one playbook")
    return registry_by_id


def _load_surface_map(path: Path, *, key_name: str) -> dict[str, dict[str, object]]:
    payload = read_json(path)
    if not isinstance(payload, list):
        raise SystemExit(f"[error] {path.relative_to(REPO_ROOT).as_posix()} must contain a JSON list")
    return {
        item[key_name]: item
        for item in payload
        if isinstance(item, dict) and isinstance(item.get(key_name), str)
    }


def _load_review_status_by_id() -> dict[str, dict[str, object]]:
    payload = read_json(REVIEW_STATUS_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("playbooks"), list):
        raise SystemExit("[error] generated/playbook_review_status.min.json must contain a playbooks list")
    return {
        item["playbook_id"]: item
        for item in payload["playbooks"]
        if isinstance(item, dict) and isinstance(item.get("playbook_id"), str)
    }


def _ordered_unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


def _available_runtime_eval_anchors() -> set[str]:
    anchors: set[str] = set()
    payload = read_json(runtime_template_index_path(), root=AOA_EVALS_ROOT)
    if not isinstance(payload, dict) or not isinstance(payload.get("templates"), list):
        raise SystemExit(
            "[error] aoa-evals generated/runtime_candidate_template_index.min.json must contain a templates list"
        )
    for item in payload["templates"]:
        if not isinstance(item, dict):
            raise SystemExit(
                "[error] aoa-evals generated/runtime_candidate_template_index.min.json templates entries must be objects"
            )
        source_example_ref = item.get("source_example_ref")
        if not isinstance(source_example_ref, str) or not source_example_ref:
            raise SystemExit(
                "[error] aoa-evals runtime candidate template entries must keep source_example_ref"
            )
        source_example_path = AOA_EVALS_ROOT / source_example_ref
        if not source_example_path.is_file():
            raise SystemExit(
                "[error] aoa-evals runtime candidate template source is unavailable: "
                f"{describe_path(source_example_path, root=AOA_EVALS_ROOT)}"
            )
        eval_anchor = item.get("eval_anchor")
        if isinstance(eval_anchor, str):
            anchors.add(eval_anchor)
    return anchors


def _string_list(payload: dict[str, object] | None, field_name: str) -> list[str]:
    if payload is None:
        return []
    values = payload.get(field_name)
    if not isinstance(values, list):
        return []
    return [item for item in values if isinstance(item, str)]


def _candidate_packet_kinds(*, memo_runtime_surfaces: list[str], eval_anchors: list[str]) -> list[str]:
    packet_kinds: list[str] = []
    if memo_runtime_surfaces:
        packet_kinds.append("memo_candidate")
    if eval_anchors:
        packet_kinds.extend(
            [
                "runtime_evidence_selection_candidate",
                "artifact_hook_candidate",
            ]
        )
    return [kind for kind in CANDIDATE_PACKET_KIND_ORDER if kind in packet_kinds]


def _playbook_source_review_ref(playbook_name: str) -> str:
    return f"playbooks/{playbook_name}/PLAYBOOK.md"


def build_review_packet_contracts_payload() -> dict[str, object]:
    registry_by_id = _load_registry_by_id()
    activation_by_id = _load_surface_map(ACTIVATION_PATH, key_name="playbook_id")
    federation_by_id = _load_surface_map(FEDERATION_PATH, key_name="playbook_id")
    review_status_by_id = _load_review_status_by_id()
    available_eval_anchors = _available_runtime_eval_anchors()

    entries: list[dict[str, object]] = []
    for playbook_id, registry_entry in sorted(registry_by_id.items()):
        activation_entry = activation_by_id.get(playbook_id)
        federation_entry = federation_by_id.get(playbook_id)
        review_status_entry = review_status_by_id.get(playbook_id)

        expected_artifacts = _string_list(activation_entry, "expected_artifacts")
        if not expected_artifacts:
            expected_artifacts = _string_list(registry_entry, "expected_artifacts")
        eval_anchors = _ordered_unique(
            _string_list(activation_entry, "eval_anchors")
            + _string_list(federation_entry, "eval_anchors")
        )
        eval_anchors = [anchor for anchor in eval_anchors if anchor in available_eval_anchors]
        memo_runtime_surfaces = [
            artifact for artifact in expected_artifacts if artifact in KNOWN_MEMO_RUNTIME_SURFACES
        ]
        candidate_packet_kinds = _candidate_packet_kinds(
            memo_runtime_surfaces=memo_runtime_surfaces,
            eval_anchors=eval_anchors,
        )

        if not (
            review_status_entry is not None
            or activation_entry is not None
            or federation_entry is not None
            or candidate_packet_kinds
        ):
            continue

        source_review_refs: list[str] = [_playbook_source_review_ref(str(registry_entry["name"]))]
        gate_verdict: str | None = None
        if review_status_entry is not None:
            gate_review_ref = review_status_entry.get("gate_review_ref")
            if isinstance(gate_review_ref, str):
                source_review_refs.append(gate_review_ref)
            reviewed_run_refs = review_status_entry.get("reviewed_run_refs")
            if isinstance(reviewed_run_refs, list):
                source_review_refs.extend(ref for ref in reviewed_run_refs if isinstance(ref, str))
            if isinstance(review_status_entry.get("gate_verdict"), str):
                gate_verdict = review_status_entry["gate_verdict"]

        entries.append(
            {
                "playbook_id": playbook_id,
                "playbook_name": registry_entry["name"],
                "scenario": registry_entry["scenario"],
                "expected_artifacts": expected_artifacts,
                "eval_anchors": eval_anchors,
                "memo_runtime_surfaces": memo_runtime_surfaces,
                "candidate_packet_kinds": candidate_packet_kinds,
                "review_required": bool(candidate_packet_kinds),
                "source_review_refs": _ordered_unique(source_review_refs),
                "gate_verdict": gate_verdict,
            }
        )

    return {
        "schema_version": 1,
        "layer": "aoa-playbooks",
        "source_of_truth": {
            "registry": "generated/playbook_registry.min.json",
            "activation": "generated/playbook_activation_surfaces.min.json",
            "federation": "generated/playbook_federation_surfaces.min.json",
            "review_status": "generated/playbook_review_status.min.json",
            "runtime_template_index": "repo:aoa-evals/generated/runtime_candidate_template_index.min.json",
        },
        "playbooks": entries,
    }


def write_output(payload: dict[str, object]) -> None:
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate compact playbook review-packet contracts.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the generated output without writing files.",
    )
    args = parser.parse_args(argv)

    payload = build_review_packet_contracts_payload()
    if args.check:
        current = read_json(OUTPUT_PATH)
        if current != payload:
            raise SystemExit(
                "[error] generated/playbook_review_packet_contracts.min.json is out of date; "
                "run scripts/generate_playbook_review_packet_contracts.py"
            )
        print("[ok] generated/playbook_review_packet_contracts.min.json is current")
        return 0

    write_output(payload)
    print("[ok] wrote generated/playbook_review_packet_contracts.min.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
