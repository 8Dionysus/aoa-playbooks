# Playbook Operational Family

This document is the chooser surface for the operational playbook family.

Use it when multiple operational playbooks feel "almost right" and the main risk is semantic overlap rather than missing coverage.

## Core rule

Choose the playbook by the route anchor and closure class, not by which one happens to mention similar tools or neighboring repos.
If two playbooks seem equally plausible, prefer the one whose dominant move and fallback shape match the real scenario.

## Operational chooser

| playbook | primary trigger | dominant move | ownership span | fallback shape | closure class | do-not-use neighbors | typical follow-on |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `AOA-P-0010 cross-repo-boundary-rollout` | bounded multi-repo source-of-truth change | generic single-wave rollout sequencing | more than one source-owned repo or layer | `review_required` with boundary-anchor return | `validation_pack` plus handoff or stop | `AOA-P-0017`, `AOA-P-0018`, `AOA-P-0019`, `AOA-P-0020` | later bounded rollout, handoff, or defer wave |
| `AOA-P-0012 infra-change-guarded` | planned infra or configuration mutation needing preview | preview-first infra change with rollback posture | one operational surface or bounded service setup seam | `review_required` with preview or rollback return | bounded verification after the infra step | `AOA-P-0014`, `AOA-P-0020` | `AOA-P-0014` for local blockers or `AOA-P-0020` if a live incident appears |
| `AOA-P-0014 local-stack-diagnosis` | local startup path unstable or unclear | diagnose and isolate blockers in one bounded local route | local-only startup, dependency, or bring-up surface | `safe_stop` with blocker-oriented return | verified stack, blocker list, or safe stop | `AOA-P-0012`, `AOA-P-0020` | `AOA-P-0012` for a governed infra change or a later bounded fix |
| `AOA-P-0017 split-wave-cross-repo-rollout` | ordered cross-repo rollout where upstream bridge surfaces must land first | multi-wave bridge publication and downstream revalidation | more than one source-owned repo with ordered merge or rerun boundaries | `review_required` with wave-anchor return | merge, defer, rollback, or stop after downstream revalidation | `AOA-P-0010`, `AOA-P-0019`, `AOA-P-0020` | later wave, defer handoff, or review restart |
| `AOA-P-0018 validation-driven-remediation` | failed validator or proof surface crossing owned boundaries | bounded corrective change driven by a failing validation anchor | cross-boundary remediation across owning surfaces | `review_required` with failure-anchor return | remediation decision plus revalidation closure or handoff | `AOA-P-0010`, `AOA-P-0019`, `AOA-P-0020` | further bounded remediation, review stop, or handoff to a later governed route |
| `AOA-P-0019 release-migration-cutover` | planned release or migration window requiring authority switch | freeze, go/no-go gate, authority switch, post-cutover verification | neighboring repos or layers with named authority switch | `review_required` with cutover or rollback gate | confirm switch, reverse switch, handoff, or stop | `AOA-P-0004`, `AOA-P-0010`, `AOA-P-0017`, `AOA-P-0020` | follow-on migration work, consumer handoff, or rollback review |
| `AOA-P-0020 incident-recovery-routing` | unplanned incident requiring cross-boundary stabilization | stabilize, roll back, or degrade with recovery verification | cross-boundary incident surface, blast radius, and downstream consumers | `review_required` with recovery-anchor return | `restored`, `degraded-with-handoff`, `rollback-complete`, or `review-stop` | `AOA-P-0012`, `AOA-P-0014`, `AOA-P-0018`, `AOA-P-0019` | `AOA-P-0018`, `AOA-P-0010`, or later governed follow-on work |

## Family differentiation

- `AOA-P-0010` = generic cross-repo rollout baseline
- `AOA-P-0012` = preview-first infra change before live incident
- `AOA-P-0014` = local-only diagnosis and blocker isolation
- `AOA-P-0017` = ordered multi-wave rollout
- `AOA-P-0018` = post-failure remediation
- `AOA-P-0019` = planned cutover window
- `AOA-P-0020` = live cross-boundary incident stabilization and recovery handoff

## Boundary discipline

Do not add another operational playbook until the chooser table can no longer place the scenario honestly.
If the route is already covered here, tighten the bundle boundary or collect real-run evidence instead of widening the catalog.
