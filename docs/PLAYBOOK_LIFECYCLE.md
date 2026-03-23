# Playbook Lifecycle Doctrine

This document defines the growth path for the AoA playbook layer.

It exists to keep `aoa-playbooks` from growing by accident.
The repository should only graduate scenario forms when the route is recurring, reviewable, and clearly more than one bounded skill.

## Lifecycle states

Playbook-layer meaning can move through four states:

1. `registry-only`
2. `authored`
3. `activation-surface eligible`
4. `federation-checked`

Each state is a stronger commitment than the one before it.
The goal is not to maximize count.
The goal is to make the smallest durable form that still preserves scenario meaning.

## State meanings

### `registry-only`

Use this state when a scenario is known, but the authored route is still too thin to justify a `PLAYBOOK.md` bundle.

This state should usually carry:
- a stable name
- a compact summary
- trigger and scenario labels
- a small set of expected artifacts

This state should not pretend to own deep handoffs, fallback posture, or cross-layer choreography yet.

### `authored`

Use this state when the route needs a readable source-owned object.

An authored playbook should be chosen when:
- the route spans more than one bounded workflow
- trigger, handoff, and fallback posture need to be reviewable together
- the scenario benefits from explicit evidence expectations
- the playbook body can remain compact without becoming a workflow dump

An authored playbook should not absorb technique, skill, eval, memory, or role truth.

### `activation-surface eligible`

Use this state when a runtime-readable projection is genuinely useful.

This should be reserved for playbooks where:
- the route is already stable as an authored object
- the runtime needs a compact view of the scenario contract
- the projection can stay derived from canonical playbook surfaces
- the activation surface does not introduce new meaning

If the projection would become a second authored route, the playbook is not eligible yet.

### `federation-checked`

Use this state when the playbook is cross-repo honest enough to be checked against neighboring surfaces.

This usually means:
- participating agents resolve in `aoa-agents`
- expected proof posture can be named against `aoa-evals`
- memory posture can be named without taking over `aoa-memo`
- skill families can be named without taking over `aoa-skills`

This state does not require every playbook to touch every neighbor.
It requires the playbook to be honest about the neighbors it does touch.

For the current wave, a federation-checked playbook should expose:
- `required_skills`
- `memo_contract_refs`
- `memo_writeback_targets`

Those fields keep the closure machine-checkable without moving skill canon or memo taxonomy into `aoa-playbooks`.

## Graduation heuristics

Graduate a scenario upward only when the next state removes ambiguity that the previous state could not remove.

Prefer graduation when:
- the same scenario keeps recurring
- the route has explicit trigger and boundary language
- handoffs are stable enough to name
- fallback posture has already become part of the scenario shape
- expected evidence or artifact posture is already recurring

Hold a scenario back when:
- the route is still a one-off
- the scenario is too vague to bound honestly
- the scenario mainly belongs to a skill or an eval
- the route would need hidden orchestration to look complete
- the authored form would become large enough to be unreadable

## Graduation checks

Before promoting a scenario, ask:

1. Is this clearly a recurring scenario rather than a one-run recipe?
2. Does the route span more than one bounded workflow?
3. Can trigger, prerequisites, handoffs, fallback, and evidence posture all stay explicit?
4. Is the playbook still smaller than the neighboring layer objects it coordinates?
5. Would an activation surface be a projection, not a rewrite?
6. Would the scenario still make sense if neighboring surfaces changed independently?
7. Can exact skills, memo refs, and memo writeback kinds be named without inventing new neighboring-layer meaning?

If the answer to any of these is no, keep the playbook in the smaller form.

## Anti-patterns

Avoid these growth failures:
- promoting every workflow into a playbook
- turning authored bundles into giant orchestration scripts
- letting runtime needs rewrite the scenario contract
- using activation surfaces to smuggle new meaning into the layer
- creating playbooks that are just renamed skills

## Practical rule

The smallest honest surface wins.

If a registry row is enough, stop there.
If a readable route is needed, author a `PLAYBOOK.md`.
If runtime readability matters, derive a compact activation surface.
If other AoA layers must validate the route, add federation checks without absorbing their ownership.
