#!/usr/bin/env python3
"""Initialize only audited immutable Git commits; do not resolve moving branches."""
import copy
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
project = root.parent.parent / 'lean'
runner = root / 'run.py'
manifest = json.loads((root / 'mathlib-manifest.stdout').read_text())
mathlib = {'url': 'https://github.com/leanprover-community/mathlib4', 'type': 'git',
           'subDir': None, 'scope': '', 'rev': '905b95818eb32af7874a58b427f50c1711a5e96c',
           'name': 'mathlib', 'manifestFile': 'lake-manifest.json',
           'inputRev': '905b95818eb32af7874a58b427f50c1711a5e96c', 'inherited': False,
           'configFile': 'lakefile.lean'}
pins = copy.deepcopy(manifest['packages'])
for pin in pins:
    pin['inherited'] = True
pins.append(mathlib)
root_manifest = {'version': manifest['version'], 'packagesDir': '.lake/packages',
                 'packages': pins, 'name': 'liouvilleStatement', 'lakeDir': '.lake',
                 'fixedToolchain': False}
if (project / 'lake-manifest.json').exists():
    raise RuntimeError('Refusing to overwrite existing root manifest')
(project / 'lake-manifest.json').write_text(json.dumps(root_manifest, indent=2) + '\n')

def run(label, command):
    result = subprocess.run([sys.executable, str(runner), '--timeout', '180', label, *command], capture_output=True)
    if result.returncode:
        print(result.stdout.decode(errors='replace'))
        print(result.stderr.decode(errors='replace'))
        raise RuntimeError('Failed: ' + label)

for pin in [mathlib] + pins[:-1]:
    name, rev, url = pin['name'], pin['rev'], pin['url']
    checkout = project / '.lake' / 'packages' / name
    run(name + '-git-init', ['git', 'init', str(checkout)])
    run(name + '-git-remote', ['git', '-C', str(checkout), 'remote', 'add', 'origin', url])
    run(name + '-git-fetch', ['git', '-C', str(checkout), 'fetch', '--depth', '1', '--no-tags', 'origin', rev])
    run(name + '-git-checkout', ['git', '-C', str(checkout), 'checkout', '--detach', rev])
    run(name + '-git-identity', ['git', '-C', str(checkout), 'show', '-s', '--format=%H%n%aI%n%cI', 'HEAD'])
    print(name, rev, 'checked out')
