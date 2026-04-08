# PLAYBOOK STRESS LANES

## Goal

Teach recurring playbooks to expose what happens when the normal route becomes unsafe, under-evidenced, or derived-surface dependent.

A playbook should not become vague precisely when stress arrives.
It should show the narrower lane.

## Why `aoa-playbooks` owns this

`aoa-playbooks` owns recurring operational scenarios, multi-step composition, handoffs, fallback posture, and evidence expectations.

A stress lane belongs here because it coordinates multiple surfaces:

- agent posture
- bounded skills
- source evidence
- runtime checks
- return or re-entry posture

## Additive shape

Prefer additive playbook-owned surfaces such as:

- `schemas/playbook_stress_lane_v1.json`
- `schemas/playbook_reentry_gate_v1.json`
- matching examples

These may later inform generated families like:

- `generated/playbook_handoff_contracts.json`
- `generated/playbook_failure_catalog.json`
- `generated/playbook_composition_manifest.json`

Wave 3 does not require a generator rewrite.

## What a good stress lane names

A recurring playbook should be able to answer:

1. what activates the stress lane
2. what stop conditions block the normal route
3. what degraded lane remains valid
4. which handoff targets are expected
5. what evidence must be harvested
6. what gate allows re-entry, if any

## Scenario discipline

Stress lanes should remain:

- bounded
- reviewable
- weaker than the normal lane
- explicit about evidence
- explicit about re-entry or retirement

A stress lane is not a secret second playbook.
It is a named branch of the same recurring scenario.

## Guardrails

- do not let playbooks replace source-owned receipts
- do not hide a broad mutation path inside a so-called degraded lane
- do not create one stress lane per noisy incident if the route is not truly recurring
- do not skip re-entry conditions when the playbook expects the route to resume later
- do not confuse scenario composition with proof or source meaning

## Acceptance shape

A healthy wave-3 landing would make it possible to point to:

- one machine-readable stress-lane family
- one recurring route with explicit stop conditions and a degraded lane
- one documented evidence-harvest expectation
- one documented re-entry gate for resuming or holding the route
