#!/usr/bin/env python3
"""Record content identities and dated ancestry for the exact source slices audited."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
project = root.parent.parent / 'lean'
runner = root / 'run.py'
mathlib_sha = '905b95818eb32af7874a58b427f50c1711a5e96c'
lean_sha = 'f3b06c705e6c85f5314019d5d3baab0fec5b580c'
entries = [
    ('mathlib-factors', 'leanprover-community/mathlib4', mathlib_sha, 'Mathlib/Data/Nat/Factors.lean'),
    ('mathlib-prime-defs', 'leanprover-community/mathlib4', mathlib_sha, 'Mathlib/Data/Nat/Prime/Defs.lean'),
    ('mathlib-even', 'leanprover-community/mathlib4', mathlib_sha, 'Mathlib/Algebra/Group/Even.lean'),
    ('mathlib-irreducible', 'leanprover-community/mathlib4', mathlib_sha, 'Mathlib/Algebra/Group/Irreducible/Defs.lean'),
    ('mathlib-units', 'leanprover-community/mathlib4', mathlib_sha, 'Mathlib/Algebra/Group/Units/Defs.lean'),
    ('lean-prelude', 'leanprover/lean4', lean_sha, 'src/Init/Prelude.lean'),
    ('lean-list-basic', 'leanprover/lean4', lean_sha, 'src/Init/Data/List/Basic.lean'),
    ('lean-int-basic', 'leanprover/lean4', lean_sha, 'src/Init/Data/Int/Basic.lean')
]

def capture(label, command):
    completed = subprocess.run([sys.executable, str(runner), label, *command], capture_output=True)
    if completed.returncode:
        raise RuntimeError('Command failed: ' + label)
    return (root / (label + '.stdout')).read_bytes()

results = []
for label, repo, sha, path in entries:
    endpoint = 'repos/' + repo + '/commits?sha=' + sha + '&path=' + path + '&per_page=1'
    commits = json.loads(capture('source-' + label + '-history', ['gh', 'api', endpoint]))
    commit = commits[0]
    dates = {kind: commit['commit'][kind]['date'] for kind in ['author', 'committer']}
    if any(date > '2026-07-31T23:59:59Z' for date in dates.values()):
        raise RuntimeError('Unexpected ineligible source ancestry: ' + label)
    if repo.endswith('mathlib4'):
        local = project / '.lake/packages/mathlib' / path
        git_blob = capture('source-' + label + '-blob', ['git', '-C', str(project / '.lake/packages/mathlib'), 'rev-parse', sha + ':' + path]).decode().strip()
        local_blob = hashlib.sha1(b'blob ' + str(len(local.read_bytes())).encode() + b'\0' + local.read_bytes()).hexdigest()
        matches_pin = local_blob == git_blob
    else:
        local = Path.home() / '.elan/toolchains/leanprover--lean4---v4.32.2/src/lean' / path.removeprefix('src/')
        raw = capture('source-' + label + '-raw', ['gh', 'api', '-H', 'Accept: application/vnd.github.raw+json', 'repos/' + repo + '/contents/' + path + '?ref=' + sha])
        matches_pin = raw == local.read_bytes()
        git_blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if not matches_pin:
        raise RuntimeError('Local source differs from pinned version: ' + label)
    results.append({'label': label, 'repository': repo, 'snapshot_sha': sha,
                    'source_path': path, 'local_path': str(local),
                    'immutable_url': 'https://github.com/' + repo + '/blob/' + sha + '/' + path,
                    'latest_change_at_or_before_snapshot': commit['sha'], 'change_dates': dates,
                    'git_blob': git_blob, 'local_matches_pin': matches_pin,
                    'sha256': hashlib.sha256(local.read_bytes()).hexdigest()})
(root / 'source-file-identities.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
