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

## Anti-patterns

- treating reanchor as retry
- promoting harvest into runtime state
- hiding drift with repeated continuity claims
