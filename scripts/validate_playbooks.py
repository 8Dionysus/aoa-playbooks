#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
from functools import lru_cache
from pathlib import Path

from jsonschema import Draft202012Validator
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]


def repo_root_from_env(env_name: str, default: Path) -> Path:
    override = os.environ.get(env_name)
    if not override:
        return default
    return Path(override).expanduser().resolve()


AOA_AGENTS_ROOT = repo_root_from_env("AOA_AGENTS_ROOT", REPO_ROOT.parent / "aoa-agents")
AOA_EVALS_ROOT = repo_root_from_env("AOA_EVALS_ROOT", REPO_ROOT.parent / "aoa-evals")
AOA_SKILLS_ROOT = repo_root_from_env("AOA_SKILLS_ROOT", REPO_ROOT.parent / "aoa-skills")
AOA_MEMO_ROOT = repo_root_from_env("AOA_MEMO_ROOT", REPO_ROOT.parent / "aoa-memo")
AOA_8DIONYSUS_ROOT = repo_root_from_env("AOA_8DIONYSUS_ROOT", REPO_ROOT.parent / "8Dionysus")
AOA_SDK_ROOT = repo_root_from_env("AOA_SDK_ROOT", REPO_ROOT.parent / "aoa-sdk")
AOA_STATS_ROOT = repo_root_from_env("AOA_STATS_ROOT", REPO_ROOT.parent / "aoa-stats")
REGISTRY_PATH = REPO_ROOT / "generated" / "playbook_registry.min.json"
ACTIVATION_COLLECTION_PATH = REPO_ROOT / "generated" / "playbook_activation_surfaces.min.json"
FEDERATION_COLLECTION_PATH = REPO_ROOT / "generated" / "playbook_federation_surfaces.min.json"
COMPOSITION_CONFIG_PATH = REPO_ROOT / "config" / "playbook_composition_overrides.json"
PLAYBOOK_HANDOFF_CONTRACTS_PATH = REPO_ROOT / "generated" / "playbook_handoff_contracts.json"
PLAYBOOK_FAILURE_CATALOG_PATH = REPO_ROOT / "generated" / "playbook_failure_catalog.json"
PLAYBOOK_SUBAGENT_RECIPES_PATH = REPO_ROOT / "generated" / "playbook_subagent_recipes.json"
PLAYBOOK_AUTOMATION_SEEDS_PATH = REPO_ROOT / "generated" / "playbook_automation_seeds.json"
PLAYBOOK_COMPOSITION_MANIFEST_PATH = REPO_ROOT / "generated" / "playbook_composition_manifest.json"
PLAYBOOK_REVIEW_STATUS_PATH = REPO_ROOT / "generated" / "playbook_review_status.min.json"
PLAYBOOK_REVIEW_PACKET_CONTRACTS_PATH = (
    REPO_ROOT / "generated" / "playbook_review_packet_contracts.min.json"
)
PLAYBOOK_REVIEW_INTAKE_PATH = REPO_ROOT / "generated" / "playbook_review_intake.min.json"
PLAYBOOK_LANDING_GOVERNANCE_PATH = REPO_ROOT / "generated" / "playbook_landing_governance.min.json"
PHASE_ALPHA_CONFIG_PATH = REPO_ROOT / "config" / "phase_alpha_curated_core.json"
PHASE_ALPHA_REVIEW_PACKETS_PATH = REPO_ROOT / "generated" / "phase_alpha_review_packets.min.json"
PHASE_ALPHA_RUN_MATRIX_PATH = REPO_ROOT / "generated" / "phase_alpha_run_matrix.min.json"
SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook-registry.schema.json"
REVIEW_STATUS_SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook-review-status.schema.json"
REVIEW_PACKET_CONTRACTS_SCHEMA_PATH = (
    REPO_ROOT / "schemas" / "playbook-review-packet-contracts.schema.json"
)
PLAYBOOK_STRESS_LANES_DOC_PATH = REPO_ROOT / "docs" / "PLAYBOOK_STRESS_LANES.md"
PLAYBOOK_STRESS_HARVEST_DOC_PATH = REPO_ROOT / "docs" / "PLAYBOOK_STRESS_HARVEST.md"
PLAYBOOK_STRESS_LANE_SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook_stress_lane_v1.json"
PLAYBOOK_REENTRY_GATE_SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook_reentry_gate_v1.json"
PLAYBOOK_STRESS_LANE_EXAMPLE_PATH = REPO_ROOT / "examples" / "playbook_stress_lane.example.json"
PLAYBOOK_REENTRY_GATE_EXAMPLE_PATH = REPO_ROOT / "examples" / "playbook_reentry_gate.example.json"
CODEX_PLANE_ROLLOUT_CYCLE_DOC_PATH = REPO_ROOT / "docs" / "CODEX_PLANE_ROLLOUT_CYCLE.md"
CODEX_PLANE_ROLLOUT_LANE_EXAMPLE_PATH = REPO_ROOT / "examples" / "codex_plane_rollout_lane.example.json"
PLAYBOOK_ROOT = REPO_ROOT / "playbooks"
AGENT_REGISTRY_PATH = AOA_AGENTS_ROOT / "generated" / "agent_registry.min.json"
MODEL_TIER_REGISTRY_PATH = AOA_AGENTS_ROOT / "generated" / "model_tier_registry.json"
EVAL_CATALOG_PATH = AOA_EVALS_ROOT / "generated" / "eval_catalog.min.json"
SKILL_GOVERNANCE_PATH = AOA_SKILLS_ROOT / "generated" / "governance_backlog.json"
SKILL_HANDOFF_CONTRACTS_PATH = AOA_SKILLS_ROOT / "generated" / "skill_handoff_contracts.json"
ACTIVATION_SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook-activation-surface.schema.json"
FEDERATION_SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook-federation-surface.schema.json"
QUESTBOOK_PATH = REPO_ROOT / "QUESTBOOK.md"
QUESTBOOK_HARVEST_DOC_PATH = REPO_ROOT / "docs" / "QUEST_HARVEST_AND_REANCHOR.md"
ORCHESTRATOR_ALIGNMENT_DOC_PATH = REPO_ROOT / "docs" / "ORCHESTRATOR_ALIGNMENT_SURFACES.md"
QUEST_CATALOG_PATH = REPO_ROOT / "generated" / "quest_catalog.min.json"
QUEST_CATALOG_EXAMPLE_PATH = REPO_ROOT / "generated" / "quest_catalog.min.example.json"
QUEST_DISPATCH_PATH = REPO_ROOT / "generated" / "quest_dispatch.min.json"
QUEST_DISPATCH_EXAMPLE_PATH = REPO_ROOT / "generated" / "quest_dispatch.min.example.json"
EXTERNAL_QUEST_SCHEMA_PATH = AOA_EVALS_ROOT / "schemas" / "quest.schema.json"
EXTERNAL_QUEST_DISPATCH_SCHEMA_PATH = AOA_EVALS_ROOT / "schemas" / "quest_dispatch.schema.json"
FOUNDATION_QUESTBOOK_QUEST_IDS = ("AOA-PB-Q-0001", "AOA-PB-Q-0002")
QUESTBOOK_QUEST_IDS = FOUNDATION_QUESTBOOK_QUEST_IDS
QUESTBOOK_REQUIRED_DOC_SECTIONS = (
    "Core rule",
    "What harvest is",
    "What harvest is not",
    "What reanchor is",
    "What reanchor is not",
    "Harvest thresholds",
    "Valid anchor classes",
    "Named promotion destinations",
    "Anti-patterns",
)
QUESTBOOK_REQUIRED_DOC_TOKENS = (
    "PLAYBOOK_RECURRENCE_DISCIPLINE",
    "reanchor is not retry",
    "docs/real-runs/",
    "docs/gate-reviews/",
    "artifact anchors",
    "checkpoint anchors",
    "review anchors",
)
QUESTBOOK_REQUIRED_INDEX_TOKENS = (
    "Frontier",
    "Near",
    "Blocked / reanchor",
    "Harvest candidates",
    "docs/QUEST_HARVEST_AND_REANCHOR.md",
)
ALLOWED_ORCHESTRATOR_CAPABILITY_TARGETS = {
    "repo_layer_selection",
    "evidence_closure",
    "bounded_next_step",
}
ORCHESTRATOR_ALIGNMENT_QUESTS = {
    "AOA-PB-Q-0004": ("aoa-agents:router", "repo_layer_selection"),
    "AOA-PB-Q-0005": ("aoa-agents:review", "evidence_closure"),
    "AOA-PB-Q-0006": ("aoa-agents:bounded_execution", "bounded_next_step"),
}
ORCHESTRATOR_ALIGNMENT_REQUIRED_TOKENS = (
    "## Router",
    "## Review",
    "## Bounded execution",
    "## Boundary rule",
    "Orchestrator class identity lives in `aoa-agents`.",
)
PARTY_TEMPLATE_MODEL_NAME = "docs/PARTY_TEMPLATE_MODEL.md"
BUILD_SYNERGY_POSTURE_NAME = "docs/BUILD_SYNERGY_POSTURE.md"
PARTY_TEMPLATE_SCHEMA_NAME = "schemas/party_template_catalog.schema.json"
PARTY_TEMPLATE_EXAMPLE_NAME = "generated/party_template_cards.min.example.json"
PARTY_TEMPLATE_MODEL_REQUIRED_TOKENS = (
    "## Core rule",
    "A party template is a scenario-owned derived composition surface.",
    "It does not:",
    "using party templates as a substitute for quests, playbooks, or evals themselves",
)
BUILD_SYNERGY_REQUIRED_TOKENS = (
    "## Core rule",
    "Synergy is scenario-shaped.",
    "## Not allowed here",
    "per-run item drops or economy loops",
)
CLOSED_QUEST_STATES = {"done", "dropped"}
ACTIVATION_EXAMPLE_PATHS = {
    "AOA-P-0008": REPO_ROOT / "examples" / "playbook_activation.long-horizon-model-tier-orchestra.example.json",
    "AOA-P-0009": REPO_ROOT / "examples" / "playbook_activation.restartable-inquiry-loop.example.json",
    "AOA-P-0010": REPO_ROOT / "examples" / "playbook_activation.cross-repo-boundary-rollout.example.json",
    "AOA-P-0017": REPO_ROOT / "examples" / "playbook_activation.split-wave-cross-repo-rollout.example.json",
    "AOA-P-0018": REPO_ROOT / "examples" / "playbook_activation.validation-driven-remediation.example.json",
    "AOA-P-0019": REPO_ROOT / "examples" / "playbook_activation.release-migration-cutover.example.json",
    "AOA-P-0020": REPO_ROOT / "examples" / "playbook_activation.incident-recovery-routing.example.json",
}
HARVEST_TEMPLATE_REQUIREMENTS = {
    REPO_ROOT / "examples" / "harvests" / "split-wave-cross-repo-rollout.harvest-template.md": (
        "wave_plan",
        "bridge_surface_pack",
        "downstream_revalidation_pack",
        "handoff_record",
    ),
    REPO_ROOT / "examples" / "harvests" / "validation-driven-remediation.harvest-template.md": (
        "failure_map",
        "boundary_map",
        "remediation_change_set",
        "revalidation_pack",
        "remediation_decision",
        "handoff_record",
    ),
    REPO_ROOT / "examples" / "harvests" / "release-migration-cutover.harvest-template.md": (
        "cutover_plan",
        "cutover_decision",
        "post_cutover_verification_pack",
        "handoff_record",
    ),
    REPO_ROOT / "examples" / "harvests" / "incident-recovery-routing.harvest-template.md": (
        "incident_map",
        "stabilization_plan",
        "recovery_decision",
        "recovery_verification_pack",
        "handoff_record",
    ),
    REPO_ROOT / "examples" / "harvests" / "owner-first-capability-landing.harvest-template.md": (
        "candidate_lineage_pack",
        "owner_landing_bundle",
        "landing_decision",
        "rollout_pack",
        "validation_pack",
        "hardening_record",
        "handoff_record",
    ),
    REPO_ROOT / "examples" / "harvests" / "closeout-owner-follow-through-continuity.harvest-template.md": (
        "reviewed_closeout_pack",
        "owner_handoff_bundle",
        "owner_authorship_bundle",
        "validation_pack",
        "merge_record",
        "residual_handoff_record",
    ),
    REPO_ROOT / "examples" / "harvests" / "session-growth-cycle.harvest-template.md": (
        "checkpoint_carry_bundle",
        "reviewed_closeout_context",
        "candidate_harvest_packet",
        "route_follow_through_decision",
        "seed_trace",
        "owner_landing_bundle",
        "proof_packet",
        "writeback_record",
        "stats_refresh_record",
    ),
    REPO_ROOT / "examples" / "harvests" / "federated-live-publisher-activation.harvest-template.md": (
        "readiness_audit_pack",
        "owner_activation_plan",
        "owner_change_set",
        "publication_verification_pack",
        "stats_visibility_pack",
        "residual_handoff_record",
    ),
    REPO_ROOT / "examples" / "harvests" / "trusted-rollout-operations.harvest-template.md": (
        "rollout_decision",
        "doctor_report_ref",
        "smoke_report_ref",
        "deploy_receipt_ref",
        "drift_window_ref",
        "rollback_window_ref",
        "stats_refresh_ref",
        "memo_writeback_ref",
    ),
}
REAL_RUN_WORKFLOW_PATH = REPO_ROOT / "docs" / "PLAYBOOK_REAL_RUN_WORKFLOW.md"
REAL_RUN_SUMMARY_HOME_PATH = REPO_ROOT / "docs" / "real-runs" / "README.md"
REAL_RUN_SUMMARY_DIR = REPO_ROOT / "docs" / "real-runs"
GATE_REVIEW_DIR = REPO_ROOT / "docs" / "gate-reviews"
PHASE_ALPHA_HARVESTS_DIR = REPO_ROOT / "examples" / "alpha_harvests"
PHASE_ALPHA_REVIEWED_RUNS_DIR = REPO_ROOT / "docs" / "alpha-reviewed-runs"
PHASE_ALPHA_READINESS_DIR = REPO_ROOT / "docs" / "alpha-readiness"
PHASE_ALPHA_PLAYBOOK_ORDER = (
    "AOA-P-0014",
    "AOA-P-0006",
    "AOA-P-0018",
    "AOA-P-0008",
    "AOA-P-0009",
)
PHASE_ALPHA_FINAL_RERUN_ID = "alpha-06-validation-driven-remediation-recall-rerun"
PHASE_ALPHA_REQUIRED_HARVEST_SECTIONS = (
    "Route Header",
    "Required Artifacts",
    "Eval Anchors",
    "Memo Writeback",
    "Stop Conditions",
    "Evidence Links",
)
PHASE_ALPHA_REQUIRED_REVIEWED_RUN_SECTIONS = (
    "Run Header",
    "Runtime Path",
    "Entry Signal",
    "Required Artifacts",
    "Eval Anchors",
    "Memo Writeback",
    "Stop Conditions",
    "Recurrence Posture",
    "Evidence Links",
)
PHASE_ALPHA_REQUIRED_READINESS_SECTIONS = (
    "Readiness Header",
    "Fixed Route Order",
    "Required Evidence",
    "Eval Coverage",
    "Memo Coverage",
    "Current Verdict",
    "Next Trigger",
)
REAL_RUN_SUMMARY_SLUG_REQUIREMENTS = {
    "split-wave-cross-repo-rollout": (
        "wave_plan",
        "bridge_surface_pack",
        "downstream_revalidation_pack",
        "handoff_record",
    ),
    "validation-driven-remediation": (
        "failure_map",
        "boundary_map",
        "remediation_change_set",
        "revalidation_pack",
        "remediation_decision",
        "handoff_record",
    ),
    "release-migration-cutover": (
        "cutover_plan",
        "cutover_decision",
        "post_cutover_verification_pack",
        "handoff_record",
    ),
    "incident-recovery-routing": (
        "incident_map",
        "stabilization_plan",
        "recovery_decision",
        "recovery_verification_pack",
        "handoff_record",
    ),
    "owner-first-capability-landing": (
        "candidate_lineage_pack",
        "owner_landing_bundle",
        "landing_decision",
        "rollout_pack",
        "validation_pack",
        "hardening_record",
        "handoff_record",
    ),
    "closeout-owner-follow-through-continuity": (
        "reviewed_closeout_pack",
        "owner_handoff_bundle",
        "owner_authorship_bundle",
        "validation_pack",
        "merge_record",
        "residual_handoff_record",
    ),
    "session-growth-cycle": (
        "checkpoint_carry_bundle",
        "reviewed_closeout_context",
        "candidate_harvest_packet",
        "route_follow_through_decision",
        "seed_trace",
        "owner_landing_bundle",
        "proof_packet",
        "writeback_record",
        "stats_refresh_record",
    ),
    "federated-live-publisher-activation": (
        "readiness_audit_pack",
        "owner_activation_plan",
        "owner_change_set",
        "publication_verification_pack",
        "stats_visibility_pack",
        "residual_handoff_record",
    ),
    "trusted-rollout-operations": (
        "rollout_decision",
        "doctor_report_ref",
        "smoke_report_ref",
        "deploy_receipt_ref",
        "drift_window_ref",
        "rollback_window_ref",
        "stats_refresh_ref",
        "memo_writeback_ref",
    ),
}
GATE_REVIEW_REQUIREMENTS = {
    GATE_REVIEW_DIR / "split-wave-cross-repo-rollout.md": {
        "playbook_id": "AOA-P-0017",
        "slug": "split-wave-cross-repo-rollout",
        "required_tokens": (
            "wave_plan",
            "bridge_surface_pack",
            "downstream_revalidation_pack",
            "handoff_record",
        ),
    },
    GATE_REVIEW_DIR / "validation-driven-remediation.md": {
        "playbook_id": "AOA-P-0018",
        "slug": "validation-driven-remediation",
        "required_tokens": (
            "failure_map",
            "boundary_map",
            "remediation_change_set",
            "revalidation_pack",
            "remediation_decision",
            "handoff_record",
        ),
    },
    GATE_REVIEW_DIR / "release-migration-cutover.md": {
        "playbook_id": "AOA-P-0019",
        "slug": "release-migration-cutover",
        "required_tokens": (
            "cutover_plan",
            "cutover_decision",
            "post_cutover_verification_pack",
            "handoff_record",
        ),
    },
    GATE_REVIEW_DIR / "incident-recovery-routing.md": {
        "playbook_id": "AOA-P-0020",
        "slug": "incident-recovery-routing",
        "required_tokens": (
            "incident_map",
            "stabilization_plan",
            "recovery_decision",
            "recovery_verification_pack",
            "handoff_record",
            "Only a live incident should open the first reviewed summary",
        ),
    },
    GATE_REVIEW_DIR / "owner-first-capability-landing.md": {
        "playbook_id": "AOA-P-0021",
        "slug": "owner-first-capability-landing",
        "required_tokens": (
            "candidate_lineage_pack",
            "owner_landing_bundle",
            "landing_decision",
            "rollout_pack",
            "validation_pack",
            "hardening_record",
            "handoff_record",
        ),
    },
    GATE_REVIEW_DIR / "closeout-owner-follow-through-continuity.md": {
        "playbook_id": "AOA-P-0023",
        "slug": "closeout-owner-follow-through-continuity",
        "required_tokens": (
            "reviewed_closeout_pack",
            "owner_handoff_bundle",
            "owner_authorship_bundle",
            "validation_pack",
            "merge_record",
            "residual_handoff_record",
        ),
    },
    GATE_REVIEW_DIR / "federated-live-publisher-activation.md": {
        "playbook_id": "AOA-P-0024",
        "slug": "federated-live-publisher-activation",
        "required_tokens": (
            "readiness_audit_pack",
            "owner_activation_plan",
            "owner_change_set",
            "publication_verification_pack",
            "stats_visibility_pack",
            "residual_handoff_record",
        ),
    },
    GATE_REVIEW_DIR / "trusted-rollout-operations.md": {
        "playbook_id": "AOA-P-0028",
        "slug": "trusted-rollout-operations",
        "required_tokens": (
            "rollout_decision",
            "doctor_report_ref",
            "smoke_report_ref",
            "deploy_receipt_ref",
            "drift_window_ref",
            "rollback_window_ref",
            "stats_refresh_ref",
            "memo_writeback_ref",
        ),
    },
}
REVIEWED_SUMMARY_GATE_SENTENCE = (
    "Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still "
    "require explicit gate review under `docs/gate-reviews/`."
)
REQUIRED_PLAYBOOK_STRESS_LANE_SNIPPETS = (
    "Teach recurring playbooks to expose what happens when the normal route becomes unsafe, under-evidenced, or derived-surface dependent.",
    "do not let playbooks replace source-owned receipts",
    "do not confuse scenario composition with proof or source meaning",
    "It is a named branch of the same recurring scenario.",
)
REQUIRED_PLAYBOOK_STRESS_HARVEST_SNIPPETS = (
    "Make recurring stressed runs leave behind enough usable structure to improve the next run.",
    "That decision should cite evidence, not mood.",
    "do not let playbook harvest become the only record of what happened",
    "one machine-readable re-entry gate family",
)
CODEX_PLANE_ROLLOUT_DOC_SNIPPETS = (
    "This note is the shared-root deployment continuity companion for",
    "It does not authorize rollout by itself.",
    "It does not introduce a new playbook, activation surface, or hidden runner.",
    "stable MCP names drift from `aoa_workspace`, `aoa_stats`, and `dionysus`",
    "The deployment summary may shape continuity review, but it does not overrule",
)
CODEX_PLANE_ROLLOUT_PHASES = (
    ("render", "regeneration_report"),
    ("trust-check", "trust_state"),
    ("dry-run-validate", "regeneration_report"),
    ("execute-apply", "rollout_receipt"),
    ("doctor-verify", "deploy_status_snapshot"),
    ("activate-bounded-rollout", "rollout_campaign_record"),
    ("observe-drift-window", "drift_window_record"),
    ("repair-or-rollback", "rollback_window_record"),
    ("publish-rollout-history", "rollout_campaign_record"),
    ("stats-refresh", "rollout_operations_summary"),
    ("memo-writeback", "memo_writeback_record"),
)
CODEX_PLANE_REQUIRED_ARTIFACTS = (
    "trust_state",
    "regeneration_report",
    "rollout_receipt",
    "deploy_status_snapshot",
    "rollout_campaign_record",
    "drift_window_record",
    "rollback_window_record",
    "rollout_operations_summary",
    "rollout_drift_summary",
    "memo_writeback_record",
)
CODEX_PLANE_STOP_BEFORE_APPLY = (
    "trust_posture=root_mismatch",
    "trust_posture=config_inactive",
    "stable_mcp_name_set_drifted=true",
    "dry_run_ok=false",
)
CODEX_PLANE_ROLLBACK_TRIGGERS = (
    "doctor_result=fail",
    "hooks_active=false",
    "project_config_active=false",
    "drift_detected=true",
    "drift_state=material",
)
CODEX_PLANE_STABLE_MCP_NAMES = {"aoa_workspace", "aoa_stats", "dionysus"}
ACTIVATION_COLLECTION_PLAYBOOK_IDS = (
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
    "AOA-P-0026",
    "AOA-P-0027",
    "AOA-P-0025",
    "AOA-P-0028",
    "AOA-P-0029",
    "AOA-P-0030",
    "AOA-P-0031",
)
FEDERATION_COLLECTION_PLAYBOOK_IDS = (
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
    "AOA-P-0026",
    "AOA-P-0027",
    "AOA-P-0025",
    "AOA-P-0028",
    "AOA-P-0029",
    "AOA-P-0030",
    "AOA-P-0031",
)
COMPOSITION_COLLECTION_PLAYBOOK_IDS = (
    "AOA-P-0011",
    "AOA-P-0012",
    "AOA-P-0013",
    "AOA-P-0014",
    "AOA-P-0021",
    "AOA-P-0022",
    "AOA-P-0023",
    "AOA-P-0015",
    "AOA-P-0016",
    "AOA-P-0017",
)
FEDERATION_REQUIRED_FRONTMATTER_KEYS = ("required_skills", "memo_contract_refs", "memo_writeback_targets")

ALLOWED_STATUS = {"active", "planned", "experimental", "deprecated"}
ALLOWED_MEMORY_POSTURE = {"none", "light_recall", "bounded_recall", "deep_recall"}
ALLOWED_EVAL_POSTURE = {"minimal", "required", "strict", "paired_eval"}
ALLOWED_FALLBACK = {"none", "handoff", "rollback", "safe_stop", "review_required"}
ALLOWED_RETURN_POSTURE = {"artifact_anchor", "checkpoint_anchor", "review_anchor", "mixed_anchor"}
ALLOWED_RETURN_REENTRY_MODES = {
    "same_phase",
    "previous_phase",
    "router_reentry",
    "checkpoint_relaunch",
    "review_gate",
    "rollback_gate",
    "safe_stop",
}


def quest_sort_key(quest_id: str) -> tuple[int, str]:
    suffix = quest_id.rsplit("-", 1)[-1]
    try:
        return (int(suffix), quest_id)
    except ValueError:
        return (sys.maxsize, quest_id)


def discover_questbook_quest_ids(repo_root: Path = REPO_ROOT) -> tuple[str, ...]:
    quests_dir = repo_root / "quests"
    discovered = sorted(
        {
            path.stem
            for path in quests_dir.glob("AOA-PB-Q-*.yaml")
            if path.is_file()
        },
        key=quest_sort_key,
    )
    if not discovered:
        return FOUNDATION_QUESTBOOK_QUEST_IDS
    return tuple(discovered)


def validate_optional_orchestrator_quest_fields(
    payload: dict[str, object], *, location: str, repo_root: Path
) -> None:
    orchestrator_class_ref = payload.get("orchestrator_class_ref")
    capability_target = payload.get("capability_target")
    if orchestrator_class_ref is None and capability_target is not None:
        fail(f"{location} must not declare capability_target without orchestrator_class_ref")
    if orchestrator_class_ref is None:
        return
    validate_orchestrator_class_ref(orchestrator_class_ref, location=location)
    if capability_target not in ALLOWED_ORCHESTRATOR_CAPABILITY_TARGETS:
        fail(f"{location}.capability_target must resolve to a supported orchestrator capability")
    for field_name in ("playbook_family_refs", "proof_surface_refs", "memory_surface_refs"):
        if field_name not in payload:
            continue
        value = payload.get(field_name)
        if not isinstance(value, list) or not value:
            fail(f"{location}.{field_name} must be a non-empty list when present")
        for item in value:
            if not isinstance(item, str) or len(item) < 3:
                fail(f"{location}.{field_name} must contain non-empty string refs")
            if item.startswith("repo:"):
                continue
            local_path = item.split("#", 1)[0]
            if not (repo_root / local_path).exists():
                fail(f"{location}.{field_name} local ref does not exist: {local_path}")
RETURN_FIELD_NAMES = ("return_posture", "return_anchor_artifacts", "return_reentry_modes")
MEMO_SPEC_FIELD_NAMES = (
    "memo_recall_modes",
    "memo_scope_default",
    "memo_scope_ceiling",
    "memo_read_path",
    "memo_checkpoint_posture",
    "memo_source_route_policy",
)
RUNTIME_MEMO_SPEC_PLAYBOOK_IDS = {
    "AOA-P-0008",
    "AOA-P-0009",
    "AOA-P-0010",
    "AOA-P-0017",
    "AOA-P-0018",
    "AOA-P-0019",
    "AOA-P-0020",
}
ALLOWED_MEMO_RECALL_MODES = {"working", "episodic", "semantic", "procedural", "lineage"}
ALLOWED_MEMO_SCOPES = {"project", "workspace", "ecosystem"}
MEMO_SCOPE_ORDER = {"project": 0, "workspace": 1, "ecosystem": 2}
ALLOWED_MEMO_READ_PATHS = {"inspect_only", "inspect_then_expand", "inspect_capsule_then_expand"}
ALLOWED_MEMO_CHECKPOINT_POSTURES = {"not_needed", "preferred", "required"}
ALLOWED_MEMO_SOURCE_ROUTE_POLICIES = {"not_needed", "preferred", "required"}
SEMANTIC_LINEAGE_MEMO_CONTRACT_REFS = {
    "examples/recall_contract.router.semantic.json",
    "examples/recall_contract.router.lineage.json",
    "examples/recall_contract.object.semantic.json",
    "examples/recall_contract.object.lineage.json",
}
RUNTIME_MEMO_SPEC_EXPECTATIONS = {
    "AOA-P-0008": {
        "memo_recall_modes": ("semantic", "procedural"),
        "memo_scope_default": "workspace",
        "memo_scope_ceiling": "ecosystem",
        "memo_read_path": "inspect_capsule_then_expand",
        "memo_checkpoint_posture": "not_needed",
        "memo_source_route_policy": "required",
        "required_memo_contract_ref": "examples/recall_contract.router.semantic.json",
    },
    "AOA-P-0009": {
        "memo_recall_modes": ("working",),
        "memo_scope_default": "project",
        "memo_scope_ceiling": "ecosystem",
        "memo_read_path": "inspect_then_expand",
        "memo_checkpoint_posture": "required",
        "memo_source_route_policy": "preferred",
        "required_memo_contract_ref": "examples/recall_contract.object.working.return.json",
    },
    "AOA-P-0010": {
        "memo_recall_modes": ("episodic", "semantic"),
        "memo_scope_default": "workspace",
        "memo_scope_ceiling": "workspace",
        "memo_read_path": "inspect_capsule_then_expand",
        "memo_checkpoint_posture": "not_needed",
        "memo_source_route_policy": "required",
        "required_memo_contract_ref": "examples/recall_contract.router.semantic.json",
    },
    "AOA-P-0017": {
        "memo_recall_modes": ("episodic", "semantic"),
        "memo_scope_default": "workspace",
        "memo_scope_ceiling": "workspace",
        "memo_read_path": "inspect_capsule_then_expand",
        "memo_checkpoint_posture": "not_needed",
        "memo_source_route_policy": "required",
        "required_memo_contract_ref": "examples/recall_contract.router.semantic.json",
    },
    "AOA-P-0018": {
        "memo_recall_modes": ("episodic", "semantic"),
        "memo_scope_default": "workspace",
        "memo_scope_ceiling": "workspace",
        "memo_read_path": "inspect_capsule_then_expand",
        "memo_checkpoint_posture": "not_needed",
        "memo_source_route_policy": "required",
        "required_memo_contract_ref": "examples/recall_contract.router.semantic.json",
    },
    "AOA-P-0019": {
        "memo_recall_modes": ("working", "episodic"),
        "memo_scope_default": "workspace",
        "memo_scope_ceiling": "workspace",
        "memo_read_path": "inspect_then_expand",
        "memo_checkpoint_posture": "preferred",
        "memo_source_route_policy": "preferred",
        "required_memo_contract_ref": "examples/recall_contract.object.working.return.json",
    },
    "AOA-P-0020": {
        "memo_recall_modes": ("working", "episodic"),
        "memo_scope_default": "workspace",
        "memo_scope_ceiling": "workspace",
        "memo_read_path": "inspect_then_expand",
        "memo_checkpoint_posture": "preferred",
        "memo_source_route_policy": "preferred",
        "required_memo_contract_ref": "examples/recall_contract.object.working.return.json",
    },
}
TIER_ARTIFACT_PLAYBOOKS = {"AOA-P-0008"}
REQUIRED_BUNDLE_SECTIONS = {
    "Intent",
    "Trigger boundary",
    "Prerequisites",
    "Participating agents",
    "Required skills",
    "Decision points",
    "Handoffs",
    "Fallback and rollback posture",
    "Expected evidence posture",
    "Expected artifacts",
    "Eval anchors",
    "Memory writeback",
    "Canonical route",
}
REQUIRED_HARVEST_TEMPLATE_SECTIONS = (
    "Run Header",
    "Entry Signal",
    "Boundary Summary",
    "Required Artifacts",
    "Closure Class",
    "Follow-On Route",
    "Composition Signals",
    "Residual Risk",
)
REQUIRED_REAL_RUN_SUMMARY_SECTIONS = REQUIRED_HARVEST_TEMPLATE_SECTIONS + ("Evidence Links",)
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
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")
REVIEWED_RUN_REF_RE = re.compile(
    r"docs/real-runs/(\d{4}-\d{2}-\d{2}\.[a-z0-9-]+(?:\.[a-z0-9-]+)?\.md)"
)
BUNDLE_SEMANTIC_CHECKS = {
    "AOA-P-0006": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-approval-boundary-adherence",
                "aoa-bounded-change-quality",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-approval-gate-check",
                "aoa-dry-run-first",
                "aoa-change-protocol",
            ),
            "memo_contract_refs": (
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-approval-gate-check",
            "aoa-dry-run-first",
            "aoa-change-protocol",
            "aoa-approval-boundary-adherence",
            "aoa-bounded-change-quality",
            "decision",
            "audit_event",
            "provenance_thread",
            "architect",
            "coder",
            "reviewer",
            "memory-keeper",
        ),
    },
    "AOA-P-0007": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-witness-trace-integrity",
                "aoa-compost-provenance-preservation",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-change-protocol",
            ),
            "memo_contract_refs": (
                "examples/recall_contract.router.semantic.json",
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "episode",
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-change-protocol",
            "aoa-witness-trace-integrity",
            "aoa-compost-provenance-preservation",
            "architect",
            "coder",
            "reviewer",
            "memory-keeper",
        ),
    },
    "AOA-P-0008": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-long-horizon-depth",
                "aoa-tool-trajectory-discipline",
            ),
            "required_skills": (
                "aoa-change-protocol",
                "aoa-source-of-truth-check",
                "aoa-dry-run-first",
                "aoa-bounded-context-map",
            ),
            "memo_contract_refs": (
                "examples/recall_contract.router.semantic.json",
                "examples/checkpoint_to_memory_contract.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "claim",
                "pattern",
            ),
        },
        "text_tokens": (
            "aoa-change-protocol",
            "aoa-source-of-truth-check",
            "aoa-dry-run-first",
            "aoa-bounded-context-map",
            "decision",
            "claim",
            "pattern",
        ),
    },
    "AOA-P-0009": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-long-horizon-depth",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-change-protocol",
                "aoa-dry-run-first",
                "aoa-bounded-context-map",
            ),
            "memo_contract_refs": (
                "examples/recall_contract.object.working.return.json",
                "examples/checkpoint_to_memory_contract.example.json",
            ),
            "memo_writeback_targets": (
                "state_capsule",
                "decision",
            ),
        },
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-change-protocol",
            "aoa-dry-run-first",
            "aoa-bounded-context-map",
            "state_capsule",
            "decision",
        ),
    },
    "AOA-P-0010": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-approval-boundary-adherence",
                "aoa-scope-drift-detection",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-bounded-context-map",
                "aoa-approval-gate-check",
                "aoa-dry-run-first",
                "aoa-change-protocol",
            ),
            "memo_contract_refs": (
                "examples/recall_contract.router.semantic.json",
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-bounded-context-map",
            "aoa-approval-gate-check",
            "aoa-dry-run-first",
            "aoa-change-protocol",
            "aoa-approval-boundary-adherence",
            "aoa-scope-drift-detection",
            "AOA-P-0017",
            "AOA-P-0018",
            "AOA-P-0019",
            "AOA-P-0020",
            "architect",
            "coder",
            "reviewer",
            "evaluator",
            "memory-keeper",
        ),
    },
    "AOA-P-0011": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-approval-boundary-adherence",
                "aoa-bounded-change-quality",
            ),
            "required_skills": (
                "aoa-approval-gate-check",
                "aoa-source-of-truth-check",
                "aoa-bounded-context-map",
                "aoa-dry-run-first",
                "aoa-change-protocol",
                "aoa-contract-test",
                "aoa-tdd-slice",
                "aoa-adr-write",
                "aoa-sanitized-share",
            ),
            "memo_contract_refs": (
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-approval-gate-check",
            "aoa-source-of-truth-check",
            "aoa-change-protocol",
            "aoa-contract-test",
            "aoa-sanitized-share",
            "aoa-approval-boundary-adherence",
            "aoa-bounded-change-quality",
            "architect",
            "coder",
            "reviewer",
            "memory-keeper",
        ),
    },
    "AOA-P-0012": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-approval-boundary-adherence",
                "aoa-verification-honesty",
            ),
            "required_skills": (
                "aoa-approval-gate-check",
                "aoa-source-of-truth-check",
                "aoa-dry-run-first",
                "aoa-safe-infra-change",
                "aoa-local-stack-bringup",
                "aoa-contract-test",
                "aoa-adr-write",
                "aoa-sanitized-share",
            ),
            "memo_contract_refs": (
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-approval-gate-check",
            "aoa-source-of-truth-check",
            "aoa-dry-run-first",
            "aoa-safe-infra-change",
            "aoa-local-stack-bringup",
            "aoa-contract-test",
            "aoa-sanitized-share",
            "aoa-approval-boundary-adherence",
            "aoa-verification-honesty",
            "AOA-P-0014",
            "AOA-P-0020",
            "architect",
            "coder",
            "reviewer",
            "memory-keeper",
        ),
    },
    "AOA-P-0013": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-scope-drift-detection",
                "aoa-verification-honesty",
            ),
            "required_skills": (
                "aoa-bounded-context-map",
                "aoa-core-logic-boundary",
                "aoa-property-invariants",
                "aoa-tdd-slice",
                "aoa-port-adapter-refactor",
                "aoa-invariant-coverage-audit",
                "aoa-contract-test",
                "aoa-adr-write",
            ),
            "memo_contract_refs": (
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-bounded-context-map",
            "aoa-core-logic-boundary",
            "aoa-property-invariants",
            "aoa-port-adapter-refactor",
            "aoa-invariant-coverage-audit",
            "aoa-contract-test",
            "aoa-adr-write",
            "aoa-scope-drift-detection",
            "aoa-verification-honesty",
            "architect",
            "coder",
            "reviewer",
            "memory-keeper",
        ),
    },
    "AOA-P-0014": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-verification-honesty",
                "aoa-tool-trajectory-discipline",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-dry-run-first",
                "aoa-local-stack-bringup",
                "aoa-change-protocol",
                "aoa-contract-test",
                "aoa-sanitized-share",
            ),
            "memo_contract_refs": (
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-dry-run-first",
            "aoa-local-stack-bringup",
            "aoa-change-protocol",
            "aoa-contract-test",
            "aoa-sanitized-share",
            "aoa-verification-honesty",
            "aoa-tool-trajectory-discipline",
            "AOA-P-0012",
            "AOA-P-0020",
            "architect",
            "coder",
            "reviewer",
            "memory-keeper",
        ),
    },
    "AOA-P-0015": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-ambiguity-handling",
                "aoa-artifact-review-rubric",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-adr-write",
                "aoa-sanitized-share",
            ),
            "memo_contract_refs": (
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-adr-write",
            "aoa-sanitized-share",
            "aoa-ambiguity-handling",
            "aoa-artifact-review-rubric",
            "architect",
            "coder",
            "reviewer",
            "memory-keeper",
        ),
    },
    "AOA-P-0016": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-approval-boundary-adherence",
                "aoa-bounded-change-quality",
            ),
            "required_skills": (
                "aoa-approval-gate-check",
                "atm10-source-of-truth-check",
                "aoa-dry-run-first",
                "atm10-change-protocol",
                "aoa-contract-test",
                "aoa-sanitized-share",
            ),
            "memo_contract_refs": (
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-approval-gate-check",
            "atm10-source-of-truth-check",
            "aoa-dry-run-first",
            "atm10-change-protocol",
            "aoa-contract-test",
            "aoa-sanitized-share",
            "aoa-approval-boundary-adherence",
            "aoa-bounded-change-quality",
            "architect",
            "coder",
            "reviewer",
            "memory-keeper",
        ),
    },
    "AOA-P-0017": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-approval-boundary-adherence",
                "aoa-scope-drift-detection",
                "aoa-verification-honesty",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-bounded-context-map",
                "aoa-approval-gate-check",
                "aoa-dry-run-first",
                "aoa-change-protocol",
                "aoa-contract-test",
                "aoa-adr-write",
            ),
            "memo_contract_refs": (
                "examples/recall_contract.router.semantic.json",
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-bounded-context-map",
            "aoa-approval-gate-check",
            "aoa-dry-run-first",
            "aoa-change-protocol",
            "aoa-contract-test",
            "aoa-adr-write",
            "aoa-approval-boundary-adherence",
            "aoa-scope-drift-detection",
            "aoa-verification-honesty",
            "AOA-P-0010",
            "AOA-P-0019",
            "AOA-P-0020",
            "architect",
            "coder",
            "reviewer",
            "evaluator",
            "memory-keeper",
        ),
    },
    "AOA-P-0018": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-approval-boundary-adherence",
                "aoa-scope-drift-detection",
                "aoa-verification-honesty",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-bounded-context-map",
                "aoa-approval-gate-check",
                "aoa-dry-run-first",
                "aoa-change-protocol",
                "aoa-contract-test",
                "aoa-adr-write",
            ),
            "memo_contract_refs": (
                "examples/recall_contract.router.semantic.json",
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "aoa-source-of-truth-check",
            "aoa-bounded-context-map",
            "aoa-approval-gate-check",
            "aoa-dry-run-first",
            "aoa-change-protocol",
            "aoa-contract-test",
            "aoa-adr-write",
            "aoa-approval-boundary-adherence",
            "aoa-scope-drift-detection",
            "aoa-verification-honesty",
            "AOA-P-0010",
            "AOA-P-0019",
            "AOA-P-0020",
            "architect",
            "coder",
            "reviewer",
            "evaluator",
            "memory-keeper",
        ),
    },
    "AOA-P-0019": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-approval-boundary-adherence",
                "aoa-scope-drift-detection",
                "aoa-verification-honesty",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-bounded-context-map",
                "aoa-approval-gate-check",
                "aoa-dry-run-first",
                "aoa-change-protocol",
                "aoa-contract-test",
                "aoa-adr-write",
                "aoa-sanitized-share",
            ),
            "memo_contract_refs": (
                "examples/recall_contract.object.working.return.json",
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "authority_map",
            "cutover_plan",
            "cutover_decision",
            "cutover_change_set",
            "post_cutover_verification_pack",
            "handoff_record",
            "aoa-source-of-truth-check",
            "aoa-bounded-context-map",
            "aoa-approval-gate-check",
            "aoa-dry-run-first",
            "aoa-change-protocol",
            "aoa-contract-test",
            "aoa-adr-write",
            "aoa-sanitized-share",
            "aoa-approval-boundary-adherence",
            "aoa-scope-drift-detection",
            "aoa-verification-honesty",
            "AOA-P-0004",
            "AOA-P-0010",
            "AOA-P-0017",
            "AOA-P-0020",
            "architect",
            "coder",
            "reviewer",
            "evaluator",
            "memory-keeper",
        ),
    },
    "AOA-P-0020": {
        "frontmatter_lists": {
            "eval_anchors": (
                "aoa-approval-boundary-adherence",
                "aoa-scope-drift-detection",
                "aoa-verification-honesty",
            ),
            "required_skills": (
                "aoa-source-of-truth-check",
                "aoa-bounded-context-map",
                "aoa-approval-gate-check",
                "aoa-dry-run-first",
                "aoa-change-protocol",
                "aoa-safe-infra-change",
                "aoa-local-stack-bringup",
                "aoa-contract-test",
                "aoa-adr-write",
                "aoa-sanitized-share",
            ),
            "memo_contract_refs": (
                "examples/recall_contract.object.working.return.json",
                "examples/checkpoint_to_memory_contract.example.json",
                "examples/provenance_thread.example.json",
            ),
            "memo_writeback_targets": (
                "decision",
                "audit_event",
                "provenance_thread",
            ),
        },
        "text_tokens": (
            "incident_map",
            "stabilization_plan",
            "stabilization_change_set",
            "recovery_decision",
            "recovery_verification_pack",
            "handoff_record",
            "aoa-source-of-truth-check",
            "aoa-bounded-context-map",
            "aoa-approval-gate-check",
            "aoa-dry-run-first",
            "aoa-change-protocol",
            "aoa-safe-infra-change",
            "aoa-local-stack-bringup",
            "aoa-contract-test",
            "aoa-adr-write",
            "aoa-sanitized-share",
            "aoa-approval-boundary-adherence",
            "aoa-scope-drift-detection",
            "aoa-verification-honesty",
            "AOA-P-0012",
            "AOA-P-0014",
            "AOA-P-0018",
            "AOA-P-0019",
            "architect",
            "coder",
            "reviewer",
            "evaluator",
            "memory-keeper",
        ),
    },
}


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def validate_nested_agents_surface() -> None:
    try:
        from validate_nested_agents import validate_nested_agents_docs
    except Exception as exc:  # defensive import guard for local validator wiring
        fail(f"unable to load nested AGENTS validator: {exc}")

    try:
        validate_nested_agents_docs()
    except RuntimeError as exc:
        fail(str(exc))


def display_path(path: Path) -> str:
    for root in (
        REPO_ROOT,
        AOA_AGENTS_ROOT,
        AOA_EVALS_ROOT,
        AOA_SKILLS_ROOT,
        AOA_MEMO_ROOT,
        AOA_8DIONYSUS_ROOT,
        AOA_SDK_ROOT,
        AOA_STATS_ROOT,
    ):
        try:
            return path.relative_to(root).as_posix()
        except ValueError:
            continue
    return path.as_posix()


def load_composition_builder_module():
    module_path = REPO_ROOT / "scripts" / "generate_playbook_composition_surfaces.py"
    spec = importlib.util.spec_from_file_location("generate_playbook_composition_surfaces", module_path)
    if spec is None or spec.loader is None:
        fail(f"unable to load composition builder module from {display_path(module_path)}")
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:
        fail(f"unable to load composition builder module from {display_path(module_path)}: {exc}")
    return module


def skill_is_federation_eligible(skill: dict[str, object], *, playbook_status: str) -> bool:
    if skill.get("lineage_state") != "published":
        return False
    readiness = skill.get("readiness_reconciliation")
    if readiness == "governance_and_eval_ready":
        return True
    if readiness == "project_overlay_federation_ready":
        return True
    return playbook_status == "experimental" and readiness == "eval_ready_but_governance_blocked"


def read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {display_path(path)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {display_path(path)}: {exc}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing required file: {display_path(path)}")


def local_ref_error(ref_value: object, label: str) -> str | None:
    if not isinstance(ref_value, str) or not ref_value:
        return f"{label}: reference must be a non-empty string"
    if ref_value.startswith(("repo:", "http://", "https://")):
        return None
    target = REPO_ROOT / ref_value
    if not target.exists():
        return f"{label}: referenced path does not exist: {ref_value}"
    return None


def read_yaml(path: Path) -> object:
    text = read_text(path)
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as exc:
        fail(f"invalid YAML in {display_path(path)}: {exc}")


def format_schema_path(path_parts: list[object]) -> str:
    parts: list[str] = []
    for part in path_parts:
        if isinstance(part, int):
            parts.append(f"[{part}]")
        else:
            if parts:
                parts.append(f".{part}")
            else:
                parts.append(str(part))
    return "".join(parts)


@lru_cache(maxsize=None)
def external_schema_validator(schema_path: Path) -> Draft202012Validator:
    schema = read_json(schema_path)
    if not isinstance(schema, dict):
        fail(f"{display_path(schema_path)} must remain a JSON object")
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def validate_against_external_schema(data: object, schema_path: Path, *, location: str) -> None:
    validator = external_schema_validator(schema_path)
    errors = sorted(
        validator.iter_errors(data),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    if not errors:
        return
    first = errors[0]
    error_path = format_schema_path(list(first.absolute_path))
    if error_path:
        fail(f"{location} schema violation at '{error_path}': {first.message}")
    fail(f"{location} schema violation: {first.message}")


@lru_cache(maxsize=None)
def load_live_orchestrator_class_ids() -> set[str]:
    payload = read_json(AOA_AGENTS_ROOT / "generated" / "orchestrator_class_catalog.min.json")
    if not isinstance(payload, dict):
        fail("aoa-agents generated/orchestrator_class_catalog.min.json must be a JSON object")
    entries = payload.get("orchestrator_classes")
    if not isinstance(entries, list):
        fail("aoa-agents generated/orchestrator_class_catalog.min.json must expose orchestrator_classes")
    class_ids: set[str] = set()
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            fail(
                "aoa-agents generated/orchestrator_class_catalog.min.json "
                f"orchestrator_classes[{index}] must be an object"
            )
        class_id = entry.get("id")
        if not isinstance(class_id, str) or not class_id:
            fail(
                "aoa-agents generated/orchestrator_class_catalog.min.json "
                f"orchestrator_classes[{index}] must expose a string id"
            )
        class_ids.add(class_id)
    return class_ids


def validate_orchestrator_class_ref(orchestrator_class_ref: object, *, location: str) -> None:
    if not isinstance(orchestrator_class_ref, str):
        fail(f"{location}.orchestrator_class_ref must be a string")
    repo_name, separator, class_id = orchestrator_class_ref.partition(":")
    if separator != ":" or repo_name != "aoa-agents" or not class_id:
        fail(f"{location}.orchestrator_class_ref must use the form 'aoa-agents:<class_id>'")
    if class_id not in load_live_orchestrator_class_ids():
        fail(
            f"{location}.orchestrator_class_ref must resolve in "
            "aoa-agents/generated/orchestrator_class_catalog.min.json"
        )


def build_expected_quest_catalog_entry(
    quest: dict[str, object], *, source_path: str
) -> dict[str, object]:
    entry: dict[str, object] = {
        "id": quest["id"],
        "title": quest["title"],
        "repo": quest["repo"],
        "theme_ref": quest.get("theme_ref", ""),
        "milestone_ref": quest.get("milestone_ref", ""),
        "state": quest["state"],
        "band": quest["band"],
        "kind": quest["kind"],
        "difficulty": quest["difficulty"],
        "risk": quest["risk"],
        "owner_surface": quest["owner_surface"],
        "source_path": source_path,
        "public_safe": quest["public_safe"],
    }
    for optional_key in (
        "orchestrator_class_ref",
        "capability_target",
        "playbook_family_refs",
        "proof_surface_refs",
        "memory_surface_refs",
    ):
        if optional_key in quest:
            entry[optional_key] = quest[optional_key]
    return entry


def build_expected_quest_dispatch_entry(
    quest: dict[str, object], *, quest_id: str, source_path: str
) -> dict[str, object]:
    activation = quest.get("activation")
    if not isinstance(activation, dict):
        activation = {}
    requires_artifacts = ["recurrence_evidence", "promotion_decision"] if quest.get("kind") == "harvest" else [
        "bounded_plan",
        "work_result",
        "verification_result",
    ]
    entry: dict[str, object] = {
        "schema_version": "quest_dispatch_v1",
        "id": quest["id"],
        "repo": quest["repo"],
        "state": quest["state"],
        "band": quest["band"],
        "difficulty": quest["difficulty"],
        "risk": quest["risk"],
        "control_mode": quest["control_mode"],
        "delegate_tier": quest["delegate_tier"],
        "split_required": quest["split_required"],
        "write_scope": quest["write_scope"],
        "requires_artifacts": requires_artifacts,
        "activation_mode": activation.get("mode"),
        "source_path": source_path,
        "public_safe": quest["public_safe"],
    }
    if "fallback_tier" in quest:
        entry["fallback_tier"] = quest.get("fallback_tier")
    if "wrapper_class" in quest:
        entry["wrapper_class"] = quest.get("wrapper_class")
    for optional_key in ("orchestrator_class_ref", "capability_target"):
        if optional_key in quest:
            entry[optional_key] = quest.get(optional_key)
    return entry


def build_quest_catalog_projection(repo_root: Path = REPO_ROOT) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    for quest_id in discover_questbook_quest_ids(repo_root):
        quest_path = repo_root / "quests" / f"{quest_id}.yaml"
        payload = read_yaml(quest_path)
        if not isinstance(payload, dict):
            fail(f"{quest_path.relative_to(repo_root).as_posix()} must contain a YAML mapping")
        entries.append(
            build_expected_quest_catalog_entry(
                payload,
                source_path=quest_path.relative_to(repo_root).as_posix(),
            )
        )
    return entries


def build_quest_dispatch_projection(repo_root: Path = REPO_ROOT) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    for quest_id in discover_questbook_quest_ids(repo_root):
        quest_path = repo_root / "quests" / f"{quest_id}.yaml"
        payload = read_yaml(quest_path)
        if not isinstance(payload, dict):
            fail(f"{quest_path.relative_to(repo_root).as_posix()} must contain a YAML mapping")
        entries.append(
            build_expected_quest_dispatch_entry(
                payload,
                quest_id=quest_id,
                source_path=quest_path.relative_to(repo_root).as_posix(),
            )
        )
    return entries


def parse_scalar(value: str) -> str:
    scalar = value.strip()
    if len(scalar) >= 2 and scalar[0] in {"'", '"'} and scalar[-1] == scalar[0]:
        return scalar[1:-1]
    return scalar


def parse_frontmatter(text: str, path: Path) -> tuple[dict[str, object], str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        fail(f"{path.relative_to(REPO_ROOT).as_posix()} must start with YAML frontmatter")

    frontmatter: dict[str, object] = {}
    current_key: str | None = None
    body_start = 0

    for index in range(1, len(lines)):
        line = lines[index]
        if line.strip() == "---":
            body_start = index + 1
            break
        if not line.strip():
            continue
        if line.startswith("  - ") or line.startswith("- "):
            if current_key is None:
                fail(f"{path.relative_to(REPO_ROOT).as_posix()} has a list item without a key in frontmatter")
            frontmatter.setdefault(current_key, [])
            assert isinstance(frontmatter[current_key], list)
            frontmatter[current_key].append(parse_scalar(line.split("-", 1)[1]))
            continue
        if ":" not in line:
            fail(f"{path.relative_to(REPO_ROOT).as_posix()} has an invalid frontmatter line: {line}")
        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if not value:
            frontmatter[key] = []
            current_key = key
            continue
        frontmatter[key] = parse_scalar(value)
        current_key = key
    else:
        fail(f"{path.relative_to(REPO_ROOT).as_posix()} is missing the closing YAML frontmatter boundary")

    return frontmatter, "\n".join(lines[body_start:])


def markdown_sections(body: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current_heading: str | None = None
    current_lines: list[str] = []
    for line in body.splitlines():
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


def authored_bundle_paths() -> list[Path]:
    if not PLAYBOOK_ROOT.exists():
        return []
    return sorted(path for path in PLAYBOOK_ROOT.rglob("PLAYBOOK.md") if path.is_file())


def validate_schema_surface() -> None:
    schema = read_json(SCHEMA_PATH)
    if not isinstance(schema, dict):
        fail("schema file must contain a JSON object")
    required_top_level = {"$schema", "$id", "title", "type", "properties", "required"}
    missing = sorted(required_top_level - set(schema))
    if missing:
        fail(f"schema is missing required top-level keys: {', '.join(missing)}")
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        fail("schema must expose top-level properties")
    playbooks = properties.get("playbooks")
    if not isinstance(playbooks, dict):
        fail("schema must expose a playbooks property")
    items = playbooks.get("items")
    if not isinstance(items, dict):
        fail("schema playbooks.items must be an object schema")
    validate_return_contract_schema(items, location="playbook registry item schema")
    validate_memo_recall_spec_schema(items, location="playbook registry item schema")


def validate_activation_schema_surface() -> dict[str, object]:
    schema = read_json(ACTIVATION_SCHEMA_PATH)
    if not isinstance(schema, dict):
        fail("playbook activation schema file must contain a JSON object")
    required_top_level = {"$schema", "$id", "title", "type", "properties", "required"}
    missing = sorted(required_top_level - set(schema))
    if missing:
        fail(f"playbook activation schema is missing required top-level keys: {', '.join(missing)}")
    if schema.get("type") != "object":
        fail("playbook activation schema must declare type 'object'")
    properties = schema.get("properties")
    if not isinstance(properties, dict) or "surface_type" not in properties:
        fail("playbook activation schema must expose a surface_type property")
    surface_type = properties["surface_type"]
    if not isinstance(surface_type, dict) or surface_type.get("const") != "playbook_activation_surface":
        fail("playbook activation schema must pin surface_type.const to 'playbook_activation_surface'")
    validate_return_contract_schema(schema, location="playbook activation schema")
    validate_memo_recall_spec_schema(schema, location="playbook activation schema")
    return schema


def validate_federation_schema_surface() -> dict[str, object]:
    schema = read_json(FEDERATION_SCHEMA_PATH)
    if not isinstance(schema, dict):
        fail("playbook federation schema file must contain a JSON object")
    required_top_level = {"$schema", "$id", "title", "type", "properties", "required"}
    missing = sorted(required_top_level - set(schema))
    if missing:
        fail(f"playbook federation schema is missing required top-level keys: {', '.join(missing)}")
    if schema.get("type") != "object":
        fail("playbook federation schema must declare type 'object'")
    properties = schema.get("properties")
    if not isinstance(properties, dict) or "surface_type" not in properties:
        fail("playbook federation schema must expose a surface_type property")
    surface_type = properties["surface_type"]
    if not isinstance(surface_type, dict) or surface_type.get("const") != "playbook_federation_surface":
        fail("playbook federation schema must pin surface_type.const to 'playbook_federation_surface'")
    validate_memo_recall_spec_schema(schema, location="playbook federation schema")
    return schema


def validate_review_status_schema_surface() -> dict[str, object]:
    schema = read_json(REVIEW_STATUS_SCHEMA_PATH)
    if not isinstance(schema, dict):
        fail("playbook review-status schema file must contain a JSON object")
    required_top_level = {"$schema", "$id", "title", "type", "properties", "required"}
    missing = sorted(required_top_level - set(schema))
    if missing:
        fail(f"playbook review-status schema is missing required top-level keys: {', '.join(missing)}")
    if schema.get("type") != "object":
        fail("playbook review-status schema must declare type 'object'")
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        fail("playbook review-status schema must expose properties")
    playbooks = properties.get("playbooks")
    if not isinstance(playbooks, dict):
        fail("playbook review-status schema must expose a playbooks property")
    items = playbooks.get("items")
    if not isinstance(items, dict):
        fail("playbook review-status schema playbooks.items must be an object schema")
    composition_summary = items.get("properties", {}).get("composition_signal_summary")
    if not isinstance(composition_summary, dict):
        fail("playbook review-status schema must expose composition_signal_summary")
    verdict_field = items.get("properties", {}).get("gate_verdict")
    if not isinstance(verdict_field, dict) or set(verdict_field.get("enum", ())) != set(ALLOWED_GATE_VERDICT_TOKENS):
        fail("playbook review-status schema must pin gate_verdict to the allowed verdict tokens")
    return schema


def validate_review_packet_contracts_schema_surface() -> dict[str, object]:
    schema = read_json(REVIEW_PACKET_CONTRACTS_SCHEMA_PATH)
    if not isinstance(schema, dict):
        fail("playbook review-packet contracts schema file must contain a JSON object")
    required_top_level = {"$schema", "$id", "title", "type", "properties", "required"}
    missing = sorted(required_top_level - set(schema))
    if missing:
        fail(
            "playbook review-packet contracts schema is missing required top-level keys: "
            + ", ".join(missing)
        )
    if schema.get("type") != "object":
        fail("playbook review-packet contracts schema must declare type 'object'")
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        fail("playbook review-packet contracts schema must expose properties")
    playbooks = properties.get("playbooks")
    if not isinstance(playbooks, dict):
        fail("playbook review-packet contracts schema must expose a playbooks property")
    items = playbooks.get("items")
    if not isinstance(items, dict):
        fail("playbook review-packet contracts schema playbooks.items must be an object schema")
    candidate_packet_kinds = items.get("properties", {}).get("candidate_packet_kinds")
    if not isinstance(candidate_packet_kinds, dict):
        fail("playbook review-packet contracts schema must expose candidate_packet_kinds")
    allowed_packet_kinds = {
        "memo_candidate",
        "runtime_evidence_selection_candidate",
        "artifact_hook_candidate",
    }
    packet_kind_items = candidate_packet_kinds.get("items")
    if not isinstance(packet_kind_items, dict) or set(packet_kind_items.get("enum", ())) != allowed_packet_kinds:
        fail("playbook review-packet contracts schema must pin candidate_packet_kinds to the allowed packet kinds")
    return schema


def validate_antifragility_stress_surfaces() -> None:
    readme = read_text(REPO_ROOT / "README.md")
    docs_readme = read_text(REPO_ROOT / "docs" / "README.md")
    lanes_doc = read_text(PLAYBOOK_STRESS_LANES_DOC_PATH)
    harvest_doc = read_text(PLAYBOOK_STRESS_HARVEST_DOC_PATH)

    for token in ("docs/PLAYBOOK_STRESS_LANES.md", "docs/PLAYBOOK_STRESS_HARVEST.md"):
        if token not in readme:
            fail(f"README.md must link {token}")
    for token in ("PLAYBOOK_STRESS_LANES", "PLAYBOOK_STRESS_HARVEST"):
        if token not in docs_readme:
            fail(f"docs/README.md must mention {token}")
    for snippet in REQUIRED_PLAYBOOK_STRESS_LANE_SNIPPETS:
        if snippet not in lanes_doc:
            fail(f"docs/PLAYBOOK_STRESS_LANES.md is missing required stress-lane guidance: {snippet}")
    for snippet in REQUIRED_PLAYBOOK_STRESS_HARVEST_SNIPPETS:
        if snippet not in harvest_doc:
            fail(f"docs/PLAYBOOK_STRESS_HARVEST.md is missing required harvest guidance: {snippet}")

    for schema_path, example_path in (
        (PLAYBOOK_STRESS_LANE_SCHEMA_PATH, PLAYBOOK_STRESS_LANE_EXAMPLE_PATH),
        (PLAYBOOK_REENTRY_GATE_SCHEMA_PATH, PLAYBOOK_REENTRY_GATE_EXAMPLE_PATH),
    ):
        schema = read_json(schema_path)
        if not isinstance(schema, dict):
            fail(f"{display_path(schema_path)} must remain a JSON object")
        Draft202012Validator.check_schema(schema)
        payload = read_json(example_path)
        errors = sorted(
            Draft202012Validator(schema).iter_errors(payload),
            key=lambda error: (list(error.absolute_path), error.message),
        )
        if errors:
            first = errors[0]
            error_path = format_schema_path(list(first.absolute_path))
            if error_path:
                fail(f"{display_path(example_path)} schema violation at '{error_path}': {first.message}")
            fail(f"{display_path(example_path)} schema violation: {first.message}")
        if isinstance(payload, dict):
            playbook_ref = payload.get("playbook_id")
            error = local_ref_error(playbook_ref, f"{display_path(example_path)}.playbook_id")
            if error is not None:
                fail(error)


def validate_codex_plane_rollout_cycle_companion() -> None:
    readme = read_text(REPO_ROOT / "README.md")
    docs_readme = read_text(REPO_ROOT / "docs" / "README.md")
    execution_seam = read_text(REPO_ROOT / "docs" / "PLAYBOOK_EXECUTION_SEAM.md")
    workflow = read_text(REAL_RUN_WORKFLOW_PATH)
    session_growth_cycle = read_text(REPO_ROOT / "playbooks" / "session-growth-cycle" / "PLAYBOOK.md")
    cycle_doc = read_text(CODEX_PLANE_ROLLOUT_CYCLE_DOC_PATH)
    cadence_doc = read_text(REPO_ROOT / "docs" / "TRUSTED_ROLLOUT_CAMPAIGN_CADENCE.md")

    for text, location in (
        (readme, "README.md"),
        (docs_readme, "docs/README.md"),
    ):
        if "CODEX_PLANE_ROLLOUT_CYCLE.md" not in text:
            fail(f"{location} must mention docs/CODEX_PLANE_ROLLOUT_CYCLE.md")
        if "TRUSTED_ROLLOUT_CAMPAIGN_CADENCE.md" not in text:
            fail(f"{location} must mention docs/TRUSTED_ROLLOUT_CAMPAIGN_CADENCE.md")
    if "examples/codex_plane_rollout_lane.example.json" not in readme:
        fail("README.md must mention examples/codex_plane_rollout_lane.example.json")
    if "docs/CODEX_PLANE_ROLLOUT_CYCLE.md" not in execution_seam:
        fail("docs/PLAYBOOK_EXECUTION_SEAM.md must mention docs/CODEX_PLANE_ROLLOUT_CYCLE.md")
    if "docs/CODEX_PLANE_ROLLOUT_CYCLE.md" not in workflow:
        fail("docs/PLAYBOOK_REAL_RUN_WORKFLOW.md must mention docs/CODEX_PLANE_ROLLOUT_CYCLE.md")
    for token in (
        "docs/CODEX_PLANE_ROLLOUT_CYCLE.md",
        "examples/codex_plane_rollout_lane.example.json",
        "hidden rollout runner",
    ):
        if token not in session_growth_cycle:
            fail(f"playbooks/session-growth-cycle/PLAYBOOK.md must mention '{token}'")

    for snippet in CODEX_PLANE_ROLLOUT_DOC_SNIPPETS:
        if snippet not in cycle_doc:
            fail(f"docs/CODEX_PLANE_ROLLOUT_CYCLE.md is missing required guidance: {snippet}")
    for snippet in (
        "AOA-P-0028",
        "rollout_campaign_window",
        "drift_review_window",
        "rollback_followthrough_window",
        "not a second playbook",
        "not a hidden runner",
    ):
        if snippet not in cadence_doc:
            fail(f"docs/TRUSTED_ROLLOUT_CAMPAIGN_CADENCE.md is missing required guidance: {snippet}")

    payload = read_json(CODEX_PLANE_ROLLOUT_LANE_EXAMPLE_PATH)
    if not isinstance(payload, dict):
        fail("examples/codex_plane_rollout_lane.example.json must contain a JSON object")
    if payload.get("playbook_id") != "AOA-P-0028":
        fail("examples/codex_plane_rollout_lane.example.json must keep playbook_id AOA-P-0028")
    if payload.get("playbook") != "trusted-rollout-operations":
        fail("examples/codex_plane_rollout_lane.example.json must keep playbook trusted-rollout-operations")
    if payload.get("lane") != "codex-plane-rollout":
        fail("examples/codex_plane_rollout_lane.example.json must keep lane codex-plane-rollout")
    if payload.get("workspace_scope") != "shared-root":
        fail("examples/codex_plane_rollout_lane.example.json must keep workspace_scope shared-root")
    if payload.get("success_condition") != "latest_state=stabilized":
        fail("examples/codex_plane_rollout_lane.example.json must keep success_condition latest_state=stabilized")

    phases = payload.get("phases")
    if not isinstance(phases, list):
        fail("examples/codex_plane_rollout_lane.example.json phases must be a list")
    actual_phases: list[tuple[str, str]] = []
    for index, phase in enumerate(phases):
        if not isinstance(phase, dict):
            fail(f"examples/codex_plane_rollout_lane.example.json phases[{index}] must be an object")
        name = phase.get("name")
        artifact = phase.get("required_artifact")
        if not isinstance(name, str) or not isinstance(artifact, str):
            fail(
                "examples/codex_plane_rollout_lane.example.json phases entries must keep "
                "string name and required_artifact"
            )
        actual_phases.append((name, artifact))
    if tuple(actual_phases) != CODEX_PLANE_ROLLOUT_PHASES:
        fail("examples/codex_plane_rollout_lane.example.json phases drifted from the rollout lane order")

    required_artifacts = payload.get("required_artifacts")
    if tuple(required_artifacts or ()) != CODEX_PLANE_REQUIRED_ARTIFACTS:
        fail("examples/codex_plane_rollout_lane.example.json required_artifacts drifted")
    stop_before_apply = payload.get("stop_before_apply")
    if tuple(stop_before_apply or ()) != CODEX_PLANE_STOP_BEFORE_APPLY:
        fail("examples/codex_plane_rollout_lane.example.json stop_before_apply drifted")
    rollback_triggers = payload.get("rollback_triggers")
    if tuple(rollback_triggers or ()) != CODEX_PLANE_ROLLBACK_TRIGGERS:
        fail("examples/codex_plane_rollout_lane.example.json rollback_triggers drifted")

    stable_mcp_names = payload.get("stable_mcp_names")
    if not isinstance(stable_mcp_names, list) or set(stable_mcp_names) != CODEX_PLANE_STABLE_MCP_NAMES:
        fail("examples/codex_plane_rollout_lane.example.json must keep the stable MCP name set")

    trust_payload = read_json(AOA_8DIONYSUS_ROOT / "examples" / "codex_plane_trust_state.example.json")
    regeneration_payload = read_json(
        AOA_8DIONYSUS_ROOT / "examples" / "codex_plane_regeneration_report.example.json"
    )
    receipt_payload = read_json(AOA_8DIONYSUS_ROOT / "examples" / "codex_plane_rollout_receipt.example.json")
    rollout_latest_payload = read_json(
        AOA_8DIONYSUS_ROOT / "generated" / "codex" / "rollout" / "rollout_latest.min.json"
    )
    rollback_payload = read_json(
        AOA_8DIONYSUS_ROOT / "generated" / "codex" / "rollout" / "rollback_windows.min.json"
    )
    status_payload = read_json(AOA_SDK_ROOT / "examples" / "codex_plane_deploy_status_snapshot.example.json")
    stats_payload = read_json(AOA_STATS_ROOT / "examples" / "codex_plane_deployment_summary.example.json")
    drift_summary_payload = read_json(AOA_STATS_ROOT / "generated" / "codex_rollout_drift_summary.min.json")

    for sibling_payload, label in (
        (trust_payload, "8Dionysus trust-state example"),
        (regeneration_payload, "8Dionysus regeneration-report example"),
        (receipt_payload, "8Dionysus rollout-receipt example"),
        (rollout_latest_payload, "8Dionysus rollout-latest generated surface"),
        (rollback_payload, "8Dionysus rollback-windows generated surface"),
        (status_payload, "aoa-sdk deploy-status example"),
        (stats_payload, "aoa-stats deployment-summary example"),
        (drift_summary_payload, "aoa-stats rollout-drift generated surface"),
    ):
        if not isinstance(sibling_payload, dict):
            fail(f"{label} must remain a JSON object")

    evidence_refs = payload.get("evidence_refs")
    if not isinstance(evidence_refs, list) or len(evidence_refs) != 4 or len(evidence_refs) != len(set(evidence_refs)):
        fail("examples/codex_plane_rollout_lane.example.json must keep four unique evidence_refs")
    rollback_windows = rollback_payload.get("rollback_windows")
    if not isinstance(rollback_windows, list) or not rollback_windows:
        fail("8Dionysus rollback-windows generated surface must expose at least one rollback window")
    first_rollback_window = rollback_windows[0]
    if not isinstance(first_rollback_window, dict):
        fail("8Dionysus rollback-windows generated surface entries must remain objects")
    expected_evidence_refs = [
        rollout_latest_payload.get("latest_stable_rollout_campaign_ref"),
        rollout_latest_payload.get("latest_rollout_campaign_ref"),
        drift_summary_payload.get("drift_window_ref"),
        first_rollback_window.get("rollback_window_ref"),
    ]
    if evidence_refs != expected_evidence_refs:
        fail("examples/codex_plane_rollout_lane.example.json evidence_refs must match sibling rollout examples")

    if status_payload.get("latest_trust_state_ref") != trust_payload.get("trust_state_id"):
        fail("aoa-sdk deploy-status example must point at the 8Dionysus trust-state example")
    if status_payload.get("latest_rollout_receipt_ref") != receipt_payload.get("rollout_receipt_id"):
        fail("aoa-sdk deploy-status example must point at the 8Dionysus rollout-receipt example")
    if status_payload.get("rollout_state") != "verified":
        fail("aoa-sdk deploy-status example must keep rollout_state verified")
    status_mcp_names = status_payload.get("active_mcp_servers")
    if not isinstance(status_mcp_names, list) or set(status_mcp_names) != CODEX_PLANE_STABLE_MCP_NAMES:
        fail("aoa-sdk deploy-status example must keep the stable MCP name set")

    if receipt_payload.get("regeneration_report_id") != regeneration_payload.get("regeneration_report_id"):
        fail("8Dionysus rollout-receipt example must point at the 8Dionysus regeneration-report example")

    if stats_payload.get("latest_receipt_ref") != receipt_payload.get("rollout_receipt_id"):
        fail("aoa-stats deployment summary example must point at the 8Dionysus rollout receipt")
    if stats_payload.get("latest_rollout_state") != "verified":
        fail("aoa-stats deployment summary example must keep latest_rollout_state verified")
    stats_mcp_names = stats_payload.get("stable_mcp_name_set")
    if not isinstance(stats_mcp_names, list) or set(stats_mcp_names) != CODEX_PLANE_STABLE_MCP_NAMES:
        fail("aoa-stats deployment summary example must keep the stable MCP name set")


def validate_return_contract_schema(schema: dict[str, object], *, location: str) -> None:
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        fail(f"{location} must expose properties")

    for field_name in RETURN_FIELD_NAMES:
        if field_name not in properties:
            fail(f"{location} must define '{field_name}'")

    return_posture = properties["return_posture"]
    if not isinstance(return_posture, dict) or set(return_posture.get("enum", ())) != ALLOWED_RETURN_POSTURE:
        fail(f"{location} must define return_posture with the allowed posture set")

    return_anchor_artifacts = properties["return_anchor_artifacts"]
    if not isinstance(return_anchor_artifacts, dict):
        fail(f"{location} must define return_anchor_artifacts as an array schema")
    return_anchor_items = return_anchor_artifacts.get("items")
    if (
        return_anchor_artifacts.get("type") != "array"
        or not isinstance(return_anchor_items, dict)
        or return_anchor_items.get("type") != "string"
    ):
        fail(f"{location} must define return_anchor_artifacts as an array of strings")

    return_reentry_modes = properties["return_reentry_modes"]
    return_reentry_items = return_reentry_modes.get("items") if isinstance(return_reentry_modes, dict) else None
    if (
        not isinstance(return_reentry_modes, dict)
        or return_reentry_modes.get("type") != "array"
        or not isinstance(return_reentry_items, dict)
        or set(return_reentry_items.get("enum", ())) != ALLOWED_RETURN_REENTRY_MODES
    ):
        fail(f"{location} must define return_reentry_modes with the allowed re-entry mode set")

    all_of = schema.get("allOf")
    if not isinstance(all_of, list) or len(all_of) < 3:
        fail(f"{location} must define allOf conditional rules for return_* field dependencies")

    expected_rules = {
        ("return_posture", ("return_anchor_artifacts", "return_reentry_modes")),
        ("return_anchor_artifacts", ("return_posture",)),
        ("return_reentry_modes", ("return_posture",)),
    }
    seen_rules: set[tuple[str, tuple[str, ...]]] = set()
    for clause in all_of:
        if not isinstance(clause, dict):
            continue
        condition = clause.get("if")
        consequence = clause.get("then")
        if not isinstance(condition, dict) or not isinstance(consequence, dict):
            continue
        condition_required = condition.get("required")
        consequence_required = consequence.get("required")
        if (
            isinstance(condition_required, list)
            and len(condition_required) == 1
            and all(isinstance(item, str) for item in consequence_required or [])
        ):
            seen_rules.add((condition_required[0], tuple(str(item) for item in consequence_required)))

    missing_rules = expected_rules - seen_rules
    if missing_rules:
        fail(f"{location} is missing required conditional return_* dependency rules")


def validate_return_configuration(payload: dict[str, object], *, location: str) -> None:
    has_return_posture = "return_posture" in payload
    has_return_anchor_artifacts = "return_anchor_artifacts" in payload
    has_return_reentry_modes = "return_reentry_modes" in payload
    return_posture = payload.get("return_posture")
    return_anchor_artifacts = payload.get("return_anchor_artifacts")
    return_reentry_modes = payload.get("return_reentry_modes")

    if not has_return_posture:
        if has_return_anchor_artifacts:
            fail(f"{location}.return_anchor_artifacts must not appear without return_posture")
        if has_return_reentry_modes:
            fail(f"{location}.return_reentry_modes must not appear without return_posture")
        return

    if return_posture not in ALLOWED_RETURN_POSTURE:
        fail(f"{location}.return_posture '{return_posture}' is not allowed")

    if not isinstance(return_anchor_artifacts, list) or not return_anchor_artifacts:
        fail(f"{location}.return_anchor_artifacts must be a non-empty list when return_posture is present")
    for item in return_anchor_artifacts:
        if not isinstance(item, str) or len(item) < 2:
            fail(f"{location}.return_anchor_artifacts contains an invalid entry")

    if not isinstance(return_reentry_modes, list) or not return_reentry_modes:
        fail(f"{location}.return_reentry_modes must be a non-empty list when return_posture is present")
    for item in return_reentry_modes:
        if item not in ALLOWED_RETURN_REENTRY_MODES:
            fail(f"{location}.return_reentry_modes contains an invalid entry: {item}")


def validate_memo_recall_spec_schema(schema: dict[str, object], *, location: str) -> None:
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        fail(f"{location} must expose properties")

    for field_name in MEMO_SPEC_FIELD_NAMES:
        if field_name not in properties:
            fail(f"{location} must define '{field_name}'")

    memo_recall_modes = properties["memo_recall_modes"]
    memo_recall_mode_items = memo_recall_modes.get("items") if isinstance(memo_recall_modes, dict) else None
    if (
        not isinstance(memo_recall_modes, dict)
        or memo_recall_modes.get("type") != "array"
        or not isinstance(memo_recall_mode_items, dict)
        or set(memo_recall_mode_items.get("enum", ())) != ALLOWED_MEMO_RECALL_MODES
    ):
        fail(f"{location} must define memo_recall_modes with the allowed recall-mode set")

    for field_name in ("memo_scope_default", "memo_scope_ceiling"):
        field = properties[field_name]
        if not isinstance(field, dict) or set(field.get("enum", ())) != ALLOWED_MEMO_SCOPES:
            fail(f"{location} must define {field_name} with the allowed scope set")

    memo_read_path = properties["memo_read_path"]
    if not isinstance(memo_read_path, dict) or set(memo_read_path.get("enum", ())) != ALLOWED_MEMO_READ_PATHS:
        fail(f"{location} must define memo_read_path with the allowed read-path set")

    memo_checkpoint_posture = properties["memo_checkpoint_posture"]
    if (
        not isinstance(memo_checkpoint_posture, dict)
        or set(memo_checkpoint_posture.get("enum", ())) != ALLOWED_MEMO_CHECKPOINT_POSTURES
    ):
        fail(f"{location} must define memo_checkpoint_posture with the allowed checkpoint posture set")

    memo_source_route_policy = properties["memo_source_route_policy"]
    if (
        not isinstance(memo_source_route_policy, dict)
        or set(memo_source_route_policy.get("enum", ())) != ALLOWED_MEMO_SOURCE_ROUTE_POLICIES
    ):
        fail(f"{location} must define memo_source_route_policy with the allowed source-route policy set")


def validate_memo_recall_spec(
    payload: dict[str, object],
    *,
    location: str,
    required: bool,
) -> None:
    present = {field_name for field_name in MEMO_SPEC_FIELD_NAMES if field_name in payload}
    if not present:
        if required:
            fail(f"{location} must expose the full memo recall spec for the runtime-facing cohort")
        return

    missing = [field_name for field_name in MEMO_SPEC_FIELD_NAMES if field_name not in payload]
    if missing:
        fail(
            f"{location} must expose the full memo recall spec together; missing: "
            + ", ".join(missing)
        )

    memo_recall_modes = payload["memo_recall_modes"]
    if not isinstance(memo_recall_modes, list) or not memo_recall_modes:
        fail(f"{location}.memo_recall_modes must be a non-empty list when present")
    for item in memo_recall_modes:
        if item not in ALLOWED_MEMO_RECALL_MODES:
            fail(f"{location}.memo_recall_modes contains an invalid entry: {item}")

    memo_scope_default = payload["memo_scope_default"]
    memo_scope_ceiling = payload["memo_scope_ceiling"]
    if memo_scope_default not in ALLOWED_MEMO_SCOPES:
        fail(f"{location}.memo_scope_default '{memo_scope_default}' is not allowed")
    if memo_scope_ceiling not in ALLOWED_MEMO_SCOPES:
        fail(f"{location}.memo_scope_ceiling '{memo_scope_ceiling}' is not allowed")
    if MEMO_SCOPE_ORDER[memo_scope_default] > MEMO_SCOPE_ORDER[memo_scope_ceiling]:
        fail(f"{location}.memo_scope_default cannot be wider than memo_scope_ceiling")

    memo_read_path = payload["memo_read_path"]
    if memo_read_path not in ALLOWED_MEMO_READ_PATHS:
        fail(f"{location}.memo_read_path '{memo_read_path}' is not allowed")

    memo_checkpoint_posture = payload["memo_checkpoint_posture"]
    if memo_checkpoint_posture not in ALLOWED_MEMO_CHECKPOINT_POSTURES:
        fail(f"{location}.memo_checkpoint_posture '{memo_checkpoint_posture}' is not allowed")

    memo_source_route_policy = payload["memo_source_route_policy"]
    if memo_source_route_policy not in ALLOWED_MEMO_SOURCE_ROUTE_POLICIES:
        fail(f"{location}.memo_source_route_policy '{memo_source_route_policy}' is not allowed")


def validate_runtime_memo_spec_expectation(payload: dict[str, object], *, playbook_id: str, location: str) -> None:
    expected = RUNTIME_MEMO_SPEC_EXPECTATIONS.get(playbook_id)
    if expected is None:
        return

    expected_modes = expected["memo_recall_modes"]
    assert isinstance(expected_modes, tuple)
    actual_modes = payload.get("memo_recall_modes")
    if tuple(actual_modes) != expected_modes:
        fail(f"{location}.memo_recall_modes must equal {list(expected_modes)}")

    for field_name in (
        "memo_scope_default",
        "memo_scope_ceiling",
        "memo_read_path",
        "memo_checkpoint_posture",
        "memo_source_route_policy",
    ):
        if payload.get(field_name) != expected[field_name]:
            fail(f"{location}.{field_name} must equal '{expected[field_name]}'")


def has_semantic_or_lineage_recall_contract(contract_refs: list[str]) -> bool:
    return any(contract_ref in SEMANTIC_LINEAGE_MEMO_CONTRACT_REFS for contract_ref in contract_refs)


def validate_registry() -> dict[str, dict[str, object]]:
    payload = read_json(REGISTRY_PATH)
    if not isinstance(payload, dict):
        fail("playbook registry must be a JSON object")

    for key in ("version", "layer", "playbooks"):
        if key not in payload:
            fail(f"playbook registry is missing required key '{key}'")

    if not isinstance(payload["version"], int) or payload["version"] < 1:
        fail("registry 'version' must be an integer >= 1")
    if payload["layer"] != "aoa-playbooks":
        fail("registry 'layer' must equal 'aoa-playbooks'")

    playbooks = payload["playbooks"]
    if not isinstance(playbooks, list) or not playbooks:
        fail("registry 'playbooks' must be a non-empty list")

    seen_ids: set[str] = set()
    required_seed = {"repo-bootstrap", "safe-change-rollout", "bounded-research-pass", "release-prep", "memory-curation-pass"}
    seen_names: set[str] = set()
    playbooks_by_id: dict[str, dict[str, object]] = {}

    for index, playbook in enumerate(playbooks):
        location = f"playbooks[{index}]"
        if not isinstance(playbook, dict):
            fail(f"{location} must be an object")

        for key in (
            "id",
            "name",
            "status",
            "summary",
            "scenario",
            "trigger",
            "prerequisites",
            "participating_agents",
            "required_skill_families",
            "evaluation_posture",
            "memory_posture",
            "fallback_mode",
            "expected_artifacts",
        ):
            if key not in playbook:
                fail(f"{location} is missing required key '{key}'")

        playbook_id = playbook["id"]
        name = playbook["name"]
        status = playbook["status"]
        summary = playbook["summary"]
        scenario = playbook["scenario"]
        trigger = playbook["trigger"]
        prerequisites = playbook["prerequisites"]
        participating_agents = playbook["participating_agents"]
        required_skill_families = playbook["required_skill_families"]
        evaluation_posture = playbook["evaluation_posture"]
        memory_posture = playbook["memory_posture"]
        fallback_mode = playbook["fallback_mode"]
        expected_artifacts = playbook["expected_artifacts"]

        if not isinstance(playbook_id, str) or len(playbook_id) < 3:
            fail(f"{location}.id must be a string of length >= 3")
        if playbook_id in seen_ids:
            fail(f"duplicate playbook id in registry: '{playbook_id}'")
        seen_ids.add(playbook_id)
        playbooks_by_id[playbook_id] = playbook

        if not isinstance(name, str) or len(name) < 3:
            fail(f"{location}.name must be a string of length >= 3")
        if name in seen_names:
            fail(f"duplicate playbook name in registry: '{name}'")
        seen_names.add(name)
        if status not in ALLOWED_STATUS:
            fail(f"{location}.status '{status}' is not allowed")
        if not isinstance(summary, str) or len(summary) < 10:
            fail(f"{location}.summary must be a string of length >= 10")
        if not isinstance(scenario, str) or len(scenario) < 3:
            fail(f"{location}.scenario must be a string of length >= 3")
        if not isinstance(trigger, str) or len(trigger) < 3:
            fail(f"{location}.trigger must be a string of length >= 3")

        for array_name, value in (
            ("prerequisites", prerequisites),
            ("participating_agents", participating_agents),
            ("required_skill_families", required_skill_families),
            ("expected_artifacts", expected_artifacts),
        ):
            if not isinstance(value, list) or not value:
                fail(f"{location}.{array_name} must be a non-empty list")
            for item in value:
                if not isinstance(item, str) or len(item) < 2:
                    fail(f"{location}.{array_name} contains an invalid entry")

        eval_anchors = playbook.get("eval_anchors")
        if eval_anchors is not None:
            if not isinstance(eval_anchors, list) or not eval_anchors:
                fail(f"{location}.eval_anchors must be a non-empty list when present")
            for anchor in eval_anchors:
                if not isinstance(anchor, str) or len(anchor) < 3:
                    fail(f"{location}.eval_anchors contains an invalid entry")

        if evaluation_posture not in ALLOWED_EVAL_POSTURE:
            fail(f"{location}.evaluation_posture '{evaluation_posture}' is not allowed")
        if memory_posture not in ALLOWED_MEMORY_POSTURE:
            fail(f"{location}.memory_posture '{memory_posture}' is not allowed")
        if fallback_mode not in ALLOWED_FALLBACK:
            fail(f"{location}.fallback_mode '{fallback_mode}' is not allowed")
        validate_return_configuration(playbook, location=location)
        validate_memo_recall_spec(
            playbook,
            location=location,
            required=playbook_id in RUNTIME_MEMO_SPEC_PLAYBOOK_IDS,
        )
        validate_runtime_memo_spec_expectation(playbook, playbook_id=playbook_id, location=location)

    missing_seed = sorted(required_seed - seen_names)
    if missing_seed:
        fail(f"playbook registry is missing required seed playbooks: {', '.join(missing_seed)}")
    return playbooks_by_id


def load_agent_names() -> set[str]:
    payload = read_json(AGENT_REGISTRY_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("agents"), list):
        fail("aoa-agents/generated/agent_registry.min.json must contain an 'agents' list")
    agent_names = {
        item["name"]
        for item in payload["agents"]
        if isinstance(item, dict) and isinstance(item.get("name"), str)
    }
    if not agent_names:
        fail("aoa-agents/generated/agent_registry.min.json must list at least one agent")
    return agent_names


def load_model_tier_artifacts() -> set[str]:
    payload = read_json(MODEL_TIER_REGISTRY_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("model_tiers"), list):
        fail("aoa-agents/generated/model_tier_registry.json must contain a 'model_tiers' list")
    artifacts = {
        item["artifact_requirement"]
        for item in payload["model_tiers"]
        if isinstance(item, dict) and isinstance(item.get("artifact_requirement"), str)
    }
    if not artifacts:
        fail("aoa-agents/generated/model_tier_registry.json must list at least one artifact requirement")
    return artifacts


def load_eval_catalog() -> dict[str, dict[str, object]]:
    payload = read_json(EVAL_CATALOG_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("evals"), list):
        fail("aoa-evals/generated/eval_catalog.min.json must contain an 'evals' list")
    evals_by_name: dict[str, dict[str, object]] = {}
    for item in payload["evals"]:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if isinstance(name, str):
            evals_by_name[name] = item
    if not evals_by_name:
        fail("aoa-evals/generated/eval_catalog.min.json must list at least one eval")
    return evals_by_name


def load_skill_catalog() -> dict[str, dict[str, object]]:
    payload = read_json(SKILL_GOVERNANCE_PATH)
    if not isinstance(payload, dict) or not isinstance(payload.get("skills"), list):
        fail("aoa-skills/generated/governance_backlog.json must contain a 'skills' list")
    skills_by_name: dict[str, dict[str, object]] = {}
    for item in payload["skills"]:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if isinstance(name, str):
            skills_by_name[name] = item
    if not skills_by_name:
        fail("aoa-skills/generated/governance_backlog.json must list at least one skill")
    return skills_by_name


def collect_string_field_values(payload: object, field_name: str) -> set[str]:
    values: set[str] = set()
    if isinstance(payload, dict):
        for key, value in payload.items():
            if key == field_name and isinstance(value, str):
                values.add(value)
            values.update(collect_string_field_values(value, field_name))
    elif isinstance(payload, list):
        for item in payload:
            values.update(collect_string_field_values(item, field_name))
    return values


def memo_contract_path(contract_ref: str) -> Path:
    path = (AOA_MEMO_ROOT / contract_ref).resolve()
    try:
        path.relative_to(AOA_MEMO_ROOT)
    except ValueError:
        fail(
            "memo_contract_refs must resolve within aoa-memo: "
            + contract_ref
        )
    return path


def memo_kinds_for_contract(contract_ref: str) -> set[str]:
    path = memo_contract_path(contract_ref)
    payload = read_json(path)
    kinds = collect_string_field_values(payload, "kind")
    kinds.update(collect_string_field_values(payload, "target_kind"))
    if isinstance(payload, dict) and "memory_object_ids" in payload and "timeline" in payload:
        kinds.add("provenance_thread")
    return kinds


def validate_projection_refs(
    *,
    location: str,
    participating_agents: object,
    expected_artifacts: object,
    eval_anchors: object,
    agent_names: set[str],
    model_tier_artifacts: set[str],
    evals_by_name: dict[str, dict[str, object]],
) -> None:
    if not isinstance(participating_agents, list) or not participating_agents:
        fail(f"{location} must expose a non-empty participating_agents list")
    missing_agents = [
        item for item in participating_agents if not isinstance(item, str) or item not in agent_names
    ]
    if missing_agents:
        fail(
            f"{location} references participating_agents that do not resolve in aoa-agents: "
            + ", ".join(str(item) for item in missing_agents)
        )

    if not isinstance(expected_artifacts, list) or not expected_artifacts:
        fail(f"{location} must expose a non-empty expected_artifacts list")
    if location.endswith("AOA-P-0008"):
        unknown_artifacts = [
            item
            for item in expected_artifacts
            if not isinstance(item, str) or item not in model_tier_artifacts
        ]
        if unknown_artifacts:
            fail(
                f"{location} expected_artifacts do not resolve against aoa-agents model-tier artifacts: "
                + ", ".join(str(item) for item in unknown_artifacts)
            )

    if eval_anchors is None:
        return
    if not isinstance(eval_anchors, list) or not eval_anchors:
        fail(f"{location} must expose a non-empty eval_anchors list when present")
    missing_eval_anchors = [
        anchor for anchor in eval_anchors if not isinstance(anchor, str) or anchor not in evals_by_name
    ]
    if missing_eval_anchors:
        fail(
            f"{location} references eval_anchors that do not resolve in aoa-evals: "
            + ", ".join(str(item) for item in missing_eval_anchors)
        )


def activation_surface_for_playbook(playbook_id: str, registry_entry: dict[str, object]) -> dict[str, object]:
    payload: dict[str, object] = {
        "surface_type": "playbook_activation_surface",
        "playbook_id": playbook_id,
        "name": registry_entry["name"],
        "scenario": registry_entry["scenario"],
        "trigger": registry_entry["trigger"],
        "participating_agents": registry_entry["participating_agents"],
        "required_skill_families": registry_entry["required_skill_families"],
        "expected_artifacts": registry_entry["expected_artifacts"],
        "evaluation_posture": registry_entry["evaluation_posture"],
        "memory_posture": registry_entry["memory_posture"],
        "fallback_mode": registry_entry["fallback_mode"],
    }
    if "eval_anchors" in registry_entry:
        payload["eval_anchors"] = registry_entry["eval_anchors"]
    for field_name in RETURN_FIELD_NAMES:
        if field_name in registry_entry:
            payload[field_name] = registry_entry[field_name]
    for field_name in MEMO_SPEC_FIELD_NAMES:
        if field_name in registry_entry:
            payload[field_name] = registry_entry[field_name]
    return payload


def activation_surfaces_for_playbooks(
    playbooks_by_id: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    surfaces: list[dict[str, object]] = []
    for playbook_id in ACTIVATION_COLLECTION_PLAYBOOK_IDS:
        if playbook_id not in playbooks_by_id:
            fail(f"playbook registry is missing required activation target '{playbook_id}'")
        surfaces.append(activation_surface_for_playbook(playbook_id, playbooks_by_id[playbook_id]))
    return surfaces


def validate_activation_collection(
    playbooks_by_id: dict[str, dict[str, object]],
    *,
    agent_names: set[str],
    model_tier_artifacts: set[str],
    evals_by_name: dict[str, dict[str, object]],
) -> None:
    payload = read_json(ACTIVATION_COLLECTION_PATH)
    if not isinstance(payload, list):
        fail("generated/playbook_activation_surfaces.min.json must be a JSON array")

    expected = activation_surfaces_for_playbooks(playbooks_by_id)
    if payload != expected:
        fail(
            "generated/playbook_activation_surfaces.min.json is out of date; "
            "run scripts/generate_playbook_activation_surfaces.py"
        )

    for index, surface in enumerate(payload):
        if not isinstance(surface, dict):
            fail(f"generated/playbook_activation_surfaces.min.json[{index}] must be an object")
        playbook_id = surface.get("playbook_id")
        if not isinstance(playbook_id, str):
            fail(f"generated/playbook_activation_surfaces.min.json[{index}] is missing a string playbook_id")
        validate_memo_recall_spec(
            surface,
            location=f"generated/playbook_activation_surfaces.min.json[{index}]",
            required=playbook_id in RUNTIME_MEMO_SPEC_PLAYBOOK_IDS,
        )
        validate_runtime_memo_spec_expectation(
            surface,
            playbook_id=playbook_id,
            location=f"generated/playbook_activation_surfaces.min.json[{index}]",
        )
        validate_projection_refs(
            location=f"generated/playbook_activation_surfaces.min.json[{index}]:{playbook_id}",
            participating_agents=surface.get("participating_agents"),
            expected_artifacts=surface.get("expected_artifacts"),
            eval_anchors=surface.get("eval_anchors"),
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
        )


def federation_surface_for_frontmatter(frontmatter: dict[str, object]) -> dict[str, object]:
    payload: dict[str, object] = {
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
        payload["eval_anchors"] = frontmatter["eval_anchors"]
    for field_name in MEMO_SPEC_FIELD_NAMES:
        if field_name in frontmatter:
            payload[field_name] = frontmatter[field_name]
    return payload


def validate_federation_bundle(
    *,
    bundle_path: Path,
    frontmatter: dict[str, object],
    sections: dict[str, str],
    skills_by_name: dict[str, dict[str, object]],
) -> None:
    bundle_location = bundle_path.relative_to(REPO_ROOT).as_posix()

    for key in FEDERATION_REQUIRED_FRONTMATTER_KEYS:
        if key not in frontmatter:
            fail(f"{bundle_location} is missing required federation frontmatter '{key}'")

    required_skills = frontmatter["required_skills"]
    memo_contract_refs = frontmatter["memo_contract_refs"]
    memo_writeback_targets = frontmatter["memo_writeback_targets"]
    participating_agents = frontmatter.get("participating_agents")
    eval_anchors = frontmatter.get("eval_anchors")
    playbook_status = str(frontmatter.get("status", ""))
    playbook_id = frontmatter.get("id")
    if not isinstance(playbook_id, str):
        fail(f"{bundle_location} is missing string frontmatter 'id'")

    for field_name, value in (
        ("required_skills", required_skills),
        ("memo_contract_refs", memo_contract_refs),
        ("memo_writeback_targets", memo_writeback_targets),
    ):
        if not isinstance(value, list) or not value:
            fail(f"{bundle_location} federation field '{field_name}' must be a non-empty list")
        for item in value:
            if not isinstance(item, str) or len(item) < 3:
                fail(f"{bundle_location} federation field '{field_name}' contains an invalid entry")

    if not isinstance(eval_anchors, list) or not eval_anchors:
        fail(f"{bundle_location} federation-checked playbooks must expose non-empty 'eval_anchors'")
    validate_memo_recall_spec(
        frontmatter,
        location=bundle_location,
        required=playbook_id in RUNTIME_MEMO_SPEC_PLAYBOOK_IDS,
    )
    validate_runtime_memo_spec_expectation(frontmatter, playbook_id=playbook_id, location=bundle_location)

    if not isinstance(participating_agents, list) or "memory-keeper" not in participating_agents:
        fail(
            f"{bundle_location} federation-checked playbooks with memo writeback targets must include "
            "'memory-keeper' in participating_agents"
        )

    missing_skills: list[str] = []
    invalid_skill_readiness: list[str] = []
    for skill_name in required_skills:
        skill = skills_by_name.get(skill_name)
        if skill is None:
            missing_skills.append(skill_name)
            continue
        if not skill_is_federation_eligible(skill, playbook_status=playbook_status):
            invalid_skill_readiness.append(skill_name)
    if missing_skills:
        fail(
            f"{bundle_location} required_skills do not resolve in aoa-skills/generated/governance_backlog.json: "
            + ", ".join(missing_skills)
        )
    if invalid_skill_readiness:
        fail(
            f"{bundle_location} required_skills are not federation-ready in aoa-skills/generated/governance_backlog.json: "
            + ", ".join(invalid_skill_readiness)
        )

    allowed_memo_kinds: set[str] = set()
    missing_memo_contract_refs: list[str] = []
    for contract_ref in memo_contract_refs:
        contract_path = memo_contract_path(contract_ref)
        if not contract_path.exists():
            missing_memo_contract_refs.append(contract_ref)
            continue
        allowed_memo_kinds.update(memo_kinds_for_contract(contract_ref))
    if missing_memo_contract_refs:
        fail(
            f"{bundle_location} memo_contract_refs do not resolve in aoa-memo: "
            + ", ".join(missing_memo_contract_refs)
        )
    memo_source_route_policy = frontmatter.get("memo_source_route_policy")
    if memo_source_route_policy == "required" and not has_semantic_or_lineage_recall_contract(memo_contract_refs):
        fail(
            f"{bundle_location} with memo_source_route_policy=required must reference a semantic or lineage "
            "recall contract in memo_contract_refs"
        )
    expected_runtime_spec = RUNTIME_MEMO_SPEC_EXPECTATIONS.get(playbook_id)
    if expected_runtime_spec is not None:
        required_contract_ref = str(expected_runtime_spec["required_memo_contract_ref"])
        if required_contract_ref not in memo_contract_refs:
            fail(
                f"{bundle_location} must include '{required_contract_ref}' in memo_contract_refs for the "
                "runtime-facing memo cohort"
            )

    invalid_targets = [target for target in memo_writeback_targets if target not in allowed_memo_kinds]
    if invalid_targets:
        allowed_list = ", ".join(sorted(allowed_memo_kinds)) if allowed_memo_kinds else "none"
        fail(
            f"{bundle_location} memo_writeback_targets are not supported by the referenced aoa-memo contracts: "
            + ", ".join(invalid_targets)
            + f" (allowed: {allowed_list})"
        )

    memory_writeback_section = sections.get("Memory writeback", "")
    for target in memo_writeback_targets:
        if target not in memory_writeback_section:
            fail(
                f"{bundle_location} Memory writeback section must mention federation target '{target}' explicitly"
            )


def federation_surfaces_for_bundles(
    frontmatter_by_id: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    surfaces: list[dict[str, object]] = []
    for playbook_id in FEDERATION_COLLECTION_PLAYBOOK_IDS:
        if playbook_id not in frontmatter_by_id:
            fail(f"authored bundles are missing required federation target '{playbook_id}'")
        surfaces.append(federation_surface_for_frontmatter(frontmatter_by_id[playbook_id]))
    return surfaces


def validate_federation_collection(
    frontmatter_by_id: dict[str, dict[str, object]],
    *,
    agent_names: set[str],
    evals_by_name: dict[str, dict[str, object]],
    skills_by_name: dict[str, dict[str, object]],
) -> None:
    payload = read_json(FEDERATION_COLLECTION_PATH)
    if not isinstance(payload, list):
        fail("generated/playbook_federation_surfaces.min.json must be a JSON array")

    expected = federation_surfaces_for_bundles(frontmatter_by_id)
    if payload != expected:
        fail(
            "generated/playbook_federation_surfaces.min.json is out of date; "
            "run scripts/generate_playbook_federation_surfaces.py"
        )

    for index, surface in enumerate(payload):
        if not isinstance(surface, dict):
            fail(f"generated/playbook_federation_surfaces.min.json[{index}] must be an object")
        playbook_id = surface.get("playbook_id")
        if not isinstance(playbook_id, str):
            fail(f"generated/playbook_federation_surfaces.min.json[{index}] is missing a string playbook_id")
        validate_memo_recall_spec(
            surface,
            location=f"generated/playbook_federation_surfaces.min.json[{index}]",
            required=playbook_id in RUNTIME_MEMO_SPEC_PLAYBOOK_IDS,
        )
        validate_runtime_memo_spec_expectation(
            surface,
            playbook_id=playbook_id,
            location=f"generated/playbook_federation_surfaces.min.json[{index}]",
        )

        participating_agents = surface.get("participating_agents")
        if not isinstance(participating_agents, list) or not participating_agents:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must expose a non-empty "
                "participating_agents list"
            )
        if "memory-keeper" not in participating_agents:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must include 'memory-keeper' in "
                "participating_agents"
            )
        missing_agents = [
            item for item in participating_agents if not isinstance(item, str) or item not in agent_names
        ]
        if missing_agents:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] references participating_agents "
                f"that do not resolve in aoa-agents: {', '.join(str(item) for item in missing_agents)}"
            )

        eval_anchors = surface.get("eval_anchors")
        if not isinstance(eval_anchors, list) or not eval_anchors:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must expose a non-empty eval_anchors list"
            )
        missing_eval_anchors = [
            anchor for anchor in eval_anchors if not isinstance(anchor, str) or anchor not in evals_by_name
        ]
        if missing_eval_anchors:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] references eval_anchors that do not "
                f"resolve in aoa-evals: {', '.join(str(item) for item in missing_eval_anchors)}"
            )

        required_skills = surface.get("required_skills")
        if not isinstance(required_skills, list) or not required_skills:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must expose a non-empty required_skills list"
            )
        unresolved_skills = [skill for skill in required_skills if not isinstance(skill, str) or skill not in skills_by_name]
        if unresolved_skills:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] references required_skills that do not "
                f"resolve in aoa-skills: {', '.join(str(item) for item in unresolved_skills)}"
            )
        invalid_skill_readiness = [
            skill
            for skill in required_skills
            if isinstance(skill, str)
            and skill in skills_by_name
            and not skill_is_federation_eligible(
                skills_by_name[skill],
                playbook_status=str(frontmatter_by_id[playbook_id].get("status", "")),
            )
        ]
        if invalid_skill_readiness:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] references required_skills that are "
                f"not federation-ready in aoa-skills: {', '.join(invalid_skill_readiness)}"
            )

        memo_contract_refs = surface.get("memo_contract_refs")
        if not isinstance(memo_contract_refs, list) or not memo_contract_refs:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must expose a non-empty "
                "memo_contract_refs list"
            )
        allowed_memo_kinds: set[str] = set()
        missing_contracts: list[str] = []
        for contract_ref in memo_contract_refs:
            if not isinstance(contract_ref, str):
                missing_contracts.append(str(contract_ref))
                continue
            contract_path = memo_contract_path(contract_ref)
            if not contract_path.exists():
                missing_contracts.append(contract_ref)
                continue
            allowed_memo_kinds.update(memo_kinds_for_contract(contract_ref))
        if missing_contracts:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] references memo_contract_refs that do "
                f"not resolve in aoa-memo: {', '.join(missing_contracts)}"
            )
        if (
            surface.get("memo_source_route_policy") == "required"
            and not has_semantic_or_lineage_recall_contract(
                [contract_ref for contract_ref in memo_contract_refs if isinstance(contract_ref, str)]
            )
        ):
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] with memo_source_route_policy=required "
                "must reference a semantic or lineage recall contract"
            )

        memo_writeback_targets = surface.get("memo_writeback_targets")
        if not isinstance(memo_writeback_targets, list) or not memo_writeback_targets:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] must expose a non-empty "
                "memo_writeback_targets list"
            )
        invalid_targets = [
            target
            for target in memo_writeback_targets
            if not isinstance(target, str) or target not in allowed_memo_kinds
        ]
        if invalid_targets:
            fail(
                f"generated/playbook_federation_surfaces.min.json[{index}] exposes memo_writeback_targets that are "
                f"not supported by the referenced aoa-memo contracts: {', '.join(str(item) for item in invalid_targets)}"
            )


def validate_composition_surfaces(
    frontmatter_by_id: dict[str, dict[str, object]],
) -> None:
    builder = load_composition_builder_module()
    try:
        outputs = builder.build_outputs()
    except Exception as exc:
        fail(str(exc))

    for path, expected in outputs.items():
        payload = read_json(path)
        if payload != expected:
            fail(
                f"{display_path(path)} is out of date; run scripts/generate_playbook_composition_surfaces.py"
            )

    handoff_payload = read_json(PLAYBOOK_HANDOFF_CONTRACTS_PATH)
    if not isinstance(handoff_payload, dict) or not isinstance(handoff_payload.get("playbooks"), list):
        fail("generated/playbook_handoff_contracts.json must contain a 'playbooks' list")
    handoff_ids = {
        item.get("playbook_id")
        for item in handoff_payload["playbooks"]
        if isinstance(item, dict) and isinstance(item.get("playbook_id"), str)
    }
    expected_handoff_ids = set(COMPOSITION_COLLECTION_PLAYBOOK_IDS)
    if handoff_ids != expected_handoff_ids:
        fail("generated/playbook_handoff_contracts.json must cover the managed playbook cohort exactly")

    manifest_payload = read_json(PLAYBOOK_COMPOSITION_MANIFEST_PATH)
    if not isinstance(manifest_payload, dict):
        fail("generated/playbook_composition_manifest.json must contain a JSON object")
    generated_files = manifest_payload.get("generated_files")
    if not isinstance(generated_files, list):
        fail("generated/playbook_composition_manifest.json must expose generated_files")
    expected_generated_files = {
        "generated/playbook_handoff_contracts.json",
        "generated/playbook_failure_catalog.json",
        "generated/playbook_subagent_recipes.json",
        "generated/playbook_automation_seeds.json",
        "generated/playbook_composition_manifest.json",
    }
    if set(item for item in generated_files if isinstance(item, str)) != expected_generated_files:
        fail("generated/playbook_composition_manifest.json generated_files must match the composition outputs exactly")

    managed_playbooks = manifest_payload.get("managed_playbooks")
    if not isinstance(managed_playbooks, list):
        fail("generated/playbook_composition_manifest.json must expose managed_playbooks")
    expected_managed_names = [frontmatter_by_id[playbook_id]["name"] for playbook_id in COMPOSITION_COLLECTION_PLAYBOOK_IDS]
    if managed_playbooks != expected_managed_names:
        fail("generated/playbook_composition_manifest.json managed_playbooks must stay aligned with the composition cohort")


def validate_cross_repo_bundle(
    *,
    bundle_path: Path,
    frontmatter: dict[str, object],
    sections: dict[str, str],
    agent_names: set[str],
    model_tier_artifacts: set[str],
    evals_by_name: dict[str, dict[str, object]],
) -> None:
    bundle_location = bundle_path.relative_to(REPO_ROOT).as_posix()

    participating_agents = frontmatter.get("participating_agents")
    if not isinstance(participating_agents, list):
        fail(f"{bundle_location} is missing required list frontmatter 'participating_agents'")
    missing_agents = [
        item for item in participating_agents if not isinstance(item, str) or item not in agent_names
    ]
    if missing_agents:
        fail(
            f"{bundle_location} references participating_agents that do not resolve in aoa-agents: "
            + ", ".join(str(item) for item in missing_agents)
        )

    playbook_id = frontmatter.get("id")
    validate_projection_refs(
        location=f"{bundle_location}:{playbook_id}",
        participating_agents=participating_agents,
        expected_artifacts=frontmatter.get("expected_artifacts"),
        eval_anchors=frontmatter.get("eval_anchors"),
        agent_names=agent_names,
        model_tier_artifacts=model_tier_artifacts,
        evals_by_name=evals_by_name,
    )

    eval_anchors = frontmatter.get("eval_anchors")
    if eval_anchors is None:
        return
    draft_eval_anchors = [
        anchor
        for anchor in eval_anchors
        if isinstance(anchor, str) and evals_by_name[anchor].get("status") == "draft"
    ]
    if draft_eval_anchors:
        if frontmatter.get("status") != "experimental":
            fail(
                f"{bundle_location} uses draft eval_anchors and must remain experimental: "
                + ", ".join(draft_eval_anchors)
            )
        eval_anchor_section = sections.get("Eval anchors", "").lower()
        if "draft" not in eval_anchor_section or "review-only" not in eval_anchor_section:
            fail(
                f"{bundle_location} must state that draft eval_anchors are draft and review-only in the "
                "'Eval anchors' section"
            )


def validate_authored_bundles(
    playbooks_by_id: dict[str, dict[str, object]],
    *,
    agent_names: set[str],
    model_tier_artifacts: set[str],
    evals_by_name: dict[str, dict[str, object]],
    skills_by_name: dict[str, dict[str, object]],
) -> dict[str, dict[str, object]]:
    seen_bundle_ids: set[str] = set()
    seen_bundle_names: set[str] = set()
    frontmatter_by_id: dict[str, dict[str, object]] = {}

    for bundle_path in authored_bundle_paths():
        text = read_text(bundle_path)
        frontmatter, body = parse_frontmatter(text, bundle_path)
        sections = markdown_sections(body)

        playbook_id = frontmatter.get("id")
        if not isinstance(playbook_id, str) or not playbook_id:
            fail(f"{bundle_path.relative_to(REPO_ROOT).as_posix()} is missing a non-empty frontmatter 'id'")
        if playbook_id in seen_bundle_ids:
            fail(f"duplicate authored bundle id discovered: '{playbook_id}'")
        seen_bundle_ids.add(playbook_id)
        frontmatter_by_id[playbook_id] = frontmatter

        if playbook_id not in playbooks_by_id:
            fail(f"{bundle_path.relative_to(REPO_ROOT).as_posix()} has no registry entry for '{playbook_id}'")
        registry_entry = playbooks_by_id[playbook_id]

        bundle_name = frontmatter.get("name")
        if not isinstance(bundle_name, str) or not bundle_name:
            fail(f"{bundle_path.relative_to(REPO_ROOT).as_posix()} is missing a non-empty frontmatter 'name'")
        if bundle_name in seen_bundle_names:
            fail(f"duplicate authored bundle name discovered: '{bundle_name}'")
        seen_bundle_names.add(bundle_name)

        expected_path = PLAYBOOK_ROOT / bundle_name / "PLAYBOOK.md"
        if bundle_path != expected_path:
            fail(
                f"{bundle_path.relative_to(REPO_ROOT).as_posix()} must live at "
                f"{expected_path.relative_to(REPO_ROOT).as_posix()} to match its bundle name"
            )

        for key in (
            "id",
            "name",
            "status",
            "summary",
            "scenario",
            "trigger",
            "prerequisites",
            "participating_agents",
            "required_skill_families",
            "evaluation_posture",
            "memory_posture",
            "fallback_mode",
            "expected_artifacts",
        ):
            if key not in frontmatter:
                fail(f"{bundle_path.relative_to(REPO_ROOT).as_posix()} is missing frontmatter key '{key}'")
            if frontmatter[key] != registry_entry[key]:
                fail(
                    f"{bundle_path.relative_to(REPO_ROOT).as_posix()} frontmatter '{key}' does not match "
                    f"generated/playbook_registry.min.json"
                )
        if "eval_anchors" in registry_entry:
            if frontmatter.get("eval_anchors") != registry_entry["eval_anchors"]:
                fail(
                    f"{bundle_path.relative_to(REPO_ROOT).as_posix()} frontmatter 'eval_anchors' does not match "
                    f"generated/playbook_registry.min.json"
                )
        for field_name in RETURN_FIELD_NAMES:
            if field_name in registry_entry:
                if frontmatter.get(field_name) != registry_entry[field_name]:
                    fail(
                        f"{bundle_path.relative_to(REPO_ROOT).as_posix()} frontmatter '{field_name}' does not match "
                        f"generated/playbook_registry.min.json"
                    )
            elif field_name in frontmatter:
                fail(
                    f"{bundle_path.relative_to(REPO_ROOT).as_posix()} frontmatter '{field_name}' is not present in "
                    f"generated/playbook_registry.min.json"
                )
        for field_name in MEMO_SPEC_FIELD_NAMES:
            if field_name in registry_entry:
                if frontmatter.get(field_name) != registry_entry[field_name]:
                    fail(
                        f"{bundle_path.relative_to(REPO_ROOT).as_posix()} frontmatter '{field_name}' does not match "
                        f"generated/playbook_registry.min.json"
                    )
            elif field_name in frontmatter:
                fail(
                    f"{bundle_path.relative_to(REPO_ROOT).as_posix()} frontmatter '{field_name}' is not present in "
                    f"generated/playbook_registry.min.json"
                )

        missing_sections = sorted(REQUIRED_BUNDLE_SECTIONS - set(sections))
        if missing_sections:
            fail(
                f"{bundle_path.relative_to(REPO_ROOT).as_posix()} is missing required sections: "
                f"{', '.join(missing_sections)}"
            )

        semantic_checks = BUNDLE_SEMANTIC_CHECKS.get(playbook_id, {})

        for field_name, expected_items in semantic_checks.get("frontmatter_lists", {}).items():
            value = frontmatter.get(field_name)
            if not isinstance(value, list):
                fail(
                    f"{bundle_path.relative_to(REPO_ROOT).as_posix()} is missing required list frontmatter "
                    f"'{field_name}'"
                )
            actual_items = tuple(item for item in value if isinstance(item, str))
            if actual_items != expected_items:
                fail(
                    f"{bundle_path.relative_to(REPO_ROOT).as_posix()} frontmatter '{field_name}' must equal "
                    f"{list(expected_items)}"
                )

        for token in semantic_checks.get("text_tokens", ()):
            if token not in text:
                fail(f"{bundle_path.relative_to(REPO_ROOT).as_posix()} must mention '{token}' explicitly")

        validate_cross_repo_bundle(
            bundle_path=bundle_path,
            frontmatter=frontmatter,
            sections=sections,
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
        )
        if playbook_id in FEDERATION_COLLECTION_PLAYBOOK_IDS:
            validate_federation_bundle(
                bundle_path=bundle_path,
                frontmatter=frontmatter,
                sections=sections,
                skills_by_name=skills_by_name,
            )

    missing_semantic_check_bundles = sorted(set(BUNDLE_SEMANTIC_CHECKS) - seen_bundle_ids)
    if missing_semantic_check_bundles:
        fail(
            "authored bundle validation expected bundle ids that were not discovered: "
            + ", ".join(missing_semantic_check_bundles)
        )
    return frontmatter_by_id


def validate_activation_examples(
    playbooks_by_id: dict[str, dict[str, object]],
    *,
    agent_names: set[str],
    model_tier_artifacts: set[str],
    evals_by_name: dict[str, dict[str, object]],
) -> None:
    for playbook_id, example_path in ACTIVATION_EXAMPLE_PATHS.items():
        payload = read_json(example_path)
        location = example_path.relative_to(REPO_ROOT).as_posix()
        if not isinstance(payload, dict):
            fail(f"{location} must contain a JSON object")

        if playbook_id not in playbooks_by_id:
            fail(f"{location} references playbook_id '{playbook_id}' that is missing from the registry")

        registry_entry = playbooks_by_id[playbook_id]
        expected = activation_surface_for_playbook(playbook_id, registry_entry)
        if payload != expected:
            fail(f"{location} does not match generated/playbook_activation_surfaces.min.json")

        validate_projection_refs(
            location=f"{location}:{playbook_id}",
            participating_agents=payload.get("participating_agents"),
            expected_artifacts=payload.get("expected_artifacts"),
            eval_anchors=payload.get("eval_anchors"),
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
        )


def validate_harvest_templates() -> None:
    for template_path, required_tokens in HARVEST_TEMPLATE_REQUIREMENTS.items():
        text = read_text(template_path)
        location = template_path.relative_to(REPO_ROOT).as_posix()
        sections = markdown_sections(text)

        missing_sections = [
            section_name for section_name in REQUIRED_HARVEST_TEMPLATE_SECTIONS if section_name not in sections
        ]
        if missing_sections:
            fail(
                f"{location} is missing required harvest sections: "
                + ", ".join(missing_sections)
            )

        for token in required_tokens:
            if token not in text:
                fail(f"{location} must mention '{token}' explicitly")


def validate_real_run_workflow_surfaces() -> None:
    workflow_text = read_text(REAL_RUN_WORKFLOW_PATH)
    workflow_location = REAL_RUN_WORKFLOW_PATH.relative_to(REPO_ROOT).as_posix()
    for token in (
        REVIEWED_SUMMARY_GATE_SENTENCE,
        "examples/harvests/",
        "docs/real-runs/",
        "docs/gate-reviews/",
        "AOA-P-0017",
        "AOA-P-0021",
        "AOA-P-0023",
        "AOA-P-0024",
        "AOA-P-0019",
        "AOA-P-0020",
    ):
        if token not in workflow_text:
            fail(f"{workflow_location} must mention '{token}' explicitly")

    summary_home_text = read_text(REAL_RUN_SUMMARY_HOME_PATH)
    summary_home_location = REAL_RUN_SUMMARY_HOME_PATH.relative_to(REPO_ROOT).as_posix()
    for token in (
        REVIEWED_SUMMARY_GATE_SENTENCE,
        "YYYY-MM-DD.<playbook-slug>.md",
        "split-wave-cross-repo-rollout",
        "owner-first-capability-landing",
        "closeout-owner-follow-through-continuity",
        "federated-live-publisher-activation",
        "trusted-rollout-operations",
        "release-migration-cutover",
        "incident-recovery-routing",
        "Evidence Links",
    ):
        if token not in summary_home_text:
            fail(f"{summary_home_location} must mention '{token}' explicitly")

    for gate_path, requirement in GATE_REVIEW_REQUIREMENTS.items():
        text = read_text(gate_path)
        location = gate_path.relative_to(REPO_ROOT).as_posix()
        sections = markdown_sections(text)

        missing_sections = [
            section_name for section_name in REQUIRED_GATE_REVIEW_SECTIONS if section_name not in sections
        ]
        if missing_sections:
            fail(
                f"{location} is missing required gate-review sections: "
                + ", ".join(missing_sections)
            )

        current_verdict = sections.get("Current Verdict", "")
        matching_verdicts = [
            token for token in ALLOWED_GATE_VERDICT_TOKENS if token in current_verdict
        ]
        if len(matching_verdicts) != 1:
            fail(
                f"{location} must expose exactly one allowed verdict token in 'Current Verdict': "
                + ", ".join(ALLOWED_GATE_VERDICT_TOKENS)
            )
        current_verdict_token = matching_verdicts[0]
        playbook_id = requirement["playbook_id"]
        in_composition_cohort = playbook_id in COMPOSITION_COLLECTION_PLAYBOOK_IDS
        if current_verdict_token == "composition-landed" and not in_composition_cohort:
            fail(
                f"{location} cannot use 'composition-landed' unless {playbook_id} is in the composition cohort"
            )
        if current_verdict_token == "ready-for-composition-review" and in_composition_cohort:
            fail(
                f"{location} cannot use 'ready-for-composition-review' after {playbook_id} has landed in composition"
            )

        for token in (requirement["playbook_id"], *requirement["required_tokens"]):
            if token not in text:
                fail(f"{location} must mention '{token}' explicitly")

        latest_review_section = sections.get("Latest Reviewed Run", "")
        slug = requirement["slug"]
        summary_reference_re = re.compile(
            rf"docs/real-runs/(?:YYYY-MM-DD|\d{{4}}-\d{{2}}-\d{{2}})\.{re.escape(slug)}(?:\.[a-z0-9-]+)?\.md"
        )
        if not summary_reference_re.search(latest_review_section):
            fail(
                f"{location} must reference the matching reviewed-summary path in 'Latest Reviewed Run'"
            )

    for summary_path in sorted(REAL_RUN_SUMMARY_DIR.glob("*.md")):
        if summary_path.name == "README.md":
            continue

        location = summary_path.relative_to(REPO_ROOT).as_posix()
        match = REAL_RUN_SUMMARY_FILENAME_RE.match(summary_path.name)
        if not match:
            fail(
                f"{location} must match the filename pattern YYYY-MM-DD.<playbook-slug>[.<run-label>].md"
            )
        slug = match.group(1)
        if slug not in REAL_RUN_SUMMARY_SLUG_REQUIREMENTS:
            fail(
                f"{location} uses unsupported playbook slug '{slug}' for this wave"
            )

        text = read_text(summary_path)
        sections = markdown_sections(text)
        missing_sections = [
            section_name for section_name in REQUIRED_REAL_RUN_SUMMARY_SECTIONS if section_name not in sections
        ]
        if missing_sections:
            fail(
                f"{location} is missing required reviewed-summary sections: "
                + ", ".join(missing_sections)
            )

        for token in REAL_RUN_SUMMARY_SLUG_REQUIREMENTS[slug]:
            if token not in text:
                fail(f"{location} must mention '{token}' explicitly")

        if "No reviewed run is harvested yet." in text:
            fail(f"{location} cannot use gate-review placeholder language")

        evidence_links_section = sections.get("Evidence Links", "")
        if not MARKDOWN_LINK_RE.search(evidence_links_section):
            fail(f"{location} must include at least one Markdown link in 'Evidence Links'")

        if slug == "incident-recovery-routing" and "live incident" not in text.lower():
            fail(f"{location} must mention 'live incident' explicitly for incident recovery runs")


def load_review_status_builder_module():
    module_path = REPO_ROOT / "scripts" / "generate_playbook_review_status.py"
    spec = importlib.util.spec_from_file_location("generate_playbook_review_status", module_path)
    if spec is None or spec.loader is None:
        fail("unable to load playbook review-status generator module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_review_packet_contract_builder_module():
    module_path = REPO_ROOT / "scripts" / "generate_playbook_review_packet_contracts.py"
    spec = importlib.util.spec_from_file_location(
        "generate_playbook_review_packet_contracts",
        module_path,
    )
    if spec is None or spec.loader is None:
        fail("unable to load playbook review-packet contract generator module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_review_intake_builder_module():
    module_path = REPO_ROOT / "scripts" / "generate_playbook_review_intake.py"
    spec = importlib.util.spec_from_file_location(
        "generate_playbook_review_intake",
        module_path,
    )
    if spec is None or spec.loader is None:
        fail("unable to load playbook review intake generator module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_playbook_landing_governance_builder_module():
    module_path = REPO_ROOT / "scripts" / "generate_playbook_landing_governance.py"
    spec = importlib.util.spec_from_file_location(
        "generate_playbook_landing_governance",
        module_path,
    )
    if spec is None or spec.loader is None:
        fail("unable to load playbook landing governance generator module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_phase_alpha_builder_module():
    module_path = REPO_ROOT / "scripts" / "generate_phase_alpha_surfaces.py"
    spec = importlib.util.spec_from_file_location("generate_phase_alpha_surfaces", module_path)
    if spec is None or spec.loader is None:
        fail("unable to load Phase Alpha surface generator module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_phase_alpha_surfaces(
    playbooks_by_id: dict[str, dict[str, object]],
    *,
    evals_by_name: dict[str, dict[str, object]],
) -> None:
    config = read_json(PHASE_ALPHA_CONFIG_PATH)
    if not isinstance(config, dict):
        fail("config/phase_alpha_curated_core.json must stay a JSON object")

    runtime_paths = config.get("runtime_paths")
    if not isinstance(runtime_paths, dict):
        fail("config/phase_alpha_curated_core.json must expose runtime_paths")
    primary_runtime = runtime_paths.get("primary")
    control_runtime = runtime_paths.get("control")
    if not isinstance(primary_runtime, str) or "5403" not in primary_runtime or "LangGraph" not in primary_runtime:
        fail("config/phase_alpha_curated_core.json runtime_paths.primary must keep the llama.cpp + LangGraph worker path")
    if (
        not isinstance(control_runtime, str)
        or "5403" not in control_runtime
        or "llama.cpp" not in control_runtime
        or "recurrence" not in control_runtime
    ):
        fail("config/phase_alpha_curated_core.json runtime_paths.control must keep the canonical llama.cpp second-pass recurrence path")

    playbooks = config.get("playbooks")
    if not isinstance(playbooks, list) or len(playbooks) != len(PHASE_ALPHA_PLAYBOOK_ORDER):
        fail("config/phase_alpha_curated_core.json must expose the five Alpha core playbooks in order")

    seen_ids: list[str] = []
    for index, entry in enumerate(playbooks):
        location = f"config/phase_alpha_curated_core.json.playbooks[{index}]"
        if not isinstance(entry, dict):
            fail(f"{location} must be an object")
        playbook_id = entry.get("playbook_id")
        playbook_name = entry.get("playbook_name")
        if playbook_id != PHASE_ALPHA_PLAYBOOK_ORDER[index]:
            fail(f"{location}.playbook_id must stay in the fixed Phase Alpha order")
        if playbook_id not in playbooks_by_id:
            fail(f"{location}.playbook_id '{playbook_id}' does not resolve in generated/playbook_registry.min.json")
        registry_entry = playbooks_by_id[playbook_id]
        if playbook_name != registry_entry.get("name"):
            fail(f"{location}.playbook_name must match generated/playbook_registry.min.json")
        seen_ids.append(playbook_id)
        runtime_path_key = entry.get("runtime_path_key")
        if not isinstance(runtime_path_key, str) or not runtime_path_key:
            fail(f"{location}.runtime_path_key must stay a non-empty string")
        runtime_path = runtime_paths.get(runtime_path_key)
        if not isinstance(runtime_path, str) or not runtime_path:
            fail(f"{location}.runtime_path_key must resolve in config/phase_alpha_curated_core.json.runtime_paths")

        for field_name in (
            "required_artifacts",
            "eval_anchors",
            "memo_outputs",
            "stop_conditions",
            "allowed_reentry_modes",
            "source_review_refs",
        ):
            value = entry.get(field_name)
            if not isinstance(value, list) or not value:
                fail(f"{location}.{field_name} must stay a non-empty list")
            if len(value) != len(set(value)):
                fail(f"{location}.{field_name} must not duplicate entries")

        for anchor in entry["eval_anchors"]:
            if anchor not in evals_by_name:
                fail(f"{location}.eval_anchors contains unknown eval '{anchor}'")

        for ref_field in (
            "harvest_template_ref",
            "reviewed_run_ref",
            "readiness_review_ref",
        ):
            error = local_ref_error(entry.get(ref_field), f"{location}.{ref_field}")
            if error:
                fail(error)
        for ref_index, ref in enumerate(entry["source_review_refs"]):
            error = local_ref_error(ref, f"{location}.source_review_refs[{ref_index}]")
            if error:
                fail(error)

        harvest_text = read_text(REPO_ROOT / entry["harvest_template_ref"])
        harvest_sections = markdown_sections(harvest_text)
        missing_harvest_sections = [
            section_name
            for section_name in PHASE_ALPHA_REQUIRED_HARVEST_SECTIONS
            if section_name not in harvest_sections
        ]
        if missing_harvest_sections:
            fail(
                f"{entry['harvest_template_ref']} is missing required Alpha harvest sections: "
                + ", ".join(missing_harvest_sections)
            )
        for artifact in entry["required_artifacts"]:
            if artifact not in harvest_sections["Required Artifacts"]:
                fail(f"{entry['harvest_template_ref']} must mention required artifact '{artifact}'")

        reviewed_run_text = read_text(REPO_ROOT / entry["reviewed_run_ref"])
        reviewed_sections = markdown_sections(reviewed_run_text)
        missing_review_sections = [
            section_name
            for section_name in PHASE_ALPHA_REQUIRED_REVIEWED_RUN_SECTIONS
            if section_name not in reviewed_sections
        ]
        if missing_review_sections:
            fail(
                f"{entry['reviewed_run_ref']} is missing required Alpha reviewed-run sections: "
                + ", ".join(missing_review_sections)
            )
        if playbook_id not in reviewed_sections["Run Header"]:
            fail(f"{entry['reviewed_run_ref']} Run Header must mention {playbook_id}")
        for artifact in entry["required_artifacts"]:
            if artifact not in reviewed_sections["Required Artifacts"]:
                fail(f"{entry['reviewed_run_ref']} must mention required artifact '{artifact}'")
        for anchor in entry["eval_anchors"]:
            if anchor not in reviewed_sections["Eval Anchors"]:
                fail(f"{entry['reviewed_run_ref']} must mention eval anchor '{anchor}'")
        for memo_output in entry["memo_outputs"]:
            if memo_output not in reviewed_sections["Memo Writeback"]:
                fail(f"{entry['reviewed_run_ref']} must mention memo output '{memo_output}'")

        readiness_text = read_text(REPO_ROOT / entry["readiness_review_ref"])
        readiness_sections = markdown_sections(readiness_text)
        missing_readiness_sections = [
            section_name
            for section_name in PHASE_ALPHA_REQUIRED_READINESS_SECTIONS
            if section_name not in readiness_sections
        ]
        if missing_readiness_sections:
            fail(
                f"{entry['readiness_review_ref']} is missing required Alpha readiness sections: "
                + ", ".join(missing_readiness_sections)
            )
        if "Alpha is a readiness proof lane, not composition promotion." not in readiness_text:
            fail(
                f"{entry['readiness_review_ref']} must preserve the readiness-proof-lane boundary sentence"
            )
        if "curated-ready" not in readiness_sections["Current Verdict"]:
            fail(f"{entry['readiness_review_ref']} Current Verdict must expose curated-ready")

    if tuple(seen_ids) != PHASE_ALPHA_PLAYBOOK_ORDER:
        fail("config/phase_alpha_curated_core.json playbooks drifted from the fixed Phase Alpha order")

    final_rerun = config.get("final_rerun")
    if not isinstance(final_rerun, dict):
        fail("config/phase_alpha_curated_core.json must expose final_rerun")
    if final_rerun.get("run_id") != PHASE_ALPHA_FINAL_RERUN_ID:
        fail("config/phase_alpha_curated_core.json final_rerun.run_id must stay fixed")
    if final_rerun.get("playbook_id") != "AOA-P-0018":
        fail("config/phase_alpha_curated_core.json final_rerun.playbook_id must stay AOA-P-0018")
    if final_rerun.get("recall_mode") != "memo_only":
        fail("config/phase_alpha_curated_core.json final_rerun.recall_mode must stay memo_only")
    final_runtime_path_key = final_rerun.get("runtime_path_key")
    if not isinstance(final_runtime_path_key, str) or not final_runtime_path_key:
        fail("config/phase_alpha_curated_core.json final_rerun.runtime_path_key must stay a non-empty string")
    final_runtime_path = runtime_paths.get(final_runtime_path_key)
    if not isinstance(final_runtime_path, str) or not final_runtime_path:
        fail("config/phase_alpha_curated_core.json final_rerun.runtime_path_key must resolve in runtime_paths")
    for field_name in ("required_artifacts", "eval_anchors", "memo_outputs", "stop_conditions"):
        value = final_rerun.get(field_name)
        if not isinstance(value, list) or not value:
            fail(f"config/phase_alpha_curated_core.json final_rerun.{field_name} must stay a non-empty list")
    for anchor in final_rerun["eval_anchors"]:
        if anchor not in evals_by_name:
            fail(f"config/phase_alpha_curated_core.json final_rerun.eval_anchors contains unknown eval '{anchor}'")
    for ref_field in ("run_ref", "recall_contract_ref"):
        error = local_ref_error(final_rerun.get(ref_field), f"config/phase_alpha_curated_core.json.final_rerun.{ref_field}")
        if error:
            fail(error)

    final_run_text = read_text(REPO_ROOT / final_rerun["run_ref"])
    final_sections = markdown_sections(final_run_text)
    missing_final_sections = [
        section_name
        for section_name in PHASE_ALPHA_REQUIRED_REVIEWED_RUN_SECTIONS
        if section_name not in final_sections
    ]
    if missing_final_sections:
        fail(
            f"{final_rerun['run_ref']} is missing required Alpha reviewed-run sections: "
            + ", ".join(missing_final_sections)
        )
    if "memo-only" not in final_sections["Recurrence Posture"]:
        fail(f"{final_rerun['run_ref']} Recurrence Posture must name memo-only recall")

    builder = load_phase_alpha_builder_module()
    expected_review_packets = builder.build_phase_alpha_review_packets_payload()
    actual_review_packets = read_json(PHASE_ALPHA_REVIEW_PACKETS_PATH)
    if actual_review_packets != expected_review_packets:
        fail(
            "generated/phase_alpha_review_packets.min.json drifted from "
            "config/phase_alpha_curated_core.json"
        )
    expected_run_matrix = builder.build_phase_alpha_run_matrix_payload()
    actual_run_matrix = read_json(PHASE_ALPHA_RUN_MATRIX_PATH)
    if actual_run_matrix != expected_run_matrix:
        fail(
            "generated/phase_alpha_run_matrix.min.json drifted from "
            "config/phase_alpha_curated_core.json"
        )


def validate_playbook_review_status_surface(playbooks_by_id: dict[str, dict[str, object]]) -> None:
    builder = load_review_status_builder_module()
    try:
        expected = builder.build_review_status_payload()
    except Exception as exc:
        fail(str(exc))

    payload = read_json(PLAYBOOK_REVIEW_STATUS_PATH)
    if payload != expected:
        fail(
            "generated/playbook_review_status.min.json is out of date; "
            "run scripts/generate_playbook_review_status.py"
        )
    if not isinstance(payload, dict):
        fail("generated/playbook_review_status.min.json must contain a JSON object")
    if payload.get("schema_version") != 1:
        fail("generated/playbook_review_status.min.json must declare schema_version 1")
    if payload.get("layer") != "aoa-playbooks":
        fail("generated/playbook_review_status.min.json must declare layer 'aoa-playbooks'")
    source_of_truth = payload.get("source_of_truth")
    if not isinstance(source_of_truth, dict):
        fail("generated/playbook_review_status.min.json must expose source_of_truth")
    if source_of_truth.get("reviewed_runs_dir") != "docs/real-runs":
        fail("generated/playbook_review_status.min.json must keep source_of_truth.reviewed_runs_dir")
    if source_of_truth.get("gate_reviews_dir") != "docs/gate-reviews":
        fail("generated/playbook_review_status.min.json must keep source_of_truth.gate_reviews_dir")

    entries = payload.get("playbooks")
    if not isinstance(entries, list):
        fail("generated/playbook_review_status.min.json must expose playbooks as a list")

    playbook_ids = [entry.get("playbook_id") for entry in entries if isinstance(entry, dict)]
    if playbook_ids != sorted(playbook_ids):
        fail("generated/playbook_review_status.min.json playbooks must stay ordered by playbook_id")
    if len(playbook_ids) != len(set(playbook_ids)):
        fail("generated/playbook_review_status.min.json playbooks must not duplicate playbook_id")

    actual_reviewed_run_refs_by_playbook: dict[str, list[str]] = {}
    for summary_path in sorted(REAL_RUN_SUMMARY_DIR.glob("*.md")):
        if summary_path.name == "README.md":
            continue
        location = summary_path.relative_to(REPO_ROOT).as_posix()
        text = read_text(summary_path)
        sections = markdown_sections(text)
        run_header = sections.get("Run Header", "")
        match = re.search(r"\bAOA-P-\d{4}\b", run_header)
        if match is None:
            fail(f"{location} must mention an owning playbook id in 'Run Header'")
        actual_reviewed_run_refs_by_playbook.setdefault(match.group(0), []).append(location)

    for index, entry in enumerate(entries):
        location = f"generated/playbook_review_status.min.json.playbooks[{index}]"
        if not isinstance(entry, dict):
            fail(f"{location} must be an object")
        playbook_id = entry.get("playbook_id")
        if not isinstance(playbook_id, str) or playbook_id not in playbooks_by_id:
            fail(f"{location}.playbook_id must resolve in generated/playbook_registry.min.json")
        if entry.get("playbook_name") != playbooks_by_id[playbook_id]["name"]:
            fail(f"{location}.playbook_name must match generated/playbook_registry.min.json")
        if entry.get("scenario") != playbooks_by_id[playbook_id]["scenario"]:
            fail(f"{location}.scenario must match generated/playbook_registry.min.json")
        gate_review_ref = entry.get("gate_review_ref")
        if not isinstance(gate_review_ref, str) or not (REPO_ROOT / gate_review_ref).exists():
            fail(f"{location}.gate_review_ref must point to an existing gate review")
        reviewed_run_refs = entry.get("reviewed_run_refs")
        if not isinstance(reviewed_run_refs, list):
            fail(f"{location}.reviewed_run_refs must be a list")
        expected_run_refs = actual_reviewed_run_refs_by_playbook.get(playbook_id, [])
        if reviewed_run_refs != expected_run_refs:
            fail(f"{location}.reviewed_run_refs must match the reviewed runs harvested for {playbook_id}")
        if entry.get("reviewed_run_count") != len(expected_run_refs):
            fail(f"{location}.reviewed_run_count must match the number of reviewed_run_refs")
        expected_latest = expected_run_refs[-1] if expected_run_refs else None
        if entry.get("latest_reviewed_run_ref") != expected_latest:
            fail(f"{location}.latest_reviewed_run_ref must match the latest reviewed run ref")
        if entry.get("gate_verdict") not in ALLOWED_GATE_VERDICT_TOKENS:
            fail(f"{location}.gate_verdict must be an allowed verdict token")
        composition_signal_summary = entry.get("composition_signal_summary")
        if not isinstance(composition_signal_summary, dict):
            fail(f"{location}.composition_signal_summary must be an object")
        for field_name in ("failure_or_follow_up", "adjunct_candidate"):
            value = composition_signal_summary.get(field_name)
            if not isinstance(value, str) or len(value.strip()) < 10:
                fail(f"{location}.composition_signal_summary.{field_name} must be a non-empty summary")

        gate_review_text = read_text(REPO_ROOT / gate_review_ref)
        sections = markdown_sections(gate_review_text)
        latest_review_section = sections.get("Latest Reviewed Run", "")
        referenced_run_refs = sorted(
            {
                f"docs/real-runs/{match.group(1)}"
                for match in REVIEWED_RUN_REF_RE.finditer(latest_review_section)
            }
        )
        missing_run_refs = [ref for ref in expected_run_refs if ref not in referenced_run_refs]
        if missing_run_refs:
            fail(
                f"{gate_review_ref} must reference the reviewed runs it claims: "
                + ", ".join(missing_run_refs)
            )


def validate_playbook_review_packet_contracts_surface(
    playbooks_by_id: dict[str, dict[str, object]]
) -> None:
    builder = load_review_packet_contract_builder_module()
    try:
        expected = builder.build_review_packet_contracts_payload()
    except (Exception, SystemExit) as exc:
        fail(str(exc))

    payload = read_json(PLAYBOOK_REVIEW_PACKET_CONTRACTS_PATH)
    if payload != expected:
        fail(
            "generated/playbook_review_packet_contracts.min.json is out of date; "
            "run scripts/generate_playbook_review_packet_contracts.py"
        )
    if not isinstance(payload, dict):
        fail("generated/playbook_review_packet_contracts.min.json must contain a JSON object")
    if payload.get("schema_version") != 1:
        fail("generated/playbook_review_packet_contracts.min.json must declare schema_version 1")
    if payload.get("layer") != "aoa-playbooks":
        fail("generated/playbook_review_packet_contracts.min.json must declare layer 'aoa-playbooks'")
    expected_source_of_truth = {
        "registry": "generated/playbook_registry.min.json",
        "activation": "generated/playbook_activation_surfaces.min.json",
        "federation": "generated/playbook_federation_surfaces.min.json",
        "review_status": "generated/playbook_review_status.min.json",
        "runtime_template_index": "repo:aoa-evals/generated/runtime_candidate_template_index.min.json",
    }
    if payload.get("source_of_truth") != expected_source_of_truth:
        fail("generated/playbook_review_packet_contracts.min.json must keep source_of_truth stable")

    entries = payload.get("playbooks")
    if not isinstance(entries, list):
        fail("generated/playbook_review_packet_contracts.min.json must expose playbooks as a list")

    activation_payload = read_json(ACTIVATION_COLLECTION_PATH)
    if not isinstance(activation_payload, list):
        fail("generated/playbook_activation_surfaces.min.json must stay a list")
    activation_entries = {
        entry["playbook_id"]: entry for entry in activation_payload if isinstance(entry, dict)
    }

    federation_payload = read_json(FEDERATION_COLLECTION_PATH)
    if not isinstance(federation_payload, list):
        fail("generated/playbook_federation_surfaces.min.json must stay a list")
    federation_entries = {
        entry["playbook_id"]: entry for entry in federation_payload if isinstance(entry, dict)
    }

    review_status_payload = read_json(PLAYBOOK_REVIEW_STATUS_PATH)
    if not isinstance(review_status_payload, dict):
        fail("generated/playbook_review_status.min.json must stay an object")
    review_entries = {
        entry["playbook_id"]: entry
        for entry in review_status_payload.get("playbooks", [])
        if isinstance(entry, dict)
    }

    contract_ids = [entry.get("playbook_id") for entry in entries if isinstance(entry, dict)]
    if contract_ids != sorted(contract_ids):
        fail("generated/playbook_review_packet_contracts.min.json playbooks must stay ordered by playbook_id")
    if len(contract_ids) != len(set(contract_ids)):
        fail("generated/playbook_review_packet_contracts.min.json playbooks must not duplicate playbook_id")

    allowed_packet_kinds = {
        "memo_candidate",
        "runtime_evidence_selection_candidate",
        "artifact_hook_candidate",
    }

    for index, entry in enumerate(entries):
        location = f"generated/playbook_review_packet_contracts.min.json.playbooks[{index}]"
        if not isinstance(entry, dict):
            fail(f"{location} must be an object")
        playbook_id = entry.get("playbook_id")
        if not isinstance(playbook_id, str) or playbook_id not in playbooks_by_id:
            fail(f"{location}.playbook_id must resolve in generated/playbook_registry.min.json")
        if entry.get("playbook_name") != playbooks_by_id[playbook_id]["name"]:
            fail(f"{location}.playbook_name must match generated/playbook_registry.min.json")
        if entry.get("scenario") != playbooks_by_id[playbook_id]["scenario"]:
            fail(f"{location}.scenario must match generated/playbook_registry.min.json")

        expected_artifacts = entry.get("expected_artifacts")
        if not isinstance(expected_artifacts, list):
            fail(f"{location}.expected_artifacts must be a list")
        activation_entry = activation_entries.get(playbook_id)
        if activation_entry is not None and expected_artifacts != activation_entry.get("expected_artifacts", []):
            fail(f"{location}.expected_artifacts must match the activation surface when present")

        eval_anchors = entry.get("eval_anchors")
        if not isinstance(eval_anchors, list):
            fail(f"{location}.eval_anchors must be a list")
        available_eval_anchors = builder._available_runtime_eval_anchors()
        expected_eval_anchors = []
        if activation_entry is not None:
            expected_eval_anchors.extend(activation_entry.get("eval_anchors", []))
        federation_entry = federation_entries.get(playbook_id)
        if federation_entry is not None:
            expected_eval_anchors.extend(federation_entry.get("eval_anchors", []))
        deduped_eval_anchors = []
        for value in expected_eval_anchors:
            if value in available_eval_anchors and value not in deduped_eval_anchors:
                deduped_eval_anchors.append(value)
        if eval_anchors != deduped_eval_anchors:
            fail(
                f"{location}.eval_anchors must match activation/federation eval anchors "
                "that have live runtime template coverage"
            )

        memo_runtime_surfaces = entry.get("memo_runtime_surfaces")
        if not isinstance(memo_runtime_surfaces, list):
            fail(f"{location}.memo_runtime_surfaces must be a list")
        if memo_runtime_surfaces != [
            artifact for artifact in expected_artifacts if artifact in builder.KNOWN_MEMO_RUNTIME_SURFACES
        ]:
            fail(
                f"{location}.memo_runtime_surfaces must resolve from expected_artifacts "
                "using the known memo runtime surfaces"
            )

        candidate_packet_kinds = entry.get("candidate_packet_kinds")
        if not isinstance(candidate_packet_kinds, list):
            fail(f"{location}.candidate_packet_kinds must be a list")
        if not set(candidate_packet_kinds).issubset(allowed_packet_kinds):
            fail(f"{location}.candidate_packet_kinds must stay within the allowed packet kinds")
        expected_packet_kinds = builder._candidate_packet_kinds(
            memo_runtime_surfaces=memo_runtime_surfaces,
            eval_anchors=eval_anchors,
        )
        if candidate_packet_kinds != expected_packet_kinds:
            fail(f"{location}.candidate_packet_kinds must derive from memo_runtime_surfaces and eval_anchors")
        if entry.get("review_required") is not bool(candidate_packet_kinds):
            fail(f"{location}.review_required must reflect whether candidate packet kinds exist")

        source_review_refs = entry.get("source_review_refs")
        if not isinstance(source_review_refs, list):
            fail(f"{location}.source_review_refs must be a list")
        expected_playbook_ref = f"playbooks/{entry['playbook_name']}/PLAYBOOK.md"
        review_entry = review_entries.get(playbook_id)
        if not source_review_refs or source_review_refs[0] != expected_playbook_ref:
            fail(f"{location}.source_review_refs must start with the owning PLAYBOOK.md")
        if entry.get("review_required") is True and not source_review_refs:
            fail(f"{location}.source_review_refs must stay non-empty for review-required packet contracts")
        if review_entry is None:
            if source_review_refs != [expected_playbook_ref]:
                fail(
                    f"{location}.source_review_refs must stay limited to the owning PLAYBOOK.md "
                    "when no review status exists"
                )
            if entry.get("gate_verdict") is not None:
                fail(f"{location}.gate_verdict must stay null when no review status exists")
        else:
            expected_review_refs = [
                expected_playbook_ref,
                review_entry["gate_review_ref"],
                *review_entry["reviewed_run_refs"],
            ]
            if source_review_refs != expected_review_refs:
                fail(
                    f"{location}.source_review_refs must match the owning PLAYBOOK.md, "
                    "gate review, and reviewed runs"
                )
            if entry.get("gate_verdict") != review_entry.get("gate_verdict"):
                fail(f"{location}.gate_verdict must match generated/playbook_review_status.min.json")


def validate_playbook_review_intake_surface() -> None:
    builder = load_review_intake_builder_module()
    try:
        expected = builder.build_review_intake_payload()
    except Exception as exc:
        fail(str(exc))

    payload = read_json(PLAYBOOK_REVIEW_INTAKE_PATH)
    if payload != expected:
        fail(
            "generated/playbook_review_intake.min.json is out of date; "
            "run scripts/generate_playbook_review_intake.py"
        )
    if not isinstance(payload, dict):
        fail("generated/playbook_review_intake.min.json must contain a JSON object")
    if payload.get("schema_version") != 1:
        fail("generated/playbook_review_intake.min.json must declare schema_version 1")
    if payload.get("layer") != "aoa-playbooks":
        fail("generated/playbook_review_intake.min.json must declare layer 'aoa-playbooks'")
    expected_source_of_truth = {
        "review_packet_contracts": "generated/playbook_review_packet_contracts.min.json",
        "review_status": "generated/playbook_review_status.min.json",
        "activation_examples": "examples/playbook_activation.*.example.json",
        "gate_reviews_dir": "docs/gate-reviews",
        "reviewed_runs_dir": "docs/real-runs",
    }
    if payload.get("source_of_truth") != expected_source_of_truth:
        fail("generated/playbook_review_intake.min.json must keep source_of_truth stable")

    entries = payload.get("playbooks")
    if not isinstance(entries, list):
        fail("generated/playbook_review_intake.min.json must expose playbooks as a list")

    contract_payload = read_json(PLAYBOOK_REVIEW_PACKET_CONTRACTS_PATH)
    if not isinstance(contract_payload, dict):
        fail("generated/playbook_review_packet_contracts.min.json must stay an object")
    contracts_by_id = {
        entry["playbook_id"]: entry
        for entry in contract_payload.get("playbooks", [])
        if isinstance(entry, dict) and isinstance(entry.get("playbook_id"), str)
    }
    review_status_payload = read_json(PLAYBOOK_REVIEW_STATUS_PATH)
    if not isinstance(review_status_payload, dict):
        fail("generated/playbook_review_status.min.json must stay an object")
    review_status_by_id = {
        entry["playbook_id"]: entry
        for entry in review_status_payload.get("playbooks", [])
        if isinstance(entry, dict) and isinstance(entry.get("playbook_id"), str)
    }

    playbook_ids = [entry.get("playbook_id") for entry in entries if isinstance(entry, dict)]
    if playbook_ids != sorted(playbook_ids):
        fail("generated/playbook_review_intake.min.json playbooks must stay ordered by playbook_id")
    if len(playbook_ids) != len(set(playbook_ids)):
        fail("generated/playbook_review_intake.min.json playbooks must not duplicate playbook_id")
    if set(playbook_ids) != set(contracts_by_id):
        fail("generated/playbook_review_intake.min.json must cover every playbook review packet contract exactly once")

    for index, entry in enumerate(entries):
        location = f"generated/playbook_review_intake.min.json.playbooks[{index}]"
        if not isinstance(entry, dict):
            fail(f"{location} must be an object")

        playbook_id = entry.get("playbook_id")
        if not isinstance(playbook_id, str) or playbook_id not in contracts_by_id:
            fail(f"{location}.playbook_id must resolve in generated/playbook_review_packet_contracts.min.json")

        contract = contracts_by_id[playbook_id]
        review_status = review_status_by_id.get(playbook_id)

        if entry.get("playbook_name") != contract.get("playbook_name"):
            fail(f"{location}.playbook_name must match generated/playbook_review_packet_contracts.min.json")
        if entry.get("scenario") != contract.get("scenario"):
            fail(f"{location}.scenario must match generated/playbook_review_packet_contracts.min.json")
        if entry.get("required_artifact_set") != contract.get("expected_artifacts"):
            fail(f"{location}.required_artifact_set must match expected_artifacts")
        if entry.get("accepted_packet_kinds") != contract.get("candidate_packet_kinds"):
            fail(f"{location}.accepted_packet_kinds must match candidate_packet_kinds")
        if entry.get("source_review_refs") != contract.get("source_review_refs"):
            fail(f"{location}.source_review_refs must match generated/playbook_review_packet_contracts.min.json")

        expected_gate_verdict = (
            review_status.get("gate_verdict")
            if isinstance(review_status, dict)
            else contract.get("gate_verdict")
        )
        if entry.get("gate_verdict") != expected_gate_verdict:
            fail(f"{location}.gate_verdict must match generated/playbook_review_status.min.json when present")

        expected_gate_review_ref = review_status.get("gate_review_ref") if isinstance(review_status, dict) else None
        if entry.get("gate_review_ref") != expected_gate_review_ref:
            fail(f"{location}.gate_review_ref must match generated/playbook_review_status.min.json when present")

        expected_template_ref = f"examples/playbook_activation.{contract['playbook_name']}.example.json"
        if (REPO_ROOT / expected_template_ref).is_file():
            if entry.get("real_run_template_ref") != expected_template_ref:
                fail(f"{location}.real_run_template_ref must match the current activation example")
        elif entry.get("real_run_template_ref") is not None:
            fail(f"{location}.real_run_template_ref must stay null when no activation example exists")

        review_outcome_targets = entry.get("review_outcome_targets")
        if not isinstance(review_outcome_targets, dict):
            fail(f"{location}.review_outcome_targets must be an object")
        expected_real_runs = review_status.get("reviewed_run_refs") if isinstance(review_status, dict) else []
        if review_outcome_targets.get("real_runs") != expected_real_runs:
            fail(f"{location}.review_outcome_targets.real_runs must match generated/playbook_review_status.min.json")
        expected_gate_reviews = [expected_gate_review_ref] if expected_gate_review_ref else []
        if review_outcome_targets.get("gate_reviews") != expected_gate_reviews:
            fail(f"{location}.review_outcome_targets.gate_reviews must match the current gate review posture")

        gate_verdict = entry.get("gate_verdict")
        reviewed_run_count = len(expected_real_runs) if isinstance(expected_real_runs, list) else 0
        if gate_verdict == "composition-landed":
            expected_composition_posture = "landed"
        elif gate_verdict == "ready-for-composition-review":
            expected_composition_posture = "ready-for-composition-review"
        elif gate_verdict == "hold" and reviewed_run_count > 0:
            expected_composition_posture = "held-after-review"
        elif gate_verdict == "hold":
            expected_composition_posture = "awaiting-reviewed-run"
        else:
            expected_composition_posture = "ungated"
        if entry.get("composition_posture") != expected_composition_posture:
            fail(f"{location}.composition_posture must stay aligned with the current gate posture")


def validate_playbook_landing_governance_surface(playbooks_by_id: dict[str, dict[str, object]]) -> None:
    builder = load_playbook_landing_governance_builder_module()
    try:
        expected = builder.build_playbook_landing_governance_payload()
    except Exception as exc:
        fail(str(exc))

    payload = read_json(PLAYBOOK_LANDING_GOVERNANCE_PATH)
    if payload != expected:
        fail(
            "generated/playbook_landing_governance.min.json is out of date; "
            "run scripts/generate_playbook_landing_governance.py"
        )
    if not isinstance(payload, dict):
        fail("generated/playbook_landing_governance.min.json must contain a JSON object")
    if payload.get("schema_version") != 1:
        fail("generated/playbook_landing_governance.min.json must declare schema_version 1")
    if payload.get("layer") != "aoa-playbooks":
        fail("generated/playbook_landing_governance.min.json must declare layer 'aoa-playbooks'")
    if payload.get("scope") != "review-track":
        fail("generated/playbook_landing_governance.min.json must declare scope 'review-track'")
    expected_source_of_truth = {
        "registry": "generated/playbook_registry.min.json",
        "review_packet_contracts": "generated/playbook_review_packet_contracts.min.json",
        "review_intake": "generated/playbook_review_intake.min.json",
        "review_status": "generated/playbook_review_status.min.json",
        "composition_manifest": "generated/playbook_composition_manifest.json",
    }
    if payload.get("source_of_truth") != expected_source_of_truth:
        fail("generated/playbook_landing_governance.min.json must keep source_of_truth stable")

    entries = payload.get("playbooks")
    if not isinstance(entries, list):
        fail("generated/playbook_landing_governance.min.json must expose playbooks as a list")

    review_packet_payload = read_json(PLAYBOOK_REVIEW_PACKET_CONTRACTS_PATH)
    if not isinstance(review_packet_payload, dict):
        fail("generated/playbook_review_packet_contracts.min.json must stay an object")
    packet_by_id = {
        entry["playbook_id"]: entry
        for entry in review_packet_payload.get("playbooks", [])
        if isinstance(entry, dict) and isinstance(entry.get("playbook_id"), str)
    }

    review_intake_payload = read_json(PLAYBOOK_REVIEW_INTAKE_PATH)
    if not isinstance(review_intake_payload, dict):
        fail("generated/playbook_review_intake.min.json must stay an object")
    intake_by_id = {
        entry["playbook_id"]: entry
        for entry in review_intake_payload.get("playbooks", [])
        if isinstance(entry, dict) and isinstance(entry.get("playbook_id"), str)
    }
    if set(packet_by_id) != set(intake_by_id):
        fail(
            "generated/playbook_review_packet_contracts.min.json and "
            "generated/playbook_review_intake.min.json must keep review-track scope identical"
        )

    review_status_payload = read_json(PLAYBOOK_REVIEW_STATUS_PATH)
    if not isinstance(review_status_payload, dict):
        fail("generated/playbook_review_status.min.json must stay an object")
    review_status_by_id = {
        entry["playbook_id"]: entry
        for entry in review_status_payload.get("playbooks", [])
        if isinstance(entry, dict) and isinstance(entry.get("playbook_id"), str)
    }

    composition_manifest_payload = read_json(PLAYBOOK_COMPOSITION_MANIFEST_PATH)
    if not isinstance(composition_manifest_payload, dict):
        fail("generated/playbook_composition_manifest.json must stay an object")
    managed_playbook_names = composition_manifest_payload.get("managed_playbooks")
    if not isinstance(managed_playbook_names, list):
        fail("generated/playbook_composition_manifest.json must expose managed_playbooks")
    managed_playbook_names = {item for item in managed_playbook_names if isinstance(item, str)}

    scoped_ids = [entry.get("playbook_id") for entry in entries if isinstance(entry, dict)]
    expected_scope = sorted(set(packet_by_id) & set(intake_by_id))
    if scoped_ids != expected_scope:
        fail("generated/playbook_landing_governance.min.json must cover the review-track scope exactly once")

    for index, entry in enumerate(entries):
        location = f"generated/playbook_landing_governance.min.json.playbooks[{index}]"
        if not isinstance(entry, dict):
            fail(f"{location} must be an object")

        playbook_id = entry.get("playbook_id")
        if not isinstance(playbook_id, str) or playbook_id not in packet_by_id or playbook_id not in intake_by_id:
            fail(f"{location}.playbook_id must resolve in the shared review-track scope")
        packet_entry = packet_by_id[playbook_id]
        intake_entry = intake_by_id[playbook_id]
        registry_entry = playbooks_by_id.get(playbook_id)
        review_status_entry = review_status_by_id.get(playbook_id)

        expected_name = packet_entry.get("playbook_name")
        if entry.get("playbook_name") != expected_name:
            fail(f"{location}.playbook_name must match generated/playbook_review_packet_contracts.min.json")
        if intake_entry.get("playbook_name") != expected_name:
            fail(f"{location}.playbook_name must stay aligned with generated/playbook_review_intake.min.json")

        expected_status = registry_entry.get("status") if registry_entry is not None else None
        if entry.get("registry_status") != expected_status:
            fail(f"{location}.registry_status must match generated/playbook_registry.min.json")
        if expected_status != "experimental":
            fail(f"{location} review-track playbooks must stay experimental in generated/playbook_registry.min.json")

        if entry.get("in_registry") is not (registry_entry is not None):
            fail(f"{location}.in_registry must reflect generated/playbook_registry.min.json")
        if entry.get("in_review_packet_contracts") is not True:
            fail(f"{location}.in_review_packet_contracts must stay true for every scoped playbook")
        if entry.get("in_review_intake") is not True:
            fail(f"{location}.in_review_intake must stay true for every scoped playbook")
        if entry.get("in_review_status") is not (review_status_entry is not None):
            fail(f"{location}.in_review_status must reflect generated/playbook_review_status.min.json")

        expected_gate_verdict = review_status_entry.get("gate_verdict") if review_status_entry is not None else None
        if entry.get("gate_verdict") != expected_gate_verdict:
            fail(f"{location}.gate_verdict must match generated/playbook_review_status.min.json when present")
        if expected_gate_verdict is not None and expected_gate_verdict not in {"composition-landed", "hold"}:
            fail(f"{location}.gate_verdict must stay within the review-track landing verdict set")

        expected_in_manifest = isinstance(expected_name, str) and expected_name in managed_playbook_names
        if entry.get("in_composition_manifest") is not expected_in_manifest:
            fail(f"{location}.in_composition_manifest must reflect generated/playbook_composition_manifest.json")
        if expected_gate_verdict == "composition-landed" and not expected_in_manifest:
            fail(
                f"{location} must be represented in generated/playbook_composition_manifest.json "
                "when gate_verdict is composition-landed"
            )

        blockers = entry.get("blockers")
        if not isinstance(blockers, list) or not all(isinstance(item, str) for item in blockers):
            fail(f"{location}.blockers must be a list of strings")
        if entry.get("landing_passed") is not (len(blockers) == 0):
            fail(f"{location}.landing_passed must reflect whether blockers is empty")
        if blockers:
            fail(f"{location} must not carry blockers in the committed governance surface")


def validate_questbook_surface(repo_root: Path = REPO_ROOT) -> None:
    questbook_path = repo_root / "QUESTBOOK.md"
    harvest_doc_path = repo_root / "docs" / "QUEST_HARVEST_AND_REANCHOR.md"
    alignment_doc_path = repo_root / "docs" / "ORCHESTRATOR_ALIGNMENT_SURFACES.md"
    quest_ids = discover_questbook_quest_ids(repo_root)
    missing_foundation = [
        quest_id for quest_id in FOUNDATION_QUESTBOOK_QUEST_IDS if quest_id not in quest_ids
    ]
    if missing_foundation:
        missing_display = ", ".join(missing_foundation)
        fail(f"quests/ must include the foundation quest ids: {missing_display}")
    quest_paths = {quest_id: repo_root / "quests" / f"{quest_id}.yaml" for quest_id in quest_ids}

    questbook_text = read_text(questbook_path)
    questbook_location = questbook_path.relative_to(repo_root).as_posix()

    harvest_doc_text = read_text(harvest_doc_path)
    harvest_doc_location = harvest_doc_path.relative_to(repo_root).as_posix()
    sections = markdown_sections(harvest_doc_text)
    missing_sections = [
        section_name for section_name in QUESTBOOK_REQUIRED_DOC_SECTIONS if section_name not in sections
    ]
    if missing_sections:
        fail(
            f"{harvest_doc_location} is missing required questbook sections: "
            + ", ".join(missing_sections)
        )
    for token in QUESTBOOK_REQUIRED_DOC_TOKENS:
        if token not in harvest_doc_text:
            fail(f"{harvest_doc_location} must mention '{token}' explicitly")

    active_quest_ids: list[str] = []
    closed_quest_ids: list[str] = []
    expected_catalog_entries: list[dict[str, object]] = []
    expected_dispatch_entries: list[dict[str, object]] = []
    needs_alignment_doc = alignment_doc_path.exists()
    for quest_id, quest_path in quest_paths.items():
        payload = read_yaml(quest_path)
        location = quest_path.relative_to(repo_root).as_posix()
        if not isinstance(payload, dict):
            fail(f"{location} must contain a YAML mapping")
        validate_against_external_schema(payload, EXTERNAL_QUEST_SCHEMA_PATH, location=location)
        if payload.get("schema_version") != "work_quest_v1":
            fail(f"{location} must declare schema_version 'work_quest_v1'")
        if payload.get("id") != quest_id:
            fail(f"{location} must declare id '{quest_id}'")
        if payload.get("repo") != "aoa-playbooks":
            fail(f"{location} must target repo 'aoa-playbooks'")
        if payload.get("public_safe") is not True:
            fail(f"{location} must declare public_safe: true")
        validate_optional_orchestrator_quest_fields(payload, location=location, repo_root=repo_root)
        expected_orchestrator_pair = ORCHESTRATOR_ALIGNMENT_QUESTS.get(quest_id)
        if expected_orchestrator_pair is not None:
            needs_alignment_doc = True
            expected_ref, expected_target = expected_orchestrator_pair
            if payload.get("kind") != "seam":
                fail(f"{location} must keep kind 'seam' for orchestrator alignment quests")
            if payload.get("owner_surface") != "docs/ORCHESTRATOR_ALIGNMENT_SURFACES.md":
                fail(f"{location} must keep owner_surface docs/ORCHESTRATOR_ALIGNMENT_SURFACES.md")
            if payload.get("orchestrator_class_ref") != expected_ref:
                fail(f"{location} must keep orchestrator_class_ref '{expected_ref}'")
            if payload.get("capability_target") != expected_target:
                fail(f"{location} must keep capability_target '{expected_target}'")
        if quest_id == "AOA-PB-Q-0007":
            if payload.get("kind") != "seam":
                fail(f"{location} must keep kind 'seam' for the bridge-wave party template quest")
            if payload.get("owner_surface") != "docs/PARTY_TEMPLATE_MODEL.md":
                fail(f"{location} must keep owner_surface docs/PARTY_TEMPLATE_MODEL.md")
        if payload.get("state") in CLOSED_QUEST_STATES:
            closed_quest_ids.append(quest_id)
        else:
            active_quest_ids.append(quest_id)
        source_path = quest_path.relative_to(repo_root).as_posix()
        expected_catalog_entries.append(
            build_expected_quest_catalog_entry(payload, source_path=source_path)
        )
        expected_dispatch_entries.append(
            build_expected_quest_dispatch_entry(payload, quest_id=quest_id, source_path=source_path)
        )

    if needs_alignment_doc:
        alignment_text = read_text(alignment_doc_path)
        alignment_location = alignment_doc_path.relative_to(repo_root).as_posix()
        for token in ORCHESTRATOR_ALIGNMENT_REQUIRED_TOKENS:
            if token not in alignment_text:
                fail(f"{alignment_location} must mention '{token}' explicitly")

    for token in QUESTBOOK_REQUIRED_INDEX_TOKENS:
        if token not in questbook_text:
            fail(f"{questbook_location} must mention '{token}' explicitly")
    for quest_id in active_quest_ids:
        if quest_id not in questbook_text:
            fail(f"{questbook_location} must reference active quest id '{quest_id}'")
    for quest_id in closed_quest_ids:
        if quest_id in questbook_text:
            fail(f"{questbook_location} must not list closed quest id '{quest_id}'")

    actual_catalog = read_json(repo_root / "generated" / "quest_catalog.min.json")
    if actual_catalog != expected_catalog_entries:
        fail("generated/quest_catalog.min.json is out of date or mismatched")
    actual_catalog_example = read_json(repo_root / "generated" / "quest_catalog.min.example.json")
    if actual_catalog_example != expected_catalog_entries:
        fail("generated/quest_catalog.min.example.json is out of date or mismatched")
    actual_dispatch = read_json(repo_root / "generated" / "quest_dispatch.min.json")
    if not isinstance(actual_dispatch, list):
        fail("generated/quest_dispatch.min.json must be an array")
    for index, entry in enumerate(actual_dispatch):
        validate_against_external_schema(
            entry,
            EXTERNAL_QUEST_DISPATCH_SCHEMA_PATH,
            location=f"generated/quest_dispatch.min.json[{index}]",
        )
    if actual_dispatch != expected_dispatch_entries:
        fail("generated/quest_dispatch.min.json is out of date or mismatched")
    actual_dispatch_example = read_json(repo_root / "generated" / "quest_dispatch.min.example.json")
    if not isinstance(actual_dispatch_example, list):
        fail("generated/quest_dispatch.min.example.json must be an array")
    for index, entry in enumerate(actual_dispatch_example):
        validate_against_external_schema(
            entry,
            EXTERNAL_QUEST_DISPATCH_SCHEMA_PATH,
            location=f"generated/quest_dispatch.min.example.json[{index}]",
        )
    if actual_dispatch_example != expected_dispatch_entries:
        fail("generated/quest_dispatch.min.example.json is out of date or mismatched")

    if "AOA-PB-Q-0007" in quest_ids:
        party_template_model_path = repo_root / PARTY_TEMPLATE_MODEL_NAME
        build_synergy_posture_path = repo_root / BUILD_SYNERGY_POSTURE_NAME
        party_template_schema_path = repo_root / PARTY_TEMPLATE_SCHEMA_NAME
        party_template_example_path = repo_root / PARTY_TEMPLATE_EXAMPLE_NAME
        playbook_registry_path = repo_root / "generated" / "playbook_registry.min.json"

        party_template_model_text = read_text(party_template_model_path)
        for token in PARTY_TEMPLATE_MODEL_REQUIRED_TOKENS:
            if token not in party_template_model_text:
                fail(f"{party_template_model_path.relative_to(repo_root).as_posix()} must mention '{token}' explicitly")

        build_synergy_text = read_text(build_synergy_posture_path)
        for token in BUILD_SYNERGY_REQUIRED_TOKENS:
            if token not in build_synergy_text:
                fail(f"{build_synergy_posture_path.relative_to(repo_root).as_posix()} must mention '{token}' explicitly")

        schema_payload = read_json(party_template_schema_path)
        if not isinstance(schema_payload, dict):
            fail("schemas/party_template_catalog.schema.json must be a JSON object")
        if schema_payload.get("title") != "party_template_catalog_v1":
            fail("schemas/party_template_catalog.schema.json must keep title 'party_template_catalog_v1'")
        Draft202012Validator.check_schema(schema_payload)

        example_payload = read_json(party_template_example_path)
        if not isinstance(example_payload, dict):
            fail("generated/party_template_cards.min.example.json must be a JSON object")
        validate_against_external_schema(
            example_payload,
            party_template_schema_path,
            location=party_template_example_path.relative_to(repo_root).as_posix(),
        )
        if example_payload.get("schema_version") != "party_template_catalog_v1":
            fail("generated/party_template_cards.min.example.json must keep schema_version 'party_template_catalog_v1'")
        templates = example_payload.get("templates")
        if not isinstance(templates, list) or not templates:
            fail("generated/party_template_cards.min.example.json must expose a non-empty templates list")
        playbook_registry_payload = read_json(playbook_registry_path)
        if not isinstance(playbook_registry_payload, dict):
            fail("generated/playbook_registry.min.json must remain a JSON object")
        registry_entries = playbook_registry_payload.get("playbooks")
        if not isinstance(registry_entries, list):
            fail("generated/playbook_registry.min.json must expose a playbooks array")
        playbooks_by_id = {
            entry.get("id"): entry
            for entry in registry_entries
            if isinstance(entry, dict) and isinstance(entry.get("id"), str)
        }
        for index, template in enumerate(templates):
            if not isinstance(template, dict):
                fail(f"generated/party_template_cards.min.example.json.templates[{index}] must be an object")
            playbook_id = template.get("playbook_id")
            if playbook_id not in playbooks_by_id:
                fail(
                    "generated/party_template_cards.min.example.json references a playbook_id that does not resolve "
                    f"in generated/playbook_registry.min.json: {playbook_id}"
                )
            if template.get("public_safe") is not True:
                fail(f"generated/party_template_cards.min.example.json.templates[{index}] must keep public_safe true")


def main() -> int:
    try:
        validate_nested_agents_surface()
        validate_schema_surface()
        validate_activation_schema_surface()
        validate_federation_schema_surface()
        validate_review_status_schema_surface()
        validate_review_packet_contracts_schema_surface()
        validate_antifragility_stress_surfaces()
        validate_codex_plane_rollout_cycle_companion()
        playbooks_by_id = validate_registry()
        agent_names = load_agent_names()
        model_tier_artifacts = load_model_tier_artifacts()
        evals_by_name = load_eval_catalog()
        skills_by_name = load_skill_catalog()
        validate_activation_collection(
            playbooks_by_id,
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
        )
        frontmatter_by_id = validate_authored_bundles(
            playbooks_by_id,
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
            skills_by_name=skills_by_name,
        )
        validate_federation_collection(
            frontmatter_by_id,
            agent_names=agent_names,
            evals_by_name=evals_by_name,
            skills_by_name=skills_by_name,
        )
        validate_composition_surfaces(frontmatter_by_id)
        validate_activation_examples(
            playbooks_by_id,
            agent_names=agent_names,
            model_tier_artifacts=model_tier_artifacts,
            evals_by_name=evals_by_name,
        )
        validate_harvest_templates()
        validate_real_run_workflow_surfaces()
        validate_playbook_review_status_surface(playbooks_by_id)
        validate_playbook_review_packet_contracts_surface(playbooks_by_id)
        validate_playbook_review_intake_surface()
        validate_playbook_landing_governance_surface(playbooks_by_id)
        validate_phase_alpha_surfaces(playbooks_by_id, evals_by_name=evals_by_name)
        validate_questbook_surface()
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    print("[ok] validated nested AGENTS docs")
    print("[ok] validated playbook registry schema surface")
    print("[ok] validated playbook activation schema surface")
    print("[ok] validated playbook federation schema surface")
    print("[ok] validated playbook review-status schema surface")
    print("[ok] validated playbook review-packet contracts schema surface")
    print("[ok] validated antifragility stress-lane adjunct surfaces")
    print("[ok] validated codex-plane rollout cycle companion surfaces")
    print("[ok] validated generated/playbook_registry.min.json")
    print("[ok] validated generated/playbook_activation_surfaces.min.json")
    print("[ok] validated authored playbook bundles")
    print("[ok] validated generated/playbook_federation_surfaces.min.json")
    print("[ok] validated generated playbook composition surfaces")
    print("[ok] validated generated playbook review-status surface")
    print("[ok] validated generated playbook review-packet contracts surface")
    print("[ok] validated generated playbook review intake surface")
    print("[ok] validated generated playbook landing governance surface")
    print("[ok] validated Phase Alpha readiness surfaces")
    print("[ok] validated playbook activation examples")
    print("[ok] validated shipped playbook real-run harvest templates")
    print("[ok] validated repo-first real-run workflow surfaces")
    print("[ok] validated questbook foundation surface")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
