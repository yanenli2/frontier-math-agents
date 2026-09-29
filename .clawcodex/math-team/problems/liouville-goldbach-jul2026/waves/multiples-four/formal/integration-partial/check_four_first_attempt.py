#!/usr/bin/env python3
"""Read-only master audit; writes only this wave's mechanical evidence."""
from pathlib import Path
import datetime, difflib, hashlib, json, re, shlex, subprocess, sys, time
D = Path(__file__).resolve().parent
W = D.parent.parent
P = W.parent.parent
L = P / 'lean'
B = P.parent.parent / 'review-inputs/r20260924-four-v1'
C = W / 'formal/generator/FourCandidate.lean'
M = L / 'Statement/FourPartial.lean'
ROOT = L / 'Statement.lean'
GATE = W / 'formal/reviews/four-candidate-review-v1.compile.json'
ALLOW = {'propext', 'Classical.choice', 'Quot.sound'}

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def h(s): return hashlib.sha256(s.encode()).hexdigest()
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def write_json(p, v):
    with Path(p).open('x') as f: json.dump(v, f, indent=2, ensure_ascii=False); f.write('\n')
def gate():
    assert sha(GATE) == '7b380889526d86a557ba3c389c4f97a3a6f40392349340d7ef5cdcc23e0a79f5'
    return json.loads(GATE.read_text())
def inputs():
    expected = gate()['input_hashes_before'].copy()
    expected.pop(str(ROOT))
    assert all(sha(p) == s for p, s in expected.items()), 'Protected gate input drift'
    extra = [GATE, W/'formal/reviews/four-candidate-review-v1.md',
             W/'formal/reviews/four-candidate-review-v1.compile.log',
             W/'formal/reviews/helper-fidelity-v1.md', W/'nl/reviews/partial-review-v1.md',
             W/'nl/generator/proof-attempt-v1.md', P/'formal/approved-v1/Definitions.lean',
             W/'formal/generator/four-cache-sum-two-squares-v1.json',
             P/'REPRODUCE.md', P/'FINAL_ARGUMENT.md', P/'sources.md',
             P/'formal/environment/public-availability-witnesses.json']
    extra += [p for p in (P/'formal/integration').iterdir() if p.is_file()]
    expected.update({str(p): sha(p) for p in extra})
    return expected

def declarations(path):
    text = Path(path).read_text()
    matches = list(re.finditer(r'^theorem (\w+)\b|^end ArithmeticStatement\s*$', text, re.M))
    out = {}
    for i, m in enumerate(matches):
        if not m.group(1): continue
        body = text[m.start():matches[i+1].start()].rstrip()
        header = body.split(':=', 1)[0].rstrip()
        out[m.group(1)] = {'header': header, 'header_sha256': h(header), 'declaration_sha256': h(body),
                          'line': text.count('\n', 0, m.start()) + 1}
    return out

def compare(path):
    actual = declarations(path)
    approved = declarations(W/'formal/generator/four-interfaces-v1.lean')
    assert len(actual) == 19 and actual.keys() == approved.keys()
    for n, a in actual.items():
        assert a['header'] == approved[n]['header'], n
        a.update(approved_line=approved[n]['line'], exact_header_match=True)
    normalized = '\n'.join(' '.join(a['header'].split()) for a in actual.values()) + '\n'
    assert h(normalized) == '20d393bd6cd7e9528ec555c41c00bf610ede2a731d97668bdb81f4cc2d63590c'
    return actual

def preflight():
    assert not M.exists(), 'Master exists: stop rather than overwrite'
    assert sha(C) == '4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325'
    assert sha(ROOT) == '426a0b62a141387e22f0e5481a705e3ffe3d64e0f8ad100daea3101c802e8458'
    assert (L/'Statement/Definitions.lean').read_bytes() == (P/'formal/approved-v1/Definitions.lean').read_bytes()
    assert (B/'Interfaces.lean').read_bytes() == (W/'formal/generator/four-interfaces-v1.lean').read_bytes()
    neutral = (B/'Declaration.lean').read_text().splitlines(True)
    base = (L/'Statement/Definitions.lean').read_text().splitlines(True)
    partial = (L/'Statement/Partial.lean').read_text().splitlines(True)
    assert neutral[4:7] == base[5:8] and neutral[8:15] == partial[13:20]
    report = {'mode': 'CERTIFICATION partial-only mechanical preflight', 'utc': now(),
              'inputs': inputs(), 'root_before': ROOT.read_text(), 'root_before_sha256': sha(ROOT),
              'master_before': 'absent', 'comparisons': compare(C)}
    with (D/'Statement.before.lean').open('xb') as f: f.write(ROOT.read_bytes())
    write_json(D/'preflight-v1.json', report)
    print('Preflight PASS: exact candidate, 19 exact headers, fixed definitions/readback and preserved prior master.')

def axiom_map(text, expected):
    out = {}
    for line in text.splitlines():
        m = re.match(r"^'(.*)' depends on axioms: \[(.*)\]$", line)
        n = re.match(r"^'(.*)' does not depend on any axioms$", line)
        if m: out[m[1]] = [x.strip() for x in m[2].split(',') if x.strip()]
        elif n: out[n[1]] = []
    assert set(out) == set(expected), (set(expected)-set(out), set(out)-set(expected))
    for name, axioms in out.items():
        assert set(axioms) <= ALLOW, (name, axioms)
        if name.startswith('ArithmeticStatement.'): assert set(axioms) == ALLOW
    return out

def verify():
    baseline = json.loads((D/'preflight-v1.json').read_text())
    result = {'mode': 'CERTIFICATION integrated 19-helper baseline only', 'started_utc': now(), 'commands': []}
    def run(tag, argv, stdin=None, expected=0):
        t, utc = time.monotonic(), now()
        cp = subprocess.run(argv, cwd=L, input=stdin, text=True, capture_output=True, timeout=600)
        stem = D/f'v1-{tag}'
        stem.with_suffix('.stdout').write_text(cp.stdout)
        stem.with_suffix('.stderr').write_text(cp.stderr)
        rec = {'argv': argv, 'shell_display': shlex.join(argv), 'cwd': str(L), 'started_utc': utc,
               'elapsed_seconds': round(time.monotonic()-t, 3), 'exit_status': cp.returncode,
               'expected_exit_status': expected, 'timeout_seconds': 600,
               'stdout_path': str(stem.with_suffix('.stdout')), 'stderr_path': str(stem.with_suffix('.stderr')),
               'stdout_sha256': h(cp.stdout), 'stderr_sha256': h(cp.stderr)}
        if stdin is not None:
            stem.with_suffix('.stdin.lean').write_text(stdin)
            rec.update(stdin_path=str(stem.with_suffix('.stdin.lean')), stdin_sha256=h(stdin))
        write_json(stem.with_suffix('.json'), rec)
        result['commands'].append(rec)
        print(f'{tag}: exit {cp.returncode}, expected {expected}, {rec["elapsed_seconds"]}s', flush=True)
        assert cp.returncode == expected, tag
        return cp.stdout
    try:
        result['inputs_before'] = inputs()
        assert result['inputs_before'] == baseline['inputs'], 'Concurrent input change'
        assert M.read_bytes() == C.read_bytes()
        assert ROOT.read_text() == baseline['root_before'] + 'import Statement.FourPartial\n'
        result.update(master_sha256=sha(M), root_sha256=sha(ROOT), comparisons=compare(M))
        diff = ''.join(difflib.unified_diff([], M.read_text().splitlines(True), fromfile='/dev/null', tofile='lean/Statement/FourPartial.lean'))
        diff += ''.join(difflib.unified_diff(baseline['root_before'].splitlines(True), ROOT.read_text().splitlines(True), fromfile='lean/Statement.lean.before', tofile='lean/Statement.lean'))
        (D/'integration-v1.diff').write_text(diff)
        pattern = r'\b(sorry|admit|sorryAx|native_decide|implemented_by|unsafe|axiom)\b|Lean\.ofReduceBool|^opaque\b'
        for p in [M, L/'Statement/Partial.lean', L/'Statement/Definitions.lean']:
            assert not re.search(pattern, p.read_text(), re.M), p
        result['local_source_scan'] = {'pattern': pattern, 'matches': []}
        result['lean_version'] = run('00-lean-version', ['lake','env','lean','--version'])
        assert 'f3b06c705e6c85f5314019d5d3baab0fec5b580c' in result['lean_version']
        result['lake_version'] = run('01-lake-version', ['lake','--version'])
        lean_path = run('02-lean-path', ['lake','env','printenv','LEAN_PATH']).strip().split(':')
        witnesses = {w['name']: w for w in json.loads((P/'formal/environment/public-availability-witnesses.json').read_text())}
        packages = json.loads((L/'lake-manifest.json').read_text())['packages']
        result['package_provenance'] = []
        for package in packages:
            name, rev = package['name'], package['rev']
            repo = L/'.lake/packages'/name
            actual = run(f'{name}-head', ['git','-C',str(repo),'rev-parse','HEAD']).strip()
            status = run(f'{name}-status', ['git','-C',str(repo),'status','--porcelain=v1','--untracked-files=no'])
            assert actual == rev and status == ''
            record = witnesses[name]
            assert record['sha'] == rev and record['exit_status'] == 0
            eligible = [w for w in record['witnesses'] if w['head_sha'] == rev and w['created_at'] < '2026-08-01T00:00:00Z' and w['updated_at'] < '2026-08-01T00:00:00Z']
            assert eligible
            raw_path = P/f'formal/environment/public-ci-{name}.stdout'
            raw_runs = {w['id']:w for w in json.loads(raw_path.read_text())['workflow_runs']}
            w = eligible[0]
            assert raw_runs[w['id']]['head_sha'] == rev and raw_runs[w['id']]['repository']['private'] is False
            result['package_provenance'].append(dict(package, witness=w, raw_witness_sha256=sha(raw_path), tracked_sources_clean=True))
        result['lean_public_availability'] = witnesses['lean']
        mathlib = L/'.lake/packages/mathlib'
        pin = '905b95818eb32af7874a58b427f50c1711a5e96c'
        result['new_source_provenance'] = []
        for relative in ['Mathlib/NumberTheory/SumTwoSquares.lean','Mathlib/NumberTheory/Zsqrtd/GaussianInt.lean','Mathlib/NumberTheory/Zsqrtd/QuadraticReciprocity.lean']:
            tag = Path(relative).stem
            blob = run(f'{tag}-pin-blob', ['git','-C',str(mathlib),'rev-parse',f'{pin}:{relative}']).strip()
            actual = run(f'{tag}-actual-blob', ['git','-C',str(mathlib),'hash-object',relative]).strip()
            assert blob == actual
            result['new_source_provenance'].append({'path':relative,'git_blob':blob,'sha256':sha(mathlib/relative),
                'url':f'https://github.com/leanprover-community/mathlib4/blob/{pin}/{relative}'})
        cache = json.loads((W/'formal/generator/four-cache-sum-two-squares-v1.json').read_text())
        assert cache['exit_status'] == 0 and cache['mathlib_head'] == pin
        assert sha(W/'formal/generator/four-cache-sum-two-squares-v1.stdout') == cache['stdout_sha256']
        assert sha(W/'formal/generator/four-cache-sum-two-squares-v1.stderr') == cache['stderr_sha256']
        result['new_cache_record'] = cache
        run('03-default-build', ['lake','build'])
        run('04-fourpartial-build', ['lake','build','Statement.FourPartial'])
        direct = run('05-fourpartial-direct', ['lake','env','lean','Statement/FourPartial.lean'])
        trust = run('06-fourpartial-trust-zero', ['lake','env','lean','-t','0','Statement/FourPartial.lean'])
        expected = re.findall(r'^#print axioms (\S+)$', M.read_text(), re.M)
        assert len(expected) == len(set(expected)) == 48
        result['axioms_direct'] = axiom_map(direct, expected)
        result['axioms_trust_zero'] = axiom_map(trust, expected)
        assert result['axioms_direct'] == result['axioms_trust_zero']
        assert not any(x in (direct+trust).lower() for x in ['sorry','error:','warning:'])
        old_expected = re.findall(r'^#print axioms (\S+)$', (L/'Statement/Partial.lean').read_text(), re.M)
        all_axioms = list(dict.fromkeys(expected + old_expected))
        diagnostic = 'import Statement\n' + ''.join(f'#check @ArithmeticStatement.{n}\n' for n in result['comparisons'])
        diagnostic += ''.join(f'#print ArithmeticStatement.{n}\n' for n in ['omega','lambda','HasSignedRepresentation','HasRepresentation','Target'])
        diagnostic += ''.join(f'#print axioms {n}\n' for n in all_axioms)
        root_out = run('07-root-import', ['lake','env','lean','--stdin'], stdin=diagnostic)
        result['axioms_root'] = axiom_map(root_out, all_axioms)
        assert all(result['axioms_root'][n] == result['axioms_direct'][n] for n in expected)
        old_axioms = json.loads((P/'formal/integration/audit-v1.json').read_text())['axioms_direct']
        assert all(result['axioms_root'][n] == old_axioms[n] for n in old_expected)
        missing = ['representation_multiple_four','pointwise_keystone','liouville_goldbach']
        missing_in = 'import Statement\n' + ''.join(f'#check ArithmeticStatement.{n}\n' for n in missing)
        missing_out = run('08-absent-endpoints', ['lake','env','lean','--stdin'], stdin=missing_in, expected=1)
        assert missing_out.lower().count('unknown identifier') == 3
        assert all(f'ArithmeticStatement.{n}' in missing_out for n in missing)
        result['absent_endpoints'] = missing
        result['import_resolution'] = []
        for module in ['Statement','Statement.FourPartial','Statement.Partial','Statement.Definitions','Mathlib.NumberTheory.SumTwoSquares']:
            rel = Path(*module.split('.')).with_suffix('.olean')
            found = [Path(p)/rel for p in lean_path if (Path(p)/rel).is_file()]
            assert found
            result['import_resolution'].append({'module':module,'resolved_olean':str(found[0]),'sha256':sha(found[0])})
        result['inputs_after'] = inputs()
        assert result['inputs_after'] == result['inputs_before'], 'Concurrent protected-input change'
        assert sha(M) == result['master_sha256'] and sha(ROOT) == result['root_sha256']
        result['status'] = 'PASS: exact 19-helper baseline integrated; full T4 and original Target not proved here'
    except Exception as e:
        result.update(status='FAIL: preserve prior accepted master; no mathematical repair', error=repr(e))
        raise
    finally:
        result['finished_utc'] = now()
        write_json(D/'audit-v1.json', result)
        print(result['status'])

if __name__ == '__main__':
    if sys.argv[1:] == ['preflight']: preflight()
    elif sys.argv[1:] == ['verify']: verify()
    else: raise SystemExit('Usage: check_four.py preflight|verify; run each once to preserve evidence')
