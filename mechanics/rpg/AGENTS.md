# AGENTS.md

## Applies to

This card applies to `mechanics/rpg/`.

## Role

`rpg/` is the head-fed and local mechanic for party-template and build-synergy
reflection inside playbooks.

It keeps RPG vocabulary bounded as reflection, not route authority.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/README.md`,
this package `README.md`, `mechanics/rpg/parts/party-template-model/docs/party-template-model.md`, and
`mechanics/rpg/parts/build-synergy-posture/docs/build-synergy-posture.md`.

## Boundaries

- Do not let RPG vocabulary become role authority or progression truth.
- Do not claim campaign runtime, quest authority, proof, or memory truth.
- Keep party-template readouts public and bounded.

## Validation

```bash
python mechanics/rpg/scripts/validate_rpg_package.py
python scripts/validate_playbooks.py
```

## Closeout

Report whether party-template docs, schema, example, or generated readout
changed.
