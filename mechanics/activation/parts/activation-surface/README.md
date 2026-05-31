# Activation Surface Part

## Role

This part owns the implementation that builds
`generated/playbook_activation_surfaces.min.json` from the root playbook
registry.

## Source surfaces

- `generated/playbook_registry.min.json`
- `generated/playbook_activation_surfaces.min.json`
- root command wrapper `mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py`

## Boundary

The generated output remains root-published. This part owns the builder
implementation, not the public output path.

## Validation

Run:

```bash
python mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py --check
python mechanics/activation/scripts/validate_activation_package.py
```
