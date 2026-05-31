# Decision Records Index

This directory is the durable decision surface for `aoa-playbooks`.

Use it when a future contributor needs the rationale for a route, topology,
owner split, validator route, workflow boundary, playbook source surface,
mechanic package, generated read model, or review-gate posture.

Ordinary edit summaries, generated output, runtime logs, private evidence,
proof verdicts, and one-off planning thoughts route to their owning surfaces
instead.

## Operating Card

| Field | Route |
| --- | --- |
| role | durable decision rationale entrypoint and agent-facing index chooser |
| entry | use when a structural, topology, validation, public-contract, playbook-route, mechanic, generated-index, or agent-route change needs recoverable rationale |
| input | changed source surface, owner boundary, rejected option, validator guard, or cross-surface route pressure |
| output | canonical decision note, metadata-backed lookup index, and route back to the source surface |
| owner | `docs/decisions/AGENTS.md` for lane law; canonical decision notes for rationale; generated indexes for lookup only |
| next route | source surface first, then root `AGENTS.md`, `README.md`, `CHARTER.md`, `docs/BOUNDARIES.md`, generated lookup indexes, or the affected playbook/mechanic owner |
| validation | `python scripts/generate_decision_indexes.py --check`, `git diff --check`, and the owning validator for the changed surface |

## Authority

Decision notes explain why a route was chosen.

They are weaker than the source surface they describe:

- repository authority stays in `CHARTER.md`;
- playbook-layer identity stays in `README.md`, `CHARTER.md`, and
  `docs/BOUNDARIES.md`;
- source-authored scenario meaning stays in `playbooks/*/PLAYBOOK.md`;
- generated readers stay derived from their builders and source surfaces;
- real-run and gate-review evidence stays in `docs/real-runs/` and
  `docs/gate-reviews/`;
- future mechanic shape belongs under `mechanics/` once that layer is created;
- sibling repositories keep their stronger truth for skills, techniques, evals,
  routing, memory objects, agents, stats, and runtime behavior.

Generated decision indexes are weaker than the decision notes. They exist to
make lookup cheaper for agents, not to carry decision rationale.

## Index Shape

Each decision owns:

- a canonical `Decision ID: AOA-PB-D-####`;
- a full canonical-ID filename, for example `AOA-PB-D-0001-*.md`;
- an `## Index Metadata` block naming original date, surface classes, playbook
  routes, mechanic parents, guard families, and posture.

The lookup indexes under [indexes](indexes/README.md) are generated from that
metadata:

- [Decisions by canonical ID and number](indexes/by-number.md)
- [Decisions by date](indexes/by-date.md)
- [Decisions by surface class](indexes/by-surface.md)
- [Decisions by playbook route](indexes/by-playbook-route.md)
- [Decisions by mechanic parent](indexes/by-mechanic.md)
- [Decisions by validation or guard family](indexes/by-guard.md)

Use them in both directions:

- top down: repo route -> playbook route -> surface class -> mechanic parent ->
  guard family -> decision rationale;
- bottom up: changed source surface -> local route card or generated read model
  -> validator guard -> decision rationale -> stronger owner surface.

Regenerate the read models after decision metadata changes:

```bash
python scripts/generate_decision_indexes.py
```

Check generated parity before closeout:

```bash
python scripts/generate_decision_indexes.py --check
```

## Addressing

Full canonical-ID decision paths are the active source files:

- `docs/decisions/AOA-PB-D-0001-*.md`
- `docs/decisions/AOA-PB-D-0002-*.md`
- `docs/decisions/AOA-PB-D-####-*.md`

Canonical IDs remain the stable handles. Previous date-prefixed paths are not
live files and are not preserved as a repository lookup layer. Use git history,
PRs, or release notes when old path archaeology is actually needed.

Do not recreate date-named files or generated compatibility maps for retired
paths.

## Naming

Use the full canonical decision ID as the filename prefix:

`AOA-PB-D-0003-short-decision-slug.md`

Prefer short titles that name the route, not the whole debate.

## Template

Start from [TEMPLATE.md](TEMPLATE.md) for new decisions. Keep notes concise, but
include enough context, options, rationale, consequences, index metadata, and
validation for a future agent to avoid repeating the same route question.
