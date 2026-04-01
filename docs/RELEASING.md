# Releasing `aoa-playbooks`

This guide defines the bounded publication flow for `aoa-playbooks`.

`aoa-playbooks` is released as a repository of scenario-level doctrine, authored playbook bundles, reviewed evidence notes, and derived activation/federation/review-status/composition surfaces.

See also:
- [Documentation Map](README.md)
- [PLAYBOOK_EXECUTION_SEAM](PLAYBOOK_EXECUTION_SEAM.md)
- [PLAYBOOK_GAP_MATRIX](PLAYBOOK_GAP_MATRIX.md)
- [CHANGELOG](../CHANGELOG.md)

## Release goals

A release should make it easy to answer:

- what changed
- why it matters
- how it was validated
- what evidence is still intentionally missing
- what is intentionally not included

## Recommended release flow

1. Confirm the release scope stays bounded.
2. Update `CHANGELOG.md` with the section that will anchor the human release narrative.
3. Run the repo-level validation loop:
   - `python -m pip install -r requirements-dev.txt`
   - `python scripts/generate_playbook_activation_surfaces.py --check`
   - `python scripts/generate_playbook_federation_surfaces.py --check`
   - `python scripts/generate_playbook_review_status.py --check`
   - `python scripts/generate_playbook_composition_surfaces.py --check`
   - `python scripts/validate_playbooks.py`
4. If the release touches validator behavior directly, also run:
   - `python -m unittest tests.test_validate_playbooks`
5. Confirm generated surfaces are current when the release touches authored bundles, schemas, cohort membership, or composition overrides.
6. Confirm reviewed-summary and gate-review wording still match the current evidence posture.
7. Review public-safety hygiene:
   - no secrets
   - no private topology
   - no raw operational traces
   - no implied authority moved out of source repos
8. If the release depends on a sibling-repo bridge, merge the source-owned upstream change first.
9. Merge the release-prep PR to `main`.
10. Create a Git tag such as `v0.1.0`.
11. Publish GitHub release notes from the matching changelog section or a clearly equivalent human-first shape.

## Release note shape

Recommended changelog and GitHub release-note sections:

- summary
- added
- changed
- included in this release
- validation
- notes

Exact headings do not need to be rigid, but the changelog entry and the published GitHub release should answer the same questions in roughly the same shape.

## Versioning guidance

Suggested interpretation:

- `0.x.y` for early public baselines, doctrine shaping, and seam hardening
- `1.0.0` only when the repository structure, release path, and evidence expectations feel stable enough to promise a durable public baseline

## What not to optimize yet

For now, avoid:

- package-publication theater without a real package artifact
- per-playbook version metadata that duplicates changelog or registry truth
- release automation that promises more than the current validator actually proves
- overstating `hold` playbooks as if they were already evidence-complete

## Current stance

Right now, `aoa-playbooks` is best released as:

- a curated public playbook and scenario-composition corpus
- a repository with bounded authored, activation, federation, and composition seams
- a validator-backed repo whose strongest next moves are still evidence-led rather than catalog-led
- a release identity anchored in `CHANGELOG.md`, the Git tag, and the GitHub release body rather than any package registry
