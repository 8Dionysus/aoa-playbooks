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
- `validation-driven-remediation`
- `release-migration-cutover`
- `incident-recovery-routing`
- `owner-first-capability-landing`
- `closeout-owner-follow-through-continuity`
- `federated-live-publisher-activation`

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
`docs/real-runs/2026-04-07.split-wave-cross-repo-rollout.md` is the latest committed reviewed summary for `AOA-P-0017` and captures the surface-detection second-wave bridge from sibling surface publication through downstream validation, review-tail repair, merge, and merged-reality sync.
`docs/real-runs/2026-04-05.validation-driven-remediation.md` is the first committed general reviewed summary for `AOA-P-0018` and keeps the playbook at `hold` pending a second different-family remediation run or a stable adjunct candidate.
`docs/real-runs/2026-04-07.owner-first-capability-landing.md` is the first committed reviewed summary for `AOA-P-0021` and closes the federated audit remediation pack as a composition-landed owner-first route rather than leaving it as staged lineage fiction.
`docs/real-runs/2026-04-08.owner-first-capability-landing.md` is the latest committed reviewed summary for `AOA-P-0021` and confirms that the same owner-first bridge also governs the via-negativa doctrine/checklist wave from staged lineage to merged owner truth.
`docs/real-runs/2026-04-08.closeout-owner-follow-through-continuity.md` is the first committed reviewed summary for `AOA-P-0023` and closes the diagnostic-spine follow-through route as a composition-landed continuity bridge from reviewed closeout to merged owner truth.
`docs/real-runs/2026-04-07.federated-live-publisher-activation.md` is the first committed reviewed summary for `AOA-P-0024` and closes the owner-local publisher readiness route at the audit layer while keeping the gate at `hold` until a stable playbook-owned adjunct candidate appears.
`AOA-P-0019` and `AOA-P-0020` still have no qualifying reviewed summary committed as of April 8, 2026.
