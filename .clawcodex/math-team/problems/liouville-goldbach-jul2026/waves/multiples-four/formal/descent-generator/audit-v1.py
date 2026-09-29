#!/usr/bin/env python3
"""Compare all seven approved descent headers and audit actual direct/Lake builds."""
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
snapshot = wave / 'formal/descent-blueprint/Readback.lean.txt'
output = root / 'audit-v1.json'
if output.exists():
    raise RuntimeError('Refusing to overwrite audit evidence')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def headers(text, proved):
    matches = list(re.finditer(r'^theorem (\w+)\b', text, re.M))
    result = {}
    for i, match in enumerate(matches):
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        chunk = text[match.start():end]
        if proved:
            chunk = chunk.split(':=', 1)[0]
        else:
            chunk = re.split(r'^end ', chunk, maxsplit=1, flags=re.M)[0]
        result[match.group(1)] = {'header': chunk.strip(), 'line': text.count('\n', 0, match.start()) + 1}
    return result

expected = {
    'cyclic_short_multiple': 'aad618b6d15cfbf061dc18936d91becbf4d2e2816c199aa1a0153ce255188182',
    'lambda_reflection_eq_one_of_neg': 'f65b58b57c96085fd4c6f24c388988301bfd6a9a4024d3b3ab7d47053be51529',
    'lambda_double_reflection_eq_neg_one_of_pos': '6b2eeb821e58532ffbd1a21a16107129f31efc184c23a5a92e327cf7b623284e',
    'three_not_dvd_of_positive_pair': '9f380c462b87b1bef9d7c683893e808359726460a40fbd96ee776648bb1d57ae',
    'positive_pair_gap_step': '04c8c1983e2ddef6edf6051463bb4b1d4a2c0455e6c77dd8b3e5bd6601ccb35e',
    'no_positive_pair': 'f712da17ce78c49776ee2e33ae75399a99657f1a163d9b39ae0aca6cb7166d52',
    'lambda_antireflection_of_no_representation': '2e98d41965376ae2e1b5b1813e25d83ef3e5bf875dfcea49c4e89b98320e32cd',
}
assert sha(snapshot) == '372c3a6b8acfc112331707944bfef543c12ea03049ce5bb95eae7e34f9591763'
approved = headers(snapshot.read_text(), False)
modules, comparisons, axiom_sets = [], [], {}
for module, direct, build in [('Cyclic', 'cyclic-02', 'cyclic-03-lake-build'), ('Ternary', 'ternary-03', 'ternary-04-lake-build')]:
    source = project / ('Statement/FourWork/Descent/' + module + '.lean')
    text = source.read_text()
    actual = headers(text, True)
    assert len(actual) == (1 if module == 'Cyclic' else 6)
    assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe|run_tac)\b', text)
    assert not re.search(r'^(def|structure|opaque|variable|axiom)\b', text, re.M)
    assert not re.search(r'\b(representation_four_prime_three_mod_four|representation_multiple_four|lambda_eq_one_of_isSquare|residueLambda_mul)\b', text)
    for name, decl in actual.items():
        assert decl['header'] == approved[name]['header']
        signature_hash = hashlib.sha256((decl['header'] + '\n').encode()).hexdigest()
        assert signature_hash == expected[name]
        comparisons.append({'name': 'ArithmeticStatement.FourWork.' + name, 'module': module,
                            'candidate_line': decl['line'], 'approved_line': approved[name]['line'],
                            'signature_sha256': signature_hash, 'exact_internal_text_equal': True})
    records = []
    for label in [direct, build]:
        record_path = root / (label + '.json')
        record = json.loads(record_path.read_text())
        assert record['exit_status'] == 0
        assert record['source_sha256_before'] == sha(source) == record['source_sha256_after']
        assert sha(Path(record['snapshot'])) == sha(source)
        assert sha(root / (label + '.stdout')) == record['stdout_sha256']
        assert sha(root / (label + '.stderr')) == record['stderr_sha256']
        assert record['protected_unchanged_after']
        records.append({'path': str(record_path), 'sha256': sha(record_path), 'argv': record['argv'], 'exit_status': 0})
    log = (root / (direct + '.stdout')).read_text()
    assert not re.search(r'\b(sorryAx|error|warning)\b', log)
    module_axioms = {}
    for match in re.finditer(r"'([^\n]+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", log):
        module_axioms[match.group(1)] = [a.strip() for a in (match.group(2) or '').split(',') if a.strip()]
    for name in actual:
        assert 'ArithmeticStatement.FourWork.' + name in module_axioms
    assert all(set(ax) <= {'propext', 'Classical.choice', 'Quot.sound'} for ax in module_axioms.values())
    axiom_sets.update(module_axioms)
    olean = project / ('.lake/build/lib/lean/Statement/FourWork/Descent/' + module + '.olean')
    assert olean.exists()
    modules.append({'module': 'Statement.FourWork.Descent.' + module, 'source': str(source),
                    'source_sha256': sha(source), 'olean': str(olean), 'olean_sha256': sha(olean),
                    'imports': re.findall(r'^import (.+)$', text, re.M), 'records': records,
                    'axioms': module_axioms})
assert {c['name'].split('.')[-1] for c in comparisons} == set(expected)

commands = []
def run(argv, cwd):
    result = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=30)
    assert result.returncode == 0
    commands.append({'argv': argv, 'shell_display': shlex.join(argv), 'cwd': str(cwd),
                     'exit_status': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
    return result.stdout.strip()
version = run(['lake', 'env', 'lean', '--version'], project)
manifest = json.loads((project / 'lake-manifest.json').read_text())
checkouts = []
for package in manifest['packages']:
    checkout = project / '.lake/packages' / package['name']
    head = run(['git', 'rev-parse', 'HEAD'], checkout)
    status = run(['git', 'status', '--short'], checkout)
    assert head == package['rev'] and status == ''
    checkouts.append({'name': package['name'], 'pin': head, 'clean': True})
protected_hashes = {p: sha(Path(p)) for p in record['protected_hashes']}
assert protected_hashes == record['protected_hashes']
source = wave / 'nl/descent/proof-attempt-v1.md'
assert sha(source) == '23fc6ad19d1c45dd432945aa84756b190700b8c15394b1554ebb3ecaff82235e'
field_source = project / '.lake/packages/mathlib/Mathlib/Algebra/Field/ZMod.lean'
report = {'mode': 'CERTIFICATION candidate production; independent acceptance and integration separate',
          'task_id': '8770ba99c0f5', 'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'modules': modules, 'comparisons': comparisons, 'exported_theorem_count': 7,
          'axiom_report_count': sum(len(m['axioms']) for m in modules),
          'axiom_union': sorted(set(a for ax in axiom_sets.values() for a in ax)),
          'new_definition_count': 0, 'admitted_obligations': [],
          'endpoint_dependencies': [], 'protected_hashes': protected_hashes,
          'source': str(source), 'source_sha256': sha(source),
          'fidelity_report': str(wave / 'formal/reviews/descent-fidelity-v1.md'),
          'fidelity_sha256': sha(wave / 'formal/reviews/descent-fidelity-v1.md'),
          'prime_field_source': str(field_source), 'prime_field_source_sha256': sha(field_source),
          'compiler_version': version, 'checkouts': checkouts, 'commands': commands,
          'full_target_status': 'Not supplied in these modules; await character package and authorized Assembly proof',
          'master_status': 'Existing masters/root/pins unchanged; only assigned scratch modules built'}
output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'exported_theorems': 7, 'axiom_reports': report['axiom_report_count'],
                  'axiom_union': report['axiom_union'], 'modules': [(m['module'], m['source_sha256']) for m in modules]}, indent=2))
print('Audit evidence: ' + str(output))
