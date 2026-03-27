# AGENTS.md

Guidance for coding agents and humans contributing to `aoa-playbooks`.

## Purpose

`aoa-playbooks` is the scenario and composition layer of AoA.

It stores explicit playbooks for recurring operational situations, multi-step compositions across neighboring layers, handoff-aware scenarios, fallback paths, and expected evidence posture for those scenarios.

This repository is for scenario-level composition, not for the underlying source practice, skill canon, proof canon, or routing layer itself.

## Owns

This repository is the source of truth for:

- playbook structure
- scenario-level intent and composition wording
- step ordering and scenario posture
- fallback and exception posture at the playbook layer
- expected evidence posture for a scenario
- playbook-layer metadata and generated registry surfaces
- bounded composition adjuncts such as shared failure catalogs, subagent recipes, automation seeds, and playbook-owned handoff bridges

## Does not own

Do not treat this repository as the source of truth for:

- reusable engineering practice in `aoa-techniques`
- bounded skill execution meaning in `aoa-skills`
- proof doctrine or verdict logic in `aoa-evals`
- routing and dispatch logic in `aoa-routing`
- role contracts in `aoa-agents`
- explicit memory-object meaning in `aoa-memo`
- derived knowledge substrate semantics in `aoa-kag`

A playbook coordinates these layers.
It does not replace them.

## Core rule

A playbook is not a skill.

A skill is a bounded execution unit.
A playbook composes multiple units, boundaries, handoffs, and evidence expectations across a recurring scenario.

If the task really belongs to one bounded workflow, keep it in `aoa-skills` instead of inflating it into a playbook.

## Read this first

Before making changes, read in this order:

1. `README.md`
2. any playbook-schema or composition docs referenced by the README
3. the target playbook source you plan to edit
4. any generated playbook registry or capsule surfaces affected by the task
5. neighboring repo docs if the playbook touches skills, agents, memo, evals, or routing

If you are editing inside `playbooks/` or `generated/`, also follow the nested `AGENTS.md` in that directory.

## Primary objects

The most important objects in this repository are:

- playbook definitions
- `config/playbook_composition_overrides.json`
- scenario-composition docs
- fallback posture docs
- expected evidence posture docs
- generated playbook catalogs, registry outputs, and playbook-owned composition surfaces

## Allowed changes

Safe, normal contributions include:

- refining a recurring scenario
- tightening composition boundaries
- clarifying prerequisites, fallbacks, and handoffs
- clarifying expected evidence or review posture
- fixing metadata drift between source files and generated outputs
- adding a new playbook when it clearly belongs to the recurring scenario layer

## Changes requiring extra care

Use extra caution when:

- changing playbook names or identifiers
- changing scenario boundaries
- changing fallback semantics
- changing generated registry shape
- changing composition wording that neighboring repos may depend on
- rewriting playbooks in a way that absorbs too much skill or agent-layer meaning

## Hard NO

Do not:

- turn a playbook into a single skill
- turn a playbook into a role contract
- turn a playbook into proof doctrine
- turn a playbook into routing logic
- store secrets, private infra details, or unsafe operational specifics
- create vague scenario prose with no bounded steps, fallbacks, or evidence posture

Do not let “composition” become an excuse for hidden orchestration sprawl.

## Playbook doctrine

A good playbook change should make it easier to answer:

- when this scenario applies
- what neighboring layers are involved
- what order of operations makes sense
- where handoffs occur
- what fallback paths exist
- what evidence should exist when the scenario finishes

A bad playbook change usually makes the scenario less bounded, less explicit, less reviewable, or too similar to a single skill.

## Public hygiene

Assume everything here is public, inspectable, and challengeable.

Write for portability:

- keep scenarios generalizable
- keep fallbacks explicit
- keep private topology out
- keep evidence posture reviewable
- avoid hidden environment assumptions
- sanitize examples

## Default editing posture

Prefer the smallest reviewable change.

Preserve canonical wording unless the task explicitly requires semantic change.
If semantic change is made, report it explicitly.

## Contribution doctrine

Use this flow:

`PLAN -> DIFF -> VERIFY -> REPORT`

### PLAN

State:

- what playbook or scenario surface is changing
- what composition or fallback risk exists
- which neighboring layers are involved
- whether the change is semantic or metadata-only

### DIFF

Keep the change focused.

Do not mix unrelated cleanup into a playbook change unless it is necessary for repository integrity.

### VERIFY

Confirm that:

- the scenario remains bounded
- the scenario is still clearly more than one skill
- handoffs remain explicit
- fallback posture remains coherent
- expected evidence posture is still visible
- generated outputs remain aligned if metadata surfaces changed

### REPORT

Summarize:

- what playbooks changed
- whether semantics changed or only metadata changed
- whether fallback or evidence posture changed
- what validation was run
- any neighboring repo follow-up likely needed

## Validation

Run the validation commands documented in `README.md`.

If catalogs, capsules, or other generated playbook surfaces changed, regenerate and validate them before finishing.

Do not claim checks you did not run.

## Cross-repo neighbors

Use these neighboring repositories when the task crosses boundaries:

- `aoa-skills` for bounded execution units
- `aoa-agents` for role and handoff posture
- `aoa-evals` for proof surfaces and evidence framing
- `aoa-memo` for explicit memory objects
- `aoa-routing` for smallest-next-object navigation
- `Agents-of-Abyss` for ecosystem-level map and boundary doctrine

## Output expectations

When reporting back after a change, include:

- which playbooks changed
- whether semantics changed or only metadata changed
- whether fallback, handoff, or evidence posture changed
- whether generated outputs changed
- what validation was run
- any neighboring repo follow-up likely needed

## Default editing posture

Prefer the smallest reviewable change.
Preserve canonical wording unless the task explicitly requires semantic change.
If semantic change is made, report it explicitly.
