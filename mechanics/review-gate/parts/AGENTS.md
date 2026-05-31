# AGENTS.md

## Applies to

This card applies to `mechanics/review-gate/parts/`.

## Role

Parts hold active review-gate builder implementations.

Each part must keep one clear input/output map and leave root-public commands
and generated outputs stable unless a decision changes the compatibility
contract.

## Boundaries

- Do not move evidence directories into parts.
- Do not write generated outputs inside `parts/`.
- Do not claim proof, runtime, memory, eval, or source playbook authority.

## Validation

Run the package validator and the root wrapper `--check` command for the part
being changed.
