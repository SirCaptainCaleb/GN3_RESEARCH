# Certified-square, rooted snake-exchange, and mixed-cap obstructions

- Stable ID: note_certified_square_snake_exchange_and_mixed_cap_obstructions
- Author: NORI manuscript editorial migration; mathematical origins recorded in original compositions
- Primary home: article:nori_article_v_local_connectors
- Labels: obstruction, counterexample
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r4593_2
- Disposition: none
- Successor: none

## Related references

- subsection:certified_four_geodesic_squares_and_physical_edge_coverage, exact version 1
- subsection:maximal_geodesic_blockers_and_snake_exchanges, exact version 2
- subsection:bichromatic_root_diamonds_and_mixed_terminal_cap_obstruction, exact version 1
- section:nori_maximal_geodesic_exchanges, exact version 2

## Research note

# Editorial scope and mathematical status

Method-specific limits of certified-square carriers, one-move geodesic descent, rooted short-support coverage, and opposite-color hub/terminal-cap splicing. These proved failures do not establish a universal positive NORI theorem.

The exact compositions below are copied verbatim from the previous manuscript hierarchy for reproducibility. Editorial transfer is not a refutation or a new mathematical proof. Manuscript historical versions and provenance remain accessible through nori.read_manuscript.


---

## Retired Subsection: Certified four-geodesic squares and physical edge coverage

Source ID: `certified_four_geodesic_squares_and_physical_edge_coverage`
Source Section: `nori_local_connector_geometry`
Exact original Subsection composition: v1.

# Certified four-geodesic squares and physical edge coverage

An edge of the cube is certified when it lies in a genuine monochromatic four-edge geodesic. Root squares and overlapping four-geodesic witnesses create a physical two-dimensional carrier with antipodal symmetries, and dead edges are exactly its missing certificates. The statements below turn parity and coverage into structural constraints on that carrier.

FINITE OBSTRUCTION TO OVERSTRENGTHENING THE CENTERED FIVE-CYCLE. The guaranteed centered four-edge mono two-window connector CANNOT in general be strengthened to a centered five-edge mono THREE-window connector using only the binary labels of ordered triples at one prescribed hub z on a fixed six-direction set. This is already false for an arbitrary vertex-local table of ordered-triple colors, and such a table is locally compatible with the global NORI antipodal-reversal axiom (the axiom constrains the antipodal physical face at bar z, not the reversed triple at the same z).
EXPLICIT CERTIFICATE. Index six directions as 0,1,2,3,4,5. For a in ascending order, b runs ascending through [0..5] except a, and for each (a,b), c runs ascending through [0..5] except a,b. Assign the 120 ordered-triple colors from six successive 20-bit rows:
  a=0: 11001110110011111111
  a=1: 00000000110011111111
  a=2: 11011100110011111111
  a=3: 00001100000011111111
  a=4: 00001100000010100000
  a=5: 00001100000010100000
There are exactly 6*5*4=120 ordered triples and 6*5*4*3*2=720 ordered five-tuples of distinct directions. Direct exhaustive substitution in the table shows for every distinct (a,b,c,d,e), the three bits f(a,b,c), f(b,c,d), f(c,d,e) are NEVER all equal. Thus a monochromatic center-z five-edge ordered-three-face geodesic cannot be forced by an arbitrary six-direction hub labeling.
SELF-CONTAINED VERIFIER (Python syntax):
B=['11001110110011111111','00000000110011111111','11011100110011111111','00001100000011111111','00001100000010100000','00001100000010100000']
def f(a,b,c):
    bs=[x for x in range(6) if x!=a]
    cs=[x for x in range(6) if x not in (a,b)]
    return int(B[a][4*bs.index(b)+cs.index(c)])
from itertools import permutations
assert all(len({f(a,b,c),f(b,c,d),f(c,d,e)})==2 for a,b,c,d,e in permutations(range(6),5))
The certificate demonstrates a precise limitation of purely hub-local extension from length four to five. It does not refute NORI, because globally a full six-edge one-switch path might exist through a different alignment or an external root exchange. It strengthens the motivation for root-coupled five-cycle overlap, antipodal compatibility, and the two-window seam extraction rather than an automatic greedy hub-local absorption.

## Dense antipodal certified-square geometry does not by itself force Tucker index two

This is a **combinatorial topological no-go model**, not a claim that its precise square family is realized by some active NORI coloring. It tests whether the new certified hub-square theorem's *abstract* local bounds alone suffice to force a nonzero second equivariant index.

Let \(n\ge5\) and choose two distinct coordinate directions \(i,j\). Build a cubical two-dimensional complex \(Y_{i,j}\subset[0,1]^n\) containing **all** cube vertices and edges and **all** ordinary coordinate two-faces **except** those whose two free coordinate directions are exactly \(\{i,j\}\).

**Theorem.** The complex \(Y_{i,j}\) has the following properties.

1. Every vertex's link is \(K_n\) with just the single edge \(\{i,j\}\) deleted. Thus every link has independence number \(2\le4\), there are no isolated coordinate directions, and the center-move graph is the **entire connected cube** \(Q_n\), of degree \(n\) at every vertex.
2. The cube antipodal involution acts freely on \(|Y_{i,j}|\), and \(Y_{i,j}\) has all but the \(2^{n-2}\) squares of one direction-pair class. In particular, this example is far denser and more connected than the universal \(n-3\) minimum-degree and link-independence constraints of the proved certified center-square complex.
3. **Nevertheless there is an equivariant continuous map**
\[
Y_{i,j}\longrightarrow S^1
\]
with the antipodal action on \(S^1\). Hence its cohomological antipodal-cover class \(w\in H^1(Y_{i,j}/\tau;\mathbb F_2)\) satisfies \(w^2=0\). Any attempt to force a two-dimensional Tucker/Borsuk–Ulam obstruction *merely* from cube-wide degree, \(\alpha(\operatorname{link})\le4\), dense squares, connectedness, and free antipodality is invalid.

**Proof.** At each vertex, an incident square with two free directions \(a,b\) contributes an edge \(\{a,b\}\) to the vertex's coordinate link. Precisely the pair \(\{i,j\}\) is missing; all cube edges remain. This proves (1) and the square count in (2). No cubical face of dimension at most two contains the geometric center \((\frac12,\ldots,\frac12)\) when \(n\ge3\), so the antipodal action is free.

Let \(\mathrm{pr}_{i,j}:[0,1]^n\to[0,1]^2\) be the projection to the selected coordinates. On every cell of \(Y_{i,j}\), at least one of \(i,j\) is **fixed at 0 or 1**, because the cells with both free have been deleted. Therefore the restricted projection lands in the **boundary of the square** \(\partial[0,1]^2\cong S^1\). It is continuous and respects coordinatewise complementation: \(\mathrm{pr}_{i,j}(\bar t)=\overline{\mathrm{pr}_{i,j}(t)}\). The involution on the boundary square is a half-turn, conjugate to the antipodal action on \(S^1\). This is the asserted equivariant map.

The quotient double cover of \(Y_{i,j}\) is the pullback along the quotient map of the universal antipodal cover of \(S^1\), whose first Stiefel–Whitney class generates \(H^1(S^1/\tau;\mathbb F_2)\). Therefore \(w\) is pulled back from a 1-dimensional circle and \(w^2=0\). \(\square\)

**Interpretation and repair target.** The all-dimensional *actual* certified-square complex from Item \`nori_certified_center_square_complex_high_degree_eight_components_20261008\` may carry additional global incidence restrictions not shared by this artificial model. But a proof invoking only its unconditional *link density and 2-dimensional cell count* cannot force a nonzero \(w^2\). To apply fixed-point topology, establish extra constraints on how **actual monochromatic ordered-three-face path certificates** on neighboring squares glue; or construct a compatible higher-dimensional carrier using root/terminal-memory witnesses whose topology cannot be collapsed by such a two-coordinate projection. A topological zero must still extract the precise same-root reversed-two-tail complementary-support pair (or a four-facet odd cap-memory cycle).

THEOREM (GLOBAL ROOT-COUPLED ANTIPODAL TOPOLOGY). Let n>=5, active NORI c(bar F,reverse pi)=1-c(F,pi). A physical cube edge is DEAD if no genuine monochromatic directed four-edge geodesic traverses it; dead edges form an antipodally invariant MATCHING. Let U⊆Q_n be the physical FULLY COVERED ROOT VERTICES incident to ZERO dead cube edges. Every incident physical edge at a vertex of U has some genuine monochromatic four-geodesic witness.
For each z∈D=Q_n\U there is exactly one dead incident edge, with a rigidity bit t(z). Its antipodal partner has t(bar z)=1−t(z). Crucially, for ANY z,w∈D of Hamming distance at most2, t(z)=t(w): if their dead edges have different directions, the existing NORI dead-direction separation theorem forbids endpoint-set distance<=2; if both have the same dead direction, their projected dead-edge positions are at distance<=2 and the same physical three-face omitting that direction forces equality. Hence antipodally opposite t-values NEVER occur within a two-dimensional physical cube face.
Let X be the τ-equivariant Freudenthal triangulation of the TWO-DIMENSIONAL CUBICAL SKELETON of the boundary of the geometric cube [0,1]^n. Its quotient is the 2-skeleton of RP^(n-1) in the induced cubical cell structure, so w1(X/τ)^2 !=0. Assign vertex scalar f(z)=(-1)^{t(z)} to dead-incident vertices z∈D, and f(z)=0 to the fully covered vertices z∈U. The antipodal coloring axiom makes f odd, and affine extension over Freudenthal simplices yields an odd PL function F:|X|→R. Every simplex of X lies inside a physical two-dimensional cube face, so any nonzero scalar vertex values all have the SAME sign. Accordingly the entire zero locus F^-1(0) is the literal INDUCED LIVE-ROOT SUBCOMPLEX |X[U]|, consisting of simplices all of whose physical cube vertices have complete monochromatic-four-geodesic coverage. No mixture of opposite bad-label values creates a spurious zero.
By the standard odd-scalar zero-index theorem, the nonzero second cover-class power of X forces w1(X[U]/τ) !=0. Thus the free antipodal space X[U] has index AT LEAST ONE and, in particular, possesses a connected component invariant under τ. Taking any genuine fully covered cube vertex x in this component yields a chain
  x=x0,x1,...,x_r=bar x
where EVERY x_j is an ACTUAL fully covered physical cube vertex (all n incident physical edges support monochromatic four-geodesic witnesses), and successive vertices x_j,x_(j+1) share one physical cube face of dimension≤2 and hence have Hamming distance at most2. This conclusion is strictly stronger than the previously proved unconditional fact that U merely meets every antipodal graph path.
SPECIAL SINGLE-DEAD-DIRECTION STRENGTHENING. If all dead cube edges, if any, have ONE common coordinate direction i, then t(z) is locally constant on D at physical Hamming distances<=3, by the same-direction dead-hub 3-face rigidity. Repeat the construction using the THREE-dimensional cubical skeleton of ∂[0,1]^n: this has w1^3 !=0 and its odd scalar zero locus is the induced fully covered root subcomplex X_3[U]. Consequently ind_Z2(X_3[U])>=2; there is an antipodally invariant connected component linked by Hamming-at-most-three steps and a nonzero square of the antipodal covering class. Under hypothetical NORI grand failure in n<=10, the previously proved mixed-dead-direction closure theorems say precisely that any dead edges must all share a single direction, so the stronger index-two root carrier is available in this entire low-dimensional counterexample regime.
LIMITATION. Simplicial edges of Freudenthal triangulations may be physical FACE DIAGONALS, not necessarily original Q_n graph edges; the antipodal chain is a chain of genuine covered cube roots with steps of Hamming distance<=2 (or<=3 in the single-direction strengthening), NOT automatically a cube-edge walk within U. Nor do the separately existing local four-geodesic witnesses have synchronized colors or ordered middle-pair memories. The theorem proves a global topological root carrier from actual ordered-face coloring constraints, not full NORI one-switch closure.

Strong edge coverage and connected certified-square complexes need not have the antipodal index required for global closure. The certificate must retain its path order, root and physical window labels.



---

## Retired Subsection: Maximal geodesic blockers and snake exchanges

Source ID: `maximal_geodesic_blockers_and_snake_exchanges`
Source Section: `nori_maximal_geodesic_exchanges`
Exact original Subsection composition: v2.

# Rooted blockers, physical exchanges, and the limit of support coverage

Let a legal NORI coloring assign bits to physical ordered three-faces with antipodal-reversal oddness. Good paths have at most one change. The following established lemmas separate rooted availability from globally compatible extension. They **do not** contradict the unrooted grand conjecture.

## Rooted short-path coverage without a full rooted path

THEOREM (legal NORI root with every short rooted path good and every full rooted path bad). For EVERY n>=6 there exists an antipodally reversal-odd binary coloring of physical ordered 3-faces of Q_n and a fixed cube root x=0 such that:
(i) EVERY directed geodesic starting at x and using k distinct coordinate directions, 3<=k<=floor(n/2)+1, has a three-window color word with AT MOST ONE switch;
(ii) EVERY FULL n-edge antipodal geodesic from that SAME root x has AT LEAST TWO switches, regardless of its direction order.
Moreover, in dimension n=7 every one of the 21 five-coordinate supports has at least one good rooted five-edge geodesic from x even though no full rooted path is good. For n>=8, every five-edge geodesic from x, on every support, is good.

PROOF. Let q=n-3 be the number of exterior fixed coordinates of a physical ordered three-face F; let z(F) be the number of exterior coordinates fixed to 1. Along ANY distinct-direction path rooted at x=0, the i-th ordered-three-face window (i starting at1) has precisely i-1 exterior 1 bits: all already traversed directions have become1 and all untraversed directions remain0. Thus z(F_i)=i-1 independently of direction order and support.

EVEN n=2m>=6: q=2m-3=2h+1 where h=m-2>=1. Define the symmetric-complement-odd layer table f on 0<=j<=q by f(0)=0, f(j)=1 for 1<=j<=h, and f(q-j)=1-f(j) for 0<=j<=h. Color EVERY ordered physical three-face by c(F,pi)=f(z(F)); the ordered triple is ignored. Since z(bar F)=q-z(F), the NORI axiom c(bar F,reverse pi)=1-c(F,pi) holds exactly. Every full path from root0 has window word 0,1^h,0^h,1, hence THREE switches. Every rooted path of length k<=h+3=m+1=floor(n/2)+1 reads just the initial segment f(0),...,f(k-3), namely 0 followed by 1s (possibly just0), and has at most one switch.

ODD n=2m+1>=7: q=2m-2=2h where h=m-1>=2. Prescribe f(0)=0, f(j)=1 for 1<=j<=h-1, and f(q-j)=1-f(j) for 0<=j<=h-1. At all exterior weights j!=h set c(F,pi)=f(j). On the self-complementary central weight j=h choose ANY tournament t on the n directions with t(a,c)+t(c,a)=1, and set c(F,(a,b,c))=t(a,c). The central ordered triple is reversal-odd by tournament skewness; all noncentral weights satisfy antipodal oddness by the layer complement prescription. Every full path rooted at0 has first two window colors f(0),f(1)=(0,1) and last two f(q-1),f(q)=(0,1), independently of its direction order and all central values. The first seam and last seam are therefore distinct mandatory switches, proving (ii). Every rooted k-edge path with k<=h+2=m+1=floor(n/2)+1 reads only weights 0,...,k-3<=h-1 and has color word 0 followed by 1s, proving (i).

SPECIAL Q7 STRENGTHENING: Here q=4,h=2. Every five-edge path from root0 has three colors (0,1,t(p_3,p_5)). Given ANY five-coordinate support B, select distinct a,c in B with t(a,c)=1; make them the third and fifth directions of the support path and arrange the other directions arbitrarily. Its word is (0,1,1), hence good. Thus ALL 21 five-supports have good rooted witnesses at x=0 while all full seven-edge paths from x remain bad.

SCOPE. These colorings are fully legal GLOBAL NORI colorings. Other starting cube vertices may have good full antipodal geodesics, as required by the grand conjecture. This theorem refutes every proposed implication of the form: simultaneous same-root good paths on every k-support, with k<=floor(n/2)+1, force a full same-root good path. It also refutes the all-21-five-support version in Q7. Any successful local-to-global proof must use terminal ordered-face memory, compatible phases, larger support, or change the starting root. This construction is a layer-weight obstruction and complements the team's rank-five common-root packing results.

## Sharp explicit Q7 certificate beyond the half-rank barrier

EXPLICIT FINITE CERTIFICATE (Q7 all proper supports good at one root; no full rooted good geodesic).

There exists a fully legal antipodally reversal-odd binary coloring c of ordered PHYSICAL three-faces of Q7 and a root x=0000000 such that:
(i) For EVERY nonempty proper coordinate support B subset of [7] with 3<=|B|<=6, at least one ordering p of B gives a rooted directed geodesic starting at x whose 3-window colors have at most ONE switch.
(ii) For EVERY full permutation p of [7], the actual rooted 7-edge antipodal path from x has AT LEAST TWO switches.
Thus even simultaneous same-root good paths on EVERY proper support, including all seven six-supports and all 21 five-supports, do not by themselves imply a full one-switch path rooted there. The construction respects every global NORI antipodal-reversal identity and is independently checked by a short exact enumerator.

COMPLETE COLORING CERTIFICATE. Represent each physical ordered face by key (t,z), where t is an ordered triple of distinct vertex direction labels 0..6, and z is an integer bitmask of fixed exterior coordinates equal to 1, z disjoint from the bits of t. Define its reversal-odd mate theta(t,z)=(reverse(t), ((1<<7)-1)^support_mask(t)^z). These 3360 ordered physical-face states form 1680 two-element orbits. Sort lexicographically the 1680 canonical representatives min((t,z),theta(t,z)). Assign to the j-th canonical representative the j-th little-endian bit in the following 210-byte BASE64 certificate (j=0 first bit). Give the other orbit member the complementary color.

BASE64:
AAAAAAAAAAAAAAEAAAAAAAAAAAABAAEAAAAAAAAAAQABAAAAAAAAAAEAAQABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIUBAIERARGAAQAAgACAAYAQgBSABIAFgRCAkIAAgACBAKAAgACAAYAAAAAAAAAAAAUBAIERARGAGIEYgRgBHIEcgRyBmIEYgRihGKEIoQiBAAAAAAAAGQEZARkBGIAYgBmBPIE8gTyAHKE4oTiBAAAAADyBPQE8gTyBHIE8gRyhOIEAAD0DPIM8ARyB

A PURE-PYTHON VERIFIER (no SAT solver):
import base64,itertools as it
Z='AAAAAAAAAAAAAAEAAAAAAAAAAAABAAEAAAAAAAAAAQABAAAAAAAAAAEAAQABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIUBAIERARGAAQAAgACAAYAQgBSABIAFgRCAkIAAgACBAKAAgACAAYAAAAAAAAAAAAUBAIERARGAGIEYgRgBHIEcgRyBmIEYgRihGKEIoQiBAAAAAAAAGQEZARkBGIAYgBmBPIE8gTyAHKE4oTiBAAAAADyBPQE8gTyBHIE8gRyhOIEAAD0DPIM8ARyB'
n=7; M=(1<<n)-1; reps=set()
for t in it.permutations(range(n),3):
    free=sum(1<<d for d in t)
    for z in range(1<<n):
        if z&free: continue
        mate=(t[::-1],(M^free)^z)
        reps.add(min((t,z),mate))
reps=sorted(reps)
assert len(reps)==1680
index={key:j for j,key in enumerate(reps)}
bits=int.from_bytes(base64.b64decode(Z),'little')
def color(t,z):
    t=tuple(t);free=sum(1<<d for d in t)
    key=(t,z);mate=(t[::-1],(M^free)^z)
    return ((bits>>index[min(key,mate)])&1) ^ int(key>mate)
def switches(p):
    prefix=0;w=[]
    for i in range(len(p)-2):
        w.append(color(p[i:i+3],prefix))
        prefix|=1<<p[i]
    return sum(w[j]!=w[j+1] for j in range(len(w)-1))
assert min(switches(p) for p in it.permutations(range(n)))>=2
for k in range(3,n):
    good_per_support=[
        sum(switches(p)<=1 for p in it.permutations(B))
        for B in it.combinations(range(n),k)
    ]
    assert min(good_per_support)>0
    print(k,len(good_per_support),min(good_per_support),max(good_per_support))

Output from independent verification:
  support length3: 35 supports, good permutation counts all 6;
  support length4: 35 supports, good permutation counts all 24;
  support length5: 21 supports, good permutations min 6, max 103;
  support length6: 7 supports, good permutations min 117, max 307.
  Full support7: exactly 5040 tested permutations, min switches2, max4, ZERO good.

This is a 1680-bit explicit globally legal coloring; all counts follow by exhaustive permutation enumeration with no solver trust required. The base64 string fixes the entire coloring uniquely.

STRATEGIC CONSEQUENCE. A proof based exclusively on requiring good partial paths on every proper support at the SAME ROOT is insufficient, even when the support rank is n-1 (Q7). Closing the grand conjecture needs shared ordered-terminal memory/phase compatibility or the freedom to change root and exchange full paths. This sharply strengthens the analytic half-rank all-short-path counterexample and the Q7 all-21-five-support obstruction documented in the companion Item nori_all_dimensions_same_root_every_half_rank_path_good_no_full_path_and_q7_all21_supports_20261009. The COLORING IS NOT A COUNTEREXAMPLE TO THE GRAND CONJECTURE: it rules out full paths at one fixed root, while the grand conjecture requires a good full path at some root.

EXPLICIT POSITIVE GLOBAL WITNESS FOR THE SAME COLORING. At a DIFFERENT root x=1 (bit0=1, other bits0) and full direction order p=(0,1,2,4,6,3,5), the certificate yields the actual physical full-window word (0,0,1,1,1), with exactly one switch. This was checked by extending the verifier's face address to z=(x XOR traversed_prefix_mask) AND exterior_coordinate_mask. Thus the finite construction explicitly demonstrates the necessity of root mobility and satisfies the grand conclusion for this coloring.

STRICT STRENGTHENING: BOTH monochromatic colors on EVERY smaller support. An INDEPENDENT SECOND globally legal physical Q7 coloring, encoded by exactly the same 1680-orbit canonical-bit prescription above, has the following simultaneous root x=0 properties:
  * For each of all35 three-supports, all35 four-supports, and all21 five-supports, at least ONE fully monochromatic rooted path of color 0 AND at least ONE fully monochromatic rooted path of color 1 exist.
  * For each of all7 six-supports, at least112 different rooted six-edge orders are at most one-switch good.
  * For each of all5040 full seven-direction orders, the rooted path has 2 to4 switches and NONE is good.
The second coloring has an explicit GOOD full path at a different root x=1 (coordinate0 initially1) with direction order (0,1,2,5,3,4,6) and true color word (1,1,1,1,0), one switch.

SECOND BASE64 ORBIT CERTIFICATE (210 bytes; replace Z in the complete pure-Python verifier above):
X81XzTYHw3dDgHTYC97CAXdSwrRYJ9M98FyHvUYxXJ1efk9ZdvXWBXdBEvkQ8TIFBXP2jaPQtl4WSJ5PkpWnpfbxf8lOvBBx9/YRjhPmv2zR/Vh4RT96/DKlciATlD6FtBFzt3EePbMrvnHZrdaibeo5jy+GFMoLVp/bdnNR9Up2Gn78Ki3St6IFjdbAllKcky7Svt9d4DTlzf69biRq9HgelWdjH6JB9hirDFRMVK9KNFPMqhCQnszdXRxHkkapUCFX/Nutkvy1kCW9MWlSPtKk

An additional independent check for BOTH monochromatic colors on each k-support, k=3,4,5: for every B in combinations(range(7),k), generate all permutations p of B, compute w=[color(p[i:i+3],sum(1<<d for d in p[:i])) for i in range(k-2)], and assert that an all-zero w and an all-one w each occur. Exact checked minima over all supports are 1 for each color at every k=3,4,5. Existing full and rank6 verifier loops on this second certificate return no full rooted one-switch order and six-support good-permutation counts ranging from112 to144. Thus even complete both-color monochromatic support COVERAGE through rank n-2, coupled to one-switch coverage at rank n-1, fails to force a full same-root good path. The missing ingredient is precise reversed-two-tail terminal memory and phase matching or a different starting root. This second witness substantially strengthens the support-level obstruction while satisfying global antipodal reversal.

## Local swaps and extremal terminal walls

# Physical adjacent-transposition localization

**Lemma.** In a physical k-edge direction-distinct cube geodesic P rooted at x, interchange consecutive directions p_i and p_(i+1) to obtain P'. Both paths have the same root, endpoint, and direction support. Their genuine ordered-three-face windows W_j are *identical as physical ordered faces* for all j outside [i-2,i+1] intersect [1,k-2]. Consequently their color words differ in at most four consecutive positions under an arbitrary active NORI coloring.

**Proof.** Both direction words flip the same coordinates. Their prefix vertices are identical up through step i-1 and again from step i+1 onward, because coordinate flips commute. Every triple window whose indices avoid i and i+1 has the same ordered directions and the same preceding prefix vertex, hence determines the same physical ordered face. The only potentially modified starts j obey j<=i+1 and j+2>=i. QED.

**Exchange application and scope.** An adjacent direction swap therefore preserves the entire certified color word outside one four-window interval; only that interval and its boundary color comparisons need rechecking. This provides an exact root- and support-preserving operation for studying globally maximal one-switch geodesics. It does not force an improving exchange, missing-coordinate extension, or grand closure.

# Global LONGEST ≤1-switch geodesics have two-sided antipodal snake blockers

Let n>=5 and c be arbitrary active NORI coloring of actual ordered 3-faces with c(bar F,reverse pi)=1-c(F,pi). Define a GOOD direction-distinct cube geodesic as one whose ordered three-face window color word has at most ONE change; no antipodality/ full dimension requirement for shorter paths. Assume the unrestricted GRAND conjecture fails. Choose P to have globally MAXIMUM edge length k among all GOOD geodesics in the whole Q_n (all roots, supports, direction orders). Then 4<=k<=n−1. Write
 P: x -- (p_1,...,p_k) --> y,
its ordered-three-face window colors as q repeated s times followed by r repeated t times, with s,t>=1 and q≠r, s+t=k−2. Let a=p_(k−1), b=p_k, initial α=p_1, β=p_2 and T=[n]\{p_1,...,p_k}, m=n−k>=1.

**THEOREM (TWO-SIDED GOOD-SNAKE BLOCKER LAW).** P NECESSARILY has EXACTLY ONE color switch. For every missing direction d∈T, the physical three-face windows at the two ends are FORCED:
   c(F_y({a,b,d});(a,b,d)) = q = 1−r;
   c(F_x({d,α,β});(d,α,β)) = r = 1−q.
Consequently the genuine full-direction-distinct (k+1)-edge geodesics
   P followed by d (root x) have color word q^s r^t q;
   d followed by P (root x xor d) have color word r q^s r^t.
Both have EXACTLY TWO switches, with the same ACTUAL interior P window colors. Their new root locations are distinct because prepending d begins at x xor d, and both paths are actual cubes, not abstract words. Under active antipodal reversal these blocked caps give the dual certified incoming and outgoing three-face fans:
   c(F_bar_y({a,b,d});(d,b,a))=r;
   c(F_bar_x({d,α,β});(β,α,d))=q.
The terminal r-colored opposite-corner incoming snake of P lies in a Boolean T-root cube, and the initial r-colored prepend 3-face fan is at the OTHER endpoint.

**PROOF.** If the maximal good P were MONOCHROMATIC, any unused direction d could be appended; it creates exactly one new window, so the resulting (k+1)-edge path would still have at most one switch, contradicting maximality. Hence P is genuinely q^s r^t with q≠r. Appending d creates exactly one new physical window (a,b,d). If this were color r, the longer path would still be good, contradiction. Therefore its color is 1−r=q. Prepending d from root x xor d creates exactly one new physical window (d,α,β) and leaves the original P window sequence on the SAME physical faces (because the new first step d ends at x); if it were q, the longer path would remain good, contradiction. Therefore its color is 1−q=r. Reversing at antipodal physical faces gives the dual colors. The proof uses neither any claimed long mono path nor a freely reorderable tail. QED.

**NEAR-FULL n−1 CASE.** If k=n−1 then T={d} and bar y=x xor d (since y=x xor ([n]\{d})). Thus the prepended full path d+P starts EXACTLY AT bar y, while the appended full path P+d begins at x. Their color words are forced r q^s r^t and q^s r^t q, respectively, with two switches. Meanwhile the global antipodal reversal ΘP starts at bar y and has complementary reversed window word q^t r^s. This gives a concrete *two-by-two antipodal rectangle of full/near-full cube paths* where the two end-caps are opposite phases. The geometry does NOT by itself imply a good full path, because the cap free-coordinate triples at two ends differ and their colors can be independently assigned consistently with the oddness axiom when all directions of P are distinct.

**EXACT LIMITATION.** A longest good path P gives an opposite-corner fan in its LAST phase r, whereas its FIRST phase q differs. In contrast to the monochromatic maximal-path fan, splicing a fan branch through P_s would generally make TWO switches, not one. Thus neither the maximal-q rank bound nor its top-rank extraction transfers automatically to globally maximal *good* paths. To find a genuine descent, use a new defect measure that tracks both phases and both endpoint ordered pairs.

**GLOBAL STRATEGIC VALUE.** This is the proper maximal-defect analogue of the Devine–Milans snake method, directly about the target property rather than only about monochromatic paths: a hypothetical counterexample produces mandatory, bidirectional, oppositely colored extension walls at BOTH ends of a globally longest good partial cube geodesic. Progress requires constructing an extension or root exchange that breaks one wall while preserving one-switch coloring. The theorem does not solve unrestricted grand closure.

## Logical boundary

Universal existence of good paths on proper supports, even at one root, does not imply a rooted full good geodesic. Nor do forced caps yield a globally decreasing exchange automatically: new seam windows are actual physical faces. An unrooted extraction mechanism may move roots and retain terminal-order memory. Further improvements to support counts should be interpreted only with such a mechanism.

## An all-dimensional flat worst-case exchange trap

**Theorem (strict adjacent-swap descent fails in every \(n\ge7\)).**
For every \(n\ge7\) there is a *position-independent*, antipodal-reversal-odd ordered-three-face coloring \(c\) and permutations
\[
p=(1,2,\ldots,n),\qquad
q=(1,3,5,\ldots;\ 2,4,6,\ldots)
\]
such that the window word of \(p\) and of *every one of its \(n-1\) adjacent transpositions* is the same maximally alternating word
\[
1,0,1,0,\ldots
\]
(of length \(n-2\), hence with \(n-3\) color changes), whereas the word of \(q\) is monochromatic. These assertions hold at *every* cube root. In particular, even permitting arbitrary starting-root changes alongside a single adjacent swap cannot guarantee a strict improvement in the number of switches, despite a globally optimal monochromatic full geodesic.

**Proof.**
Let \(\mathcal B=\{p,\tau_1p,\ldots,\tau_{n-1}p\}\). A triple \(t=(a,b,c)\) occurring as the \(i\)-th consecutive three-window in a member of \(\mathcal B\) has
\[
a+b+c\in\{3i+2,3i+3,3i+4\}.
\tag{E1}
\]
Indeed, the identity permutation has \((i,i+1,i+2)\) at that window, and an adjacent swap can change the sum of the three occupied labels by at most one. The three-element intervals in (E1) are disjoint for distinct \(i\). Thus each such *ordered triple* has a unique window index \(i(t)\). Prescribe
\[
h(t)=i(t)\pmod2\qquad(t\text{ occurring in }\mathcal B).
\tag{E2}
\]
Every member of \(\mathcal B\) has at most one inversion relative to the natural order of labels. Consequently each of its ordered triples has at most one inversion, while its reversal has at least two of the three possible inversions. Therefore no triple in \(\mathcal B\) is the reverse of another triple in \(\mathcal B\), and the assignments (E2) are consistent with
\[
h(c,b,a)=1\oplus h(a,b,c).
\tag{E3}
\]

Now put all odd labels in increasing order, followed by all even labels in increasing order, to form \(q\). For \(n\ge7\), the numerical span \(\max\{a,b,c\}-\min\{a,b,c\}\) of every consecutive triple of \(q\) is at least four: inside either parity block the three labels are spaced by two, and either of the two triples crossing the block boundary spans at least five. Conversely, every triple appearing in \(\mathcal B\) has numerical span at most three, since one adjacent swap changes only one boundary label of a consecutive triple. Thus none of \(q\)'s ordered triples, nor any of their reversals, has been assigned a value in (E2). Moreover, the consecutive triples of the single permutation \(q\) are distinct and never reversals of each other. Assign
\[
h(q_i,q_{i+1},q_{i+2})=0 \qquad(1\le i\le n-2).
\tag{E4}
\]
Finally extend \(h\) to all ordered triples, choosing one bit arbitrarily in each still-unassigned reversal pair and assigning the complementary bit to the reversed triple.

Define \(c(F,(a,b,c))=h(a,b,c)\) independently of the physical face's exterior bits. Equation (E3) is exactly the NORI antipodal-reversal law for this coloring. Equations (E1)–(E2) give alternating words for \(p\) and every immediate swap neighbor; equation (E4) gives a monochromatic word for \(q\). Exterior-independence makes all statements uniform in the starting vertex. \(\square\)

**Scope and obstruction.**
The theorem disproves the universal *strict local descent* implication
\[
\exists\text{ a good full geodesic}
\quad\Longrightarrow\quad
\forall\text{ bad }(x,p)\ \exists\,x',j:
\operatorname{switches}(x',\tau_jp)<\operatorname{switches}(x,p).
\]
It does **not** exclude neutral-step sequences, exchanges that change several positions, a different global potential, or an antipodal/topological forcing mechanism. In particular, any general exchange proof must tolerate arbitrarily high-defect one-move plateaus; the obstruction holds in every ambient dimension and already in the exterior-independent class.




---

## Retired Subsection: Bichromatic root diamonds and mixed terminal cap obstruction

Source ID: `bichromatic_root_diamonds_and_mixed_terminal_cap_obstruction`
Source Section: `nori_connector_root_hubs`
Exact original Subsection composition: v1.

# Bichromatic root diamonds and mixed terminal cap obstruction

Suppose a cube root lies on monochromatic four-edge geodesics of both colors. Their root-square certificates form an opposite-color diamond. At its boundary, the two ordered terminal windows can obstruct one another, and maximality of the monochromatic branches imposes strong local color equalities on mixed-class caps.

## Actual physical-face transposition blockers for opposite-color same-root reversed-tail diamonds

Let n>=5 and let c be ANY binary coloring of physical ordered 3-faces (antipodal oddness not needed). Suppose two GENUINE length-four MONOCHROMATIC geodesics begin at SAME ROOT x, end at SAME PHYSICAL ENDPOINT y, have four pairwise distinct used directions a,b,c,d and specifically direction orders
  P0=(c,a,b,d), color 0 in BOTH windows,
  P1=(a,c,d,b), color 1 in BOTH windows.
These are exactly the two-color diamonds constructed in NORI's item nori_bichromatic_hub_same_root_reverse_tail_opposite_color_diamond_20261008 at a bichromatic hub when opposite-color common-edge certificates are absent. The common midpoint hub is z=x xor {a,c}, and y=x xor {a,b,c,d}. The first TWO and last TWO directions are swapped between the two paths.

Fix ANY fresh unused coordinate e∉{a,b,c,d}.

**Theorem 1 (exact append blocker).** Appending e to P0 and P1 gives two ACTUAL length-five geodesics with window-color words respectively
  (0,0, A_e),  where A_e = c(F(y;{b,d,e}),(b,d,e)),
  (1,1, B_e),  where B_e = c(F(y;{b,d,e}),(d,b,e)).
Crucially, A_e and B_e refer to two ORDERS OF THE SAME PHYSICAL THREE-FACE through their COMMON endpoint y. If neither length-five extension is monochromatic, then
  (A_e,B_e)=(1,0).
If the two order colors are equal, at least ONE extension is monochromatic; if (A_e,B_e)=(0,1), BOTH are monochromatic.

**Theorem 2 (exact prepend blocker).** Prepending e to P0 and P1 gives two ACTUAL length-five geodesics with window-color words respectively
  (C_e,0,0), where C_e=c(F(x;{a,c,e}),(e,c,a)),
  (D_e,1,1), where D_e=c(F(x;{a,c,e}),(e,a,c)).
Again C_e,D_e are two ordered colors on the SAME PHYSICAL three-face, now through common root x. If neither prepended length-five path is monochromatic, then
  (C_e,D_e)=(1,0).
Equal order colors guarantee at least one monochromatic extension; (0,1) guarantees both.

**Proof.** For append, the only new color window consists of the last two directions of P0/P1 followed by e, respectively (b,d,e) and (d,b,e), whose physical free-face has common endpoint y. The first two window colors are 0,0 and1,1 by hypothesis. Appended path monochromatic iff A_e=0 for P0 and iff B_e=1 for P1; simultaneous failure iff (1,0). For prepend, the new window has e followed by first two directions of each path, respectively (e,c,a) and (e,a,c), and through same root x. Prepend P0 stays monochromatic iff C_e=0 and prepend P1 stays monochromatic iff D_e=1; simultaneous failure iff (1,0). QED.

**Corollary 3 (active NORI no-grand constraints in dimension n=6).** In Q_6 a length-five monochromatic directed geodesic can be extended via its only unused coordinate to a FULL one-switch antipodal geodesic, irrespective of the last window color. Hence if the ACTIVE grand conjecture hypothetically fails in Q_6 and a two-color four-edge diamond as above exists, for BOTH unused coordinates e,f it is NECESSARY that at the relevant physical faces:
  c(F(y;{b,d,e}),(b,d,e))=1,
  c(F(y;{b,d,e}),(d,b,e))=0,
  c(F(x;{a,c,e}),(e,c,a))=1,
  c(F(x;{a,c,e}),(e,a,c))=0,
and likewise substituting f for e. These are four precise ordered-face transposition defects per unused direction. They are compatible with the active antipodal reversal law locally; no false contradiction is claimed.

**Corollary 4 (higher-dimensional conditional extension).** If n>6 and an opposite-color rank-(n−2) geodesic diamond can be constructed with two distinct final ordered directions swapped between its colors, then an equal-color pair on EITHER shared physical extension face (root or endpoint) produces a MONOCHROMATIC (n−1)-edge path. Extending by the final unused direction gives grand closure. The theorem therefore identifies an exact physical three-face adjacent-transposition obstruction to lifting a color-flexible diamond across its remaining coordinates. A general existence theorem for such near-spanning diamonds is NOT known.

**Research strategy.** The present color-free reachability diamond provides same-root SAME-SUPPORT reversed tails. To upgrade it into a complementary-support grand witness, attempt a sequence of actual root/terminal-order exchanges that either (i) extends one of the mono colors by a fresh coordinate (eliminating a terminal tail), or (ii) accumulates transposition defects whose antipodal sign product around a closed compatible memory cycle is odd. The local blockers alone do not close grand NORI.

## A bichromatic hub forbids every monochromatic near-spanning core across each mixed omitted pair in a counterexample

Fix an active NORI ordered-three-face coloring of \(Q_n\), \(n\ge6\). Assume the **no-common-colored-certified-edge** alternative B of the square-edge-shadow dichotomy, so the connectedness theorem supplies a *bichromatic hub* \(z\) and two disjoint sets \(A,B\subset[n]\) of certified middle-edge directions of colors \(0,1\), respectively, \(|A|,|B|\ge2\), with at most one remaining isolated direction. The proved mixed-class selector rigidity says that every actual ordered face through \(z\) with middle free direction in \(A\) or \(B\), and one outer direction in the opposite class, has color equal to the middle-direction class.

**Theorem (all cross-pair codimension-two caps are uniform; immediate extension).** Choose **any** \(a\in A\), \(c\in B\) and write
\[
U=[n]\setminus\{a,c\},\qquad r=z|_U.
\]
For each \(i\in U\) and **every** cube vertex \(x_t\) whose \(U\)-coordinates equal \(r\) (the four choices of the omitted \(a,c\) bits), the genuine geometric cap labels obey
\[
\boxed{
c(F(x_t;\{a,c,i\}),(a,c,i))=1,\qquad
c(F(x_t;\{a,c,i\}),(c,a,i))=0.}
\tag{1}
\]
The values are independent of \(i\) and the two omitted-coordinate exterior assignments. Consequently **any monochromatic \((n-2)\)-edge geodesic** spanning all coordinates in \(U\), rooted at any \(x_t\) above projected root \(r\), forces a full NORI antipodal geodesic with at most one change.

**Proof.** Both cap faces in (1) have free coordinates \(\{a,c,i\}\), so varying the \(a,c\) bits of \(x_t\) leaves each physical face literally unchanged. At \(z\), the first ordered triple has middle direction \(c\in B\) and adjacent outer direction \(a\in A\), so its color is 1 by the mixed selector. The second has middle direction \(a\in A\) and adjacent outer direction \(c\in B\), so its color is 0. This proves (1).

Let \(P\) be any monochromatic \(U\)-spanning geodesic, with color \(q\), rooted at \(x_t\), first direction \(i\), last direction \(j\). If \(q=0\), **prepend** the omitted directions in order \((a,c)\) to \(P\), choosing the new root \(x_t\oplus e_a\oplus e_c\) so that the resulting path reaches \(x_t\) after the first two steps. Its first three window colors are \((1,s,0)\) for some \(s\in\{0,1\}\), and every later window is 0. The word changes color exactly once regardless of \(s\). If \(q=1\), instead **append** the omitted directions in order \((c,a)\) after \(P\). Its last three window colors are \((1,s,0)\), using the cap reversal-odd identity
\[
c(F(y_t;\{j,c,a\}),(j,c,a))
=1-c(F(x_t;\{a,c,j\}),(a,c,j))=0,
\]
where \(y_t=x_t\oplus\chi_U\) is the endpoint of \(P\) and the opposite physical face is used; all earlier windows are 1. Thus again exactly one change occurs. Both extensions use each coordinate exactly once. \(\square\)

**Corollary (uniform forbidden four-facet bundles under hypothetical grand failure).** If the grand conjecture fails and alternative B holds, then for **every** bichromatic hub \(z\) and **every** cross-class pair \(a\in A(z)\), \(c\in B(z)\), none of the four \(U\)-parallel facets based at projected root \(z|_U\) contains a monochromatic full \(U\)-geodesic **from its projected root**. Equivalently the four-facet monochromatic first–last memory graph \(\mathcal H_U(z|_U)\) is **empty**, not merely bipartite. In particular, there are at least \(|A||B|\ge2(n-3)\) distinct forbidden omitted-coordinate pairs (because \(|A|,|B|\ge2\) and \(|A|+|B|\ge n-1\), the product is at least \(2(n-3)\)) at each such hub.

This is a substantial strengthening of the generic four-facet cap-memory odd-cycle criterion: *every* near-spanning monochromatic core with a cross-class omitted pair is a grand-closure certificate, irrespective of its first and last directions or color.

**Exact open forcing implication.** The theorem does not supply a near-spanning monochromatic geodesic in any chosen facet; arbitrary ordered-face colorings can lack such paths at prescribed roots. A dimension-independent grand proof would follow if the physical-face incidences and antipodal symmetry guaranteed that at some bichromatic hub of alternative B, at least one of these \(4|A||B|\) root/facet cases has a monochromatic \(n-2\)-direction geodesic. The theorem isolates a concrete *global monochromatic-core transversal problem* in place of the broader one-change condition.

## Higher-index NORI forcing is an ANTIPODAL PATH of doubly certified physical edges, not merely one overlap edge

Let X be a finite regular CW (in particular simplicial/cubical) complex with a free cellular involution τ, and suppose X=A∪τ A, for subcomplex A; put C=A∩τA (automatically τ-invariant).

**GENERAL THEOREM (componentwise equivariant two-shore bridge).** If every CONNECTED COMPONENT of C is distinct from its τ-image, then there is a τ-equivariant continuous map X→S¹ (target antipodal). Consequently w_1(X/τ)²=0. Its contrapositive is
  w_1(X/τ)² !=0
    => SOME connected component of C is τ-INVARIANT.
This conclusion is strictly stronger than the preceding theorem nori_equivariant_two_shore_overlap_dimension_bounds_antipodal_index_20261008 when C contains many edges and cells yet its components all occur in antipodal pairs. No upper dimension bound on C is needed.

**Proof.** The finite complex C has finitely many connected components, each a closed and open subcomplex. By hypothesis τ pairs them with no fixed component. Choose one component from each τ-pair and assign constant value +1 to all its points; assign −1 on the image component. This is a continuous equivariant map g:C→S^0={−1,+1}. Embed S^0 as the two boundary endpoints of a closed upper semicircle H_+⊂S¹. Because H_+ is homeomorphic to an interval, the map g extends continuously from C to A with image in H_+ (either by barycentric interpolation on a triangulation of A or the elementary Tietze theorem for finite polyhedra). Write G:A→H_+ for this extension. On τA define F(x)=−G(τx), mapping to the opposite lower semicircle. On C the prescriptions agree: −G(τx)=−g(τx)=g(x)=G(x). The gluing lemma gives continuous F:X→S¹, satisfying F(τx)=−F(x). Pulling back the antipodal S¹ double cover implies w_1²=0 on X/τ. QED.

**NORI APPLICATION (actual two-color overlap geometry).** In an active NORI coloring n>=5, let X=X_c be the genuinely certified-center square complex, let A=X_0 be the subcomplex containing all physical cube vertices and all actually color-0-certified middle-pair squares and their boundary edges, and τA=X_1 be the corresponding color-1 complex. The overlap
  C=X_0∩X_1
contains ALL cube vertices; its one-skeleton consists EXACTLY of physical cube edges e for which K(e)={0,1}, i.e. edges lying in honest centered mono-four middle-pair squares of BOTH colors. A square of X is in C iff it has both color certificates; any such square has all boundary edges doubly certified. Therefore connectivity of C is equivalent to connectivity of this PHYSICAL BICHROMATIC COMMON-EDGE GRAPH H whose vertex set is all physical cube vertices and whose edge set is {e:K(e)={0,1}}.

**COROLLARY (higher index forces an antipodal chain of genuine color-flexible edges).**
If
   w_1(X_c/τ)^2 !=0,
then for some actual cube vertex z, there is a sequence
  z=z_0,z_1,...,z_m=bar z
of adjacent physical cube vertices such that EVERY physical edge {z_(j−1),z_j} is certified by a genuine monochromatic centered four-edge geodesic of color0 AND (possibly different) one of color1. As z and bar z differ in ALL n coordinates, necessarily m>=n. The chain can reuse coordinate directions; it is NOT automatically geodesic or witness-compatible.

**Proof.** The general theorem supplies a τ-invariant connected component C0 of C. Pick any physical vertex z in C0 (every nonempty subcomplex component contains vertices). Because τC0=C0, its antipode bar z also lies in C0. Connectivity of a finite CW complex implies connectivity of its 1-skeleton: cell attachments of dimension at least2 cannot connect distinct 1-skeleton components. Thus z and bar z are joined by a path in the 1-skeleton C0^(1), precisely the doubly-certified physical edges. Hamming distance between endpoints is n, so every such edge path has length >=n. QED.

**Position in the NORI program.** This isolates a very tangible topological-to-combinatorial task. A proof forcing w_1² nonzero would guarantee a FULL ANTIPODAL CHAIN of opposite-color certificates, not only a local bichromatic edge. To close the GRAND geodesic conjecture, one would still need a directional-no-repeat, ordered-terminal-memory coherent extraction from that chain (or find a different higher-index carrier if the actual X_c has index one, as the valid coordinate-only no-go example shows). No universal positive w_1² is claimed.

These diamonds provide many genuine short paths, but a monochromatic long core exists only when its terminal cap agrees with one of the diamond branches. The exact incompatibility conditions are preserved rather than silently filled by a color-only argument.
