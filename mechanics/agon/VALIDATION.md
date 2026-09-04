# Validation routes

```bash
python mechanics/agon/scripts/validate_agon_package.py
python mechanics/agon/parts/trial-playbooks/scripts/build_agon_trial_playbook_registry.py --check
python mechanics/agon/parts/trial-playbooks/scripts/validate_agon_trial_playbooks.py
python mechanics/agon/parts/trial-kernel-bindings/scripts/build_agon_trial_kernel_binding_registry.py --check
python mechanics/agon/parts/trial-kernel-bindings/scripts/validate_agon_trial_kernel_bindings.py
python mechanics/agon/parts/campaign-playbooks/scripts/build_agon_campaign_playbook_registry.py --check
python mechanics/agon/parts/campaign-playbooks/scripts/validate_agon_campaign_playbook_registry.py
python -m pytest -q tests/test_agon_trial_playbooks.py tests/test_agon_trial_kernel_bindings.py tests/test_agon_campaign_playbook_registry.py tests/test_agon_mechanics_package.py
```
