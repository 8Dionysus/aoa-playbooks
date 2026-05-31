# AGENTS.md

## Applies to

This card applies to `mechanics/antifragility/parts/`.

## Role

Parts hold active antifragility docs, schemas, and examples for the playbook
layer.

## Boundaries

- Keep source playbook truth in `playbooks/`.
- Keep proof, runtime, memory, KAG, routing, and role truth with stronger
  owners.
- Keep schemas/examples paired with validation.

## Validation

Run the antifragility package validator and the focused tests for the changed
part.
