# Scenario Composition Provenance

## Active-first rule

Start with current scenario-composition surfaces:

- `README.md`
- `PARTS.md`
- `parts/composition-surfaces/`
- root wrapper `scripts/generate_playbook_composition_surfaces.py`

Use this file only when old root paths or compatibility paths matter.

## Center or local origin

Scenario composition is a local playbook-native mechanic. It starts from
authored playbook routes, root source config, and upstream skill handoff
contracts. It is not center mechanic law.

## Previous placement

| Former root path | Active route | Status |
| --- | --- | --- |
| `scripts/generate_playbook_composition_surfaces.py` | `mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py` | implementation moved into scenario-composition package on 2026-05-31; root path retained as compatibility command wrapper |

## Legacy boundary

Former root script placement is historical. The active implementation is
package-local.

The root command path is `accepted-input` and `root-public`, not an alternate
source of truth.

Root config, root docs, root generated outputs, and root tests are intentionally
retained until a compatibility-backed package move lands.

## Archive route

- `legacy/INDEX.md` maps former root paths to active package routes.
- `legacy/DISTILLATION_LOG.md` records dated movement.
- No raw receipts are preserved for this package because the move used current
  repository source files, not external raw artifacts.
