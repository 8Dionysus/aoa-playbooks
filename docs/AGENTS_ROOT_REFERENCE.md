# AGENTS root reference

This file preserves the previous full root guidance for `aoa-playbooks`.
The live root route card is `../AGENTS.md`.

Use this reference when:

- auditing a legacy rule from before Pack 5
- resolving a task branch that the short route card intentionally summarized
- checking whether a slimming move should become a nested `AGENTS.md`, owner doc, or validator rule

Do not treat this file as a competing root. If a preserved rule still actively governs a local directory, move or restate it at the smallest owner surface rather than re-bloating the root.

## Preserved root AGENTS.md from before Pack 5

# AGENTS.md

Guidance for coding agents and humans contributing to `aoa-playbooks`.

## Purpose

`aoa-playbooks` is the scenario and composition layer of AoA.
It stores explicit playbooks for recurring operational situations, multi-step
compositions across neighboring layers, handoff-aware scenarios, fallback
paths, expected evidence posture, and, in the current wave, reviewed
questline / campaign outline adjuncts for long-horizon recurrence.

This repository is for scenario-level composition.
It is not the underlying technique, skill, proof, memory, routing, or role
layer itself.

## Owns

This repository is the source of truth for:

- playbook structure
- scenario-level intent and composition wording
- step ordering and scenario posture
- fallback, rollback, return, and reanchor posture at the playbook layer
- expected evidence posture for a scenario
- playbook-layer metadata and generated registry surfaces
- bounded composition adjuncts such as handoff contracts, failure catalogs, subagent recipes, automation seeds, and composition manifests
- questline, campaign, and raid outline posture when those surfaces are explicitly defined in playbook-owned docs
- playbook-owned harvest posture hints for reviewed long-horizon routes

## Does not own

Do not treat this repository as the source of truth for:

- reusable engineering practice in `aoa-techniques`
- bounded skill execution meaning in `aoa-skills`
- proof doctrine or verdict logic in `aoa-evals`
- routing and dispatch logic in `aoa-routing`
- role contracts or progression doctrine in `aoa-agents`
- explicit memory-object meaning in `aoa-memo`
- derived knowledge substrate semantics in `aoa-kag`
- live quest state, progression state, or runtime ledger state

A playbook coordinates these layers.
It does not replace them.

## Core rules

A playbook is not a skill.

Questline and campaign reflection are reviewed outline seams, not runtime state.
A questbook is evidence-first. It is not a hidden run ledger, not a quest
sovereign, and not the harvest authority for the whole federation.

## Read this first

Before making changes, read in this order:

1. `README.md`
2. `ROADMAP.md`
3. the relevant model, bundle, gate, or evidence docs referenced there
4. the target playbook source you plan to edit
5. any affected generated registry or composition surfaces
6. neighboring repo docs if the playbook touches skills, agents, memo, evals, or routing

Then branch by task:

- questline / campaign / raid / reanchor changes: `docs/QUESTLINE_AND_CAMPAIGN_MODEL.md`, `docs/QUEST_HARVEST_AND_REANCHOR.md`, and `QUESTBOOK.md`
- orchestrator-facing alignment surfaces: `docs/ORCHESTRATOR_ALIGNMENT_SURFACES.md`
- playbook recurrence or reviewed-run posture: the recurrence and reviewed-run docs referenced from `README.md`

If you are editing inside `playbooks/` or `generated/`, also follow the nested
`AGENTS.md` in that directory.

## Primary objects

The most important objects in this repository are:

- playbook definitions under `playbooks/*/PLAYBOOK.md`
- `config/playbook_composition_overrides.json`
- scenario-composition, fallback, evidence-posture, and recurrence docs
- `QUESTBOOK.md` and its backing files when the task touches quest reflection
- generated playbook registry, activation, federation, review-status, and composition surfaces

## Hard NO

Do not:

- turn a playbook into a single skill
- turn a playbook into a role contract, proof doctrine, or routing logic
- store secrets, private infrastructure details, or unsafe operational specifics
- create vague scenario prose with no bounded steps, fallbacks, or evidence posture
- let “composition” become an excuse for hidden orchestration sprawl
- turn questline or campaign surfaces into a run ledger
- use campaign language to hide unbounded sprawl
- use raid language for ordinary multi-file work
- hide missing anchors behind continuity language
- let `QUESTBOOK.md` replace source docs, memo truth, eval truth, or harvest authority

## Contribution doctrine

Use this flow: `PLAN -> DIFF -> VERIFY -> REPORT`

### PLAN

State:

- what playbook, outline surface, or quest reflection surface is changing
- what composition, fallback, anchor, or evidence risk exists
- which neighboring layers are involved
- whether the change is semantic, metadata-only, or reviewed-outline-only

### DIFF

Keep the change focused.
Do not mix unrelated cleanup into a playbook change unless it is necessary for
repository integrity.

### VERIFY

Confirm that:

- the scenario remains bounded
- the scenario is still clearly more than one skill
- handoffs remain explicit
- fallback and return posture remain coherent
- expected evidence posture is still visible
- generated outputs remain aligned if metadata surfaces changed
- any questline or campaign surface keeps anchors, reanchor posture, stop conditions, and harvest posture explicit when applicable
- `QUESTBOOK.md` remains evidence-first and does not become a runtime ledger

### REPORT

Summarize:

- what playbooks or outline surfaces changed
- whether semantics changed or only metadata changed
- whether fallback, handoff, anchor, reanchor, or evidence posture changed
- whether quest reflection remained adjunct-only
- what validation was run
- any neighboring repo follow-up likely needed

## Validation

Run the validation commands documented in `README.md`.
If generated playbook surfaces changed, regenerate and validate them before
finishing.
