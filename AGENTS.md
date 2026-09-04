# AGENTS.md

Root route card for `aoa-playbooks`.

## Purpose

`aoa-playbooks` is the scenario and composition layer of AoA.
It stores recurring operational situations, multi-step compositions, handoff-aware scenarios, fallback paths, evidence posture, and reviewed questline or campaign outline adjuncts.
A playbook coordinates neighboring layers. It does not replace them.

## Owner lane

This repository owns:

- playbook structure, scenario intent, step ordering, fallback, rollback, return, and reanchor posture
- expected evidence posture at the scenario layer
- playbook metadata, generated registries, handoff contracts, failure catalogs, and composition manifests
- questline, campaign, raid, and harvest posture only when defined as playbook-owned reviewed outlines

It does not own:

- technique, skill, eval, routing, role, memory, KAG, shared statistical
  grammar, runtime, or live quest-state truth

It does own the meaning of playbook-local statistical questions and evidence
references exposed through `stats/`. Cross-owner composition and the shared
measurement protocol remain owned by `aoa-stats`.

## Skill and MCP boundary

This repository has no top-level `skills/` home or repo-scoped
`.agents/skills/` projection. Shared workflow skills remain owned by
`aoa-skills`. A local owner skill remains deferred until an owner MCP exists,
fresh admission evidence is reviewed, and an explicit decision admits the
surface; repository documentation alone cannot create that capability.

## Route by task

The inherited card and the nearest nested `AGENTS.md` define the active
instruction chain. Load only the owner sources needed by the task:

- public orientation or contributor entrypoint: `README.md`
- current direction: `ROADMAP.md`
- repository shape, source authority, or owner boundaries: `DESIGN.md`
- agent-card shape or guidance topology: `DESIGN.AGENTS.md`
- repeatable operation topology: `mechanics/AGENTS.md`; use
  `mechanics/README.md` for the public package atlas, placement, or provenance
- a playbook-local statistical question: `stats/AGENTS.md` and
  `stats/port.manifest.json`; use `stats/README.md` for human orientation
- scenario meaning: the target
  `playbooks/<branch>/<family>/<slug>/PLAYBOOK.md`
- a derived reader: its source config or builder before the generated output
- a neighboring-owner claim: that owner's source contract
- validation selection: nearest `VALIDATION.md`, then the root validation map
- branch, PR, CI, release, or merge work: `docs/RELEASING.md`
- legacy root-law archaeology: `docs/AGENTS_ROOT_REFERENCE.md`

The nearest nested card supplies only its local contract, risk, stop-lines, and
route delta. Authored source owns meaning; generated, exported, compact,
runtime, and adapter surfaces are derived. Keep quest, recurrence, progression,
or autonomy language bounded, evidence-linked, reversible, and weaker than its
owner contract.

## Memory route

For reviewed continuity or prior rationale use the `aoa-memo` route. Session
evidence, a local candidate port, and durable reviewed memory remain distinct;
none becomes playbook truth merely by being recalled here.

## Route away when

- the change is really one skill, reusable technique, proof doctrine, memory object, role contract, routing logic, or runtime state
- the request is to scaffold an `aoa-playbooks` skill before the owner MCP and
  manual admission route exist
- campaign or raid language hides unbounded sprawl or missing anchors

## Landing boundary

`docs/RELEASING.md` owns the branch, PR, CI, release, and merge procedure;
`.github/AGENTS.md` owns GitHub-native files. If required status, review,
authority, or post-merge state cannot be observed, stop rather than infer it.

## Verify

Use the nearest `VALIDATION.md` for focused checks and the root validation map
for repository-wide composition. Regenerate derived playbook surfaces through
their builders before checking parity.

## Report

State which playbook or outline changed, whether semantics or metadata changed, whether fallback, handoff, anchor, reanchor, or evidence posture changed, and what validation ran.

For changes to repository topology or durable card shape, use `DESIGN.md` or
`DESIGN.AGENTS.md` respectively. `docs/AGENTS_ROOT_REFERENCE.md` is historical
detail, not an inherited preload.
