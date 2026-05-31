# Mechanic Package Template

Use this template only when a roster row is ready to become a child package.

Replace `<slug>`, `<class>`, and bracketed notes before landing.

## Required files

A first package landing should create:

- `mechanics/<slug>/AGENTS.md`
- `mechanics/<slug>/README.md`
- `mechanics/<slug>/PARTS.md`
- `mechanics/<slug>/PROVENANCE.md`

Add `docs/`, `parts/`, `schemas/`, `examples/`, `config/`, `generated/`,
`scripts/`, or `tests/` only when those homes have real payloads and local
validation.

## README shape

```markdown
# <Mechanic Name>

## Mechanic card

| Field | Route |
| --- | --- |
| class | <head-fed or local> |
| role |  |
| trigger |  |
| playbooks owns |  |
| stronger owner split |  |
| inputs |  |
| outputs |  |
| must not claim |  |
| validation |  |
| next route |  |

## Active route

## Functioning parts

## Source surfaces

## Owner boundary

## Growth posture
```

## AGENTS shape

```markdown
# AGENTS.md

## Applies to

## Role

## Read before editing

## Boundaries

## Validation

## Closeout
```

## PARTS shape

```markdown
# <Mechanic Name> Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |

## Deferred payloads

## Part growth rule
```

## PROVENANCE shape

```markdown
# <Mechanic Name> Provenance

## Active-first rule

## Center or local origin

## Previous placement

## Legacy boundary
```

## Validation

Every package creation must update or add:

- `scripts/validate_mechanics_skeleton.py` or a narrower package validator;
- tests for the new package route;
- `docs/decisions/` when package creation changes topology or owner split;
- generated/readout checks if source-backed generated surfaces move.
