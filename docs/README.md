# Documentation Map

This file is the human-first entrypoint for the `docs/` surface of `aoa-playbooks`.

Use it when you want to understand the AoA playbook layer rather than the broader federation as a whole.

## Start here

- Read [CHARTER](../CHARTER.md) for the role and boundaries of the playbook layer.
- Read [PLAYBOOK_MODEL](PLAYBOOK_MODEL.md) for the conceptual model.
- Read [BOUNDARIES](BOUNDARIES.md) for ownership discipline relative to neighboring AoA layers.
- Read [PLAYBOOK_BUNDLE_CONTRACT](PLAYBOOK_BUNDLE_CONTRACT.md) for the authored bundle contract.
- Read [PLAYBOOK_EXECUTION_SEAM](PLAYBOOK_EXECUTION_SEAM.md) for the derived runtime-readable activation seam.
- Open [../playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md](../playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md) for the first real playbook object.
- Read [ROADMAP](../ROADMAP.md) for the current direction.

## Docs in this repository

- [PLAYBOOK_MODEL](PLAYBOOK_MODEL.md) — what the playbook layer is for
- [BOUNDARIES](BOUNDARIES.md) — what the playbook layer owns and must not absorb
- [PLAYBOOK_BUNDLE_CONTRACT](PLAYBOOK_BUNDLE_CONTRACT.md) — how authored `PLAYBOOK.md` bundles stay compact and aligned with the registry
- [PLAYBOOK_EXECUTION_SEAM](PLAYBOOK_EXECUTION_SEAM.md) — how derived activation surfaces stay runtime-readable without becoming a second authored source

## Notes

This repository should stay bounded.
If a document starts trying to become a technique corpus, workflow corpus, proof corpus, memory store, or routing surface, it probably belongs in a neighboring AoA repository instead.
