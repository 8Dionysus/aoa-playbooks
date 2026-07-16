# AGENTS.md

Root route card for `aoa-playbooks`.

## Purpose

`aoa-playbooks` is the scenario and composition layer of AoA.
It stores recurring operational situations, multi-step compositions, handoff-aware scenarios, fallback paths, evidence posture, and reviewed questline or campaign outline adjuncts.
A playbook coordinates neighboring layers. It does not replace them.

## Owner lane

This repository owns:

- playbook structure, scenario intent, step ordering, fallback, rollback, return, and reanchor posture
- expected evidence posture at the scenario layer
- playbook metadata, generated registries, handoff contracts, failure catalogs, and composition manifests
- questline, campaign, raid, and harvest posture only when defined as playbook-owned reviewed outlines

It does not own:

- technique, skill, eval, routing, role, memory, KAG, shared statistical
  grammar, runtime, or live quest-state truth

It does own the meaning of playbook-local statistical questions and evidence
references exposed through `stats/`. Cross-owner composition and the shared
measurement protocol remain owned by `aoa-stats`.

## Skill and MCP boundary

This repository intentionally has no top-level `skills/` home and no
repo-scoped `.agents/skills/` projection. Shared workflow skills remain owned
by `aoa-skills` and may be supplied by the user profile; copying them here
would create false local ownership and routing competition.

An `aoa-playbooks` owner skill is deferred until a separately owned
`aoa-playbooks-mcp` exposes the playbook capability through a live action/data
interface. That MCP project is outside this repository audit. After it exists,
the skill still requires fresh manual isolated, negative, held-out,
coexistence, and effect trials plus an explicit owner admission decision before
either local skill directory may appear.

## Start here

1. `README.md`
2. `ROADMAP.md`
3. `DESIGN.md` when repository shape, source authority, or owner boundaries move
4. `DESIGN.AGENTS.md` when agent-facing route cards or guidance shape move
5. `mechanics/README.md` and `mechanics/AGENTS.md` when repeatable operation topology moves
6. the relevant model, bundle, gate, or evidence docs referenced there
7. `stats/README.md` and `stats/AGENTS.md` when a playbook-local statistical
   question or reference packet moves
8. the target `playbooks/<branch>/<family>/<slug>/PLAYBOOK.md` or outline surface
9. affected generated registry or composition surfaces
10. neighboring repo docs when the playbook touches their meaning
11. `docs/AGENTS_ROOT_REFERENCE.md` for preserved full root branches


## AGENTS stack law

- Start with this root card, then follow the nearest nested `AGENTS.md` for every touched path.
- Root guidance owns repository identity, owner boundaries, route choice, and the shortest honest verification path.
- Nested guidance owns local contracts, local risk, exact files, and local checks.
- Authored source surfaces own meaning. Generated, exported, compact, derived, runtime, and adapter surfaces summarize, transport, or support meaning.
- Self-agency, recurrence, quest, progression, checkpoint, or growth language must stay bounded, reviewable, evidence-linked, and reversible.
- Report what changed, what was verified, what was not verified, and where the next agent should resume.

## Memory route

For recall, continuity, compaction recovery, comparison with past work, or
preserved lessons, start with `aoa-memo` and the workspace memory map. Session
grounding routes through `.aoa`; local candidate writing routes through this
repository's `memo/` port when that port exists; durable reviewed memory lands
through `aoa-memo`.

## Route away when

- the change is really one skill, reusable technique, proof doctrine, memory object, role contract, routing logic, or runtime state
- the request is to scaffold an `aoa-playbooks` skill before the owner MCP and
  manual admission route exist
- campaign or raid language hides unbounded sprawl or missing anchors

## GitHub landing workflow

Root `AGENTS.md` owns the repository-wide branch, PR, CI, and merge route.
`.github/AGENTS.md` owns the GitHub-native files that support it.

When the user asks to commit, push, and merge in this repository, use this route:

1. Start from a branch based on the current `origin/main`. If the worktree is already dirty, inventory it first and carry forward only the intended diff.
2. Commit the intended change with a message that names the changed surface.
3. Push the branch and open a pull request that states changed surfaces, validation run, skipped checks, and remaining risk.
4. Wait for GitHub `Repo Validation` and any required GitHub checks. If a check fails, fix the branch and wait for the new result.
5. Merge through GitHub after green validation. Use squash unless repository settings report a different required method; report the method that landed.
6. Return to `main`, fast-forward from `origin/main`, and confirm the worktree is clean before closeout.

If GitHub status or merge permissions cannot be observed, stop the landing route and report the exact blocker instead of guessing.

## Verify

Use the nearest `AGENTS.md` for focused checks and `scripts/release_check.py`
for the repository-wide validation route.
If generated playbook surfaces change, regenerate and validate them before finishing.
Use `docs/AGENTS_ROOT_REFERENCE.md` for preserved branch guidance around questline, campaign, raid, reanchor, and evidence posture.

## Report

State which playbook or outline changed, whether semantics or metadata changed, whether fallback, handoff, anchor, reanchor, or evidence posture changed, and what validation ran.

## Full reference

`docs/AGENTS_ROOT_REFERENCE.md` preserves the former detailed root guidance, including hard boundaries and verification questions.

## Design spine

`DESIGN.md` names the system form of the playbook layer.
`DESIGN.AGENTS.md` names the desired form of the agent-facing route mesh.
Use them before adding new root topology, moving repeatable operation pressure,
or changing durable `AGENTS.md` card shape.
`mechanics/README.md` names the checked mechanics atlas, including head-fed
mechanics from `Agents-of-Abyss`, local playbook-native mechanics, placement
audit, legacy-name posture, and the first active package routes under
`mechanics/activation/`, `mechanics/scenario-composition/`,
`mechanics/federation-closure/`, `mechanics/review-gate/`, and
`mechanics/real-run-harvest/`, plus the head-fed/local package landings under
`mechanics/antifragility/`, `mechanics/agon/`, `mechanics/recurrence/`,
`mechanics/checkpoint/`, `mechanics/experience/`, `mechanics/release-support/`,
`mechanics/questbook/`, `mechanics/rpg/`, `mechanics/titan/`, and
`mechanics/portfolio-governance/`.
