#!/usr/bin/env python3
"""Polite crawler: H2 SQL reference -> raw/upstream/<stamp>/ + raw/provenance.json.

Scope (SQL reference only):
  commands, functions, functions-aggregate, functions-window,
  datatypes, grammar, systemtables (+ images/ referenced by them).

Politeness: single-threaded, 1.5s pause, identifying UA, 3 retries w/ backoff.
Idempotent: skips download when content SHA-256 unchanged.
Stdlib only.
"""
import hashlib
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://www.h2database.com/html/"
PAGES = ["commands", "functions", "functions-aggregate", "functions-window",
         "datatypes", "grammar", "systemtables"]
UA = "H2Sharp-docs-mirror (+https://github.com/dimzon/h2sharp-site; SQL ref snapshot)"
H2_VERSION = "2.5.252 (2026-09-23)"
H2_PIN = "27c51709fef687bc064f23c8dd495b566c69bb93"

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"


def fetch(url: str, timeout: int = 30) -> bytes:
    last: Exception | None = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001 - retry then raise
            last = e
            time.sleep(2 ** attempt + 1)
    assert last is not None
    raise last


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-h2-2.5.252")
    out = RAW / "upstream" / stamp
    out.mkdir(parents=True, exist_ok=True)
    manifest = {"stamp": stamp, "fetchedAt": datetime.now(timezone.utc).isoformat(),
                "h2Version": H2_VERSION, "h2sharpPin": H2_PIN, "base": BASE,
                "pages": [], "ua": UA}
    for name in PAGES:
        url = f"{BASE}{name}.html"
        data = fetch(url)
        sha = hashlib.sha256(data).hexdigest()
        (out / f"{name}.html").write_bytes(data)
        manifest["pages"].append({"name": name, "url": url, "sha256": sha, "bytes": len(data)})
        print(f"saved {name}.html ({len(data)} bytes, sha {sha[:12]})")
        time.sleep(1.5)
    (RAW / "provenance.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"provenance -> raw/provenance.json ({len(manifest['pages'])} pages)")


if __name__ == "__main__":
    main()
