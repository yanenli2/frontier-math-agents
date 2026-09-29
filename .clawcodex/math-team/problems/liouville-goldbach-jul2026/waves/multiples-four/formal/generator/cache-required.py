#!/usr/bin/env python3
"""Fetch only the pinned SumTwoSquares source-hash cache closure, with evidence."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
project = root.parent.parent.parent.parent / 'lean'
label = 'four-cache-sum-two-squares-v1'
for suffix in ('.json', '.stdout', '.stderr'):
    if (root / (label + suffix)).exists():
        raise RuntimeError('Refusing to overwrite cache evidence')
assert (root / 'cache').is_dir()
checkout = project / '.lake/packages/mathlib'
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=checkout, text=True).strip()
assert head == '905b95818eb32af7874a58b427f50c1711a5e96c'
manifest = project / 'lake-manifest.json'
manifest_hash = hashlib.sha256(manifest.read_bytes()).hexdigest()
assert manifest_hash == 'de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03'
source = checkout / 'Mathlib/NumberTheory/SumTwoSquares.lean'
source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
assert source_hash == 'ecc1647de087331c1876ca386b495ff2a83943a428bf140bf6ba8047f9fd80f9'
argv = ['lake', 'exe', 'cache', 'get', 'Mathlib.NumberTheory.SumTwoSquares']
env_additions = {'MATHLIB_CACHE_DIR': str(root / 'cache')}
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
clock = time.monotonic()
try:
    result = subprocess.run(argv, cwd=project, env=dict(os.environ, **env_additions), capture_output=True, timeout=600)
    out, err, status = result.stdout, result.stderr, result.returncode
except subprocess.TimeoutExpired as exc:
    out, err, status = exc.stdout or b'', exc.stderr or b'', 124
(root / (label + '.stdout')).write_bytes(out)
(root / (label + '.stderr')).write_bytes(err)
record = {'argv': argv, 'shell_display': shlex.join(argv), 'cwd': str(project),
          'environment_additions': env_additions, 'started_utc': started,
          'elapsed_seconds': time.monotonic() - clock, 'timeout_seconds': 600,
          'exit_status': status, 'mathlib_head': head,
          'manifest_sha256_before': manifest_hash,
          'manifest_sha256_after': hashlib.sha256(manifest.read_bytes()).hexdigest(),
          'source': str(source), 'source_sha256': source_hash,
          'stdout_sha256': hashlib.sha256(out).hexdigest(),
          'stderr_sha256': hashlib.sha256(err).hexdigest()}
(root / (label + '.json')).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
print(out.decode(errors='replace'))
if status or len(err) < 4000:
    print(err.decode(errors='replace'), file=sys.stderr)
sys.exit(status)
