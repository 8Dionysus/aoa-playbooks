#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "generated" / "playbook_registry.min.json"
REAL_RUN_SUMMARY_DIR = REPO_ROOT / "docs" / "real-runs"
GATE_REVIEW_DIR = REPO_ROOT / "docs" / "gate-reviews"
OUTPUT_PATH = REPO_ROOT / "generated" / "playbook_review_status.min.json"

REQUIRED_REAL_RUN_SUMMARY_SECTIONS = (
    "Run Header",
    "Entry Signal",
    "Boundary Summary",
    "Required Artifacts",
    "Closure Class",
    "Follow-On Route",
    "Composition Signals",
    "Residual Risk",
    "Evidence Links",
)
REQUIRED_GATE_REVIEW_SECTIONS = (
    "Gate Header",
    "Minimum Evidence Threshold",
    "Latest Reviewed Run",
    "Dual Signal Check",
    "Current Verdict",
    "Next Trigger",
)
ALLOWED_GATE_VERDICT_TOKENS = ("hold", "ready-for-composition-review", "composition-landed")
REAL_RUN_SUMMARY_FILENAME_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}\.([a-z0-9-]+)(?:\.([a-z0-9-]+))?\.md$"
)
REVIEWED_RUN_REF_RE = re.compile(
    r"docs/real-runs/(\d{4}-\d{2}-\d{2}\.[a-z0-9-]+(?:\.[a-z0-9-]+)?\.md)"
)
PLAYBOOK_ID_RE = re.compile(r"\bAOA-P-\d{4}\b")


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


def markdown_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current_heading: str | None = None
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            if current_heading is not None:
                sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = line[3:].strip()
            current_lines = []
            continue
        if current_heading is not None:
            current_lines.append(line)
    if current_heading is not None:
        sections[current_heading] = "\n".join(current_lines).strip()
    return sections


def extract_list_items(section_text: str) -> list[str]:
    items: list[str] = []
    for raw_line in section_text.splitlines():
        line = raw_line.strip()
        if line.startswith("- "):
            items.append(line[2:].strip())
            continue
        if ". " in line:
            prefix, rest = line.split(". ", 1)
            if prefix.isdigit() and rest.strip():
                items.append(rest.strip())
    return items


def collapse_text(text: str) -> str:
    return " ".join(text.replace("`", "").split())


def extract_reviewed_run_refs(section_text: str) -> list[str]:
    refs: list[str] = []
    seen: set[str] = set()
    for match in REVIEWED_RUN_REF_RE.finditer(section_text):
        ref = f"docs/real-runs/{match.group(1)}"
        if ref not in seen:
            refs.append(ref)
            seen.add(ref)
    return refs


def parse_playbook_id(section_text: str, *, location: str) -> str:
    match = PLAYBOOK_ID_RE.search(section_text)
    if match is None:
        raise SystemExit(f"[error] {location} must mention an owning playbook id")
    return match.group(0)


def parse_gate_verdict(section_text: str, *, location: str) -> str:
    matches = [token for token in ALLOWED_GATE_VERDICT_TOKENS if token in section_text]
    if len(matches) != 1:
        raise SystemExit(
            f"[error] {location} must expose exactly one gate verdict token: "
            + ", ".join(ALLOWED_GATE_VERDICT_TOKENS)
        )
    return matches[0]


def load_registry_by_id() -> dict[str, dict[str, object]]:
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


def load_reviewed_runs() -> tuple[dict[str, list[str]], dict[str, str]]:
    reviewed_run_refs_by_playbook: dict[str, list[str]] = {}
    slug_by_playbook_id: dict[str, str] = {}

    for summary_path in sorted(REAL_RUN_SUMMARY_DIR.glob("*.md")):
        if summary_path.name == "README.md":
            continue
        location = summary_path.relative_to(REPO_ROOT).as_posix()
        match = REAL_RUN_SUMMARY_FILENAME_RE.match(summary_path.name)
        if match is None:
            raise SystemExit(f"[error] {location} must match YYYY-MM-DD.<playbook-slug>.md")
        slug = match.group(1)
        text = read_text(summary_path)
        sections = markdown_sections(text)
        missing_sections = [
            section_name for section_name in REQUIRED_REAL_RUN_SUMMARY_SECTIONS if section_name not in sections
        ]
        if missing_sections:
            raise SystemExit(
                f"[error] {location} is missing required reviewed-summary sections: "
                + ", ".join(missing_sections)
            )
        playbook_id = parse_playbook_id(sections["Run Header"], location=location)
        previous_slug = slug_by_playbook_id.get(playbook_id)
        if previous_slug is not None and previous_slug != slug:
            raise SystemExit(
                f"[error] {location} disagrees with an existing slug for {playbook_id}: "
                f"{previous_slug} vs {slug}"
            )
        slug_by_playbook_id[playbook_id] = slug
        reviewed_run_refs_by_playbook.setdefault(playbook_id, []).append(location)

    return reviewed_run_refs_by_playbook, slug_by_playbook_id


def build_review_status_payload() -> dict[str, object]:
    registry_by_id = load_registry_by_id()
    reviewed_run_refs_by_playbook, slug_by_playbook_id = load_reviewed_runs()

    entries: list[dict[str, object]] = []
    for gate_path in sorted(GATE_REVIEW_DIR.glob("*.md")):
        location = gate_path.relative_to(REPO_ROOT).as_posix()
        text = read_text(gate_path)
        sections = markdown_sections(text)
        missing_sections = [
            section_name for section_name in REQUIRED_GATE_REVIEW_SECTIONS if section_name not in sections
        ]
        if missing_sections:
            raise SystemExit(
                f"[error] {location} is missing required gate-review sections: "
                + ", ".join(missing_sections)
            )

        playbook_id = parse_playbook_id(sections["Gate Header"], location=location)
        if playbook_id not in registry_by_id:
            raise SystemExit(f"[error] {location} references unknown playbook id: {playbook_id}")
        registry_entry = registry_by_id[playbook_id]

        minimum_threshold_items = extract_list_items(sections["Minimum Evidence Threshold"])
        if len(minimum_threshold_items) != 1:
            raise SystemExit(
                f"[error] {location} must list exactly one minimum evidence threshold bullet"
            )

        dual_signal_items = extract_list_items(sections["Dual Signal Check"])
        if len(dual_signal_items) < 2:
            raise SystemExit(
                f"[error] {location} must list at least two dual-signal bullets"
            )

        slug = gate_path.stem
        existing_slug = slug_by_playbook_id.get(playbook_id)
        if existing_slug is not None and existing_slug != slug:
            raise SystemExit(
                f"[error] {location} slug '{slug}' does not match reviewed-summary slug '{existing_slug}' "
                f"for {playbook_id}"
            )

        referenced_run_refs = extract_reviewed_run_refs(sections["Latest Reviewed Run"])
        actual_run_refs = reviewed_run_refs_by_playbook.get(playbook_id, [])
        missing_refs = [ref for ref in actual_run_refs if ref not in referenced_run_refs]
        unexpected_refs = [ref for ref in referenced_run_refs if ref not in actual_run_refs]
        if missing_refs or unexpected_refs:
            details: list[str] = []
            if missing_refs:
                details.append(
                    "missing reviewed runs: " + ", ".join(missing_refs)
                )
            if unexpected_refs:
                details.append(
                    "unexpected reviewed runs: " + ", ".join(unexpected_refs)
                )
            raise SystemExit(
                f"[error] {location} must reference exactly the reviewed runs listed under docs/real-runs/: "
                + "; ".join(details)
            )

        entries.append(
            {
                "playbook_id": playbook_id,
                "playbook_name": registry_entry["name"],
                "scenario": registry_entry["scenario"],
                "gate_review_ref": location,
                "reviewed_run_count": len(referenced_run_refs),
                "reviewed_run_refs": referenced_run_refs,
                "latest_reviewed_run_ref": referenced_run_refs[-1] if referenced_run_refs else None,
                "minimum_evidence_threshold": minimum_threshold_items[0],
                "gate_verdict": parse_gate_verdict(sections["Current Verdict"], location=location),
                "next_trigger": collapse_text(sections["Next Trigger"]),
                "composition_signal_summary": {
                    "failure_or_follow_up": collapse_text(dual_signal_items[0]),
                    "adjunct_candidate": collapse_text(dual_signal_items[1]),
                },
            }
        )

    entries.sort(key=lambda item: item["playbook_id"])
    return {
        "schema_version": 1,
        "layer": "aoa-playbooks",
        "source_of_truth": {
            "reviewed_runs_dir": "docs/real-runs",
            "gate_reviews_dir": "docs/gate-reviews",
        },
        "playbooks": entries,
    }


def write_output(payload: dict[str, object]) -> None:
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate compact playbook review-status surfaces.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the generated output without writing files.",
    )
    args = parser.parse_args(argv)

    payload = build_review_status_payload()
    rendered = json.dumps(payload, indent=2) + "\n"

    if args.check:
        try:
            existing = OUTPUT_PATH.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"[error] missing required file: {OUTPUT_PATH.relative_to(REPO_ROOT).as_posix()}", file=sys.stderr)
            return 1
        if existing != rendered:
            print(
                "[error] generated/playbook_review_status.min.json is out of date; "
                "run scripts/generate_playbook_review_status.py",
                file=sys.stderr,
            )
            return 1
    else:
        write_output(payload)

    print("[ok] derived playbook review status surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
