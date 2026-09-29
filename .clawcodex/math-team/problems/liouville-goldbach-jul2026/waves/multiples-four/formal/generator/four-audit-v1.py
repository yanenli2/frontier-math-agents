#!/usr/bin/env python3
"""Audit the completed 19-helper candidate against its reviewed signature snapshot."""
import datetime
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess

root = Path(__file__).resolve().parent
wave = root.parent.parent
problem = wave.parent.parent
project = problem / 'lean'
candidate = root / 'FourCandidate.lean'
interfaces = root / 'four-interfaces-v1.lean'
output = root / 'four-audit-v1.json'
if output.exists():
    raise RuntimeError('Refusing to overwrite audit evidence')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def declarations(text, with_proofs):
    starts = list(re.finditer(r'^theorem (\w+)\b', text, re.M))
    results = {}
    for i, match in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else text.index('\nend ArithmeticStatement', match.start())
        chunk = text[match.start():end].strip()
        header = chunk.split(':=', 1)[0].rstrip() if with_proofs else chunk
        results[match.group(1)] = {'header': header, 'line': text.count('\n', 0, match.start()) + 1}
    return results

ctext = candidate.read_text()
cd, idc = declarations(ctext, True), declarations(interfaces.read_text(), False)
assert len(cd) == len(idc) == 19
assert set(cd) == set(idc)
comparisons = []
for name, decl in cd.items():
    approved = idc[name]
    assert decl['header'] == approved['header']
    comparisons.append({'name': 'ArithmeticStatement.' + name,
                        'candidate_line': decl['line'], 'approved_line': approved['line'],
                        'header_identical': True, 'header': decl['header']})
assert not re.search(r'^theorem (representation_multiple_four|liouville_goldbach|pointwise_keystone)\b', ctext, re.M)
assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe|run_tac)\b', ctext)
assert not re.search(r'^(def|structure|opaque|variable|axiom)\b', ctext, re.M)

build_path = root / 'four-build-04-final-axioms.json'
build = json.loads(build_path.read_text())
stdout_path = root / 'four-build-04-final-axioms.stdout'
assert build['exit_status'] == 0
assert sha(candidate) == build['source_sha256_before'] == build['source_sha256_after']
assert sha(candidate) == sha(Path(build['snapshot']))
assert sha(stdout_path) == build['stdout_sha256']
assert sha(root / 'four-build-04-final-axioms.stderr') == build['stderr_sha256']
stdout = stdout_path.read_text()
axioms = {}
for match in re.finditer(r"'([^\n]+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", stdout):
    axioms[match.group(1)] = [a.strip() for a in (match.group(2) or '').split(',') if a.strip()]
assert len(axioms) == 48
allowed = {'propext', 'Classical.choice', 'Quot.sound'}
assert all(set(ax) <= allowed for ax in axioms.values())
assert all('ArithmeticStatement.' + name in axioms for name in cd)
assert 'Nat.Prime.sq_add_sq' in axioms
assert not re.search(r'\b(sorryAx|error|warning)\b', stdout)

commands = []
def run(argv, cwd):
    result = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=30)
    commands.append({'argv': argv, 'shell_display': shlex.join(argv), 'cwd': str(cwd),
                     'exit_status': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
    assert result.returncode == 0
    return result.stdout.strip()

version = run(['lake', 'env', 'lean', '--version'], project)
manifest = json.loads((project / 'lake-manifest.json').read_text())
checkouts = []
for package in manifest['packages']:
    directory = project / '.lake/packages' / package['name']
    head = run(['git', 'rev-parse', 'HEAD'], directory)
    status = run(['git', 'status', '--short'], directory)
    assert head == package['rev'] and status == ''
    checkouts.append({'package': package['name'], 'pin': package['rev'], 'actual_head': head, 'clean': True})
protected_hashes = {p: sha(Path(p)) for p in build['protected_hashes']}
assert protected_hashes == build['protected_hashes']

mathlib = project / '.lake/packages/mathlib/Mathlib'
source_paths = [mathlib / x for x in [
    'NumberTheory/SumTwoSquares.lean',
    'NumberTheory/Zsqrtd/GaussianInt.lean',
    'NumberTheory/Zsqrtd/QuadraticReciprocity.lean',
    'Data/Nat/Factors.lean', 'Data/Nat/Prime/Defs.lean',
    'Data/Nat/Prime/Basic.lean', 'Data/Nat/ModEq.lean',
    'Data/ZMod/Basic.lean', 'Algebra/Ring/Int/Defs.lean']]
source_hashes = {str(p): sha(p) for p in source_paths}
assert source_hashes[str(source_paths[0])] == 'ecc1647de087331c1876ca386b495ff2a83943a428bf140bf6ba8047f9fd80f9'
cache_path = root / 'four-cache-sum-two-squares-v1.json'
cache = json.loads(cache_path.read_text())
assert cache['exit_status'] == 0
assert cache['manifest_sha256_before'] == cache['manifest_sha256_after'] == sha(project / 'lake-manifest.json')

input_paths = [wave / 'nl/generator/proof-attempt-v1.md', wave / 'nl/reviews/partial-review-v1.md',
               wave / 'formal/reviews/helper-fidelity-v1.md', interfaces,
               wave / 'formal/approved-v1/Declaration.lean']
report = {
    'mode': 'CERTIFICATION compiled candidate; independent acceptance and integration separate',
    'task_id': 'c58d66c51213', 'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'candidate': str(candidate), 'candidate_sha256': sha(candidate),
    'theorem_count': len(cd), 'new_definition_count': 0,
    'statement_comparison': 'Outer whitespace stripped only; all internal bytes of all 19 headers identical.',
    'comparisons': comparisons, 'reviewed_input_hashes': {str(p): sha(p) for p in input_paths},
    'final_build': str(build_path), 'final_build_sha256': sha(build_path),
    'final_build_exit_status': 0, 'stdout_sha256': sha(stdout_path),
    'axiom_report_count': len(axioms), 'axioms': axioms,
    'axiom_union': sorted(set(a for ax in axioms.values() for a in ax)),
    'admitted_or_native_trust_tokens': [], 'diagnostic_warnings': [],
    'imports': re.findall(r'^import (.+)$', ctext, re.M),
    'protected_hashes': protected_hashes, 'library_source_hashes': source_hashes,
    'checkouts': checkouts, 'compiler_version': version, 'commands': commands,
    'cache_record': str(cache_path), 'cache_record_sha256': sha(cache_path),
    'full_target_status': 'OPEN and not declared as a theorem in this candidate',
    'residual_goal': 'p : ℕ; hp : Nat.Prime p; hLower : 7 ≤ p; hMod : p % 4 = 3; ⊢ HasRepresentation (4 * p)',
    'integration_status': 'No master edit; exact candidate offered for independent review before integrator merge',
}
output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({key: report[key] for key in ['candidate_sha256', 'theorem_count', 'new_definition_count',
      'final_build_exit_status', 'axiom_report_count', 'axiom_union', 'compiler_version', 'full_target_status']}, indent=2))
print('Audit evidence: ' + str(output))
