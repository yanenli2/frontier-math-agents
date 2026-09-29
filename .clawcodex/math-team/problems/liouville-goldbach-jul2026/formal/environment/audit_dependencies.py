#!/usr/bin/env python3
"""Audit only the immutable dependency commits fixed by the eligible Mathlib release."""
import datetime
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
runner = root / 'run.py'
cutoff = '2026-07-31T23:59:59Z'
manifest = json.loads((root / 'mathlib-manifest.stdout').read_text())
pins = {p['name']: p['rev'] for p in manifest['packages']}
results = []

def capture(label, command):
    completed = subprocess.run([sys.executable, str(runner), label, *command], capture_output=True)
    return completed.returncode, (root / (label + '.stdout')).read_text()

for package in manifest['packages']:
    name, sha = package['name'], package['rev']
    repo = package['url'].removeprefix('https://github.com/').removesuffix('.git')
    status, raw = capture('dep-' + name + '-commit', ['gh', 'api', 'repos/' + repo + '/git/commits/' + sha])
    if status:
        raise RuntimeError('metadata failed: ' + name)
    commit = json.loads(raw)
    dates = {'author': commit['author']['date'], 'committer': commit['committer']['date']}
    if commit['sha'] != sha or any(d > cutoff for d in dates.values()):
        raise RuntimeError('ineligible dependency metadata: ' + name)
    entry = {'name': name, 'repo': repo, 'sha': sha, 'dates': dates,
             'availability_witness': 'Immutable pin in Mathlib v4.32.2 release manifest; release published 2026-07-28T16:47:51Z',
             'files': {}}
    for filename, suffix in [('lake-manifest.json', 'manifest'), ('lean-toolchain', 'toolchain'), (package['configFile'], 'lakefile')]:
        label = 'dep-' + name + '-' + suffix
        status, raw = capture(label, ['gh', 'api', '-H', 'Accept: application/vnd.github.raw+json',
                                     'repos/' + repo + '/contents/' + filename + '?ref=' + sha])
        entry['files'][filename] = {'command_exit_status': status, 'capture': label + '.stdout'}
        if suffix == 'manifest' and status == 0:
            nested = json.loads(raw)
            entry['nested_pins'] = [{'name': p['name'], 'rev': p.get('rev'),
                                     'root_revision': pins.get(p['name']),
                                     'agrees_with_root': p.get('rev') == pins.get(p['name'])}
                                    for p in nested.get('packages', [])]
        if suffix == 'toolchain' and status == 0:
            entry['toolchain'] = raw.strip()
    results.append(entry)
(root / 'dependency-pins.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
