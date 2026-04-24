# AGENTS.md
Local guidance for `config/` in `aoa-playbooks`.

Read the root `AGENTS.md` first. This directory holds playbook-owned composition
configuration such as `playbook_composition_overrides.json` and Agon seed inputs.

## Local role
Config may declare source-owned composition overrides, failure codes, handoff
refs, automation seeds, or trial registry inputs. It must stay subordinate to
authored playbooks and explicit docs.

## Editing posture
Keep each override tied to a playbook id, source surface, and generated consumer.
When config changes alter generated outputs, regenerate and validate them in the
same diff.

## Hard no
Do not hide new scenario meaning in config. Do not import skill, eval, memo,
routing, or runtime doctrine by side door.

## Validation
Run the matching generator in `--check` mode and:

```bash
python scripts/validate_playbooks.py
python -m pytest -q tests
```
