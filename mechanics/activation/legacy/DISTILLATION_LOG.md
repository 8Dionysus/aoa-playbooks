# Activation Distillation Log

## 2026-05-31 - Builder implementation move

- Former root path: `scripts/generate_playbook_activation_surfaces.py`
- Active implementation:
  `mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py`
- Compatibility path retained:
  `scripts/generate_playbook_activation_surfaces.py`
- Reason: activation is a local playbook-native mechanic, while the root
  command path remains public operator tooling.
- Validation was completed by the package executable validator and generated-freshness owner.
