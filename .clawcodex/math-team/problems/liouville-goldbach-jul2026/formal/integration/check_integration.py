#!/usr/bin/env python3
"""Mechanical evidence only. Does not edit Lean source, pins, or accepted snapshots."""
import datetime as dt
import difflib
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys
import time

D = Path(__file__).resolve().parent
P = D.parent.parent
L = P / 'lean'
Q = P.parent.parent / 'review-inputs/r20260924-v1'
CANDIDATE = P / 'formal/generator/Candidate.lean'
MASTER = L / 'Statement/Partial.lean'
EXPECTED = {
    CANDIDATE: '9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0',
    P / 'formal/approved-v1/Definitions.lean': '79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d',
    L / 'Statement/Definitions.lean': '79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d',
    P / 'formal/blueprinter/interfaces-v1.lean': '89080f705ec6f0ba690edbc4e7d3d97cea18a6f3d3c3cdcb31e30abefbb434bc',
    Q / 'Declaration.lean': '79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d',
    Q / 'Interfaces.lean': '89080f705ec6f0ba690edbc4e7d3d97cea18a6f3d3c3cdcb31e30abefbb434bc',
    Q / 'readback.md': 'dbe6c1e5ff159fd8f2f5e21e0c95981829ebb6e6133598a94597975d8b563ca6',
    Q / 'interfaces-readback.md': '88a3bb1152043c2eb245914cbec5a569cbf81ab47e4031f1330e1ba27d139e9e',
    L / 'lake-manifest.json': 'de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03',
    P / 'formal/reviews/candidate-audit-v1.json': 'cf36dd42c567308de978da49921092b994d95cc31184d12e6aeb9896b4e437ec',
    P / 'formal/reviews/candidate-audit-v1.log': 'f9be352c079cf3addf5b43988f35c59650fef2e84dd38988576bdb6274ea9523',
}
EXTRA_INPUTS = [
    P / 'request.md', L / 'lean-toolchain', L / 'lakefile.toml',
    L / 'Statement/Scaffold.lean', L / 'Statement/Smoke.lean',
    P / 'formal/reviews/candidate-audit-v1.md',
    P / 'nl/reviews/partial-proof-review-v1.md',
    P / 'nl/generator/proof-v1.md', P / 'nl/generator/proof-v2.md',
    P / 'formal/environment/public-availability-witnesses.json',
    P / 'formal/environment/source-file-identities.json',
    P / 'formal/environment/cache-factors.json',
    P / 'formal/environment/fl-generator-cache-required-v1.json',
]
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
OPEN = {'pointwise_keystone', 'liouville_goldbach'}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def sha(path):
    return digest(path.read_bytes())

def save(path, data):
    with path.open('x') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')

def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def inputs():
    actual = {str(p): sha(p) for p in [*EXPECTED, *EXTRA_INPUTS]}
    for p, expected in EXPECTED.items():
        assert actual[str(p)] == expected, f'Protected/review identity changed: {p}'
    return actual

def declarations(path):
    text = path.read_text()
    markers = list(re.finditer(r'^(def|theorem) ([A-Za-z_][A-Za-z_0-9]*)\b|^end ArithmeticStatement\s*$', text, re.M))
    result = {}
    for i, m in enumerate(markers):
        kind, name = m.group(1), m.group(2)
        if kind is None:
            continue
        end = markers[i + 1].start() if i + 1 < len(markers) else len(text)
        body = text[m.start():end].rstrip()
        comparison = body.split(':=', 1)[0].rstrip() if kind == 'theorem' else body
        result[name] = {'kind': kind, 'line': text.count('\n', 0, m.start()) + 1,
                        'comparison': comparison, 'comparison_sha256': digest(comparison.encode()),
                        'declaration_sha256': digest(body.encode())}
    return result

def compare(path):
    actual = declarations(path)
    approved = declarations(P / 'formal/blueprinter/interfaces-v1.lean')
    assert len(actual) == 50
    assert sum(x['kind'] == 'theorem' for x in actual.values()) == 42
    assert set(approved) - set(actual) == OPEN
    assert not (set(actual) - set(approved))
    for name, item in actual.items():
        assert item['comparison'] == approved[name]['comparison'], f'Statement/definition drift: {name}'
        item['approved_line'] = approved[name]['line']
        item['exact_comparison_passed'] = True
    return actual

def parse_axioms(text, expected):
    result = {}
    for line in text.splitlines():
        m = re.match(r"^'(.*)' depends on axioms: \[(.*)\]$", line)
        n = re.match(r"^'(.*)' does not depend on any axioms$", line)
        if m:
            result[m.group(1)] = [x.strip() for x in m.group(2).split(',') if x.strip()]
        elif n:
            result[n.group(1)] = []
    assert set(result) == set(expected), (set(expected) - set(result), set(result) - set(expected))
    for name, axioms in result.items():
        assert set(axioms) <= ALLOWED_AXIOMS, (name, axioms)
        if name.startswith('ArithmeticStatement.'):
            assert set(axioms) == ALLOWED_AXIOMS, (name, axioms)
    return result

def preflight():
    assert not MASTER.exists(), 'Existing master: stop, do not overwrite'
    root = L / 'Statement.lean'
    expected_root = b'import Statement.Definitions\nimport Statement.Scaffold\nimport Statement.Smoke\n'
    assert root.read_bytes() == expected_root, 'Concurrent/unexpected root edit'
    report = {'mode': 'CERTIFICATION mechanical integration', 'utc': utc(),
              'input_hashes': inputs(), 'root_before_sha256': sha(root),
              'root_before_text': root.read_text(), 'partial_before': 'absent',
              'candidate_comparisons': compare(CANDIDATE)}
    gate = json.loads((P / 'formal/reviews/candidate-audit-v1.json').read_text())
    candidate_commands = [c for c in gate['commands'] if str(CANDIDATE) in c['argv']]
    assert len(candidate_commands) >= 2 and all(c['exit_status'] == 0 for c in candidate_commands)
    report['exact_candidate_gate_commands'] = candidate_commands
    save(D / 'preflight-v1.json', report)
    with (D / 'Statement.before.lean').open('xb') as f:
        f.write(expected_root)
    print('Preflight PASS: exact candidate, protected snapshots/readbacks, 50 declaration comparisons; master absent.')


def verify(label):
    assert re.fullmatch(r'[a-zA-Z0-9_-]+', label)
    assert not (D / f'audit-{label}.json').exists(), 'Use a fresh evidence label; do not overwrite prior audit'
    baseline = json.loads((D / 'preflight-v1.json').read_text())
    report = {'mode': 'CERTIFICATION mechanical partial integration only', 'utc_start': utc(),
              'commands': [], 'status': 'RUNNING', 'label': label}

    def run(tag, argv, stdin=None, expected=0, timeout=300):
        stem = D / f'{label}-{tag}'
        assert not stem.with_suffix('.json').exists(), f'Existing evidence: {stem}'
        start = time.monotonic()
        started = utc()
        proc = subprocess.run(argv, cwd=L, input=stdin, text=True, capture_output=True, timeout=timeout)
        stem.with_suffix('.stdout').write_text(proc.stdout)
        stem.with_suffix('.stderr').write_text(proc.stderr)
        record = {'argv': argv, 'shell_display': shlex.join(argv), 'cwd': str(L),
                  'started_utc': started, 'elapsed_seconds': round(time.monotonic() - start, 3),
                  'exit_status': proc.returncode, 'expected_exit_status': expected,
                  'timeout_seconds': timeout, 'stdout_path': str(stem.with_suffix('.stdout')),
                  'stderr_path': str(stem.with_suffix('.stderr')),
                  'stdout_sha256': digest(proc.stdout.encode()), 'stderr_sha256': digest(proc.stderr.encode())}
        if stdin is not None:
            stem.with_suffix('.stdin.lean').write_text(stdin)
            record.update(stdin_path=str(stem.with_suffix('.stdin.lean')), stdin_sha256=digest(stdin.encode()))
        save(stem.with_suffix('.json'), record)
        report['commands'].append(record)
        print(f'{tag}: exit {proc.returncode} (expected {expected}), {record["elapsed_seconds"]}s', flush=True)
        assert proc.returncode == expected, f'Command failed: {record["shell_display"]}; see {stem}'
        return proc.stdout

    try:
        report['input_hashes_before'] = inputs()
        assert report['input_hashes_before'] == baseline['input_hashes'], 'Input changed after preflight'
        assert MASTER.read_bytes() == CANDIDATE.read_bytes(), 'Master is not exact accepted candidate'
        expected_root = baseline['root_before_text'] + 'import Statement.Partial\n'
        assert (L / 'Statement.lean').read_text() == expected_root, 'Concurrent/unexpected root edit'
        report['integrated_sha256'] = sha(MASTER)
        report['root_sha256'] = sha(L / 'Statement.lean')
        report['declaration_comparisons'] = compare(MASTER)
        new_diff = ''.join(difflib.unified_diff([], MASTER.read_text().splitlines(True),
                           fromfile='/dev/null', tofile='lean/Statement/Partial.lean'))
        root_diff = ''.join(difflib.unified_diff(baseline['root_before_text'].splitlines(True),
                            expected_root.splitlines(True), fromfile='lean/Statement.lean.before',
                            tofile='lean/Statement.lean'))
        (D / f'integration-{label}.diff').write_text(new_diff + root_diff)
        # Source scan is supplementary: the transitive axiom checks below are decisive.
        prohibited = r'\b(sorry|admit|sorryAx|native_decide|implemented_by|unsafe|axiom)\b|Lean\.ofReduceBool|^opaque\b'
        accepted_sources = [MASTER, L / 'Statement/Definitions.lean']
        for p in accepted_sources:
            assert not re.search(prohibited, p.read_text(), re.M), f'Prohibited token in {p}'
        report['source_scan'] = {'paths': [str(p) for p in accepted_sources], 'pattern': prohibited,
                                 'matches': [], 'scope': 'accepted local proof closure'}
        expected_axioms = re.findall(r'^#print axioms (\S+)$', MASTER.read_text(), re.M)
        assert len(expected_axioms) == len(set(expected_axioms)) == 82
        report['lean_version'] = run('00-lean-version', ['lake', 'env', 'lean', '--version'])
        assert 'f3b06c705e6c85f5314019d5d3baab0fec5b580c' in report['lean_version']
        report['lake_version'] = run('01-lake-version', ['lake', '--version'])
        prefix = Path(run('02-prefix', ['lake', 'env', 'lean', '--print-prefix']).strip())
        lean_path = run('03-lean-path', ['lake', 'env', 'printenv', 'LEAN_PATH']).strip().split(':')
        manifest = json.loads((L / 'lake-manifest.json').read_text())
        witnesses = {w['name']: w for w in json.loads((P / 'formal/environment/public-availability-witnesses.json').read_text())}
        cutoff = '2026-08-01T00:00:00Z'
        packages = []
        for package in manifest['packages']:
            name, rev = package['name'], package['rev']
            repo = L / '.lake/packages' / name
            actual = run(f'git-{name}-head', ['git', '-C', str(repo), 'rev-parse', 'HEAD']).strip()
            status = run(f'git-{name}-status', ['git', '-C', str(repo), 'status', '--porcelain=v1', '--untracked-files=no'])
            assert actual == rev and not status, f'Pin or tracked-source drift: {name}'
            witness = witnesses[name]
            assert witness['sha'] == rev and witness['exit_status'] == 0
            eligible = [w for w in witness['witnesses'] if w['head_sha'] == rev and w['created_at'] < cutoff and w['updated_at'] < cutoff]
            assert eligible, f'No exact-SHA pre-cutoff availability witness: {name}'
            raw_path = P / f'formal/environment/public-ci-{name}.stdout'
            raw = json.loads(raw_path.read_text())
            raw_runs = {w['id']: w for w in raw['workflow_runs']}
            w = eligible[0]
            assert raw_runs[w['id']]['head_sha'] == rev
            assert raw_runs[w['id']]['repository']['private'] is False
            assert raw_runs[w['id']]['created_at'] == w['created_at']
            packages.append({'name': name, 'revision': rev, 'tracked_sources_clean': True,
                             'url': package['url'], 'availability_witness': w, 'raw_sha256': sha(raw_path)})
        report['package_provenance'] = packages
        lean_witness = witnesses['lean']
        assert lean_witness['sha'] == 'f3b06c705e6c85f5314019d5d3baab0fec5b580c'
        assert all(w['created_at'] < cutoff and w['updated_at'] < cutoff for w in lean_witness['witnesses'])
        report['lean_public_availability'] = lean_witness
        report['cache_records'] = []
        for name in ['cache-factors', 'fl-generator-cache-required-v1']:
            record = json.loads((P / f'formal/environment/{name}.json').read_text())
            assert record['exit_status'] == 0
            for stream in ['stdout', 'stderr']:
                assert sha(Path(record[stream + '_path'])) == record[stream + '_sha256']
            report['cache_records'].append(record)
        source_identities = json.loads((P / 'formal/environment/source-file-identities.json').read_text())
        for source in source_identities:
            assert sha(Path(source['local_path'])) == source['sha256'], source['local_path']
        report['recorded_source_identities_rechecked'] = source_identities
        imports = re.findall(r'^import (\S+)', MASTER.read_text(), re.M)
        imports += re.findall(r'^import (\S+)', (L / 'Statement/Definitions.lean').read_text(), re.M)
        report['import_resolution'] = []
        for module in dict.fromkeys(imports):
            relative = Path(*module.split('.')).with_suffix('.olean')
            candidates = [Path(p) / relative for p in lean_path if (Path(p) / relative).exists()]
            assert candidates, module
            report['import_resolution'].append({'module': module, 'resolved_olean': str(candidates[0]), 'sha256': sha(candidates[0])})
        # No network/update/cache command is run in this integration.
        run('04-default-build', ['lake', 'build'], timeout=600)
        run('05-partial-build', ['lake', 'build', 'Statement.Partial'], timeout=600)
        direct = run('06-partial-direct', ['lake', 'env', 'lean', 'Statement/Partial.lean'])
        trust_zero = run('07-partial-trust-zero', ['lake', 'env', 'lean', '-t', '0', 'Statement/Partial.lean'])
        report['axioms_direct'] = parse_axioms(direct, expected_axioms)
        report['axioms_trust_zero'] = parse_axioms(trust_zero, expected_axioms)
        assert report['axioms_direct'] == report['axioms_trust_zero']
        for output in [direct, trust_zero]:
            assert 'sorry' not in output.lower() and 'error:' not in output.lower()
            assert output.count('warning:') == 4
        diagnostic = 'import Statement\n'
        for name in report['declaration_comparisons']:
            diagnostic += f'#check @ArithmeticStatement.{name}\n'
        for name in ['omega', 'lambda', 'Target'] + [n for n, d in report['declaration_comparisons'].items() if d['kind'] == 'def']:
            diagnostic += f'#print ArithmeticStatement.{name}\n'
        diagnostic += '\n'.join(f'#print axioms {name}' for name in expected_axioms) + '\n'
        root_out = run('08-root-import-check', ['lake', 'env', 'lean', '--stdin'], stdin=diagnostic)
        report['axioms_root_import'] = parse_axioms(root_out, expected_axioms)
        assert report['axioms_root_import'] == report['axioms_direct']
        missing = 'import Statement\n#check ArithmeticStatement.pointwise_keystone\n#check ArithmeticStatement.liouville_goldbach\n'
        missing_out = run('09-absent-endpoints', ['lake', 'env', 'lean', '--stdin'], stdin=missing, expected=1)
        assert missing_out.lower().count('unknown identifier') == 2, missing_out
        assert all(f'ArithmeticStatement.{n}' in missing_out for n in OPEN)
        report['absent_endpoints'] = sorted(OPEN)
        report['input_hashes_after'] = inputs()
        assert report['input_hashes_before'] == report['input_hashes_after'], 'Concurrent input edit during build'
        assert sha(MASTER) == report['integrated_sha256'] and sha(L / 'Statement.lean') == report['root_sha256']
        report['build_artifacts'] = {str(p): sha(p) for p in [L / '.lake/build/lib/lean/Statement.olean', L / '.lake/build/lib/lean/Statement/Partial.olean', L / '.lake/build/lib/lean/Statement/Definitions.olean']}
        report['status'] = 'PASS: exact approved partial artifact integrated; original Target unresolved'
    except Exception as exc:
        report['status'] = 'FAIL: preserve/restore prior accepted master; no mathematical repair authorized'
        report['error'] = repr(exc)
        raise
    finally:
        report['utc_finish'] = utc()
        save(D / f'audit-{label}.json', report)
        print(report['status'], flush=True)

if __name__ == '__main__':
    if sys.argv[1:] == ['preflight']:
        preflight()
    elif len(sys.argv) == 3 and sys.argv[1] == 'verify':
        verify(sys.argv[2])
    else:
        raise SystemExit('Usage: check_integration.py preflight | verify FRESH_LABEL')
