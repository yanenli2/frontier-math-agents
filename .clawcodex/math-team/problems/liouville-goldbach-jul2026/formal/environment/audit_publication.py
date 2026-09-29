#!/usr/bin/env python3
"""Find dated public CI metadata for already pinned source commits, not new source versions."""
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'mathlib-manifest.stdout').read_text())
entries = [('mathlib', 'leanprover-community/mathlib4', '905b95818eb32af7874a58b427f50c1711a5e96c'),
           ('lean', 'leanprover/lean4', 'f3b06c705e6c85f5314019d5d3baab0fec5b580c')]
entries += [(p['name'], p['url'].removeprefix('https://github.com/').removesuffix('.git'), p['rev'])
            for p in manifest['packages']]
results = []
for name, repo, sha in entries:
    label = 'public-ci-' + name
    cmd = ['gh', 'api', 'repos/' + repo + '/actions/runs?head_sha=' + sha + '&per_page=100']
    status = subprocess.run([sys.executable, str(root / 'run.py'), label, *cmd], capture_output=True).returncode
    entry = {'name': name, 'sha': sha, 'exit_status': status, 'witnesses': []}
    if status == 0:
        data = json.loads((root / (label + '.stdout')).read_text())
        for run in data.get('workflow_runs', []):
            if run['head_sha'] == sha and run['created_at'] <= '2026-07-31T23:59:59Z':
                entry['witnesses'].append({key: run.get(key) for key in ['name', 'id', 'html_url', 'created_at', 'updated_at', 'event', 'status', 'conclusion', 'head_sha']})
    results.append(entry)
(root / 'public-availability-witnesses.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
