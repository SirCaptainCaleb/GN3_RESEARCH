import json, sys, re, shutil, hashlib
from pathlib import Path

ROOT = Path.cwd()
SNAPSHOT = Path('/tmp/a7c3-snapshot.json')
with SNAPSHOT.open(encoding='utf-8') as f:
    S = json.load(f)

def write_utf8(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)

def git_blob_sha(text: str) -> str:
    b = text.encode('utf-8')
    return hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()

def nonempty(v):
    return v is not None and v != ''

def add_section(parts, heading, value):
    if not nonempty(value):
        return
    parts.append(f'## {heading}\n')
    parts.append(value)
    if not value.endswith('\n'):
        parts.append('\n')
    parts.append('\n')

docs = S['workspaces']['documents']
drevs = {int(r['id']): r for r in S['workspaces']['revisions']}
claims = S['results']['claims']
revs = {int(r['id']): r for r in S['results']['revisions']}
health = {int(h['revision_id']): h for h in S['results']['health']}
proofs = {int(p['id']): p for p in S['results']['proofs']}
links = {}
for pc in S['results']['proof_conclusions']:
    links.setdefault(int(pc['claim_revision_id']), []).append(pc)

if len(docs) != 23:
    raise RuntimeError(f'expected 23 active workspaces, got {len(docs)}')
d17 = [d for d in docs if d['agent_id'] == 'D17']
if len(d17) != 1 or int(d17[0]['current_revision_id']) != 814:
    raise RuntimeError(f'D17 frontier drifted: {d17}')
if len(drevs) != 22:
    raise RuntimeError(f'expected 22 non-D17 current workspace revisions, got {len(drevs)}')
if len(claims) != 708 or len(revs) != 708 or len(health) != 708:
    raise RuntimeError(f'current result cardinality drift: claims={len(claims)} revs={len(revs)} health={len(health)}')

def choose_proof(rid, link_map=links, proof_map=proofs):
    candidates = []
    for pc in link_map.get(rid, []):
        p = proof_map.get(int(pc['proof_id']))
        if p and nonempty(p.get('proof_text')):
            candidates.append((pc, p))
    if not candidates:
        return None
    preferred = [(pc, p) for pc, p in candidates if bool(pc.get('is_preferred')) or bool(p.get('is_preferred'))]
    if preferred:
        if len(preferred) != 1:
            raise RuntimeError(f'R{rid} has {len(preferred)} explicit preferred proofs')
        return preferred[0][1]
    def rank(pair):
        _, p = pair
        return (bool(p.get('dependency_complete')), bool(p.get('is_valid')), p.get('review_status') == 'accepted', int(p['id']))
    return max(candidates, key=rank)[1]

selected = {rid: choose_proof(rid) for rid in revs}
with_text = sum(1 for p in selected.values() if p is not None)
if with_text != 703:
    raise RuntimeError(f'expected 703 current results with proof text, got {with_text}')

claim_by_rid = {int(c['current_revision_id']): c for c in claims}
if set(claim_by_rid) != set(revs):
    raise RuntimeError('claim/current-revision mismatch')

def classification(rid, claim, rev, h):
    if bool(h.get('usable')):
        return 'USABLE/ACTIVE' if claim.get('lifecycle_status') == 'active' else 'USABLE/LEGACY'
    if rev.get('is_valid') is False or claim.get('lifecycle_status') == 'invalidated':
        return 'UNUSABLE/INVALID'
    return 'UNUSABLE/QUARANTINED'

classes = {rid: classification(rid, claim_by_rid[rid], revs[rid], health[rid]) for rid in revs}
counts = {}
for cls in classes.values():
    counts[cls] = counts.get(cls, 0) + 1
if counts.get('USABLE/ACTIVE', 0) != 272 or counts.get('USABLE/LEGACY', 0) != 287 or sum(v for k, v in counts.items() if k.startswith('UNUSABLE/')) != 149:
    raise RuntimeError(f'trust classification drift: {counts}')
if classes.get(5) != 'UNUSABLE/QUARANTINED':
    raise RuntimeError(f'R5 unexpectedly classified {classes.get(5)}')

def render_result(rid, claim, rev, h, proof, historical=False):
    expected_agent = f'R{rid}'
    if rev.get('agent_id') != expected_agent:
        raise RuntimeError(f'revision {rid} agent_id={rev.get("agent_id")} expected {expected_agent}')
    parts = [f'# R{rid} — {claim["title"]}\n\n']
    cls = 'UNUSABLE/QUARANTINED' if historical else classification(rid, claim, rev, h)
    if cls != 'USABLE/ACTIVE':
        parts.append(f'**Record status:** `{cls}`')
        if historical:
            parts.append(' (preserved historical quarantined revision)')
        parts.append('\n\n')
    add_section(parts, 'Statement', rev.get('statement'))
    add_section(parts, 'Hypotheses', rev.get('hypotheses'))
    add_section(parts, 'Scope', rev.get('scope'))
    add_section(parts, 'Applicability', rev.get('applicability'))
    add_section(parts, 'Persistence', rev.get('persistence'))
    add_section(parts, 'Exclusions / nonclaims', rev.get('exclusions_nonclaims'))
    safety_relevant = cls.startswith('UNUSABLE/') or claim.get('lifecycle_status') != 'active' or rev.get('review_status') != 'accepted' or rev.get('is_valid') is False
    if safety_relevant:
        notes = []
        for label, value in [
            ('Lifecycle', claim.get('lifecycle_status')),
            ('Lifecycle note', claim.get('lifecycle_note')),
            ('Curation note', claim.get('curation_note')),
            ('Validity note', rev.get('validity_note')),
            ('Review status', rev.get('review_status')),
            ('Review note', rev.get('review_note')),
        ]:
            if nonempty(value):
                notes.append(f'- **{label}:** {value}')
        if notes:
            parts.append('## Record notes\n' + '\n'.join(notes) + '\n\n')
    parts.append('## Proof\n')
    if proof is None:
        parts.append('No preferred proof was present in the authoritative Supabase record.\n')
    else:
        parts.append(proof['proof_text'])
        if not proof['proof_text'].endswith('\n'):
            parts.append('\n')
    return ''.join(parts)

phase = sys.argv[1]
if phase == 'workspaces':
    hashes = {}
    for d in docs:
        aid = d['agent_id']
        if aid == 'D17':
            continue
        r = drevs[int(d['current_revision_id'])]
        content = f'# {aid} — {d["title"]}\n\n' + r['body'] + '\n'
        dest = ROOT / 'A7C3' / 'WORKSPACE' / aid
        if dest.exists():
            shutil.rmtree(dest)
        write_utf8(dest / 'CURRENT.md', content)
        hashes[aid] = git_blob_sha(content)
    print('WORKSPACES', len(hashes), json.dumps(hashes, sort_keys=True))
elif phase in ('active', 'legacy'):
    cls = 'USABLE/ACTIVE' if phase == 'active' else 'USABLE/LEGACY'
    dest = ROOT / 'A7C3' / 'RESULTS' / cls
    dest.mkdir(parents=True, exist_ok=True)
    for old in dest.glob('R*.md'):
        if re.fullmatch(r'R\d+\.md', old.name):
            old.unlink()
    ids = sorted(rid for rid, c in classes.items() if c == cls)
    for rid in ids:
        write_utf8(dest / f'R{rid}.md', render_result(rid, claim_by_rid[rid], revs[rid], health[rid], selected[rid]))
    print(phase.upper(), len(ids), ids[0] if ids else None, ids[-1] if ids else None)
elif phase == 'unusable':
    base = ROOT / 'A7C3' / 'RESULTS' / 'UNUSABLE'
    for old in base.rglob('R*.md'):
        if re.fullmatch(r'R\d+\.md', old.name):
            old.unlink()
    ids = sorted(rid for rid, c in classes.items() if c.startswith('UNUSABLE/'))
    for rid in ids:
        cls = classes[rid]
        write_utf8(ROOT / 'A7C3' / 'RESULTS' / cls / f'R{rid}.md', render_result(rid, claim_by_rid[rid], revs[rid], health[rid], selected[rid]))
    hs = S['historical_results']
    hrev = {int(r['id']): r for r in hs['revisions']}
    hclaim = {int(c['id']): c for c in hs['claims']}
    hhealth = {int(h['revision_id']): h for h in hs['health']}
    hproofs = {int(p['id']): p for p in hs['proofs']}
    hlinks = {}
    for pc in hs['proof_conclusions']:
        hlinks.setdefault(int(pc['claim_revision_id']), []).append(pc)
    if 24 not in hrev:
        raise RuntimeError('historical R24 missing')
    r = hrev[24]
    c = hclaim[int(r['claim_id'])]
    hp = choose_proof(24, hlinks, hproofs)
    hh = hhealth.get(24, {'usable': False})
    if bool(hh.get('usable')):
        raise RuntimeError('R24 unexpectedly cleared quarantine in health cache')
    write_utf8(ROOT / 'A7C3' / 'RESULTS' / 'UNUSABLE' / 'QUARANTINED' / 'R24.md', render_result(24, c, r, hh, hp, historical=True))
    print('UNUSABLE current', len(ids), 'plus historical R24')
elif phase == 'audit':
    current = set(revs)
    found = {}
    for p in (ROOT / 'A7C3' / 'RESULTS').rglob('R*.md'):
        m = re.fullmatch(r'R(\d+)\.md', p.name)
        if not m:
            continue
        rid = int(m.group(1))
        found.setdefault(rid, []).append(str(p.relative_to(ROOT)))
    dup = {rid: ps for rid, ps in found.items() if len(ps) != 1}
    missing = sorted(current - set(found))
    unexpected = sorted(set(found) - current - {24})
    if dup or missing or unexpected or 24 not in found:
        raise RuntimeError(f'result audit failed dup={dup} missing={missing} unexpected={unexpected} has24={24 in found}')
    if len(found) != 709:
        raise RuntimeError(f'expected 709 durable result ids (708 current + R24), got {len(found)}')
    numeric_d17 = [p for p in (ROOT / 'A7C3' / 'WORKSPACE' / 'D17').glob('*.md') if re.match(r'^\d{3}-', p.name)]
    if len(numeric_d17) != 430:
        raise RuntimeError(f'D17 section count drift: {len(numeric_d17)}')
    for d in docs:
        aid = d['agent_id']
        if aid == 'D17':
            continue
        if not (ROOT / 'A7C3' / 'WORKSPACE' / aid / 'CURRENT.md').is_file():
            raise RuntimeError(f'missing workspace {aid}/CURRENT.md')
    print('AUDIT PASS workspaces=23 current_results=708 historical_quarantined=1 d17_sections=430 classes=', json.dumps(counts, sort_keys=True))
else:
    raise RuntimeError('unknown phase')
