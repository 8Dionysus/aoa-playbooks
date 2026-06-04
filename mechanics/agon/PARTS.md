# Agon Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `trial-playbooks` | Wave VI pre-protocol trial playbook doctrine, seed, schema, examples, builder, and validator | `parts/trial-playbooks/**`, `playbooks/agon/trials/agon-*-trial/PLAYBOOK.md`, `generated/agon_trial_playbook_registry.min.json` | `python mechanics/agon/parts/trial-playbooks/scripts/build_agon_trial_playbook_registry.py --check`, `python mechanics/agon/parts/trial-playbooks/scripts/validate_agon_trial_playbooks.py` | active |
| `trial-kernel-bindings` | Wave XIII kernel-binding candidate registry | `parts/trial-kernel-bindings/**`, `generated/agon_trial_kernel_binding_registry.min.json` | builder `--check` plus kernel validator | active |
| `campaign-playbooks` | Wave XVI campaign playbook candidate registry | `parts/campaign-playbooks/**`, `playbooks/agon/campaigns/agon-campaign-*/PLAYBOOK.md`, `generated/agon_campaign_playbook_registry.min.json` | builder `--check` plus campaign validator | active |
| `adoption` | agonic adoption run contract surfaces | `parts/adoption/**` | package validator | active |
| `recurrence-adapter` | Agon recurrence adapter route doc and recurrence manifests | `parts/recurrence-adapter/docs/agon-recurrence-adapter.md`, `parts/recurrence-adapter/manifests/**` | package validator | active |

## Deferred payloads

- `playbooks/agon/*/agon-*/PLAYBOOK.md` stay in `playbooks/` as source playbook
  canon.
- `quests/AOP-Q-AGON-*` stay in root `quests/` as quest source notes.
- Agon recurrence manifests and hook manifests live under the owning Agon parts.
- `generated/agon_*_registry.min.json` stay root generated read models.

## Part growth rule

Each part must keep:

- pre-protocol status explicit;
- source playbook truth out of mechanics;
- generated registry output root-published;
- root command compatibility;
- stronger-owner stop-lines visible.
