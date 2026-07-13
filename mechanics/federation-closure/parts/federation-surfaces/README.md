# Federation Surfaces Part

## Role

This part owns the implementation that builds
`generated/playbook_federation_surfaces.min.json` from authored playbooks.

## Source surfaces

- `playbooks/*/*/*/PLAYBOOK.md`
- `generated/playbook_federation_surfaces.min.json`
- root command wrapper `mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py`

## Boundary

The generated output remains root-published. This part owns the builder
implementation, not the public output path.

## Validation

The part-local builder and package validator are the executable owners. Their
focused order lives in the nearest `AGENTS.md`.
