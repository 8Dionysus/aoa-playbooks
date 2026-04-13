# Decision: Keep The Reviewed Closeout Route Candidate In Incubation

## Context

Reviewed closeout for
`session:2026-04-13T17-04-26-415462Z-aoa-memo-checkpoint-growth-97a0427d-db7`
preserved `candidate:route:aoa-playbooks-playbook-registry-min` as a
playbook-shaped survivor.

The surviving route has:

- cluster ref:
  `cluster:route:candidate-route-aoa-playbooks-playbook-registry-min`
- owner shape:
  `playbook`
- status posture:
  `reanchor`
- next decision class:
  `reanchor_owner`
- nearest wrong target:
  `aoa-skills`

The route is real enough to deserve a tracked owner-local home.
It is not yet honest enough to mint a new playbook or questline artifact from
one session alone.

## Options considered

1. Extract a new playbook immediately.
2. Push the survivor directly into quest continuity now.
3. Keep one explicit incubation decision in `aoa-playbooks` until a second
   reviewed route proves that the recurring shape is real.

## Decision

Choose option 3.

Keep this route candidate visible and owner-local, but incubated.
Do not extract a new playbook yet.

## Why

- the survivor is route-shaped, not skill-shaped, so `aoa-playbooks` is the
  right owner to hold it
- one reviewed closeout is enough to track the route, not enough to canonize it
- immediate extraction would overstate recurrence and make the repo noisier
  than the evidence warrants

## Consequences

- the route no longer lives only inside closeout carry or chat memory
- later review can explicitly decide whether it should:
  - merge into an existing playbook family
  - become a new playbook
  - remain incubated
  - be dropped as false recurrence
- the next honest trigger for reopening this decision is a second materially
  different reviewed route that pressures the same route shape
