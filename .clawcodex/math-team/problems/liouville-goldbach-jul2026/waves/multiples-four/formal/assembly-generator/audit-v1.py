#!/usr/bin/env python3
"""Audit frozen endpoint compilation and the entire approved local helper graph."""
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
source = project / 'Statement/FourWork/Assembly.lean'
approved_path = wave / 'formal/descent-blueprint/Readback.lean.txt'
output = root / 'audit-v1.json'
if output.exists():
    raise RuntimeError('Refusing to overwrite audit evidence')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def declarations(text, implemented):
    matches = list(re.finditer(r'^(def|theorem) (\w+)\b', text, re.M))
    result = {}
    for i, match in enumerate(matches):
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        chunk = text[match.start():end]
        chunk = re.split(r'^(?:end |namespace |#)', chunk, maxsplit=1, flags=re.M)[0].strip()
        if implemented and match.group(1) == 'theorem':
            chunk = chunk.split(':=', 1)[0].rstrip()
        result[match.group(2)] = {'kind': match.group(1), 'text': chunk,
                               'line': text.count('\n', 0, match.start()) + 1}
    return result

assert sha(source) == 'fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066'
assert sha(approved_path) == '372c3a6b8acfc112331707944bfef543c12ea03049ce5bb95eae7e34f9591763'
approved = declarations(approved_path.read_text(), False)
module_names = ['Statement.FourWork.Descent.Cyclic', 'Statement.FourWork.Descent.Ternary',
                'Statement.FourWork.Character.ResiduePrime', 'Statement.FourWork.Character.ResidueValue',
                'Statement.FourWork.Character.Rigidity', 'Statement.FourWork.Assembly']
modules, comparisons, actual_names = [], [], set()
for module in module_names:
    path = project / (module.replace('.', '/') + '.lean')
    text = path.read_text()
    assert 'set_option autoImplicit false' in text
    assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe|run_tac)\b', text)
    assert not re.search(r'^(variable|axiom|opaque|structure)\b', text, re.M)
    imports = re.findall(r'^import (.+)$', text, re.M)
    decls = declarations(text, True)
    for name, decl in decls.items():
        assert name not in actual_names
        actual_names.add(name)
        assert decl['kind'] == approved[name]['kind'] and decl['text'] == approved[name]['text']
        comparisons.append({'name': name, 'module': module, 'kind': decl['kind'],
                            'candidate_line': decl['line'], 'approved_line': approved[name]['line'],
                            'exact_internal_text_equal': True,
                            'text_sha256_with_final_lf': hashlib.sha256((decl['text']+'\n').encode()).hexdigest()})
    olean = project / ('.lake/build/lib/lean/' + module.replace('.', '/') + '.olean')
    assert olean.exists()
    modules.append({'module': module, 'path': str(path), 'sha256': sha(path),
                    'imports': imports, 'olean': str(olean), 'olean_sha256': sha(olean)})
expected_names = set(approved) - {'omega', 'lambda', 'HasSignedRepresentation', 'HasRepresentation'}
assert actual_names == expected_names
assert sum(x['kind'] == 'theorem' for x in comparisons) == 19
assert sum(x['kind'] == 'def' for x in comparisons) == 2
endpoint_signature_hashes = {c['name']: c['text_sha256_with_final_lf'] for c in comparisons if c['module'] == 'Statement.FourWork.Assembly'}
assert endpoint_signature_hashes == {
    'representation_four_prime_three_mod_four': 'dfd44352a26873c9bdcf1991d5e5c5df3911e1e96f1cff87f8c0e6113fb7e22a',
    'representation_multiple_four': '7a9e41b3137280c725f18e0fa08aa019a0103351b40f3e0440675c0356ec88bd',
}
legacy_path = wave / 'formal/approved-v1/Declaration.lean'
assert sha(legacy_path) == 'bdfb30bcfade7b9df33e48f280125d10a40dd76f365cf5b87047183475fee7ed'
legacy = declarations(legacy_path.read_text(), False)['representation_multiple_four']['text']
final_header = declarations(source.read_text(), True)['representation_multiple_four']['text']
assert re.sub(r'\s+', '', legacy) == re.sub(r'\s+', '', final_header)

# The owned module import graph is acyclic and only Assembly depends on endpoint modules.
graph = {m['module']: [i for i in m['imports'] if i in module_names] for m in modules}
def visit(node, stack):
    assert node not in stack
    for dep in graph[node]:
        visit(dep, stack + [node])
for node in graph:
    visit(node, [])
assert all('Statement.FourWork.Assembly' not in m['imports'] for m in modules)

records = []
for label in ['assembly-01-direct', 'assembly-02-lake-build', 'assembly-03-trust-zero']:
    path = root / (label + '.json')
    record = json.loads(path.read_text())
    assert record['exit_status'] == 0
    assert record['source_sha256_before'] == sha(source) == record['source_sha256_after']
    assert sha(Path(record['snapshot'])) == sha(source)
    assert sha(root / (label + '.stdout')) == record['stdout_sha256']
    assert sha(root / (label + '.stderr')) == record['stderr_sha256']
    assert record['protected_unchanged_after']
    if label != 'assembly-02-lake-build':
        assert not re.search(r'\b(error|warning|sorryAx)\b', (root / (label + '.stdout')).read_text())
    records.append({'path': str(path), 'sha256': sha(path), 'argv': record['argv'], 'exit_status': 0})
protected_hashes = {p: sha(Path(p)) for p in record['protected_hashes']}
assert protected_hashes == record['protected_hashes']
assert 'Statement.FourWork.Assembly' not in (project / 'Statement.lean').read_text()

log = (root / 'assembly-03-trust-zero.stdout').read_text()
axioms = {}
for match in re.finditer(r"'([^\n]+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", log):
    axioms[match.group(1)] = [a.strip() for a in (match.group(2) or '').split(',') if a.strip()]
assert len(axioms) == 69
allowed = {'propext', 'Classical.choice', 'Quot.sound'}
assert all(set(ax) <= allowed for ax in axioms.values())
for c in comparisons:
    prefix = 'ArithmeticStatement.' if c['module'] == 'Statement.FourWork.Assembly' else 'ArithmeticStatement.FourWork.'
    assert prefix + c['name'] in axioms
for name in endpoint_signature_hashes:
    assert set(axioms['ArithmeticStatement.' + name]) == allowed

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
proof_source = wave / 'nl/descent/proof-attempt-v1.md'
assert sha(proof_source) == '23fc6ad19d1c45dd432945aa84756b190700b8c15394b1554ebb3ecaff82235e'

report = {
    'mode': 'CERTIFICATION compiled endpoint candidate; independent acceptance and root promotion separate',
    'task_id': '2db45639290a', 'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'candidate': str(source), 'candidate_sha256': sha(source),
    'approved_snapshot': str(approved_path), 'approved_snapshot_sha256': sha(approved_path),
    'modules': modules, 'module_import_graph': graph, 'graph_acyclic': True,
    'comparisons': comparisons, 'full_graph_theorems': 19, 'full_graph_definitions': 2,
    'endpoint_signature_hashes': endpoint_signature_hashes,
    'legacy_target_equal_up_to_whitespace': True, 'build_records': records,
    'axiom_reports': 69, 'axioms': axioms, 'axiom_union': sorted(allowed),
    'admitted_obligations': [], 'additional_endpoint_hypotheses': [],
    'protected_hashes': protected_hashes, 'compiler_version': version,
    'checkouts': checkouts, 'commands': commands,
    'source_proof': str(proof_source), 'source_proof_sha256': sha(proof_source),
    'fidelity_report': str(wave / 'formal/reviews/descent-fidelity-v1.md'),
    'fidelity_sha256': sha(wave / 'formal/reviews/descent-fidelity-v1.md'),
    'multiples_four_status': 'Exact unrestricted positive-multiple statement compiled with no remaining obligation',
    'original_all_even_status': 'Not proved by this candidate; no liouville_goldbach declaration added',
    'root_promotion': 'Not performed; root Statement.lean remains unchanged and does not import Assembly',
}
output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({key: report[key] for key in ['candidate_sha256', 'full_graph_theorems', 'full_graph_definitions', 'axiom_reports', 'axiom_union', 'multiples_four_status', 'root_promotion']}, indent=2))
print('Audit evidence: ' + str(output))
