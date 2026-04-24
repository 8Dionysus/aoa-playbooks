# Changelog

All notable changes to `aoa-playbooks` will be documented in this file.

The format is intentionally simple and human-first.
Tracking starts with the community-docs baseline for this repository.

## [Unreleased]

## [0.3.3] - 2026-04-23

### Summary

- this patch expands reviewed playbook continuity across release-wave,
  workspace closeout, eval closeout, owner follow-through, Agon trial,
  recurrence, mechanical-kernel, schools/lineages/campaigns, Titan, and
  Experience follow-through routes
- Titan live-session drills, Experience closed-loop pilot, certification
  forge, adoption, rollback, retention, governance, sovereign-office,
  service-mesh incident response, and wave5 repair closeout follow-through are
  added or tightened
- `aoa-playbooks` remains the scenario-composition and reviewed-evidence layer
  rather than a runtime ledger, source-of-truth owner, or automation scheduler

### Added

- reviewed workspace/release/eval closeout continuity surfaces,
  closeout-owner follow-through records, real-run notes, and owner adoption
  quest playbooks
- Agon Wave VI trial playbooks, recurrence trial-playbook manifests,
  Wave XIII trial-kernel bindings, mechanical-trial rehearsal boundaries,
  schools/lineages/campaign playbooks, and seed-wave closeout follow-through
- Titan playbooks and live-session drill route plus Experience closed-loop
  pilot, certification forge, adoption, rollback, retention, governance,
  first-release, installation, office bootstrap, service mesh incident
  response, sovereign-office, and repair closeout follow-through surfaces

### Changed

- reviewed-run ordering, Agon and playbook contract follow-ups, recurrence
  observation boundaries, wave2/wave3 schema and contract guards, Titan drill
  review posture, gate-review posture, and closeout-owner continuity were
  tightened

### Validation

- `python scripts/release_check.py`

### Notes

- this patch grows scenario composition and reviewed continuity evidence only;
  source repos, runtime, memory, routing, and eval layers keep their own
  authority

## [0.3.2] - 2026-04-19

### Summary

- this patch adds runtime chaos recovery, A2A summon return, and live Codex
  repair closeout playbooks to the reviewed rollout lane
- closeout continuity, recurrence beacons, and release-audit pins are
  tightened around current owner-routed playbook evidence
- `aoa-playbooks` remains the scenario-composition and review layer

### Added

- a runtime chaos recovery playbook, an A2A summon return checkpoint playbook,
  and live Codex repair closeout run capture
- recurrence beacons with hook bindings and reviewed closeout follow-through
  seed examples

### Changed

- aoa-kag closeout continuity carry, Wave5 survivor routing,
  roadmap/current-direction docs, and CI/protection surfaces are aligned with
  the current playbook contour

### Validation

- `python scripts/release_check.py`

### Notes

- this patch grows reviewed scenario composition and closeout evidence without
  changing routing or runtime ownership boundaries

## [0.3.1] - 2026-04-12

### Summary

- this patch advances the trusted-rollout line with the reviewed hold track,
  rollout cadence adjunct, and self-agency continuity playbook
- release-audit pins and reviewed-case counting are tightened around the
  current evidence path
- `aoa-playbooks` remains the scenario-composition and review layer

### Added

- the reviewed rollout hold track for `AOA-P-0028`, a trusted rollout campaign
  cadence adjunct, and a self-agency continuity playbook.

### Changed

- release-audit dependency pins and reviewed-case counting are refreshed for
  the current rollout evidence path.

### Validation

- `python scripts/release_check.py`

### Notes

- detailed trusted-rollout hold-track, rollout-cadence adjunct, and continuity playbook changes for this patch remain enumerated below under `Added` and `Changed`

## [0.3.0] - 2026-04-10

### Summary

- this release adds owner-first capability review tracks, live-publisher activation evidence, checkpoint-growth playbook surfaces, and stress/via-negativa adjuncts
- review-status contracts, evidence posture, and canary/remediation guidance are hardened around the current reviewed-run contour
- `aoa-playbooks` remains the scenario-composition and review layer rather than a generic runtime logging surface

### Validation

- `python scripts/release_check.py`

### Notes

- detailed playbook, review-track, generated-surface, and operator-surface coverage for this release remains enumerated below under `Added`, `Changed`, and `Included in this release`

### Added

- owner-first capability review track, federated live-publisher activation
  evidence, split-wave reviewed runs, and labeled same-day reviewed summaries
- closeout owner follow-through and workspace checkpoint-growth playbook
  surfaces plus checkpoint closeout bridge install
- third-wave playbook stress surfaces and a via negativa checklist for the
  scenario-composition layer

### Changed

- hardened playbook review-status contracts, evidence posture, and live-gate
  alignment for owner-first reviewed runs
- refreshed compatibility-canary scheduling, remediation-gate notes, and
  questline posture docs around the current reviewed-run contour

### Included in this release

- authored playbook and review-track expansions across `playbooks/`, `docs/`,
  `generated/`, `schemas/`, `examples/`, and `config/`, including Phase Alpha
  readiness runs, owner-first capability landing and review flows,
  remediation-harvest surfaces, and RPG party-template adjuncts
- repo-local quest, follow-through, and operating surfaces under `.agents/`,
  `.github/`, `QUESTBOOK.md`, `quests/`, `AGENTS.md`, `README.md`, `scripts/`,
  and `tests/`, including live receipt publishing, project-foundation
  installs, checkpoint-closeout follow-through, and canary schedule updates

## [0.2.0] - 2026-04-01

Second public release of `aoa-playbooks`.

This changelog entry uses the release-prep merge date.

### Summary

- this release focuses on reviewability after the `v0.1.0` baseline by adding playbook review status, review packet contracts, and review intake surfaces
- the public playbook layer now ships stronger evidence-harvest and operator-audit support without collapsing back into raw runtime logging
- scenario composition stays bounded: the repo adds execution feed contracts and adjunct questline/campaign surfaces while preserving skill, memo, eval, and routing ownership boundaries

### Added

- questbook harvest and reanchor foundation from the first manual harvest pass
- questline and campaign adjunct surfaces
- playbook execution feed contracts for downstream consumers
- generated playbook review status surfaces
- generated playbook review packet contracts
- generated playbook review intake surfaces
- CI canary and validator-hardening coverage for the expanded review families

### Changed

- hardened review packet contracts for operator audit and review prep
- validated review-surface parity now sits beside the existing activation, federation, and composition checks

### Included in this release

- the authored playbook corpus under `playbooks/*/PLAYBOOK.md`
- generated review surfaces under `generated/playbook_review_status.min.json`, `generated/playbook_review_packet_contracts.min.json`, and `generated/playbook_review_intake.min.json`
- existing activation, federation, composition, handoff, failure-catalog, subagent-recipe, and automation-seed surfaces under `generated/`

### Validation

- `python scripts/generate_playbook_activation_surfaces.py --check`
- `python scripts/generate_playbook_federation_surfaces.py --check`
- `python scripts/generate_playbook_review_status.py --check`
- `python scripts/generate_playbook_composition_surfaces.py --check`
- `python scripts/validate_playbooks.py`
- `python -m unittest tests.test_validate_playbooks`

### Notes

- this release continues the evidence-led maturation path from `v0.1.0`; it does not claim that every playbook has equal real-run evidence

## [0.1.0] - 2026-03-28

First public baseline release of `aoa-playbooks` as the scenario and composition layer in the AoA public surface.

This changelog entry uses the release-prep merge date.

### Summary

- first public baseline release of `aoa-playbooks` as a bounded repository for scenario-level operating recipes, activation seams, federation seams, and playbook-owned composition surfaces
- current public posture is intentionally mixed rather than flattened:
  - `20` registry entries total
  - `15` authored `PLAYBOOK.md` bundles
  - `13` activation-readable playbooks
  - `15` federation-checked playbooks
  - `7` composition-managed playbooks
- release messaging remains intentionally modest:
  - `AOA-P-0017 split-wave-cross-repo-rollout` is the only operational route that has already landed a minimal composition-owned adjunct
  - `AOA-P-0019 release-migration-cutover` still remains on evidence hold
  - `AOA-P-0020 incident-recovery-routing` still remains on live-incident hold

### Added

- first public baseline release of `aoa-playbooks` as the canonical scenario and composition layer within AoA
- public bundle-contract, lifecycle, execution-seam, recurrence, portfolio, and gap-matrix doctrine under `docs/`
- repo-first real-run workflow and harvest doctrine under `docs/PLAYBOOK_REAL_RUN_WORKFLOW.md`, `docs/PLAYBOOK_REAL_RUN_HARVEST.md`, `docs/real-runs/`, and `docs/gate-reviews/`
- authored playbook corpus across checkpoint, witness/compost, long-horizon inquiry, cross-repo rollout, bounded change, infra guard, local diagnosis, remediation, cutover, incident-recovery, and ATM10 overlay scenarios
- generated activation, federation, and composition surfaces under `generated/`
- local validator and GitHub Actions repo validation path for authored bundles and derived surfaces
- bounded release guide under `docs/RELEASING.md`

### Changed

- the activation seam now carries explicit return posture plus bounded memo-read defaults for the runtime-facing cohort without moving recall ownership into `aoa-playbooks`
- the federation seam now validates exact skill and memo-contract closure against `aoa-skills` and `aoa-memo`
- `AOA-P-0017 split-wave-cross-repo-rollout` now has a minimal composition-owned handoff bridge derived from two reviewed real runs
- `AOA-P-0016 atm10-bounded-change` has returned to `A+Act+F+C` after `aoa-skills` published the downstream bridge signal `project_overlay_federation_ready`

### Included in this release

- `20` total registry rows in `generated/playbook_registry.min.json`
- `15` authored playbook bundles under `playbooks/*/PLAYBOOK.md`
- `13` activation example-backed runtime-readable entries in `generated/playbook_activation_surfaces.min.json`
- `15` federation-checked entries in `generated/playbook_federation_surfaces.min.json`
- `7` composition-managed playbooks in `generated/playbook_composition_manifest.json`
- the first reviewed real-run summaries under `docs/real-runs/` plus gate-review verdict surfaces for `AOA-P-0017`, `AOA-P-0019`, and `AOA-P-0020`

### Validation

- `python scripts/generate_playbook_activation_surfaces.py --check`
- `python scripts/generate_playbook_federation_surfaces.py --check`
- `python scripts/generate_playbook_composition_surfaces.py --check`
- `python scripts/validate_playbooks.py`

### Notes

- this is a repository release, not a claim that every current playbook is equally evidenced or equally mature
- `AOA-P-0019` and `AOA-P-0020` intentionally remain weaker than `AOA-P-0017` because their next moves depend on fresh real-world evidence rather than more repo-only elaboration
- package publishing, registry publishing, and per-playbook semantic versioning remain out of scope for `v0.1.0`
