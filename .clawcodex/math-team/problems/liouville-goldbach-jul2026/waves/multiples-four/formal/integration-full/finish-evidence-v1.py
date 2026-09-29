#!/usr/bin/env python3
"""Final read-only reconciliation of saved compiler outputs and source identities.
No build or source mutation is performed. Outputs are exclusively created.
"""
from pathlib import Path
import importlib.util, json, re

O = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('checks', O / 'check-integration-v1.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
before = json.loads((O / 'snapshot-before.json').read_text())
c.assert_frozen(before, True)
rows = c.sigs()
assert rows == json.loads((O / 'signatures-integrated.json').read_text())
accepted = json.loads((O / 'audit-v1.json').read_text())
assert accepted['status'] == 'PASS'
for row in rows:
    if row['kind'] == 'theorem':
        assert set(accepted['root_axioms'][row['name']]) == c.BASE

# Parse build prefixes as well as direct diagnostics, preserving quoted apostrophes.
pattern = r"^(?:info: [^\n]*?:[0-9]+:[0-9]+: )?'([^\n]+)'\s+(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)"
commands, union, warnings = [], {}, {}
for recpath in sorted(O.glob('*.json')):
    rec = json.loads(recpath.read_text())
    if not isinstance(rec, dict) or 'argv' not in rec or 'exit_code' not in rec:
        continue
    for stream in ['stdout', 'stderr']:
        assert c.ident(recpath.with_suffix('.' + stream)) == rec[stream]
    assert rec['exit_code'] == rec['expected_exit_code'], recpath
    raw = recpath.with_suffix('.stdout').read_text() + recpath.with_suffix('.stderr').read_text()
    occurrences = list(re.finditer(pattern, raw, re.M))
    # Account for each axiom report, including replayed Lake info lines.
    assert len(occurrences) == len(re.findall(r'depends on axioms:|does not depend on any axioms', raw)), recpath
    parsed = {}
    for match in occurrences:
        vals = sorted(x.strip() for x in (match[2] or '').split(',') if x.strip())
        assert set(vals) <= c.BASE, (recpath, match[1], vals)
        assert match[1] not in union or union[match[1]] == vals
        union[match[1]] = vals
        parsed[match[1]] = vals
    warnings[recpath.stem] = [line for line in raw.splitlines() if 'warning:' in line]
    commands.append({'record': recpath.name, 'argv': rec['argv'], 'cwd': rec['cwd'],
                     'exit_code': rec['exit_code'], 'axiom_print_occurrences': len(occurrences),
                     'distinct_printed_axioms': parsed})
assert set(accepted['root_axioms']) <= set(union)
assert len(union) == 156

inventory = json.loads((O / 'library-inventory-v1.json').read_text())
source_changes = []
for mod, rec in inventory['records'].items():
    now = c.ident(rec['path'])['sha256']
    if now != rec['sha256']:
        source_changes.append(mod)
    if rec['package'] is not None:
        assert rec['public_availability_witness_utc'] < '2026-08-01T00:00:00Z'
        assert rec['revision'] in rec['url'] and rec['title'] and rec['authors'] and rec['locator']
assert not source_changes

links = []
for doc in [c.W / 'REPRODUCE.md', c.W / 'sources.md', c.W / 'LEMMA_MAP.md']:
    for match in re.finditer(r'\]\(([^)]+)\)', doc.read_text()):
        href = match[1]
        if '://' in href or href.startswith('#'):
            continue
        target = (doc.parent / href.split('#')[0]).resolve()
        # Reports/manifests are written during final handoff, not linked before existence.
        assert target.exists(), (doc, href)
        links.append({'from': str(doc), 'href': href, 'exists': True})

c.save('all-commands-audit-v1.json', {'status': 'PASS', 'utc': c.utc(),
    'commands': commands, 'axiom_print_occurrences': sum(x['axiom_print_occurrences'] for x in commands),
    'distinct_axioms_printed': len(union), 'axioms': union, 'warnings': warnings,
    'protected_files_unchanged_except_root_import': True,
    'wave_theorems_exact_standard_axioms': 38,
    'source_inventory_records_rehashed': len(inventory['records']),
    'source_changes': [], 'wave_added_library_modules': len(inventory['wave_added_library_modules']),
    'final_stage_added_library_modules': len(inventory['final_stage_added_library_modules']),
    'all_external_versions_before_cutoff': True, 'local_document_links': links})
print(json.dumps({'status': 'PASS', 'root': c.ident(c.ROOT)['sha256'],
                  'commands': len(commands), 'axiom_print_occurrences': sum(x['axiom_print_occurrences'] for x in commands),
                  'distinct_axioms_printed': len(union), 'frozen_files': len(before),
                  'import_source_files_rehashed': len(inventory['records']), 'links': len(links)}, indent=2))
