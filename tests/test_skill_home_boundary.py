from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_repo_skill_home_stays_absent_until_owner_mcp_and_admission_exist() -> None:
    unexpected = [
        path.relative_to(REPO_ROOT).as_posix()
        for path in (REPO_ROOT / "skills", REPO_ROOT / ".agents" / "skills")
        if path.exists()
    ]

    assert unexpected == [], (
        "aoa-playbooks has no local skill home before aoa-playbooks-mcp and a "
        f"fresh owner admission decision exist: {unexpected}"
    )
