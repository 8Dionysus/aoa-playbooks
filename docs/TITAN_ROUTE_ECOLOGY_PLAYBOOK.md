# Titan Route Ecology Playbook

A successful path is not universal law.

Promotion ladder:

```text
raw trace -> observation -> candidate -> reviewed candidate -> owner accepted artifact
```

## Promotion Criteria

Each transition is explicit. Absence of rejection is not promotion.

| Transition | Required evidence | Fallback |
| --- | --- | --- |
| raw trace -> observation | A visible source trace, timestamp or session ref, and owner route hint are recorded. | Keep as raw trace when source or owner route is unclear. |
| observation -> candidate | The observation names a bounded claim, candidate owner repo, and expected use. | Split or defer when the claim has multiple owners or no review surface. |
| candidate -> reviewed candidate | A reviewer or validation step records criteria, evidence refs, and residual risk. | Return to candidate with the missing criterion; do not compose downstream. |
| reviewed candidate -> owner accepted artifact | The owner repo accepts the artifact by commit, PR, status file, or explicit reviewed note. | Keep as reviewed candidate and link the owner blocker. |

Promotion must preserve the weaker-source posture of prior states. A reviewed
candidate can inform playbook composition, but only an owner accepted artifact
can be treated as landed owner truth.
