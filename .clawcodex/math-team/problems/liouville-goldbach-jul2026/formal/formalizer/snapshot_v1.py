#!/usr/bin/env python3
"""Hash the production snapshot; does not confer mathematical acceptance."""
import datetime
import hashlib
import json
from pathlib import Path

own = Path(__file__).resolve().parent
problem = own.parent.parent
environment = own.parent / 'environment'
review = problem.parent.parent / 'review-inputs/r20260924-v1'
target = own / 'snapshot-v1.json'
if target.exists():
    raise RuntimeError('Refusing to overwrite production snapshot')
assert (problem / 'lean/Statement/Definitions.lean').read_bytes() == (review / 'Declaration.lean').read_bytes()

files = [problem / 'request.md', problem / 'RUN.md']
files += [problem / ('lean/' + name) for name in [
    'lean-toolchain', 'lakefile.toml', 'lake-manifest.json', 'Statement.lean',
    'Statement/Definitions.lean', 'Statement/Scaffold.lean', 'Statement/Smoke.lean',
    '.lake/build/lib/lean/Statement.olean',
    '.lake/build/lib/lean/Statement/Definitions.olean',
    '.lake/build/lib/lean/Statement/Scaffold.olean',
    '.lake/build/lib/lean/Statement/Smoke.olean']]
files += [review / name for name in ['Declaration.lean', 'Dependencies.lean', 'ListOperations.lean']]
files += [p for p in own.iterdir() if p.is_file() and p != target]
files += [p for p in environment.iterdir() if p.is_file()]
files = sorted(set(files))
identities = [{'path': str(p), 'bytes': p.stat().st_size,
               'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
record = {
    'snapshot_kind': 'Unapproved production snapshot, not a theorem proof or acceptance record',
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'task': 'ca76ab6f021e', 'role': 'fl-formalizer',
    'target': 'ArithmeticStatement.Target (definition of Prop only; no proof)',
    'mathlib_revision': '905b95818eb32af7874a58b427f50c1711a5e96c',
    'lean_revision': 'f3b06c705e6c85f5314019d5d3baab0fec5b580c',
    'neutral_declaration_byte_identical_to_compiled_definition': True,
    'files': identities
}
target.write_text(json.dumps(record, indent=2) + '\n')
print('production snapshot:', target)
print('snapshot SHA256:', hashlib.sha256(target.read_bytes()).hexdigest())
print('hashed file count:', len(identities))
