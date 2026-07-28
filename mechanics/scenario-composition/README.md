# Scenario Composition Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | local |
| role | derive scenario-level handoff, failure, subagent, automation, manifest, and runtime-neutral plan-contour read models |
| trigger | a managed playbook, composition or plan-contour config, upstream skill handoff contract, or generated composition output changes |
| playbooks owns | scenario-level composition and abstract plan-contour shape plus source config alignment |
| stronger owner split | `aoa-skills` owns skill execution and skill handoff meaning; routing/runtime owners own dispatch and execution |
| inputs | `playbooks/*/*/*/PLAYBOOK.md`, `generated/playbook_registry.min.json`, part-local composition and plan-contour configs, and `../aoa-skills/generated/capability_graph.json` |
| outputs | root-published composition read models plus `generated/playbook_plan_contours.min.json` |
| must not claim | runtime state, scheduler authority, route dispatch, skill semantics, proof verdicts, or memory truth |
| validation | package executable owners; focused order in `AGENTS.md` |
| next route | `parts/composition-surfaces/`, `parts/plan-contours/`, root generated read models, or the stronger owner |

## Active route

The existing composition builder implementation lives under
`parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py`.

The root command `scripts/generate_playbook_composition_surfaces.py` remains as
an operator-facing compatibility wrapper because README, release checks, and
tests already use that command path.

The runtime-neutral plan-contour builder lives under
`parts/plan-contours/scripts/generate_playbook_plan_contours.py` and publishes
its closed ABI directly to `generated/playbook_plan_contours.min.json`.

## Functioning parts

- `composition-surfaces`: builds and validates the compact composition read
  models from authored playbooks, root source config, and skill handoff
  contracts.
- `plan-contours`: builds and validates abstract step/effect, reviewed-input
  versus step-output, guarded-branch, evidence, eval, retention, and closeout
  contours for the three C2 golden scenarios without publishing commands or
  runtime bindings.

## Source surfaces

- `playbooks/*/*/*/PLAYBOOK.md`
- `generated/playbook_registry.min.json`
- `mechanics/scenario-composition/parts/composition-surfaces/config/playbook_composition_overrides.json`
- `../aoa-skills/generated/capability_graph.json`
- root generated composition outputs
- `mechanics/scenario-composition/parts/composition-surfaces/docs/handoff-contracts.md`
- `mechanics/scenario-composition/parts/composition-surfaces/docs/failure-recovery.md`
- `mechanics/scenario-composition/parts/composition-surfaces/docs/subagent-patterns.md`
- `mechanics/scenario-composition/parts/composition-surfaces/docs/automation-seeds.md`
- `mechanics/scenario-composition/parts/composition-surfaces/docs/playbook-composition-gates.md`
- `generated/playbook_handoff_contracts.json`
- `mechanics/scenario-composition/parts/plan-contours/config/playbook_plan_contours.json`
- `mechanics/scenario-composition/parts/plan-contours/schemas/playbook-plan-contours.schema.json`
- `mechanics/scenario-composition/parts/plan-contours/docs/playbook-plan-contour-contract.md`
- `generated/playbook_plan_contours.min.json`

## Owner boundary

Composition outputs are derived readers. They are weaker than authored
playbooks, root source config, and upstream skill contracts.

This mechanic may project handoff, failure, subagent, and automation metadata
that is already source-backed. It may also project an abstract plan contour
whose agents, capabilities, artifacts, eval anchors, and memo references match
authored frontmatter exactly and whose optional paths stay behind reviewed
boolean bindings. It must not invent runtime execution behavior, condition
values, commands, transport, verdicts, or skill semantics.

## Growth posture

The plan-contour ABI grows only through explicit owner changes with exact
source alignment and negative execution-boundary tests. Downstream compilation
does not implicitly enlarge the owner ABI.
