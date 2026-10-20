#!/usr/bin/env python3
"""Check the H2Sharp repositories for new commits.

The site follows three repositories: the engine and the two provider projects.
This prints what landed since the last run, so the pages can be checked against
the code instead of against commit titles.

    python tools/check-updates.py            # report and remember
    python tools/check-updates.py --all      # report everything, forget nothing
    python tools/check-updates.py --reset    # forget the remembered state

State lives in .state/updates.json (git-ignored). Uses the `gh` CLI, so it
needs the same authentication the rest of the tooling does.
"""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / ".state" / "updates.json"

REPOS = [
    ("engine", "dimzon/h2sharp"),
    ("efcore", "dimzon/h2sharp-efcore"),
    ("linq2db", "dimzon/h2sharp-linq2db"),
]


def gh(*args: str) -> str:
    out = subprocess.run(["gh", *args], capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip() or "gh failed")
    return out.stdout


def commits(repo: str, limit: int = 30) -> list[dict]:
    raw = gh("api", f"repos/{repo}/commits?per_page={limit}")
    data = json.loads(raw)
    return [{"sha": c["sha"][:7], "date": c["commit"]["committer"]["date"], "msg": c["commit"]["message"].split("\n")[0]}
            for c in data]


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {}


def save_state(state: dict) -> None:
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> int:
    args = sys.argv[1:]
    if "--reset" in args:
        if STATE.exists():
            STATE.unlink()
        print("state cleared")
        return 0

    state = load_state()
    seen = state.get("seen", {})
    changed = False

    for label, repo in REPOS:
        try:
            cs = commits(repo)
        except Exception as e:  # noqa: BLE001 - report and continue
            print(f"{label}: could not read {repo}: {e}")
            continue
        head = cs[0]["sha"] if cs else None
        last = seen.get(repo)
        print(f"\n=== {label}  {repo}")
        if not cs:
            print("  (no commits)")
        elif last is None:
            print(f"  first look - head {head}")
            for c in cs[:5]:
                print(f"    {c['date'][:16]} {c['sha']} {c['msg']}")
        elif last == head:
            print(f"  no change since {last}")
        else:
            print(f"  new since {last} (head {head}):")
            idx = next((i for i, c in enumerate(cs) if c["sha"] == last), None)
            fresh = cs if idx is None else cs[:idx]
            for c in fresh:
                print(f"    {c['date'][:16]} {c['sha']} {c['msg']}")
        seen[repo] = head
        changed = True

    if changed and "--all" not in args:
        state["seen"] = seen
        state["checkedAt"] = datetime.now(timezone.utc).isoformat()
        save_state(state)
        print(f"\nstate written to {STATE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
