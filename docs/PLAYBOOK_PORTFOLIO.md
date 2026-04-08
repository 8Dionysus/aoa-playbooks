# Playbook Portfolio Guidance

This document describes how the AoA playbook layer should be covered as a portfolio.

The point is not completeness for its own sake.
The point is to make sure the repository grows across distinct scenario families instead of overfitting to one favorite route shape.

## Portfolio goal

`aoa-playbooks` should cover recurring scenario families that are materially different in:
- trigger posture
- fallback posture
- evidence posture
- handoff density
- cross-layer composition shape

If a new playbook does not add a distinct scenario family, it probably belongs as a refinement of an existing playbook rather than a new entry.

## Current portfolio classes

The current authored set already covers these classes:

| Class | Primary shape | Representative playbooks |
| --- | --- | --- |
| Repository bootstrap | establish a new repository or layer with bounded scaffolding and validation | `repo-bootstrap` |
| Safe change rollout | make a bounded change with validation, review, and rollback posture | `safe-change-rollout` |
| Bounded research pass | answer a constrained question with explicit synthesis and next steps | `bounded-research-pass` |
| Release prep | prepare a repository or layer for merge or release | `release-prep` |
| Memory curation pass | curate memory outputs without confusing them with proof or execution | `memory-curation-pass` |
| Self-agent checkpoint rollout | handle policy-sensitive or self-changing work with approval and rollback | `self-agent-checkpoint-rollout` |
| Witness to compost | preserve a witness and promote it toward memo or knowledge forms | `witness-to-compost-pilot` |
| Long-horizon tier orchestration | coordinate a long route through explicit tier handoffs | `long-horizon-model-tier-orchestra` |
| Restartable inquiry | preserve inquiry continuity across pauses and relaunches | `restartable-inquiry-loop` |
| Cross-repo boundary rollout | coordinate bounded changes across more than one source-owned AoA repository | `cross-repo-boundary-rollout` |
| Split-wave cross-repo rollout | coordinate ordered multi-wave cross-repo changes where upstream bridge surfaces must land before downstream revalidation or merge | `split-wave-cross-repo-rollout` |
| Validation-driven remediation | remediate a failed validator or proof surface through bounded corrective change and revalidation across source-owned boundaries | `validation-driven-remediation` |
| Release or migration cutover | switch authority during a bounded cutover window through freeze posture, go-no-go gating, post-cutover verification, and rollback-or-handoff closure | `release-migration-cutover` |
| Incident or recovery routing | stabilize a live cross-boundary incident through bounded rollback or degraded-mode recovery, recovery verification, and explicit handoff | `incident-recovery-routing` |
| Owner-first capability landing | land a reviewed capability through owner-first landing, bounded rollout, and post-landing hardening across neighboring AoA layers | `owner-first-capability-landing` |
| Closeout-to-owner continuity | carry a reviewed closeout through persistent owner handoff, bounded owner authorship, and merged follow-through | `closeout-owner-follow-through-continuity` |
| Federated live publisher activation | activate known live publishers in owner order through readiness audit, publication checks, and stats-visible closure | `federated-live-publisher-activation` |

## Portfolio gaps

The current portfolio is strong on guarded, evidence-heavy, restartable, and operational cross-boundary routes.
The last major operational and federated gap is now covered, so the main risk has shifted from undercoverage to semantic overlap and premature composition.
The next portfolio move is a consolidation wave, not another new playbook:
- use [PLAYBOOK_OPERATIONAL_FAMILY](PLAYBOOK_OPERATIONAL_FAMILY.md) to choose between `AOA-P-0010`, `AOA-P-0012`, `AOA-P-0014`, `AOA-P-0017`, `AOA-P-0018`, `AOA-P-0019`, `AOA-P-0020`, `AOA-P-0021`, `AOA-P-0023`, and `AOA-P-0024`
- use [PLAYBOOK_REAL_RUN_HARVEST](PLAYBOOK_REAL_RUN_HARVEST.md) to capture reviewable evidence from fresh `AOA-P-0018`, `AOA-P-0019`, `AOA-P-0020`, and `AOA-P-0024` follow-on runs while keeping already-landed `AOA-P-0017`, `AOA-P-0021`, and `AOA-P-0023` bounded
- use [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) before any new handoff bridge, subagent split, automation seed, or failure/follow-up mapping reaches composition

The operational family now covers:
- `AOA-P-0010` = generic cross-repo rollout baseline
- `AOA-P-0012` = preview-first infra change before a live incident
- `AOA-P-0014` = local-only stack diagnosis and blocker isolation
- `AOA-P-0017` = ordered multi-wave rollout
- `AOA-P-0018` = post-failure remediation after the incident is already bounded
- `AOA-P-0019` = planned authority-switch cutover window
- `AOA-P-0020` = live cross-boundary incident stabilization and recovery handoff
- `AOA-P-0021` = owner-first landing from reviewed lineage into bounded rollout and post-landing hardening
- `AOA-P-0023` = reviewed closeout continuity into persistent owner follow-through and merged closure
- `AOA-P-0024` = owner-ordered live publisher activation after a reviewed readiness audit

## Coverage rules

Use these rules when deciding whether to add a new playbook:

1. Add a new playbook only when the scenario family is distinct.
2. Refine an existing playbook when the change only adds one more decision or one more variation.
3. Prefer a new playbook when the scenario introduces a different fallback shape or a different evidence posture.
4. Prefer a new playbook when the scenario crosses a new ownership boundary.
5. Prefer a refinement when the scenario stays in the same layer mix and the same handoff pattern.

## Portfolio checks

A healthy portfolio should answer these questions:
- Do we cover both local and cross-repo scenarios?
- Do we cover both operational and reflective routes?
- Do we cover both rollback-heavy and handoff-heavy fallback posture?
- Do we cover both short bounded routes and long restartable routes?
- Do we avoid overrepresenting one scenario family just because it is easy to author?

## Composition guidance

When a scenario is underrepresented, do not inflate it just to fill a matrix.
The playbook layer should only record honest recurring method.

When a scenario family is already covered, prefer tightening:
- trigger boundaries
- fallback posture
- evidence posture
- handoffs
- neighbor references

This keeps the portfolio stable and keeps future additions legible.
