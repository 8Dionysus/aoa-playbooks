# Federation Closure Provenance

## Active-first rule

Start with current federation-closure surfaces:

- `README.md`
- `PARTS.md`
- `parts/federation-surfaces/`
- root wrapper `scripts/generate_playbook_federation_surfaces.py`

Use this file only when old root paths or compatibility paths matter.

## Center or local origin

Federation closure is a local playbook-native mechanic. It starts from
authored playbook cross-repo refs and sibling-owner closure checks.

## Previous placement

| Former root path | Active route | Status |
| --- | --- | --- |
| `scripts/generate_playbook_federation_surfaces.py` | `mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py` | implementation moved into federation-closure package on 2026-05-31; root path retained as compatibility command wrapper |

## Legacy boundary

Former root script placement is historical. The active implementation is
package-local.

The root command path is `accepted-input` and `root-public`, not an alternate
source of truth.

Root schema and generated output paths are intentionally retained until a
compatibility-backed package move lands.

## Archive route

- `legacy/INDEX.md` maps former root paths to active package routes.
- `legacy/DISTILLATION_LOG.md` records dated movement.
- No raw receipts are preserved for this package because the move used current
  repository source files, not external raw artifacts.
