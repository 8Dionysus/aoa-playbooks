# AGENTS.md

## Applies to

This card applies to `memo/`.

## Role

`memo/` is the aoa-playbooks local memory port. It holds scenario-layer memory
candidates, receipts, exports, and local notes before reviewed landing in
`aoa-memo`.

## Route by task

- Local candidate or packet: start from `PORT.yaml` and the exact target
  directory.
- Human port orientation: use `memo/README.md`.
- Direction or lifecycle change: use `ROADMAP.md`.
- Central landing: use the current `aoa-memo` operation contract.

## Boundaries

Use this port for `write_candidate_only` work. Keep playbook truth in playbook
source surfaces; use this port for recall, candidate memory, receipts, and
reviewed handoff.

Use `PORT.yaml` for the local port contract and `INDEX.md` / `index.min.json`
as generated read models. Use `candidates/` for proposed memory, `receipts/`
for review or handoff traces, `exports/` for packets meant for `aoa-memo`, and
`local/` for playbook-layer memory that stays local for now.

## Candidate Route

Create scenario-layer candidates through the stack MCP helper:

Run `VALIDATION.md#candidate-creation` in this directory when deliberately creating a reviewed candidate.

Then validate the emitted candidate path:

Run `VALIDATION.md#candidate-validation` in this directory on demand.

## Reviewed Landing Route

Run `VALIDATION.md#pending-exports-and-landing-plan` in this directory on demand.

`landing-plan` is an access-plane check. Durable memory lands only in
`aoa-memo` through reviewed intake, generated read models, validators, and
review.

## Validation

Run `VALIDATION.md#local-memo-port` in this directory on demand.

For repo-wide release posture, use the root `AGENTS.md` validation route.

## Closeout

Report candidate path, evidence refs, validation result, and whether the item
stayed local, was exported for reviewed intake, or was landed in `aoa-memo`.
