# AGENTS.md

## Applies to

This card applies to `docs/decisions/` and durable decision notes inside it.

## Role

Decision records preserve why structural, ownership, workflow, route-law,
validator, public-contract, playbook-route, generated lookup, or mechanics
choices were made in `aoa-playbooks`.

Decision notes explain why a route was chosen. Current playbook, design,
boundary, generated-reader, review-evidence, and sibling-owner authority stays
with the owning source surface.

## Route by task

- New record: use `docs/decisions/TEMPLATE.md`, the nearest decision for the
  same route, and the source surface whose choice is being recorded.
- Existing rationale or index navigation: use `docs/decisions/README.md` and
  the generated lookup indexes, then verify the authored decision.
- Amendment or supersession: inspect the exact current source surface before
  changing the rationale record.

## Boundaries

- Do not use a decision record to make active behavior by itself. If current
  behavior changes, update the active source surface and let the decision
  explain why.
- Give every decision a canonical `Decision ID: AOA-PB-D-####` whose filename
  prefix matches the ID exactly.
- Give every decision an `## Index Metadata` block so lookup indexes can be
  regenerated from source notes instead of hand-maintained crosswalks.
- Treat `indexes/` as generated lookup read models, not rationale authority.
- Keep `modeled_surfaces` in `indexes/index_contract.yaml` as a top-level list
  of normalized repo-relative paths under `docs/decisions/`; do not use it for
  root non-record Markdown.
- Old date-prefixed decision paths stay in git history only. Do not recreate
  date-named stubs or compatibility maps for retired paths.
- Route sibling-owner truth to the owning AoA repository.

## Amendment route

For a small clarification of the same decision, add a dated review note in the
existing file. If a route is materially replaced, preserve the old decision and
add a new canonical decision with explicit supersession prose.

## Validation

Run:

```bash
python scripts/generate_decision_indexes.py --check
git diff --check
```

When decision metadata changes, run `python scripts/generate_decision_indexes.py`
before the `--check` form.

If the decision changes a validated playbook, generated surface, schema,
review-evidence lane, or mechanics surface, run that surface's validator too.

## Closeout

Report which decision was added or changed, whether generated lookup indexes
were refreshed, which source surface it constrains, what validation ran, and
which follow-up route the decision enables.
