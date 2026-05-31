# Boundary Contract Split

Playbook: `invariants-first-refactor`

Use when a refactor is noisy enough that boundary mapping and contract verification should be split explicitly.

Expected split:

- boundary mapper returns a context map and interface notes
- contract verifier returns contract assumptions and invariant candidates
