# AGENTS.md

## Applies to

This card applies to `mechanics/activation/` until a nearer `AGENTS.md`
narrows the lane.

## Role

`mechanics/activation/` owns the local mechanic that turns authored playbook
metadata into a compact activation-readable projection without making
`aoa-playbooks` a runtime owner.

## Route by task

- Projection meaning or builder: use the execution-seam doc, source registry,
  target builder, and generated output.
- Package topology or provenance: use `README.md`, `PARTS.md`, and
  `PROVENANCE.md`.
- Authored playbook input: follow `playbooks/AGENTS.md` and the exact bundle.
- Repository or agent-route shape: use `DESIGN.md` or `DESIGN.AGENTS.md`
  respectively.

## Boundaries

- Activation is a local mechanic, not a head-fed center mechanic.
- Source playbook truth stays in `playbooks/*/*/*/PLAYBOOK.md` and
  `generated/playbook_registry.min.json`.
- `generated/playbook_activation_surfaces.min.json` stays a root-published
  derived read model.
- Root `mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py` stays a compatibility
  command wrapper.
- Do not add runtime state, tool bindings, routing policy, memo truth, proof
  verdicts, or hidden execution packets to activation surfaces.

## Validation

Run:

```bash
python mechanics/activation/scripts/validate_activation_package.py
python mechanics/activation/parts/activation-surface/scripts/generate_playbook_activation_surfaces.py --check
python scripts/validate_mechanics_skeleton.py
python scripts/validate_playbooks.py
```

For release-bound changes, run:

```bash
python scripts/release_check.py
```

## Closeout

Report whether activation source inputs changed, whether the root generated
surface changed, whether the package implementation or compatibility wrapper
changed, and which validation proved the projection stayed derived.
