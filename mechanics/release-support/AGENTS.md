# AGENTS.md

## Applies to

This card applies to `mechanics/release-support/`.

## Role

`release-support/` is the head-fed and local mechanic for release, deployment,
installation, rollback, promotion, retention, and publication-support posture.

The root release command and release docs stay operator-facing public routes.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/README.md`,
this package `README.md`, `docs/RELEASING.md`, and `scripts/release_check.py`.

## Boundaries

- Do not move `scripts/release_check.py` out of root command space.
- Do not claim GitHub/CI authority, runtime deployment authority, or support
  desk process ownership.
- Do not move release schemas/examples without updating release tests and
  package-local provenance.

## Validation

```bash
python mechanics/release-support/scripts/validate_release_support_package.py
python scripts/release_check.py
```

## Closeout

Report whether release docs, root release commands, or release contract pairs
changed.
