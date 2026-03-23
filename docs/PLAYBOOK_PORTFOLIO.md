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

## Portfolio gaps

The current portfolio is strong on guarded, evidence-heavy, and restartable routes.
The next coverage gaps are still more operational and federated:
- release or migration cutover across neighboring AoA layers
- incident or recovery routing with explicit rollback and handoff
- validation-driven remediation across source-of-truth boundaries

These gaps matter because they test whether the playbook layer can scale beyond introspective or checkpoint-heavy routes.

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
