# Experience Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | head-fed/local |
| role | keep adoption, certification, service, office, retention, rollback, and governance playbook posture explicit |
| trigger | Experience Wave 3 contract changes, adoption/certification route changes, service/watch route changes, or office/governance posture changes |
| playbooks owns | playbook-layer adoption and service choreography plus package-local contract pairs |
| stronger owner split | `aoa-agents` owns agent roles and service identity; `aoa-evals` owns proof; runtime owners own live service operation |
| inputs | Experience docs, schemas, examples, tests, and source playbooks |
| outputs | checked package-local Experience posture and stronger-owner handoff |
| must not claim | role authority, service runtime, proof verdict, memory truth, or Tree of Sophia promotion |
| validation | package executable owners; focused order in `AGENTS.md` |
| next route | Experience part doc/schema/example, Agon adoption part, source playbook, or stronger owner repo |

## Active route

This package is active as package-local Experience posture.

Experience docs, schemas, and examples are package-local contract pairs under
`mechanics/experience/parts/`. Current tests and readouts consume those package
paths directly. The Agonic trial adoption contract has moved to
`mechanics/agon/parts/adoption/` and is treated as a transferred Agon payload.

## Source surfaces

- adoption, certification, office, service, governance, watch, rollback, and
  dossier docs under `mechanics/experience/parts/*/docs/`
- Wave 3 contract schemas under `mechanics/experience/parts/*/schemas/`
- Wave 3 examples under `mechanics/experience/parts/*/examples/`
- Agonic trial adoption schema/example under `mechanics/agon/parts/adoption/`

## Growth posture

Future Experience growth should add narrower part validators and compatibility
maps around the package-local contract pairs.
