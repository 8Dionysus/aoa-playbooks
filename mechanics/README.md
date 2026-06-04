# Playbook Mechanics

`mechanics/` is the dispatcher for repeatable playbook-layer operations.

Use this atlas when the work is about the operation around a playbook: handoff,
gate, recurrence, release, evidence posture, generated reader, or boundary
choreography. Use `playbooks/` when authored scenario canon changes.

## Route

1. Choose the package from the map below.
2. Read package `AGENTS.md`, `README.md`, `PARTS.md`, and `PROVENANCE.md`.
3. Follow the owning source surface: package part, source playbook, generated
   builder, decision record, or stronger owner repo.
4. Run the package validator and the repo-level mechanics checks.

## Package Map

| Package | Class | Use for |
| --- | --- | --- |
| `activation/` | local | activation-readable projections without runtime ownership |
| `agon/` | head-fed/local | trial, kernel-binding, campaign, adoption, and recurrence-adapter choreography |
| `antifragility/` | head-fed/local | stress lanes, re-entry gates, harvest, runtime-chaos, and via negativa posture |
| `boundary-bridge/` | head-fed/local | cross-owner handoff and orchestrator alignment without ownership transfer |
| `checkpoint/` | head-fed/local | checkpoint return and distillation without memory truth |
| `experience/` | head-fed/local | adoption, certification, service, office, and governance posture |
| `federation-closure/` | local | sibling refs and federation readouts without sibling ownership |
| `portfolio-governance/` | local | model, lifecycle, gap, portfolio, and chooser discipline |
| `questbook/` | head-fed/local | questline and campaign adjuncts without quest authority |
| `real-run-harvest/` | local | run evidence and review posture without proof or memory truth |
| `recurrence/` | head-fed/local | recurrence, return, relaunch, and reanchor posture |
| `release-support/` | head-fed/local | release, rollout, rollback, retention, and operator support posture |
| `review-gate/` | local | review status, packet, intake, landing governance, and Phase Alpha readouts |
| `rpg/` | head-fed/local | RPG vocabulary as bounded reflection only |
| `scenario-composition/` | local | handoffs, failure catalog, automation seeds, subagent recipes, and composition manifests |
| `titan/` | head-fed/local | Titan route ecology and drill posture without role authority |

## Root Contract

Root `mechanics/` has only:

- `README.md`
- `AGENTS.md`

Do not add root rosters, audits, templates, backlogs, notes, `_meta/`, or
`legacy/` holding areas. Active operation detail belongs in the owning package.
Durable rationale belongs in `docs/decisions/`. Former-path accounting belongs
in package `PROVENANCE.md` and package-local `legacy/` when needed.

## Class Contract

- `head-fed`: pressure starts in `Agents-of-Abyss`.
- `local`: pressure starts in `aoa-playbooks`.
- `head-fed/local`: both are true for this repository.

The class names route origin and owner split. They do not transfer center law,
runtime execution, proof verdicts, memory truth, role authority, route dispatch,
stats truth, KAG promotion, generated-reader source truth, or source playbook
canon.

## Placement

- Source-authored scenario canon stays in `playbooks/*/*/*/PLAYBOOK.md`.
- Mechanics-owned docs, schemas, examples, config, manifests, builders, and
  evidence templates live under `mechanics/<package>/parts/...`.
- Root generated read models stay root-published under `generated/`.
- Root command wrappers may stay in `scripts/` only as public compatibility
  entrypoints.
- A package starts with `AGENTS.md`, `README.md`, `PARTS.md`, `PROVENANCE.md`,
  and a package validator when payloads move.

No source playbook has moved.

## Validation

```bash
python scripts/validate_mechanics_skeleton.py
python scripts/validate_playbooks.py
```

For package-local work, run the target package validator. For release-bound
changes, run:

```bash
python scripts/release_check.py
```
