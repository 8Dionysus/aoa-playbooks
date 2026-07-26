# AoA Playbooks Agent Surface Design

## Role

`DESIGN.AGENTS.md` describes the desired form of agent-facing guidance within
`aoa-playbooks`.

It is not an `AGENTS.md` card, playbook bundle, prompt library, policy matrix,
charter, roadmap, schema, validator, generated index, or review note.

It answers one question:

What shape should agent-facing surfaces take so agents can change the playbook
canon without losing scenario truth, generated boundaries, evidence,
reviewability, or return routes?

## Design Thesis

`aoa-playbooks` should not give agents one giant instruction wall.

It should give them a navigable route mesh:

- a root card that names repository identity, owner boundaries, route choice,
  validation posture, and landing workflow;
- district cards for durable editable surfaces such as `playbooks/`,
  `generated/`, `config/`, `examples/`, `schemas/`, `scripts/`, `tests/`,
  `memo/`, `stats/`, and `docs/decisions/`;
- playbook source surfaces that keep scenario meaning stronger than generated
  summaries;
- mechanics atlas cards, placement/legacy gates, and mechanic package cards
  that route repeatable operation topology without becoming playbook canon;
- generated cards that protect derived readers from hand edits;
- review, gate, and decision cards that preserve why a route moved;
- closeout contracts that let the next agent resume without archaeology.

Agent guidance is useful when it routes to the nearest owner surface and stops
before stealing authority from that surface.

The root names the playbook-layer road system.
The nearest card narrows the lane.
The authored playbook keeps scenario truth.
The builder carries derived surfaces.
The validator tests the claim.
The closeout returns the work to reviewable memory.

## Design as Appearance

Agent guidance should appear as a readable route network.

A healthy `aoa-playbooks` agent-facing layer has:

- a clear root `AGENTS.md`;
- local `AGENTS.md` cards in durable editable districts;
- explicit owner boundaries for authored playbooks, generated surfaces,
  config, scripts, schemas, tests, examples, memo-port output, decisions,
  review evidence, and future mechanics packages;
- named validation routes near the work;
- negative boundaries that say what must not be claimed;
- closeout expectations for changed surfaces, skipped checks, remaining risk,
  and next owner route;
- generated companions that help navigation without becoming source truth.

A low-context agent should be able to answer: where am I, what owns this, what
must I read, what must I not claim, how do I verify, and where do I hand off?

## Design as Anatomy

The agent-facing layer has several different surface classes.

### Root card

The root `AGENTS.md` owns repository identity, route modes, owner boundaries,
cross-repository routing, broad validation posture, GitHub landing workflow,
and closeout expectations.

It should route to local truth. It should not contain every playbook,
mechanic, script, or generated-surface rule.

### District cards

District cards own local risks and source surfaces for durable editable
districts such as `playbooks/`, `generated/`, `config/`, `examples/`,
`schemas/`, `scripts/`, `tests/`, `memo/`, `stats/`, and `docs/decisions/`.

They narrow the root card. They do not overturn it.

### Playbook source cards

`playbooks/AGENTS.md` protects the authored scenario canon under
`playbooks/*/*/*/PLAYBOOK.md`.

It should keep the split between scenario route, neighboring owner references,
generated registry metadata, and review evidence visible.

### Mechanics Root and Package Cards

The mechanics route starts at `mechanics/AGENTS.md` and `mechanics/README.md`.

The root has only two mechanics docs: `README.md` and `AGENTS.md`. It routes
head-fed mechanics that begin in `Agents-of-Abyss`, local mechanics born inside
this repository, placement rules, legacy-name posture, and package shape.

Do not add root-level mechanics rosters, audits, templates, backlog files,
scratch notes, migration notes, or `_meta/` lanes. Active detail belongs in the
owning package. Historical rationale belongs in `docs/decisions/`. Former-path
accounting belongs in the package README provenance section or its
`PROVENANCE.md` companion and package-local `legacy/` only after the active
route exists.

`mechanics/activation/`, `mechanics/scenario-composition/`,
`mechanics/federation-closure/`, `mechanics/review-gate/`, and
`mechanics/real-run-harvest/` are the first active local packages. They own
dedicated builder implementations and package-local evidence posture while
keeping root generated outputs and root command compatibility intact.

`mechanics/antifragility/` and `mechanics/agon/` are package-active head-fed
mechanics in this repo. They own playbook-local stress, re-entry, trial,
kernel-binding, campaign, adoption, and recurrence-adapter payloads while
keeping source playbook canon in `playbooks/`.

`mechanics/recurrence/`, `mechanics/checkpoint/`,
`mechanics/experience/`, `mechanics/release-support/`,
`mechanics/questbook/`, `mechanics/rpg/`, `mechanics/titan/`, and
`mechanics/portfolio-governance/` are package-active route packages. They make
owner, input, output, next route, and validation explicit while leaving only
true root contracts at the repository root.

Future mechanic cards should describe repeatable movement around the playbook
canon: activation, review gates, recurrence, release support, runtime-seam
rehearsal, questbook support, and cross-owner handoff
pressure.

They should name local source surfaces, part-local validation, generated
mirrors, and stronger-owner stop lines.

They should not become authored playbook meaning by proximity.

### Generated cards

Generated cards protect derived read models. They should name the builder or
source config before any edit route.

They must say when a file is not hand-authored.

### Review and decision cards

Review notes, gate reviews, decision records, incubation notes, and memo-port
surfaces preserve why a route moved or why it stayed bounded.

They are not substitutes for changing the active source surface when active
meaning has changed.

## Design as Operation

A safe agent move in `aoa-playbooks` follows this route before content
mutation:

1. Read the root card.
2. Read `DESIGN.md` when repository shape, source authority, or owner boundary
   is changing.
3. Read this file when agent-facing route law, local cards, or guidance shape
   is changing.
4. Read the nearest nested `AGENTS.md` for every touched path.
5. Read the source playbook, config, schema, builder, review note, decision, or
   generated-source owner that owns the claim.
6. Make the smallest change that preserves the owner boundary.
7. Regenerate derived surfaces from source when a source-backed derived layer
   moved.
8. Run the narrowest relevant validation first, then broader gates when the
   change is release-facing, route-facing, generated, structural, or
   cross-owner.
9. Close out with changed surfaces, checks run, checks skipped, remaining
   risk, decision-review result, and next owner route.

Agency becomes stronger when it can stop, explain itself, and hand off
cleanly.

## Design as Authority

Agent guidance in `aoa-playbooks` may:

- route work;
- name local risks;
- name owner surfaces;
- require reading order;
- require validation;
- set closeout shape;
- prevent common unsafe claims.

It must not:

- override authored playbook meaning;
- override source docs, schemas, configs, builders, validators, or owner repos;
- claim hidden autonomy;
- claim live runtime state unless the runtime owner proves it;
- claim skill, technique, eval, memo, routing, role, shared stats grammar or
  cross-owner composition, KAG, or center doctrine authority;
- turn generated surfaces into authority;
- convert AoA vocabulary into permission;
- bury semantic changes under docs-only wording.

The agent layer is route law. It is not the playbook canon, proof system,
skill runtime, memory layer, routing engine, or live orchestrator.

## Operational Map Shape

Prefer route cards that answer:

| Field | Meaning |
| --- | --- |
| role | what this surface does |
| input | what enters here |
| output | what leaves here |
| owner | which surface owns truth |
| next route | where to go next |
| tools | what to run or inspect |
| validation | how to prove the route held |

When a boundary is needed, state the positive route that handles the pressure.

## Canonical Card Shape

Every durable `AGENTS.md` card that adopts the canonical shape should begin
from this form:

```markdown
# AGENTS.md

## Applies to

## Role

## Read before editing

## Boundaries

## Validation

## Closeout
```

`Applies to` names scope.
`Role` names what the lane is for.
`Read before editing` gives the minimum route.
`Boundaries` prevents authority drift.
`Validation` turns action into checkable work.
`Closeout` preserves handoff memory.

Optional sections may be added when the lane needs them: `Purpose`, `Owner
lane`, `Route modes`, `Source Surfaces`, `Post-change route review`, `Editing
posture`, `Decision review`, `Generated companions`, or local equivalents.

Optional sections should sharpen the route. They should not decorate it into
fog.

## Relationship to Other Surfaces

`README.md` introduces the repository.
`CHARTER.md` names the repository authority boundary.
`DESIGN.md` names the playbook-layer system form.
`AGENTS.md` routes agent work in the repository.
Nested `AGENTS.md` cards narrow local work.
`docs/README.md` maps documentation.
`docs/BOUNDARIES.md` names owner boundaries.
`docs/decisions/` preserves topology and route-law rationale.
`mechanics/AGENTS.md`, `mechanics/README.md`, and package-local
`mechanics/*/AGENTS.md` cards route repeatable operation topology during
package growth.
`generated/` remains a derived companion.
`Spark/` remains a companion lane; it is not authored playbook meaning.
There is no repository-local skill lane. A future `aoa-playbooks` skill must
follow a separately owned `aoa-playbooks-mcp` and a new manual admission
decision; shared profile skills must not be copied into this route mesh.

`DESIGN.AGENTS.md` holds the design form of the agent-facing layer.

It tells humans and agents what kind of agent guidance they are preserving
when they add, move, split, validate, generate, or port `AGENTS.md` surfaces.

## Portability to Sibling Projects

Sibling repositories may adopt this shape without adopting `aoa-playbooks`
truth.

The portable minimum is:

- one root `AGENTS.md`;
- local cards for durable editable districts;
- explicit owner surfaces;
- explicit negative boundaries;
- validation named close to the work;
- closeout that records changed surfaces, checks, skipped checks, risk, and
  next route;
- generated summaries only when they remain source-linked and reproducible.

Port the shape, then let the local owner speak in its own tongue.

## Use by Agents

Agents should consult this file when a change alters:

- the shape of any `AGENTS.md` card;
- root-to-local precedence;
- route modes or reading order;
- validation authority;
- generated or exported agent-facing companions;
- closeout requirements;
- local card placement;
- cross-repository owner routing;
- adapter vocabulary in agent-facing guidance;
- future mechanics card posture.

This file does not override local owner truth. It tells agents what kind of
agent-facing form they are preserving.

## Landing Rule

When this design changes, review whether the following surfaces also need to
move:

- root `AGENTS.md`;
- affected nested `AGENTS.md` cards;
- `README.md`;
- `docs/README.md`;
- `ROADMAP.md`;
- validators for root design, local cards, generated freshness, and release
  checks;
- generated companions when a source-backed machine capsule changed;
- `CHANGELOG.md` and `docs/decisions/` when root or route-law meaning changed.

Only update a surface when its meaning actually moved. The design is a compass,
not a broom.
