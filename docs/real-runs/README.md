# Real-Run Reviewed Summaries

This folder is the repo-first home for reviewed summaries of real operational runs.

Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.

## What belongs here

- one short reviewed summary per harvested real run
- explicit artifact presence rather than raw artifacts
- closure class, follow-on route, composition signals, and residual risk
- external evidence pointers through `Evidence Links`

## What does not belong here

- raw logs
- runtime traces
- execution-state packets
- placeholder runs that never happened
- candidate dossiers or rehearsal plans

## Filename rule

Future summary files must use:

- `YYYY-MM-DD.<playbook-slug>.md`

Allowed slug values in this wave:

- `split-wave-cross-repo-rollout`
- `release-migration-cutover`
- `incident-recovery-routing`

## Required headings

Every committed summary file must contain:

- `Run Header`
- `Entry Signal`
- `Boundary Summary`
- `Required Artifacts`
- `Closure Class`
- `Follow-On Route`
- `Composition Signals`
- `Residual Risk`
- `Evidence Links`

## Current posture

This folder should stay sparse and hold only committed reviewed summaries that fully qualify under the workflow and validator rules.
`docs/real-runs/2026-03-21.split-wave-cross-repo-rollout.md` is the first committed reviewed summary and captures the March 21, 2026 `AOA-P-0017` section-expand wave across source-owned AoA repos and `aoa-routing`.
`AOA-P-0019` and `AOA-P-0020` still have no qualifying reviewed summary committed as of March 28, 2026.
