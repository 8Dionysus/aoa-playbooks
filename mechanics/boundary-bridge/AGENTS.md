# AGENTS.md

## Applies to

This card applies to `mechanics/boundary-bridge/`.

## Role

`boundary-bridge/` owns playbook-local cross-owner handoff and orchestrator
alignment mechanics without absorbing sibling owner truth.

## Boundaries

- Do not make playbooks own skills, proof, memory, agent role, or routing
  truth.
- Keep handoff drills as choreography and evidence contracts, not execution
  authority.
- Keep orchestrator alignment as advisory surfaces.

## Validation

```bash
python mechanics/boundary-bridge/scripts/validate_boundary_bridge_package.py
python scripts/validate_playbooks.py
```

## Closeout

Report which handoff/orchestrator bridge payload changed and which stronger
owner was referenced.
