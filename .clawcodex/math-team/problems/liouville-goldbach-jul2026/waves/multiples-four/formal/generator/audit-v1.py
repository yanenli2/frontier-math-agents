#!/usr/bin/env python3
"""Audit failed exact-statement attempts and successful dependency-only evidence."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parent
wave = root.parent.parent
problem = wave.parent.parent
project = problem / 'lean'
output = root / 'audit-v1.json'
if output.exists():
    raise RuntimeError('Refusing to overwrite audit evidence')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def header(text):
    match = re.search(r'^theorem representation_multiple_four .*?\n  HasRepresentation \(4 \* m\)', text, re.M | re.S)
    assert match is not None
    return match.group(0) + '\n'

approved = wave / 'formal/approved-v1/Declaration.lean'
approved_header = header(approved.read_text())
assert hashlib.sha256(approved_header.encode()).hexdigest() == '8553b2804a2be4c99b92e7e8127e588b00351a5d650386160c3056ee997d1728'
attempts = []
for source_name, label in [('Attempt-v1.lean', 'build-01-residual'), ('Attempt-v2.lean', 'build-02-prime-core')]:
    source = root / source_name
    record = json.loads((root / (label + '.json')).read_text())
    assert record['exit_status'] == 1
    assert record['source_sha256_before'] == sha(source) == record['source_sha256_after']
    assert header(source.read_text()) == approved_header
    assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe)\b', source.read_text())
    assert sha(root / (label + '.stdout')) == record['stdout_sha256']
    attempts.append({'source': str(source), 'sha256': sha(source),
                     'statement_header_identical': True, 'exit_status': 1,
                     'status': 'INCOMPLETE, not accepted or importable',
                     'build_record': str(root / (label + '.json'))})

audit_record = json.loads((root / 'build-03-dependency-audit.json').read_text())
assert audit_record['exit_status'] == 0
assert audit_record['source_sha256_before'] == sha(root / 'DependencyAudit.lean')
axiom_log = (root / 'build-03-dependency-audit.stdout').read_text()
axioms = {}
for match in re.finditer(r"'([^\n]+)' depends on axioms: \[([^\]]*)\]", axiom_log):
    axioms[match.group(1)] = [a.strip() for a in match.group(2).split(',')]
assert len(axioms) == 17
assert all(set(a) == {'propext', 'Classical.choice', 'Quot.sound'} for a in axioms.values())
assert 'representation_multiple_four' not in (root / 'DependencyAudit.lean').read_text()
commands = []
for argv, cwd in [(['lake', 'env', 'lean', '--version'], project),
                  (['git', 'rev-parse', 'HEAD'], project / '.lake/packages/mathlib'),
                  (['git', 'status', '--short'], project / '.lake/packages/mathlib')]:
    result = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=30)
    assert result.returncode == 0
    commands.append({'argv': argv, 'cwd': str(cwd), 'exit_status': result.returncode,
                     'stdout': result.stdout, 'stderr': result.stderr})
assert commands[1]['stdout'].strip() == '905b95818eb32af7874a58b427f50c1711a5e96c'
assert commands[2]['stdout'].strip() == ''
protected_hashes = {p: sha(Path(p)) for p in audit_record['protected_hashes']}
assert protected_hashes == audit_record['protected_hashes']
report = {'mode': 'CERTIFICATION focused attempt; mathematical blocker, not a proved target',
          'approved_statement': str(approved), 'approved_sha256': sha(approved),
          'header_sha256': hashlib.sha256(approved_header.encode()).hexdigest(),
          'attempts': attempts,
          'target_proof_status': 'UNPROVED; no successful target compilation or target axiom certificate',
          'dependency_audit_exit_status': 0, 'dependency_axioms': axioms,
          'dependency_audit_scope': 'Accepted pre-existing declarations only; not the new target',
          'protected_hashes': protected_hashes, 'commands': commands,
          'next_obligation': 'For arbitrary p : Nat, hp : Nat.Prime p, hpne : p ≠ 2, construct HasRepresentation (4*p).',
          'master_integration': 'Nothing proposed for integration; existing master unchanged'}
output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print('Exact approved target header preserved in both failed attempts.')
print('Both target compiles exit 1 at explicit residual goals, not setup errors.')
print('Accepted-dependency audit exit 0; 17 standard-only axiom reports.')
print('All checked protected hashes unchanged. Output: ' + str(output))
