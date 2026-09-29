#!/usr/bin/env python3
"""Record exact commands, statuses, diagnostics, and owned Lean source snapshots."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import shlex
import subprocess
import sys

OUT = Path(__file__).resolve().parent
P = OUT.parents[3]
CWD = P / "lean"
label, *argv = sys.argv[1:]
if not label or not argv or any(x in label for x in "/\\"):
    raise SystemExit("usage: run_check.py LABEL COMMAND ARG...")
metadata = {"cwd": str(CWD), "argv": argv, "command": shlex.join(argv),
            "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "sources": {}}
for path in sorted((CWD / "Statement/FourWork/Character").glob("*.lean")):
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    snapshot = OUT / f"{label}.{path.stem}.{digest[:12]}.lean.txt"
    snapshot.write_bytes(data)
    metadata["sources"][str(path)] = {"sha256": digest, "snapshot": str(snapshot)}
for rel in ["lean-toolchain", "lakefile.toml", "lake-manifest.json", "Statement/Definitions.lean", "Statement/Partial.lean", "Statement/FourPartial.lean"]:
    path = CWD / rel
    metadata.setdefault("fixed_files", {})[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
env = os.environ.copy()
if argv[:3] == ["lake", "exe", "cache"]:
    env["MATHLIB_CACHE_DIR"] = str(OUT / "cache")
    metadata["environment_override"] = {"MATHLIB_CACHE_DIR": env["MATHLIB_CACHE_DIR"]}
logpath = OUT / f"{label}.log"
with logpath.open("w") as log:
    log.write(f"cwd: {CWD}\nargv: {json.dumps(argv)}\ncommand: {shlex.join(argv)}\n\n")
    log.flush()
    proc = subprocess.run(argv, cwd=CWD, env=env, stdout=log, stderr=subprocess.STDOUT)
    log.write(f"\nexit_status: {proc.returncode}\n")
metadata["exit_status"] = proc.returncode
metadata["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
metadata["diagnostics"] = str(logpath)
(OUT / f"{label}.json").write_text(json.dumps(metadata, indent=2) + "\n")
print(logpath.read_text())
raise SystemExit(proc.returncode)
