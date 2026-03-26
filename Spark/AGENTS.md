# Spark lane for aoa-playbooks

This file only governs work started from `Spark/`.

The root `AGENTS.md` remains authoritative for repository identity, ownership boundaries, reading order, and validation commands. This local file only narrows how GPT-5.3-Codex-Spark should behave when used as the fast-loop lane.

If `SWARM.md` exists in this directory, treat it as queue / swarm context. This `AGENTS.md` is the operating policy for Spark work.

## Default Spark posture

- Use Spark for short-loop work where a small diff is enough.
- Start with a map: task, files, risks, and validation path.
- Prefer one bounded patch per loop.
- Read the nearest source docs before editing.
- Use the narrowest relevant validation already documented by the repo.
- Report exactly what was and was not checked.
- Escalate instead of widening into a broad architectural rewrite.

## Spark is strongest here for

- recurring-scenario wording cleanup
- fallback, handoff, and expected-evidence clarity work
- playbook schema/example/generated-surface alignment
- tight audits that keep scenario boundaries explicit
- small composition repairs across already-defined neighboring layers

## Do not widen Spark here into

- inflating a single skill into a playbook without need
- rewriting skill, role, memory, or eval canon here
- hidden orchestration sprawl disguised as composition
- broad scenario-portfolio redesign

## Local done signal

A Spark task is done here when:

- the scenario remains bounded and clearly more than one skill
- handoffs and fallback paths are explicit
- expected evidence posture remains visible
- generated surfaces are aligned when touched
- the documented validation path ran when relevant

## Local note

Spark should think in recurring recipes here, not in boundless orchestration epics.

## Reporting contract

Always report:

- the restated task and touched scope
- which files or surfaces changed
- whether the change was semantic, structural, or clarity-only
- what validation actually ran
- what still needs a slower model or human review
