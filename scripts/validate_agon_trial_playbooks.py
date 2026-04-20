#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CFG = ROOT / "config" / "agon_trial_playbooks.seed.json"
REG = ROOT / "generated" / "agon_trial_playbook_registry.min.json"
KNOWN_LAWFUL_MOVES = {
    "assert_position", "challenge_claim", "request_evidence", "offer_evidence_reference",
    "probe_trace", "deny_trace_closure", "mark_contradiction", "localize_contradiction",
    "deny_closure", "request_closure_review", "request_summon_intent", "request_witness",
    "revise_position", "stand_fast", "concede", "defer_with_cost",
    "flag_scope_breach", "escalate_to_agon_gate",
}
KNOWN_GATE_TRIGGERS = {
    "contested_closure", "open_material_contradiction", "broken_trace_or_trace_gap",
    "evidence_floor_collapse", "repeated_failure_without_delta", "assistant_scope_breach",
    "assistant_anti_drift_alarm", "model_divergence_above_threshold", "canonical_risk",
    "summon_intent_requires_review", "novelty_above_service_threshold", "actor_kind_mismatch",
}
REQUIRED_FORBIDDEN = {
    "contestant_seat", "judge_seat", "closer_jurisdiction", "summon_initiator_jurisdiction",
    "scar_writer", "rank_mutator", "tos_promoter",
}
STOP_LINE_PARTS = ["no_arena_session_creation", "no_verdict_authority", "no_scar_write", "no_retention_schedule"]

def fail(msg: str) -> int:
    print(f"agon trial playbook validation failed: {msg}", file=sys.stderr)
    return 1

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_frontmatter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    _, remainder = text.split("---\n", 1)
    frontmatter_text, separator, body = remainder.partition("\n---\n")
    if not separator:
        return {}, text
    frontmatter = yaml.safe_load(frontmatter_text) or {}
    if not isinstance(frontmatter, dict):
        raise ValueError(f"{path} frontmatter must decode to a mapping")
    return frontmatter, body

def optional_neighbor_note() -> None:
    workspace = ROOT.parent
    center_moves = workspace / "Agents-of-Abyss" / "generated" / "agon_lawful_move_registry.min.json"
    routing_gate = workspace / "aoa-routing" / "generated" / "agon_gate_routing_registry.min.json"
    missing = []
    if not center_moves.exists():
        missing.append("Agents-of-Abyss/generated/agon_lawful_move_registry.min.json")
    if not routing_gate.exists():
        missing.append("aoa-routing/generated/agon_gate_routing_registry.min.json")
    if missing:
        print("optional workspace neighbors not found; using embedded Wave III/V vocabularies:")
        for item in missing:
            print(f"  - {item}")

def main() -> int:
    builder = ROOT / "scripts" / "build_agon_trial_playbook_registry.py"
    result = subprocess.run([sys.executable, str(builder), "--check"], cwd=ROOT)
    if result.returncode != 0:
        return result.returncode
    optional_neighbor_note()
    cfg = load(CFG)
    reg = load(REG)
    if cfg.get("wave") != "VI" or reg.get("wave") != "VI":
        return fail("wave must be VI")
    if cfg.get("live_protocol") is not False or reg.get("live_protocol") is not False:
        return fail("live_protocol must be false")
    if cfg.get("runtime_effect") != "none" or reg.get("runtime_effect") != "none":
        return fail("runtime_effect must be none")
    for required in STOP_LINE_PARTS:
        if required not in set(cfg.get("stop_lines", [])):
            return fail(f"missing stop-line {required}")
    forbidden = set(cfg.get("assistant_forbidden_authority", []))
    if not REQUIRED_FORBIDDEN.issubset(forbidden):
        return fail(f"assistant forbidden authority incomplete: {sorted(REQUIRED_FORBIDDEN - forbidden)}")
    trials = cfg.get("trials", [])
    if len(trials) < 5:
        return fail("expected at least five trials")
    ids = [t.get("id") for t in trials]
    slugs = [t.get("slug") for t in trials]
    trial_ids = [t.get("trial_id") for t in trials]
    if len(ids) != len(set(ids)):
        return fail("duplicate playbook ids")
    if len(slugs) != len(set(slugs)):
        return fail("duplicate slugs")
    if len(trial_ids) != len(set(trial_ids)):
        return fail("duplicate trial_ids")
    for t in trials:
        if t.get("status") != "seeded_pre_protocol_trial_playbook":
            return fail(f"bad status for {t.get('id')}")
        if t.get("live_protocol") is not False:
            return fail(f"live_protocol must be false for {t.get('id')}")
        if t.get("runtime_effect") != "none":
            return fail(f"runtime_effect must be none for {t.get('id')}")
        if not set(t.get("lawful_moves", [])).issubset(KNOWN_LAWFUL_MOVES):
            return fail(f"unknown lawful move in {t.get('id')}: {sorted(set(t.get('lawful_moves', [])) - KNOWN_LAWFUL_MOVES)}")
        if not set(t.get("gate_triggers", [])).issubset(KNOWN_GATE_TRIGGERS):
            return fail(f"unknown gate trigger in {t.get('id')}: {sorted(set(t.get('gate_triggers', [])) - KNOWN_GATE_TRIGGERS)}")
        if not t.get("terminal_pre_protocol_outcomes"):
            return fail(f"missing terminal_pre_protocol_outcomes for {t.get('id')}")
        pb = ROOT / "playbooks" / t["slug"] / "PLAYBOOK.md"
        if not pb.exists():
            return fail(f"missing authored playbook bundle: {pb}")
        try:
            frontmatter, body = load_frontmatter(pb)
        except ValueError as exc:
            return fail(str(exc))
        if frontmatter.get("agon_pre_protocol") is not True:
            return fail(f"{pb} frontmatter agon_pre_protocol must be true")
        if frontmatter.get("live_protocol") is not False:
            return fail(f"{pb} frontmatter live_protocol must be false")
        if frontmatter.get("runtime_effect") != "none":
            return fail(f"{pb} frontmatter runtime_effect must be none")
        if "## Terminal pre-protocol outcomes" not in body:
            return fail(f"{pb} missing ## Terminal pre-protocol outcomes")
    if reg.get("trial_count") != len(trials):
        return fail("registry trial_count mismatch")
    print("agon trial playbook validation passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
