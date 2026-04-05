#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "config" / "phase_alpha_curated_core.json"
REVIEW_PACKETS_OUTPUT_PATH = REPO_ROOT / "generated" / "phase_alpha_review_packets.min.json"
RUN_MATRIX_OUTPUT_PATH = REPO_ROOT / "generated" / "phase_alpha_run_matrix.min.json"


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


def _load_config() -> dict[str, object]:
    payload = read_json(CONFIG_PATH)
    if not isinstance(payload, dict):
        raise SystemExit("[error] config/phase_alpha_curated_core.json must contain an object")
    return payload


def _require_runtime_path(
    runtime_paths: dict[str, object],
    runtime_path_key: object,
    *,
    location: str,
) -> str:
    if not isinstance(runtime_path_key, str) or not runtime_path_key:
        raise SystemExit(f"[error] {location} runtime_path_key must be a non-empty string")
    runtime_path = runtime_paths.get(runtime_path_key)
    if not isinstance(runtime_path, str) or not runtime_path:
        raise SystemExit(
            f"[error] {location} runtime_path_key '{runtime_path_key}' must resolve in runtime_paths"
        )
    return runtime_path


def build_phase_alpha_review_packets_payload() -> dict[str, object]:
    config = _load_config()
    playbooks = config.get("playbooks", [])
    if not isinstance(playbooks, list):
        raise SystemExit("[error] Phase Alpha config playbooks must stay a list")

    entries: list[dict[str, object]] = []
    for entry in playbooks:
        if not isinstance(entry, dict):
            continue
        entries.append(
            {
                "playbook_id": entry.get("playbook_id"),
                "playbook_name": entry.get("playbook_name"),
                "sequence": entry.get("sequence"),
                "runtime_path_key": entry.get("runtime_path_key"),
                "required_artifacts": entry.get("required_artifacts"),
                "eval_anchors": entry.get("eval_anchors"),
                "memo_outputs": entry.get("memo_outputs"),
                "allowed_reentry_modes": entry.get("allowed_reentry_modes"),
                "recurrence_proof_mode": entry.get("recurrence_proof_mode"),
                "harvest_template_ref": entry.get("harvest_template_ref"),
                "reviewed_run_ref": entry.get("reviewed_run_ref"),
                "readiness_review_ref": entry.get("readiness_review_ref"),
                "source_review_refs": entry.get("source_review_refs"),
            }
        )

    return {
        "schema_version": 1,
        "layer": "aoa-playbooks",
        "phase": "alpha",
        "source_of_truth": {
            "phase_alpha_config": "config/phase_alpha_curated_core.json",
            "alpha_harvests_dir": "examples/alpha_harvests",
            "alpha_reviewed_runs_dir": "docs/alpha-reviewed-runs",
            "alpha_readiness_dir": "docs/alpha-readiness",
        },
        "playbooks": entries,
    }


def build_phase_alpha_run_matrix_payload() -> dict[str, object]:
    config = _load_config()
    runtime_paths = config.get("runtime_paths", {})
    if not isinstance(runtime_paths, dict):
        raise SystemExit("[error] Phase Alpha config runtime_paths must stay an object")
    control_path = _require_runtime_path(runtime_paths, "control", location="Phase Alpha config")

    runs: list[dict[str, object]] = []
    playbooks = config.get("playbooks", [])
    if not isinstance(playbooks, list):
        raise SystemExit("[error] Phase Alpha config playbooks must stay a list")
    for index, entry in enumerate(playbooks):
        if not isinstance(entry, dict):
            continue
        runtime_path_key = entry.get("runtime_path_key")
        runtime_path = _require_runtime_path(
            runtime_paths,
            runtime_path_key,
            location=f"playbooks[{index}]",
        )
        runs.append(
            {
                "run_id": f"alpha-{int(entry['sequence']):02d}-{entry.get('playbook_name')}",
                "sequence": entry.get("sequence"),
                "playbook_id": entry.get("playbook_id"),
                "playbook_name": entry.get("playbook_name"),
                "runtime_path_key": runtime_path_key,
                "runtime_path": runtime_path,
                "control_path": control_path,
                "required_artifacts": entry.get("required_artifacts"),
                "eval_anchors": entry.get("eval_anchors"),
                "memo_outputs": entry.get("memo_outputs"),
                "stop_conditions": entry.get("stop_conditions"),
                "reviewed_run_ref": entry.get("reviewed_run_ref"),
                "recurrence_proof_mode": entry.get("recurrence_proof_mode"),
            }
        )

    final_rerun = config.get("final_rerun", {})
    if not isinstance(final_rerun, dict):
        raise SystemExit("[error] Phase Alpha config final_rerun must stay an object")
    final_runtime_path_key = final_rerun.get("runtime_path_key")
    final_runtime_path = _require_runtime_path(
        runtime_paths,
        final_runtime_path_key,
        location="final_rerun",
    )
    runs.append(
        {
            "run_id": final_rerun.get("run_id"),
            "sequence": 6,
            "playbook_id": final_rerun.get("playbook_id"),
            "playbook_name": final_rerun.get("playbook_name"),
            "runtime_path_key": final_runtime_path_key,
            "runtime_path": final_runtime_path,
            "control_path": control_path,
            "required_artifacts": final_rerun.get("required_artifacts"),
            "eval_anchors": final_rerun.get("eval_anchors"),
            "memo_outputs": final_rerun.get("memo_outputs"),
            "stop_conditions": final_rerun.get("stop_conditions"),
            "reviewed_run_ref": final_rerun.get("run_ref"),
            "recall_mode": final_rerun.get("recall_mode"),
            "recall_contract_ref": final_rerun.get("recall_contract_ref"),
        }
    )

    return {
        "schema_version": 1,
        "layer": "aoa-playbooks",
        "phase": "alpha",
        "source_of_truth": {
            "phase_alpha_config": "config/phase_alpha_curated_core.json",
            "review_packets": "generated/phase_alpha_review_packets.min.json",
        },
        "runs": runs,
    }


def write_output(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate compact Phase Alpha readiness surfaces.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the generated output without writing files.",
    )
    args = parser.parse_args(argv)

    review_packets = build_phase_alpha_review_packets_payload()
    run_matrix = build_phase_alpha_run_matrix_payload()
    if args.check:
        current_review_packets = read_json(REVIEW_PACKETS_OUTPUT_PATH)
        current_run_matrix = read_json(RUN_MATRIX_OUTPUT_PATH)
        if current_review_packets != review_packets:
            raise SystemExit(
                "[error] generated/phase_alpha_review_packets.min.json is out of date; "
                "run scripts/generate_phase_alpha_surfaces.py"
            )
        if current_run_matrix != run_matrix:
            raise SystemExit(
                "[error] generated/phase_alpha_run_matrix.min.json is out of date; "
                "run scripts/generate_phase_alpha_surfaces.py"
            )
        print("[ok] Phase Alpha generated surfaces are current")
        return 0

    write_output(REVIEW_PACKETS_OUTPUT_PATH, review_packets)
    write_output(RUN_MATRIX_OUTPUT_PATH, run_matrix)
    print("[ok] wrote Phase Alpha generated surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
