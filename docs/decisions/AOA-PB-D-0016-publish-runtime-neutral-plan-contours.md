# Publish Runtime-Neutral Plan Contours

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0016
- Original date: 2026-07-26
- Surface classes: mechanic part, generated/readout, config/source, schema/example, validation guard, decision record
- Playbook routes: bounded-change-safe, a2a-summon-return-checkpoint, runtime-chaos-recovery
- Mechanic parents: scenario-composition
- Guard families: playbook source boundary, generated/read-model, validation guard, runtime seam, sibling-owner boundary
- Posture: accepted runtime-neutral plan-contour ABI

## Context

The `aoa-sdk` control plane needs to compile a reviewed route decision and
scenario binding into a deterministic typed plan. Authored playbooks already
own recurring scenario meaning, but their Markdown prose is neither a stable
machine ABI nor an appropriate runtime parser input. Repeating step meaning
inside the SDK would create a second playbook authority and make drift
invisible.

The existing activation and composition projections describe discoverability,
handoffs, failure posture, and adjuncts. They intentionally do not carry the
typed step/evidence structure needed by a compiler.

## Options Considered

- Parse `PLAYBOOK.md` prose inside `aoa-sdk`.
- Hardcode the three golden scenario plans inside `aoa-sdk`.
- Add command-bearing execution packets to activation or composition outputs.
- Publish a separate, closed, runtime-neutral plan-contour ABI owned by
  `aoa-playbooks`.

## Decision

Publish `aoa_playbook_plan_contour_v1` as a new `plan-contours` part of the
local scenario-composition mechanic.

The initial source declares exactly three golden contours:

- `AOA-P-0011 bounded-change-safe`
- `AOA-P-0031 a2a-summon-return-checkpoint`
- `AOA-P-0032 runtime-chaos-recovery`

Each contour must match the source playbook's ID, name, scenario, agents,
required skills, eval anchors, and expected artifacts. Every retention input
must come from the source playbook's declared memo contract references. The
generator validates an ordered DAG, an exact partition between reviewed
scenario-input artifacts and step-produced artifacts, evidence coverage,
owner-qualified eval/memo references, checkpoint/rollback bindings, reviewed
boolean branch guards, and a closed public JSON schema.

An expected artifact that already exists before compilation remains a typed
scenario input and must never be reclassified as a step output. A conditional
step and its conditional requirements carry one owner-declared
`guard_condition_id`. The downstream compiler must bind every declared
condition to a reviewed boolean with provenance, prune false guarded steps and
their requirements, and reject missing, extra, or unreviewed condition
bindings. It must not infer a condition from artifact presence or fabricate an
optional artifact to satisfy the unpruned contour.

Typed scenario inputs use `selected_scenario_inputs`; the SDK must bind each
declared artifact kind exactly once to an owner-qualified provenance reference
and select the exact step subset by kind. `all_scenario_inputs` is reserved for
generic request context in contours without typed input artifacts. Positional
matching or copying an undifferentiated reference tuple cannot satisfy a typed
input binding.

The contour may expose abstract operation/effect classes and binding modes. It
must reject commands, prompts, tools, arguments, MCP, transport, models,
scripts, shell, mutable runtime state, and verdict meaning at any depth.

`aoa-sdk` may consume only a pinned generated projection and its schema. It
must not parse playbook prose or supply hardcoded replacement meaning when the
projection is missing, stale, or incompatible.

The generated projection and schema are subjects of
`docs/artifact-bundles/playbook_registry.bundle.json`. Registry/latest
consumers must pass the bundle trust gate and use the materialized subject
store instead of treating working-tree presence as admission.

## Rationale

The separate ABI keeps scenario meaning with the playbook owner while giving a
control plane deterministic structured input. Runtime neutrality prevents an
owner projection from becoming a hidden runner or transport contract. Exact
frontmatter, artifact-role, and branch alignment makes source drift fail
visibly rather than silently changing downstream plans.

This boundary also creates a stable point for measuring compilation and
execution costs later: the contour identifies intended structure, while SDK
snapshots and runtime receipts can prove what was bound and executed.

## Consequences

- Positive: `aoa-sdk` can compile without prose parsing or duplicate scenario
  definitions.
- Positive: playbook changes fail the owner generator when a contour becomes
  stale.
- Positive: the ABI is small enough to pin, hash, review, and cache.
- Positive: reviewed input artifacts cannot be accepted as newly emitted
  runtime outputs.
- Positive: optional preview, eval, memo, regrounding, and proof-handoff paths
  remain explicit without becoming mandatory runtime theater.
- Positive: the contour and schema travel through the existing fail-closed
  artifact admission and materialization path.
- Positive: commands and runtime bindings remain downstream owner concerns.
- Tradeoff: adding another compiled scenario requires an explicit owner config
  and validation change before SDK support.
- Tradeoff: a green projection proves alignment and shape, not invocation,
  execution, usefulness, or cost reduction.

## Current Applicability

As of 2026-07-26:

- Valid: the ABI is limited to the three named golden scenarios.
- Valid: the generated output is a derived read model, not authored playbook
  truth or a runnable plan.
- Valid: `aoa-sdk` compilation and runtime execution remain separate
  downstream work.
- Superseded by: none.

## Review Log

### 2026-07-26 - C2 owner ABI

- Previous assumption: a downstream compiler could reconstruct enough plan
  meaning from existing discovery and composition projections.
- New reality: deterministic compilation needs a typed scenario-owned contour
  that is stricter and narrower than an execution packet.
- Reason: prevent prose parsing, duplicated playbook authority, and hidden
  execution semantics while enabling an Agent OS control plane.
- Source surfaces updated: scenario-composition part, generated owner
  projection, execution seam, release validation, tests, and decision indexes.
- Validation: focused generator parity, package validator, owner tests, nested
  agent validation, KAG rebuild, and repository release gate.

### 2026-07-26 - Reviewed inputs and conditional paths

- Previous assumption: exact coverage of frontmatter artifacts by step outputs
  was sufficient, and optional scenario prose could remain a linear DAG.
- New reality: reviewed `child_task_result` and `owner_runtime_receipt`
  artifacts are compiler inputs, while optional preview, eval, memo,
  regrounding, and proof-handoff paths need explicit reviewed guards.
- Reason: otherwise a compiler could accept a newly emitted artifact in place
  of reviewed source evidence or force a branch by fabricating an optional
  output.
- Source surfaces updated: plan-contour config, schema, generator, generated
  projection, contract docs, tests, and decision indexes.
- Validation: focused role-partition and guard negative tests, generated
  parity, package validation, KAG rebuild, and repository release gate.

### 2026-07-26 - Kind-selected input provenance

- Previous assumption: `all_scenario_inputs` plus a list of artifact kinds was
  enough for a compiler to identify reviewed input references.
- New reality: a generic reference tuple cannot prove which reference carries
  each artifact kind, while a contour with only generic request context still
  needs direct provenance validation.
- Reason: compilation must select typed inputs by kind without positional
  guessing, and output-producing steps must not lose generic request context
  merely because the contour has no typed input artifact partition.
- Source surfaces updated: plan-contour config, schema, generator, generated
  projection, contract docs, tests, and decision indexes.
- Validation: focused kind-selection and generic-provenance negative tests,
  generated parity, package validation, KAG rebuild, and repository release
  gate.

## Boundaries

- This decision does not authorize runtime execution, agent spawning, external
  effects, or retries.
- It does not move routing, agent, skill, eval, memo, or runtime ownership into
  `aoa-playbooks`.
- It does not prove the future SDK compiler, runner, agent-in-loop trial, or
  cost-reduction claim.
- It does not expand the initial ABI beyond the three named scenarios.

## Source Surfaces

- `mechanics/scenario-composition/parts/plan-contours/config/playbook_plan_contours.json`
- `mechanics/scenario-composition/parts/plan-contours/schemas/playbook-plan-contours.schema.json`
- `mechanics/scenario-composition/parts/plan-contours/scripts/generate_playbook_plan_contours.py`
- `mechanics/scenario-composition/parts/plan-contours/docs/playbook-plan-contour-contract.md`
- `generated/playbook_plan_contours.min.json`
- `docs/artifact-bundles/playbook_registry.bundle.json`
- `tests/test_generate_playbook_plan_contours.py`

## Follow-Up Route

Pin the merged owner revision and artifact digests in `aoa-sdk`, then implement
the deterministic `ScenarioBinding -> RunPlan` compiler and three golden
fixtures. Keep runner execution and agent-in-loop trials as later, separately
proven stages.

## Verification

Verification is owned by the plan-contour generator check, scenario-composition
package validator, JSON Schema and semantic negative tests, decision-index
generator, nested-agent validator, KAG parity, and repository release gate.
