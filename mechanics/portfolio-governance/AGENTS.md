# AGENTS.md

## Applies to

This card applies to `mechanics/portfolio-governance/`.

## Role

`portfolio-governance/` is the local mechanic for keeping the playbook model,
operational family, lifecycle, portfolio, and gap matrix coherent.

It validates package-local model docs rather than moving public conceptual
entrypoints into a package.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/PLACEMENT_AUDIT.md`,
this package `README.md`, and the root portfolio docs being touched.

## Boundaries

- Do not hide public model docs inside mechanics.
- Do not let portfolio governance become proof, memory, routing, or roadmap
  authority.
- Do not duplicate source playbook truth.

## Validation

```bash
python mechanics/portfolio-governance/scripts/validate_portfolio_governance_package.py
python scripts/validate_root_design.py
python scripts/validate_playbooks.py
```

## Closeout

Report which public model docs changed and whether root discoverability remains
intact.
