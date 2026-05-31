# Party Template Model

## Purpose

This note defines the bridge-wave party-template surface for `aoa-playbooks`.

It exists so that recurring scenarios can publish reviewed party composition and build posture without turning playbooks into runtime state.

## Core rule

A party template is a scenario-owned derived composition surface.

It may describe:
- which playbook and route it belongs to
- which cohort pattern fits
- which slots should exist
- which abilities, feats, and reputation slices matter
- which failure followups or reanchor anchors matter

It does not:
- create live session state
- equip agents at runtime
- rewrite skill or feat meaning
- replace proof doctrine
- replace routing logic

## Why playbooks own this

Playbooks already own recurring scenario composition.
Party templates are a scenario-level reflection of that same composition discipline.

If the question becomes “which recurring route wants which roles, build edges, and fallback posture?”, the playbook layer is the right home.

## Slot posture

A slot should stay small and legible.

Good first bridge-wave slot fields:
- role or archetype fit
- minimum reviewed rank
- preferred mastery axes
- required abilities
- preferred feats
- optional reputation slices when trust posture matters

Do not turn a slot into a hidden psychological profile or a runtime secret.

## Unlock gates

A template may name its expected proof posture.
That does not mean `aoa-playbooks` owns proof.
It only means the scenario can name what proof shape it expects before a party lane should be treated as ready.

## Reanchor posture

Party templates may name:
- valid return modes
- anchor refs
- maximum reanchors
- failure followups

That keeps scenario recurrence honest without turning the playbook layer into a run ledger.

## Anti-patterns

- storing current equipped runtime state inside the template
- inventing new skill or feat semantics inside playbooks
- hiding proof requirements behind cinematic language
- treating one scenario template as a universal class build
- using party templates as a substitute for quests, playbooks, or evals themselves
