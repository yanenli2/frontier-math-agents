#!/usr/bin/env python3
"""Record an exact command, exit status, streams, environment additions and hashes."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('--cwd', default=str(Path(__file__).resolve().parents[6]))
parser.add_argument('--timeout', type=int, default=600)
parser.add_argument('--env', action='append', default=[])
parser.add_argument('label')
parser.add_argument('command', nargs=argparse.REMAINDER)
args = parser.parse_args()
root = Path(__file__).resolve().parent
if not args.command:
    parser.error('command is required')
for suffix in ('.stdout', '.stderr', '.json'):
    if (root / (args.label + suffix)).exists():
        parser.error('label already exists: ' + args.label)
env_additions = dict(x.split('=', 1) for x in args.env)
env = dict(os.environ, **env_additions)
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
clock = time.monotonic()
try:
    result = subprocess.run(args.command, cwd=args.cwd, env=env, capture_output=True,
                            timeout=args.timeout)
    out, err, status = result.stdout, result.stderr, result.returncode
except subprocess.TimeoutExpired as exc:
    out, err, status = exc.stdout or b'', exc.stderr or b'', 124
except OSError as exc:
    out, err, status = b'', str(exc).encode(), 127
out_path = root / (args.label + '.stdout')
err_path = root / (args.label + '.stderr')
out_path.write_bytes(out)
err_path.write_bytes(err)
record = {
    'argv': args.command, 'shell_display': shlex.join(args.command),
    'cwd': args.cwd, 'environment_additions': env_additions,
    'started_utc': started, 'elapsed_seconds': time.monotonic() - clock,
    'timeout_seconds': args.timeout, 'exit_status': status,
    'stdout_path': str(out_path), 'stderr_path': str(err_path),
    'stdout_sha256': hashlib.sha256(out).hexdigest(),
    'stderr_sha256': hashlib.sha256(err).hexdigest()
}
(root / (args.label + '.json')).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
if len(out) < 4000:
    print(out.decode(errors='replace'))
if len(err) < 4000:
    print(err.decode(errors='replace'), file=sys.stderr)
sys.exit(status)
