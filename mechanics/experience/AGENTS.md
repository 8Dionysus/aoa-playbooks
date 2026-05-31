# AGENTS.md

## Applies to

This card applies to `mechanics/experience/`.

## Role

`experience/` is the head-fed and local mechanic for adoption, certification,
retention, rollback, governance, office, service, and watch playbook posture.

It validates why the current Experience Wave 3 docs, schemas, and examples
remain package-local contract pairs in `aoa-playbooks`.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/PLACEMENT_AUDIT.md`,
this package `README.md`, and the focused Experience tests.

## Boundaries

- Do not move source playbooks out of `playbooks/`.
- Do not claim assistant service authority, proof verdicts, memory truth, or
  runtime service operation.
- Do not move package-local Experience schemas/examples again unless
  compatibility tests and package provenance move in the same slice.

## Validation

```bash
python mechanics/experience/scripts/validate_experience_package.py
python -m pytest -q tests/test_experience_wave3_seed_contracts.py
python scripts/validate_playbooks.py
```

## Closeout

Report whether Experience docs, schema/example pairs, or Agon adoption
transferred-path references changed.
