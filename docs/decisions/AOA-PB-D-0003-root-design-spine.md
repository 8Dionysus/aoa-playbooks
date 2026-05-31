# Add Root Design Spine Before Mechanics Split

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0003
- Original date: 2026-05-31
- Surface classes: root/topology, agent route, docs route, validation guard, decision record
- Playbook routes: none
- Mechanic parents: cross-mechanic
- Guard families: source topology, AGENTS/mesh, decision index/read-model, validation guard
- Posture: accepted root design spine

## Context

`aoa-playbooks` had a clear charter, root `AGENTS.md`, authored playbook canon,
generated readers, and a newly canonicalized decision lane.

It did not yet have root `DESIGN.md` and `DESIGN.AGENTS.md` surfaces like the
already-refactored sibling AoA repositories.

That gap matters before the next topology move:

- `mechanics/` needs a system-level reason to exist before packages are moved
  into it;
- `playbooks/` needs to remain visibly source-authored playbook canon rather
  than a catch-all operational directory;
- agent-facing route cards need a design form separate from the operational
  root `AGENTS.md`;
- future agents need positive route maps instead of a growing pile of
  prohibitions.

## Options Considered

1. Create `mechanics/` first and backfill design after files move.
2. Keep using `AGENTS.md`, `README.md`, and `docs/BOUNDARIES.md` without a
   root design spine.
3. Add `DESIGN.md` and `DESIGN.AGENTS.md` first, then let that spine guide the
   later mechanics and playbooks split.

## Decision

Choose option 3.

Add root design surfaces before the mechanics split:

- `DESIGN.md` owns the system form of the playbook layer;
- `DESIGN.AGENTS.md` owns the design form of the agent-facing route mesh;
- validators and root entrypoints must know these surfaces are live;
- `mechanics/` remains a follow-up topology move, not part of this decision's
  landing.

## Rationale

This preserves the order of authority.

The design spine says what kind of organ `aoa-playbooks` is before new
districts are created. It gives future mechanics work a positive map:
repeatable operation topology belongs in mechanics, source-authored recurring
scenario meaning remains in playbooks, and generated readers remain derived.

It also keeps agent guidance bounded. `DESIGN.AGENTS.md` can describe how route
cards should behave without bloating root `AGENTS.md` or pretending that
agent-facing guidance is playbook source truth.

## Consequences

- Positive: future `mechanics/` work has a root design contract before file
  movement starts.
- Positive: root entrypoints can route design and route-law changes without
  re-bloating `AGENTS.md`.
- Tradeoff: the repository gains two root files and a validator lane before
  the visible mechanics split.
- Follow-up: create `mechanics/` and sharpen `playbooks/` in a later landing
  using this design spine as the authority map.

## Current Applicability

As of 2026-05-31:

- Still valid: `DESIGN.md` and `DESIGN.AGENTS.md` are live root surfaces.
- Changed: design and agent-surface shape no longer live only in root
  `AGENTS.md`, README prose, or sibling examples.
- Superseded by: none.

## Review Log

### 2026-05-31 - Initial landing

- Previous assumption: `aoa-playbooks` could rely on charter, README,
  boundaries, and root `AGENTS.md` until mechanics existed.
- New reality: mechanics and playbook-canon separation needs a root design
  spine before movement.
- Reason: future topology work should follow a positive owner map rather than
  copying sibling repo shapes literally.
- Source surfaces updated: `DESIGN.md`, `DESIGN.AGENTS.md`, root entrypoints,
  and root design validation.
- Validation: `python scripts/validate_root_design.py` and
  `python scripts/generate_decision_indexes.py --check`.

## Boundaries

- This decision does not create `mechanics/`.
- This decision does not move playbook source files.
- This decision does not promote any candidate route into a new playbook.
- This decision does not make generated readers authoritative.
- This decision does not move skill, technique, eval, memo, agent, routing,
  stats, KAG, runtime, or center truth into `aoa-playbooks`.

## Source Surfaces

- `DESIGN.md`
- `DESIGN.AGENTS.md`
- `AGENTS.md`
- `README.md`
- `docs/README.md`
- `ROADMAP.md`
- `scripts/validate_root_design.py`
- `scripts/release_check.py`

## Follow-Up Route

Use `DESIGN.md`, `DESIGN.AGENTS.md`, and this decision before creating
`mechanics/` or moving operation-topology material out of flat docs and into
mechanic packages.

## Verification

```bash
python scripts/validate_root_design.py
python scripts/generate_decision_indexes.py --check
python scripts/validate_playbooks.py
```
