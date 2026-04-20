# Release Wave Closeout Followthrough

Playbook: `reviewed-automation-followthrough`

Use this example only when a reviewed release wave has already produced explicit closeout context, persistent owner handoff, and strict publish plus postpublish audit evidence, and the next honest move is to stage an automation candidate without granting scheduler authority.

Suggested seed:

- start from `closeout_followthrough_decision` and the owner handoff bundle
- run `aoa-automation-opportunity-scan`
- preserve public-share guards, dry-run publish, strict preflight and postpublish audit, rollback and tag-restore posture, and explicit human review
- reject `promote_to_skill` if the route pretends a fourteen-repo release publication wave is one leaf workflow
- stop or defer if the due repo set, tag history, branch protection, or GitHub publication state cannot be verified cleanly

Primary evidence anchors:

- `repo:aoa-sdk/.aoa/session-growth/current/a6d4afed-40bc-4f50-b77d-43213f9e74f5/workspace/closeout-context.json`
- `repo:aoa-sdk/.aoa/session-growth/current/a6d4afed-40bc-4f50-b77d-43213f9e74f5/workspace/closeout-execution-report.json`
- `repo:aoa-sdk/.aoa/closeout/handoffs/session-2026-04-20T04-56-34-124016Z-workspace-checkpoint-growth-a6d4afed-40b.owner-handoff.json`
- `repo:aoa-playbooks/docs/real-runs/2026-04-20.closeout-owner-follow-through-continuity.release-wave-closeout.md`

This file is illustrative only.
It is not a live schedule, not a composition-owned automation seed, and not permission to publish.
