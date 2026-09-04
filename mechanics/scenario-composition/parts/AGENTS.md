# AGENTS.md

## Applies to

This card applies to `mechanics/scenario-composition/parts/`.

## Role

Parts under scenario composition own bounded sub-operations of the composition
mechanic.

## Route by task

Start from the target part's source, config, builder, schema, and part README.
Use the package `README.md` and `PARTS.md` only when topology changes.

## Boundaries

Parts may own package-local implementation details and explicit source config
for their own projection. They must not become authored playbook truth, skill
meaning, runtime execution authority, or root generated-output authority.

## Validation

Run the validation named by the part README and then:

Run the parent package route in `../VALIDATION.md` on demand.

## Closeout

Report which part changed and whether root compatibility paths changed.
