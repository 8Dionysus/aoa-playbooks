# AGENTS.md

## Applies to

This card applies to `mechanics/agon/` and every nested path until a nearer
`AGENTS.md` narrows the lane.

## Role

`agon/` is the `head-fed/local` playbook mechanic for pre-protocol Agon trial,
trial-kernel, campaign, adoption, and recurrence-adapter surfaces.

It receives center pressure from `Agents-of-Abyss/mechanics/agon/`, but this
package owns only playbook-local rehearsal and registry payloads.

## Read before editing

Read:

1. root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/README.md`
4. this package `README.md`
5. `PARTS.md`
6. target part README/doc/schema/config/example/script
7. affected `playbooks/agon-*/PLAYBOOK.md` when source playbook meaning changes
8. affected recurrence manifest or quest only when root source stores change

## Boundaries

- Source Agon playbooks stay in `playbooks/agon-*/PLAYBOOK.md`.
- Agon quest notes stay in root `quests/`.
- Recurrence manifests stay in root `manifests/recurrence/`.
- Generated Agon registries stay in root `generated/`.
- Root `scripts/*agon*.py` commands stay compatibility wrappers.
- This package must not open a live arena protocol, write scars, mutate rank or
  trust, schedule retention, promote Tree of Sophia/KAG state, or make
  assistants hidden contestants.

## Validation

Run:

```bash
python mechanics/agon/scripts/validate_agon_package.py
python mechanics/agon/parts/trial-playbooks/scripts/build_agon_trial_playbook_registry.py --check
python mechanics/agon/parts/trial-playbooks/scripts/validate_agon_trial_playbooks.py
python mechanics/agon/parts/trial-kernel-bindings/scripts/build_agon_trial_kernel_binding_registry.py --check
python mechanics/agon/parts/trial-kernel-bindings/scripts/validate_agon_trial_kernel_bindings.py
python mechanics/agon/parts/campaign-playbooks/scripts/build_agon_campaign_playbook_registry.py --check
python mechanics/agon/parts/campaign-playbooks/scripts/validate_agon_campaign_playbook_registry.py
python scripts/validate_playbooks.py
python -m pytest -q tests/test_agon_trial_playbooks.py tests/test_agon_trial_kernel_bindings.py tests/test_agon_campaign_playbook_registry.py tests/test_agon_mechanics_package.py
```

## Closeout

Report which Agon part changed, whether source playbooks moved, whether root
generated/quest/manifest stores stayed retained, and which validators ran.
