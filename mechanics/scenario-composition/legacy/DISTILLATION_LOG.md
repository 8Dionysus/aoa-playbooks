# Scenario Composition Distillation Log

## 2026-05-31 - Builder implementation move

- Former root path: `scripts/generate_playbook_composition_surfaces.py`
- Active implementation:
  `mechanics/scenario-composition/parts/composition-surfaces/scripts/generate_playbook_composition_surfaces.py`
- Compatibility path retained:
  `scripts/generate_playbook_composition_surfaces.py`
- Reason: scenario composition is a local playbook-native mechanic, while the
  root command path remains public operator tooling.
- Validation was completed by the package executable validator and generated-freshness owner.
