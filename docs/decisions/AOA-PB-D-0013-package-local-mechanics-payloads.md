# Move Mechanics Payloads Into Package Parts

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0013
- Original date: 2026-05-31
- Surface classes: mechanic package, package-local payload, validation guard, source topology, stronger-owner handoff, decision record
- Playbook routes: a2a-summon-return-checkpoint, checkpoint-distillation-closed-loop-pilot, self-agency-continuity-cycle, component-refresh-cycle, titan-closeout-audit
- Mechanic parents: recurrence, checkpoint, experience, release-support, questbook, rpg, titan, portfolio-governance
- Guard families: package route, source topology, package-local payload, validation guard, generated/read-model, stronger-owner boundary, playbook source boundary
- Posture: accepted package-local mechanics packages

## Context

After package-moving `activation`, `scenario-composition`,
`federation-closure`, `review-gate`, `real-run-harvest`, `antifragility`, and
`agon`, the placement audit still had mechanics-shaped root payloads across
recurrence, checkpoint, Experience, release support, questbook, RPG reflection,
Titan, and portfolio governance.

The correction is structural: mechanics-owned docs, schemas, examples, config,
and manifests should live in mechanics packages. Root stays for source
playbooks, quest sources, release entrypoints, generated read models, decision
records, root overview docs, and compatibility wrappers where they are real
operator contracts.

## Decision

Create package-local route packages and move their active payloads into parts:

- `mechanics/recurrence/`
- `mechanics/checkpoint/`
- `mechanics/experience/`
- `mechanics/release-support/`
- `mechanics/questbook/`
- `mechanics/rpg/`
- `mechanics/titan/`
- `mechanics/portfolio-governance/`

Each package has `AGENTS.md`, `README.md`, `PARTS.md`, `PROVENANCE.md`, and a
package validator. Package-local `PROVENANCE.md` and `legacy/` indices may name
former root paths only as historical names or accepted inputs. They are not
active root routes.

## Rationale

The right refactor is not a flat move of every root file. The right refactor is
a clear operation map: role, input, output, owner, next route, tools, and
validation.

For these mechanics, the owner is the package. Moving payloads into package
parts makes ownership visible without stealing:

- source playbook canon from `playbooks/`;
- quest source and campaign notes from `QUESTBOOK.md` and `quests/`;
- root public generated read models from `generated/`;
- release operator entrypoints from `docs/RELEASING.md` and
  `scripts/release_check.py`;
- sibling truth from memo, evals, skills, agents, or routing repos.

## Consequences

- Positive: remaining mechanics-shaped payloads now have package-local owners.
- Positive: root `legacy/` remains forbidden, and historical names are contained
  in package provenance/legacy surfaces.
- Positive: package validators can prove payload presence, owner split, and
  generated/read-model boundaries.
- Tradeoff: link repair is broader because old root docs/schemas/examples/config
  paths were heavily cited.
- Follow-up: future moves must update package parts, provenance, generated refs,
  validators, tests, and decision indexes in one slice.

## Current Applicability

As of 2026-05-31:

- Valid: recurrence, checkpoint, Experience, release-support, questbook, RPG,
  Titan, and portfolio-governance are active package-local mechanics packages.
- Valid: generated outputs stay root-published read models.
- Valid: source playbooks stay in `playbooks/`.
- Superseded by: AOA-PB-D-0014 for root mechanics file shape; still valid for
  package-local payload placement.

## Review Log

### 2026-05-31 - Package-local mechanics landing

- Previous assumption: some remaining mechanics-shaped root paths could be
  documented in place.
- New reality: mechanics-owned payloads moved into package parts; root retains
  only source, generated, release, overview, decision, sentinel, and wrapper
  surfaces.
- Source surfaces updated: `mechanics/*/`, `scripts/release_check.py`,
  `docs/RELEASING.md`, root design/readme surfaces, placement audit, rosters,
  generated refs, validators, and focused tests.
- Validation:
  package validators, `python scripts/validate_mechanics_skeleton.py`,
  `python scripts/validate_playbooks.py`, focused pytest, decision index check,
  and release check.

## Boundaries

- This decision does not move authored playbook canon out of `playbooks/`.
- This decision does not move quest source routes out of `QUESTBOOK.md` or
  `quests/`.
- This decision does not move generated read models out of `generated/`.
- This decision does not move release operator commands out of root.
- This decision does not claim memory checkpoint truth, role authority, proof
  verdicts, runtime deployment, CI authority, or route dispatch.
- This decision does not create a root `legacy/` directory.

## Source Surfaces

- `mechanics/recurrence/`
- `mechanics/checkpoint/`
- `mechanics/experience/`
- `mechanics/release-support/`
- `mechanics/questbook/`
- `mechanics/rpg/`
- `mechanics/titan/`
- `mechanics/portfolio-governance/`
- `scripts/mechanic_package_validator.py`
- `tests/test_package_local_mechanics_packages.py`
- `scripts/release_check.py`
- `mechanics/README.md`
- `docs/decisions/AOA-PB-D-0014-collapse-mechanics-root-entrypoints.md`

## Verification

```bash
python mechanics/recurrence/scripts/validate_recurrence_package.py
python mechanics/checkpoint/scripts/validate_checkpoint_package.py
python mechanics/experience/scripts/validate_experience_package.py
python mechanics/release-support/scripts/validate_release_support_package.py
python mechanics/questbook/scripts/validate_questbook_package.py
python mechanics/rpg/scripts/validate_rpg_package.py
python mechanics/titan/scripts/validate_titan_package.py
python mechanics/portfolio-governance/scripts/validate_portfolio_governance_package.py
python scripts/validate_mechanics_skeleton.py
python scripts/generate_decision_indexes.py --check
python scripts/validate_playbooks.py
python -m pytest -q tests/test_package_local_mechanics_packages.py tests/test_experience_wave3_seed_contracts.py
```
