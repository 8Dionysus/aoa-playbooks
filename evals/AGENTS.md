# AGENTS.md

## Applies to

This card applies to `aoa-playbooks/evals/` and every file below it.

## Role

This skeleton port captures playbook-layer eval pressure before it is accepted,
rejected, or normalized by `aoa-evals`.

`aoa-evals` owns central verdict, scoring, regression, and proof doctrine
authority. This port owns only playbook-local intake, cases, fixtures, suites,
reports, and source refs.

## Route by task

Start from `PORT.yaml` and the exact intake, suite, report, or fixture being
changed. Use `README.md` for human port topology or empty-state conventions.
For central proof adoption, use the local-port standard owned by `aoa-evals`.

## Boundaries

- Keep playbook bundles, scenario composition, handoff posture, and run
  choreography in `aoa-playbooks`.
- Keep proof doctrine, verdicts, scoring, and regression authority in
  `aoa-evals`.
- Do not treat an intake packet as proof acceptance or a central eval verdict.
- Do not place private traces, secrets, or unreduced operator evidence here.

## Validation

Run `VALIDATION.md` in this directory on demand.

## Closeout

Report changed eval surfaces, current `PORT.yaml` status, validation run, any
skipped central proof adoption, and the next route into `aoa-evals` when needed.
