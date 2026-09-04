#!/usr/bin/env python3
"""Validate the Agon mechanic package."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "mechanics" / "agon"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.playbook_source_home import playbook_path_for_name

REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "PARTS.md",
    "PROVENANCE.md",
    "parts/AGENTS.md",
    "parts/README.md",
    "parts/trial-playbooks/README.md",
    "parts/trial-kernel-bindings/README.md",
    "parts/campaign-playbooks/README.md",
    "parts/adoption/README.md",
    "parts/recurrence-adapter/README.md",
    "parts/trial-playbooks/config/agon_trial_playbooks.seed.json",
    "parts/trial-kernel-bindings/config/agon_trial_kernel_bindings.seed.json",
    "parts/campaign-playbooks/config/agon_campaign_playbooks.seed.json",
    "parts/trial-playbooks/scripts/build_agon_trial_playbook_registry.py",
    "parts/trial-playbooks/scripts/validate_agon_trial_playbooks.py",
    "parts/trial-kernel-bindings/scripts/build_agon_trial_kernel_binding_registry.py",
    "parts/trial-kernel-bindings/scripts/validate_agon_trial_kernel_bindings.py",
    "parts/campaign-playbooks/scripts/build_agon_campaign_playbook_registry.py",
    "parts/campaign-playbooks/scripts/validate_agon_campaign_playbook_registry.py",
    "scripts/validate_agon_package.py",
)

REQUIRED_TEXT = {
    "README.md": (
        "## Mechanic card",
        "class | head-fed/local",
        "trial-playbooks",
        "campaign-playbooks",
        "pre-protocol",
    ),
    "PARTS.md": (
        "trial-playbooks",
        "trial-kernel-bindings",
        "campaign-playbooks",
        "adoption",
        "recurrence-adapter",
    ),
    "PROVENANCE.md": (
        "docs/AGON_*.md",
        "config/agon_*.seed.json",
        "scripts/*agon*.py",
        "root script paths remain compatibility command wrappers",
    ),
    "legacy/INDEX.md": (
        "Former root family",
        "mechanics/agon/parts/trial-playbooks/docs/",
        "mechanics/agon/parts/campaign-playbooks/docs/",
    ),
}

ROOT_WRAPPERS = (
    ("scripts/build_agon_trial_playbook_registry.py", "trial-playbooks"),
    ("scripts/validate_agon_trial_playbooks.py", "trial-playbooks"),
    ("scripts/build_agon_trial_kernel_binding_registry.py", "trial-kernel-bindings"),
    ("scripts/validate_agon_trial_kernel_bindings.py", "trial-kernel-bindings"),
    ("scripts/build_agon_campaign_playbook_registry.py", "campaign-playbooks"),
    ("scripts/validate_agon_campaign_playbook_registry.py", "campaign-playbooks"),
)

OLD_ROOT_PAYLOADS = (
    "docs/AGON_MECHANICAL_TRIAL_MODEL.md",
    "docs/AGON_MECHANICAL_TRIAL_REHEARSAL_BOUNDARY.md",
    "docs/AGON_TRIAL_ASSISTANT_SERVICE_BOUNDARY.md",
    "docs/AGON_TRIAL_CHOREOGRAPHY_BOUNDARY.md",
    "docs/AGON_TRIAL_OWNER_HANDOFFS.md",
    "docs/AGON_TRIAL_PLAYBOOKS.md",
    "docs/AGON_TRIAL_KERNEL_BINDINGS.md",
    "docs/AGON_CAMPAIGN_PLAYBOOKS.md",
    "docs/AGON_CAMPAIGN_CHOREOGRAPHY_BOUNDARY.md",
    "docs/AGON_RECURRENCE_ADAPTER.md",
    "docs/AGONIC_TRIAL_ADOPTION_PLAYBOOK.md",
    "config/agon_trial_playbooks.seed.json",
    "config/agon_trial_kernel_bindings.seed.json",
    "config/agon_campaign_playbooks.seed.json",
    "schemas/agon-trial-playbook.schema.json",
    "schemas/agon-trial-playbook-registry.schema.json",
    "schemas/agon-trial-kernel-binding.schema.json",
    "schemas/agon-trial-kernel-binding-registry.schema.json",
    "schemas/agon-campaign-playbook.schema.json",
    "schemas/agon-campaign-playbook-registry.schema.json",
    "schemas/agonic_trial_adoption_run_v1.json",
    "examples/agon_trial_playbook.example.json",
    "examples/agon_trial_kernel_binding.example.json",
    "examples/agon_campaign_playbook.example.json",
    "examples/agonic_trial_adoption_run.example.json",
    "manifests/recurrence/component.agon.trial-playbook-surfaces.json",
    "manifests/recurrence/hooks/component.agon.trial-playbook-surfaces.hooks.json",
    "manifests/recurrence/component.agon.trial-kernel-bindings.json",
    "manifests/recurrence/hooks/component.agon.trial-kernel-bindings.hooks.json",
    "manifests/recurrence/component.agon.wave16.aoa_playbooks.json",
    "manifests/recurrence/hooks/component.agon.wave16.aoa_playbooks.hooks.json",
)

COMMANDS = (
    ("build trial playbook registry", [sys.executable, "mechanics/agon/parts/trial-playbooks/scripts/build_agon_trial_playbook_registry.py", "--check"]),
    ("validate trial playbooks", [sys.executable, "mechanics/agon/parts/trial-playbooks/scripts/validate_agon_trial_playbooks.py"]),
    (
        "build trial-kernel binding registry",
        [sys.executable, "mechanics/agon/parts/trial-kernel-bindings/scripts/build_agon_trial_kernel_binding_registry.py", "--check"],
    ),
    ("validate trial-kernel bindings", [sys.executable, "mechanics/agon/parts/trial-kernel-bindings/scripts/validate_agon_trial_kernel_bindings.py"]),
    (
        "build campaign playbook registry",
        [sys.executable, "mechanics/agon/parts/campaign-playbooks/scripts/build_agon_campaign_playbook_registry.py", "--check"],
    ),
    ("validate campaign playbooks", [sys.executable, "mechanics/agon/parts/campaign-playbooks/scripts/validate_agon_campaign_playbook_registry.py"]),
)


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def display(path: Path, repo_root: Path = REPO_ROOT) -> str:
    return path.relative_to(repo_root).as_posix()


def validate_json_examples(
    schema_path: Path,
    example_paths: tuple[Path, ...],
    issues: list[str],
    *,
    repo_root: Path,
) -> None:
    try:
        schema = read_json(schema_path)
    except Exception as exc:
        issues.append(f"{display(schema_path, repo_root)}: invalid JSON schema: {exc}")
        return
    if not isinstance(schema, dict):
        issues.append(f"{display(schema_path, repo_root)}: schema must be a JSON object")
        return
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        issues.append(f"{display(schema_path, repo_root)}: invalid schema: {exc}")
        return
    validator = Draft202012Validator(schema)
    for example_path in example_paths:
        try:
            payload = read_json(example_path)
        except Exception as exc:
            issues.append(f"{display(example_path, repo_root)}: invalid JSON: {exc}")
            continue
        errors = sorted(
            validator.iter_errors(payload),
            key=lambda error: (list(error.absolute_path), error.message),
        )
        if errors:
            first = errors[0]
            where = ".".join(str(part) for part in first.absolute_path) or "<root>"
            issues.append(f"{display(example_path, repo_root)}: schema error at {where}: {first.message}")


def validate_schema_examples(repo_root: Path, issues: list[str]) -> None:
    package_root = repo_root / "mechanics" / "agon"
    validate_json_examples(
        package_root / "parts/trial-playbooks/schemas/agon-trial-playbook.schema.json",
        tuple((package_root / "parts/trial-playbooks/examples").glob("agon*.json")),
        issues,
        repo_root=repo_root,
    )
    validate_json_examples(
        package_root / "parts/trial-kernel-bindings/schemas/agon-trial-kernel-binding.schema.json",
        (package_root / "parts/trial-kernel-bindings/examples/agon_trial_kernel_binding.example.json",),
        issues,
        repo_root=repo_root,
    )
    validate_json_examples(
        package_root / "parts/campaign-playbooks/schemas/agon-campaign-playbook.schema.json",
        (package_root / "parts/campaign-playbooks/examples/agon_campaign_playbook.example.json",),
        issues,
        repo_root=repo_root,
    )
    validate_json_examples(
        package_root / "parts/adoption/schemas/agonic_trial_adoption_run_v1.json",
        (package_root / "parts/adoption/examples/agonic_trial_adoption_run.example.json",),
        issues,
        repo_root=repo_root,
    )


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    repo_root = repo_root.resolve()
    package_root = repo_root / "mechanics" / "agon"
    issues: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (package_root / relative_path).is_file():
            issues.append(f"mechanics/agon/{relative_path}: missing required file")

    for relative_path, tokens in REQUIRED_TEXT.items():
        path = package_root / relative_path
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                issues.append(f"mechanics/agon/{relative_path}: missing token {token!r}")

    for wrapper, part in ROOT_WRAPPERS:
        path = repo_root / wrapper
        if not path.is_file():
            issues.append(f"{wrapper}: missing compatibility wrapper")
            continue
        text = path.read_text(encoding="utf-8")
        if "mechanics" not in text or "agon" not in text or part not in text:
            issues.append(f"{wrapper}: wrapper must route to mechanics/agon/{part}")

    for relative_path in OLD_ROOT_PAYLOADS:
        if (repo_root / relative_path).exists():
            issues.append(f"{relative_path}: old root Agon payload should be package-local")

    for playbook_name in (
        "agon-broken-trace-trial",
        "agon-expensive-summon-intent-trial",
    ):
        try:
            playbook_path = playbook_path_for_name(playbook_name, repo_root)
        except KeyError:
            issues.append(f"{playbook_name}: missing source-home manifest entry")
            continue
        if not playbook_path.is_file():
            issues.append(f"{display(playbook_path, repo_root)}: expected retained source playbook")
    if not any((repo_root / "quests").glob("AOP-Q-AGON-*.md")):
        issues.append("quests/AOP-Q-AGON-*.md: expected retained quest source notes")
    if not any((package_root / "parts").glob("*/manifests/component.agon*.json")):
        issues.append("mechanics/agon/parts/*/manifests/component.agon*.json: expected package-local recurrence manifests")

    validate_schema_examples(repo_root, issues)

    for label, command in COMMANDS:
        completed = subprocess.run(command, cwd=repo_root, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if completed.returncode != 0:
            issues.append(f"{label} failed: {completed.stderr.strip() or completed.stdout.strip()}")

    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)

    issues = validate(args.repo_root.resolve())
    if issues:
        print("Agon package validation failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Agon package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
