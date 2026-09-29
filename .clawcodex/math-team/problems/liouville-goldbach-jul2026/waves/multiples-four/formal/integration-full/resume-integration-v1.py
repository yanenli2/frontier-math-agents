#!/usr/bin/env python3
"""Resume the interrupted recorder; reuse successful, hash-checked Lean runs.
No Lean source is written and no passed build/compile is repeated.
The first recorder failed only because a theorem identifier ended in apostrophe.
"""
from pathlib import Path
import importlib.util, json, re, tempfile

O = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('checked_run', O / 'check-integration-v1.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def axiom_map(stream):
    result = {}
    # The closing quote is identified by the following diagnostic phrase.
    # Identifier apostrophes and multiline axiom lists remain part of the match.
    pattern = r"^'([^\n]+)'\s+(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)"
    for m in re.finditer(pattern, stream, re.M):
        values = sorted(x.strip() for x in (m[2] or '').split(',') if x.strip())
        assert set(values) <= c.BASE, (m[1], values)
        assert m[1] not in result or result[m[1]] == values
        result[m[1]] = values
    return result


def load_run(tag):
    record = json.loads((O / (tag + '.json')).read_text())
    assert record['exit_code'] == record['expected_exit_code'] == 0, tag
    for suffix in ['stdout', 'stderr']:
        assert c.ident(O / (tag + '.' + suffix)) == record[suffix], (tag, suffix)
    if 'stdin' in record:
        recorded = record['stdin']
        assert c.ident(recorded['path']) == {k: recorded[k] for k in ['sha256', 'bytes']}
    return (O / (tag + '.stdout')).read_text() + (O / (tag + '.stderr')).read_text()


begin = json.loads((O / 'snapshot-before.json').read_text())
c.assert_frozen(begin, True)
rows = c.sigs()
assert rows == json.loads((O / 'signatures-integrated.json').read_text())
graph, order = c.local_graph()
assert graph == json.loads((O / 'local-closure.json').read_text())['graph']
raw_interruption = (Path(tempfile.gettempdir()) / 'clawcodex-bg/bircrgynm.log').read_text()
c.text('recorder-attempt-1.raw.txt', raw_interruption)
outputs = {}
for tag in ['01-default-build', '02-assembly-build', '03-assembly-direct', '04-assembly-trust0']:
    outputs[tag] = load_run(tag)
for i, module in enumerate(order):
    if module == 'Statement.FourWork.Assembly':
        continue
    tag = '05-trust0-' + f'{i:02d}-' + module.replace('.', '-')
    outputs[tag] = load_run(tag)
outputs['06-root-import'] = load_run('06-root-import')
assert 'Statement.FourWork.Assembly' in outputs['01-default-build']
queries = re.findall(r'^#print axioms\s+(\S+)', (O / '06-root-import.stdin.lean').read_text(), re.M)
root_axioms = axiom_map(outputs['06-root-import'])
assert set(root_axioms) == set(queries)
assert "Finset.sum_nbij'" in root_axioms
assert all(row['name'] in root_axioms for row in rows)
for endpoint in ['ArithmeticStatement.representation_four_prime_three_mod_four', 'ArithmeticStatement.representation_multiple_four']:
    assert set(root_axioms[endpoint]) == c.BASE
all_axioms = {}
diagnostics = {}
for tag, stream in outputs.items():
    assert not re.search(r'\b(sorryAx|sorry|admit|native_decide)\b', stream), tag
    parsed = axiom_map(stream)
    for name, values in parsed.items():
        assert name not in all_axioms or all_axioms[name] == values
        all_axioms[name] = values
    diagnostics[tag] = {'axiom_count': len(parsed), 'warnings': [s for s in stream.splitlines() if 'warning:' in s]}
absence = c.run('07-original-endpoints-absent', ['lake', 'env', 'lean', '-t0', '--stdin'],
    stdin='import Statement\n#check ArithmeticStatement.pointwise_keystone\n#check ArithmeticStatement.liouville_goldbach\n', expected=1)
assert absence.count('Unknown identifier') == 2, absence
assert 'ArithmeticStatement.pointwise_keystone' in absence and 'ArithmeticStatement.liouville_goldbach' in absence
expanded = c.run('08-root-expanded-type', ['lake', 'env', 'lean', '-t0', '--stdin'], stdin='''import Statement
set_option autoImplicit false
#check (id (α := ∀ m : ℕ, 0 < m → ∃ a b : ℕ,
    0 < a ∧ 0 < b ∧ 4 * m = a + b ∧
    (-1 : ℤ) ^ a.primeFactorsList.length = (-1 : ℤ) ∧
    (-1 : ℤ) ^ b.primeFactorsList.length = (-1 : ℤ))
  ArithmeticStatement.representation_multiple_four)
#print axioms ArithmeticStatement.representation_multiple_four
''')
assert 'primeFactorsList.length' in expanded, expanded
assert set(axiom_map(expanded)['ArithmeticStatement.representation_multiple_four']) == c.BASE
c.packages('post')
c.assert_frozen(begin, True)
c.save('snapshot-after.json', {p: c.ident(p) for p in begin})
c.save('olean-identities.json', {mod: c.ident(c.L / '.lake/build/lib/lean' / (mod.replace('.', '/') + '.olean')) for mod in order})
c.save('audit-v1.json', {'status': 'PASS', 'utc': c.utc(), 'candidate': {'path': str(c.A), **c.ident(c.A)},
    'root_before': c.ROOT_OLD, 'root_after': c.ident(c.ROOT)['sha256'], 'root_only_change': True,
    'exact_signature_comparisons': 38, 'exact_definition_comparisons': 6,
    'root_axiom_queries': len(queries), 'root_axioms': root_axioms,
    'all_printed_axioms': all_axioms, 'diagnostics': diagnostics,
    'axiom_union': sorted(set(a for xs in all_axioms.values() for a in xs)),
    'admissions': [], 'frozen_file_count': len(begin), 'concurrent_edits_detected': [],
    'new_full_theorem_count': 19, 'earlier_wave_theorem_count': 19,
    'successful_prior_run_count': len(outputs), 'successful_prior_runs_repeated': False,
    'recorder_repair_only': "Parse internal apostrophes in quoted identifiers, including Finset.sum_nbij'; no Lean source or statement changes",
    'original_all_even_target': 'Not proved; original endpoint names absent',
    'remaining_review_obligations': ['Independent integrated-version NL reviews and final regulator are leader-owned'],
    'trust_boundary': 'Installed Lean/Lake compiler, kernel, elaborator/tactic implementations and pinned imported library .olean/build artifacts; no cold bootstrap or complete from-source upstream rebuild. Every local closure file re-elaborated at trust level zero. Standard axioms propext, Classical.choice, Quot.sound only.'})
print('PASS root', c.ident(c.ROOT)['sha256'], 'axiom queries', len(queries))
