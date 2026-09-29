#!/usr/bin/env python3
"""Compile/build an owned descent module with protected-source and stream evidence."""
import datetime
import hashlib
import json
from pathlib import Path
import shlex
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
wave = root.parent.parent
problem = wave.parent.parent
project = problem / 'lean'
label, module = sys.argv[1:3]
assert module in {'Cyclic', 'Ternary'}
source = project / ('Statement/FourWork/Descent/' + module + '.lean')
mode = sys.argv[3] if len(sys.argv) > 3 else 'direct'
argv = ['lake', 'build', 'Statement.FourWork.Descent.' + module] if mode == 'build' else ['lake', 'env', 'lean', str(source)]
for suffix in ('.lean', '.json', '.stdout', '.stderr'):
    if (root / (label + suffix)).exists():
        raise RuntimeError('Refusing to overwrite evidence label')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

protected = {
    wave / 'formal/descent-blueprint/Readback.lean.txt': '372c3a6b8acfc112331707944bfef543c12ea03049ce5bb95eae7e34f9591763',
    project / 'Statement/Definitions.lean': '79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d',
    project / 'Statement/Partial.lean': '9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0',
    project / 'Statement/FourPartial.lean': '4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325',
    project / 'lake-manifest.json': 'de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03',
    project / 'lakefile.toml': '0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4',
    project / 'lean-toolchain': '2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273',
}
protected_hashes = {str(p): sha(p) for p in protected}
assert all(protected_hashes[str(p)] == h for p, h in protected.items())
snapshot = root / (label + '.lean')
snapshot.write_bytes(source.read_bytes())
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
clock = time.monotonic()
try:
    result = subprocess.run(argv, cwd=project, capture_output=True, timeout=180)
    out, err, status = result.stdout, result.stderr, result.returncode
except subprocess.TimeoutExpired as exc:
    out, err, status = exc.stdout or b'', exc.stderr or b'', 124
(root / (label + '.stdout')).write_bytes(out)
(root / (label + '.stderr')).write_bytes(err)
record = {'argv': argv, 'shell_display': shlex.join(argv), 'cwd': str(project),
          'started_utc': started, 'elapsed_seconds': time.monotonic() - clock,
          'timeout_seconds': 180, 'exit_status': status, 'source': str(source),
          'source_sha256_before': sha(snapshot), 'source_sha256_after': sha(source),
          'snapshot': str(snapshot), 'stdout_sha256': hashlib.sha256(out).hexdigest(),
          'stderr_sha256': hashlib.sha256(err).hexdigest(), 'protected_hashes': protected_hashes,
          'protected_unchanged_after': all(sha(p) == h for p, h in protected.items())}
(root / (label + '.json')).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
if mode == 'build' and len(out) > 6000:
    print('Full Lake stdout preserved at ' + str(root / (label + '.stdout')))
else:
    print(out.decode(errors='replace'))
print(err.decode(errors='replace'), file=sys.stderr)
sys.exit(status)
