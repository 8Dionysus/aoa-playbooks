#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "generated" / "playbook_registry.min.json"
OUTPUT_PATH = REPO_ROOT / "generated" / "playbook_activation_surfaces.min.json"
ACTIVATION_PLAYBOOK_IDS = (
    "AOA-P-0008",
    "AOA-P-0009",
    "AOA-P-0010",
    "AOA-P-0011",
    "AOA-P-0012",
    "AOA-P-0013",
    "AOA-P-0014",
    "AOA-P-0015",
    "AOA-P-0016",
    "AOA-P-0017",
)
OPTIONAL_RETURN_FIELDS = ("return_posture", "return_anchor_artifacts", "return_reentry_modes")


def read_registry() -> dict[str, object]:
    try:
        payload = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"[error] missing required file: {REGISTRY_PATH.relative_to(REPO_ROOT).as_posix()}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"[error] invalid JSON in {REGISTRY_PATH.relative_to(REPO_ROOT).as_posix()}: {exc}")

    if not isinstance(payload, dict) or not isinstance(payload.get("playbooks"), list):
        raise SystemExit("[error] playbook registry must contain a 'playbooks' list")
    return payload


def build_activation_surface(playbook: dict[str, object]) -> dict[str, object]:
    surface = {
        "surface_type": "playbook_activation_surface",
        "playbook_id": playbook["id"],
        "name": playbook["name"],
        "scenario": playbook["scenario"],
        "trigger": playbook["trigger"],
        "participating_agents": playbook["participating_agents"],
        "required_skill_families": playbook["required_skill_families"],
        "expected_artifacts": playbook["expected_artifacts"],
        "evaluation_posture": playbook["evaluation_posture"],
        "memory_posture": playbook["memory_posture"],
        "fallback_mode": playbook["fallback_mode"],
    }
    if "eval_anchors" in playbook:
        surface["eval_anchors"] = playbook["eval_anchors"]
    for field_name in OPTIONAL_RETURN_FIELDS:
        if field_name in playbook:
            surface[field_name] = playbook[field_name]
    return surface


def build_activation_surfaces(registry: dict[str, object]) -> list[dict[str, object]]:
    playbooks = registry["playbooks"]
    if not isinstance(playbooks, list):
        raise SystemExit("[error] playbook registry must contain a 'playbooks' list")
    playbooks_by_id: dict[str, dict[str, object]] = {}
    for item in playbooks:
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            playbooks_by_id[item["id"]] = item

    surfaces: list[dict[str, object]] = []
    for playbook_id in ACTIVATION_PLAYBOOK_IDS:
        if playbook_id not in playbooks_by_id:
            raise SystemExit(f"[error] playbook registry is missing required activation target: {playbook_id}")
        surfaces.append(build_activation_surface(playbooks_by_id[playbook_id]))
    return surfaces


def write_output(surfaces: list[dict[str, object]]) -> None:
    OUTPUT_PATH.write_text(json.dumps(surfaces, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate derived playbook activation surfaces.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the generated output without writing files.",
    )
    args = parser.parse_args(argv)

    registry = read_registry()
    surfaces = build_activation_surfaces(registry)
    rendered = json.dumps(surfaces, indent=2) + "\n"

    if args.check:
        try:
            existing = OUTPUT_PATH.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"[error] missing required file: {OUTPUT_PATH.relative_to(REPO_ROOT).as_posix()}", file=sys.stderr)
            return 1
        if existing != rendered:
            print(
                "[error] generated/playbook_activation_surfaces.min.json is out of date; "
                "run scripts/generate_playbook_activation_surfaces.py",
                file=sys.stderr,
            )
            return 1
    else:
        write_output(surfaces)

    print("[ok] derived playbook activation surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
