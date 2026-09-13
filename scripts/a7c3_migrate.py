import hashlib, json, re, subprocess, sys
from pathlib import Path

ROOT = Path.cwd()
SNAPSHOT = Path('/tmp/a7c3-snapshot.json')
S = json.loads(SNAPSHOT.read_text(encoding='utf-8'))


def write_exact(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def blob_sha_text(text: str) -> str:
    b = text.encode('utf-8')
    return hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()


def blob_sha_file(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()


def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()


docs = S['workspaces']['documents']
drevs = {int(r['id']): r for r in S['workspaces']['revisions']}
claims = S['results']['claims']
revs = {int(r['id']): r for r in S['results']['revisions']}
health = {int(h['revision_id']): h for h in S['results']['health']}
proofs = {int(p['id']): p for p in S['results']['proofs']}
links = {}
for pc in S['results']['proof_conclusions']:
    links.setdefault(int(pc['claim_revision_id']), []).append(pc)
claim_by_rid = {int(c['current_revision_id']): c for c in claims}

if len(docs) != 23:
    raise RuntimeError(f'expected 23 active workspaces, got {len(docs)}')
if len(claims) != 709 or len(revs) != 709 or len(health) != 709:
    raise RuntimeError(f'current result cardinality drift claims={len(claims)} revs={len(revs)} health={len(health)}')
if set(claim_by_rid) != set(revs):
    raise RuntimeError('claim/current-revision mismatch')


def choose_proof(rid):
    candidates = []
    for pc in links.get(rid, []):
        p = proofs.get(int(pc['proof_id']))
        if p and p.get('proof_text') not in (None, ''):
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
proofless = sorted(rid for rid, p in selected.items() if p is None)
if proofless != [888, 892]:
    raise RuntimeError(f'proofless set drifted: {proofless}')


def cls(rid):
    c, r, h = claim_by_rid[rid], revs[rid], health[rid]
    if bool(h.get('usable')):
        return 'USABLE/ACTIVE' if c.get('lifecycle_status') == 'active' else 'USABLE/LEGACY'
    if r.get('is_valid') is False or c.get('lifecycle_status') == 'invalidated':
        return 'UNUSABLE/INVALID'
    return 'UNUSABLE/QUARANTINED'


classes = {rid: cls(rid) for rid in revs}
counts = {k: list(classes.values()).count(k) for k in set(classes.values())}
expected_counts = {'USABLE/ACTIVE': 272, 'USABLE/LEGACY': 287, 'UNUSABLE/INVALID': 1, 'UNUSABLE/QUARANTINED': 149}
if counts != expected_counts:
    raise RuntimeError(f'classification drift: {counts}')
if classes.get(5) != 'UNUSABLE/QUARANTINED' or classes.get(685) != 'UNUSABLE/INVALID' or classes.get(1026) != 'UNUSABLE/QUARANTINED':
    raise RuntimeError('critical result classification drift')


def render_active(rid):
    c, r = claim_by_rid[rid], revs[rid]
    fields = ['statement', 'hypotheses', 'scope', 'applicability', 'persistence', 'exclusions_nonclaims']
    if any(r.get(x) is None for x in fields):
        raise RuntimeError(f'R{rid} has NULL active field')
    p = selected[rid]
    proof = p['proof_text'] if p is not None else 'No preferred proof was present in the authoritative Supabase record.'
    return (
        f'# R{rid} — {c["title"]}\n\n'
        f'## Statement\n{r["statement"]}\n\n'
        f'## Hypotheses\n{r["hypotheses"]}\n\n'
        f'## Scope\n{r["scope"]}\n\n'
        f'## Applicability\n{r["applicability"]}\n\n'
        f'## Persistence\n{r["persistence"]}\n\n'
        f'## Exclusions / nonclaims\n{r["exclusions_nonclaims"]}\n\n'
        f'## Proof\n{proof}'
    )


def validate_workspaces():
    by_agent = {d['agent_id']: d for d in docs}
    if set(by_agent) != {'D1','D2','D3','D4','D5','D8','D9','D10','D11','D12','D13','D14','D15','D16','D17','D19','D20','D21','D22','D23','D24','D25','D27'}:
        raise RuntimeError('active workspace set drifted')
    d17 = by_agent['D17']
    if int(d17['current_revision_id']) != 814:
        raise RuntimeError(f'D17 frontier drifted to {d17["current_revision_id"]}')
    if git('rev-parse', 'HEAD:A7C3/WORKSPACE/D17') != '02bc036b1b37a15a9dcd56fa5ad628358aef8b3c':
        raise RuntimeError('D17 tree mismatch')
    if blob_sha_file(ROOT/'A7C3/WORKSPACE/D1/CURRENT.md') != '83185e39e61a443be5b7fd92086fe213e68a3bf0':
        raise RuntimeError('corrected D1 blob mismatch')
    d1text = (ROOT/'A7C3/WORKSPACE/D1/CURRENT.md').read_text(encoding='utf-8')
    if '4*(22+2*21)=256' not in d1text or '172 directed-candidate tail is invalid' not in d1text:
        raise RuntimeError('D1 correction markers missing')
    for aid, d in by_agent.items():
        if aid in ('D1', 'D17'):
            continue
        r = drevs[int(d['current_revision_id'])]
        expected = f'# {aid} — {d["title"]}\n\n{r["body"]}'
        path = ROOT/'A7C3/WORKSPACE'/aid/'CURRENT.md'
        if not path.is_file() or path.read_text(encoding='utf-8') != expected:
            raise RuntimeError(f'workspace {aid} differs from live Supabase source')


def validate_nonactive():
    legacy = list((ROOT/'A7C3/RESULTS/USABLE/LEGACY').glob('R*.md'))
    invalid = list((ROOT/'A7C3/RESULTS/UNUSABLE/INVALID').glob('R*.md'))
    quarantined = list((ROOT/'A7C3/RESULTS/UNUSABLE/QUARANTINED').glob('R*.md'))
    if len(legacy) != 287 or len(invalid) != 1 or len(quarantined) != 150:
        raise RuntimeError(f'nonactive counts wrong legacy={len(legacy)} invalid={len(invalid)} quarantined={len(quarantined)}')
    if blob_sha_file(ROOT/'A7C3/RESULTS/UNUSABLE/INVALID/R685.md') != 'fbed72f56e511d25f3ff03f2cbeea8943d92dd19':
        raise RuntimeError('R685 invalid record mismatch')
    if blob_sha_file(ROOT/'A7C3/RESULTS/UNUSABLE/QUARANTINED/R1026.md') != 'de0f938c0e638e3f2487a54c8fd9ac0a07d1fdc2':
        raise RuntimeError('R1026 quarantined record mismatch')
    if not (ROOT/'A7C3/RESULTS/UNUSABLE/QUARANTINED/R5.md').is_file() or not (ROOT/'A7C3/RESULTS/UNUSABLE/QUARANTINED/R24.md').is_file():
        raise RuntimeError('R5/R24 quarantine missing')


phase = sys.argv[1]
if phase == 'workspaces':
    validate_workspaces()
    print('WORKSPACES PASS 23 active; corrected D1; D17 exact')
elif phase == 'active':
    dest = ROOT/'A7C3/RESULTS/USABLE/ACTIVE'
    dest.mkdir(parents=True, exist_ok=True)
    for p in dest.glob('R*.md'):
        if re.fullmatch(r'R\d+\.md', p.name):
            p.unlink()
    ids = sorted(rid for rid in revs if classes[rid] == 'USABLE/ACTIVE')
    for rid in ids:
        write_exact(dest/f'R{rid}.md', render_active(rid))
    print('ACTIVE WRITE', len(ids), ids[0], ids[-1])
elif phase == 'legacy':
    validate_nonactive()
    print('LEGACY PASS 287')
elif phase == 'unusable':
    validate_nonactive()
    print('UNUSABLE PASS 150 current + historical R24')
elif phase == 'audit':
    validate_workspaces()
    validate_nonactive()
    active = list((ROOT/'A7C3/RESULTS/USABLE/ACTIVE').glob('R*.md'))
    if len(active) != 272:
        raise RuntimeError(f'active count wrong: {len(active)}')
    for rid in sorted(r for r in revs if classes[r] == 'USABLE/ACTIVE'):
        path = ROOT/'A7C3/RESULTS/USABLE/ACTIVE'/f'R{rid}.md'
        expected = render_active(rid)
        if not path.is_file() or path.read_text(encoding='utf-8') != expected:
            raise RuntimeError(f'ACTIVE R{rid} differs from authoritative render')
    found = {}
    for p in (ROOT/'A7C3/RESULTS').rglob('R*.md'):
        m = re.fullmatch(r'R(\d+)\.md', p.name)
        if m:
            found.setdefault(int(m.group(1)), []).append(str(p.relative_to(ROOT)))
    dup = {rid: paths for rid, paths in found.items() if len(paths) != 1}
    missing = sorted(set(revs) - set(found))
    unexpected = sorted(set(found) - set(revs) - {24})
    if dup or missing or unexpected or 24 not in found or len(found) != 710:
        raise RuntimeError(f'result audit failed count={len(found)} dup={dup} missing={missing} unexpected={unexpected} has24={24 in found}')
    d17_sections = len(list((ROOT/'A7C3/WORKSPACE/D17').glob('[0-9][0-9][0-9]-*.md')))
    if d17_sections != 430:
        raise RuntimeError(f'D17 section count {d17_sections}')
    temp = (ROOT/'A7C3/WORKSPACE/MISSING_PROOFS_TEMP.md').read_text(encoding='utf-8')
    if '## R888' not in temp or '## R892' not in temp:
        raise RuntimeError('temporary proof-gap note is stale/missing')
    print('AUDIT PASS workspaces=23 active=272 legacy=287 current_unusable=150 historical_R24=1 durable_ids=710 proofless=R888,R892 D17_sections=430')
else:
    raise RuntimeError(f'unknown phase {phase}')
