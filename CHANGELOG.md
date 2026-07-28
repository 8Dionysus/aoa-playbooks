# Changelog

All notable changes to `aoa-playbooks` will be documented in this file.

The format is intentionally simple and human-first.
Tracking starts with the community-docs baseline for this repository.

## [Unreleased]

### Changed

- The repository now states an explicit MCP-first boundary for any future
  `aoa-playbooks` owner skill; no empty skill home is scaffolded in advance.
- Current navigation, dispatch, recurrence, portfolio, and Agon handoffs now
  route to the canonical `aoa-sdk` control plane. The Agon trial validator can
  compare its embedded vocabularies with explicit SDK and center roots while
  no active check requires an `aoa-routing` checkout.

### Removed

- Removed the copied shared `.agents/skills/` catalog and its obsolete
  documentation/test exceptions. Shared workflows remain owned by
  `aoa-skills` and are supplied outside this repository.

## [0.4.0] - 2026-07-13

### Summary

- This release makes the playbook layer structurally publishable: authored
  scenarios now have a checked convex source home, repeatable operation
  pressure lives in package-local mechanics, and root/design/route documents
  remain compact dispatch surfaces rather than duplicate inventories.
- Public handoffs now fail closed. The playbook registry carries an OS Abyss
  artifact identity and trust-gated bundle, local eval/KAG/stats/memo ports
  preserve stronger-owner boundaries, and the canonical seven-index KAG
  family is deterministic and squash-stable.
- The release was reconstructed from Git rather than from the prior
  `[Unreleased]` prose: all 45 first-parent commits from `v0.3.3` through
  `5d6551e` are accounted for below, spanning 901 changed paths and 48,368
  additions / 4,424 deletions. Only 7 of those 45 commits had touched this
  changelog before release preparation.

### Added

- Authored Titan closeout/audit and seed-pack publication-route playbooks,
  together with their registry, composition, documentation, reviewed
  closeout-follow-through evidence, and quest surfaces.
- District-local `AGENTS.md` guardrails plus a slim root route card backed by a
  preserved full reference surface.
- A portable checked `.agents/skills/` foundation, including session-growth,
  closeout, summon, diagnosis, repair, progression, route-fork, source-truth,
  safe-change, and related reusable workflow exports with review examples and
  GitHub landing support.
- A local `memo/` candidate/receipt/export port and reviewed-intake contract;
  playbook memory fields now consume reviewed `aoa-memo` objects through ids,
  provenance, lifecycle, and generated read models without claiming durable
  memory authority.
- Canonical decision ids and lookup indexes, the `DESIGN.md` system spine, and
  the `DESIGN.AGENTS.md` agent-route spine with parity tests.
- A checked package-local mechanics atlas for activation, scenario
  composition, federation closure, review gate, real-run harvest,
  antifragility, boundary bridge, Agon, recurrence, checkpoint, Experience,
  release support, Questbook, RPG, Titan, and portfolio governance.
- A convex `playbooks/<branch>/<family>/<slug>/PLAYBOOK.md` source home with an
  explicit manifest, branch/family route cards, generated compatibility
  readers, and source-home validation.
- A repo-local `evals/` intake/suite/report port that carries playbook eval
  pressure without becoming central verdict authority.
- An OS Abyss playbook-registry artifact bundle with ABI and SLSA/in-toto
  controls, durable evidence promotion, a materialized subject store, consumer
  trust-gate admission, and fail-closed compatibility checks.
- A local KAG provider packet and canonical source/entity/artifact/anchor/event/
  assertion/relation index family with owner-return and MCP source-return
  routes.
- An owner-local `stats/` port measuring reviewed-run reference coverage in the
  current gate-reviewed cohort while shared grammar and composition remain in
  `aoa-stats`.

### Changed

- Workspace paths and portable support surfaces now target the `/srv/AbyssOS`
  workspace posture.
- Audit, dependency-root, frontmatter, handoff, review-packet, landing-
  governance, and live-receipt contracts were hardened; valid quoted YAML
  punctuation is accepted without weakening malformed-quote checks.
- Memo checkpoint references and every authored/generated consumer contract
  were migrated to current reviewed `aoa-memo` routes.
- Mechanics payloads, builders, schemas, examples, tests, and evidence stores
  moved under their owning packages and parts. Root compatibility entrypoints
  were retained only where they remain public contracts, then mechanically
  slimmed and link/class validated.
- Decision indexing now detects unmodeled lanes, requires explicit modeled
  surface lists, and validates normalized contract paths.
- Review-packet generation preserves the canonical `aoa-evals` runtime-template
  source even when a legacy sibling layout supplies the compatible file.
- Compatibility Canary and Repo Validation now materialize every pinned sibling
  input needed by the full validator and trust path.
- Runnable validation and test commands are consolidated in executable owners
  and nearest `AGENTS.md` route cards rather than general documentation.

### Fixed

- Mechanics roots reject non-Markdown residue, route-card class drift, broken
  links, missing package validators, and unmodeled package/source surfaces.
- The playbook artifact consumer path now rejects missing identity, stale
  registry evidence, absent subject-store materialization, or a missing
  trust-gate verdict instead of accepting partial publication evidence.

### First-Parent Reconciliation (45/45)

The ordered pre-release history is recorded explicitly so the 38 commits that
were absent from the old changelog remain discoverable:

1. `d4c86ac` — Plant Titan sixteenth wave seed.
2. `d1b983d` — Add seed pack publication route playbook.
3. `53961ed` — Add playbook surface AGENTS guardrails (#147).
4. `f05c99c` — Slim root AGENTS route card (#148).
5. `1a2e848` — Retarget playbook workspace paths to AbyssOS.
6. `8ef684e` — Land AoA v0.4.0 playbook closeout follow-through (#150).
7. `ef4a4b2` — Install portable AoA skill foundation.
8. `d7d7ac7` — Roll out session-growth skills and GitHub landing (#152).
9. `78069a7` — Refresh shared AoA skill pack (#153).
10. `a0fc623` — Refresh shared AoA skill pack (#154).
11. `6096949` — Close playbook audit contract gaps (#155).
12. `e215e6c` — Allow quoted punctuation in playbook frontmatter.
13. `dad1107` — Refresh aoa-summon skill export (#157).
14. `4264cd2` — Refresh self-diagnose skill export.
15. `2e7b7ba` — Refresh memo checkpoint contract refs.
16. `c586604` — Add memory route trigger law (#160).
17. `f09955c` — Add local memo port (#161).
18. `ed1a973` — Make memo validation route portable (#162).
19. `d73839f` — Refresh memo contract routes (#163).
20. `fc35282` — Route playbook memory through reviewed intake.
21. `ed1b79d` — Add memo candidate for playbook reviewed intake.
22. `485cc16` — Canonicalize playbook decision indexes (#166).
23. `5ce2f68` — Add playbook root design spine (#167).
24. `b5fd44e` — Refactor playbook mechanics into package routes (#168).
25. `ef7e6b1` — Collapse mechanics root entrypoints (#169).
26. `a319eb3` — Harden mechanics documentation routes.
27. `b497263` — Slim mechanics README.
28. `f650756` — Refactor playbook source home routes (#172).
29. `a74e65f` — Add decision index tests (#173).
30. `f2642b6` — Detect unmodeled decision lane surfaces (#174).
31. `d56e78a` — Validate modeled decision surface contract entries (#175).
32. `5667de3` — Add local eval port skeleton.
33. `7c11165` — Reject non-markdown mechanics root files (#177).
34. `69d9fa2` — Fix review packet runtime template provenance.
35. `ebd584a` — Keep review packet template ref canonical.
36. `5ab6af2` — Fix canary deps and add playbook registry trust gate.
37. `71f55d6` — Add playbook KAG provider home (#181).
38. `24c7628` — Align KAG provider validation route (#182).
39. `5559ac6` — Add repo-local KAG indexes (#184).
40. `c712612` — Enforce repo-local KAG index parity (#186).
41. `2a51f77` — Pin deterministic repo-local KAG index gate (#187).
42. `cb33caa` — Add repository KAG index family (#188).
43. `1bfad25` — Publish canonical repository KAG indexes (#189).
44. `04e31a6` — Add playbook-local stats port (#190).
45. `5d6551e` — Enforce fail-closed playbook artifact admission (#191).

### Validation

- Release preparation reconciled the exact `v0.3.3..5d6551e` first-parent
  history, changed-path inventory, authored playbook source home, mechanics
  owners, decision records/indexes, generated readers, local ports, sibling
  contracts, and published artifact boundary instead of trusting the previous
  `[Unreleased]` section.
- The repository release gate validates root design, every mechanics package,
  decision/index parity, authored and generated playbook surfaces, review and
  composition contracts, local stats, sibling compatibility, the OS Abyss
  artifact/subject-store trust route, and the complete test suite.

### Notes

- Portable skill copies support playbook execution but do not make this
  repository the skill owner. Likewise, local memo, eval, KAG, and stats ports
  remain bounded consumers/providers and do not absorb durable memory, verdict,
  global graph, or shared measurement authority.
- Release-only marker, changelog, and regenerated-index commits follow the 45
  reconciled product/maintenance commits and are not hidden inside that count.

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

- The executable repository release gate completed successfully.

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

- The executable repository release gate completed successfully.

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

- The executable repository release gate completed successfully.

### Notes

- detailed trusted-rollout hold-track, rollout-cadence adjunct, and continuity playbook changes for this patch remain enumerated below under `Added` and `Changed`

## [0.3.0] - 2026-04-10

### Summary

- this release adds owner-first capability review tracks, live-publisher activation evidence, checkpoint-growth playbook surfaces, and stress/via-negativa adjuncts
- review-status contracts, evidence posture, and canary/remediation guidance are hardened around the current reviewed-run contour
- `aoa-playbooks` remains the scenario-composition and review layer rather than a generic runtime logging surface

### Validation

- The executable repository release gate completed successfully.

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

- the authored playbook corpus under `playbooks/*/*/*/PLAYBOOK.md`
- generated review surfaces under `generated/playbook_review_status.min.json`, `generated/playbook_review_packet_contracts.min.json`, and `generated/playbook_review_intake.min.json`
- existing activation, federation, composition, handoff, failure-catalog, subagent-recipe, and automation-seed surfaces under `generated/`

### Validation

- The executable repository release gate completed successfully.

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
- repo-first real-run workflow and harvest doctrine under `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/playbook-real-run-workflow.md`, `mechanics/real-run-harvest/parts/harvest-template-source-store/docs/playbook-real-run-harvest.md`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`, and `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`
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
- `15` authored playbook bundles under `playbooks/*/*/*/PLAYBOOK.md`
- `13` activation example-backed runtime-readable entries in `generated/playbook_activation_surfaces.min.json`
- `15` federation-checked entries in `generated/playbook_federation_surfaces.min.json`
- `7` composition-managed playbooks in `generated/playbook_composition_manifest.json`
- the first reviewed real-run summaries under `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/` plus gate-review verdict surfaces for `AOA-P-0017`, `AOA-P-0019`, and `AOA-P-0020`

### Validation

- The executable repository release gate completed successfully.

### Notes

- this is a repository release, not a claim that every current playbook is equally evidenced or equally mature
- `AOA-P-0019` and `AOA-P-0020` intentionally remain weaker than `AOA-P-0017` because their next moves depend on fresh real-world evidence rather than more repo-only elaboration
- package publishing, registry publishing, and per-playbook semantic versioning remain out of scope for `v0.1.0`
