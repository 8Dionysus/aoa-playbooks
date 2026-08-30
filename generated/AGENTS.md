# AGENTS.md

This file applies to artifacts under `generated/`.

## Authority and derivation map

`playbook_registry.min.json` is source-authored registry metadata. Keep it
aligned with authored `PLAYBOOK.md` frontmatter and the trusted bundle
contract.

Every other file in this directory is a derived read model. Route by family:

| Outputs | Owner source or builder |
| --- | --- |
| `agon_*_registry.min.json` | matching config and builder under `mechanics/agon/parts/*/` |
| `playbook_activation_surfaces.min.json` | `mechanics/activation/parts/activation-surface/` |
| `playbook_federation_surfaces.min.json` | `mechanics/federation-closure/parts/federation-surfaces/` |
| review, intake, landing, and Phase Alpha readouts | matching part under `mechanics/review-gate/parts/` |
| handoff, failure, subagent, automation, and composition readouts | `mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py` |
| `playbook_plan_contours.min.json` | `mechanics/scenario-composition/parts/plan-contours/` |

Inspect the exact output's declared builder or schema before editing its
source. Derived files stay compact, reviewable, and weaker than authored
playbooks, configs, evidence notes, and sibling-owner contracts.

## Editing posture

For `playbook_registry.min.json`:

- edit carefully because it is source-authored metadata
- preserve stable ids, names, and ordering unless a real semantic change requires otherwise
- keep it aligned with the corresponding authored `PLAYBOOK.md` bundles

For `agon_*_registry.min.json`, `playbook_activation_surfaces.min.json`, `playbook_federation_surfaces.min.json`, `playbook_review_status.min.json`, `playbook_landing_governance.min.json`, the composition outputs, and `playbook_plan_contours.min.json`:

- Do not hand-edit derived payloads
- regenerate them from canonical inputs
- activation surfaces may include compact return hints when those hints are derived from canonical playbook inputs
- composition surfaces may include bounded handoff, failure, subagent, and automation metadata when that metadata is derived from authored playbooks plus source-owned composition overrides
- plan contours may include only abstract DAG, effect, artifact, evidence, eval,
  retention, and closeout bindings derived from exact source alignment
- keep runtime-local details, hidden wiring, and transport specifics out
- do not invent new skill, agent, eval, or memo semantics here

## Validation

Run the exact owner builder in `--check` mode and its package validator.
Regenerate from source when parity fails; never patch the output to make the
check green.

Then run:

```bash
python scripts/validate_playbooks.py
```

For registry or artifact-bundle identity changes, also run
`python scripts/validate_abyss_machine_playbook_bundle.py`. For release-bound
or cross-family changes, use `python scripts/release_check.py`.
