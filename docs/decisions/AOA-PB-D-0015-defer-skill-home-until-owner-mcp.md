# Defer Skill Home Until Owner MCP

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0015
- Original date: 2026-07-16
- Surface classes: root/topology, agent route, docs route, decision record, validation guard, codex projection
- Playbook routes: none
- Mechanic parents: none
- Guard families: source topology, validation guard, projection guard, runtime seam, AGENTS/mesh, sibling-owner boundary
- Posture: accepted no local skill home before owner MCP

## Context

The repository carried a copied catalog of shared `aoa-skills` bundles under
`.agents/skills/` but owned no canonical skill home. Those copies made foreign
workflows look repository-owned and competed with the same shared capabilities
when supplied through the user profile.

Manual work compared direct owner-document use with a temporary
`aoa-playbooks` front-door candidate. The candidate improved retrieval on some
selection cases and preserved important negative boundaries, but it still
acted as filesystem-search guidance over playbook documents. It did not expose
an executable playbook capability or live owner access plane. The candidate
and its task-local trial artifacts were therefore scaffolding, not an admitted
repository capability.

## Options Considered

- Keep the copied shared catalog as a convenient local projection.
- Admit the text-only owner front door and defer tool integration.
- Remove all local skill copies and defer any owner skill until a dedicated
  `aoa-playbooks-mcp` exists.

## Decision

Keep both `skills/` and `.agents/skills/` absent from `aoa-playbooks`.

Shared workflow skills stay owned by `aoa-skills` and may be supplied through
the user profile or another declared shared runtime surface. They are not
copied into this repository.

An `aoa-playbooks` owner skill may be reconsidered only after a separately
owned `aoa-playbooks-mcp` provides the live action and data interface that the
skill will route. Building that MCP is outside this change. Its eventual
existence is necessary but not sufficient: the skill must then pass fresh
manual isolated, negative, held-out, coexistence, and effect trials and receive
an explicit owner admission decision before a canonical home or repo
projection is created.

Do not create an empty `skills/` port as a placeholder.

## Rationale

A playbook skill without its owner access plane would package search advice as
if it were an executable, composable capability. That would blur the intended
split between skill procedure, MCP action/data access, and playbook scenario
truth. Removing the foreign catalog also reduces prompt-visible routing
competition without transferring shared skill ownership into this repository.

Deferral preserves the useful manual findings while avoiding premature
admission. A future MCP-backed proposal can be evaluated against the same real
selection and boundary cases instead of inheriting success from a temporary
text-only candidate.

## Consequences

- Positive: repository-local agent discovery no longer advertises copied
  shared bundles as `aoa-playbooks` capabilities.
- Positive: future skill work has an explicit MCP-first prerequisite and must
  still prove added value manually.
- Positive: authored playbooks, generated readers, and cross-owner skill
  handoff contracts keep their current owners.
- Tradeoff: agents select and review playbooks through owner documents and
  existing generated navigation surfaces until an MCP-backed capability is
  designed.
- Follow-up: a future, separately scoped `aoa-playbooks-mcp` project may reopen
  owner-skill admission.

## Current Applicability

As of 2026-07-16:

- Valid: no top-level `skills/` home exists.
- Valid: no repo-scoped `.agents/skills/` projection exists.
- Valid: shared workflow skills remain external to this repository.
- Valid: `aoa-playbooks-mcp` is not part of the current work.
- Superseded by: none.

## Review Log

### 2026-07-16 - Owner skill boundary audit

- Previous assumption: copied shared skills could remain a useful companion
  lane or a text-only owner skill could be admitted first.
- New reality: a playbook-owned callable capability requires its MCP access
  plane before local skill admission is meaningful.
- Reason: preserve the skill/MCP/playbook separation and avoid false local
  ownership.
- Source surfaces updated: root routes, agent-surface design, quest-harvest
  posture, obsolete test and validator exceptions, and decision indexes.
- Validation: manual positive, negative, held-out, and coexistence work;
  prompt-visible inspection; focused owner tests; repository release gate.

## Boundaries

- This decision applies to `aoa-playbooks`; it does not claim that every skill
  in the wider ecosystem requires a dedicated MCP.
- This decision does not authorize or scaffold `aoa-playbooks-mcp`.
- This decision does not remove playbook references to skills owned by
  `aoa-skills` or their generated handoff contracts.
- Historical changelog and reviewed-run references remain historical evidence,
  not current installation instructions.
- A future MCP does not automatically admit a skill or prove routing quality.

## Source Surfaces

- `AGENTS.md`
- `README.md`
- `DESIGN.AGENTS.md`
- `QUESTBOOK.md`
- `tests/test_skill_home_boundary.py`
- `scripts/validate_nested_agents.py`
- `aoa-skills:docs/decisions/AOA-SK-D-0040-owner-skill-homes-and-projection-boundaries.md`
- `aoa-skills:docs/decisions/AOA-SK-D-0041-minimal-owner-home-port-contract.md`

## Follow-Up Route

Design `aoa-playbooks-mcp` as a separate owner project. After it has a live,
reviewable contract, reopen owner-skill work from new manual trials rather than
from this session's discarded candidate.

## Verification

Verification is owned by the focused skill-home boundary test, nested-agent
validator, decision-index generator, prompt-visible inspection, KAG rebuild,
and repository release gate. Structural green checks do not prove future MCP
or skill usefulness.
