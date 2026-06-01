# AGENTS.md

## Applies to

This card applies to `mechanics/federation-closure/` until a nearer
`AGENTS.md` narrows the lane.

## Role

`mechanics/federation-closure/` owns the local mechanic that derives compact
cross-repo closure surfaces from authored playbooks without absorbing skill,
eval, memo, agent, routing, or runtime truth.

## Read before editing

Read:

1. root `AGENTS.md`
2. `DESIGN.md`
3. `DESIGN.AGENTS.md`
4. `mechanics/AGENTS.md`
5. `mechanics/README.md`
6. `mechanics/federation-closure/README.md`
7. `mechanics/federation-closure/PARTS.md`
8. `mechanics/activation/parts/activation-surface/docs/playbook-execution-seam.md`
9. the sibling owner docs for refs being checked

## Boundaries

- Federation closure is class `local`.
- It validates cross-repo refs; it does not own sibling truth.
- Root `generated/playbook_federation_surfaces.min.json` stays a
  root-published closure read model.
- Root `mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py` stays a
  compatibility command wrapper.
- Do not encode runtime execution, router policy, skill meaning, proof
  verdicts, memo truth, or role authority in federation surfaces.

## Validation

Run:

```bash
python mechanics/federation-closure/scripts/validate_federation_closure_package.py
python mechanics/federation-closure/parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py --check
python scripts/validate_mechanics_skeleton.py
python scripts/validate_playbooks.py
```

For release-bound changes, run:

```bash
python scripts/release_check.py
```

## Closeout

Report whether federation source refs changed, whether the root generated
surface changed, whether the package implementation or root wrapper changed,
and which validation proved closure stayed derived.
