# AGENTS.md

## Applies to

This card applies to `mechanics/recurrence/`.

## Role

`recurrence/` is the head-fed and local mechanic for playbook-layer return
choreography: recurrence discipline, component refresh, observation producers,
and review-decision closure.

It validates package-local recurrence docs and manifests. Source playbooks stay
under `playbooks/`.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/PLACEMENT_AUDIT.md`,
this package `README.md`, and `mechanics/recurrence/parts/recurrence-discipline/docs/playbook-recurrence-discipline.md`.

## Boundaries

- Do not move source playbooks out of `playbooks/`.
- Do not claim memory checkpoint truth, route dispatch, runtime self-healing,
  or hidden scheduler authority.
- Do not move package-local recurrence manifests again without a new
  compatibility decision.

## Validation

```bash
python mechanics/recurrence/scripts/validate_recurrence_package.py
python scripts/validate_playbooks.py
```

## Closeout

Report whether recurrence docs, manifests, or source playbooks changed and
whether the package-local reason still holds.
