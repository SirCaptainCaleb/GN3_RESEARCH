# Phase-rigid six-vertex boundary tournament and global endpoint lock in seven vertices

- Stable ID: note_nori_xi_phase_rigid_and_seven_vertex_endpoint_lock
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: counterexample, boundary-tournament, phase-rigidity, spanning-one-turn, endpoint-extension, interior-insertion, finite-certificate
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_2
- Updated session: session_nori_r6430_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Consequential refutation of universal "terminal-phase flexibility" and of universal one-ended insertion for optimal (n−1)-vertex paths.

Index reversal pairs of distinct triples (a,b,c) by increasing middle b then lexicographic outer pair a<c. Color the representative by its indexed bit of the mask; reversing outer elements complements the color.

SIX-VERTEX PHASE-RIGID EXAMPLE. For V={0,...,5}, take mask M6=0x7f9ed7b30020000. All 720 permutations have internal turn-count histogram 0:0, 1:84, 2:360, 3:276. Among the 84 spanning one-turn words, 20 distinct ordered starting pairs occur; for each of those 20 pairs, all good words starting there have the SAME initial triple color. Thus there is no ordered starting pair with two spanning one-turn words having opposite initial colors. This refutes the universal terminal-phase-flexibility strengthening already at n=6, but not the original spanning one-turn conjecture.

SEVEN-VERTEX ENDPOINT-LOCKED EXTENSION. Add vertex z=6 and use mask M7=0x3ff0ecd1d98f0021004000. Every one of the 84 spanning one-turn paths in the original induced six-set, upon prepending z or appending z, has TWO turns, so no such path extends through either endpoint. Nevertheless, every one of those 84 paths DOES admit an interior insertion of z giving ONE turn. The seven-vertex tournament has 376 spanning one-turn paths and no monochromatic spanning path. An example is (0,1,2,4,6,3,5).

The construction of the extension is systematic: for each initial ordered pair (u,v) occurring among the 84 six-vertex good paths, their first color f(u,v) is uniquely defined. Set b(6,u,v)=1−f(u,v) and b(v,u,6)=f(u,v). Arbitrary reversal-compatible choices suffice for unused pairs and triples with 6 in the middle. This forces an additional initial turn after prepending z to every good word, and, by reversal, an additional final turn after appending z. For the displayed M7, undefined roots use f=0 and the middle-6 triples use ordinary outer-comparison orientation.

Python 3 verification certificate:

from itertools import combinations, permutations
from collections import Counter, defaultdict
def index(n):
    t=[(a,b,c) for b in range(n) for a,c in combinations([x for x in range(n) if x!=b],2)]
    return {tr:i for i,tr in enumerate(t)}
def run(w,mask,idx):
    C=[]
    for i in range(len(w)-2):
        a,b,c=w[i:i+3]
        C.append(((mask>>idx[(a,b,c) if a<c else (c,b,a)])&1)^int(a>c))
    return C,sum(C[i]!=C[i+1] for i in range(len(C)-1))
i6=index(6); i7=index(7)
m6=0x7f9ed7b30020000
m7=0x3ff0ecd1d98f0021004000
h6=Counter(run(w,m6,i6)[1] for w in permutations(range(6)))
assert h6==Counter({1:84,2:360,3:276})
good=[w for w in permutations(range(6)) if run(w,m6,i6)[1]<=1]
phases=defaultdict(set)
for w in good: phases[w[:2]].add(run(w,m6,i6)[0][0])
assert len(good)==84 and len(phases)==20
assert all(len(S)==1 for S in phases.values())
assert all(run((6,)+w,m7,i7)[1]==2 for w in good)
assert all(run(w+(6,),m7,i7)[1]==2 for w in good)
assert all(min(run(w[:i]+(6,)+w[i:],m7,i7)[1] for i in range(1,6))==1 for w in good)
h7=Counter(run(w,m7,i7)[1] for w in permutations(range(7)))
assert h7[0]==0 and h7[1]==376
assert run((0,1,2,4,6,3,5),m7,i7)[1]==1

Scope: the counterexample invalidates a conjectural ROOTED strengthening, not the original one-turn Hamilton conjecture. It shows that the spanning proof must permit interior insertions or global two-arm rerouting, not only endpoints of near-spanning paths.

LOCAL INTERIOR INSERTION CRITERION (valid in every order). Let W contain consecutive four original vertices a,b,c,d, and suppose we insert a new vertex z between b and c. The original two triple colors
  A=b(a,b,c), B=b(b,c,d)
are replaced by the three colors
  A'=b(a,b,z), B'=b(b,z,c), C'=b(z,c,d);
all other triple colors are unchanged. If the unique old color change occurs strictly outside the affected windows, the new three colors must all agree with the old constant phase on that segment for a one-turn extension (subject to the obvious boundary cases). If the old change occurs between the two replaced windows (A≠B), and unaffected windows of both phases remain, then the replacement triple colors must form one of the four weakly monotone patterns
  AAA, AAB, ABB, BBB,
where A and B are the opposite old phases; the old external colors bound the new triple sequence. This is a finite, three-window surgery test, not an assumed global insertion theorem. It explains why the seven-vertex endpoint-locked example can remain fully internally absorbable: interior insertion replaces TWO old constraints with THREE new ones and allows moving the unique phase change within that window.

Proposed next research target (open): prove that for every legal boundary coloring and every designated omitted vertex z, there exists at least one spanning one-turn path of the induced n−1 tournament that admits an interior insertion of z preserving at most one turn. This is stronger than the original spanning one-turn conjecture because removing an interior vertex from a one-turn full path need not preserve the one-turn property. The six/seven-vertex constructions above support this specific route but do not prove it.
