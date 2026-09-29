#!/usr/bin/env python3
"""Freeze completed integrator delivery; no proof, pin, source or build edits."""
from pathlib import Path
import importlib.util, json, re

O = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('checks', O / 'check-integration-v1.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
before = json.loads((O / 'snapshot-before.json').read_text())
c.assert_frozen(before, True)
assert c.ident(c.ROOT)['sha256'] == 'cd6a1dd9bff63ef400559805123c5e6cb7d2d4c9af28cf7f7c24f2cc640abc3c'
assert c.sigs() == json.loads((O / 'signatures-integrated.json').read_text())
assert json.loads((O / 'audit-v1.json').read_text())['status'] == 'PASS'
assert json.loads((O / 'all-commands-audit-v1.json').read_text())['status'] == 'PASS'
reviews = {
    c.W / 'nl/reviews/final-four-review-a-v1.md': 'f8a73c44d01e7f8e09657c004341e73a86f7cff61707bdfc5e077aa5513542bd',
    c.W / 'nl/reviews/final-four-review-b-v1.md': '7bf8a90a16d1b20a14142095892d11d23abb4deb8f82daf25aa7d46dfa6971c4',
}
for path, expected in reviews.items():
    assert c.ident(path)['sha256'] == expected
    assert 'PASS' in path.read_text()
    for sha in ['205df4c7b85c9ce40cccf1b42aa92f174fb0365b058466a3c4f2d3ba6968831b',
                'fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066']:
        assert sha in path.read_text()
links = []
documents = [c.W / 'REPRODUCE.md', c.W / 'sources.md', c.W / 'LEMMA_MAP.md']
for doc in documents:
    for match in re.finditer(r'\]\(([^)]+)\)', doc.read_text()):
        href = match[1]
        if '://' not in href and not href.startswith('#'):
            target = (doc.parent / href.split('#')[0]).resolve()
            assert target.exists(), (doc, href)
            links.append({'from': str(doc), 'href': href, 'exists': True})
for record in json.loads((O / 'all-commands-audit-v1.json').read_text())['commands']:
    p = O / record['record']
    original = json.loads(p.read_text())
    for stream in ['stdout', 'stderr']:
        assert c.ident(p.with_suffix('.' + stream)) == original[stream]
inventory = json.loads((O / 'library-inventory-v1.json').read_text())
for rec in inventory['records'].values():
    assert c.ident(rec['path'])['sha256'] == rec['sha256']

c.save('delivery-check-v1.json', {'status': 'PASS', 'utc': c.utc(),
    'command': 'python3 ' + str(Path(__file__).resolve()),
    'cwd': str(Path.cwd()), 'source_or_build_changes': False,
    'new_final_nl_review_identities': {str(p): c.ident(p) for p in reviews},
    'final_documents': {str(p): c.ident(p) for p in documents},
    'document_links': links,
    'remaining_obligation': 'Leader-owned final regulator and publication only; original all-even Target remains outside this result'})
files = {Path(p) for p in before} | set(documents) | set(reviews)
files.update(p for p in O.iterdir() if p.is_file() and p.name != 'artifact-hashes-v1.json')
c.save('artifact-hashes-v1.json', {'utc': c.utc(), 'status': 'final integration delivery',
    'root': str(c.ROOT), 'files': {str(p): c.ident(p) for p in sorted(files)},
    'excluded_self': 'artifact-hashes-v1.json',
    'scope': 'Integrators evidence/documents, protected inputs, exact NL reviews; upstream library module hashes separately in library-inventory-v1.json'})
print('PASS; final manifest', c.ident(O / 'artifact-hashes-v1.json')['sha256'])
print('Report', c.ident(O / 'integration-report-v1.txt')['sha256'])
