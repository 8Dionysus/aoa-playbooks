# AGENTS.md

## Applies to

This card applies to `mechanics/release-support/`.

## Role

`release-support/` is the `head-fed/local` mechanic for release, deployment,
installation, rollback, promotion, retention, and publication-support posture.

The root release command and release docs stay operator-facing public routes.

## Route by task

- Repository release law or command: use `docs/RELEASING.md` and
  `scripts/release_check.py`.
- Package-local contract: use the exact doc, schema, example, and focused test.
- Package topology or provenance: use `README.md`.

## Boundaries

- Do not move `scripts/release_check.py` out of root command space.
- Do not claim GitHub/CI authority, runtime deployment authority, or support
  desk process ownership.
- Do not move release schemas/examples without updating release tests and
  package-local provenance.

## Validation

Run `VALIDATION.md` in this directory, then the common mechanics route in the root `VALIDATION.md`.

## Closeout

Report whether release docs, root release commands, or release contract pairs
changed.
