#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

COMMANDS = [
    ("check activation surfaces", [sys.executable, "scripts/generate_playbook_activation_surfaces.py", "--check"]),
    ("check federation surfaces", [sys.executable, "scripts/generate_playbook_federation_surfaces.py", "--check"]),
    ("check review status", [sys.executable, "scripts/generate_playbook_review_status.py", "--check"]),
    ("check review packet contracts", [sys.executable, "scripts/generate_playbook_review_packet_contracts.py", "--check"]),
    ("check review intake", [sys.executable, "scripts/generate_playbook_review_intake.py", "--check"]),
    ("check composition surfaces", [sys.executable, "scripts/generate_playbook_composition_surfaces.py", "--check"]),
    ("check phase alpha surfaces", [sys.executable, "scripts/generate_phase_alpha_surfaces.py", "--check"]),
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
