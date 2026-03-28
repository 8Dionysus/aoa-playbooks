#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK_ROOT = REPO_ROOT / "playbooks"
OUTPUT_PATH = REPO_ROOT / "generated" / "playbook_federation_surfaces.min.json"
FEDERATION_PLAYBOOK_IDS = (
    "AOA-P-0006",
    "AOA-P-0007",
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
    "AOA-P-0018",
    "AOA-P-0019",
    "AOA-P-0020",
)
OPTIONAL_MEMO_SPEC_FIELDS = (
    "memo_recall_modes",
    "memo_scope_default",
    "memo_scope_ceiling",
    "memo_read_path",
    "memo_checkpoint_posture",
    "memo_source_route_policy",
)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"[error] missing required file: {path.relative_to(REPO_ROOT).as_posix()}")


def parse_scalar(value: str) -> str:
    scalar = value.strip()
    if len(scalar) >= 2 and scalar[0] in {"'", '"'} and scalar[-1] == scalar[0]:
        return scalar[1:-1]
    return scalar


def parse_frontmatter(text: str, path: Path) -> dict[str, object]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        raise SystemExit(f"[error] {path.relative_to(REPO_ROOT).as_posix()} must start with YAML frontmatter")

    frontmatter: dict[str, object] = {}
    current_key: str | None = None

    for index in range(1, len(lines)):
        line = lines[index]
        if line.strip() == "---":
            return frontmatter
        if not line.strip():
            continue
        if line.startswith("  - ") or line.startswith("- "):
            if current_key is None:
                raise SystemExit(
                    f"[error] {path.relative_to(REPO_ROOT).as_posix()} has a list item without a key in frontmatter"
                )
            frontmatter.setdefault(current_key, [])
            assert isinstance(frontmatter[current_key], list)
            frontmatter[current_key].append(parse_scalar(line.split("-", 1)[1]))
            continue
        if ":" not in line:
            raise SystemExit(
                f"[error] {path.relative_to(REPO_ROOT).as_posix()} has an invalid frontmatter line: {line}"
            )
        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if not value:
            frontmatter[key] = []
            current_key = key
            continue
        frontmatter[key] = parse_scalar(value)
        current_key = key

    raise SystemExit(
        f"[error] {path.relative_to(REPO_ROOT).as_posix()} is missing the closing YAML frontmatter boundary"
    )


def authored_bundle_paths() -> list[Path]:
    if not PLAYBOOK_ROOT.exists():
        return []
    return sorted(path for path in PLAYBOOK_ROOT.rglob("PLAYBOOK.md") if path.is_file())


def build_federation_surface(frontmatter: dict[str, object]) -> dict[str, object]:
    surface: dict[str, object] = {
        "surface_type": "playbook_federation_surface",
        "playbook_id": frontmatter["id"],
        "name": frontmatter["name"],
        "participating_agents": frontmatter["participating_agents"],
        "memory_posture": frontmatter["memory_posture"],
        "required_skills": frontmatter["required_skills"],
        "memo_contract_refs": frontmatter["memo_contract_refs"],
        "memo_writeback_targets": frontmatter["memo_writeback_targets"],
    }
    if "eval_anchors" in frontmatter:
        surface["eval_anchors"] = frontmatter["eval_anchors"]
    for field_name in OPTIONAL_MEMO_SPEC_FIELDS:
        if field_name in frontmatter:
            surface[field_name] = frontmatter[field_name]
    return surface


def build_federation_surfaces() -> list[dict[str, object]]:
    playbooks_by_id: dict[str, dict[str, object]] = {}
    for bundle_path in authored_bundle_paths():
        frontmatter = parse_frontmatter(read_text(bundle_path), bundle_path)
        playbook_id = frontmatter.get("id")
        if isinstance(playbook_id, str):
            playbooks_by_id[playbook_id] = frontmatter

    surfaces: list[dict[str, object]] = []
    for playbook_id in FEDERATION_PLAYBOOK_IDS:
        if playbook_id not in playbooks_by_id:
            raise SystemExit(f"[error] authored bundles are missing required federation target: {playbook_id}")
        surfaces.append(build_federation_surface(playbooks_by_id[playbook_id]))
    return surfaces


def write_output(surfaces: list[dict[str, object]]) -> None:
    OUTPUT_PATH.write_text(json.dumps(surfaces, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate derived playbook federation surfaces.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the generated output without writing files.",
    )
    args = parser.parse_args(argv)

    surfaces = build_federation_surfaces()
    rendered = json.dumps(surfaces, indent=2) + "\n"

    if args.check:
        try:
            existing = OUTPUT_PATH.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"[error] missing required file: {OUTPUT_PATH.relative_to(REPO_ROOT).as_posix()}", file=sys.stderr)
            return 1
        if existing != rendered:
            print(
                "[error] generated/playbook_federation_surfaces.min.json is out of date; "
                "run scripts/generate_playbook_federation_surfaces.py",
                file=sys.stderr,
            )
            return 1
    else:
        write_output(surfaces)

    print("[ok] derived playbook federation surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
