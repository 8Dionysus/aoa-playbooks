# AGENTS.md
Local guidance for `tests/` in `aoa-playbooks`.

Read the root `AGENTS.md` first. Tests protect scenario boundaries, generated
alignment, and composition safety.

## Local role
Tests should catch when a playbook becomes too small to be a playbook, too vague
to be reusable, or too broad to respect neighboring repo ownership.

## Editing posture
Use fixtures that exercise handoffs, fallback posture, evidence posture,
registry alignment, stress lanes, and generated composition surfaces.

## Hard no
Do not write tests that bless hidden orchestration, giant prompt scripts, or
questline surfaces acting as runtime ledgers.

## Validation
Run:

```bash
python -m pytest -q tests
python scripts/validate_playbooks.py
```
