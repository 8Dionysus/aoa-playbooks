# Federation Surfaces Part

## Role

This part owns the implementation that builds
`generated/playbook_federation_surfaces.min.json` from authored playbooks.

## Source surfaces

- `playbooks/*/PLAYBOOK.md`
- `generated/playbook_federation_surfaces.min.json`
- root command wrapper `mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py`

## Boundary

The generated output remains root-published. This part owns the builder
implementation, not the public output path.

## Validation

Run:

```bash
python mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py --check
python mechanics/federation-closure/scripts/validate_federation_closure_package.py
```
