# Activation Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | local |
| role | make authored playbook scenarios activation-readable through a derived projection |
| trigger | a playbook joins, leaves, or changes the activation-readable cohort |
| playbooks owns | activation projection shape, source registry alignment, fallback and return posture projection |
| stronger owner split | runtime owns execution; routing owns dispatch; memo owns recall truth; evals own proof; skills own bounded execution |
| inputs | `generated/playbook_registry.min.json`, authored `playbooks/*/*/*/PLAYBOOK.md`, activation cohort constants |
| outputs | root-published `generated/playbook_activation_surfaces.min.json` |
| must not claim | runtime state, tool binding, route dispatch, memo search/ranking, eval verdicts, or hidden autonomous execution |
| validation | `python mechanics/activation/scripts/validate_activation_package.py` and `python mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py --check` |
| next route | `parts/activation-surface/`, `mechanics/activation/parts/activation-surface/docs/playbook-execution-seam.md`, root generated read model, or stronger owner repo |

## Active route

The active builder implementation lives under
`parts/activation-surface/scripts/generate_playbook_activation_surfaces.py`.

The root command `scripts/generate_playbook_activation_surfaces.py` remains as
an operator-facing compatibility wrapper because README, release checks, and
downstream agents already use that command path.

## Functioning parts

- `activation-surface`: builds and validates the compact activation projection
  from the playbook registry.

## Source surfaces

- `generated/playbook_registry.min.json`
- `playbooks/*/*/*/PLAYBOOK.md`
- `mechanics/activation/parts/activation-surface/docs/playbook-execution-seam.md`
- `generated/playbook_activation_surfaces.min.json`
- `mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py`

## Owner boundary

Activation surfaces are derived readers. They are weaker than authored
playbooks and the source registry.

Activation may expose trigger, participant, required skill family, evidence,
fallback, return, and memo posture fields that already exist in source
metadata. It must not invent runtime execution behavior.

## Growth posture

The next safe growth is part-local schema/example localization only if the
generated review and intake refs can preserve compatibility for the currently
published `mechanics/activation/parts/activation-surface/examples/playbook_activation.*.example.json` paths.
