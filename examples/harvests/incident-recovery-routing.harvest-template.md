# incident-recovery-routing harvest template

## Run Header

- Run identifier:
- Date:
- Owning playbook: `AOA-P-0020 incident-recovery-routing`

## Entry Signal

- What exact incident surface triggered the route?

## Boundary Summary

- Which authority surfaces, consumers, and blast-radius boundaries were inside scope?
- Which neighboring playbooks were explicitly ruled out?

## Required Artifacts

- `incident_map`
- `stabilization_plan`
- `recovery_decision`
- `recovery_verification_pack`
- `handoff_record`

## Closure Class

- Was the route closed as `restored`, `degraded-with-handoff`, `rollback-complete`, or `review-stop`?

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
