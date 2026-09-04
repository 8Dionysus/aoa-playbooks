# AGENTS.md

## Applies to

This card applies to `mechanics/portfolio-governance/`.

## Role

`portfolio-governance/` is the local mechanic for keeping the playbook model,
operational family, lifecycle, portfolio, and gap matrix coherent.

It validates package-local model docs rather than moving public conceptual
entrypoints into a package.

## Route by task

Start from the exact model, lifecycle, portfolio, gap, or chooser doc being
changed. Use `README.md` for package topology and the root public model route
when discoverability moves.

## Boundaries

- Do not hide public model docs inside mechanics.
- Do not let portfolio governance become proof, memory, routing, or roadmap
  authority.
- Do not duplicate source playbook truth.

## Validation

Run `VALIDATION.md` in this directory, then the common mechanics route in the root `VALIDATION.md`.

## Closeout

Report which public model docs changed and whether root discoverability remains
intact.
