# Validation routes

```bash
python -c 'import json, pathlib; p=json.loads(pathlib.Path("generated/playbook_review_status.min.json").read_text()); rows=p["playbooks"]; covered=sum(row["reviewed_run_count"] > 0 for row in rows); print({"population": len(rows), "covered": covered, "ratio": covered / len(rows)})'
```

```bash
python scripts/validate_local_stats_port.py
```
