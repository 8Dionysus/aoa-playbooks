# Allow a Checked Compact Mechanics Package Tier

## Status

Accepted.

## Index Metadata

- Decision ID: AOA-PB-D-0017
- Original date: 2026-07-25
- Surface classes: mechanic package, docs route, source topology, validation guard, decision record
- Playbook routes: none
- Mechanic parents: release-support
- Guard families: package route, source topology, validation guard, AGENTS/mesh, generated/read-model
- Posture: accepted compact release-support navigation tier

## Context

The release-support package carried four navigation documents even though
`PARTS.md` and `PROVENANCE.md` had no independent non-generated consumer and
had not evolved independently since package localization. Their semantic
content remained necessary, but separate files were no longer load-bearing.

## Options Considered

- Keep the four-file package shape mandatory for every mechanics package.
- Delete the companions without replacing their route and provenance guards.
- Allow a checked compact tier while retaining the full companion tier.

## Decision

Every mechanics package keeps `AGENTS.md` and `README.md`. A compact package
embeds checked `## Parts` and `## Provenance` sections in README. A larger
package may keep `PARTS.md` and `PROVENANCE.md`, but the companion files must
exist as a complete pair.

Release-support adopts the compact tier. The other mechanics packages retain
their current full tier until their own owner-local evidence supports a change.

## Rationale

This removes two navigation hops without removing package ownership, part
identity, provenance, accepted-input lineage, stronger-owner boundaries, or
validation. The shared validators own only the two legal shapes; the
release-support validator continues to own package-specific meaning.

## Consequences

- Positive: release-support has one semantic README instead of three
  overlapping navigation documents.
- Positive: an incomplete companion pair and missing compact sections fail
  closed.
- Tradeoff: generic mechanics validators now understand two explicit local
  tiers.
- Follow-up: any second compact package needs its own consumer, semantic,
  mutation, generated-index, release, and rollback proof.

## Current Applicability

As of 2026-07-25:

- Valid: release-support is the only compact package.
- Valid: all other packages retain their full companion pair.
- Superseded by: none.

## Boundaries

- This does not move or remove package payloads.
- This does not remove package `AGENTS.md` or its focused validator.
- This does not infer that companion files are overcode in other packages.
- This does not move source playbook, CI, runtime, KAG, or stronger-owner
  authority.

## Source Surfaces

- `mechanics/AGENTS.md`
- `mechanics/README.md`
- `mechanics/release-support/README.md`
- `scripts/validate_mechanics_skeleton.py`
- `scripts/mechanic_package_validator.py`
- `mechanics/release-support/scripts/validate_release_support_package.py`
- `tests/test_mechanics_skeleton.py`
- `tests/test_package_local_mechanics_packages.py`
- `docs/decisions/AOA-PB-D-0013-package-local-mechanics-payloads.md`

## Follow-Up Route

Keep release-support on the compact tier. Reopen another package only through
its own bounded owner proof.

## Verification

Verification is owned by the focused package and mechanics tests, decision
index checks, generated KAG freshness route, and repository release gate.
