#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "config" / "agon_trial_playbooks.seed.json"
OUT = ROOT / "generated" / "agon_trial_playbook_registry.min.json"

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def build():
    data = load_json(SRC)
    trials = []
    for t in data.get("trials", []):
        trials.append({
            "id": t["id"],
            "trial_id": t["trial_id"],
            "slug": t["slug"],
            "name": t["display_name"],
            "status": t["status"],
            "live_protocol": t["live_protocol"],
            "runtime_effect": t["runtime_effect"],
            "playbook_path": f"playbooks/{t['slug']}/PLAYBOOK.md",
            "gate_triggers": t["gate_triggers"],
            "lawful_moves": t["lawful_moves"],
            "participating_agents": t["participating_agents"],
            "assistant_support": t["assistant_support"],
            "terminal_pre_protocol_outcomes": t["terminal_pre_protocol_outcomes"],
        })
    return {
        "schema_version": data["schema_version"],
        "wave": data["wave"],
        "repo": data["repo"],
        "status": data["status"],
        "live_protocol": data["live_protocol"],
        "runtime_effect": data["runtime_effect"],
        "generated_by": "scripts/build_agon_trial_playbook_registry.py",
        "source": data["source"],
        "trial_count": len(trials),
        "stop_lines": data["stop_lines"],
        "assistant_forbidden_authority": data["assistant_forbidden_authority"],
        "trials": trials,
    }

def dump_min(data):
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    built = dump_min(build())
    if args.check:
        if not OUT.exists():
            print(f"missing generated file: {OUT}", file=sys.stderr)
            return 1
        if OUT.read_text(encoding="utf-8") != built:
            print(f"generated drift: {OUT}", file=sys.stderr)
            return 1
        print("agon trial playbook registry is up to date")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(built, encoding="utf-8")
    print(f"wrote {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
