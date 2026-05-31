# Extract Trusted Rollout Operations As AOA-P-0028

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0001
- Original date: 2026-04-11
- Surface classes: playbook source, scenario composition, activation/federation, docs route
- Playbook routes: trusted-rollout-operations, session-growth-cycle
- Mechanic parents: activation, review-gate
- Guard families: scenario boundary, playbook extraction gate, activation/read-model
- Posture: accepted

## Context

The shared-root Codex-plane rollout lane began as a companion route card under
`AOA-P-0025 session-growth-cycle`.

Wave 7 made the boundary mismatch visible:
- the route anchor is rollout, drift, rollback, receipt publication, and
  derived continuity
- the source truth lives in `8Dionysus`
- the route has its own stop-lines, closure classes, and artifact chain
- the route is not primarily about checkpoint carry, reviewed harvest, seed
  staging, proof, or recurring growth closure

Keeping the rollout cycle only as a companion of `AOA-P-0025` now hides a real
scenario boundary and keeps the operational family less honest than it could be.

## Options considered

1. Keep the rollout lane as a permanent companion inside `AOA-P-0025`.
2. Treat it as a generic infra or incident subcase under `AOA-P-0012` or
   `AOA-P-0020`.
3. Extract it as a sovereign operational playbook with its own lifecycle and
   companion route card.

## Decision

Choose option 3.

`trusted-rollout-operations` becomes sovereign `AOA-P-0028`.
The companion note in `docs/CODEX_PLANE_ROLLOUT_CYCLE.md` stays, but it now
points to `AOA-P-0028` rather than hiding inside `AOA-P-0025`.

## Why

- The dominant move is a governed rollout operations cycle, not a growth cycle.
- The closure classes are distinct: `stabilized`, `rolled_back`, `abandoned`.
- The artifact chain is distinct and source-owned by adjacent repos.
- The route is reviewable without turning `aoa-playbooks` into rollout truth.

## Consequences

- `AOA-P-0028` joins the authored activation/federation cohort at
  `A+Act+F`, not composition.
- `AOA-P-0025` narrows back to session growth proper.
- The companion lane remains companion-only and does not become a second
  activation surface.
- Real-run evidence and one reviewed proving run are still required before any
  broader gate or composition claim becomes honest.

## Source Surfaces

- `playbooks/trusted-rollout-operations/PLAYBOOK.md`
- `playbooks/session-growth-cycle/PLAYBOOK.md`
- `docs/CODEX_PLANE_ROLLOUT_CYCLE.md`
- `docs/TRUSTED_ROLLOUT_CAMPAIGN_CADENCE.md`
- `generated/playbook_activation_surfaces.min.json`
- `generated/playbook_federation_surfaces.min.json`

## Follow-Up Route

Future changes to the rollout route should update the authored playbook first,
then any derived activation, federation, review, or composition surfaces.

## Verification

```bash
python scripts/generate_decision_indexes.py --check
python scripts/validate_playbooks.py
```
