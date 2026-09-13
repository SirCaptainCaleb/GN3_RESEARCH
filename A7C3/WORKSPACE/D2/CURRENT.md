# D2 — Bounded boundary compression of selected deletion-cover reconstructions

For any fixed exact two-path deletion cover, deleting a bounded distinguished set yields only a bounded number of inherited residual blocks; every reconstruction preserving those blocks is decided by a finite boundary-state instance whose size is independent of the long native rail. The development proves the exact forest count, suffix-state recognizer, and equivalent finite surrogate, specializes the bounds to the inward-anchor five-cell residue, and records the sharp R904 all-order obstruction showing why an intact-native-middle normalization cannot suffice. The unresolved step is existential: one must still force some selected exact cover to pass the recognizer.

## Scope, quantifiers, and ownership boundary

Fix a finite boundary tournament H. Let D be a deleted set and let T be one fixed ordered two-path cover of H-D. Every residual block below is a literal interval of this T in its inherited order. Different exact covers may yield different blocks and different recognizer outcomes; nothing in this document synchronizes them.

The reconstruction mechanism is separate from neighboring gate and five-cell geometry. R862 supplies a selected exact cover in the crossed inward-anchor frame. R885/R894/R901 describe fragmentation and conservation inside such covers and are developed in D1. R911 and pending R917 are gate-phase consumers, not premises of the compression theorem. R904 is a fence against a more restrictive intact-native-middle strategy.

Status discipline: R904/P975 and the cited exact source results retain their live resolver status. The fixed-cover compression theorem, recognizer theorem, and finite-surrogate equivalence are newly assembled mathematical conclusions in this document and are pending fresh review. The final closure target is explicitly unresolved.

## Exact fixed-cover boundary compression

General counting reference: D13/selected-forest-counting proves the deletion identity for any number of selected paths. Here the component count is two and the symbol k below denotes |K|, so its formula specializes to r=2+k-p-delta_K. The boundary-compression argument below is the additional content of this section.

Let |D|=d and let T=T_1 sqcup T_2 be a fixed ordered two-path cover of H-D. Choose K subset V(T), |K|=k. Remove K from the two listed paths without recompleting or reordering anything. Let B_1,...,B_r be the nonempty maximal residual intervals, in inherited T order. Put p=e_T(K) and delta_K=sum_{x in K}(2-deg_T(x)), where degree is taken in the undirected spanning linear forest underlying T. A singleton rail has degree zero and contributes two end slots.

Then r=2+k-p-delta_K, hence r<=k+2.

Proof. Let q=e_T(K,V(T)-K). The two rails of T form an undirected spanning linear forest with |V(T)|-2 edges. Degree summation on K gives 2p+q=2k-delta_K. After deleting K, the induced forest on V(T)-K has |V(T)|-2-p-q edges. Its component count is |V(T)|-k-(|V(T)|-2-p-q)=2-k+p+q=2+k-p-delta_K. These components are exactly the nonempty maximal residual intervals B_i. The same formula handles singleton-rail and empty-residue degeneracies because delta_K records missing endpoint incidences.

Now restrict to spanning covers of H by at most two tight paths that retain every B_i intact in inherited order. Vertices of K union D may move freely. The B_i may be permuted, assigned to either output path, and separated by distinguished singletons; no B_i reversal is allowed.

There are b=r+k+d pieces. Every admissible reconstruction is two ordered lists partitioning these pieces, with an empty list allowed. Its validity is determined by certified internal tightness of each B_i, the first two and last two vertices of each B_i with overlaps retained for lengths 1,2,3, all vertices of K union D, and every ordered triple crossing a piece boundary. Hence the entire instance uses at most k+d+4r<=5k+d+8 actual original vertices.

This boundary data is sufficient. Every consecutive triple in an expanded candidate either lies wholly inside one B_i, where tightness is inherited from T, or crosses a piece boundary, where it uses only the retained first/last two vertices. Conversely if every crossing triple is tight, expansion gives disjoint spanning tight paths. Thus the interface is exact for the stated block-preserving class.

## Exact suffix-state recognizer and the two-join seam caveat

Pairwise compatibility of adjacent pieces is insufficient. If a singleton x sits between retained blocks A and B, the triple (last(A),x,first(B)) meets two joins and must be checked in addition to any turns (penultimate(A),last(A),x) and (x,first(B),second(B)). Runs of singletons give the analogous phenomenon. A correct recognizer must therefore remember two physical terminal vertices.

For every subset S of the b pieces, store all suffix states of length zero, one, or two actual vertices reachable by ordering exactly the pieces of S into one tight macro-path. Initialize the empty subset by the empty suffix. From a reachable state, append any unused piece P, expose only the boundary needed at the new join, and test every newly created consecutive triple whose final piece is P. Reject if any is bad; otherwise store the final at most two actual vertices.

Let good(S) mean that some suffix state is reachable. A block-preserving spanning cover by at most two paths exists exactly when some subset S satisfies good(S) and good(All-S), including S=empty and S=All.

Correctness is inductive: the suffix contains exactly the old actual vertices that can enter a newly created triple; internal triples of P are already certified. Every reachable state therefore expands to a tight path, and every valid macro-path traces accepted transitions piece by piece.

There are O(b^2) ordered suffixes over the bounded representation and at most b next-piece choices, giving a straightforward O(2^b b^3) transition bound up to a constant number of turn tests. This recognizes the designated block-preserving class, not unrestricted two-coverability.

## Equivalent finite boundary-tournament surrogate and lifting fence

Replace every retained block B of length at least five by four distinct representatives in inherited order: first(B), second(B), penultimate(B), last(B). Keep shorter blocks verbatim and every distinguished singleton.

Preserve the original orientation of every turn whose support meets more than one piece. Inside each shortened four-vertex block, declare its two consecutive inherited-order triples tight and their complete reversals bad. These two triples have different supports, so there is no antisymmetry conflict. Complete all remaining reversal pairs arbitrarily. The result is a genuine smaller boundary tournament with designated ordered blocks.

The surrogate has a spanning cover by at most two tight paths preserving all designated blocks iff the original selected-cover instance has such a reconstruction. Contracting a valid original reconstruction preserves every inter-piece turn and replaces each inherited block by a designated internally tight surrogate block. Conversely, expanding a designated-block surrogate cover restores tight inherited intervals and preserves every checked boundary turn.

The restriction is essential. An arbitrary surrogate two-cover may split, reverse, or interleave designated blocks and need not lift. The surrogate is not merely an induced subtournament of H and need not inherit smallest-counterexample hypotheses, native-Q structure, or other global properties not encoded in the interface.

## Thirty-, forty-, and sixty-vertex interfaces in the inward-anchor residue

In accepted R862 let D={v,d}={q_2,q_{m-2}} and T be any exact two-cover of W=H-D. With X={a,b,c,z} and K=X, k=4,d=2, so r=6-p-delta_X and b=r+6<=12. The original-vertex boundary budget is 6+4r=30-4(p+delta_X)<=30. Thus every X-movable block-preserving reconstruction of this selected T is represented on at most thirty original vertices, independent of m.

The residual blocks are arbitrary T-ordered portions of W-X, not necessarily native-Q intervals. The same forest identity explains the numerical conservation layer R901; the stronger M/N skeleton geometry of R885/R894 is separate mathematics already developed in D1.

To expose q_3 and q_{m-3} as independently movable physical labels, take K=X union {q_3,q_{m-3}}. Then k<=6,d=2,r<=8, giving at most forty boundary vertices. If L,u,s,R must also remain movable, add them to K; k<=10 gives the crude sixty-vertex bound. A labelled vertex sitting inside a retained block is not automatically movable.

## All-order obstruction to preserving the native middle rail

Accepted R904 shows that the selected-cover formulation is necessary. For every n>=11 there is a Hamiltonian boundary tournament satisfying the transitive crossed eight-core geometry but admitting no spanning two-cover that preserves the obvious native middle rail N as one contiguous block.

The fixed core G has X={a,b,c,z} and caps {L,u,s,R}. Its exact support property, exhaustively verified by the 168-bit certificate in P975, is: G[X union E] is Hamiltonian iff (u in E and L notin E) or (s in E and R notin E), for every E subset {L,u,s,R}. It also has the endpoint barriers (x,L,u) bad outside {L,u} and (s,R,x) bad outside {s,R}, plus the crossed gate/core paths used by the local frame.

For arbitrary k>=1 introduce v,d,w_1,...,w_k, write W=(w_1,...,w_k), N=(v,W,d), Q=(L,u,v,W,d,s,R), and prescribe comparisons so the only nonempty core prefix immediately before N is (u) or (L,u), and dually the only nonempty core suffix after N is (s) or (s,R). The prescriptions are consistent for every k and R904 gives an explicit spanning Hamilton path, so H is Hamiltonian.

Suppose a cover by at most two paths keeps N intact. Write the N-containing path as A N C and the other path as B, with A,B,C using only core vertices. The first comparison family forces nonempty A to end in u; if |A|>=2 its penultimate vertex is L; the core barrier forbids a third core vertex before L,u. Thus A is empty,(u),or(L,u). Dually C is empty,(s),or(s,R).

Hence B contains X plus a cap set E satisfying u in E => L in E and s in E => R in E. The core support criterion makes X union E nonHamiltonian, contradicting B being a path. Thus no two-cover may keep N intact.

The exact 168-bit data and self-contained verifier stay in P975. R904 does not obstruct D2, because a selected recompletion T may already split or reorder the old native middle before D2 compresses its own inherited blocks.

## The remaining existential theorem

D2 now removes the unbounded-rail-size problem for any fixed selected exact cover. What remains unproved is existence of a relevant exact cover whose bounded instance actually accepts.

A sufficient crossed-frame closure statement is: there exists an exact R862 cover T of H-{q_2,q_{m-2}} such that, after exposing K=X union {q_3,q_{m-3}}, the resulting boundary instance is accepted by the exact recognizer.

This is open. Failure for one selected T says nothing about another. Success of an arbitrary surrogate cover says nothing unless it preserves the designated blocks. R911 supplies exact first-depth clauses and pending R917 supplies stronger conditional BI-anchor geometry, but neither presently forces recognizer acceptance. No P4, Reverse-Ear, witness packet, or transition count is treated as closure without a cover-valued consumer.

## The intact-middle obstruction is hereditarily two-coverable

The explicit default completion in P975 has a stronger property than recorded in R904: for every k>=1, EVERY induced subsystem of H_k has a cover by at most two tight paths. Nevertheless H_k has no two-cover preserving N=(v,w_1,...,w_k,d) intact.

This assertion is specific to the increasing-outer-index completion used by P975's construct(k), not to every arbitrary completion allowed in its existence proof. H_k itself is Hamiltonian; it is not a smallest counterexample.

Construction and finite reduction. Keep P975's labels (a,b,c,z,L,u,s,R,v,d)=(0,...,9) and w_i=9+i. Let B=G union {v,d}, with |B|=10. The induced boundary tournament on B is independent of k. It is obtained from the 168-bit G certificate by imposing (x,u,v) tight iff x=L, (d,s,x) tight iff x=R, the three turns (c,v,a),(v,a,b),(b,z,d) tight, and setting each remaining canonical reversal-pair bit to 1. The first two families range over the admissible core vertices as in P975.

Call a Hamilton path on a base subset safe-ended if it is empty or a singleton, or its final ordered pair (i,j) avoids:
  j=v with i in G-{u};
  (i,j)=(s,d);
  (i,j)=(u,L).
The finite certificate in hereditary-obstruction-certificate verifies:
  for EVERY A subseteq B, A partitions as P sqcup Q,
  where P and Q are tight paths (empty paths allowed) and P is safe-ended.
In particular every base subset is two-coverable. This finite statement is stronger than mere two-coverability because it retains the append port needed below.

Boundary inspection of the P975 default completion gives, for distinct i,j in B,
  (i,j,w_h) is bad iff
  [h=1 and j=v and i in G-{u}]
  OR [h=k and ((i,j)=(s,d) OR (i,j)=(u,L))].
Every other such triple is tight. This follows directly from the two first/last-W comparison families, the forced P975 Hamilton-path turn (w_k,L,u), and default bit 1. Also, for j in B and h<ell, (j,w_h,w_ell) is tight. Every increasing subsequence of W is tight. The extra Q/P prescriptions involving two or three W vertices are consistent with these assertions: those having increasing W indices agree with the default; their reversals have decreasing indices and are not used here.

Now take any S subseteq V(H_k), put A=S intersect B and Z=S intersect W. If Z is empty, use the certified two-cover of A. Otherwise let Z=(w_{i_1},...,w_{i_t}) in increasing index order and choose the certified P,Q for A. Replace P by P followed by Z. If P has at least two vertices, its first junction triple is tight by the safe-ended condition. If P is nonempty and |Z|>=2, the second junction triple is tight by the preceding boundary identity. Internal Z triples are tight; singleton and empty cases omit nonexistent triples. Hence (P+Z) sqcup Q is a spanning at-most-two-cover of H_k[S]. This proves the all-subsets, all-k assertion.

R904/P975 already proves that these same default-completed H_k are Hamiltonian and admit no cover retaining N intact. Thus the local crossed-core data, together with the bare inductive assertion pc(H[S])<=2 for every nonempty proper S, still do not imply intact-N normalization.

Scope of the strengthened fence. It does NOT rule out reasoning that uses pc(H)>2 to obtain additional restrictions, prescribed endpoint information, coherent relations among deletion covers, or selected deeper cuts. In particular “smallest-counterexample minimality” includes pc(H)=3, which these examples do not satisfy. The conclusion is only that proper-subsystem cover availability alone does not repair the proposed local normalization.

This is new computer-assisted internal mathematics: a fixed ten-vertex exhaustive certificate plus a symbolic arbitrary-length proof. It awaits independent review and does not change the accepted statement or proof of R904/P975.

## Finite certificate for hereditary two-coverability of the obstruction

This is the complete finite verification required by hereditary-intact-middle-obstruction. BITS is exactly the core certificate of P975; the following forces give its k-independent induced base on ten vertices.

For each subset, the dynamic program exhausts all possible last-two-vertex states of Hamilton paths on that subset. Its induction is exact: any path is obtained by deleting its last vertex, and appending a new vertex requires only the last consecutive triple to be tight. Empty and singleton paths are handled explicitly. The final submask loop exhausts unordered support partitions with a distinguished safe-ended component. An assertion passes precisely when a safe-ended Hamilton path and a complementary Hamilton path exist. Execution returned PASS for all 1024 subsets.

This verifies only the fixed base property. The adjacent section proves the lift for every subset of every H_k symbolically; no finite sample is substituted for that argument.

```python
from itertools import permutations

BITS='111011100000000100000111111000001111000001100000000001100000000000001010011001001011101000000001000000111010000000000000000100100001000010001001011101001010011101001011'
a,b,c,z,L,u,s,R,v,d=range(10)
keys=[(x,y,t) for y in range(8) for x in range(8)
      for t in range(x+1,8) if y not in (x,t)]
assert len(keys)==len(BITS)==168
T=dict(zip(keys,map(int,BITS)))
def force(triple,value=True):
    x,y,t=triple
    key=(min(x,t),y,max(x,t))
    bit=int(value if x<t else not value)
    assert key not in T or T[key]==bit
    T[key]=bit
def tight(x,y,t):
    return bool(T[(x,y,t)]) if x<t else not T[(t,y,x)]
for x in range(8):
    if x!=u: force((x,u,v),x==L)
    if x!=s: force((d,s,x),x==R)
for triple in [(c,v,a),(v,a,b),(b,z,d)]:
    force(triple)
for y in range(10):
    for x in range(10):
        for t in range(x+1,10):
            if y not in (x,t): T.setdefault((x,y,t),1)

# states[M]: every reachable last-two-vertex state of a Hamilton path on M.
# Empty and singleton states are kept explicitly.
states=[set() for _ in range(1<<10)]
states[0].add(())
for mask in range(1<<10):
    for tail in states[mask]:
        for x in range(10):
            if mask>>x&1: continue
            if len(tail)==2 and not tight(tail[0],tail[1],x): continue
            states[mask|1<<x].add((tail+(x,))[-2:])

def safe(tail):
    if len(tail)<2: return True
    i,j=tail
    return not ((j==v and i<8 and i!=u)
                or (i==s and j==d) or (i==u and j==L))

ham=[bool(q) for q in states]
extendible=[any(map(safe,q)) for q in states]
for mask in range(1<<10):
    sub=mask
    while not (extendible[sub] and ham[mask^sub]):
        assert sub!=0, ('failed subset',mask)
        sub=(sub-1)&mask
print('PASS: all 1024 base subsets have a two-path partition with a safe append end.')

```
