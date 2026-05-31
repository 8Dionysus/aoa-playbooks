# validation-driven-remediation harvest template

## Run Header

- Run identifier:
- Date:
- Owning playbook: `AOA-P-0018 validation-driven-remediation`

## Entry Signal

- What exact failing validator, proof surface, or cross-boundary audit finding anchored remediation?

## Boundary Summary

- Which source-owned boundaries were inside scope?
- Which neighboring playbooks were explicitly ruled out?

## Required Artifacts

- `failure_map`
- `boundary_map`
- `remediation_change_set`
- `revalidation_pack`
- `remediation_decision`
- `handoff_record`

## Closure Class

- Was the route closed as merge, handoff, rollback, or review stop?

## Follow-On Route

- If follow-on work remained, which governed route owns it next?

## Composition Signals

- `new failure/follow-up mapping not already covered`:
- `handoff bridge candidate`:
- `subagent split candidate`:
- `automation seed candidate`:
- `insufficient signal`:

## Residual Risk

- What bounded risk remained after closure?
