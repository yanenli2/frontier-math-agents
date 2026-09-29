from pathlib import Path
import hashlib
import json
import shlex
import subprocess

ROOT = Path(__file__).resolve().parents[8]
P = ROOT / '.clawcodex/math-team/problems/liouville-goldbach-jul2026'
LEAN = P / 'lean'
OUT = P / 'waves/multiples-four/formal/formalizer'
NEUTRAL = ROOT / '.clawcodex/math-team/review-inputs/r20260924-four-v1'
PRIOR = ROOT / '.clawcodex/math-team/review-inputs/r20260924-v1'

EXPECTED = {
    LEAN / 'Statement/Definitions.lean': '79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d',
    LEAN / 'Statement/Partial.lean': '9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0',
    LEAN / 'lean-toolchain': '2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273',
    LEAN / 'lakefile.toml': '0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4',
    LEAN / 'lake-manifest.json': 'de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03',
}
source_records = json.loads((P / 'formal/environment/source-file-identities.json').read_text())
for source in source_records:
    EXPECTED[Path(source['local_path'])] = source['sha256']

protected = list(EXPECTED) + [
    LEAN / '.lake/build/lib/lean/Statement/Definitions.olean',
    LEAN / '.lake/build/lib/lean/Statement/Definitions.trace',
    LEAN / '.lake/build/lib/lean/Statement/Partial.olean',
    LEAN / '.lake/build/lib/lean/Statement/Partial.trace',
    PRIOR / 'Declaration.lean',
    PRIOR / 'Dependencies.lean',
    PRIOR / 'ListOperations.lean',
]

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def snapshot(paths):
    return {str(path): sha256(path) for path in paths}

record = {'scope': 'Statement/interface elaboration only; no theorem proof or old-proof rebuild.',
          'commands': []}

def run(argv, label, cwd=LEAN):
    result = subprocess.run(argv, cwd=cwd, text=True, capture_output=True, check=False)
    entry = {'command': shlex.join([str(arg) for arg in argv]), 'cwd': str(cwd),
             'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
    record['commands'].append(entry)
    if label in ('Interface', 'Check'):
        (OUT / (label + '.stdout')).write_text(result.stdout)
        (OUT / (label + '.stderr')).write_text(result.stderr)
    return result

record['protected_before'] = snapshot(protected)
record['expected_hashes_match'] = all(sha256(path) == digest for path, digest in EXPECTED.items())
assert record['expected_hashes_match'], 'Frozen source/config hash mismatch'

original_defs = (LEAN / 'Statement/Definitions.lean').read_text().splitlines(keepends=True)
original_partial = (LEAN / 'Statement/Partial.lean').read_text().splitlines(keepends=True)
neutral = (NEUTRAL / 'Declaration.lean').read_text()
expected_declaration = (
    'import Mathlib.Data.Nat.Factors\n\nnamespace ArithmeticStatement\n\n'
    + ''.join(original_defs[5:8]) + '\n'
    + ''.join(original_partial[13:20]) + '\n'
    + 'theorem representation_multiple_four (m : ℕ) (hm : 0 < m) :\n'
    + '  HasRepresentation (4 * m)\n\nend ArithmeticStatement\n'
)
record['neutral_exact_custom_definitions_and_signature'] = neutral == expected_declaration
prior_dependencies = (PRIOR / 'Dependencies.lean').read_text().splitlines(keepends=True)
record['factor_supplement_exact_prior_lines_5_53'] = (
    (NEUTRAL / 'Dependencies.lean').read_text() == ''.join(prior_dependencies[4:53]))
record['list_supplement_exact_prior_copy'] = (
    (NEUTRAL / 'ListOperations.lean').read_bytes() == (PRIOR / 'ListOperations.lean').read_bytes())
assert record['neutral_exact_custom_definitions_and_signature']
assert record['factor_supplement_exact_prior_lines_5_53']
assert record['list_supplement_exact_prior_copy']

manifest = json.loads((LEAN / 'lake-manifest.json').read_text())
record['packages'] = []
for package in manifest['packages']:
    checkout = LEAN / '.lake/packages' / package['name']
    head = run(['git', 'rev-parse', 'HEAD'], package['name'] + '-head', cwd=checkout)
    status = run(['git', 'status', '--porcelain=v1', '--untracked-files=no'],
                 package['name'] + '-status', cwd=checkout)
    record['packages'].append({
        'name': package['name'], 'manifest_revision': package['rev'],
        'head': head.stdout.strip(),
        'matches_manifest': head.returncode == 0 and head.stdout.strip() == package['rev'],
        'tracked_checkout_clean': status.returncode == 0 and status.stdout == '',
    })
assert all(pkg['matches_manifest'] and pkg['tracked_checkout_clean'] for pkg in record['packages'])

version = run(['lake', 'env', 'lean', '--version'], 'version')
assert version.returncode == 0
assert 'version 4.32.2' in version.stdout
assert 'f3b06c705e6c85f5314019d5d3baab0fec5b580c' in version.stdout
run(['lean', '--print-prefix'], 'prefix')
run(['lake', 'env', 'lean', str(OUT / 'Interface.lean')], 'Interface')
run(['lake', 'env', 'lean', str(OUT / 'Check.lean')], 'Check')

record['protected_after'] = snapshot(protected)
record['protected_unchanged'] = record['protected_before'] == record['protected_after']
record['all_commands_exit_zero'] = all(cmd['exit'] == 0 for cmd in record['commands'])
record['artifacts_sha256'] = snapshot([
    NEUTRAL / 'Declaration.lean', NEUTRAL / 'Dependencies.lean', NEUTRAL / 'ListOperations.lean',
    OUT / 'Interface.lean', OUT / 'Check.lean', OUT / 'run-check.py',
    OUT / 'Interface.stdout', OUT / 'Interface.stderr', OUT / 'Check.stdout', OUT / 'Check.stderr',
    P / 'request.md', P / 'waves/multiples-four/request.md',
    P / 'sources.md', P / 'formal/environment/source-file-identities.json',
])
(OUT / 'check-record.json').write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({
    'all_commands_exit_zero': record['all_commands_exit_zero'],
    'protected_unchanged': record['protected_unchanged'],
    'record': str(OUT / 'check-record.json'),
}, indent=2))
assert record['all_commands_exit_zero']
assert record['protected_unchanged']
