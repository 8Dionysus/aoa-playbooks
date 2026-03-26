# Playbook Layer Boundaries

This document records the most important ownership boundaries for `aoa-playbooks`.

## Rule 1: playbook owns scenario composition, not everything the scenario touches

`aoa-playbooks` should own playbook-layer meaning such as:
- playbook profiles
- scenario contracts
- trigger posture
- participating role patterns
- required skill-family composition hints
- fallback posture
- expected artifact posture

It should not become the default dumping ground for everything a scenario might use.

## Rule 2: playbook is not skill

A playbook may compose skills.
That does not make the playbook profile itself a skill bundle.

Reusable execution still belongs to `aoa-skills`.

## Rule 3: playbook is not proof

A playbook may require eval posture.
That does not make the playbook profile itself a proof object.

Bounded proof still belongs to `aoa-evals`.

## Rule 4: playbook is not memory

A playbook may specify memory posture.
That does not make the playbook layer the owner of memory objects or recall truth.

Memory still belongs to `aoa-memo`.

## Rule 5: playbook is not routing

A playbook may rely on routing.
That does not make the playbook layer the owner of cross-repo dispatch.

Navigation still belongs to `aoa-routing`.

## Rule 6: fallback matters

A playbook should make clear what happens when the scenario drifts, fails, becomes risky, or needs review.
That posture should not stay implicit.

## Rule 7: keep playbooks reviewable

If playbooks become giant nonlinear orchestration scripts or folklore archives, the layer will stop being trustworthy.
Compactness and explicit posture matter.

## Rule 8: scenario-level method belongs here, not everywhere at once

When a recurring route spans techniques, skills, roles, memory posture, and proof posture, the playbook layer should own that route as scenario-level method.

That should not be used as an excuse to absorb the source meaning of those neighboring layers.

## Rule 9: recurrence belongs here only as scenario composition

`aoa-playbooks` may own scenario-level return posture.
It may name anchors and re-entry modes for a recurring route.
It must not absorb runtime state-machine logic, artifact-schema ownership, or stack wrapper behavior.

## Rule 10: authored playbook bundles own route wording, not neighboring layer truth

When `aoa-playbooks` publishes a `PLAYBOOK.md`, that bundle becomes the source of truth for the scenario route itself:
- trigger boundary
- decision points
- handoffs
- fallback posture
- expected evidence posture

It does not become the source of truth for:
- technique meaning
- skill meaning
- eval doctrine
- memory-object taxonomy

## Compact rule

`aoa-playbooks` should help AoA name its recurring scenarios without letting the scenario layer blur every other layer.
