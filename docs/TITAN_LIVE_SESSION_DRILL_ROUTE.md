# Titan Live Session Drill Route

This route is a live-session drill, not runtime automation. Each drill must
leave visible evidence and an explicit fallback before the next gate opens.

## Drill 1: Read-Only Mapping

- Bearers: Atlas, Sentinel, Mneme.
- Step: map owner repos, route risks, and memory anchors without mutating files.
- Required evidence: named repo roots, source docs read, and any unresolved
  ambiguity or owner-route risk.
- Fallback: if owner fit is unclear, stop at a route note and do not open Forge.
- Review gate: another operator can see why the selected owner route is bounded.

## Drill 2: Forge Mutation Gate

- Bearer: Forge.
- Step: open only after a mutation payload names scope, expected files,
  rollback note, approval ref, and test plan.
- Required evidence: the gate payload plus before/after diff for every touched
  file.
- Fallback: if scope expands or expected files drift, close the gate as aborted,
  keep the receipt, and return to Drill 1 for remapping.
- Review gate: every mutation has a named rollback path and no hidden extra
  owner layer.

## Drill 3: Delta Judgment Gate

- Bearer: Delta.
- Step: judge the mutation against named criteria and evidence refs before
  promotion or merge.
- Required evidence: criteria, evidence refs, verdict scope, validation output,
  and any remaining risk.
- Fallback: if evidence is missing or validation is red, mark the verdict
  blocked and return to Forge with the failed criterion.
- Review gate: the verdict can be checked without trusting operator memory.

## Drill 4: Mneme Memory Humility

- Bearer: Mneme.
- Step: record only route-to-source memory candidates, never proof claims.
- Required evidence: source refs that resolve locally or externally, authority
  label, and temporal posture.
- Fallback: if a source ref cannot be resolved, keep the memory candidate out of
  promotion and repair the source anchor first.
- Review gate: memory remains a recall aid weaker than owner evidence.
