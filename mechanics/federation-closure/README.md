# Federation Closure Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | local |
| role | derive compact cross-repo closure surfaces from authored playbooks |
| trigger | playbook participant, skill, eval, memo, or writeback refs change |
| playbooks owns | federation projection shape and playbook source alignment |
| stronger owner split | `aoa-skills`, `aoa-evals`, `aoa-memo`, `aoa-agents`, routing, and runtime owners keep their truth |
| inputs | `playbooks/*/*/*/PLAYBOOK.md` and sibling owner refs named by those playbooks |
| outputs | root-published `generated/playbook_federation_surfaces.min.json` |
| must not claim | sibling source truth, runtime state, route dispatch, proof verdicts, memo truth, or skill semantics |
| validation | package executable owners; focused order in `AGENTS.md` |
| next route | `parts/federation-surfaces/`, `mechanics/activation/parts/activation-surface/docs/playbook-execution-seam.md`, root generated read model, or stronger owner repo |

## Active route

The active builder implementation lives under
`parts/federation-surfaces/scripts/generate_playbook_federation_surfaces.py`.

The root command `scripts/generate_playbook_federation_surfaces.py` remains as
an operator-facing compatibility wrapper.

## Functioning parts

- `federation-surfaces`: builds and validates the compact federation closure
  read model from authored playbooks.

## Source surfaces

- `playbooks/*/*/*/PLAYBOOK.md`
- `mechanics/activation/parts/activation-surface/docs/playbook-execution-seam.md`
- `generated/playbook_federation_surfaces.min.json`
- sibling owner refs resolved by `scripts/validate_playbooks.py`

## Owner boundary

Federation surfaces are derived closure readers. They are weaker than authored
playbooks and all sibling owner repositories.

This mechanic may expose the cross-repo refs a playbook depends on. It must
not redefine the meaning of those refs.

## Growth posture

The next safe growth is stronger schema/ref validation while keeping the public
generated read model stable.
