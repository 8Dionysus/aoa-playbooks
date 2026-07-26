#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

COMMANDS = [
    ("validate root design", [sys.executable, "scripts/validate_root_design.py"]),
    ("validate mechanics skeleton", [sys.executable, "scripts/validate_mechanics_skeleton.py"]),
    ("validate activation mechanic", [sys.executable, "mechanics/activation/scripts/validate_activation_package.py"]),
    (
        "validate scenario-composition mechanic",
        [sys.executable, "mechanics/scenario-composition/scripts/validate_scenario_composition_package.py"],
    ),
    (
        "validate federation-closure mechanic",
        [sys.executable, "mechanics/federation-closure/scripts/validate_federation_closure_package.py"],
    ),
    ("validate review-gate mechanic", [sys.executable, "mechanics/review-gate/scripts/validate_review_gate_package.py"]),
    (
        "validate real-run-harvest mechanic",
        [sys.executable, "mechanics/real-run-harvest/scripts/validate_real_run_harvest_package.py"],
    ),
    (
        "validate antifragility mechanic",
        [sys.executable, "mechanics/antifragility/scripts/validate_antifragility_package.py"],
    ),
    (
        "validate boundary-bridge mechanic",
        [sys.executable, "mechanics/boundary-bridge/scripts/validate_boundary_bridge_package.py"],
    ),
    ("validate agon mechanic", [sys.executable, "mechanics/agon/scripts/validate_agon_package.py"]),
    ("validate recurrence mechanic", [sys.executable, "mechanics/recurrence/scripts/validate_recurrence_package.py"]),
    ("validate checkpoint mechanic", [sys.executable, "mechanics/checkpoint/scripts/validate_checkpoint_package.py"]),
    ("validate experience mechanic", [sys.executable, "mechanics/experience/scripts/validate_experience_package.py"]),
    (
        "validate release-support mechanic",
        [sys.executable, "mechanics/release-support/scripts/validate_release_support_package.py"],
    ),
    ("validate questbook mechanic", [sys.executable, "mechanics/questbook/scripts/validate_questbook_package.py"]),
    ("validate rpg mechanic", [sys.executable, "mechanics/rpg/scripts/validate_rpg_package.py"]),
    ("validate titan mechanic", [sys.executable, "mechanics/titan/scripts/validate_titan_package.py"]),
    (
        "validate portfolio-governance mechanic",
        [sys.executable, "mechanics/portfolio-governance/scripts/validate_portfolio_governance_package.py"],
    ),
    ("check decision indexes", [sys.executable, "scripts/generate_decision_indexes.py", "--check"]),
    ("check agon trial playbooks", [sys.executable, "mechanics/agon/parts/trial-playbooks/scripts/build_agon_trial_playbook_registry.py", "--check"]),
    ("validate agon trial playbooks", [sys.executable, "mechanics/agon/parts/trial-playbooks/scripts/validate_agon_trial_playbooks.py"]),
    (
        "check agon trial-kernel bindings",
        [sys.executable, "mechanics/agon/parts/trial-kernel-bindings/scripts/build_agon_trial_kernel_binding_registry.py", "--check"],
    ),
    ("validate agon trial-kernel bindings", [sys.executable, "mechanics/agon/parts/trial-kernel-bindings/scripts/validate_agon_trial_kernel_bindings.py"]),
    (
        "check agon campaign playbooks",
        [sys.executable, "mechanics/agon/parts/campaign-playbooks/scripts/build_agon_campaign_playbook_registry.py", "--check"],
    ),
    ("validate agon campaign playbooks", [sys.executable, "mechanics/agon/parts/campaign-playbooks/scripts/validate_agon_campaign_playbook_registry.py"]),
    ("check activation surfaces", [sys.executable, "mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py", "--check"]),
    ("check federation surfaces", [sys.executable, "mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py", "--check"]),
    ("check review status", [sys.executable, "mechanics/review-gate/parts/review-status/scripts/generate_playbook_review_status.py", "--check"]),
    ("check review packet contracts", [sys.executable, "mechanics/review-gate/parts/review-packet-contracts/scripts/generate_playbook_review_packet_contracts.py", "--check"]),
    ("check review intake", [sys.executable, "mechanics/review-gate/parts/review-intake/scripts/generate_playbook_review_intake.py", "--check"]),
    ("check composition surfaces", [sys.executable, "mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py", "--check"]),
    ("check plan contours", [sys.executable, "mechanics/scenario-composition/parts/plan-contours/scripts/generate_playbook_plan_contours.py", "--check"]),
    ("check phase alpha surfaces", [sys.executable, "mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py", "--check"]),
    ("validate owner-local stats port", [sys.executable, "scripts/validate_local_stats_port.py"]),
    ("validate OS Abyss playbook artifact bundle", [sys.executable, "scripts/validate_abyss_machine_playbook_bundle.py"]),
    ("validate playbooks", [sys.executable, "scripts/validate_playbooks.py"]),
    ("run tests", [sys.executable, "-m", "pytest", "-q", "tests"]),
]


def run_step(label: str, command: list[str]) -> int:
    print(f"[run] {label}: {subprocess.list2cmdline(command)}", flush=True)
    completed = subprocess.run(command, cwd=REPO_ROOT, env=os.environ.copy(), check=False)
    if completed.returncode != 0:
        print(f"[error] {label} failed with exit code {completed.returncode}", flush=True)
        return completed.returncode
    print(f"[ok] {label}", flush=True)
    return 0


def main() -> int:
    for label, command in COMMANDS:
        exit_code = run_step(label, command)
        if exit_code != 0:
            return exit_code
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
