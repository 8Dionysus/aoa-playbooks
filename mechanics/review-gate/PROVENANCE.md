# Review Gate Provenance

## Active-first rule

Start with current review-gate package surfaces:

- `README.md`
- `PARTS.md`
- `parts/review-status/`
- `parts/review-packet-contracts/`
- `parts/review-intake/`
- `parts/landing-governance/`
- `parts/phase-alpha-readiness/`
- root compatibility wrappers in `scripts/`

Use this file only when former root builder paths or compatibility paths
matter.

## Center or local origin

Review gate is a local playbook-native mechanic. It starts from
`aoa-playbooks` review evidence, generated read models, and Phase Alpha
readiness config, not from a center mechanic in `Agents-of-Abyss`.

## Previous placement

| Former root path | Active route | Status |
| --- | --- | --- |
| `scripts/generate_playbook_review_status.py` | `mechanics/review-gate/parts/review-status/scripts/generate_playbook_review_status.py` | implementation moved into review-gate package on 2026-05-31; root path retained as compatibility command wrapper |
| `scripts/generate_playbook_review_packet_contracts.py` | `mechanics/review-gate/parts/review-packet-contracts/scripts/generate_playbook_review_packet_contracts.py` | implementation moved into review-gate package on 2026-05-31; root path retained as compatibility command wrapper |
| `scripts/generate_playbook_review_intake.py` | `mechanics/review-gate/parts/review-intake/scripts/generate_playbook_review_intake.py` | implementation moved into review-gate package on 2026-05-31; root path retained as compatibility command wrapper |
| `scripts/generate_playbook_landing_governance.py` | `mechanics/review-gate/parts/landing-governance/scripts/generate_playbook_landing_governance.py` | implementation moved into review-gate package on 2026-05-31; root path retained as compatibility command wrapper |
| `scripts/generate_phase_alpha_surfaces.py` | `mechanics/review-gate/parts/phase-alpha-readiness/scripts/generate_phase_alpha_surfaces.py` | implementation moved into review-gate package on 2026-05-31; root path retained as compatibility command wrapper |

## Legacy boundary

Former root script placement is historical. The active implementations are
package-local.

Root command paths are `accepted-input` and `root-public`, not alternate
sources of truth.

Evidence directories, source config, schemas, examples, and generated outputs
are intentionally retained at root because those paths are public contracts and
source stores.

## Archive route

- Historical former-path accounting is preserved in [AOA-PB-D-0018](../../docs/decisions/AOA-PB-D-0018-spark-and-legacy-scaffolding-retirement.md).
- No raw receipts are preserved for this package because the move used current
  repository source files, not external raw artifacts.
