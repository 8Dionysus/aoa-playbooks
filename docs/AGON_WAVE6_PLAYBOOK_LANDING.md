# Agon Wave VI Playbook Landing

Wave VI lands seven experimental authored playbook bundles and one compact trial registry.

It follows the existing playbook lifecycle discipline: a route graduates only when the scenario is recurring, reviewable, and clearly more than one bounded skill.

The trial routes are experimental because the live arena protocol does not exist yet. Their job is to make the first mechanical rehearsals repeatable without pretending to run Agon.

## Validation

```bash
python scripts/build_agon_trial_playbook_registry.py --check
python scripts/validate_agon_trial_playbooks.py
python -m pytest -q tests/test_agon_trial_playbooks.py
```
