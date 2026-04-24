# AGENTS.md
Local guidance for `examples/` in `aoa-playbooks`.

Read the root `AGENTS.md` first. Examples demonstrate playbook contracts,
activation lanes, stress lanes, and re-entry gates without becoming canon.

## Local role
Examples must demonstrate contracts without becoming canon. They should clarify
schema shape, handoff posture, stress posture, or activation posture while
remaining weaker than authored playbooks and docs.

## Editing posture
Pair example changes with schemas, docs, validators, or generated surfaces when
shape changes. Keep sample data public-safe and obviously bounded.

## Hard no
Do not let examples become hidden playbooks, hidden run ledgers, or private
operator scripts.

## Validation
Run:

```bash
python scripts/validate_playbooks.py
python -m pytest -q tests
```
