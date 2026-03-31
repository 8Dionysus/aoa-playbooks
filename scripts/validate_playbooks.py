#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
from pathlib import Path

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
REGISTRY_PATH = REPO_ROOT / "generated" / "playbook_registry.min.json"
ACTIVATION_COLLECTION_PATH = REPO_ROOT / "generated" / "playbook_activation_surfaces.min.json"
FEDERATION_COLLECTION_PATH = REPO_ROOT / "generated" / "playbook_federation_surfaces.min.json"
COMPOSITION_CONFIG_PATH = REPO_ROOT / "config" / "playbook_composition_overrides.json"
PLAYBOOK_HANDOFF_CONTRACTS_PATH = REPO_ROOT / "generated" / "playbook_handoff_contracts.json"
PLAYBOOK_FAILURE_CATALOG_PATH = REPO_ROOT / "generated" / "playbook_failure_catalog.json"
PLAYBOOK_SUBAGENT_RECIPES_PATH = REPO_ROOT / "generated" / "playbook_subagent_recipes.json"
PLAYBOOK_AUTOMATION_SEEDS_PATH = REPO_ROOT / "generated" / "playbook_automation_seeds.json"
PLAYBOOK_COMPOSITION_MANIFEST_PATH = REPO_ROOT / "generated" / "playbook_composition_manifest.json"
SCHEMA_PATH = REPO_ROOT / "schemas" / "playbook-registry.schema.json"
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
QUESTBOOK_QUEST_IDS = ("AOA-PB-Q-0001", "AOA-PB-Q-0002")
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
    "AOA-PB-Q-0001",
    "AOA-PB-Q-0002",
    "Frontier",
    "Near",
    "docs/QUEST_HARVEST_AND_REANCHOR.md",
)
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
}
REAL_RUN_WORKFLOW_PATH = REPO_ROOT / "docs" / "PLAYBOOK_REAL_RUN_WORKFLOW.md"
REAL_RUN_SUMMARY_HOME_PATH = REPO_ROOT / "docs" / "real-runs" / "README.md"
REAL_RUN_SUMMARY_DIR = REPO_ROOT / "docs" / "real-runs"
GATE_REVIEW_DIR = REPO_ROOT / "docs" / "gate-reviews"
REAL_RUN_SUMMARY_SLUG_REQUIREMENTS = {
    "split-wave-cross-repo-rollout": (
        "wave_plan",
        "bridge_surface_pack",
        "downstream_revalidation_pack",
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
}
REVIEWED_SUMMARY_GATE_SENTENCE = (
    "Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still "
    "require explicit gate review under `docs/gate-reviews/`."
)
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
)
COMPOSITION_COLLECTION_PLAYBOOK_IDS = (
    "AOA-P-0011",
    "AOA-P-0012",
    "AOA-P-0013",
    "AOA-P-0014",
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
REAL_RUN_SUMMARY_FILENAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.([a-z0-9-]+)\.md$")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")
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
    for root in (REPO_ROOT, AOA_AGENTS_ROOT, AOA_EVALS_ROOT, AOA_SKILLS_ROOT, AOA_MEMO_ROOT):
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


def read_yaml(path: Path) -> object:
    text = read_text(path)
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as exc:
        fail(f"invalid YAML in {display_path(path)}: {exc}")


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
    return_posture = payload.get("return_posture")
    return_anchor_artifacts = payload.get("return_anchor_artifacts")
    return_reentry_modes = payload.get("return_reentry_modes")

    if return_posture is None:
        if return_anchor_artifacts is not None:
            fail(f"{location}.return_anchor_artifacts must not appear without return_posture")
        if return_reentry_modes is not None:
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
            rf"docs/real-runs/(?:YYYY-MM-DD|\d{{4}}-\d{{2}}-\d{{2}})\.{re.escape(slug)}\.md"
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
                f"{location} must match the filename pattern YYYY-MM-DD.<playbook-slug>.md"
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


def validate_questbook_surface(repo_root: Path = REPO_ROOT) -> None:
    questbook_path = repo_root / "QUESTBOOK.md"
    harvest_doc_path = repo_root / "docs" / "QUEST_HARVEST_AND_REANCHOR.md"
    quest_paths = {quest_id: repo_root / "quests" / f"{quest_id}.yaml" for quest_id in QUESTBOOK_QUEST_IDS}

    questbook_text = read_text(questbook_path)
    questbook_location = questbook_path.relative_to(repo_root).as_posix()
    for token in QUESTBOOK_REQUIRED_INDEX_TOKENS:
        if token not in questbook_text:
            fail(f"{questbook_location} must mention '{token}' explicitly")

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

    for quest_id, quest_path in quest_paths.items():
        payload = read_yaml(quest_path)
        location = quest_path.relative_to(repo_root).as_posix()
        if not isinstance(payload, dict):
            fail(f"{location} must contain a YAML mapping")
        if payload.get("schema_version") != "work_quest_v1":
            fail(f"{location} must declare schema_version 'work_quest_v1'")
        if payload.get("id") != quest_id:
            fail(f"{location} must declare id '{quest_id}'")
        if payload.get("repo") != "aoa-playbooks":
            fail(f"{location} must target repo 'aoa-playbooks'")
        if payload.get("public_safe") is not True:
            fail(f"{location} must declare public_safe: true")


def main() -> int:
    try:
        validate_nested_agents_surface()
        validate_schema_surface()
        validate_activation_schema_surface()
        validate_federation_schema_surface()
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
        validate_questbook_surface()
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    print("[ok] validated nested AGENTS docs")
    print("[ok] validated playbook registry schema surface")
    print("[ok] validated playbook activation schema surface")
    print("[ok] validated playbook federation schema surface")
    print("[ok] validated generated/playbook_registry.min.json")
    print("[ok] validated generated/playbook_activation_surfaces.min.json")
    print("[ok] validated authored playbook bundles")
    print("[ok] validated generated/playbook_federation_surfaces.min.json")
    print("[ok] validated generated playbook composition surfaces")
    print("[ok] validated playbook activation examples")
    print("[ok] validated shipped playbook real-run harvest templates")
    print("[ok] validated repo-first real-run workflow surfaces")
    print("[ok] validated questbook foundation surface")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
