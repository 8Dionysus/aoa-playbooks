# AGENTS.md

## Applies to

Everything under `stats/` in `aoa-playbooks`.

## Role

This directory owns playbook-local statistical questions, their embedded
measurement contracts, and evidence-linked reference packets. Shared
statistical grammar and cross-owner composition remain owned by `aoa-stats`.

## Route by task

- Question or measurement meaning: `stats/port.manifest.json`.
- Human port orientation: `stats/README.md`.
- Reference-packet refresh: `generated/playbook_review_status.min.json` and
  its owner builder and schema under
  `mechanics/review-gate/parts/review-status/`.
- Shared grammar or packet compatibility: the central contracts under
  `aoa-stats/stats/`.
- Owner-boundary change: `DESIGN.md`.

## Boundaries

- `port.manifest.json` owns the playbook-local question and measurement
  meaning.
- Reference packets are derived snapshots and remain weaker than the
  review-status source chain.
- Reviewed-run reference coverage reports whether a current gate-reviewed
  playbook entry references at least one reviewed run. It does not report run
  quality, proof, an eval verdict, readiness, gate acceptance, execution
  success, runtime state, or a scenario decision.
- Keep packet refs repository-relative and raw reviewed-run content out of
  packets.

## Validation

Inspect the owner read model first:

Run the stats route in `VALIDATION.md` on demand.

Then validate the port and its packet with the central contract owner:

Run the stats route in `VALIDATION.md` on demand.

## Closeout

Report the question or contract changed, the owner evidence inspected, whether
the reference packet was refreshed, and which validation route ran.
