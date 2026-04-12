# Reviewed Automation Followthrough

Playbook: `reviewed-automation-followthrough`

Use when a reviewed route already makes automation a serious candidate, but
the next honest move is still one playbook-seed decision plus one reviewed
real-run note.

Suggested seed:

- start from `closeout_followthrough_decision` and the current `automation_candidate_packet`
- use `aoa-automation-opportunity-scan` and `aoa-session-route-forks` to decide whether a playbook-seed candidate is honest now or should defer
- keep `aoa-approval-gate-check`, rollback notes, and one real-run review note explicit before any broader automation claim

This example is illustrative only.
It is not a live schedule and it is not yet a composition-owned automation
seed.
