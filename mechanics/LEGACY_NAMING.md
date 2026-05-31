# Mechanics Legacy Naming

## Role

This note defines how `aoa-playbooks` treats old or overloaded mechanics names
while the mechanics refactor moves from skeleton to package landings.

It is a posture guide, not an archive.

Use it to classify a name before moving, renaming, or preserving a payload.
Concrete old-path lookup belongs in the owning package `PROVENANCE.md` and, if
needed, package-local `legacy/` indexes after the active route exists.

## Operating Card

| Field | Route |
| --- | --- |
| role | classify old and overloaded mechanics names before package movement |
| input | old root path, wave name, generated field, accepted compatibility path, candidate route, or sibling-mechanic vocabulary |
| output | name posture, active owner route, provenance route, rename gate, or stop-line |
| owner | `mechanics/LEGACY_NAMING.md` owns posture vocabulary; package `PROVENANCE.md` owns concrete former-path accounting |
| next route | `mechanics/PLACEMENT_AUDIT.md`, target package `README.md`, target package `PARTS.md`, package `PROVENANCE.md`, then package-local `legacy/` only when needed |
| validation | `python scripts/validate_mechanics_skeleton.py` and package-local validators when payloads move |

## Active-First Rule

Start from the active owner before archive context:

1. root `AGENTS.md`, `DESIGN.md`, and `DESIGN.AGENTS.md`;
2. `mechanics/README.md`, `HEAD_MECHANICS.md`, and `LOCAL_MECHANICS.md`;
3. `mechanics/PLACEMENT_AUDIT.md` for current placement status;
4. the target package route card, part map, and package validator;
5. package `PROVENANCE.md` for former-path lookup;
6. package-local `legacy/` only when the package has real former paths or raw
   source receipts to preserve.

Do not create a root `legacy/` directory for mechanics accounting.

## Name Postures

| Posture | Meaning | Use |
| --- | --- | --- |
| `active` | current package, part, source, generated, or public route name | use in new route cards, validators, and docs |
| `historical` | old root path, wave name, release-stage name, or prior placement | preserve in package `PROVENANCE.md` after active placement is known |
| `accepted-input` | old path or name still accepted by builders, schemas, examples, tests, generated readers, or sibling refs | keep compatibility visible until a validator-backed compatibility change lands |
| `generated-projection` | name carried by generated files or generated fields | rebuild from source and keep weaker than authored source |
| `candidate-only` | named pressure that is rostered but not yet an operational package | do not move payloads into it until package acceptance is proven |
| `provenance-bridge` | package-local bridge from active surfaces into history | enter only after active surfaces are insufficient |
| `root-public` | root entrypoint or published read model intentionally retained at root | keep root path and explain why in `PLACEMENT_AUDIT.md` |
| `stronger-owner` | vocabulary whose source truth belongs to another repo | route out instead of localizing authority |

## Legacy Is Not A Root Folder

For this repository, `legacy` means package-local provenance for a mechanics
move. It does not mean a root archive lane.

Allowed forms:

- `mechanics/<package>/PROVENANCE.md`
- `mechanics/<package>/legacy/INDEX.md`
- `mechanics/<package>/legacy/DISTILLATION_LOG.md`
- `mechanics/<package>/legacy/raw/` only when real source receipts exist

Disallowed form:

- `legacy/` at repository root for mechanics paths

Root `legacy/` would make old names look like an alternate active route. The
playbook layer needs the opposite: active owner first, former path second.

## Rename Gate

A rename is a topology change. Before changing a public path, package name,
part name, schema field, generated filename, accepted input, or source ref,
collect:

1. current owner route;
2. source surface that owns meaning;
3. old-path or old-name posture from this note;
4. generated reader and builder impact;
5. validator constants and regression tests;
6. decision record when the route will matter to future agents.

If the chain is incomplete, keep the current path and record the ambiguity in
`PLACEMENT_AUDIT.md` or the owning package roadmap instead of renaming.

## Current High-Risk Legacy Names

| Name family | Current posture | Positive route |
| --- | --- | --- |
| `Wave VI`, `Wave XIII`, `Wave XVI`, `wave16` | `historical` release-wave and landing labels | map through `mechanics/agon/PROVENANCE.md` after the Agon package lands |
| `trial-playbook-surfaces`, `trial-kernel-bindings` | `accepted-input` recurrence component names | route through Agon package parts while manifests remain validated |
| `chaos-wave1`, `wave 3 stress` | `historical` stress-lane landing names | route through `antifragility` package once accepted |
| `phase-alpha` | `accepted-input` review/readiness route | route through `review-gate` or `real-run-harvest` depending on payload class |
| `questbook`, `QUESTBOOK.md`, `quests/` | `root-public` and source-store vocabulary | keep root source/readout surfaces; mechanics owns route law only |
| `Titan` | `stronger-owner` plus local playbook route pressure | do not claim role authority; route local drills only if a Titan package lands |
| `playbook_activation.*.example.json` | `accepted-input` public example path | keep root example refs unless a compatibility-backed move lands |

## Stop Lines

- Do not use old names as active package names when a clearer active route is
  known.
- Do not preserve old paths by duplicating authority.
- Do not treat generated field names as source names.
- Do not promote a candidate-only roster row because a filename matched it.
- Do not move authored `playbooks/*/PLAYBOOK.md` into mechanics.
