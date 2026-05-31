# Questbook Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `root-public-index` | keep public obligation index visible | `QUESTBOOK.md` | `validate_playbooks.py` | root-source |
| `quest-source-store` | keep quest items lane-readable | `quests/` | `validate_playbooks.py` | root-source |
| `quest-read-models` | keep compact quest readouts root-published | `generated/quest_catalog.min.json`, `generated/quest_dispatch.min.json` | `validate_playbooks.py` | generated-projection |
| `questline-outline` | keep campaign outline posture bounded | `mechanics/questbook/parts/questline-outline/docs/questline-and-campaign-model.md`, schema/example pair | package validator | package-local |
| `harvest-reanchor` | keep harvest and reanchor posture explicit | `mechanics/questbook/parts/harvest-reanchor/docs/quest-harvest-and-reanchor.md` | `validate_playbooks.py` | package-local |

## Deferred payloads

Payloads moved into package-local parts in this package landing.

Questline and harvest/reanchor payloads are package-local. `QUESTBOOK.md`,
`quests/`, and generated quest readouts remain root source/readout routes.
