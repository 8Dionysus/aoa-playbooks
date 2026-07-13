# Move Agon Payloads Into Mechanics Package

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0012
- Original date: 2026-05-31
- Surface classes: mechanic package, mechanic part, docs route, schema/example, generated/readout, validation guard, legacy/provenance, recurrence manifest, decision record
- Playbook routes: agon-broken-trace-trial, agon-fallback-honor-trial, agon-contradiction-endurance-trial, agon-costly-closure-trial, agon-assistant-escalation-trial, agon-prediction-trial, agon-expensive-summon-intent-trial
- Mechanic parents: agon
- Guard families: package route, source topology, legacy/provenance, validation guard, generated/read-model, recurrence boundary, sibling-owner boundary, playbook source boundary
- Posture: accepted agon package

## Context

Agon pressure was the largest mechanics-shaped payload in `aoa-playbooks`.
It included trial doctrine, trial-kernel bindings, campaign choreography,
adoption examples, recurrence adapter notes, seed config, schemas, examples,
generated registries, builders, validators, source playbooks, quests, and
recurrence manifests.

Leaving all Agon doctrine and schemas at root made the active route ambiguous:
root `docs/`, `config/`, `schemas/`, and `examples/` looked like independent
source homes even though the repeatable operation was one head-fed mechanic.

## Options Considered

1. Leave Agon payloads scattered across root `docs/`, `config/`, `schemas/`,
   `examples/`, and `scripts/`.
2. Move the source `playbooks/agon/*/agon-*/PLAYBOOK.md` bundles into mechanics.
3. Move Agon mechanics-owned docs, seed config, schemas, examples, and builder
   implementations into `mechanics/agon/parts/`, keep source playbooks, quests,
   generated registries, recurrence manifests, and root commands in their
   owner paths, and add package validation.

## Decision

Choose option 3.

Create `mechanics/agon/` with:

- package `AGENTS.md`, `README.md`, `PARTS.md`, and `PROVENANCE.md`;
- parts for trial playbooks, trial-kernel bindings, campaign playbooks,
  adoption, and recurrence adapter;
- package-local docs, seed config, schemas, examples, and builder
  implementations;
- package-local `legacy/` index and distillation log for former root paths;
- `mechanics/agon/scripts/validate_agon_package.py`;
- root `scripts/*agon*.py` compatibility wrappers for public command paths.

## Rationale

This follows the source-derived agent design rule: make the operational map
simple, composable, and explicit.

Agon has separate resources, tools, generated read models, source playbooks,
quests, and recurrence manifests. The package route makes those owners visible:
mechanics owns the repeatable choreography payloads and builder
implementations; `playbooks/` owns authored scenario canon; `generated/` owns
public read models; recurrence manifests stay in the recurrence district.

## Consequences

- Positive: `agon` is now a package-active head-fed mechanic in
  `aoa-playbooks`.
- Positive: former root Agon docs/config/schemas/examples are package-local
  and recorded through package provenance and legacy index.
- Positive: root Agon command paths remain stable compatibility wrappers.
- Positive: package validation now checks examples, root wrappers, generated
  builder/validator commands, retained source playbooks, retained quests, and
  retained recurrence manifests.
- Tradeoff: public docs/schema/example paths changed from root to package
  routes.
- Follow-up: continue the placement audit for recurrence/checkpoint,
  Experience, release-support, questbook, Titan, and portfolio-governance rows.

## Current Applicability

As of 2026-05-31:

- Still valid: `mechanics/agon/` owns playbook-local Agon choreography payloads.
- Changed: `mechanics/HEAD_MECHANICS.md` marks `agon` as `package-active`.
- Superseded by: none.

## Review Log

### 2026-05-31 - Agon package landing

- Previous assumption: Agon was the largest pending package candidate after
  smaller wrapper/provenance packages proved the route.
- New reality: Agon has package cards, part map, provenance bridge, moved
  docs/config/schemas/examples/builder implementations, compatibility wrappers,
  package validator, focused tests, and release-check wiring.
- Reason: trial, kernel-binding, campaign, adoption, and recurrence-adapter
  payloads form one repeated playbook-layer mechanic with clear stronger-owner
  boundaries.
- Source surfaces updated: `mechanics/agon/`, root Agon wrappers, Agon
  recurrence manifests, generated readout guidance, `README.md`,
  `docs/README.md`, `ROADMAP.md`, `scripts/release_check.py`, and focused
  tests.
- Validation: the owning executable validator, generated-freshness checks, relevant tests, and repository release gate.

## Boundaries

- This decision does not move authored Agon playbook canon out of
  `playbooks/`.
- This decision does not move quest source notes out of `quests/`.
- This decision does not move root generated Agon registries.
- This decision does not move recurrence manifests out of
  `manifests/recurrence/`.
- This decision does not claim live arena protocol authority, proof verdicts,
  scar writes, rank/trust mutation, memory truth, route dispatch, role
  authority, or runtime execution.
- This decision does not create a root `legacy/` directory.

## Source Surfaces

- `mechanics/agon/AGENTS.md`
- `mechanics/agon/README.md`
- `mechanics/agon/PARTS.md`
- `mechanics/agon/PROVENANCE.md`
- `mechanics/agon/parts/trial-playbooks/`
- `mechanics/agon/parts/trial-kernel-bindings/`
- `mechanics/agon/parts/campaign-playbooks/`
- `mechanics/agon/parts/adoption/`
- `mechanics/agon/parts/recurrence-adapter/`
- `mechanics/agon/scripts/validate_agon_package.py`
- root compatibility wrappers under `scripts/*agon*.py`
- `generated/agon_trial_playbook_registry.min.json`
- `generated/agon_trial_kernel_binding_registry.min.json`
- `generated/agon_campaign_playbook_registry.min.json`
- `mechanics/agon/parts/*/manifests/component.agon*.json`
- `playbooks/agon/*/agon-*/PLAYBOOK.md`
- `quests/AOP-Q-AGON-*.md`
- `tests/test_agon_mechanics_package.py`
- `tests/test_agon_trial_playbooks.py`
- `tests/test_agon_trial_kernel_bindings.py`
- `tests/test_agon_campaign_playbook_registry.py`

## Follow-Up Route

Continue with the placement audit row-by-row. Do not move root directories by
name. Move only mechanics-owned payloads whose source owner, generated owner,
or root exception is explicit.

## Verification

Verification is owned by the corresponding executable validators and the repository release gate; focused invocation lives in the nearest `AGENTS.md`.
