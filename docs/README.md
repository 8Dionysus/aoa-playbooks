# Documentation Map

This file is the human-first entrypoint for the `docs/` surface of `aoa-playbooks`.

Use it when you want to understand the AoA playbook layer rather than the broader federation as a whole.

## Start here

- Read [CHARTER](../CHARTER.md) for the role and boundaries of the playbook layer.
- Read [PLAYBOOK_MODEL](PLAYBOOK_MODEL.md) for the conceptual model.
- Read [BOUNDARIES](BOUNDARIES.md) for ownership discipline relative to neighboring AoA layers.
- Read [PLAYBOOK_BUNDLE_CONTRACT](PLAYBOOK_BUNDLE_CONTRACT.md) for the authored bundle contract.
- Read [PLAYBOOK_EXECUTION_SEAM](PLAYBOOK_EXECUTION_SEAM.md) for the derived runtime-readable activation seam.
- Read [PLAYBOOK_OPERATIONAL_FAMILY](PLAYBOOK_OPERATIONAL_FAMILY.md) for chooser discipline across the operational playbook family.
- Read [HANDOFF_CONTRACTS](HANDOFF_CONTRACTS.md) for the bounded playbook-to-skill handoff bridge.
- Read [FAILURE_RECOVERY](FAILURE_RECOVERY.md) for the shared failure catalog posture.
- Read [SUBAGENT_PATTERNS](SUBAGENT_PATTERNS.md) for explicit subagent recipe doctrine.
- Read [AUTOMATION_SEEDS](AUTOMATION_SEEDS.md) for example-only automation seed posture.
- Read [PLAYBOOK_RECURRENCE_DISCIPLINE](PLAYBOOK_RECURRENCE_DISCIPLINE.md) for scenario-level recurrence posture.
- Read [PLAYBOOK_LIFECYCLE](PLAYBOOK_LIFECYCLE.md) for graduation and lifecycle doctrine.
- Read [PLAYBOOK_PORTFOLIO](PLAYBOOK_PORTFOLIO.md) for coverage matrix and portfolio guidance.
- Read [PLAYBOOK_REAL_RUN_WORKFLOW](PLAYBOOK_REAL_RUN_WORKFLOW.md) for the repo-first chooser -> run -> review -> gate workflow.
- Read [PLAYBOOK_REAL_RUN_HARVEST](PLAYBOOK_REAL_RUN_HARVEST.md) for reviewable evidence scaffolding for future real runs.
- Read [PLAYBOOK_STRESS_LANES](PLAYBOOK_STRESS_LANES.md) for additive degraded-lane doctrine inside recurring scenarios.
- Read [PLAYBOOK_STRESS_HARVEST](PLAYBOOK_STRESS_HARVEST.md) for bounded harvest and re-entry posture for stressed runs.
- Read [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) for the composition promotion gate surface.
- Read [PLAYBOOK_GAP_MATRIX](PLAYBOOK_GAP_MATRIX.md) for the current prioritized lifecycle posture of the portfolio.
- Read [RELEASING](RELEASING.md) for the bounded repo-level release flow.
- Open [../playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md](../playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md) for the first real playbook object.
- Read [ROADMAP](../ROADMAP.md) for the current direction.

## Docs in this repository

- [PLAYBOOK_MODEL](PLAYBOOK_MODEL.md) - what the playbook layer is for
- [BOUNDARIES](BOUNDARIES.md) - what the playbook layer owns and must not absorb
- [PLAYBOOK_BUNDLE_CONTRACT](PLAYBOOK_BUNDLE_CONTRACT.md) - how authored `PLAYBOOK.md` bundles stay compact, registry-aligned, and federation-checkable where needed
- [PLAYBOOK_EXECUTION_SEAM](PLAYBOOK_EXECUTION_SEAM.md) - how derived activation, federation, and composition surfaces stay readable without becoming second authored sources
- [PLAYBOOK_OPERATIONAL_FAMILY](PLAYBOOK_OPERATIONAL_FAMILY.md) - how the operational playbook family stays differentiated instead of semantically overlapping
- [HANDOFF_CONTRACTS](HANDOFF_CONTRACTS.md) - how derived playbook handoff packets point to `aoa-skills` without absorbing skill meaning
- [FAILURE_RECOVERY](FAILURE_RECOVERY.md) - how a shared failure catalog stays scenario-owned without becoming a persisted run engine
- [SUBAGENT_PATTERNS](SUBAGENT_PATTERNS.md) - how explicit subagent recipes stay bounded and example-shaped
- [AUTOMATION_SEEDS](AUTOMATION_SEEDS.md) - how automation prompt seeds stay illustrative rather than authoritative schedules
- [PLAYBOOK_RECURRENCE_DISCIPLINE](PLAYBOOK_RECURRENCE_DISCIPLINE.md) - how scenario routes return to valid anchors without turning the playbook layer into runtime machinery
- [PLAYBOOK_LIFECYCLE](PLAYBOOK_LIFECYCLE.md) - how playbooks graduate from registry rows to authored and federation-checked forms
- [PLAYBOOK_PORTFOLIO](PLAYBOOK_PORTFOLIO.md) - how the playbook layer stays broad enough across scenario families without overfitting
- [PLAYBOOK_REAL_RUN_WORKFLOW](PLAYBOOK_REAL_RUN_WORKFLOW.md) - how real operational runs become reviewed summaries and explicit gate verdicts without creating a runtime log layer
- [PLAYBOOK_REAL_RUN_HARVEST](PLAYBOOK_REAL_RUN_HARVEST.md) - how reviewable real-run evidence stays distinct from runtime state and from composition promotion itself
- [PLAYBOOK_STRESS_LANES](PLAYBOOK_STRESS_LANES.md) - how recurring playbooks expose a weaker, reviewable degraded lane without replacing source-owned receipts or proof
- [PLAYBOOK_STRESS_HARVEST](PLAYBOOK_STRESS_HARVEST.md) - how stressed runs harvest bounded evidence and explicit re-entry gates without seizing ownership of what happened
- [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) - how `AOA-P-0017`, `AOA-P-0018`, `AOA-P-0019`, `AOA-P-0020`, `AOA-P-0021`, and `AOA-P-0024` use explicit gate review before composition grows
- [PLAYBOOK_GAP_MATRIX](PLAYBOOK_GAP_MATRIX.md) - the current prioritized lifecycle matrix and next bounded portfolio moves
- [RELEASING](RELEASING.md) - how repo-level releases stay small, validated, and honest about remaining evidence gaps

## Notes

This repository should stay bounded.
Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.
If a document starts trying to become a technique corpus, workflow corpus, proof corpus, memory store, or routing surface, it probably belongs in a neighboring AoA repository instead.
