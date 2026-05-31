# Mechanics Placement Audit

Status: `active-audit`.

This audit is the control surface for moving mechanics-owned payloads out of
flat root districts and into package routes.

It is not proof that every payload has already moved. It records the current
owner decision for each mechanics-related payload family so later package
landings can move only the files whose active owner is ready.

## Operating Card

| Field | Route |
| --- | --- |
| role | placement matrix for mechanics-related payloads |
| input | root/docs/config/schemas/examples/generated/scripts/tests/manifests payloads with mechanics pressure |
| output | move target, package-local reason, legacy-name posture, consumer risk, validation hook, or stronger-owner handoff |
| owner | `mechanics/PLACEMENT_AUDIT.md` for cross-package placement status; package `PROVENANCE.md` for concrete moved-path accounting |
| next route | target package package-card, `PARTS.md`, package validator, then package-local `legacy/` only after payload movement |
| validation | `python scripts/validate_mechanics_skeleton.py`, package validator, source builder `--check`, and `python scripts/validate_playbooks.py` |

## Audit Rules

- Source-authored playbooks stay under `playbooks/*/PLAYBOOK.md`.
- Root public entrypoints, generated read models, authored playbooks, quest
  sources, decisions, sentinels, and compatibility command wrappers stay at
  root only when they are the active root contract.
- A moved payload needs an active package route, part map, owner split,
  validator coverage, and provenance bridge.
- Former root names are historical or accepted-input names, not active routes.
- No repository-root `legacy/` is allowed for mechanics accounting.

## Placement Matrix

| Payload family | Current paths | Active owner decision | Target route | Legacy-name posture | Consumer risk | Validation hook | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mechanics skeleton | `mechanics/README.md`, `mechanics/AGENTS.md`, `mechanics/HEAD_MECHANICS.md`, `mechanics/LOCAL_MECHANICS.md`, `mechanics/PACKAGE_TEMPLATE.md` | already mechanics-owned | `mechanics/` root atlas | `active` | low | `scripts/validate_mechanics_skeleton.py`, `tests/test_mechanics_skeleton.py` | landed |
| legacy naming posture | `mechanics/LEGACY_NAMING.md` | mechanics-owned control surface | `mechanics/LEGACY_NAMING.md` | `active` | low | `scripts/validate_mechanics_skeleton.py` | landed |
| placement audit | `mechanics/PLACEMENT_AUDIT.md` | mechanics-owned control surface | `mechanics/PLACEMENT_AUDIT.md` | `active` | low | `scripts/validate_mechanics_skeleton.py` | landed |
| authored playbook canon | `playbooks/*/PLAYBOOK.md`, `playbooks/AGENTS.md` | source playbook owner, not mechanics | keep `playbooks/` | `active`, `root-public` | high if moved | `scripts/validate_playbooks.py` | retained |
| playbook registry | `generated/playbook_registry.min.json` | source-authored compact metadata | keep root `generated/` | `root-public` | high if moved | `scripts/validate_playbooks.py` | retained |
| activation seam docs and builder | `mechanics/activation/parts/activation-surface/docs/`, `mechanics/activation/parts/activation-surface/schemas/playbook-activation-surface.schema.json`, `mechanics/activation/parts/activation-surface/examples/playbook_activation.*.example.json`, package implementation `mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py`, root wrapper `scripts/generate_playbook_activation_surfaces.py`, `generated/playbook_activation_surfaces.min.json` | local mechanic pressure; activation source payloads are package-local | `mechanics/activation/` owns docs/schema/examples/builder; root `generated/` and `scripts/` remain public readout/compat planes | `active`, `accepted-input`, `root-public` | high: generated refs and tests cite activation output/examples | `mechanics/activation/scripts/validate_activation_package.py`, activation builder `--check`, `validate_playbooks.py`, downstream feed tests | package-active |
| federation closure | `mechanics/federation-closure/parts/federation-surfaces/schemas/playbook-federation-surface.schema.json`, package implementation `mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py`, root wrapper `scripts/generate_playbook_federation_surfaces.py`, `generated/playbook_federation_surfaces.min.json`, federation refs in activation seam | local mechanic pressure with sibling-owner closure | `mechanics/federation-closure/` owns schema/builder; root `generated/` and `scripts/` remain public readout/compat planes | `active`, `root-public`, `stronger-owner` | high: sibling closure and public generated path | `mechanics/federation-closure/scripts/validate_federation_closure_package.py`, federation builder `--check`, `validate_playbooks.py` | package-active |
| review gate and alpha readiness | review schemas under `mechanics/review-gate/parts/*/schemas/`, package implementations under `mechanics/review-gate/parts/*/scripts/`, real-run evidence under `mechanics/real-run-harvest/parts/**`, root wrappers `scripts/generate_playbook_review_*.py` / `scripts/generate_phase_alpha_surfaces.py`, `generated/playbook_review_*.json`, `generated/playbook_landing_governance.min.json`, `generated/phase_alpha_*.json` | local mechanic pressure; evidence/source stores are package-local under real-run-harvest | `mechanics/review-gate/` owns review packet/readout builders; `mechanics/real-run-harvest/` owns harvest/evidence payloads; root `generated/`/`scripts/` stay public readout/compat planes | `active`, `accepted-input`, `root-public` | high: generated source refs and public readouts | `mechanics/review-gate/scripts/validate_review_gate_package.py`, `mechanics/real-run-harvest/scripts/validate_real_run_harvest_package.py`, review builders `--check`, phase-alpha builder `--check`, `validate_playbooks.py` | package-active |
| scenario composition | `mechanics/scenario-composition/parts/composition-surfaces/docs/`, `config/playbook_composition_overrides.json` inside the composition part, package examples/manifests, package implementation `mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py`, root wrapper `scripts/generate_playbook_composition_surfaces.py`, root generated composition outputs | local mechanic pressure with package-local source config and public generated outputs | `mechanics/scenario-composition/` owns docs/config/examples/manifests/builder; root `generated/` and `scripts/` remain public readout/compat planes | `active`, `accepted-input`, `root-public` | high: downstream readers cite generated output paths | `mechanics/scenario-composition/scripts/validate_scenario_composition_package.py`, composition builder `--check`, composition tests, `validate_playbooks.py` | package-active |
| portfolio governance | `mechanics/portfolio-governance/parts/model-spine/docs/playbook-model.md`, `mechanics/portfolio-governance/parts/operational-family/docs/playbook-operational-family.md`, `mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-lifecycle.md`, `mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-portfolio.md`, `mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-gap-matrix.md`, package route `mechanics/portfolio-governance/` | local portfolio mechanic with package-local docs | `mechanics/portfolio-governance/` owns model/lifecycle/portfolio docs and coherence posture | `active`, `accepted-input`, `package-local` | medium: README/docs links cite these paths | `mechanics/portfolio-governance/scripts/validate_portfolio_governance_package.py`, root design validator, docs link audit, `validate_playbooks.py` | package-active |
| Agon trial and campaign package | package payloads under `mechanics/agon/parts/{trial-playbooks,trial-kernel-bindings,campaign-playbooks,adoption,recurrence-adapter}/`; package recurrence manifests, root generated registries, root compatibility wrappers, source playbooks, and quests | head-fed mechanic with strong local payload; playbooks/quests stay source owners and generated readouts stay root | `mechanics/agon/` package owns docs, seed config, schemas, examples, recurrence manifests, builder implementations, provenance, legacy-name accounting, and package validator | `historical`, `accepted-input`, `generated-projection`, `root-public`, `source-playbook` | high: many public paths and package manifests | `mechanics/agon/scripts/validate_agon_package.py`, Agon root wrappers, Agon tests, recurrence manifest checks, `validate_playbooks.py` | package-active |
| antifragility stress lanes | package payloads under `mechanics/antifragility/parts/stress-lanes/`, `parts/reentry-gates/`, `parts/stress-harvest/`, `parts/runtime-chaos-wave1/`, and `parts/via-negativa/`; former root docs/schemas/examples recorded in package provenance; `playbooks/runtime-chaos-recovery/PLAYBOOK.md` stays source canon | head-fed/local stress mechanic; runtime-chaos playbook stays source canon | `mechanics/antifragility/` owns docs, schemas, examples, and validator; `playbooks/` owns runtime-chaos playbook canon | `historical`, `accepted-input`, `package-local`, `source-playbook` | medium: package paths replace former public schema/example refs | `mechanics/antifragility/scripts/validate_antifragility_package.py`, antifragility tests, runtime-chaos tests, `validate_playbooks.py` | package-active |
| recurrence and checkpoint return posture | recurrence docs under `mechanics/recurrence/parts/**/docs/`, recurrence manifests under owning mechanics packages, checkpoint doc under `mechanics/checkpoint/parts/distillation-closed-loop/docs/checkpoint-distillation-closed-loop-pilot.md`, source playbooks under `playbooks/` | mixed head-fed/local return pressure; source playbooks stay in `playbooks/`, recurrence/checkpoint mechanics own their package payloads | package-local route packages with stronger-owner memo checkpoint handoff | `accepted-input`, `package-local`, `source-playbook`, `stronger-owner` | high: manifests and playbook validation | `mechanics/recurrence/scripts/validate_recurrence_package.py`, `mechanics/checkpoint/scripts/validate_checkpoint_package.py`, `validate_playbooks.py`, focused playbook tests | package-active |
| Experience adoption and service posture | Experience docs/schemas/examples under `mechanics/experience/parts/**`, transferred Agonic adoption pair under `mechanics/agon/parts/adoption/`, package `mechanics/experience/` | head-fed Experience mechanic pressure; Experience contract pairs are package-local; Agonic adoption belongs to Agon | package-local Experience route package plus Agon transferred-path validation | `accepted-input`, `package-local`, `stronger-owner`, `transferred-to-agon` | medium: many former root docs/schemas/examples moved | `mechanics/experience/scripts/validate_experience_package.py`, Experience tests, `validate_playbooks.py` | package-active |
| release support | `docs/RELEASING.md`, `mechanics/release-support/parts/promotion-and-retention/docs/first-release-runbook.md`, `mechanics/release-support/parts/promotion-and-retention/docs/release-candidate-promotion.md`, rollback/deployment/installation schemas/examples, `scripts/release_check.py`, package `mechanics/release-support/` | release mechanic pressure; root release check and release docs stay operator-facing | package-local release-support route package | `active`, `accepted-input`, `root-public` | high: release scripts and docs are operator-facing | `mechanics/release-support/scripts/validate_release_support_package.py`, `scripts/release_check.py`, release/rollback tests | package-active |
| questbook, campaign adjuncts, and RPG reflection | `QUESTBOOK.md`, `quests/`, `generated/quest_*.json`, questbook docs/schemas/examples under `mechanics/questbook/parts/**`, RPG docs/schema under `mechanics/rpg/parts/**`, packages `mechanics/questbook/` and `mechanics/rpg/` | root quest source store and generated readers remain root-published; mechanic docs/schemas/examples are package-local; RPG vocabulary stays reflection-only | package-local questbook and RPG route packages | `root-public`, `accepted-input`, `generated-projection`, `package-local` | high if source store moves | `mechanics/questbook/scripts/validate_questbook_package.py`, `mechanics/rpg/scripts/validate_rpg_package.py`, questbook validation in `validate_playbooks.py` | package-active |
| Titan route ecology | Titan docs under `mechanics/titan/parts/**/docs/`, package `mechanics/titan/` | local playbook pressure with stronger role/runtime/memo/proof owners; Titan route docs are package-local | package-local Titan route package; no role authority | `stronger-owner`, `accepted-input`, `package-local` | medium: sibling owner ambiguity | `mechanics/titan/scripts/validate_titan_package.py`, titan playbook tests, route audit | package-active |
| root decisions | `docs/decisions/` and generated indexes | decision owner, not mechanic package payload | keep `docs/decisions/` | `active`, `root-public` | high if moved | `generate_decision_indexes.py --check` | retained |

## Package Order Note

The wrapper and provenance pattern landed first in smaller local packages, then
expanded to the larger `agon` package. Remaining rows should follow the same
source-owner audit instead of moving files by root directory alone.

## Intentional Root Retentions

These are not missed moves:

- `playbooks/*/PLAYBOOK.md`: source-authored scenario canon.
- `generated/playbook_registry.min.json`: source-authored compact registry.
- root generated read models consumed by downstream readers.
- `QUESTBOOK.md`, `quests/`, and `generated/quest_*`: root source-store and
  public readout route.
- `docs/decisions/`: durable decision rationale.
- root command wrappers when operator-facing command paths are public
  compatibility.

## Completion Test

The mechanics refactor is complete only when every row above is either:

- `moved` with package `PROVENANCE.md`, package/part validator, and former-path
  accounting; or
- `kept-at-root` with an explicit root/playbooks/public/generated/source-store
  reason and validator coverage.
