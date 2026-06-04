# Titan Runtime Harness Route Note

This is a supporting Titan route note, not an authored playbook bundle. The
validated scenario surface for Titan-backed closeout lives at
`playbooks/titan/closeout/titan-closeout-audit/PLAYBOOK.md`.

## Scenario A: read-only orientation

1. Summon Atlas, Sentinel, and Mneme.
2. Create receipt.
3. Map route, risk, and provenance.
4. Close receipt.

## Scenario B: implementation

1. Run Scenario A.
2. Record mutation intent.
3. Gate Forge with `mutation`.
4. Apply bounded implementation.
5. Validate.
6. Close receipt with mutation summary.

## Scenario C: verdict or comparison

1. Run Scenario A.
2. Record judgment intent.
3. Gate Delta with `judgment`.
4. Run comparison or verdict.
5. Close receipt with limitations.

## Scenario D: implementation plus verdict

1. Run Scenario A.
2. Record both mutation intent and judgment intent.
3. Gate Forge for mutation.
4. Implement.
5. Gate Delta for judgment.
6. Evaluate.
7. Close receipt with orientation, mutation, and judgment gate trails.

## Prohibited route

Do not activate Forge and Delta just because a task is exciting. Gates are boring on purpose. That boredom is the lock.
