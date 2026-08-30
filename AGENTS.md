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

## Route by task

The inherited card and the nearest nested `AGENTS.md` define the active
instruction chain. Load only the owner sources needed by the task:

- public orientation or contributor entrypoint: `README.md`
- current direction: `ROADMAP.md`
- repository shape, source authority, or owner boundaries: `DESIGN.md`
- agent-card shape or guidance topology: `DESIGN.AGENTS.md`
- repeatable operation topology: `mechanics/AGENTS.md`; use
  `mechanics/README.md` for the public package atlas, placement, or provenance
- a playbook-local statistical question: `stats/AGENTS.md` and
  `stats/port.manifest.json`; use `stats/README.md` for human orientation
- scenario meaning: the target
  `playbooks/<branch>/<family>/<slug>/PLAYBOOK.md`
- a derived reader: its source config or builder before the generated output
- a neighboring-owner claim: that owner's source contract
- legacy root-law archaeology: `docs/AGENTS_ROOT_REFERENCE.md`


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
`mechanics/README.md` is the checked public atlas for active package routes,
class, placement, and legacy-name posture. `mechanics/AGENTS.md` carries the
agent-facing package law; nearest package cards carry the local delta.
