# trusted-rollout-operations harvest template

## Run Header

- Run identifier:
- Date:
- Owning playbook: `AOA-P-0028 trusted-rollout-operations`

## Entry Signal

- What bounded shared-root Codex rollout made this governed rollout campaign the honest next route?

## Boundary Summary

- Which trust, doctor, smoke, drift, rollback, stats, and memo boundaries were inside scope?
- Which neighboring playbooks or owner-local routes were explicitly ruled out?

## Required Artifacts

- `rollout_decision`
- `doctor_report_ref`
- `smoke_report_ref`
- `deploy_receipt_ref`
- `drift_window_ref`
- `rollback_window_ref`
- `stats_refresh_ref`
- `memo_writeback_ref`

## Closure Class

- Was the route closed as `stabilized`, `rolled_back`, `abandoned`, `review-stop`, or `safe-stop`?

## Follow-On Route

- If follow-on work remained, which governed route owns it next?

## Composition Signals

- `new failure/follow-up mapping not already covered`:
- `handoff bridge candidate`:
- `automation seed candidate`:
- `gate-review candidate`:
- `insufficient signal`:

## Residual Risk

- What bounded risk remained after closure?
