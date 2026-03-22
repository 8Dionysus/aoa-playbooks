---
id: AOA-P-0009
name: restartable-inquiry-loop
status: experimental
summary: Runs a checkpoint-based long-horizon inquiry loop that can pause, relaunch, and preserve axis through bounded artifacts.
scenario: restartable_inquiry
trigger: long_horizon_philosophy_or_architecture_question
prerequisites:
  - checkpoint_contract_defined
  - evidence_pack_defined
  - contradiction_posture_defined
  - human_resume_boundary_defined
participating_agents:
  - architect
  - reviewer
  - evaluator
  - memory-keeper
required_skill_families:
  - research
  - synthesis
  - memory-curation
  - evaluation
evaluation_posture: strict
memory_posture: deep_recall
fallback_mode: safe_stop
expected_artifacts:
  - inquiry_checkpoint
  - decision_ledger
  - contradiction_map
  - memory_delta
  - canon_delta
  - next_pass_brief
eval_anchors:
  - aoa-long-horizon-depth
---

# restartable-inquiry-loop

## Intent

Use this playbook when a philosophical, architectural, or research route must survive pauses without pretending that one infinite context window is the source of continuity.

This playbook keeps the route restartable by making artifacts primary:
- checkpoint pack
- decision ledger
- contradiction map
- memory delta
- canon delta
- next-pass brief

## Trigger boundary

Use this playbook when:
- the question is large enough to need more than one bounded pass
- the route may pause for hours, days, or longer
- contradiction preservation matters more than smooth rhetorical flow
- the next pass should relaunch from evidence and checkpoints rather than raw chat history

Do not use this playbook when:
- one bounded research pass can finish the task honestly
- the route has no artifact surface worth preserving
- the question is so vague that a checkpoint would only preserve fog
- the team is trying to treat checkpoint packs as ToS canon by default

## Prerequisites

- an `inquiry_checkpoint` contract exists and is readable
- the current route can name its evidence pack
- contradiction posture is explicit
- a human can pause, delay, relaunch, or block canonization

## Participating agents

- `architect` keeps the inquiry axis, scope, and route goal explicit
- `reviewer` checks whether contradictions, limits, and restart posture stay visible
- `evaluator` checks whether the checkpoint really supports bounded relaunch rather than false continuity
- `memory-keeper` preserves memory delta and checkpoint integrity without confusing it with ToS canon

## Required skills

- `aoa-source-of-truth-check`
- `aoa-change-protocol`
- `aoa-dry-run-first`
- `aoa-bounded-context-map`

## Decision points

1. Decide whether the current pass has enough evidence to produce a checkpoint.
2. Decide whether the current thesis is stable enough to preserve as axis rather than decoration.
3. Decide whether contradictions stay open, resolved, or deferred.
4. Decide whether the next move is relaunch, deepen, or safe stop.
5. Decide whether any part of the route should survive as memo writeback, canon delta, or only operational state.

## Handoffs

- `architect -> reviewer` after the current axis and current thesis are explicit
- `reviewer -> evaluator` after contradictions, limits, and evidence refs are explicit
- `evaluator -> memory-keeper` after the checkpoint is judged portable enough for relaunch
- `memory-keeper -> architect` when the next pass brief and memory delta are ready for the next loop

## Fallback and rollback posture

Fallback mode is `safe_stop`.

Pause or stop when:
- the route cannot state its current axis clearly
- contradiction handling has been smoothed away
- the checkpoint lacks evidence refs or open questions
- the route is trying to relaunch from summary theater instead of portable artifacts

Safe stop is acceptable.
False continuity is not.

## Expected evidence posture

The route should finish each pass with visible evidence for:
- the current axis
- the evidence pack
- unresolved contradictions
- what changed in memory
- what changed in canon-facing interpretation
- what the next pass must keep and must test

## Expected artifacts

- `inquiry_checkpoint`
- `decision_ledger`
- `contradiction_map`
- `memory_delta`
- `canon_delta`
- `next_pass_brief`

## Eval anchors

- `aoa-long-horizon-depth`

## Memory writeback

- the checkpoint pack may survive as bounded memo-facing state for relaunch
- `memory_delta` should remain distinct from `canon_delta`
- unresolved contradictions should survive as contradictions, not be rewritten as settled claims
- the route should not promote every checkpoint into durable memory automatically

## Canonical route

1. Gather the current evidence, decisions, and contradictions for the active pass.
2. Frame the current axis and current thesis without hiding uncertainty.
3. Test the current line of inquiry and record meaningful state changes.
4. Verify what the pass actually supports, what remains open, and what drift appeared.
5. Compress the pass into an `inquiry_checkpoint` plus contradiction, memory, and canon artifacts.
6. Decide whether the next move is relaunch, deepen, or safe stop.
7. Relaunch the next pass from the checkpoint pack rather than from raw chat continuity.
