# Federation Closure Distillation Log

## 2026-05-31 - Builder implementation move

- Former root path: `scripts/generate_playbook_federation_surfaces.py`
- Active implementation:
  `mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py`
- Compatibility path retained:
  `scripts/generate_playbook_federation_surfaces.py`
- Reason: federation closure is a local playbook-native mechanic, while the
  root command path remains public operator tooling.
- Validation:
  `python mechanics/federation-closure/scripts/validate_federation_closure_package.py`
  and `python scripts/generate_playbook_federation_surfaces.py --check`
