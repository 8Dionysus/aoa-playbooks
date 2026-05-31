# Head-Fed Mechanics Roster

This roster names common AoA mechanics that begin in `Agents-of-Abyss` and may
land owner-local forms in `aoa-playbooks`.

It is a skeleton. It does not claim these mechanics are operational inside
`aoa-playbooks` yet.

## Operating Card

| Field | Route |
| --- | --- |
| role | roster for center-fed mechanics that can pressure the playbook layer |
| input | center mechanic, owner request, cross-repo route pressure, or sibling-owner handoff |
| output | playbook-local package candidate, source route, deferred owner request, or stronger-owner handoff |
| owner | `Agents-of-Abyss/mechanics/` for center law; `aoa-playbooks/mechanics/` only for playbook-local operation routes |
| next route | `mechanics/LOCAL_MECHANICS.md`, target playbook source, generated builder, decision record, or sibling owner |
| validation | `python scripts/validate_mechanics_skeleton.py` |

## Acceptance Rule

A head-fed mechanic can become a playbook-local child package only when it has:

- a center route in `Agents-of-Abyss/mechanics/`;
- a playbook-local operation that repeats;
- a source surface or generated builder this repo owns;
- a stronger-owner split;
- explicit stop-lines;
- local validation.

Until then, it remains a roster row, not an active package.

## Candidate Roster

| Candidate | Center pressure | Playbook-local possible route | Current status |
| --- | --- | --- | --- |
| `agon` | trial, campaign, arena, and pre-protocol pressure | Agon trial and campaign choreography surfaces without live arena authority | package-active |
| `antifragility` | stress, degraded lane, pruning, and negative checks | stress lanes, re-entry gates, bounded failure harvest, runtime-chaos wave posture, and via negativa checklist | package-active |
| `audit` | evidence, risk, visibility, and owner handoff | audit-shaped playbook review or closeout surfaces without proof verdicts | candidate-only |
| `boundary-bridge` | cross-owner seam and handoff pressure | playbook-to-skill/eval/memo/agent handoff contracts without ownership transfer | candidate-only |
| `checkpoint` | checkpoint, bridge, return, and export pressure | checkpoint-return and reviewed-closeout scenario posture | package-active |
| `distillation` | heavy source to active form | session/route distillation into candidate playbook routes without memory truth | candidate-only |
| `experience` | adoption, certification, office, service, and governance pressure | Experience certification, adoption, retention, office, and governance playbooks | package-active |
| `growth-cycle` | reviewed growth route, harvest, owner followthrough | session growth and owner followthrough playbook routes | candidate-only |
| `method-growth` | candidate, seed, proof, method, memory, and owner landing movement | playbook route incubation and promotion discipline | candidate-only |
| `questbook` | public obligations and quest-readable follow-through | questline/campaign adjunct posture without becoming quest authority | package-active |
| `recurrence` | return, reanchor, and relaunch pressure | recurrence, return posture, and re-entry gates inside scenarios | package-active |
| `release-support` | publication, release, support, rollback, and claim transition | release-prep, rollout, retention, and post-release playbook routes | package-active |
| `rpg` | progression, campaign, quest, role, and feat vocabulary | RPG vocabulary as bounded playbook reflection only | package-active |
| `titan` | Titan role-bearing, drill, roster, and service pressure | Titan drill and route ecology playbooks without role authority | package-active |

## Stop Lines

- Head-fed does not mean center-owned operational truth inside this repo.
- A roster row is not owner acceptance.
- Playbook-local landing does not move sibling truth into `aoa-playbooks`.
- Center vocabulary does not authorize runtime execution, proof verdicts,
  memory writes, route dispatch, role rights, or KAG promotion.

## Next Route

When one candidate becomes ready, add a child package in a focused slice:

1. create `mechanics/<slug>/` from `PACKAGE_TEMPLATE.md`;
2. add a decision if topology or owner split changes;
3. add package-specific validation;
4. keep source playbook truth in `playbooks/` unless a later part-local
   contract proves otherwise.
