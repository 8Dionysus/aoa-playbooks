# AGENTS.md

## Applies to

This card applies to `mechanics/questbook/`.

## Role

`questbook/` is the head-fed and local mechanic for public follow-through
obligations, questline/campaign outlines, harvest reanchor notes, and quest
read models.

The root `QUESTBOOK.md`, `quests/`, and generated quest readouts remain
root-public source/read-model routes.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/PLACEMENT_AUDIT.md`,
this package `README.md`, `QUESTBOOK.md`, and `mechanics/questbook/parts/questline-outline/docs/questline-and-campaign-model.md`.

## Boundaries

- Do not turn quests into a private task sink.
- Do not move `QUESTBOOK.md`, `quests/`, or generated quest readouts without a
  new public compatibility decision.
- Do not claim roadmap, proof, memory, or runtime authority.

## Validation

```bash
python mechanics/questbook/scripts/validate_questbook_package.py
python scripts/validate_playbooks.py
```

## Closeout

Report whether quest source, generated quest readouts, or questline outline
contracts changed.
