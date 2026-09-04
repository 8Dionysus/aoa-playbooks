# AGENTS.md

## Applies to

This card applies to `mechanics/federation-closure/` until a nearer
`AGENTS.md` narrows the lane.

## Role

`mechanics/federation-closure/` owns the local mechanic that derives compact
cross-repo closure surfaces from authored playbooks without absorbing skill,
eval, memo, agent, routing, or runtime truth.

## Route by task

- Closure projection: use the execution-seam doc, authored playbooks, target
  builder, and exact sibling-owner sources for refs being checked.
- Package topology or provenance: use `README.md`, `PARTS.md`, and
  `PROVENANCE.md`.
- Repository or agent-route shape: use `DESIGN.md` or `DESIGN.AGENTS.md`
  respectively.

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

Run `VALIDATION.md` in this directory, then the common mechanics route in the root `VALIDATION.md`.

For release-bound changes, run:

Run the common mechanics release route in `../../VALIDATION.md` on demand.

## Closeout

Report whether federation source refs changed, whether the root generated
surface changed, whether the package implementation or root wrapper changed,
and which validation proved closure stayed derived.
