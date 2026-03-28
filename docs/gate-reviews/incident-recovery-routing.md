# incident-recovery-routing gate review

## Gate Header

- Owning playbook: `AOA-P-0020 incident-recovery-routing`
- Verdict surface: `docs/gate-reviews/incident-recovery-routing.md`

## Minimum Evidence Threshold

- One real incident recovery run with `incident_map`, `stabilization_plan`, `recovery_decision`, `recovery_verification_pack`, and `handoff_record`

## Latest Reviewed Run

- No reviewed run is harvested yet.
- Only a live incident should open the first reviewed summary at `docs/real-runs/YYYY-MM-DD.incident-recovery-routing.md`.

## Dual Signal Check

- Stable failure or follow-up mapping not already covered by neighboring recovery or remediation playbooks or the shared failure catalog: not yet demonstrated
- Stable adjunct candidate in the form of a `handoff bridge`, `subagent split`, or `automation seed`: not yet demonstrated

## Current Verdict

- `hold`

## Next Trigger

- Re-open this gate only after a live incident yields a reviewed summary and the dual-signal rule can be checked against real recovery evidence.
