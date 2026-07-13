# Activation Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `activation-surface` | derive root activation read model from source registry entries | `generated/playbook_registry.min.json`, `playbooks/*/*/*/PLAYBOOK.md`, `generated/playbook_activation_surfaces.min.json` | `mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py` | active |

## Boundary payloads

| Payload | Current route | Reason |
| --- | --- | --- |
| activation schema | `mechanics/activation/parts/activation-surface/schemas/playbook-activation-surface.schema.json` | package-local contract for activation examples and generated validation |
| activation examples | `mechanics/activation/parts/activation-surface/examples/playbook_activation.*.example.json` | package-local examples consumed by review intake |
| activation generated output | `generated/playbook_activation_surfaces.min.json` | root-published read model consumed by downstream readers |
| execution seam doc | `mechanics/activation/parts/activation-surface/docs/playbook-execution-seam.md` | activation-owned seam also governs federation, review, and composition joins |

## Part growth rule

Move only the public generated read model if downstream refs and validator
coverage can remain explicit.
