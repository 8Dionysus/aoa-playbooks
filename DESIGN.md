# AoA Playbooks System Design

## Role

`DESIGN.md` describes the system form of `aoa-playbooks`.

It is not the README, charter, roadmap, playbook bundle, decision record,
agent-instruction card, generated registry, review note, or release checklist.

It answers one question:

What shape should the AoA scenario and composition layer take as it grows?

## Design Thesis

`aoa-playbooks` is the recurring scenario and composition layer of AoA.

The repository is strongest when it keeps scenario-level method explicit:
trigger boundary, participating roles, skill-family composition, decision
points, handoffs, fallback, rollback, return posture, expected evidence, and
review gates.

A playbook coordinates neighboring layers. It does not replace them.

The playbook owns the recurring route.
The skill owns bounded execution.
The technique owns reusable practice.
The eval owns bounded proof.
The memo layer owns memory and recall truth.
The agent layer owns role meaning.
The routing layer owns dispatch.
The runtime owner owns live execution.

Generated readers and review surfaces help agents orient. They do not become a
second authored playbook canon.

## Design as Appearance

`aoa-playbooks` should appear as a scenario library with a clear public front
door:

- compact root entrypoints;
- a source-authored playbook canon under `playbooks/`;
- design, boundary, lifecycle, and chooser docs under `docs/`;
- generated readers for registry, activation, federation, review, landing, and
  composition posture;
- decision records for topology and route-law rationale;
- local agent cards for nearest-route safety;
- a mechanics atlas for repeatable operation topology around the playbook
  canon, split between head-fed mechanics, local playbook-native mechanics,
  placement audit, legacy-name posture, and package-local implementation moves
  such as `mechanics/activation/`, `mechanics/scenario-composition/`,
  `mechanics/federation-closure/`, `mechanics/review-gate/`, and
  `mechanics/real-run-harvest/`, plus head-fed/local landings such as
  `mechanics/antifragility/`, `mechanics/agon/`,
  `mechanics/recurrence/`, `mechanics/checkpoint/`,
  `mechanics/experience/`, `mechanics/release-support/`,
  `mechanics/questbook/`, `mechanics/rpg/`, `mechanics/titan/`, and
  `mechanics/portfolio-governance/`.

A reader should be able to ask: what recurring situation is this for, what owns
the route, what evidence is expected, where does it hand off, what happens when
it fails, and where should I leave for a stronger owner?

## Design as Anatomy

`aoa-playbooks` is composed of different source classes:

- root public entry and authority surfaces;
- source-authored playbook bundles under `playbooks/*/PLAYBOOK.md`;
- playbook-layer model, boundary, lifecycle, portfolio, and chooser docs under
  `docs/`;
- review evidence under `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/` and `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`;
- source-owned configuration and overrides under `config/`;
- schema, example, script, and test surfaces that make playbook claims
  checkable;
- generated reader surfaces under `generated/`;
- decision records under `docs/decisions/`;
- local memory-port surfaces under `memo/`;
- agent-facing route cards and companion lanes;
- mechanics route surfaces under `mechanics/README.md`, `mechanics/AGENTS.md`,
  and package-local `mechanics/*/README.md`, `PARTS.md`, and `PROVENANCE.md`
  cards that move repeatable operation pressure without absorbing playbook
  source truth.

Each class supports the others. No class should silently steal another class's
authority.

## Design as Operation

A good playbook-layer operation has:

- a named scenario route or owner surface;
- one bounded change target;
- explicit neighboring owner references;
- visible fallback, rollback, return, or reanchor posture;
- an evidence or review path;
- a validation path;
- a generated-freshness path when derived outputs move;
- a closeout path that tells the next reader what changed and what remains.

Scenario moves should become more reviewable, more bounded, and easier to hand
off as they mature.

When a route collapses into one bounded workflow, route it to `aoa-skills`.
When it becomes proof, route it to `aoa-evals`.
When it becomes memory truth, route it to `aoa-memo`.
When it becomes role meaning, route it to `aoa-agents`.
When it becomes reusable practice, route it to `aoa-techniques`.
When it becomes dispatch or live execution, route it to the stronger routing or
runtime owner.

## Design as Aim

The long aim is a playbook canon that can scale beyond a small hand-curated
set without becoming a pile of prompts, runtime folklore, or orchestration
scripts.

The repository should support:

- a readable source-authored playbook canon;
- stable playbook IDs and registry alignment;
- operational family choosers that reduce semantic overlap;
- generated readers for low-context activation and review;
- evidence-led graduation from candidate route to authored playbook;
- checked mechanics atlas and package-local mechanics for repeatable movement
  around canon;
- safe handoff into skills, techniques, evals, memo, agents, routing, stats,
  KAG, and runtime owners without transferring authority by accident.

The canon grows well when every new surface makes scenario selection,
ownership, fallback, evidence, validation, or return clearer than before.

## Design Principles

### 1. Scenario composition before orchestration

A playbook names a recurring scenario and its coordination posture. It should
not become a hidden runner, scheduler, workflow engine, or tool script archive.

### 2. Source before generated

`playbooks/*/PLAYBOOK.md`, source config, and reviewed docs own meaning.
Generated registries, activation surfaces, federation surfaces, review status,
landing governance, and composition manifests summarize or project that
meaning.

### 3. Playbook before campaign theater

Questline, campaign, raid, stress, and Agon language is allowed only when it
makes recurrence, evidence, handoff, or review more bounded. It fails when it
hides missing anchors or unbounded sprawl.

### 4. Evidence before promotion

A route can be tracked before it becomes canonical. Promotion should follow
reviewed evidence, gate posture, and owner-boundary clarity, not enthusiasm or
single-run polish.

### 5. Owner split before absorption

Skills, techniques, evals, memo, agents, routing, stats, KAG, runtime, and
center doctrine have stronger owners. This repository may coordinate them but
should not absorb their truth.

### 6. Mechanics before root sprawl

Repeatable operation topology around the playbook canon belongs in
`mechanics/`. The root stays a route entrypoint: `README.md` names head-fed
mechanics from `Agents-of-Abyss`, local playbook-native mechanics, placement
rules, legacy-name posture, and package shape; `AGENTS.md` names route law.
Package details belong in package cards, parts, provenance, and focused
validators. Root mechanics rosters, audits, templates, scratch notes, and
archive lanes are sprawl.

### 7. Agent guidance is route law

Agent-facing cards should tell an agent where it is, what owns the claim, what
to read, how to verify, and how to hand off. They should not become playbook
source truth by repetition.

### 8. Validation before confidence

Every meaningful change should have a local check, a generated-freshness check
when needed, and a closeout that names skipped checks and remaining risk.

## Good Design Feels Like

- a public reader can find the right scenario route;
- an agent can find the nearest rule without reading the whole repository;
- a maintainer can identify the source owner;
- a generated surface can name its builder and source;
- a candidate can find its review or incubation route;
- a sibling repository can receive a bounded handoff;
- a future contributor can find why the route exists.

## Bad Design Smells Like

- root inflation;
- duplicate playbook doctrine;
- generated files cited as source truth;
- one skill inflated into a playbook;
- one proof note treated as scenario recurrence;
- runtime state hidden in review or quest language;
- campaign or raid language masking missing anchors;
- mechanics pressure scattered across flat docs;
- public promises without validation or owner evidence.

## Relationship to Other Root Surfaces

[`README.md`](README.md) introduces the public repository.
[`CHARTER.md`](CHARTER.md) names the repository authority boundary.
[`AGENTS.md`](AGENTS.md) routes agent work.
[`DESIGN.AGENTS.md`](DESIGN.AGENTS.md) holds the design form of the
agent-facing route mesh.
[`ROADMAP.md`](ROADMAP.md) names current direction.
[`docs/README.md`](docs/README.md) maps the documentation surface.
[`docs/BOUNDARIES.md`](docs/BOUNDARIES.md) names owner boundaries.
[`mechanics/portfolio-governance/parts/model-spine/docs/playbook-model.md`](mechanics/portfolio-governance/parts/model-spine/docs/playbook-model.md) defines the conceptual
playbook model.
[`mechanics/portfolio-governance/parts/operational-family/docs/playbook-operational-family.md`](mechanics/portfolio-governance/parts/operational-family/docs/playbook-operational-family.md)
routes chooser pressure across overlapping operational playbooks.
[`mechanics/README.md`](mechanics/README.md) routes repeatable operation
topology, including head-fed and local mechanics, placement rules, legacy-name
posture, package shape, and the root-file rule. [`mechanics/AGENTS.md`](mechanics/AGENTS.md)
keeps that lane as route law. [`mechanics/activation/README.md`](mechanics/activation/README.md)
routes activation,
[`mechanics/scenario-composition/README.md`](mechanics/scenario-composition/README.md)
for scenario-composition,
[`mechanics/federation-closure/README.md`](mechanics/federation-closure/README.md)
for federation closure,
[`mechanics/review-gate/README.md`](mechanics/review-gate/README.md) for
review readouts, and
[`mechanics/real-run-harvest/README.md`](mechanics/real-run-harvest/README.md)
for package-local evidence posture, and
[`mechanics/antifragility/README.md`](mechanics/antifragility/README.md) for
stress-lane, re-entry gate, harvest, runtime-chaos, and via negativa payloads,
and [`mechanics/agon/README.md`](mechanics/agon/README.md) for trial,
kernel-binding, campaign, adoption, and recurrence-adapter choreography
payloads. Package-active route packages such as
[`mechanics/recurrence/README.md`](mechanics/recurrence/README.md),
[`mechanics/checkpoint/README.md`](mechanics/checkpoint/README.md),
[`mechanics/experience/README.md`](mechanics/experience/README.md),
[`mechanics/release-support/README.md`](mechanics/release-support/README.md),
[`mechanics/questbook/README.md`](mechanics/questbook/README.md),
[`mechanics/rpg/README.md`](mechanics/rpg/README.md),
[`mechanics/titan/README.md`](mechanics/titan/README.md), and
[`mechanics/portfolio-governance/README.md`](mechanics/portfolio-governance/README.md)
validate public root/source routes without moving them by directory name.
[`docs/decisions/`](docs/decisions/README.md) preserves topology and route-law
rationale.

`DESIGN.md` holds the system form of the playbook layer.

## Use by Agents

Agents should consult this file when a change alters:

- repository shape;
- root surfaces;
- playbook topology;
- source versus generated authority;
- future mechanics boundaries;
- review, evidence, or gate posture;
- scenario versus skill, proof, memory, role, routing, or runtime boundaries;
- agent-facing layer design;
- neighboring owner handoffs.

This file does not override local owner truth. It tells agents what kind of
shape the playbook layer is preserving.
