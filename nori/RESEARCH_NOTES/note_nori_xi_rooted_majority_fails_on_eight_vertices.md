# Eight-vertex obstruction to rooted-majority reachability

- Stable ID: note_nori_xi_rooted_majority_fails_on_eight_vertices
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: boundary-tournament, rooted-reachability, complementary-subsets, majority-obstruction, finite-certificate
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_2
- Updated session: session_nori_r6430_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Counterexample to a universal strict rooted-majority strengthening of the spanning one-turn boundary-tournament conjecture at n=8. Discovered by local search and independently verified both by subset dynamic programming and exhaustive permutation enumeration.

Index the 168 reversal pairs of distinct ordered triples (a,b,c) by increasing middle b, then increasing outer pair a<c. Color the representative by its indexed bit of
M=0x20163024f7d8f10a527d29ff9ff9bad4722810ffc0
and color its reversal complementarily.

For each root v and epsilon in {0,1}, A_v^epsilon is the family of subsets of the other seven original vertices occurring as the prefix vertex set of an epsilon-monochromatic vertex-simple tight word ending at v. Single-vertex and two-vertex words are vacuously monochromatic in either color. The family sizes, ordered by root v=0,...,7:
epsilon 0: [50,60,64,46,61,61,55,61]
epsilon 1: [47,55,64,64,52,62,54,62].
Every size is at most 64=2^(n-2), so NO rooted family has strict majority. Nevertheless W=(0,1,3,4,5,6,2,7) is a spanning one-turn path with triple colors (0,0,0,1,1,1).

Reproducible Python 3 standard-library certificate (enumerates every injective partial word, not a recurrence):
from itertools import combinations, permutations
from collections import defaultdict
V=tuple(range(8))
rep=[(a,b,c) for b in V
     for a,c in combinations([x for x in V if x!=b],2)]
assert len(rep)==168
idx={t:i for i,t in enumerate(rep)}
M=0x20163024f7d8f10a527d29ff9ff9bad4722810ffc0
def col(a,b,c):
    t=(a,b,c) if a<c else (c,b,a)
    return ((M>>idx[t])&1)^int(a>c)
F=defaultdict(set)
for k in range(1,9):
    for p in permutations(V,k):
        cs=[col(*p[i:i+3]) for i in range(k-2)]
        good=(0,1) if not cs else ((cs[0],) if all(t==cs[0] for t in cs) else ())
        for eps in good: F[p[-1],eps].add(frozenset(p[:-1]))
sizes0=[len(F[v,0]) for v in V]
sizes1=[len(F[v,1]) for v in V]
assert sizes0==[50,60,64,46,61,61,55,61]
assert sizes1==[47,55,64,64,52,62,54,62]
assert max(sizes0+sizes1)==64
W=(0,1,3,4,5,6,2,7)
assert [col(*W[i:i+3]) for i in range(6)]==[0,0,0,1,1,1]

Scope: This refutes only the majority-cardinality proof route, not the rooted complementary-reachability equivalence nor the spanning one-turn conjecture. The complemented pair exists here despite every family having at most half the subset lattice. Future proofs must exploit structure beyond cardinalities.
