# Playbook Bundle Contract

This document defines the compact authored contract for `PLAYBOOK.md` bundles in `aoa-playbooks`.

The point is not to turn the repository into a giant workflow corpus.
The point is to give scenario-level method one readable, source-owned object once a route needs more than a registry row.
When a runtime-readable projection is helpful, it should stay derived from the bundle rather than becoming a second authored playbook object.

## Core rule

A playbook bundle owns the scenario route.

It does not own:
- technique meaning
- skill meaning
- eval doctrine
- memory taxonomy
- role taxonomy

Those neighboring layers stay authoritative for their own objects.

## Required frontmatter

Each authored bundle should keep registry-aligned fields in YAML frontmatter:

- `id`
- `name`
- `status`
- `summary`
- `scenario`
- `trigger`
- `prerequisites`
- `participating_agents`
- `required_skill_families`
- `evaluation_posture`
- `memory_posture`
- `fallback_mode`
- `expected_artifacts`

Optional bundle-local fields may appear when they stay compact and do not replace neighboring layer meaning.

For activation-eligible playbooks, these compact optional fields may appear when recurrence posture is canonical in the route:

- `return_posture`
- `return_anchor_artifacts`
- `return_reentry_modes`

For federation-checked playbooks, these bundle-local fields become required:

- `required_skills`
- `memo_contract_refs`
- `memo_writeback_targets`

These fields exist to point to neighboring source-owned surfaces without absorbing their meaning into the playbook layer.

Derived activation surfaces may project a small runtime-readable subset of bundle-aligned fields.
They must remain schema-backed projections of canonical playbook surfaces rather than independent authored routes.
Derived federation surfaces may project the machine-checkable closure fields used to validate skill lineage and memo writeback posture for a bounded cohort.

Authored bundles should live at:

- `playbooks/<name>/PLAYBOOK.md`

That path keeps the bundle slug aligned with the registry `name` and lets validation discover bundles without a hand-maintained path list.

## Required sections

Each authored bundle should include these fixed sections:

- `Intent`
- `Trigger boundary`
- `Prerequisites`
- `Participating agents`
- `Required skills`
- `Decision points`
- `Handoffs`
- `Fallback and rollback posture`
- `Expected evidence posture`
- `Expected artifacts`
- `Eval anchors`
- `Memory writeback`
- `Canonical route`

Return posture should stay explicit inside those existing sections rather than becoming a new required bundle section.

## What the bundle must make legible

A good `PLAYBOOK.md` should make it easy to answer:

- when this route should start
- which roles participate
- which concrete skills usually carry the route
- where the route can pause, hand off, or roll back
- what evidence should exist when the route finishes
- what memory writeback should survive the route

If a derived activation surface exists, it should preserve that authored meaning in compact form rather than extending it with runtime implementation details.
If a derived federation surface exists, it should preserve the exact neighboring-surface refs the playbook depends on rather than inventing new routing or memory semantics.

## First authored bundle

The current first authored bundle is:

- `playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md`

It is the first method-home example for the second-wave rule:

**method lives in playbooks**
