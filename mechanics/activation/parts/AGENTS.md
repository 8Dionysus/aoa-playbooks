# AGENTS.md

## Applies to

This card applies to `mechanics/activation/parts/`.

## Role

Parts under activation own bounded sub-operations of the activation mechanic.

## Read before editing

Read `../AGENTS.md`, `../README.md`, and `../PARTS.md` before changing a part.

## Boundaries

Parts may own package-local implementation details. They must not become
authored playbook truth or root generated-output authority.

## Validation

Run the validation named by the part README and then:

```bash
python mechanics/activation/scripts/validate_activation_package.py
```

## Closeout

Report which part changed and whether root compatibility paths changed.
