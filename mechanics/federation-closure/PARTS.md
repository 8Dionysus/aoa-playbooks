# Federation Closure Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `federation-surfaces` | derive root federation closure read model from authored playbooks | `playbooks/*/*/*/PLAYBOOK.md`, `generated/playbook_federation_surfaces.min.json` | `python mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py --check` | active |

## Boundary payloads

| Payload | Current route | Reason |
| --- | --- | --- |
| federation schema | `mechanics/federation-closure/parts/federation-surfaces/schemas/playbook-federation-surface.schema.json` | package-local contract for federation readout validation |
| federation generated output | `generated/playbook_federation_surfaces.min.json` | root-published read model consumed by downstream readers |
| execution seam doc | `mechanics/activation/parts/activation-surface/docs/playbook-execution-seam.md` | activation-owned seam also governs federation, review, and composition joins |

## Part growth rule

Move only the public generated read model if downstream public refs and sibling
closure validation can remain explicit and covered.
