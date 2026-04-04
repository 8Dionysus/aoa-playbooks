# Playbook Harvest and Reanchor

This note lands the recurrence posture from `docs/PLAYBOOK_RECURRENCE_DISCIPLINE.md`.
It stays scenario-owned and does not replace that doctrine.

## Core rule

Harvest is evidence-first selection. Reanchor is governed return to a named anchor.
reanchor is not retry.

## What harvest is

Harvest keeps reviewable evidence for later reviewable movement.
It names the repeatable cases that are worth carrying forward.

## What harvest is not

Harvest is not runtime state.
Harvest is not a persisted run ledger.
Harvest is not a shortcut around boundary review.

## What reanchor is

Reanchor returns a route to a valid anchor after drift or boundary loss.
It is explicit, bounded, and tied to a named anchor.

## What reanchor is not

reanchor is not retry.
Reanchor is not vague continuity.
Reanchor is not permission to widen scope until the route feels stable.

## Harvest thresholds

- If a route has no valid anchor, do not harvest it.
- If a route loses anchor integrity twice, stop rather than simulate continuity.
- Only repeated, reviewable evidence may become a harvest candidate.

## Valid anchor classes

- artifact anchors
- checkpoint anchors
- review anchors

## Named promotion destinations

- `docs/real-runs/` for reviewed summaries
- `docs/gate-reviews/` for gate-review notes

## Installed quest-harvest posture

`aoa-quest-harvest` may assist this repo only after a reviewed run, closure, or pause.

- it is not used inside an active route
- it does not define orchestrator identity
- it does not replace playbook route canon, memo writeback, or eval proof
- one anecdotal repeat is not enough to promote a route outcome

Its allowed verdicts are:

- `keep/open quest`
- `promote to skill`
- `promote to playbook`
- `promote to orchestrator surface`
- `promote to proof surface`
- `promote to memo surface`

## Anti-patterns

- treating reanchor as retry
- promoting harvest into runtime state
- hiding drift with repeated continuity claims

## Manual-first pilot outcome

- The March 31 manual-first questbook pilot produced one reviewed source/proof lane across `aoa-techniques`, `aoa-skills`, and `aoa-evals`.
- That is enough to keep the harvest boundary explicit, but not enough recurrence to promote a reviewed summary or gate-review adjunct honestly.
- `AOA-PB-Q-0002` therefore reanchors here until a second reviewed lane shows the same harvest destination without turning playbooks into a run ledger.
