# AGENTS.md

## Applies to

This card applies to `mechanics/agon/parts/`.

## Role

Parts hold active Agon package payloads.

## Boundaries

- Keep authored playbooks in `playbooks/`.
- Keep generated registries in root `generated/`.
- Keep quest and recurrence manifest stores at root unless a later decision
  changes their source-store role.
- Keep all Agon surfaces pre-protocol unless center owner accepts otherwise.

## Validation

Run the Agon package validator and the part-specific root wrapper command.
