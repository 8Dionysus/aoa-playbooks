# AOA-PB-D-0018 Spark And Legacy Scaffolding Retirement

## Index Metadata

- Decision ID: AOA-PB-D-0018
- Original date: 2026-09-04
- Surface classes: agent route, mechanics/topology, docs/route-law, scripts/validation, legacy/provenance
- Companion layers: docs, scripts, tests, agent-lane
- Playbook routes: mechanics/topology, agent route, docs/route-law
- Mechanic parents: activation, agon, antifragility, boundary-bridge, federation-closure, review-gate, scenario-composition
- Guard families: owner boundary, source/history preservation, validator restraint
- Posture: accepted retirement record; current active routes remain authoritative

## Decision

Retire all listed Spark and legacy scaffolding roots from the current owner
surface. Historical bytes remain recoverable in git; this note records
immutable baseline links and does not recreate compatibility stubs. Active
validators and route maps must describe only current package surfaces.

## Baseline historical links

Baseline commit: [`fd115480f5eb26ce692cf666d15b7b71835fafda`](https://github.com/8Dionysus/aoa-playbooks/commit/fd115480f5eb26ce692cf666d15b7b71835fafda).

| Retired root | Baseline tree | Full historical tree link |
| --- | --- | --- |
| `Spark/` | `d3894477850ef5dccae4b386c810ecd559c4f0fd` | [tree](https://github.com/8Dionysus/aoa-playbooks/tree/fd115480f5eb26ce692cf666d15b7b71835fafda/Spark) |
| `mechanics/activation/legacy/` | `1417bad2199186bbdfdc332a81e3ab0ce0fd1085` | [tree](https://github.com/8Dionysus/aoa-playbooks/tree/fd115480f5eb26ce692cf666d15b7b71835fafda/mechanics/activation/legacy) |
| `mechanics/agon/legacy/` | `7605dec292c326262031cdcf62744713f3177dab` | [tree](https://github.com/8Dionysus/aoa-playbooks/tree/fd115480f5eb26ce692cf666d15b7b71835fafda/mechanics/agon/legacy) |
| `mechanics/antifragility/legacy/` | `8171f2e4254380877f443c99b5dad18ed9ec4a28` | [tree](https://github.com/8Dionysus/aoa-playbooks/tree/fd115480f5eb26ce692cf666d15b7b71835fafda/mechanics/antifragility/legacy) |
| `mechanics/boundary-bridge/legacy/` | `07e4edaf4bde9a794c45c8b3323eea56dc4f3e3e` | [tree](https://github.com/8Dionysus/aoa-playbooks/tree/fd115480f5eb26ce692cf666d15b7b71835fafda/mechanics/boundary-bridge/legacy) |
| `mechanics/federation-closure/legacy/` | `bf73ed021b9419aaedbc4c9287e2f37101765f20` | [tree](https://github.com/8Dionysus/aoa-playbooks/tree/fd115480f5eb26ce692cf666d15b7b71835fafda/mechanics/federation-closure/legacy) |
| `mechanics/review-gate/legacy/` | `da139bc9b0689bb704f613d151d84d29a9398da2` | [tree](https://github.com/8Dionysus/aoa-playbooks/tree/fd115480f5eb26ce692cf666d15b7b71835fafda/mechanics/review-gate/legacy) |
| `mechanics/scenario-composition/legacy/` | `3cf75460fd33c84aed9da71be2194f74a9afacd1` | [tree](https://github.com/8Dionysus/aoa-playbooks/tree/fd115480f5eb26ce692cf666d15b7b71835fafda/mechanics/scenario-composition/legacy) |

Each root is retired because it is archive-only scaffolding with no current
owner route. Recovery is by the immutable commit/tree links above or the
exact path/blob inventory in `surface-retirement-20260904/baseline.json`.

## Consequences

No runtime, memo, `.aoa`, remote, tag, or merge state is changed by this record. Generated indexes are read models and must be regenerated from this authored note. Playbook composition remains current; retired legacy scaffolding is not an active route.
