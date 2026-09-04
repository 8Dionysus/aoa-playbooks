# Activation Provenance

## Active-first rule

Start with current activation surfaces:

- `README.md`
- `PARTS.md`
- `parts/activation-surface/`
- root wrapper `scripts/generate_playbook_activation_surfaces.py`

Use this file only when old root paths or compatibility paths matter.

## Center or local origin

Activation is a local playbook-native mechanic. It starts from
`aoa-playbooks` source registry and authored playbook routes, not from a center
mechanic in `Agents-of-Abyss`.

## Previous placement

| Former root path | Active route | Status |
| --- | --- | --- |
| `scripts/generate_playbook_activation_surfaces.py` | `mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py` | implementation moved into activation package on 2026-05-31; root path retained as compatibility command wrapper |

## Legacy boundary

Former root script placement is historical. The active implementation is
package-local.

The root command path is `accepted-input` and `root-public`, not an alternate
source of truth.

Schema, example, generated output, and seam-doc root paths are intentionally
retained until a compatibility-backed package move lands.

## Archive route

- Historical former-path accounting is preserved in [AOA-PB-D-0018](../../docs/decisions/AOA-PB-D-0018-spark-and-legacy-scaffolding-retirement.md).
- No raw receipts are preserved for this package because the move used current
  repository source files, not external raw artifacts.
