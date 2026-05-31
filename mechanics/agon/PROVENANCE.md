# Agon Provenance

## Active-first rule

Start with current Agon package parts:

- `README.md`
- `PARTS.md`
- `parts/trial-playbooks/`
- `parts/trial-kernel-bindings/`
- `parts/campaign-playbooks/`
- `parts/adoption/`
- `parts/recurrence-adapter/`

Use this file only when former root paths, center source, or package-local
stores matter.

## Center or local origin

Agon is head-fed from `Agents-of-Abyss/mechanics/agon/`.

The playbook-local landing owns pre-protocol trial and campaign choreography
payloads, registry seeds, schema/example contracts, builder implementations,
and recurrence-adapter docs.

## Previous placement

| Former root family | Active route | Status |
| --- | --- | --- |
| `docs/AGON_*.md` and `docs/AGONIC_TRIAL_ADOPTION_PLAYBOOK.md` | `mechanics/agon/parts/*/docs/` | moved into Agon package on 2026-05-31 |
| `config/agon_*.seed.json` | `mechanics/agon/parts/*/config/` | moved into Agon package on 2026-05-31 |
| `schemas/agon*.json` and `schemas/agonic_trial_adoption_run_v1.json` | `mechanics/agon/parts/*/schemas/` | moved into Agon package on 2026-05-31 |
| `examples/agon*.json` and `examples/agonic_trial_adoption_run.example.json` | `mechanics/agon/parts/*/examples/` | moved into Agon package on 2026-05-31 |
| `scripts/*agon*.py` builder/validator implementations | `mechanics/agon/parts/*/scripts/` | implementations moved into Agon package on 2026-05-31; root script paths remain compatibility command wrappers |
| `manifests/recurrence/component.agon*.json` | `mechanics/agon/parts/*/manifests/` | recurrence manifests moved into Agon package on 2026-05-31 |

## Retained root stores

- `playbooks/agon-*/PLAYBOOK.md`: source playbook canon.
- `quests/AOP-Q-AGON-*`: quest source notes.
- `generated/agon_*_registry.min.json`: generated read models.
- root `scripts/*agon*.py`: compatibility command/import paths.

## Legacy boundary

Former root payload placement is historical. The active package routes are
under `mechanics/agon/parts/`.

Root script paths are `accepted-input` and `root-public`, not active
implementation homes.

## Archive route

- `legacy/INDEX.md` maps former root families to active package routes.
- `legacy/DISTILLATION_LOG.md` records dated movement.
- No raw duplicates are kept in `legacy/`; git history preserves old file
  bodies.
