# AoA Playbooks Charter

## Purpose

`aoa-playbooks` is the scenario and composition layer of the AoA ecosystem.

Its purpose is to make recurring operational recipes explicit as reusable scenario-level compositions rather than leaving them scattered across prompts, ad hoc notes, or orchestration folklore.

## Mission

This repository exists to support playbook-layer work such as:
- defining reusable scenario recipes
- naming trigger conditions and prerequisites
- clarifying participating agent roles
- clarifying which skill families are usually composed
- naming evaluation and memory posture for recurring situations
- making fallback and rollback posture reviewable

## What this repository owns

This repository owns playbook-layer truth about:
- playbook profiles
- scenario contracts
- trigger and prerequisite posture
- participating agent role patterns
- required skill-family composition hints
- fallback posture
- expected artifact posture
- compact playbook registries
- playbook-layer schemas and validation rules

## What this repository does not own

This repository does not own the primary meaning of:
- reusable techniques
- bounded execution workflows
- bounded proof surfaces
- memory objects
- routing surfaces
- infrastructure implementation

## Core principles

- recurring scenarios should be explicit rather than folkloric
- playbooks should stay compact enough to inspect
- fallback posture must be visible and reviewable
- evaluation posture should be named, not improvised later
- the playbook layer should coordinate neighboring layers without swallowing them

## Source-of-truth rule

Neighboring AoA repositories still own their own meaning.

Examples:
- `aoa-techniques` owns practice meaning
- `aoa-skills` owns execution meaning
- `aoa-evals` owns proof meaning
- `aoa-routing` owns navigation and dispatch surfaces
- `aoa-memo` owns memory and recall meaning
- `aoa-agents` owns role and persona meaning
- `aoa-playbooks` owns scenario-level composition meaning

## Role in the federation

Treat `aoa-playbooks` as:
- the scenario and composition layer of AoA
- the canonical home of recurring multi-surface operational recipes
- the place where scenario posture becomes explicit and reviewable

## Long-term direction

If `aoa-playbooks` matures well, it should help AoA move from isolated workflows toward reusable scenario-level operating forms without collapsing the distinction between:
- who acts
- how action is carried out
- how action is judged
- what memory is available
- what to do when the scenario goes sideways
