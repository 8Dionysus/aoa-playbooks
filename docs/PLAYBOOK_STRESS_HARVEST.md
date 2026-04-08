# PLAYBOOK STRESS HARVEST

## Goal

Make recurring stressed runs leave behind enough usable structure to improve the next run.

A playbook stress lane is only antifragile if it produces harvestable evidence and a reviewable gate for what happens next.

## Harvest pattern

Use the smallest loop that still leaves durable structure:

1. detect the stressed branch
2. bound the route
3. hand off or degrade explicitly
4. harvest evidence
5. decide re-entry or hold
6. open adaptation work only if repetition or impact justifies it

## Inputs worth harvesting

Prefer bounded artifacts such as:

- source-owned stressor or degradation receipts
- stress handoff envelopes
- runtime closeout receipts
- eval reports
- reviewer notes that cite the evidence

Avoid turning broad anecdotes into the main playbook record.

## Where the harvest can land

Depending on the live repo shape, a stressed run may feed:

- `docs/real-runs/`
- `docs/gate-reviews/`
- `examples/harvests/`
- playbook-owned generated review surfaces

Wave 3 only needs the doctrine and one additive contract family.
It does not require a full new pipeline.

## Re-entry discipline

A re-entry gate should be able to say one of the following:

- `resume`
- `resume_degraded`
- `hold`
- `retire_route`

That decision should cite evidence, not mood.

## Guardrails

- do not harvest every minor wobble into a giant postmortem
- do not let playbook harvest become the only record of what happened
- do not reopen a route without explicit checks
- do not keep degraded mode alive by inertia when the route should be held or retired

## Acceptance shape

A healthy wave-3 landing would make it possible to point to:

- one documented harvest loop for stressed playbook runs
- one machine-readable re-entry gate family
- one example where the route resumes only with explicit evidence
