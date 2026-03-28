# incident-recovery-routing gate review

## Gate Header

- Owning playbook: `AOA-P-0020 incident-recovery-routing`
- Verdict surface: `docs/gate-reviews/incident-recovery-routing.md`

## Minimum Evidence Threshold

- One real incident recovery run with `incident_map`, `stabilization_plan`, `recovery_decision`, `recovery_verification_pack`, and `handoff_record`

## Latest Reviewed Run

- No reviewed run is harvested yet.
- Selection pass completed on March 28, 2026 did not identify a live incident case, so no reviewed summary opened.
- Only a live incident should open the first reviewed summary at `docs/real-runs/YYYY-MM-DD.incident-recovery-routing.md`.

## Dual Signal Check

- Stable failure or follow-up mapping not already covered by neighboring recovery or remediation playbooks or the shared failure catalog: cannot be evaluated until a live incident reviewed summary exists
- Stable adjunct candidate in the form of a `handoff bridge`, `subagent split`, or `automation seed`: cannot be evaluated until a live incident reviewed summary exists

## Current Verdict

- `hold`

## Next Trigger

- Re-open this gate only after a live incident closes with the required anchor artifacts, reviewable evidence links, and a reviewed summary.
