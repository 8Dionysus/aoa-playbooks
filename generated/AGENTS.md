# AGENTS.md

This file applies to artifacts under `generated/`.

## Important split

`generated/` contains two different kinds of surfaces in this repository:

- `playbook_registry.min.json` is a source-authored machine-readable registry surface for the playbook layer
- `playbook_activation_surfaces.min.json` is a derived activation projection
- `playbook_federation_surfaces.min.json` is a derived federation-closure projection

Do not treat all files in this directory the same way.
The registry is canonical playbook metadata.
The activation and federation files are generated projections of canonical inputs.

## Source and derivation map

Keep this mapping legible:

- `generated/playbook_registry.min.json` stays aligned with authored scenario metadata and is validated by `scripts/validate_playbooks.py`
- `generated/playbook_activation_surfaces.min.json` is produced from the registry by `scripts/generate_playbook_activation_surfaces.py`
- `generated/playbook_federation_surfaces.min.json` is produced from `playbooks/*/PLAYBOOK.md` by `scripts/generate_playbook_federation_surfaces.py`

The derived surfaces should stay schema-backed, compact, and runtime-readable.
They must not become a second authored playbook layer.

## Editing posture

For `playbook_registry.min.json`:

- edit carefully because it is source-authored metadata
- preserve stable ids, names, and ordering unless a real semantic change requires otherwise
- keep it aligned with the corresponding authored `PLAYBOOK.md` bundles

For `playbook_activation_surfaces.min.json` and `playbook_federation_surfaces.min.json`:

- Do not hand-edit derived payloads
- regenerate them from canonical inputs
- keep runtime-local details, hidden wiring, and transport specifics out
- do not invent new skill, agent, eval, or memo semantics here

## Validation

Whenever canonical inputs change, run:

```bash
python scripts/generate_playbook_activation_surfaces.py --check
python scripts/generate_playbook_federation_surfaces.py --check
python scripts/validate_playbooks.py
```

If a derived file is out of date, regenerate it with the matching generator script before finishing.
