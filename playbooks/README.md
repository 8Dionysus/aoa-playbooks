# Playbook Source Home

`playbooks/` is the canonical source tree for authored scenario bundles.

Each source object is still one compact `PLAYBOOK.md`. The tree adds route
shape around those objects so a reader can find the right scenario family
without scanning a flat list.

The checked topology lives in
[`source_home.manifest.json`](source_home.manifest.json). It names every active
branch, family, bundle slug, and source path.

## Route Map

| Branch | Family | Use for |
| --- | --- | --- |
| `operations/` | `change/` | bounded repository changes, invariant refactors, source-truth cleanup, and project-scoped safe changes |
| `operations/` | `recovery/` | diagnosis, remediation, incident routing, runtime stress, and re-entry playbooks |
| `operations/` | `release/` | release, cutover, trusted rollout, and reviewed automation follow-through |
| `operations/` | `orchestration/` | multi-tier or model-orchestration scenarios |
| `continuity/` | `checkpoint/` | checkpoint, child-return, distillation closure, and closeout owner-routing routes |
| `continuity/` | `session-growth/` | harvest, owner follow-through, self-agency continuity, restartable inquiry, and growth cycles |
| `federation/` | `cross-repo/` | ordered cross-repo rollout and workspace foundation routes |
| `federation/` | `owner-landing/` | owner-first landing, publisher activation, and seed-pack publication |
| `agon/` | `trials/` | pre-protocol mechanical trial playbooks |
| `agon/` | `campaigns/` | repeated campaign playbooks built from reviewed trial pressure |
| `experience/` | `certification/` | experience certification and forge scenarios |
| `titan/` | `closeout/` | Titan-backed closeout and audit routes |

## Bundle Contract

Each authored bundle lives at:

```text
playbooks/<branch>/<family>/<slug>/PLAYBOOK.md
```

The `<slug>` must match frontmatter `name`.

Do not add flat compatibility aliases under `playbooks/<slug>/`. Compatibility
belongs in generated readers, docs links, or deterministic path resolvers.

Do not add per-bundle `AGENTS.md` by default. Bundle truth belongs in
`PLAYBOOK.md`; family route shape belongs in this README and the source-home
manifest.

## Source Split

- `PLAYBOOK.md` owns scenario intent, trigger, ordering, handoffs, fallback,
  evidence posture, artifacts, eval anchors, memory writeback, and canonical
  route.
- `mechanics/` owns repeatable operation topology around playbooks.
- `generated/` owns compact read models.
- neighboring repos own skills, agents, eval proof, durable memory, routing,
  runtime, stats, and KAG truth.

## Validation

```bash
python scripts/validate_playbooks.py
python scripts/validate_nested_agents.py
```

For release-bound changes, run:

```bash
python scripts/release_check.py
```
