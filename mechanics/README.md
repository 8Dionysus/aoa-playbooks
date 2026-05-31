# Playbook Mechanics

`mechanics/` is the package directory for repeatable playbook-layer mechanics.

The first screen should show the active packages. It should not become a shelf
of transition notes. Root-level mechanics docs are limited to this atlas and
`AGENTS.md`; durable detail belongs in package `README.md`, `PARTS.md`,
`PROVENANCE.md`, package-local `legacy/`, or `docs/decisions/`.

## Operating Card

| Field | Route |
| --- | --- |
| role | package directory for repeatable playbook-layer mechanics |
| input | recurring operation pressure, generated-reader drift, review-gate drift, package-boundary movement, or head-fed owner pressure from `Agents-of-Abyss` |
| output | package route, source-owner route, generated/read-model route, validator route, or stronger-owner handoff |
| owner | this atlas plus the target package card |
| next route | target package, source playbook, generated builder, decision record, or stronger owner repo |
| validation | `python scripts/validate_mechanics_skeleton.py`, package validator, `python scripts/validate_playbooks.py`, or `python scripts/release_check.py` |

## Root Files Rule

Allowed root files in `mechanics/`:

- `README.md`
- `AGENTS.md`

Do not add root-level roster, audit, template, backlog, legacy, notes, scratch,
migration, or `_meta/` holding surfaces. If the content is active, put it in the
package that owns the operation. If it is historical rationale, put it in
`docs/decisions/`. If it is old-path accounting, put it in package
`PROVENANCE.md`.

## Package Directory

| Package | Class | Role |
| --- | --- | --- |
| `activation/` | local | runtime-readable activation surfaces without owning runtime state |
| `agon/` | head-fed | trial, kernel-binding, campaign, adoption, and recurrence-adapter choreography |
| `antifragility/` | head-fed/local | stress lanes, re-entry gates, harvest, runtime-chaos, and via negativa posture |
| `boundary-bridge/` | head-fed | handoff and orchestrator bridge posture without ownership transfer |
| `checkpoint/` | head-fed | checkpoint return and distillation routes without memory truth |
| `experience/` | head-fed | adoption, certification, service, office, and governance playbook posture |
| `federation-closure/` | local | sibling refs and federation readouts without sibling ownership |
| `portfolio-governance/` | local | model, lifecycle, gap, portfolio, and chooser discipline |
| `questbook/` | head-fed | questline/campaign adjunct posture without quest authority |
| `real-run-harvest/` | local | run evidence and review posture without proof or memory truth |
| `recurrence/` | head-fed/local | recurrence, return, relaunch, and reanchor posture |
| `release-support/` | head-fed/local | release, rollout, rollback, retention, and operator support posture |
| `review-gate/` | local | review status, packet, intake, landing governance, and Phase Alpha readouts |
| `rpg/` | head-fed | RPG vocabulary as bounded reflection only |
| `scenario-composition/` | local | handoffs, failure catalog, automation seeds, subagent recipes, and composition manifests |
| `titan/` | head-fed/local | Titan route ecology and drill posture without role authority |

## Head-Fed Mechanics

Head-fed mechanics begin as center pressure in `Agents-of-Abyss` and become
playbook-local only when this repo has a repeatable operation, source surface,
owner split, stop-line, and validator.

Current head-fed package routes: `agon`, `antifragility`, `boundary-bridge`,
`checkpoint`, `experience`, `questbook`, `recurrence`, `release-support`,
`rpg`, and `titan`.

Head-fed never means `aoa-playbooks` owns center law, runtime execution, proof
verdicts, memory truth, role authority, route dispatch, stats truth, or KAG
promotion.

## Local Mechanics

Local mechanics begin inside `aoa-playbooks` from scenario composition,
generated readers, review gates, evidence posture, or playbook portfolio
discipline.

Current local package routes: `activation`, `federation-closure`,
`portfolio-governance`, `real-run-harvest`, `review-gate`, and
`scenario-composition`.

Local never means the package replaces source playbooks, generated read models,
root decisions, public release entrypoints, or sibling-owner truth.

## Placement Rules

- Source-authored scenario canon stays in `playbooks/*/PLAYBOOK.md`.
- Quest sources stay in `QUESTBOOK.md` and `quests/`.
- Root generated read models stay in `generated/`.
- Durable rationale stays in `docs/decisions/`.
- Root command wrappers may stay in `scripts/` only when they are public
  compatibility entrypoints.
- Mechanics-owned docs, schemas, examples, config, manifests, builders, and
  evidence templates live under `mechanics/<package>/parts/...`.
- No source playbook has moved.

## Legacy Rules

Legacy names are former paths, accepted input names, generated projections,
historical wave names, candidate names, or stronger-owner vocabulary. They are
not alternate active routes.

Concrete former-path accounting belongs in the owning package `PROVENANCE.md`
and, only when useful, package-local `legacy/`. A repository-root `legacy/`
directory is forbidden for mechanics accounting.

## Package Shape

A package needs real function before it exists. Minimum shape:

- `mechanics/<slug>/AGENTS.md`
- `mechanics/<slug>/README.md`
- `mechanics/<slug>/PARTS.md`
- `mechanics/<slug>/PROVENANCE.md`
- package validator when payloads move

Add `parts/`, `docs/`, `schemas/`, `examples/`, `config/`, `manifests/`,
`scripts/`, or `legacy/` only when the package has an active payload and local
validation.

## Validation

Run:

```bash
python scripts/validate_mechanics_skeleton.py
python scripts/validate_playbooks.py
```

For package-local work, run the target package validator. For release-bound
changes, run:

```bash
python scripts/release_check.py
```
