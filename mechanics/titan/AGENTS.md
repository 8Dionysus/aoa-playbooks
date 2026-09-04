# AGENTS.md

## Applies to

This card applies to `mechanics/titan/`.

## Role

`titan/` is the `head-fed/local` mechanic for Titan drill and route ecology
playbooks inside `aoa-playbooks`.

It validates package-local Titan docs while keeping role authority and runtime
service truth with stronger owners.

## Route by task

Start from the exact Titan route doc or source playbook being changed. Use
`README.md` for package topology or stronger-owner orientation.

## Boundaries

- Do not claim Titan role authority.
- Do not claim runtime harness, appserver, memory loom, or service cohort
  implementation.
- Do not move Titan source playbooks out of `playbooks/`.

## Validation

Run `VALIDATION.md` in this directory, then the common mechanics route in the root `VALIDATION.md`.

## Closeout

Report whether Titan route docs or source playbooks changed and which stronger
owner is implicated.
