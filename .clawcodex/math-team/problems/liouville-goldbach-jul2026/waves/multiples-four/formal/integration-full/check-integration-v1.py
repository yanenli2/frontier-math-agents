#!/usr/bin/env python3
"""Mechanical frozen-candidate integration audit. No Lean source is written.
Run preflight before the one authorized root import edit; then run integrated.
Evidence outputs use exclusive creation to preserve every earlier run.
"""
from pathlib import Path
import datetime, difflib, hashlib, json, re, shlex, subprocess, sys, time

O = Path(__file__).resolve().parent
W = O.parents[1]
P = W.parents[1]
L = P / 'lean'
ROOT = L / 'Statement.lean'
A = L / 'Statement/FourWork/Assembly.lean'
REVIEW = W / 'formal/reviews/full-candidate-review-v1'
BASE = {'propext', 'Classical.choice', 'Quot.sound'}
ROOT_OLD = 'dc72b845dbb045593ef3a6212b03a54cc0797a29baac132e870aff324cdc5853'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def ident(p):
    b = Path(p).read_bytes()
    return {'sha256': sha(b), 'bytes': len(b)}


def save(name, value):
    with (O / name).open('x') as f:
        f.write(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def text(name, s):
    with (O / name).open('x') as f:
        f.write(s)


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def run(tag, argv, cwd=L, stdin=None, expected=0):
    start = utc()
    t = time.monotonic()
    proc = subprocess.run(argv, cwd=cwd, input=stdin, capture_output=True, text=True, timeout=600)
    text(tag + '.stdout', proc.stdout)
    text(tag + '.stderr', proc.stderr)
    if stdin is not None:
        text(tag + '.stdin.lean', stdin)
    record = {'argv': argv, 'shell_display': shlex.join(argv), 'cwd': str(cwd),
              'started_utc': start, 'seconds': time.monotonic() - t,
              'exit_code': proc.returncode, 'expected_exit_code': expected,
              'stdout': ident(O / (tag + '.stdout')), 'stderr': ident(O / (tag + '.stderr'))}
    if stdin is not None:
        record['stdin'] = {'path': str(O / (tag + '.stdin.lean')), **ident(O / (tag + '.stdin.lean'))}
    save(tag + '.json', record)
    print(tag, 'exit', proc.returncode, flush=True)
    assert proc.returncode == expected, (tag, proc.returncode, proc.stderr)
    return proc.stdout + proc.stderr


def block(p, kind, name):
    s = Path(p).read_text()
    m = re.search(r'^' + kind + r'\s+' + re.escape(name) + r'\b', s, re.M)
    assert m, (p, kind, name)
    part = s[m.start():].split('\n\n', 1)[0]
    if kind == 'theorem':
        part = part.split(':=', 1)[0]
    return part.strip(), s[:m.start()].count('\n') + 1


def sigs():
    blueprint = W / 'formal/descent-blueprint/Readback.lean.txt'
    rows = []
    files = [L / 'Statement/Definitions.lean', L / 'Statement/Partial.lean',
             L / 'Statement/FourPartial.lean', *sorted((L / 'Statement/FourWork').rglob('*.lean'))]
    for kind, name in re.findall(r'^(def|theorem)\s+(\w+)', blueprint.read_text(), re.M):
        matches = [p for p in files if re.search(r'^' + kind + r'\s+' + name + r'\b', p.read_text(), re.M)]
        assert len(matches) == 1, (name, matches)
        p = matches[0]
        actual, line = block(p, kind, name)
        approved, approved_line = block(blueprint, kind, name)
        assert actual == approved, (name, actual, approved)
        namespace = 'ArithmeticStatement.' + ('FourWork.' if 'FourWork' in p.parts and p != A else '')
        rows.append({'packet': 'full', 'kind': kind, 'name': namespace + name,
                     'actual_path': str(p), 'actual_line': line, 'approved_path': str(blueprint),
                     'approved_line': approved_line, 'exact_internal_text_equal': True,
                     'text': actual, 'text_sha256_with_lf': sha((actual + '\n').encode())})
    old = W / 'formal/generator/four-interfaces-v1.lean'
    for name in re.findall(r'^theorem\s+(\w+)', old.read_text(), re.M):
        p = L / 'Statement/FourPartial.lean'
        actual, line = block(p, 'theorem', name)
        approved, approved_line = block(old, 'theorem', name)
        assert actual == approved, name
        rows.append({'packet': 'partial', 'kind': 'theorem', 'name': 'ArithmeticStatement.' + name,
                     'actual_path': str(p), 'actual_line': line, 'approved_path': str(old),
                     'approved_line': approved_line, 'exact_internal_text_equal': True,
                     'text': actual, 'text_sha256_with_lf': sha((actual + '\n').encode())})
    actual, _ = block(A, 'theorem', 'representation_multiple_four')
    approved, _ = block(W / 'formal/approved-v1/Declaration.lean', 'theorem', 'representation_multiple_four')
    assert re.sub(r'\s+', '', actual) == re.sub(r'\s+', '', approved)
    assert len([r for r in rows if r['packet'] == 'full' and r['kind'] == 'theorem']) == 19
    assert len([r for r in rows if r['packet'] == 'full' and r['kind'] == 'def']) == 6
    assert len([r for r in rows if r['packet'] == 'partial']) == 19
    return rows


def imports(p):
    return re.findall(r'^import\s+(\S+)', p.read_text(), re.M)


def local_graph():
    graph = {}
    order = []
    active = set()
    def visit(m):
        if m in active:
            raise AssertionError(('import cycle', m))
        if m in graph:
            return
        active.add(m)
        p = L / (m.replace('.', '/') + '.lean')
        imps = imports(p)
        for dep in imps:
            if dep == 'Statement' or dep.startswith('Statement.'):
                visit(dep)
        active.remove(m)
        graph[m] = imps
        order.append(m)
    visit('Statement')
    assert len(graph) == 12, graph.keys()
    return graph, order


def axiom_map(stream):
    out = {}
    pattern = r"'([^']+)'\s+(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)"
    for m in re.finditer(pattern, stream, re.S):
        vals = sorted(x.strip() for x in (m[2] or '').split(',') if x.strip())
        assert set(vals) <= BASE, (m[1], vals)
        assert m[1] not in out or out[m[1]] == vals
        out[m[1]] = vals
    return out


def assert_frozen(begin, integrated):
    changes = {}
    for p, expected in begin.items():
        now = ident(p)
        if p == str(ROOT) and integrated:
            old = (O / 'Statement.before.lean.txt').read_bytes()
            assert ROOT.read_bytes() == old + b'import Statement.FourWork.Assembly\n'
        elif now != expected:
            changes[p] = {'expected': expected, 'actual': now}
    assert not changes, ('concurrent/frozen edits', changes)


def packages(phase):
    result = []
    pins = {p['name']: p for p in json.loads((L / 'lake-manifest.json').read_text())['packages']}
    witnesses = {r['name']: r for r in json.loads((P / 'formal/environment/public-availability-witnesses.json').read_text())}
    cutoff = '2026-08-01T00:00:00Z'
    for name, pin in pins.items():
        d = L / '.lake/packages' / name
        head = run(phase + '-pin-' + name, ['git', 'rev-parse', 'HEAD'], d).strip()
        clean = run(phase + '-clean-' + name, ['git', 'status', '--porcelain', '--untracked-files=all'], d)
        assert head == pin['rev'], name
        assert clean == '', (name, clean)
        eligible = [w for w in witnesses[name]['witnesses']
                    if w['head_sha'] == head and w['created_at'] < cutoff]
        assert witnesses[name]['sha'] == head and eligible, name
        witness = min(eligible, key=lambda w: w['created_at'])
        nested = d / 'lake-manifest.json'
        nested_id = None
        if nested.exists():
            nested_id = ident(nested)
            for dependency in json.loads(nested.read_text()).get('packages', []):
                assert dependency['name'] in pins
                assert dependency['rev'] == pins[dependency['name']]['rev'], (name, dependency)
        result.append({'name': name, 'revision': head, 'source_url': pin['url'] + '/tree/' + head,
                       'clean': True, 'witness': witness, 'nested_manifest': nested_id})
    lean_sha = 'f3b06c705e6c85f5314019d5d3baab0fec5b580c'
    assert witnesses['lean']['sha'] == lean_sha
    assert any(w['head_sha'] == lean_sha and w['created_at'] < cutoff for w in witnesses['lean']['witnesses'])
    save(phase + '-provenance.json', {'packages': result, 'lean_witness': witnesses['lean'],
           'metadata_source': str(P / 'formal/environment/public-availability-witnesses.json'),
           'metadata_identity': ident(P / 'formal/environment/public-availability-witnesses.json'),
           'cutoff_exclusive': cutoff, 'method': 'Offline retained exact-SHA public CI witnesses; no network/update/install'})


def preflight():
    reviewed = json.loads(Path(str(REVIEW) + '.snapshot-begin.json').read_text())['files']
    for p, data in reviewed.items():
        assert ident(p)['sha256'] == data['sha256'], ('reviewed candidate changed', p)
    assert ident(ROOT)['sha256'] == ROOT_OLD
    assert 'VERDICT: APPROVE' in Path(str(REVIEW) + '.md').read_text()
    paths = set(reviewed)
    paths.update(str(p) for p in (W / 'formal/reviews').glob('*') if p.is_file())
    for p in [P / 'FINAL_ARGUMENT.md', P / 'REPRODUCE.md', P / 'LEMMA_MAP.md', P / 'sources.md',
              P / 'formal/environment/public-availability-witnesses.json',
              W / 'formal/assembly-generator/audit-v1.json',
              W / 'formal/assembly-generator/proof-status-map-v1.txt',
              W / 'formal/descent-generator/audit-v1.json',
              W / 'formal/character-generator/statement-comparison-v1.json',
              W / 'formal/character-generator/provenance-v1.json']:
        assert p.exists(), p
        paths.add(str(p))
    begin = {p: ident(p) for p in sorted(paths)}
    save('snapshot-before.json', begin)
    text('Statement.before.lean.txt', ROOT.read_text())
    text('REPRODUCE.before.md.txt', (W / 'REPRODUCE.md').read_text())
    save('signatures-before.json', sigs())
    version = run('pre-lean-version', ['lake', 'env', 'lean', '--version'])
    assert '4.32.2' in version and 'f3b06c705e6c85f5314019d5d3baab0fec5b580c' in version
    run('pre-lake-version', ['lake', '--version'])
    packages('pre')
    assert_frozen(begin, False)
    save('preflight-pass.json', {'utc': utc(), 'status': 'PASS', 'frozen_file_count': len(begin),
                               'root_sha256': ident(ROOT)['sha256']})


def integrated():
    begin = json.loads((O / 'snapshot-before.json').read_text())
    assert_frozen(begin, True)
    rows = sigs()
    save('signatures-integrated.json', rows)
    graph, order = local_graph()
    old = (O / 'Statement.before.lean.txt').read_text()
    text('integration.diff', ''.join(difflib.unified_diff(old.splitlines(True), ROOT.read_text().splitlines(True),
                  fromfile='before/lean/Statement.lean', tofile='after/lean/Statement.lean')))
    scan = {}
    bad = re.compile(r'\b(sorry|admit|sorryAx|axiom|native_decide|unsafe|implemented_by|extern|elab|macro)\b')
    for mod in order:
        p = L / (mod.replace('.', '/') + '.lean')
        hits = [{'line': i, 'text': line} for i, line in enumerate(p.read_text().splitlines(), 1) if bad.search(line)]
        assert not hits, (mod, hits)
        scan[mod] = {'path': str(p), **ident(p), 'forbidden_token_hits': hits}
    save('local-closure.json', {'acyclic': True, 'graph': graph, 'topological_order': order, 'source_scan': scan,
         'note': 'Source scan corroborates direct compiles/axiom outputs; it is not a standalone proof check. Smoke #eval is a definition test only; Scaffold has an unprovided Target field.'})
    outputs = {}
    outputs['01-default-build'] = run('01-default-build', ['lake', 'build'])
    assert 'Statement.FourWork.Assembly' in outputs['01-default-build'], 'Assembly missing from default build diagnostics'
    outputs['02-assembly-build'] = run('02-assembly-build', ['lake', 'build', 'Statement.FourWork.Assembly'])
    outputs['03-assembly-direct'] = run('03-assembly-direct', ['lake', 'env', 'lean', 'Statement/FourWork/Assembly.lean'])
    outputs['04-assembly-trust0'] = run('04-assembly-trust0', ['lake', 'env', 'lean', '-t0', 'Statement/FourWork/Assembly.lean'])
    for i, mod in enumerate(order):
        if mod == 'Statement.FourWork.Assembly':
            continue
        tag = '05-trust0-' + f'{i:02d}-' + mod.replace('.', '-')
        outputs[tag] = run(tag, ['lake', 'env', 'lean', '-t0', mod.replace('.', '/') + '.lean'])
        assert_frozen(begin, True)
    queries = sorted(set(q for mod in order for q in re.findall(r'^#print axioms\s+(\S+)',
                      (L / (mod.replace('.', '/') + '.lean')).read_text(), re.M)))
    assert all(row['name'] in queries for row in rows)
    source = 'import Statement\nset_option autoImplicit false\n'
    source += '\n'.join('#check @' + row['name'] for row in rows) + '\n'
    source += '''#check (ArithmeticStatement.representation_multiple_four :
  ∀ m : ℕ, 0 < m → ∃ a b : ℕ,
    0 < a ∧ 0 < b ∧ 4 * m = a + b ∧
    (-1 : ℤ) ^ a.primeFactorsList.length = (-1 : ℤ) ∧
    (-1 : ℤ) ^ b.primeFactorsList.length = (-1 : ℤ))
#print ArithmeticStatement.omega
#print ArithmeticStatement.lambda
#print ArithmeticStatement.HasSignedRepresentation
#print ArithmeticStatement.HasRepresentation
#print ArithmeticStatement.FourWork.residueLambda
#print ArithmeticStatement.FourWork.GoodMultiplier
#print ArithmeticStatement.Target
#print ArithmeticStatement.UnfinishedScaffold
'''
    source += '\n'.join('#print axioms ' + q for q in queries) + '\n'
    outputs['06-root-import'] = run('06-root-import', ['lake', 'env', 'lean', '-t0', '--stdin'], stdin=source)
    root_axioms = axiom_map(outputs['06-root-import'])
    assert set(root_axioms) == set(queries), set(queries) - set(root_axioms)
    for endpoint in ['ArithmeticStatement.representation_four_prime_three_mod_four', 'ArithmeticStatement.representation_multiple_four']:
        assert set(root_axioms[endpoint]) == BASE
    all_axioms = {}
    diagnostics = {}
    for tag, stream in outputs.items():
        assert not re.search(r'\b(sorryAx|sorry|admit|native_decide)\b', stream), tag
        parsed = axiom_map(stream)
        all_axioms.update(parsed)
        diagnostics[tag] = {'axiom_count': len(parsed), 'warnings': [s for s in stream.splitlines() if 'warning:' in s]}
    absence = run('07-original-endpoints-absent', ['lake', 'env', 'lean', '-t0', '--stdin'],
                  stdin='import Statement\n#check ArithmeticStatement.pointwise_keystone\n#check ArithmeticStatement.liouville_goldbach\n', expected=1)
    assert absence.count('Unknown identifier') == 2, absence
    assert 'ArithmeticStatement.pointwise_keystone' in absence and 'ArithmeticStatement.liouville_goldbach' in absence
    packages('post')
    assert_frozen(begin, True)
    save('snapshot-after.json', {p: ident(p) for p in begin})
    save('olean-identities.json', {mod: ident(L / '.lake/build/lib/lean' / (mod.replace('.', '/') + '.olean')) for mod in order})
    save('audit-v1.json', {'status': 'PASS', 'utc': utc(), 'candidate': {'path': str(A), **ident(A)},
        'root_before': ROOT_OLD, 'root_after': ident(ROOT)['sha256'], 'root_only_change': True,
        'exact_signature_comparisons': 38, 'exact_definition_comparisons': 6,
        'root_axiom_queries': len(queries), 'root_axioms': root_axioms,
        'all_printed_axioms': all_axioms, 'diagnostics': diagnostics,
        'axiom_union': sorted(set(a for xs in all_axioms.values() for a in xs)),
        'admissions': [], 'frozen_file_count': len(begin), 'concurrent_edits_detected': [],
        'new_full_theorem_count': 19, 'earlier_wave_theorem_count': 19,
        'original_all_even_target': 'Not proved; original endpoints absent',
        'remaining_review_obligations': ['Independent integrated-version NL reviews and final regulator are leader-owned'],
        'trust_boundary': 'Installed Lean/Lake compiler, kernel, elaborator/tactic implementations and pinned imported library .olean/build artifacts; no cold bootstrap or complete from-source upstream rebuild. Every local closure file re-elaborated at trust level zero. Standard axioms propext, Classical.choice, Quot.sound only.'})
    print('PASS root', ident(ROOT)['sha256'], 'axiom queries', len(queries), flush=True)


if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in ('preflight', 'integrated')
    if sys.argv[1] == 'preflight':
        preflight()
    else:
        integrated()
