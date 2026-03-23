# Seam Pilot Report

As of March 22, 2026, this report records bounded, contract-first seam checks for the current AoA integration-closure wave.

It is not a runtime execution log.
It is a reviewable playbook-layer report that checks whether the targeted experimental routes now line up with the current source-owned agent, eval, memo, and skill surfaces.

## Boundary

- This report does not promote any draft eval.
- This report does not claim production readiness for long-horizon or witness-facing routes.
- This report does not open a new ToS wave.
- This report stays inside AoA-only integration closure.

## Pilot: AOA-P-0008 long-horizon-model-tier-orchestra

### Artifact drift

- No blocking artifact drift found.
- `route_decision`, `bounded_plan`, `verification_result`, `transition_decision`, and `distillation_pack` all resolve against current model-tier artifact contracts in `aoa-agents/generated/model_tier_registry.json`.
- `work_result` and `deep_synthesis_note` remain tier-local outputs and are intentionally not required by this playbook's expected-artifact surface.

### Anchor drift

- No blocking anchor drift found.
- `aoa-long-horizon-depth` resolves in `aoa-evals`, remains `draft`, and is explicitly treated as `review-only`.
- `aoa-tool-trajectory-discipline` resolves in `aoa-evals` as the first non-draft operational anchor on this route.

### Recall-rights drift

- No blocking recall-rights drift found.
- `memory-keeper` can read `core`, `warm`, `cool`, and `cold`, can write `warm`, `cool`, and `cold`, and allows recall scopes `repo`, `project`, and `ecosystem`.
- `architect`, `coder`, and `reviewer` all retain bounded read posture that is sufficient for route, plan, verify, and handoff behavior.
- Freeze finalization is still not delegated to any active role. That is a caution, not a blocker.

### Lineage drift

- No blocking lineage drift found.
- The exact required skills named in the playbook body are all `published` and `governance_and_eval_ready` in `aoa-skills/generated/governance_backlog.json`:
  - `aoa-change-protocol`
  - `aoa-source-of-truth-check`
  - `aoa-dry-run-first`
  - `aoa-bounded-context-map`

## Pilot: AOA-P-0007 witness-to-compost-pilot

### Artifact drift

- No blocking artifact drift found.
- The route remains playbook-owned and intentionally keeps `principle_candidate` and `canon_bundle` optional.
- The route leaves a reviewable witness surface before any deeper promotion step.

### Anchor drift

- No blocking anchor drift found.
- `aoa-witness-trace-integrity` resolves in `aoa-evals`, remains `draft`, and is explicitly `review-only`.
- `aoa-compost-provenance-preservation` resolves in `aoa-evals`, remains `draft`, and is explicitly `review-only`.

### Recall-rights drift

- No blocking recall-rights drift found.
- The router-facing semantic recall contract in `aoa-memo/examples/recall_contract.router.semantic.json` allows `repo`, `project`, and `ecosystem`.
- `memory-keeper` remains the only active role with deep enough write posture to carry the surviving witness route into memo-facing objects without widening the role contract.
- Freeze finalization remains outside the active role set. That keeps this route pilot-safe.

### Lineage drift

- No blocking lineage drift found.
- The exact required skills named in the playbook body are `published` and `governance_and_eval_ready`:
  - `aoa-source-of-truth-check`
  - `aoa-change-protocol`

## Pilot: AOA-P-0009 restartable-inquiry-loop

### Artifact drift

- No blocking artifact drift found.
- `inquiry_checkpoint`, `decision_ledger`, `contradiction_map`, `memory_delta`, `canon_delta`, and `next_pass_brief` remain explicit route artifacts rather than hidden context assumptions.
- The route keeps `memory_delta` distinct from `canon_delta`, which preserves the memo-versus-canon boundary.

### Anchor drift

- No blocking anchor drift found.
- `aoa-long-horizon-depth` resolves and remains explicitly `draft` and `review-only`.

### Recall-rights drift

- No blocking recall-rights drift found.
- `memory-keeper` retains the broadest recall/write posture for checkpoint survival.
- `reviewer` and `evaluator` retain bounded-recall posture that is sufficient for contradiction and relaunch review.

### Lineage drift

- No blocking lineage drift found.
- The exact required skills named in the playbook body are `published` and `governance_and_eval_ready`:
  - `aoa-source-of-truth-check`
  - `aoa-change-protocol`
  - `aoa-dry-run-first`
  - `aoa-bounded-context-map`

## Pilot: AOA-P-0010 cross-repo-boundary-rollout

### Anchor drift

- No blocking anchor drift found.
- `aoa-approval-boundary-adherence` resolves in `aoa-evals` as a bounded approval surface.
- `aoa-scope-drift-detection` resolves in `aoa-evals` as a bounded scope-control surface.

### Memo-contract drift

- No blocking memo-contract drift found.
- `examples/checkpoint_to_memory_contract.example.json` resolves in `aoa-memo` and supports `decision` and `audit_event` targets through its current mapping rules.
- `examples/provenance_thread.example.json` resolves in `aoa-memo` and keeps the route history aligned to `provenance_thread` rather than hidden state.

### Lineage drift

- No blocking lineage drift found.
- The exact required skills named in the playbook body are `published` and `governance_and_eval_ready`:
  - `aoa-source-of-truth-check`
  - `aoa-bounded-context-map`
  - `aoa-approval-gate-check`
  - `aoa-dry-run-first`
  - `aoa-change-protocol`

## Mismatch Registry

### Blocking mismatches

- none

### Non-blocking cautions

- Draft anchors remain draft. This wave makes them validator-checkable, not production-ready.
- Memory writeback is now machine-readable, but freeze finalization still remains outside the active role surface.
- `aoa-adr-write` and `aoa-sanitized-share` now have published lineage, but their upstream mappings are still nearest-fit rather than perfect one-to-one technique matches.
- Federation closure for this wave remains read-only against neighboring repositories. It checks current source surfaces; it does not mutate or promote them.

## Result

The targeted long-horizon, witness-facing, and cross-repo seams are now pilot-safe, validator-checkable, and free of current blocking drift across anchors, recall rights, memo contracts, and skill lineage for the current cohort.
The compiled activation collection at `generated/playbook_activation_surfaces.min.json` now mirrors the current activation fixtures and is checked by both the generator check and the playbook validator.
The compiled federation collection at `generated/playbook_federation_surfaces.min.json` now mirrors the current federation-checked cohort and is validated against `aoa-skills` and `aoa-memo`.
