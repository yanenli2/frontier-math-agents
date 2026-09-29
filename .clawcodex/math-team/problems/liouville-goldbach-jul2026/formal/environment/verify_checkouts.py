#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
project = root.parent.parent / 'lean'
manifest = json.loads((project / 'lake-manifest.json').read_text())
release = json.loads((root / 'mathlib-manifest.stdout').read_text())
expected = {p['name']: p['rev'] for p in release['packages']}
expected['mathlib'] = '905b95818eb32af7874a58b427f50c1711a5e96c'
assert {p['name']: p['rev'] for p in manifest['packages']} == expected
results = []
for package in manifest['packages']:
    name, rev = package['name'], package['rev']
    directory = project / '.lake/packages' / name
    record = {'name': name, 'expected_rev': rev}
    for suffix, args in [('head', ['rev-parse', 'HEAD']), ('status', ['status', '--porcelain=v1', '--untracked-files=no'])]:
        label = 'final-' + name + '-' + suffix
        completed = subprocess.run([sys.executable, str(root / 'run.py'), label, 'git', '-C', str(directory), *args], capture_output=True)
        assert completed.returncode == 0
        record[suffix] = (root / (label + '.stdout')).read_text().strip()
    assert record['head'] == rev and record['status'] == ''
    results.append(record)
assert (project / '.lake/packages/mathlib/lake-manifest.json').read_bytes() == (root / 'mathlib-manifest.stdout').read_bytes()
(root / 'checkout-audit.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
