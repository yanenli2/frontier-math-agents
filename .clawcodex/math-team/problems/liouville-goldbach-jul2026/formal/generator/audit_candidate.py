#!/usr/bin/env python3
"""Audit candidate/interface identity, full printed axiom coverage and immutable pins."""
import datetime
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess

root = Path(__file__).resolve().parent
problem = root.parent.parent
project = problem / 'lean'
candidate = root / 'Candidate.lean'
interfaces = problem / 'formal/blueprinter/interfaces-v1.lean'
final_build = root / 'build-09-final-axioms.json'
final_stdout = root / 'build-09-final-axioms.stdout'
output = root / 'audit-v1.json'
if output.exists():
    raise RuntimeError('Refusing to overwrite audit evidence')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def declarations(text):
    starts = list(re.finditer(r'^(def|theorem) (\w+)\b', text, re.M))
    result = {}
    for i, match in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else text.index('\nend ArithmeticStatement', match.start())
        chunk = text[match.start():end].strip()
        kind, name = match.groups()
        body = chunk.split(':=', 1)[0].rstrip() if kind == 'theorem' else chunk
        result[name] = {'kind': kind, 'protected_text': body, 'line': text.count('\n', 0, match.start()) + 1}
    return result

ctext, itext = candidate.read_text(), interfaces.read_text()
cdecls, idecls = declarations(ctext), declarations(itext)
open_names = {'pointwise_keystone', 'liouville_goldbach'}
assert set(idecls) - set(cdecls) == open_names
assert set(cdecls) <= set(idecls)
comparisons = []
for name, decl in cdecls.items():
    approved = idecls[name]
    comparisons.append({
        'name': 'ArithmeticStatement.' + name, 'kind': decl['kind'],
        'candidate_line': decl['line'], 'approved_line': approved['line'],
        'identical_stripped_text': decl['protected_text'] == approved['protected_text'],
        'comparison': 'full definition' if decl['kind'] == 'def' else 'header before proof assignment',
        'header_or_definition': decl['protected_text'],
    })
assert all(x['identical_stripped_text'] for x in comparisons)

build = json.loads(final_build.read_text())
assert build['exit_status'] == 0 and build['source_sha256_before'] == sha(candidate) == build['source_sha256_after']
assert sha(candidate) == sha(Path(build['snapshot']))
assert build['stdout_sha256'] == sha(final_stdout)
stdout = final_stdout.read_text()
axioms = {}
for match in re.finditer(r"'([^\n]+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", stdout):
    axioms[match.group(1)] = [s.strip() for s in (match.group(2) or '').split(',') if s.strip()]
allowed = {'propext', 'Classical.choice', 'Quot.sound'}
assert all(set(ax) <= allowed for ax in axioms.values())
assert all('ArithmeticStatement.' + name in axioms for name in cdecls)
assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe|run_tac)\b', ctext)
assert not re.search(r'(^|\n).*\berror(?:\(|:)', stdout)

commands = []
def run(argv, cwd):
    result = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=30)
    commands.append({'argv': argv, 'shell_display': shlex.join(argv), 'cwd': str(cwd),
                     'exit_status': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
    assert result.returncode == 0
    return result.stdout.strip()

lean_version = run(['lake', 'env', 'lean', '--version'], project)
manifest = json.loads((project / 'lake-manifest.json').read_text())
checkouts = []
for package in manifest['packages']:
    checkout = project / '.lake/packages' / package['name']
    head = run(['git', 'rev-parse', 'HEAD'], checkout)
    status = run(['git', 'status', '--short'], checkout)
    assert head == package['rev'] and status == ''
    checkouts.append({'name': package['name'], 'manifest_pin': package['rev'], 'actual_head': head, 'clean': not status})

protected_hashes = {p: sha(Path(p)) for p in build['protected_hashes']}
assert protected_hashes == build['protected_hashes']
report = {
    'mode': 'CERTIFICATION candidate evidence; separate independent acceptance and integration required',
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'candidate': str(candidate), 'candidate_sha256': sha(candidate),
    'approved_interfaces': str(interfaces), 'approved_interfaces_sha256': sha(interfaces),
    'definitions_count': sum(d['kind'] == 'def' for d in cdecls.values()),
    'theorems_count': sum(d['kind'] == 'theorem' for d in cdecls.values()),
    'statement_comparison_scope': 'Only outer whitespace stripped. All internal bytes of definition bodies and theorem headers match approved snapshot.',
    'comparisons': comparisons,
    'absent_open_endpoints': sorted(open_names),
    'final_build': str(final_build), 'final_build_sha256': sha(final_build),
    'final_build_exit_status': build['exit_status'], 'final_stdout_sha256': sha(final_stdout),
    'axiom_report_count': len(axioms), 'axioms': axioms,
    'axiom_union': sorted(set(a for ax in axioms.values() for a in ax)),
    'admitted_or_native_trust_tokens': [],
    'candidate_imports': re.findall(r'^import (.+)$', ctext, re.M),
    'protected_hashes': protected_hashes, 'checkouts': checkouts,
    'lean_version': lean_version, 'commands': commands,
    'residual_goal': 'N : ℕ; hEven : Even N; hN : 2 < N; ⊢ 2 * L (N - 1) - ((N : ℤ) - 1) < C N',
    'final_target_status': 'OPEN: no declaration ArithmeticStatement.liouville_goldbach and no proof of Target',
}
output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({k: report[k] for k in ['candidate_sha256', 'definitions_count', 'theorems_count', 'axiom_report_count', 'axiom_union', 'absent_open_endpoints', 'final_build_exit_status', 'lean_version']}, indent=2, ensure_ascii=False))
print('Audit evidence: ' + str(output))
