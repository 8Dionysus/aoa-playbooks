# AGENTS.md

This file applies to artifacts under `generated/`.

## Important split

`generated/` contains two different kinds of surfaces in this repository:

- `playbook_registry.min.json` is a source-authored machine-readable registry surface for the playbook layer
- `playbook_activation_surfaces.min.json` is a derived activation projection
- `playbook_federation_surfaces.min.json` is a derived federation-closure projection
- `playbook_review_status.min.json` is a derived evidence-status projection over reviewed summaries and gate-review notes
- `playbook_handoff_contracts.json`, `playbook_failure_catalog.json`, `playbook_subagent_recipes.json`, `playbook_automation_seeds.json`, and `playbook_composition_manifest.json` are derived composition projections for the canonical playbook cohort

Do not treat all files in this directory the same way.
The registry is canonical playbook metadata.
The activation and federation files are generated projections of canonical inputs.

## Source and derivation map

Keep this mapping legible:

- `generated/playbook_registry.min.json` stays aligned with authored scenario metadata and is validated by `scripts/validate_playbooks.py`
- `generated/playbook_activation_surfaces.min.json` is produced from the registry by `scripts/generate_playbook_activation_surfaces.py`
- `generated/playbook_federation_surfaces.min.json` is produced from `playbooks/*/PLAYBOOK.md` by `scripts/generate_playbook_federation_surfaces.py`
- `generated/playbook_review_status.min.json` is produced from `docs/real-runs/*.md` plus `docs/gate-reviews/*.md` by `scripts/generate_playbook_review_status.py`
- `generated/playbook_handoff_contracts.json`, `generated/playbook_failure_catalog.json`, `generated/playbook_subagent_recipes.json`, `generated/playbook_automation_seeds.json`, and `generated/playbook_composition_manifest.json` are produced by `scripts/generate_playbook_composition_surfaces.py`

The derived surfaces should stay compact, reviewable, and playbook-owned.
They must not become a second authored playbook layer.

## Editing posture

For `playbook_registry.min.json`:

- edit carefully because it is source-authored metadata
- preserve stable ids, names, and ordering unless a real semantic change requires otherwise
- keep it aligned with the corresponding authored `PLAYBOOK.md` bundles

For `playbook_activation_surfaces.min.json`, `playbook_federation_surfaces.min.json`, `playbook_review_status.min.json`, and the composition outputs:

- Do not hand-edit derived payloads
- regenerate them from canonical inputs
- activation surfaces may include compact return hints when those hints are derived from canonical playbook inputs
- composition surfaces may include bounded handoff, failure, subagent, and automation metadata when that metadata is derived from authored playbooks plus source-owned composition overrides
- keep runtime-local details, hidden wiring, and transport specifics out
- do not invent new skill, agent, eval, or memo semantics here

## Validation

Whenever canonical inputs change, run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_playbook_activation_surfaces.py --check
python scripts/generate_playbook_federation_surfaces.py --check
python scripts/generate_playbook_review_status.py --check
python scripts/generate_playbook_composition_surfaces.py --check
python scripts/validate_playbooks.py
```

If a derived file is out of date, regenerate it with the matching generator script before finishing.
