#!/usr/bin/env python3
"""Compile owned candidate with exact source/command/stream evidence."""
import datetime
import hashlib
import json
from pathlib import Path
import shlex
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
problem = root.parent.parent
project = problem / 'lean'
label = sys.argv[1]
source = root / (sys.argv[2] if len(sys.argv) > 2 else 'Candidate.lean')
for suffix in ('.lean', '.stdout', '.stderr', '.json'):
    if (root / (label + suffix)).exists():
        raise RuntimeError('Refusing to overwrite evidence label: ' + label)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

protected = {
    problem / 'formal/approved-v1/Definitions.lean': '79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d',
    project / 'Statement/Definitions.lean': '79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d',
    problem / 'formal/blueprinter/interfaces-v1.lean': '89080f705ec6f0ba690edbc4e7d3d97cea18a6f3d3c3cdcb31e30abefbb434bc',
    project / 'lake-manifest.json': 'de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03',
    project / 'lakefile.toml': '0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4',
    project / 'lean-toolchain': '2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273',
}
protected_hashes = {str(p): sha(p) for p in protected}
assert all(protected_hashes[str(p)] == expected for p, expected in protected.items())
snapshot = root / (label + '.lean')
snapshot.write_bytes(source.read_bytes())
argv = ['lake', 'env', 'lean', str(source)]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
clock = time.monotonic()
try:
    result = subprocess.run(argv, cwd=project, capture_output=True, timeout=180)
    out, err, status = result.stdout, result.stderr, result.returncode
except subprocess.TimeoutExpired as exc:
    out, err, status = exc.stdout or b'', exc.stderr or b'', 124
except OSError as exc:
    out, err, status = b'', str(exc).encode(), 127
(root / (label + '.stdout')).write_bytes(out)
(root / (label + '.stderr')).write_bytes(err)
record = {
    'argv': argv, 'shell_display': shlex.join(argv), 'cwd': str(project),
    'started_utc': started, 'elapsed_seconds': time.monotonic() - clock,
    'timeout_seconds': 180, 'exit_status': status,
    'source': str(source), 'source_sha256_before': sha(snapshot),
    'source_sha256_after': sha(source), 'snapshot': str(snapshot),
    'stdout_sha256': hashlib.sha256(out).hexdigest(),
    'stderr_sha256': hashlib.sha256(err).hexdigest(),
    'protected_hashes': protected_hashes,
    'protected_unchanged_after': all(sha(p) == expected for p, expected in protected.items()),
}
(root / (label + '.json')).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
print(out.decode(errors='replace'))
print(err.decode(errors='replace'), file=sys.stderr)
sys.exit(status)
