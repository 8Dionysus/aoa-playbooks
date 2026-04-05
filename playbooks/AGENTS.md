# AGENTS.md

This file applies to authored playbook bundles under `playbooks/*/PLAYBOOK.md`.

## What lives here

`playbooks/` is the authored scenario layer of `aoa-playbooks`.
Each `PLAYBOOK.md` is a source-owned scenario object that should stay aligned with:

- `generated/playbook_registry.min.json` for compact machine-readable metadata
- `docs/PLAYBOOK_BUNDLE_CONTRACT.md` for the authored bundle contract
- `docs/PLAYBOOK_EXECUTION_SEAM.md` for the bounded derived activation and federation posture
- `config/playbook_composition_overrides.json` for bounded composition adjuncts that should not leak into frontmatter
- `scripts/validate_playbooks.py` for machine-checked shape, sections, and cross-repo closure

## Canonical shape

Keep each authored bundle compact and predictable:

- store it at `playbooks/<slug>/PLAYBOOK.md`
- keep `<slug>` aligned with frontmatter `name`
- keep YAML frontmatter registry-aligned
- keep the fixed section set expected by the validator

The required bundle sections are:

- `Intent`
- `Trigger boundary`
- `Prerequisites`
- `Participating agents`
- `Required skills`
- `Decision points`
- `Handoffs`
- `Fallback and rollback posture`
- `Expected evidence posture`
- `Expected artifacts`
- `Eval anchors`
- `Memory writeback`
- `Canonical route`

## Editing posture

A playbook is not a skill.
Do not let a bundle quietly absorb single-skill execution meaning, role taxonomy, eval doctrine, memo taxonomy, or routing logic.
Use exact neighboring references instead:

- agent names should resolve in `aoa-agents`
- eval anchors should resolve in `aoa-evals`
- federation-ready `required_skills` should resolve in `aoa-skills`
- `memo_contract_refs` and `memo_writeback_targets` should stay inside `aoa-memo` contracts

Composition-owned adjuncts such as failure codes, subagent recipe refs, automation seed refs, and bounded playbook-to-playbook followups belong in `config/playbook_composition_overrides.json` and the derived `generated/playbook_*` composition surfaces, not in ad hoc prose or runtime-only notes.

Keep handoffs, fallback posture, and expected evidence explicit in the authored bundle rather than hiding them in surrounding prose.
Keep return posture explicit inside existing sections when a playbook can lose axis, ownership boundary, or checkpoint integrity.

## Adding or changing a bundle

When you add or materially change a playbook:

- update frontmatter only when the scenario contract truly changed
- keep `generated/playbook_registry.min.json` aligned with the authored bundle
- preserve the compact authored route and avoid runtime-local implementation detail
- keep bundle text public-safe and portable

Do not create nested `AGENTS.md` inside individual playbook folders unless a future subfamily actually needs different local rules.
The authored `PLAYBOOK.md` should remain the main object, not a forest of per-playbook policy files.

## Validation

Run the normal playbook-layer checks:

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_playbook_activation_surfaces.py --check
python scripts/generate_playbook_federation_surfaces.py --check
python scripts/generate_playbook_review_status.py --check
python scripts/generate_playbook_review_packet_contracts.py --check
python scripts/generate_playbook_review_intake.py --check
python scripts/generate_playbook_composition_surfaces.py --check
python scripts/generate_phase_alpha_surfaces.py --check
python scripts/validate_playbooks.py
python -m pytest -q tests
```

If a playbook edit changed scenario meaning, say so explicitly in the final report.
If it only fixed metadata drift, say that too.
