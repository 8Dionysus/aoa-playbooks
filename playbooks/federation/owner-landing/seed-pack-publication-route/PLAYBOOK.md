---
id: AOA-P-0049
name: seed-pack-publication-route
status: experimental
summary: Coordinates a reviewed seed pack from staging through owner routing, guarded planting, repository adaptation, publication, closeout receipts, stats refresh, and owner-routed follow-through.
scenario: seed_pack_publication_route
trigger: reviewed_seed_pack_ready_for_cross_repo_planting_and_publication
prerequisites:
  - seed_pack_path_and_digest_named
  - owner_route_map_named
  - mutation_gates_and_dry_run_plan_named
  - validation_and_publication_surfaces_named
  - closeout_and_stats_followthrough_named
participating_agents:
  - architect
  - coder
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - source-of-truth
  - change-protocol
  - review
  - evaluation
  - memory-curation
evaluation_posture: strict
memory_posture: bounded_recall
fallback_mode: safe_stop
expected_artifacts:
  - seed_integrity_record
  - owner_route_map
  - planting_plan
  - repo_adaptation_notes
  - validation_matrix
  - publication_receipts
  - closeout_stats_report
  - owner_followthrough_notes
eval_anchors:
  - aoa-bounded-change-quality
  - aoa-verification-honesty
return_posture: artifact_anchor
return_anchor_artifacts:
  - seed_integrity_record
  - validation_matrix
  - publication_receipts
  - closeout_stats_report
  - owner_followthrough_notes
return_reentry_modes:
  - previous_phase
  - review_gate
  - rollback_gate
  - safe_stop
memo_recall_modes:
  - episodic
  - semantic
memo_scope_default: workspace
memo_scope_ceiling: workspace
memo_read_path: inspect_then_expand
memo_checkpoint_posture: preferred
memo_source_route_policy: required
---

# Seed Pack Publication Route

## Intent

Use this playbook when a reviewed seed pack is ready to move from staging into
one or more owner repositories, and the honest route now spans seed integrity,
owner mapping, guarded planting, repository-specific adaptation, validation,
publication, closeout receipts, stats refresh, and surviving follow-through.

The playbook coordinates the scenario. It does not make a seed pack canonical by
itself, turn generated closeout notes into source truth, or let successful PR
publication stand in for owner-layer adaptation.

## Trigger boundary

Use when a seed pack has a named source path, a visible review or handoff
context, and a cross-repository planting route that needs publication and
closeout evidence.

Do not use it for ordinary single-file imports, private scratch extraction,
hidden automation, or cases where the seed contents have not been inspected
well enough to separate useful source material from technical trash.

## Prerequisites

- The seed pack path, digest, and extraction boundary are named before import.
- Owner repositories and source-of-truth boundaries are mapped before mutation.
- Guard, dry-run, and rollback posture are explicit before files are changed.
- Repository adaptation rules and validation commands are named for each owner.
- Publication, closeout, stats, and residual follow-through surfaces are named.

## Participating agents

- `architect` maps owner routes, source-of-truth boundaries, and stop-lines.
- `coder` performs bounded planting, adaptation, and publication work.
- `reviewer` checks technical-trash exclusion, diff scope, and owner fit.
- `evaluator` judges whether validation and closeout claims match evidence.
- `memory-keeper` separates durable lessons from proof and source truth.

## Required skills

- `aoa-source-of-truth-check`
- `aoa-bounded-context-map`
- `aoa-change-protocol`
- `aoa-contract-test`
- `aoa-invariant-coverage-audit`
- `aoa-checkpoint-closeout-bridge`

These skills support reviewable planting and closure. They do not create a
hidden importer, merge authority, memory authority, or stats authority.

## Decision points

1. Decide whether the seed pack is intact and reviewed enough to plant now.
2. Decide which owner repository owns each surviving seed surface.
3. Decide which files are technical trash, generated-only context, or source
   material that must be adapted before landing.
4. Decide whether each repository needs code, docs, config, tests, or only
   generated-owner metadata.
5. Decide whether validation is strong enough to publish through PR and merge.
6. Decide whether closeout receipts and stats refresh are earned by source
   evidence or only remain provisional notes.
7. Decide which surviving follow-through belongs in playbooks, techniques,
   memo, stats, evals, agents, SDK, public routing, or seed staging.

## Handoffs

- Seed lineage, staging notes, and pack inspection route to `Dionysus`.
- Public profile, shared-root projection, and route-map posture route to
  `8Dionysus`.
- CLI behavior, schema behavior, and closeout execution contracts route to
  `aoa-sdk`.
- Role posture and agent handoff language route to `aoa-agents`.
- Scenario composition and recurring route shape stay in `aoa-playbooks`.
- Proof bundles, canaries, and verdict posture route to `aoa-evals`.
- Memory candidates and recall contracts route to `aoa-memo`.
- Derived receipt observability and stats refresh route to `aoa-stats`.
- Skill procedure changes route to `aoa-skills`.

## Fallback and rollback posture

Fallback mode is `safe_stop`.

Stop before mutation when the seed digest, owner map, or extraction boundary is
ambiguous. Stop during planting when technical trash cannot be separated from
source material without owner review. Stop before publication when validation,
required checks, or branch protection signals contradict the claimed state.

Rollback means reverting only the current bounded branch edits, closing or
updating the affected PR, or opening an owner follow-up after merge. Do not
rewrite shared history, demote owner truth, or let closeout notes patch over a
failed validation gate.

## Expected evidence posture

Evidence should include the seed pack path and digest, extraction manifest,
technical-trash exclusions, owner route map, guard and dry-run outputs, diff
scope, repository validation matrix, PR and CI receipts, merge receipts, closeout
report, stats refresh output, and residual owner follow-through notes.

Runtime closeout and stats evidence may support the route only when it remains
subordinate to owner repository commits, reviewed artifacts, and explicit source
refs.

## Expected artifacts

- `seed_integrity_record`
- `owner_route_map`
- `planting_plan`
- `repo_adaptation_notes`
- `validation_matrix`
- `publication_receipts`
- `closeout_stats_report`
- `owner_followthrough_notes`

## Eval anchors

- `aoa-bounded-change-quality`
- `aoa-verification-honesty`

Use `aoa-bounded-change-quality` to judge whether the planting stayed scoped to
the seed route and owner repositories rather than becoming opportunistic cleanup.
Use `aoa-verification-honesty` to judge whether validation, PR checks, merge
receipts, closeout, and stats claims are named with their real limits.

## Memory writeback

Memory writeback is candidate-only until source refs, route context, and owner
follow-through are explicit. A seed lesson may become a memory candidate after
closeout, but it does not become proof, authorization, or canonical owner
doctrine.

Do not store raw seed contents as durable memory merely because they were
planted. Store only the bounded route lesson, residual risk, and owner refs that
survive review.

## Canonical route

1. Name the seed pack path, digest, review context, and extraction boundary.
2. Inspect the pack and separate source material from technical trash.
3. Map each surviving seed surface to its owner repository.
4. Run ingress, guard, and dry-run posture for each mutating owner route.
5. Plant and adapt the files inside the smallest honest repository scope.
6. Run repository-local validation and record the validation matrix.
7. Publish through PRs or the approved owner publication route.
8. Confirm CI, merge receipts, and local checkout alignment.
9. Execute reviewed closeout and refresh derived stats only after source
   evidence exists.
10. Route residual follow-through to the owning layer instead of leaving it in
    session notes.
