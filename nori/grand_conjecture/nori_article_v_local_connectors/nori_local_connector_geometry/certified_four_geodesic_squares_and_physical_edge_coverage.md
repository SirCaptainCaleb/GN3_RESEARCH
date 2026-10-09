# Certified four-geodesic squares and physical edge coverage

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
