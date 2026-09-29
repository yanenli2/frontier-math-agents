#!/usr/bin/env python3
"""Compile the exact two endpoints with frozen helper and baseline dependencies."""
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
source = project / 'Statement/FourWork/Assembly.lean'
label = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else 'direct'
if mode == 'build':
    argv = ['lake', 'build', 'Statement.FourWork.Assembly']
elif mode == 'trust-zero':
    argv = ['lake', 'env', 'lean', '--trust=0', str(source)]
else:
    argv = ['lake', 'env', 'lean', str(source)]
for suffix in ('.lean', '.json', '.stdout', '.stderr'):
    if (root / (label + suffix)).exists():
        raise RuntimeError('Refusing to overwrite build evidence')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

protected = {
    wave / 'formal/descent-blueprint/Readback.lean.txt': '372c3a6b8acfc112331707944bfef543c12ea03049ce5bb95eae7e34f9591763',
    project / 'Statement/Definitions.lean': '79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d',
    project / 'Statement/Partial.lean': '9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0',
    project / 'Statement/FourPartial.lean': '4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325',
    project / 'Statement/FourWork/Descent/Cyclic.lean': '09fbee47a60bf7db94d65e871fc49f5d07d60838c8b01cfbfdecb53033471290',
    project / 'Statement/FourWork/Descent/Ternary.lean': 'd6f231fc9aa372f562b19170268b31ae16bdca178185256131232011fd255753',
    project / 'Statement/FourWork/Character/ResiduePrime.lean': '518f28a33ab98d1a44ea7b544ca7f695e28c48893982caaf72eb4879956763dd',
    project / 'Statement/FourWork/Character/ResidueValue.lean': '3df5a3f0a6de6a60c2b8b8ba89dd6e44fa4d47cb28e98c33f1e31d1dfb7d84dd',
    project / 'Statement/FourWork/Character/Rigidity.lean': '843e4ee562071ef4729a61c715b77510b378add7f19b8c02d1e3d36fa9165f88',
    project / 'Statement.lean': 'dc72b845dbb045593ef3a6212b03a54cc0797a29baac132e870aff324cdc5853',
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
    result = subprocess.run(argv, cwd=project, capture_output=True, timeout=240)
    out, err, status = result.stdout, result.stderr, result.returncode
except subprocess.TimeoutExpired as exc:
    out, err, status = exc.stdout or b'', exc.stderr or b'', 124
(root / (label + '.stdout')).write_bytes(out)
(root / (label + '.stderr')).write_bytes(err)
record = {'argv': argv, 'shell_display': shlex.join(argv), 'cwd': str(project),
          'started_utc': started, 'elapsed_seconds': time.monotonic() - clock,
          'timeout_seconds': 240, 'exit_status': status, 'source': str(source),
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
