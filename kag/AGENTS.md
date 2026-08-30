# AGENTS.md

## Applies to

This card applies to `aoa-playbooks/kag/` and every nested path until a nearer card
narrows the lane.

## Role

`kag/` is the local KAG provider home for `aoa-playbooks`. It exposes compact,
source-linked records over `playbook source home and scenario registry` for `aoa-kag` registry,
composition, and MCP consumers.

## Route by task

Provider-record changes start from `kag/manifest.json`,
`playbooks/source_home.manifest.json`, and the exact source-linked record.
Use `kag/README.md` or `playbooks/README.md` only when their public provider
or owner-return navigation is part of the change.

## Boundaries

Keep authored meaning with `aoa-playbooks` source surfaces. Keep shared KAG schema,
registry, composition, and provider validation with `aoa-kag`. Keep runtime
serving state with `abyss-stack` or the runtime owner named by the consumer.

## Validation

Use the owner validator named in `manifest.json`, then validate this provider
through the `aoa-kag` local subtree validator.

## Closeout

Report provider records changed, source-return route changed, owner validation,
`aoa-kag` validation, and the next MCP consumer route.
