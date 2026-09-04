#!/usr/bin/env python3
"""Validate the review-gate mechanic package."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "review-gate"

BUILDERS = {
    "review-status": {
        "wrapper": REPO_ROOT / "scripts" / "generate_playbook_review_status.py",
        "impl": PACKAGE_ROOT
        / "parts"
        / "review-status"
        / "scripts"
        / "generate_playbook_review_status.py",
        "module": "review_gate_status_builder",
        "functions": (("build_review_status_payload", "generated/playbook_review_status.min.json"),),
    },
    "review-packet-contracts": {
        "wrapper": REPO_ROOT / "scripts" / "generate_playbook_review_packet_contracts.py",
        "impl": PACKAGE_ROOT
        / "parts"
        / "review-packet-contracts"
        / "scripts"
        / "generate_playbook_review_packet_contracts.py",
        "module": "review_gate_packet_contracts_builder",
        "functions": (
            (
                "build_review_packet_contracts_payload",
                "generated/playbook_review_packet_contracts.min.json",
            ),
        ),
    },
    "review-intake": {
        "wrapper": REPO_ROOT / "scripts" / "generate_playbook_review_intake.py",
        "impl": PACKAGE_ROOT
        / "parts"
        / "review-intake"
        / "scripts"
        / "generate_playbook_review_intake.py",
        "module": "review_gate_intake_builder",
        "functions": (("build_review_intake_payload", "generated/playbook_review_intake.min.json"),),
    },
    "landing-governance": {
        "wrapper": REPO_ROOT / "scripts" / "generate_playbook_landing_governance.py",
        "impl": PACKAGE_ROOT
        / "parts"
        / "landing-governance"
        / "scripts"
        / "generate_playbook_landing_governance.py",
        "module": "review_gate_landing_governance_builder",
        "functions": (
            (
                "build_playbook_landing_governance_payload",
                "generated/playbook_landing_governance.min.json",
            ),
        ),
    },
    "phase-alpha-readiness": {
        "wrapper": REPO_ROOT / "scripts" / "generate_phase_alpha_surfaces.py",
        "impl": PACKAGE_ROOT
        / "parts"
        / "phase-alpha-readiness"
        / "scripts"
        / "generate_phase_alpha_surfaces.py",
        "module": "review_gate_phase_alpha_builder",
        "functions": (
            ("build_phase_alpha_review_packets_payload", "generated/phase_alpha_review_packets.min.json"),
            ("build_phase_alpha_run_matrix_payload", "generated/phase_alpha_run_matrix.min.json"),
        ),
    },
}

REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "PARTS.md",
    "PROVENANCE.md",
    "parts/AGENTS.md",
    "parts/README.md",
    "parts/review-status/README.md",
    "parts/review-packet-contracts/README.md",
    "parts/review-intake/README.md",
    "parts/landing-governance/README.md",
    "parts/phase-alpha-readiness/README.md",
    "scripts/validate_review_gate_package.py",
)

REQUIRED_TEXT = {
    "README.md": (
        "## Mechanic card",
        "class | local",
        "generated/playbook_review_status.min.json",
        "generated/phase_alpha_review_packets.min.json",
    ),
    "PARTS.md": (
        "review-status",
        "review-packet-contracts",
        "phase-alpha-readiness",
        "Boundary payloads",
    ),
    "PROVENANCE.md": (
        "mechanics/review-gate/parts/review-status/scripts/generate_playbook_review_status.py",
        "mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py",
        "accepted-input",
        "implementation moved into review-gate package",
    ),
}


def load_impl(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load review-gate builder from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    issues: list[str] = []
    package_root = repo_root / "mechanics" / "review-gate"

    for relative_path in REQUIRED_FILES:
        if not (package_root / relative_path).is_file():
            issues.append(f"mechanics/review-gate/{relative_path}: missing required file")

    for relative_path, tokens in REQUIRED_TEXT.items():
        path = package_root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                issues.append(f"mechanics/review-gate/{relative_path}: missing token {token!r}")

    for part_name, metadata in BUILDERS.items():
        wrapper = metadata["wrapper"]
        impl_path = metadata["impl"]
        if not isinstance(wrapper, Path) or not wrapper.is_file():
            issues.append(f"{wrapper.relative_to(repo_root).as_posix()}: missing compatibility wrapper")
            continue
        if not isinstance(impl_path, Path) or not impl_path.is_file():
            issues.append(f"{impl_path.relative_to(repo_root).as_posix()}: missing builder implementation")
            continue
        wrapper_text = wrapper.read_text(encoding="utf-8")
        if "mechanics" not in wrapper_text or "review-gate" not in wrapper_text or part_name not in wrapper_text:
            issues.append(f"{wrapper.relative_to(repo_root).as_posix()}: wrapper must route to review-gate/{part_name}")

        try:
            module = load_impl(str(metadata["module"]), impl_path)
            functions = metadata["functions"]
            if not isinstance(functions, tuple):
                raise RuntimeError("builder metadata functions must be a tuple")
            for function_name, output_relative_path in functions:
                built = getattr(module, function_name)()
                output_path = repo_root / output_relative_path
                current = json.loads(output_path.read_text(encoding="utf-8"))
                if current != built:
                    issues.append(f"{output_relative_path} is out of date")
        except Exception as exc:  # pragma: no cover - reported as validator issue
            issues.append(f"{part_name} builder validation failed: {exc}")

    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)

    issues = validate(args.repo_root.resolve())
    if issues:
        print("Review-gate package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Review-gate package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
