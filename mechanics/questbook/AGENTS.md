# AGENTS.md

## Applies to

This card applies to `mechanics/questbook/`.

## Role

`questbook/` is the `head-fed/local` mechanic for public follow-through
obligations, questline/campaign outlines, harvest reanchor notes, and quest
read models.

The root `QUESTBOOK.md`, `quests/`, and generated quest readouts remain
root-public source/read-model routes.

## Route by task

- Public obligation or quest state: use `QUESTBOOK.md` and the exact
  `quests/` source.
- Questline or campaign outline: use the questline-and-campaign model.
- Package topology or stronger-owner orientation: use `README.md`.

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
