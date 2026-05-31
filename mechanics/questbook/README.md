# Questbook Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | head-fed and local |
| role | keep public playbook obligations, questline outlines, and reanchor notes visible without becoming a second roadmap |
| trigger | quest item, questbook index, generated quest readout, questline outline, campaign reflection, or harvest reanchor change |
| playbooks owns | repo-local public obligation posture and questline/campaign reflection |
| stronger owner split | proof owners own proof obligations; memo owns durable lessons; roadmap stays roadmap |
| inputs | `QUESTBOOK.md`, `quests/`, generated quest readouts, questline docs, quest schemas/examples |
| outputs | checked package-local questbook posture |
| must not claim | private scratchpad, roadmap authority, proof closure, memory truth, or runtime dispatch |
| validation | `python mechanics/questbook/scripts/validate_questbook_package.py` |
| next route | root quest source, generated quest readout, rpg package, source playbook, or stronger owner repo |

## Active route

This package is active as package-local questbook posture.

Quest source and generated readouts remain root-public because they are source
stores and public read models.

## Source surfaces

- `QUESTBOOK.md`
- `quests/`
- `generated/quest_catalog.min.json`
- `generated/quest_dispatch.min.json`
- `mechanics/questbook/parts/questline-outline/docs/questline-and-campaign-model.md`
- `mechanics/questbook/parts/harvest-reanchor/docs/quest-harvest-and-reanchor.md`
- `mechanics/questbook/parts/questline-outline/schemas/questline_outline.schema.json`
- `mechanics/questbook/parts/questline-outline/examples/questline_outline.example.yaml`

## Growth posture

Future questbook package growth should validate source/readout coherence before
moving any public quest route.
