# AGENTS.md
Local guidance for `schemas/` in `aoa-playbooks`.

Read the root `AGENTS.md` first. Schema changes are contract changes for
playbook-owned adjuncts such as stress lanes, re-entry gates, activation lanes,
and review packets.

## Local role
Schemas define shape for playbook-layer composition surfaces. They do not define
skills, eval verdicts, memory objects, role contracts, or runtime execution.

## Editing posture
Pair schema changes with examples, docs, validator updates, and generated
surfaces when applicable. Keep ids, enums, refs, and owner boundaries explicit.

## Hard no
Do not loosen schemas to allow vague orchestration sprawl. Do not smuggle a
single-skill workflow into a playbook contract.

## Validation
Run:

```bash
python scripts/validate_playbooks.py
python -m pytest -q tests
```
