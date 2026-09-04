# Validation routes

Memo operations are deliberate, reviewed, and on demand. Keep the
`AOA_ABYSS_STACK_ROOT` and `AOA_MEMO_ROOT` overrides explicit.

## Candidate creation

```bash
AOA_ABYSS_STACK_ROOT="${AOA_ABYSS_STACK_ROOT:-$HOME/src/abyss-stack}"
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli create-candidate \
  --repo aoa-playbooks \
  --evidence-ref README.md \
  --claim "aoa-playbooks memory should move through reviewed local candidates before aoa-memo landing."
```

## Candidate validation

```bash
AOA_ABYSS_STACK_ROOT="${AOA_ABYSS_STACK_ROOT:-$HOME/src/abyss-stack}"
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli validate-candidate path/to/candidate.json
```

## Pending exports and landing plan

```bash
AOA_ABYSS_STACK_ROOT="${AOA_ABYSS_STACK_ROOT:-$HOME/src/abyss-stack}"
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli pending-exports --repo aoa-playbooks
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli landing-plan --repo aoa-playbooks --export-ref exports/path.reviewed-intake.json --run-dry-run
```

## Local memo port

```bash
AOA_MEMO_ROOT="${AOA_MEMO_ROOT:-/srv/AbyssOS/aoa-memo}"
python "$AOA_MEMO_ROOT/scripts/memory/validate_local_memo_port.py" --path memo
python "$AOA_MEMO_ROOT/scripts/memory/build_local_memo_port_index.py" --path memo --check
```
