# Agon Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | head-fed/local |
| role | keep pre-protocol Agon trial, kernel-binding, campaign, adoption, and recurrence-adapter playbook payloads bounded and reviewable |
| trigger | Agon trial/campaign seed change, registry drift, kernel-binding change, adoption-run contract change, or recurrence adapter update |
| playbooks owns | pre-protocol choreography, playbook-local registry seeds, schemas/examples, builder implementations, and stop-line docs |
| stronger owner split | `Agents-of-Abyss` owns center Agon law; live arena protocol, scars, rank, retention, KAG promotion, proof, memory, routing, and role authority stay with stronger owners |
| inputs | package configs, schemas, examples, docs, source playbooks, quest notes, package recurrence manifests, and generated Agon registries |
| outputs | root generated Agon registries, validated pre-protocol playbook surfaces, and explicit stronger-owner stop lines |
| must not claim | live arena authority, verdicts, scars, rank/trust mutation, retention execution, hidden scheduling, KAG/ToS promotion, or assistant contestant authority |
| validation | `python mechanics/agon/scripts/validate_agon_package.py` plus the Agon root compatibility builder/validator commands |
| next route | target part, `playbooks/agon/*/agon-*/PLAYBOOK.md`, `quests/`, package recurrence manifest, generated registry, or stronger owner repo |

## Active route

The active payloads live under package parts:

- `parts/trial-playbooks/`
- `parts/trial-kernel-bindings/`
- `parts/campaign-playbooks/`
- `parts/adoption/`
- `parts/recurrence-adapter/`

Root Agon builder and validator commands in `scripts/` are compatibility
wrappers. Root generated registries remain public read models.

## Functioning parts

- `trial-playbooks`: Wave VI trial playbook seeds, schemas, examples, docs,
  builder, and validator.
- `trial-kernel-bindings`: Wave XIII trial-kernel binding seed, schemas,
  example, builder, and validator.
- `campaign-playbooks`: Wave XVI campaign playbook seed, schemas, example,
  docs, builder, and validator.
- `adoption`: agonic adoption playbook doc, schema, and example.
- `recurrence-adapter`: Agon recurrence adapter doc plus package-local
  recurrence manifests and hook manifests.

## Source surfaces

- `mechanics/agon/parts/**`
- root `playbooks/agon/*/agon-*/PLAYBOOK.md`
- root `quests/AOP-Q-AGON-*`
- package `parts/*/manifests/component.agon*.json`
- root `generated/agon_*_registry.min.json`
- root compatibility scripts under `scripts/`

## Owner boundary

This package owns pre-protocol playbook mechanics. It does not own center Agon
law, live arena execution, proof verdicts, scars, rank, retention, KAG/ToS
promotion, or assistant contestant status.

## Growth posture

The next safe growth is stronger package-local validation and tighter
manifest/source-ref checks, not widening Agon vocabulary into live protocol.
