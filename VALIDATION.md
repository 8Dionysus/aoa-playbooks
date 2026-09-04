# Validation routes

Run only the route relevant to the changed playbook surface.

## Repository checks

```bash
python scripts/validate_playbooks.py
python -m pytest -q tests
```

## Decisions and evals

Use the dedicated decision lane below for decision checks.

The local eval procedure is owned by [evals/VALIDATION.md](evals/VALIDATION.md).

## Stats

Both stats procedures are owned by [stats/VALIDATION.md](stats/VALIDATION.md).

## Mechanics

Run the common mechanics routes here, then the nearest package route.

```bash
python scripts/validate_mechanics_skeleton.py
python scripts/validate_root_design.py
```

Run `generate_decision_indexes.py --check` through the [Decision lane](VALIDATION.md#decision-lane). Run `validate_playbooks.py` through [Repository checks](VALIDATION.md#repository-checks).

```bash
python scripts/release_check.py
```

## Decision lane

```bash
python scripts/generate_decision_indexes.py --check
git diff --check
```

When authored decision metadata changed and regeneration is explicitly in
scope, refresh the derived indexes before running the check form:

```bash
python scripts/generate_decision_indexes.py
```

## Artifact-bundle identity

When the playbook registry, generated readout, or artifact-bundle identity
changes, run the owner-local bundle validator:

```bash
python scripts/validate_abyss_machine_playbook_bundle.py
```
