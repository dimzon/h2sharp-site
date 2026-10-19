#!/usr/bin/env python3
"""Verify the site mirror against the project's committed manifest.

The main repo (dimzon/h2sharp) ships the same frozen H2 snapshot in docs/ with a
SHA-256 manifest.csv. This checks our raw/upstream copy byte for byte, so the
mirror and the snapshot the conformance tests cite can never drift silently.
Stdlib only.
"""
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"

# from docs/manifest.csv @ dimzon/h2sharp main (2026-10-19)
MANIFEST = {
    "commands.html": "e6a8bc3c3e355135aac875052901ce133e0b37d258e30563c837c437827b41a8",
    "grammar.html": "1fb94b45eb865f77aa66e2b4e737660c5fac0490035abed7402e09f80d0c52b9",
    "functions.html": "11494f4a4f0b09a8b6d8be654abca541cd29dbfd6917d9263946141b8d941c92",
    "functions-aggregate.html": "824dd991e3a9e1a4329bfe65188a0bfde5391cf53519a25ae8636dfbdb8c762d",
    "functions-window.html": "fdaf1cd1475b96451d7d100a378423dafcc7998b4067642cc0536d119ad5541e",
    "datatypes.html": "4568be7631f3d5d4bb10429d881075d5c843d13344b84be2e6f0d9fbab9bd938",
    "systemtables.html": "62aba1b47110340c400f51afaaa184545f4ae0dd0157a6e27cb9953425317ddd",
    "cheatSheet.html": "ddc22ed8bfa0a460d3afec18173242d6d21284aa4a795ee81417b13b696927d1",
}


def main() -> int:
    prov_path = RAW / "provenance.json"
    if not prov_path.exists():
        print("no raw/provenance.json")
        return 1
    prov = json.loads(prov_path.read_text(encoding="utf-8"))
    snap = RAW / "upstream" / prov["stamp"]
    print(f"snapshot: {snap.name} (downloaded {prov['fetchedAt'][:10]})\n")
    ok = bad = 0
    for name, want in MANIFEST.items():
        f = snap / name
        if not f.exists():
            print(f"  MISSING  {name}")
            bad += 1
            continue
        got = hashlib.sha256(f.read_bytes()).hexdigest()
        if got == want:
            print(f"  ok       {name}")
            ok += 1
        else:
            print(f"  MISMATCH {name}\n            ours {got}\n            main {want}")
            bad += 1
    print(f"\n{ok} identical, {bad} problem(s).")
    print("Main repo manifest: docs/manifest.csv @ dimzon/h2sharp")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())