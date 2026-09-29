#!/usr/bin/env python3
"""Read-only source-import closure and exact-version provenance inventory.
The output separates the original baseline, FourPartial additions, and final
Assembly additions. No proof declaration or dependency pin is changed.
"""
from pathlib import Path
import hashlib, json, re

O = Path(__file__).resolve().parent
W = O.parents[1]
P = W.parents[1]
L = P / 'lean'
C = Path.home() / '.elan/toolchains/leanprover--lean4---v4.32.2/src/lean'
pins = json.loads((L / 'lake-manifest.json').read_text())['packages']
roots = [(L, None)] + [(L / '.lake/packages' / p['name'], p) for p in pins] + [(C, 'lean')]
witnesses = {x['name']: x for x in json.loads((P / 'formal/environment/public-availability-witnesses.json').read_text())}
seen, visiting, records = {}, set(), {}


def uncomment(s):
    # Retain newlines so import declaration/source line locators stay accurate.
    out = []
    i = 0
    depth = 0
    while i < len(s):
        if s[i:i+2] == '/-':
            depth += 1
            i += 2
        elif depth and s[i:i+2] == '-/':
            depth -= 1
            i += 2
        elif not depth and s[i:i+2] == '--':
            j = s.find('\n', i)
            i = len(s) if j < 0 else j
        else:
            out.append(s[i] if not depth or s[i] == '\n' else ' ')
            i += 1
    return ''.join(out)


def locate(m):
    for root, package in roots:
        p = root / (m.replace('.', '/') + '.lean')
        if p.exists():
            return p, root, package
    raise AssertionError(('unresolved source module', m))


def visit(m):
    if m in visiting:
        raise AssertionError(('cycle', m))
    if m in seen:
        return seen[m]
    visiting.add(m)
    p, root, package = locate(m)
    s = p.read_text()
    code = uncomment(s)
    imports = []
    for line in code.splitlines():
        line = line.strip()
        if not line or line in ('module', 'prelude'):
            continue
        match = re.fullmatch(r'(?:(?:public|private|meta)\s+)*import\s+(.+)', line)
        if match is None:
            break  # Lean module imports occur only in the initial header.
        tokens = match[1].strip().split()
        imports.extend(x for x in tokens if x != 'all')
    if not re.search(r'^prelude\s*$', code, re.M) and m != 'Init':
        imports.append('Init')
    closure = {m}
    for dependency in imports:
        closure |= visit(dependency)
    visiting.remove(m)
    seen[m] = closure
    authors = re.search(r'Authors?:\s*([^\n]+(?:\n(?!-\/|\s*$)[^\n]+)*)', s[:1500])
    title = re.search(r'^#\s+(.+)', s, re.M)
    title_text = title[1].strip() if title else m + ' (module identifier; no top-level title supplied)'
    author_text = authors[1].strip().replace('\n', ' ') if authors else (
        ('Lean developers' if package == 'lean' else (package['name'] + ' contributors'))
        + ' (no Authors header)' if package else 'local math-team development')
    if package is None:
        url, rev, date, witness = str(p), None, None, None
    else:
        name = 'lean' if package == 'lean' else package['name']
        rev = witnesses[name]['sha']
        selected = min([x for x in witnesses[name]['witnesses'] if x['head_sha'] == rev and x['created_at'] < '2026-08-01T00:00:00Z'], key=lambda x: x['created_at'])
        date, witness = selected['created_at'], selected['html_url']
        prefix = 'https://github.com/leanprover/lean4' if package == 'lean' else package['url']
        relative = ('src/' if package == 'lean' else '') + str(p.relative_to(root))
        url = prefix + '/blob/' + rev + '/' + relative
    records[m] = {'module': m, 'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                  'package': None if package is None else ('lean' if package == 'lean' else package['name']),
                  'title': title_text, 'authors': author_text, 'url': url, 'revision': rev,
                  'public_availability_witness_utc': date, 'witness_url': witness,
                  'locator': 'whole module, lines 1-' + str(len(s.splitlines())), 'imports': imports}
    return closure


original = set().union(*(visit(m) for m in ['Statement.Definitions', 'Statement.Scaffold', 'Statement.Smoke', 'Statement.Partial']))
partial = original | visit('Statement.FourPartial')
full = partial | visit('Statement.FourWork.Assembly')
new = sorted(m for m in full - original if records[m]['package'] is not None)
final = sorted(m for m in full - partial if records[m]['package'] is not None)
output = {'method': 'Static source import graph with comment removal and public/meta imports, plus implicit Init; exact installed pinned source tree. Import inventory is broader than theorem dependency closure.',
          'original_modules': sorted(original), 'partial_modules': sorted(partial), 'full_modules': sorted(full),
          'wave_added_library_modules': new, 'final_stage_added_library_modules': final,
          'records': records}
with (O / 'library-inventory-v1.json').open('x') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
    f.write('\n')
with (O / 'new-library-modules-v1.txt').open('x') as f:
    f.write('Complete wave-added library source inventory; static imported-source closure.\n')
    f.write('Baseline: original Definitions/Scaffold/Smoke/Partial before FourPartial.\n')
    f.write('Full: baseline + FourPartial + all six FourWork modules.\n')
    f.write('Every date is an exact-SHA public witness, not a first-publication claim.\n')
    f.write('All listed versions are before 2026-08-01; inherited baseline pins: ../../../../sources.md.\n\n')
    for m in new:
        r = records[m]
        f.write(m + '\n')
        for k in ['title', 'authors', 'url', 'revision', 'public_availability_witness_utc', 'witness_url', 'locator', 'sha256']:
            f.write('  ' + k + ': ' + str(r[k]) + '\n')
        f.write('  stage: ' + ('full integration' if m in final else 'earlier FourPartial integration') + '\n\n')
print(json.dumps({'original': len(original), 'partial': len(partial), 'full': len(full), 'wave_added_library_modules': len(new), 'final_stage_added_library_modules': len(final)}, indent=2))
