# AGENTS.md

Guidance for coding agents and humans contributing to `aoa-playbooks`.

## Purpose

`aoa-playbooks` is the scenario and composition layer of AoA. It stores explicit playbooks for recurring operational situations, multi-step compositions across neighboring layers, handoff-aware scenarios, fallback paths, and expected evidence posture for those scenarios.

This repository is for scenario-level composition, not for the underlying technique, skill, proof, memory, or routing layer itself.

## Owns

This repository is the source of truth for:

- playbook structure
- scenario-level intent and composition wording
- step ordering and scenario posture
- fallback, rollback, and return posture at the playbook layer
- expected evidence posture for a scenario
- playbook-layer metadata and generated registry surfaces
- bounded composition adjuncts such as handoff contracts, failure catalogs, subagent recipes, automation seeds, and composition manifests

## Does not own

Do not treat this repository as the source of truth for:

- reusable engineering practice in `aoa-techniques`
- bounded skill execution meaning in `aoa-skills`
- proof doctrine or verdict logic in `aoa-evals`
- routing and dispatch logic in `aoa-routing`
- role contracts in `aoa-agents`
- explicit memory-object meaning in `aoa-memo`
- derived knowledge substrate semantics in `aoa-kag`

A playbook coordinates these layers. It does not replace them.

## Core rule

A playbook is not a skill.

If the task really belongs to one bounded workflow, keep it in `aoa-skills` instead of inflating it into a playbook.

## Read this first

Before making changes, read in this order:

1. `README.md`
2. the relevant model, bundle, gate, or evidence docs referenced there
3. the target playbook source you plan to edit
4. any affected generated registry or composition surfaces
5. neighboring repo docs if the playbook touches skills, agents, memo, evals, or routing

If you are editing inside `playbooks/` or `generated/`, also follow the nested `AGENTS.md` in that directory.

## Primary objects

The most important objects in this repository are:

- playbook definitions under `playbooks/*/PLAYBOOK.md`
- `config/playbook_composition_overrides.json`
- scenario-composition, fallback, and evidence-posture docs
- generated playbook registry, activation, federation, review-status, and composition surfaces

## Hard NO

Do not:

- turn a playbook into a single skill
- turn a playbook into a role contract, proof doctrine, or routing logic
- store secrets, private infrastructure details, or unsafe operational specifics
- create vague scenario prose with no bounded steps, fallbacks, or evidence posture
- let “composition” become an excuse for hidden orchestration sprawl

## Contribution doctrine

Use this flow: `PLAN -> DIFF -> VERIFY -> REPORT`

### PLAN

State:

- what playbook or scenario surface is changing
- what composition, fallback, or evidence risk exists
- which neighboring layers are involved
- whether the change is semantic or metadata-only

### DIFF

Keep the change focused. Do not mix unrelated cleanup into a playbook change unless it is necessary for repository integrity.

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
- whether fallback, handoff, or evidence posture changed
- what validation was run
- any neighboring repo follow-up likely needed

## Validation

Run the validation commands documented in `README.md`.

If generated playbook surfaces changed, regenerate and validate them before finishing.

The canonical commands are:

```bash
python scripts/generate_playbook_activation_surfaces.py --check
python scripts/generate_playbook_federation_surfaces.py --check
python scripts/generate_playbook_review_status.py --check
python scripts/generate_playbook_composition_surfaces.py --check
python scripts/validate_playbooks.py
```

Do not claim checks you did not run.
