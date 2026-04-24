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

- technique, skill, eval, routing, role, memory, KAG, stats, runtime, or live quest-state truth

## Start here

1. `README.md`
2. `ROADMAP.md`
3. the relevant model, bundle, gate, or evidence docs referenced there
4. the target `playbooks/*/PLAYBOOK.md` or outline surface
5. affected generated registry or composition surfaces
6. neighboring repo docs when the playbook touches their meaning
7. `docs/AGENTS_ROOT_REFERENCE.md` for preserved full root branches


## AGENTS stack law

- Start with this root card, then follow the nearest nested `AGENTS.md` for every touched path.
- Root guidance owns repository identity, owner boundaries, route choice, and the shortest honest verification path.
- Nested guidance owns local contracts, local risk, exact files, and local checks.
- Authored source surfaces own meaning. Generated, exported, compact, derived, runtime, and adapter surfaces summarize, transport, or support meaning.
- Self-agency, recurrence, quest, progression, checkpoint, or growth language must stay bounded, reviewable, evidence-linked, and reversible.
- Report what changed, what was verified, what was not verified, and where the next agent should resume.

## Route away when

- the change is really one skill, reusable technique, proof doctrine, memory object, role contract, routing logic, or runtime state
- campaign or raid language hides unbounded sprawl or missing anchors

## Verify

Run the validation commands documented in `README.md` for the touched surface.
If generated playbook surfaces change, regenerate and validate them before finishing.
Use `docs/AGENTS_ROOT_REFERENCE.md` for preserved branch guidance around questline, campaign, raid, reanchor, and evidence posture.

## Report

State which playbook or outline changed, whether semantics or metadata changed, whether fallback, handoff, anchor, reanchor, or evidence posture changed, and what validation ran.

## Full reference

`docs/AGENTS_ROOT_REFERENCE.md` preserves the former detailed root guidance, including hard boundaries and verification questions.
