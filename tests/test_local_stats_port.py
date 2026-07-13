from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_STATUS_PATH = REPO_ROOT / "generated" / "playbook_review_status.min.json"
PACKET_PATH = REPO_ROOT / "stats" / "packets" / (
    "reviewed-run-reference-coverage-ratio.reference.json"
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def review_status_census() -> tuple[int, int]:
    entries = load_json(REVIEW_STATUS_PATH)["playbooks"]
    covered = sum(entry["reviewed_run_count"] > 0 for entry in entries)
    return covered, len(entries)


def assert_packet_matches_owner_review_status(packet: dict) -> None:
    covered, population_size = review_status_census()

    assert packet["population"]["size"] == population_size
    assert packet["sample"]["size"] == population_size
    assert packet["value"]["numerator"] == covered, (
        "packet numerator must match entries with referenced reviewed runs"
    )
    assert packet["value"]["denominator"] == population_size
    assert packet["value"]["number"] == covered / population_size
    assert packet["progress"] == {
        "state": "terminal",
        "completed": population_size,
        "total": population_size,
    }


def test_reference_ratio_matches_current_review_status_cohort() -> None:
    packet = load_json(PACKET_PATH)
    covered, population_size = review_status_census()

    assert population_size == 8
    assert covered == 6
    assert_packet_matches_owner_review_status(packet)


def test_false_all_covered_packet_is_rejected() -> None:
    false_packet = deepcopy(load_json(PACKET_PATH))
    false_packet["value"]["numerator"] = false_packet["value"]["denominator"]
    false_packet["value"]["number"] = 1.0

    with pytest.raises(
        AssertionError,
        match="packet numerator must match entries with referenced reviewed runs",
    ):
        assert_packet_matches_owner_review_status(false_packet)
