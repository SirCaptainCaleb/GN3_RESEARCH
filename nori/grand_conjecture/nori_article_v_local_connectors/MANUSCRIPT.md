# Article V — Local connectors and exchange geometry

## Article synopsis and main argument

# Certified connectors and extremal geodesic exchanges

Let c be a binary coloring of actual ordered three-faces of Q_n with c(bar F,rev pi)=1-c(F,pi). A k-edge direction-distinct cube geodesic has k-2 ordered-face window colors; call it good when there is at most one change. We study genuine local monochromatic connectors and global consequences of choosing a maximal good path.

## Dead edges force transverse monochromatic geometry

A physical cube edge is live if some monochromatic four-edge geodesic traverses it, and dead otherwise. Let e={z,z xor e_i} be dead. The dead-edge rigidity theorem asserts that every ordered physical three-face through either endpoint whose free directions avoid i has one common color q, independent of their direction order. Accordingly choose any k distinct directions avoiding i, with 3<=k<=min(n-1,6), and root their k-edge path so an endpoint of e lies in its central window overlap. Every length-three window then contains that vertex and has color q. This gives genuine monochromatic six-edge paths through dead-edge endpoints when n>=7.

For n>=8, each eight-dimensional coordinate facet containing e inherits a dead edge. The dimension-eight dead-edge bootstrap supplies a full good eight-edge path inside that facet. Appending the remaining n-8 unused coordinates creates at most n-8 additional color changes, giving a full n-edge path with at most n-7 changes. This is a global quantitative bound conditional on a dead edge.

## Bichromatic diamonds and the seam formula

Suppose two monochromatic four-edge geodesics of opposite colors run between the same roots along two distinct orders of a four-direction support. Appending a fresh direction e gives one new ordered three-face window for each candidate path. These cap windows may be different orders of the same physical face, so their colors are separately constrained rather than dictated by the original monochromatic runs. Under appropriate maximality the forbidden extensions yield precise opposite-color cap equations.

Now take two full antipodal geodesics rooted at x whose prefixes of length ell use the same set S. Both reach the physical vertex y=x xor S. Every choice of either prefix with either complementary suffix is a genuine full geodesic. If a prefix ends (u,v) and a suffix starts (w,t), their concatenation has exactly two new seam windows,
c(F_y({u,v,w});(u,v,w)) and c(F_y({v,w,t});(v,w,t)).
All other windows lie strictly inside the original prefix or suffix. Thus an attempted monochromatic two-tail splice reduces to two actual physical color checks. Connector abundance or a midpoint crossing is not sufficient until these checks are certified.

## Longest good paths have forced two-sided walls

Assume the grand conjecture fails and choose globally longest good partial geodesic P, length k<n, with ordered word q^s r^t, where q≠r. It must have exactly one change: appending any unused direction to a monochromatic P would still be good. Let its initial pair be (alpha,beta) and last pair (a,b). For each unused d, the physical appended cap (a,b,d) has color q, and the prepended cap (d,alpha,beta) has color r. Otherwise one extension remains good. Both extensions therefore have two changes, with words q^s r^t q and r q^s r^t. Antipodal reversal transfers these walls to the opposite cube roots.

A separate globally longest q-monochromatic path forces opposite-corner q-colored three-edge fans, indexed by all missing directions. Pairwise merged roots form a Johnson graph on two-subsets of missing directions. Their first-window colors can be prescribed independently in legal physical colorings, explaining why the root geometry alone gives no global merge. Nevertheless a seam direction with two certified q windows forces an entire row of monochromatic four-edge opposite-corner branches by maximality: otherwise a longer monochromatic path would exist.

Swapping adjacent travel directions preserves every physical three-face window except at most four consecutive positions. This sharply localizes the certificate check for exchanges. The missing global lemma is a terminating exchange rule or a connector selection theorem that forces one full good path from the two-sided walls and genuine cap geometry.

## Local monochromatic connectors, certified squares, and dead-edge rigidity

# Certified squares, dead-edge rigidity, and monochromatic hubs

A physical cube edge is called *live* if some genuinely monochromatic four-edge geodesic traverses it, and *dead* otherwise. These notions depend on actual ordered-three-face colors, not merely on an edge shadow assigning one arbitrarily selected color to each edge. Under NORI antipodal-reversal oddness, certified short paths organize into antipodally related physical root squares, and dead edges exhibit strong local rigidity.

## Local rigidity converts missing certificates into long ones

**Theorem 1 (dead-edge hub lemma).** Let \(n\ge7\). If an edge \(e=\{z,z\oplus e_i\}\) is dead, there is a bit \(t\) such that at either endpoint \(h\) of \(e\), every ordered three-face through \(h\) with free triple avoiding direction \(i\) has color \(t\). Consequently \(h\) lies on monochromatic six-edge geodesics in any chosen six distinct directions avoiding \(i\), with its position among their vertices chosen so every three-direction window contains \(h\).

**Proof.** If two such local ordered faces of different colors met through the same endpoint in an admissible four-move gallery passing through \(e\), a cyclic five-direction exchange would supply a monochromatic four-edge witness traversing \(e\), contradicting deadness. Propagating this constraint around the three-face incidence links gives a common bit \(t\) for all triples avoiding \(i\). Choose six other directions \(p_1,\ldots,p_6\) and any root \(h\oplus\{p_1,p_2,p_3\}\); the directed geodesic through \(h\) after three moves has each consecutive three-window spanning \(h\). Every such window has color \(t\), so the full six-move word is monochromatic. \(\square\)

For \(5\le n\le7\), a similarly placed spanning path already yields the requested zero- or one-switch antipodal geodesic. In larger dimensions the six-move hub is a certified local component, not by itself a full-dimensional solution.

## Geometry of the certified root-square carrier

The dead edges form a matching: if two adjacent cube edges were both dead, their common physical three-face exchange links would force one of them into a monochromatic four-geodesic. Accordingly every antipodal path has live-edge opportunities, and the set of completely four-geodesic-covered roots separates some dead-edge regions. Under the ordered-face reversal law, centered five-window parity also creates physical certified squares, often in both colors; these squares form honest two-dimensional carriers with constraints on their antipodal connectivity and local degree.

If a hub supports both monochromatic colors, the overlap gives a *bichromatic root diamond*: two real short path families with compatible root-square incidence, but potentially incompatible outward terminal colors. The exact two-ended cap equalities force either a short one-switch six-geodesic or a rigid mixed-color obstruction. The latter cannot be ignored when extending a short hub path to a full geodesic.

## Transposition descent and near-midpoint defects

Swapping adjacent directions of a full order changes only the three-window comparisons local to the exchanged directions. When a dead-edge incidence is present, the admissible swaps can be chosen not to increase total defect. Repetition yields normal forms where interior dead-edge obstacles have been eliminated and any obstruction remains near a terminal cap. This is a structural reduction, not a global one-switch theorem: a path can still have several changes in its live interior.

Likewise, high-index permutation topology guarantees genuine paths through near-midpoint physical hubs, but meeting at the same hub with opposite central labels does not suffice for a one-switch splice. There are legal local root rectangles in which both original paths and both exchanges retain three changes. Each proposed repair must check both new ordered-three-face seam windows, with their correct fixed exterior bits.

Thus certified squares and dead-edge rigidity give two complementary sources of control: short monochromatic geodesics in the presence of dead edges, and dense genuinely certified carriers when few are dead. The remaining closure problem is to connect their paths through valid two-window seams without accumulating further defects.

### Certified four-geodesic squares and physical edge coverage

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

### Covered-root separators and live-edge antipodal carriers

# Covered-root separators and live-edge antipodal carriers

Certified physical squares cover parts of the cube and identify vertices through which genuine monochromatic four-path witnesses pass. The geometry of uncovered edges constrains root separators, while two-color witnesses can organize into antipodally invariant carriers. The purpose here is to pass from local certification counts to a genuine path-relevant global separator.

THEOREM A (RADIUS-THREE CONSTANCY ACROSS DIFFERENT DEAD DIRECTIONS). Let n>=5 and let c be an active NORI antipodal-reversal-odd coloring of ordered physical 3-faces. Let M be the set of DEAD physical cube edges, namely those traversed by no monochromatic directed 4-edge geodesic. M is a matching. For each vertex z incident to a dead edge e in coordinate i, denote by t(z) its unique DEAD-EDGE RIGIDITY BIT: all ordered three-faces through z omitting i, or having i in the middle, have color t(z), while those with i first or last have color 1-t(z). Both endpoints of the same dead edge have the same t. Then for ANY two dead-incident cube vertices z,w with d_H(z,w)<=3, one has t(z)=t(w), REGARDLESS of whether the two dead edges have the same or different directions.
PROOF. If both dead edges use the same direction i, their two projected positions in Q_(n-1) differ in at most 3 coordinates. Choose one endpoint of each edge with matching i-bit; the two endpoints lie in a physical three-face with free directions equal to their at-most-three exterior differing coordinates, padded to three distinct non-i directions as needed. The ordered color of this face at either endpoint is the respective dead rigidity bit (i omitted), so they are equal. If the dead edges use distinct directions i,j, the proved dead-direction separation theorem says their ENDPOINT SETS have distance >=3. In particular d_H(z,w)<3 is impossible. If d_H(z,w)=3, write S=supp(z xor w), |S|=3. If i∈S, the other endpoint z xor i of the i-dead edge lies at distance2 from w, forbidden. Thus i∉S. Similarly j∉S. Therefore the ordered physical 3-face with free triple S contains both z,w and omits both i,j, so its single color is both t(z) and t(w). QED.
THEOREM B (UNCONDITIONAL FULLY COVERED ROOT INDEX TWO). Let U={z∈Q_n:z is incident to NO dead physical cube edge}; each of its n incident edges lies on at least one actual monochromatic four-edge geodesic. Let X be the Freudenthal triangulation of the 3-dimensional cubical skeleton of the geometric n-cube boundary ∂[0,1]^n, centrally inverted by τ(z)=bar z. The quotient X/τ is the 3-skeleton of RP^(n-1) under its induced CW decomposition, and its double-cover class w satisfies w^3!=0. Define odd scalar vertex labeling f(z)=0 if z∈U and f(z)=(-1)^t(z) otherwise. By active NORI antipodal reversal, t(bar z)=1-t(z), so f(bar z)=-f(z). Extend affinely on Freudenthal simplices. Every simplex has its cube vertices in one physical 3-face, so all nonzero labels are equal-sign by Theorem A. Therefore its ZERO LOCUS is EXACTLY the simplicial subcomplex X[U] induced by REAL fully certified physical cube roots: no affine cancellation among opposite forced bits. The odd scalar zero-set index-drop lemma yields w1(X[U]/τ)^2!=0, or equivalently ind_Z2(X[U])>=2, for EVERY active NORI coloring, WITHOUT a common-dead-direction hypothesis.
In particular some component of X[U] is antipodally invariant, and there is an actual vertex chain z=z0,...,zr=bar z of fully certified roots with successive Hamming distances at most THREE (possibly using face diagonals as simplicial edges). The nonzero second power is strictly stronger than connectedness or the previously proved index-one two-skeleton carrier. If M is empty, f≡0, X[U]=X, so the same conclusion holds (in fact index>=3).
PHYSICAL LIMITATION. The adjacent root vertices in this chain have individually actual local four-geodesic witnesses, but those witnesses need not have the same color or the same ordered two-direction memory and steps of Hamming distance 2 or3 are not necessarily cube edges. The index-two topology does not alone imply a full antipodal geodesic with at most one color change. It is an exact globally equivariant certified-root carrier available in ALL dimensions and ALL active NORI colorings, improving the conditionally stated one-dead-direction variant in nori_fully_covered_root_vertex_two_skeleton_index_one_antipodal_20261008.

THEOREM (NEW DENSITY LOWER BOUND FOR COMPLETELY FOUR-WINDOW-CERTIFIED ROOTS). Let n>=5 and color actual physical ordered three-faces of Q_n with active NORI antipodal-reversal oddness. Let M be the matching of DEAD physical cube edges traversed by no genuinely monochromatic 4-edge directed geodesic. Let D be the set of cube vertices incident to dead edges (so |D|=2|M|), and U=Q_n\D the FULLY CERTIFIED vertices, each incident physical edge lying on at least one actual mono4 path. The strengthened universal dead-rigidity radius-three theorem implies a thickness-three antipodal separator: EVERY full antipodal directed n-geodesic starting in D encounters at least THREE CONSECUTIVE vertices of U.
In contrast, every full antipodal geodesic starting in U automatically contains at least TWO U vertices—its root x and its antipode bar x—because U is antipodally invariant. Choose the starting root uniformly among all 2^n cube vertices and the full coordinate permutation uniformly among n!. Let N(P) be the number of U vertices visited along the resulting full antipodal geodesic, counting both endpoints. Conditioning on the root type gives
 E[N(P)] >= (3|D|+2|U|)/2^n.
But each of the n+1 vertex positions of a uniform rooted full geodesic is UNIFORMLY distributed over Q_n, so exactly E[N(P)]=(n+1)|U|/2^n. Comparing and substituting |D|=2^n−|U| yields
 (n+1)|U| >=3(2^n−|U|)+2|U|,
 and hence
    BOXED |U| >= ceil(3*2^n/(n+2)).
Because U is antipodally paired, the sharper integral form is |U| >=2 ceil(3*2^(n−1)/(n+2)). Equivalently, the number of physical dead edges is bounded above by
    |M| <= 2^(n−1)*(n−1)/(n+2),
with the appropriate integer/even rounding.
This improves the earlier antipodal one-point hitting-set density bound |U|>=ceil(2^n/(n+1)) and is derived from a genuine three-vertex physical-separator constraint, not an abstract topological index or heuristic random choice. Every U vertex has n individually witnessed monochromatic-four-geodesic incident edges, so the bound guarantees an unconditional DIMENSION-DEPENDENT MINIMUM AMOUNT OF CERTIFIED LOCAL PATH GEOMETRY in any NORI coloring.
SCOPE. The three certified consecutive vertices on a path do not guarantee that their separate local mono4 certificates have matching ordered two-direction memories or one color. The theorem does not prove a full <=1-switch antipodal path; it quantitatively strengthens the physical substrate for a possible root-coupled connector construction.

## A six-comparison proof that a direction cannot be globally uncertified

This is an ALTERNATIVE SHORT PROOF of the global missing-direction exclusion already established in Item nori_certified_square_complex_connected_antipodal_one_class_20261008, Theorem 3. It avoids constructing or proving connectedness of the entire middle-direction window shift graph H_i. Together with that Item's independently proved seven-cycle/minimum-degree lemma, it yields its established connectedness theorem. It is NOT a new claim of connectedness.

Let n>=5, and c be a physical ordered-three-face coloring obeying c(bar F,reverse pi)=1-c(F,pi). Fix a coordinate i. Suppose there is no monochromatic centered four-edge connector whose two middle directions include i. Then for every physical hub z and distinct coordinates a,b,c,d with i in {b,c}, the actual face colors h_z(a,b,c) and h_z(b,c,d) are different.

**Exterior-bit independence.** Under this supposition, every ordered face containing i is independent of each of its exterior fixed bits. For an exterior direction d and distinct other directions a,b, use the following comparisons:
 (a,i,b) versus (i,b,d),
 (a,b,i) versus (b,i,d),
 (d,i,a) versus (i,a,b).
These are actual centered four-geodesic comparisons, each with i in the middle pair and hence with unequal colors. Change ONLY the hub bit z_d. The compared window having d FREE remains the SAME physical ordered face and retains its color; therefore the other window, which has d fixed, must also retain its color. This works for every d not in the triple and for all positions of i. Thus define h(a,b,c) as the physical-face-independent color on each ordered triple containing i. Active antipodal reversal now imposes h(c,b,a)=1-h(a,b,c).

**Six-comparison certificate.** Choose a,b,d,e pairwise distinct and outside i, and take
 T0=(i,a,b), T1=(d,i,a), T2=(b,d,i),
 T3=(d,i,e), T4=(i,e,b), T5=(a,i,e), T6=(b,a,i).
The six successive comparisons are respectively supplied (in either direction) by the actual four-direction words
 (d,i,a,b), (b,d,i,a), (b,d,i,e),
 (d,i,e,b), (a,i,e,b), (b,a,i,e).
Every four-word has i among its two middle coordinates, so each step flips the bit h. Six steps yield h(T0)=h(T6). Since T6 is EXACTLY the reverse of T0, the antipodal-reversal oddness says h(T6)=1-h(T0). Contradiction.

**Conclusion.** Every coordinate i occurs as the middle direction of an ACTUAL monochromatic four-edge connector somewhere in Q_n. Combining this with the existing seven-window proof that at most one direction is isolated in each certified-square link, and the cube isoperimetric equality classification, recovers the known global connectedness of the certified-square complex for all active NORI colorings, n>=5.

**Role.** A finite six-shift reversal certificate replaces the larger H_i connectivity-and-bipartition argument for excluding a globally missing coordinate. It does not force compatible long monochromatic paths, and does not improve the sharp equivariant index-one bound on the certified-square complex (Item nori_actual_nori_coloring_sharp_certified_square_index_one_20261008).

Even a densely covered antipodal carrier can have small cohomological index. Coverage and separation are useful only to the extent that their connecting edges preserve monochromatic path certificates.

### Connector square certificates and monochromatic edge shadows

# Connector square certificates and monochromatic edge shadows

A monochromatic four-geodesic passing through an edge or root square is a physical certificate: the neighboring ordered three-faces have equal color on one actual path. As those certificates are glued along their physical edges, a two-color shadow appears, with either a shared edge certified by both colors or a rigid one-color assignment. Local square combinatorics then constrains allowable extensions.

## Monochromatic six-edge hub geodesics from finite ordered-hypergraph Ramsey

Let \(c(F,\pi)\in\{0,1\}\) be ANY coloring of physical ORDERED three-dimensional faces in Q_n. We impose NO antipodal or reversal condition. Let \(N=R_3(6;64)\) denote any finite 64-color Ramsey number guaranteeing a monochromatic six-vertex subset in every 64-coloring of 3-element subsets of an N-element set.

**Theorem (unconditional six-edge monochromatic hub path).** For all \(n\ge N\), EVERY cube vertex z lies on a monochromatic cube geodesic of length SIX whose four ordered-three-face windows all contain z as a common physical vertex. In particular, for n>=N the maximum monochromatic-geodesic length is at least six, independently of the coloring.

**Proof.** Fix z and a fixed linear order on the n coordinate directions. To every 3-element set T={a<b<c}, assign its ordered-face **profile**
\[
\Phi_z(T)=\big(c(F(z;T),\pi):\pi\text{ ranges over all six permutations of }(a,b,c)\big)\in\{0,1\}^6.
\]
This gives at most 64 colors on triples of coordinate directions. By the definition of N, there is a six-element subset W={p1<...<p6} on which \Phi_z is constant on all C(6,3) three-subsets. In particular, for all increasing ordered triples of p's, the common ordered-face color is one fixed bit q.

Start at the cube vertex \(x=z\oplus\{p_1,p_2,p_3\}\), and traverse the six distinct coordinates in order p1,...,p6. The path is a six-edge geodesic, and after the first three edges it passes through z. Its four successive ordered-three-face windows have triples
\[
(p_1,p_2,p_3),\ (p_2,p_3,p_4),\ (p_3,p_4,p_5),\ (p_4,p_5,p_6).
\]
Each physical three-face contains z: the first ends at z, the last starts there, and the middle two pass through it. Hence all four are among the prescribed equal-color faces F(z;T), so every window color equals q. QED.

**Optimal hub-span observation.** All ordered three-edge windows of any L-edge geodesic share a common physical vertex precisely when their vertex-index intervals [0,3],[1,4],...,[L-3,L] have nonempty intersection. This requires L-3<=3, or L<=6. Thus the fixed-hub reduction to ONE ordered triple coloring can certify six-edge monochromatic paths but cannot by itself certify longer paths: an L>=7 path has no common vertex in all its three-face windows. Proving unbounded-length monochromatic geodesics therefore requires coherent color transport between distinct hub vertices, not merely a stronger Ramsey bound on one hub.

**General k-face extension.** For ordered k-face colorings, put N_k=R_k(2k;2^{k!}). If n>=N_k, every cube vertex z lies on a monochromatic 2k-edge geodesic with all k-edge windows passing through z. The proof labels each k-subset by its k!-entry ordered color profile and selects 2k coordinate directions with constant profile. The window intersection criterion is L<=2k.

**Relation to NORI.** For active ordered-three-face NORI, the resulting six-edge monochromatic path supplies an actual reachable terminal-two-tail support of size four from some root. This is a qualitative dimension-independent reachability-rank floor in very high dimensions, stronger than the universal four-edge seed. It does not force complementary reversed-tail support overlap and therefore does not prove grand closure.

## Exact realization of ALL feasible globally missing middle-direction-pair graphs by valid NORI colorings

Let n be any ODD integer >=13. Fix an arbitrary simple graph M on the n cube direction coordinates. The earlier necessary theorem nori_globally_absent_middle_pair_graph_disjoint_even_cycles_paths_20261008 proved that for ANY valid active NORI coloring the graph of unordered direction pairs which NEVER appear as a middle pair in any actual monochromatic directed four-edge geodesic has maximum degree at most TWO and no odd cycle.

**CONVERSE THEOREM (exact classification for odd n>=13).** Conversely, if M is ANY disjoint union of (possibly trivial) paths and EVEN cycles, there is a valid ACTIVE NORI coloring c of ordered PHYSICAL three-faces whose GLOBAL MISSING-MIDDLE-PAIR GRAPH is EXACTLY M. More strongly, it can be chosen independent of the exterior face bits, and for EVERY nonedge {b,c} of M, the physical square in directions b,c at EVERY cube vertex is certified by a genuine monochromatic centered four-edge cube geodesic. Thus its certified-square complex X_c is exactly the entire two-dimensional coordinate cubical skeleton of Q_n MINUS all squares whose free direction pair is an edge of M; all ordinary cube edges and vertices are included.

**Construction.** Alternately two-color the EDGES of each path or even cycle component of M so any two incident M-edges have opposite binary signatures q_e. Define a regular tournament bit f(u,v) on ordered distinct directions using a cyclic order of all n labels:
  f(u,v)=1 if (v-u mod n)∈{1,...,(n−1)/2}, else0.
Then f(v,u)=1-f(u,v); for each fixed direction v, each q∈{0,1} occurs on exactly (n−1)/2 inputs f(u,v) and likewise f(v,u).

Construct a direction-only ordered triple label h(a,b,c) on distinct directions:
- If the FIRST TWO positions (a,b) form a missing edge e∈M, require h(a,b,c)=1-q_e.
- If the LAST TWO positions (b,c) form a missing edge e∈M, require h(a,b,c)=q_e.
- If neither adjacent ordered pair is in M, put h(a,b,c)=f(a,c).

This is CONSISTENT when both (a,b) and (b,c) belong M, because they are incident and q_bc=1-q_ab, so the two forced values coincide. It is also reversal-odd: reversing a triple interchanges 'first pair' and 'last pair', with complementary forced bits; if no adjacent pair is missing, f flips. Thus c(F,(a,b,c)):=h(a,b,c) is a genuine active NORI coloring, independent of exterior assignment.

**Every pair in M is absent.** For missing inner ordered pair (b,c)∈M, and any distinct outer a,d, the first window of its centered four-geodesic has triple (a,b,c), where missing edge (b,c) occupies LAST TWO positions, hence color q_bc. The second window has (b,c,d), where that edge occupies FIRST TWO positions, hence color 1-q_bc. Therefore the path is never monochromatic in any physical hub. This also applies to reverse middle order since q is unoriented.

**Every other pair is certified everywhere.** Fix ordered middle pair (b,c) with {b,c}∉M. Choose outer a outside {b,c}∪N_M(b), and outer d outside {b,c}∪N_M(c). Each forbidden set has size at most 4 because deg M<=2. Thus the triples (a,b,c) and (b,c,d) have NO adjacent M-edge and both fall in the tournament-rule case, with colors f(a,c) and f(b,d). For a chosen bit q, the first candidate set has at least (n−1)/2−4 >=2 possible a with f(a,c)=q, and the second has at least two possible d with f(b,d)=q. Choose a≠d. The genuine centered four-direction path (a,b,c,d) then has both ordered-three-face windows of equal color q. Since h is independent of exterior bits, precisely the same certificate exists at EVERY hub z in Q_n. Thus exactly the M pair classes are globally absent.

**Topology of the genuinely certified square carrier.** The resulting X_c is antipodally invariant, contains the complete cube graph, and is connected with free cube-antipodal involution. If M is NONEMPTY, choose any missing pair e={i,j}∈M. Every included square has at least one of directions i,j FIXED (otherwise it would be an omitted {i,j}-square). Therefore coordinate projection X_c→∂[0,1]^2≅S1 on (i,j) is continuous and equivariant. Its antipodal-cover class w1 is nonzero by connectedness, yet w1²=0 by the circle factorization. Thus the equivariant cohomological index of X_c is exactly one for EVERY NONEMPTY feasible missing-pair pattern M.

If M is empty, X_c is the full cube 2-skeleton; it has the expected higher equivariant index (at least 2). Thus in actual NORI colorings the global absence of a SINGLE middle pair is sufficient to collapse the certified-square carrier's index to one—even if every other physical square is certified.

**Interpretive guardrail.** This is an *exact realization theorem for local MONOCHROMATIC FOUR-EDGE witness geometry*, not a constructed counterexample to the full one-switch grand conjecture. The dimension restriction 'odd n>=13' is a convenient sufficient condition for the cyclic regular-tournament filler; no necessity for that threshold is claimed. In particular, genuine path certifications of virtually every cube square plus antipodal symmetry alone cannot supply a universal index-two fixed-point proof. One would need to show grand NO-CLOSURE prohibits the missing-pair phenomenon, or use a relative/higher-memory carrier with additional long-path constraints.

## Strengthened realization: the same coloring can have a monochromatic FULL antipodal geodesic from EVERY cube root

There is a strengthening of the exact-realization theorem that is crucial when interpreting its low-index certified-square complex: choose the cyclic regular tournament order **adaptively**, using a Hamiltonian cycle in the COMPLEMENT of M.

Because every vertex in the missing-pair graph M has degree at most2, the complement graph G=K_n\M has minimum degree at least n−3. For odd n>=13 this is at least n/2. By the classical Dirac Hamilton-cycle theorem (or its standard elementary longest-cycle proof), G has a Hamiltonian cycle. Fix its directed cyclic order
  p1,p2,...,pn,p1.
Define the regular tournament filler f with RESPECT TO THIS CYCLIC ORDER (rather than an arbitrary labeling of directions by Z_n), exactly as in the preceding construction. All degree and uniformity arguments remain valid.

Every consecutive pair {p_t,p_(t+1)} of this cyclic order belongs to G, hence is NOT a prescribed missing pair. Consequently for the full direction permutation pi=(p1,...,pn), each consecutive ordered triple (p_t,p_(t+1),p_(t+2)) has no adjacent missing-pair edge. Its prescribed window color is therefore the FALLBACK rule
 h(p_t,p_(t+1),p_(t+2)) = f(p_t,p_(t+2))=1,
since its first and last directions are forward cyclic distance2 (which lies in the tournament's positive half for n>=5). This holds for EVERY 1<=t<=n−2.

Thus **EVERY ONE of the 2^n possible starting roots** gives a FULL antipodal geodesic along this same pi whose ENTIRE ordered-three-face window word is monochromatic 1. Reversing direction order gives monochromatic 0 by active odd reversal. The certified-square carrier STILL has exactly the desired missing-pair graph M and, when M is nonempty, STILL has equivariant index exactly1.

This supplies a particularly strong sanity check: authentic full monochromatic NORI geodesics can coexist with an arbitrarily dense yet index-one local certified-square complex. Therefore fixed-point proofs must use topology informed by long witnesses or the no-closure hypothesis; no bare local-square index argument can distinguish successful colorings from potential counterexamples.


## Witness-root cubical domination, and why a global single-valued reachability label is impossible

Let n>=5 and color actual physical ORDERED three-faces of Q_n by bits; antipodal reversal oddness is imposed only for the explicit obstruction example below. Define
  R_4={x in Q_n : there exists a genuine monochromatic FOUR-EDGE directed cube geodesic ROOTED at x}.
No requirement is placed on prescribed terminal directions in this coarse root set.

**THEOREM 1 (root-witness dominating set, all binary colorings).** Every physical cube vertex z has an ACTUAL cube neighbor x∈R_4. Equivalently, R_4 dominates the entire cube graph Q_n. In particular
  |R_4|>=ceil(2^n/(n+1)).
More precisely for each hub z there is a physical 2-dimensional ROOT SQUARE Q_root consisting entirely of starting vertices for the SAME ordered monochromatic four-edge word with identical ordered physical three-face windows, and one of the square's four vertices is a neighbor of z.

**Proof.** The centered five-direction odd-cycle theorem (proved separately in NORI; needs no NORI antipodal oddness) supplies at z some genuine monochromatic CENTERED four-edge path with ordered distinct direction word (a,b,c,d). Its start root is r=z xor {a,b}. Both consecutive physical ordered three-face windows of this path have free coordinates b,c. Therefore as proved in the middle-root-square lemma, the SAME two physical faces in the SAME order are traversed for every starting root
  r xor H, H⊆{b,c}.
All four starting vertices belong to R_4. In particular r xor b=z xor a is a CUBE NEIGHBOR of z. Since z was arbitrary, R_4 is dominating. Each chosen root in R_4 dominates at most n+1 cube vertices including itself, so |R_4|(n+1)>=2^n, yielding the cardinality bound. QED.

**THEOREM 2 (sharp qualitative warning: R_4 need not equal the whole cube even under ACTIVE NORI).** For every n>=6 and every PRESCRIBED physical cube root x, there exists a genuine binary coloring of ORDERED PHYSICAL 3-faces satisfying the active NORI axiom
  c(bar F,reverse pi)=1-c(F,pi)
such that NO FOUR-EDGE ordered cube geodesic rooted at x is monochromatic. In particular x∉R_4.

**Construction and proof.** For each physical ordered three-face (F,pi) let T be its three free coordinates. Define its *exterior Hamming distance from x* as
  d_x(F)=#{i∉T: fixed exterior bit of F in coordinate i differs from x_i}.
There are n−3 exterior coordinates. Prescribe color0 on ALL ordered physical 3-faces with d_x(F)=0, and color1 on ALL ordered physical 3-faces with d_x(F)=1, regardless of the direction order pi. These prescriptions are compatible with NORI antipodal-reversal-oddness when n−3>=3: under the face antipode, d_x(bar F)=(n−3)−d_x(F), so the antipodal mate of a 0-layer face lies at distance n−3>=3 and is unprescribed, while the mate of a 1-layer face lies at distance n−4>=2 and is unprescribed. No prescribed face lies in the reversal orbit of another prescribed face. Complete the remaining antipodal-reversal orbit colors freely, always setting mate colors complementary.

Now take ANY four distinct directions (a,b,c,d) and its genuine rooted four-edge path starting at x. Its FIRST ordered three-face (a,b,c) contains root x, so has d_x=0 and color0. Its SECOND ordered three-face (b,c,d) begins after direction a was flipped; since a lies outside {b,c,d}, the physical face's exterior bits differ from x on EXACTLY coordinate a, so it has d_x=1 and color1. Therefore every rooted four-path at x has the two-window word (0,1), hence NONE is monochromatic. QED.

**Topological architecture implication.** The center-based certified-square complex X_c has ALL physical cube vertices and genuine middle-pair squares and is connected under active NORI; each certified centered four-path also generates a separate FULL 2-face in the space of STARTING ROOTS. The union of these genuine root-squares projects to a DOMINATING vertex set, but not necessarily to all of Q_n. One may therefore build a multivalued/witnessed topological cover using closed vertex stars of these root-squares, rather than assume every physical root has a monochromatic rank-two terminal label. However thickening a witness square to cover an adjacent root does NOT turn that adjacent root into a genuine four-path witness: the combinatorial incidence/face-provenance must be retained in a carrier before applying Tucker, cubical Sperner, or KKM.

**Scope.** This does not force full grand closure; it identifies the precise geometric amount of universal local reachability and disproves the too-strong claim that every root admits even a four-edge monochromatic start in all valid colorings. The correct topological object is a supported/multivalued root-chart complex with honest certificates.

The color shadow is not a substitute for the original ordered faces. Any global conclusion must be lifted from its certified edges to a single full path retaining the correct order of overlapping three-windows.

## Dead-edge rigidity and extension constraints

# Dead-edge rigidity, monochromatic hubs, and facet lifting

Fix a binary coloring of ordered physical three-faces of Q_n. A physical cube edge is certified when some genuine monochromatic four-edge geodesic traverses it. Call an edge dead if no such geodesic exists. The following rigidity holds even without antipodal oddness.

## Rigidity around a dead edge

Let e={z,z xor e_i} be dead. The dead-edge rigidity theorem forces a color q for all ordered physical three-faces through either endpoint whose three free directions avoid i, independently of their ordering. Consequently, any directed path of length 3<=k<=min(n-1,6) through one endpoint that uses k distinct directions avoiding i is monochromatic whenever that endpoint occurs at a vertex position j satisfying k−3<=j<=3 (with the usual endpoint truncations). Indeed every consecutive three-face window along the path contains that vertex and has its free directions outside i, so each has color q. In particular for n>=7, arbitrary six-direction orders avoiding i can be rooted to pass through a dead-edge endpoint and yield genuine monochromatic six-edge geodesics.

This exhibits the tradeoff: failure of a local four-edge connector forces extensive monochromatic rigidity on transverse faces. The conclusion concerns actual physical faces; exterior bits are fixed by the chosen common hub.

## Facet-local amplification

Suppose n>=8 and e is dead. Let H be any coordinate 8-face containing e. The restriction of the coloring to H still has e dead: every four-edge witness in H would also be a witness in Q_n. Applying the established dimension-eight dead-edge polarity bootstrap inside H gives a full antipodal 8-geodesic with at most one window-color change. Its six windows are physical windows of the ambient coloring.

Order the remaining n−8 unused directions after this eight-edge path. The extension remains a full ambient geodesic and introduces at most n−8 additional windows, hence at most n−8 additional color changes. The resulting global switch count is at most 1+(n−8)=n−7. This is a conditional all-dimensional quantitative consequence of a single dead edge, rather than full one-switch closure.

The general hub-extension results further constrain how a collection of certified middle edges may be lifted across facets. Each extension must keep the actual fixed exterior coordinates and evaluate the new ordered windows; a local monochromatic hub need not persist as a globally monochromatic full path without this boundary control.

## Exact role in the global argument

Dead-edge rigidity and certified-edge density split the problem into two regimes: a dead edge yields transverse monochromatic paths and an eight-face good seed; the complementary live-edge regime supplies abundant certified local four-geodesics. The outstanding step is to synchronize these seeds or certificates across complementary supports with compatible root and terminal windows. The present theorems give physical local forcing and a global switch bound, while preserving the distinction between a long monochromatic partial path and a full antipodal one-switch geodesic.

### Dead-edge hub rigidity and forced short monochromatic geodesics

# Dead-edge hub rigidity and forced short monochromatic geodesics

Suppose a physical cube edge is absent from every monochromatic four-edge geodesic. This local failure is surprisingly rigid: the three-face colors around its endpoints become constrained uniformly in free triples avoiding its direction. Those constraints can be exploited to build much longer actual monochromatic paths through either endpoint, and to compare dead edges of different directions.

THEOREM. Let n>=5 and let c be ANY binary coloring of physical ordered three-faces of Q_n. Suppose an i-direction physical cube edge e={z,z xor e_i} is DEAD: no genuine monochromatic four-edge geodesic traverses it. Then the local dead-edge rigidity lemma gives a single bit t such that every physical ordered three-face through z OR z xor e_i whose free-coordinate triple does NOT contain i has color t, irrespective of the order of those three free directions.
Hence, for any integer 3<=k<=min(n-1,6), any k distinct directions p_1,...,p_k outside i, and any hub h in {z,z xor e_i}, there is an ACTUAL directed monochromatic k-edge cube geodesic using exactly this ordered direction list, passing through h at vertex index j with max(0,k-3)<=j<=min(3,k) (choose starting vertex h xor {p_1,...,p_j}). Every consecutive three-direction window of the path contains h, because its index interval [r,r+3] contains j for every r=0,...,k-3; since no free triple contains i, every window has color t. In particular for n>=7 the fixed dead-edge endpoints lie on monochromatic SIX-edge geodesics in arbitrary six directions avoiding i.
DIMENSIONAL COROLLARY. If 5<=n<=7 and an active NORI coloring has ANY dead edge, it has a full antipodal n-edge geodesic with at most ONE ordered-three-face color change. Proof: choose k=n-1 directions excluding the dead direction i. The exhibited (n-1)-edge geodesic is monochromatic. Append its sole unused coordinate i at either end. The resulting full antipodal n-edge path has precisely one added ordered-three-face window, hence at most one color change. Thus any counterexample on Q7 must have every physical cube edge traversed by some actual monochromatic four-edge geodesic. This is not a full Q7 proof, since dead-free colorings need separate treatment.
The six-edge hub mechanism reaches its inherent geometric limit at six: an ordered-three-face geodesic of k>=7 edges has consecutive length-three windows with NO common physical cube vertex, since the shared vertex index intersection is [k-3,3], empty for k>6. Therefore longer paths require genuinely global certificate transport.

THEOREM (UNCONDITIONAL DEAD-DIRECTION UNIQUENESS THROUGH DIMENSION EIGHT). Let c be any active NORI antipodal-reversal-odd binary ordered-three-face coloring of Q_n, 5<=n<=8. Let M be its set of physical cube edges that are traversed by no monochromatic directed four-edge geodesic. If M is nonempty, all its edges are PARALLEL: they have the same coordinate direction.
PROOF for n<=7: Two dead edges in different directions i,j have minimum endpoint distance d in exterior coordinates D=[n] minus {i,j}, and their antipodal partner has minimum endpoint distance |D|-d=n-2-d. The proved dead-edge direction-separation theorem says both distances >=3, which requires n>=8. Thus n<=7 impossible.
PROOF n=8: Here |D|=6 and both distances >=3 force d=3 and n-2-d=3. For two different dead directions i,j at this exterior distance3, choose endpoint hubs z,w matched in their i,j bits. They differ in exactly three exterior directions, so their shared physical ordered three-face FREE in those three directions but omitting i and j has color equal to BOTH local dead-edge hub bits t_i and t_j; hence t_i=t_j. Apply the same reasoning between the fixed i-dead edge and the ANTIPODAL PARTNER of the j-dead edge; its exterior distance is ALSO3. The latter partner has dead hub bit 1-t_j by active antipodal-reversal oddness. Therefore t_i=1-t_j, contradicting t_i=t_j. Hence different dead directions cannot coexist in n=8. QED.
COROLLARY (NO-CLOSURE STRUCTURAL TARGET n<=10). The earlier two-dead-hub splicing theorem proves that any active coloring in n=9 or10 with dead edges in two different directions has a full antipodal geodesic with at most one color change, and indeed n=9 gives a full monochromatic geodesic. Thus in ANY hypothetical counterexample in dimensions 5<=n<=10, if dead edges exist they must ALL share ONE direction. For n=8 this one-direction property is unconditional.
SCOPE. This is a genuine global compatibility condition between antipodal singular hubs, independent of computation. It does not show a full one-switch geodesic when all dead edges are parallel or when no dead edges exist.

THEOREM (SAME-DIRECTION DEAD-HUB SPLICING). Let n>=5 and let an arbitrary binary ordered-three-face coloring of Q_n have two different dead physical edges in the SAME direction i. Choose one endpoint z of the first and one endpoint w of the second with matching i-bit, so their difference set T subset D=[n] without {i} has size d>=1. Let m=n-1. Their dead-edge rigidity bits are t_z,t_w. If d<=3 then t_z=t_w, since a physical ordered three-face containing both hubs and omitting i exists: choose three free directions containing T. More generally if t_z=t_w, d<=4, and d>=n-7 (i.e. m-d<=6), then a MONOCHROMATIC full length-m geodesic inside their common i-facet exists. Append i at one endpoint to obtain a full n-edge antipodal geodesic with AT MOST ONE window color change. Proof: choose an ordered partition D minus T=A disjoint union B with p=|A|<=3 and ell=|B|<=3 (possible iff m-d<=6). Start at x=z xor A, traverse A to reach z at index p, traverse all d directions of T to reach w at index p+d, then traverse B. Among the m-2 consecutive three-face windows, window-start indices k in [p-3,p] contain z and hence have color t_z; those in [p+d-3,p+d] contain w and have color t_w. Since p,ell<=3, these intervals cover both ends; since d<=4, they overlap (d<=3) or are adjacent (d=4), and therefore cover ALL windows. All free triples avoid i, so all are monochromatic t_z=t_w. Appending i creates precisely one additional ordered-three-face window; the complete n-geodesic has at most one color change. QED.
APPLICATION TO ACTIVE NORI ODDNESS AND LOW DIMENSIONS. Under c(bar F,rev pi)=1-c(F,pi), the antipodal mate of a dead i-edge is dead with bit 1-t. The projected dead-edge positions form an antipodally invariant subset S of Q_m, and in any hypothetical counterexample all dead edges share one direction for n<=10 by the earlier different-direction-splice theorems.
(i) n=8, m=7: for any pair of distinct projected dead positions that are NOT antipodal, replace the second by its antipode if needed to obtain distance d=min(d0,7-d0) in {1,2,3}. Rigidity forces equal local bits, and n-7=1, so the mono m-facet splice closes NORI. Therefore any hypothetical Q8 counterexample has EITHER no dead edges OR exactly ONE antipodal orbit of two parallel dead physical edges; |M|<=2.
(ii) n=9,m=8: for two projected dead positions at distance d0 with 2<=d0<=6, if d0=4 choose either position or its antipode so its local color matches the first dead bit (the distance remains 4). Otherwise choose whichever gives d=min(d0,8-d0) in {2,3}; at distance<=3 the rigidity bits necessarily agree. In every case 2<=d<=4 and d>=n-7=2, so the mono m-facet splice closes NORI. Therefore in a hypothetical Q9 counterexample, any two projected dead positions belong either to the SAME antipodal orbit or to orbits at projected distance 1 (equivalently 7). Fix one orbit {a,bar a}. Every other dead orbit must be represented by a neighbor a xor e_j. Two different such neighbors have Hamming distance2 and would force closure, so at most ONE further orbit exists. Consequently all dead edges are parallel and |M|<=4; if |M|=4 their projected positions are exactly {a,bar a,a xor e_j,bar a xor e_j} for one direction j outside i.
(iii) n=10,m=9: any two parallel dead i-edges at projected distance3, or4 with matching dead bits, force grand closure by the same lemma (n-7=3). Other configurations are not covered.
These are unconditional implications of honest physical face color rigidity and exact geodesic splice geometry. They are structural restrictions under a hypothetical counterexample, NOT a full Q8 or Q9 proof when no dead edge exists.

Dead-edge rigidity is therefore a positive path-construction mechanism, not merely a negative certificate. Its local span reaches complete low-dimensional cubes under the stated hypotheses, but higher-dimensional closure still requires a compatible continuation beyond the hub.

### Dead-edge transposition descent and terminal normal forms

# Dead-edge transposition descent and terminal normal forms

Let the switch defect of a full geodesic be the number of changes in its consecutive ordered-three-face color word. At a dead physical edge, swapping adjacent travel directions can change only a controlled set of windows. The resulting local exchange inequalities allow a variational descent in the order/root space while preserving the full geodesic property.

## Bichromatic hub: all mixed-class ordered faces are forced by middle-edge shadow

Let \(n\ge6\) and \(c\) satisfy active NORI antipodal-reversal oddness. Consider the **no-common-edge alternative B** of Item \`nori_center_square_bichromatic_edge_or_antipodally_odd_edge_shadow_20261008\`: no physical cube edge is certified by monochromatic centered four-edge geodesics of **both** colors. Then every certified physical cube edge \(e\) has a unique square-witness color \(\sigma(e)\in\{0,1\}\).

By Item \`nori_antipodal_square_connectedness_forces_bichromatic_connector_hub_20261008\`, some center vertex \(z\) supports centered monochromatic four-geodesics of both colors. Let \(A=A(z)\subset[n]\) consist of cube coordinate directions \(b\) for which the physical edge \(\{z,z\oplus e_b\}\) has square-witness color \(0\), and \(B=B(z)\subset[n]\) those whose edge has witness color \(1\). Both \(|A|\) and \(|B|\) are at least 2, because every connector square involves two distinct middle directions. There is at most one remaining isolated direction by the certified minimum-degree \(n-1\) theorem.

For any ordered triple \((a,b,c)\) of distinct directions, write
\[
h_z(a,b,c)=c(F_z(a,b,c),(a,b,c)),
\]
where \(F_z(a,b,c)\) is the **physical three-face through \(z\)** with those free directions.

**Theorem (mixed-middle rigidity at a bichromatic hub).** Under the above no-common-edge alternative, for every ordered triple \((a,b,c)\) with \(b\in A\cup B\) and at least one of its neighboring directions \(a,c\) in the *opposite* class to \(b\),
\[
\boxed{h_z(a,b,c)=
\begin{cases}
0,&b\in A,\\
1,&b\in B.
\end{cases}}
\tag{1}
\]
Thus every ordered face through a bichromatic hub whose direction triple crosses the two shadow color classes has its color determined **solely by the color of its middle coordinate edge**. This is an honest physical-face identity, not an abstract coloring of permutations. No condition is claimed for a triple entirely within one color class, or for a triple involving the at-most-one isolated direction as the middle coordinate.

**Proof.** If \(b\in A\), \(c\in B\), then no centered four-edge connector with middle pair \(\{b,c\}\) can be monochromatic at \(z\). Such a connector would certify both physical edges in directions \(b,c\) with a common color, contradicting their already distinct singleton colors. For the ordered middle pair \((b,c)\), write
\[
I_a=h_z(a,b,c),\quad O_d=h_z(b,c,d)
\]
for outer directions \(a,d\notin\{b,c\}\). For every \(a\ne d\), \(I_a\ne O_d\). Since \(n-2\ge4\), for any \(a,a'\) choose a \(d\) distinct from both, giving \(I_a=I_{a'}\). Similarly the outgoing \(O_d\) are all equal and opposite the common incoming value. Thus there is a bit \(K_{bc}\) such that
\[
h_z(a,b,c)=K_{bc},\qquad h_z(b,c,d)=1-K_{bc}
\tag{2}
\]
for **every** allowed outer \(a,d\). There is an analogous bit \(K_{cb}\) for the reverse orientation \((c,b)\). Formula (2) holds for every cross pair of \(A,B\), in either order.

Now for \(b\ne b'\in A\), \(c\in B\), evaluate the triple \((b,c,b')\) twice, using the outgoing half of the \((b,c)\) constraint and the incoming half of the \((c,b')\) constraint:
\[
1-K_{bc}=K_{cb'}.
\tag{3}
\]
Likewise for \(c\ne c'\in B\), \(b\in A\), the triple \((c,b,c')\) gives
\[
1-K_{cb}=K_{bc'}.
\tag{4}
\]
Since \(|A|,|B|\ge2\) and \(n\ge6\) with at most one isolated coordinate, **at least one** class has size at least 3. If \(|A|\ge3\), fixing \(c\in B\) and comparing (3) for two distinct \(b,b'\) using a third \(b''\) shows all \(K_{bc}\) are equal as \(b\) varies. Then (3)-(4) show the common value is also independent of \(c\). If \(|B|\ge3\), the symmetric calculation first makes all reverse-oriented \(K_{cb}\) independent of \(c\) and then (3)-(4) make the forward-oriented \(K_{bc}\) constant as well. Thus one bit \(K\) satisfies
\[
K_{bc}=K\quad(b\in A,c\in B),\qquad
K_{cb}=1-K\quad(c\in B,b\in A).
\tag{5}
\]

Choose any existing color-0 connector at \(z\); its two middle directions \(b,b'\) belong to \(A\). Choose **distinct** outer directions \(a,d\in B\), which is possible because \(|B|\ge2\). Equations (2),(5) give
\[
h_z(a,b,b')=K,\qquad h_z(b,b',d)=K.
\]
Hence the centered path with ordered directions \((a,b,b',d)\) is monochromatic of color \(K\) and certifies the same physical middle square \(\{b,b'\}\) already certified in color 0. Alternative B forbids two colors on any physical edge of this square. Therefore \(K=0\), and (5) gives \(K_{cb}=1\).

Finally, take any triple \((a,b,c)\) with the asserted mixed-class adjacency. If \(b\in A,c\in B\), apply the first half of (2) to \((b,c)\) and get \(h_z=K=0\). If \(a\in B,b\in A\), apply the outgoing half of the constraint for \((a,b)\), where \(K_{ab}=1\), and get \(h_z=1-K_{ab}=0\). The cases with \(b\in B\) are symmetric and give 1. This proves (1). \(\square\)

**Consequences and exact research frontier.** A bichromatic hub in shadow alternative B carries a **locally reversal-even middle-coordinate selector** on all mixed-color ordered face triples. (Reversing a mixed triple preserves its middle direction, hence its value in (1).) This is substantial rigidity: the physical face coloring is forced on every triple crossing the two certified direction classes, though the remaining same-class triples can contain genuine defects. Antipodal reversal exchanges the certified 0/1 direction classes at \(\bar z\), so the local rule remains consistent with active global oddness. A possible route to eliminating alternative B is to propagate these mixed-triple identities along certified root moves, using the fact that the underlying physical faces are unchanged when any free direction is toggled. The missing theorem is **coherent propagation of the two direction partitions between different bichromatic hubs**; (1) alone does not imply a common opposite-color square or a full one-change antipodal geodesic.

The statement does not assert all faces depend only on their middle direction; it is precisely restricted to physically witnessed *mixed-class* triples.

THEOREM (ANTIPODAL FOUR-SPACING OF DEAD EDGES). Let n>=5 and let c satisfy the ACTIVE NORI c(bar F,reverse pi)=1-c(F,pi) on ordered physical three-faces of Q_n. Let M be the set of physical cube edges traversed by NO genuinely monochromatic four-edge geodesic. The proved local rigidity theorem says that any TWO dead edges in DISTINCT coordinate directions have physical endpoint-set Hamming distance at least THREE; also M is invariant under cube antipodality.
Fix any FULL directed n-edge antipodal geodesic P(x,p) with physical edges e_1,...,e_n, where each coordinate direction occurs once. Complete it to the simple symmetric 2n-edge belt by following the antipodal translates bar e_1,...,bar e_n in the SAME coordinate order. The dead-edge status of each belt edge is antipodally repeated, so its 2n-bit indicator is (d_1,...,d_n,d_1,...,d_n), where d_k=1 iff e_k is dead.
If two different positions k,l in [n] are both dead, their coordinate directions differ. Write their CYCLIC index distance s=min(|k-l|,n-|k-l|). If s<=3, there are two dead belt edges of distinct directions at cyclic edge-index separation s<=3: choose e_k and e_l if |k-l|=s, or e_l and bar e_k if n-|k-l|=s. On the 2n-edge cube belt the nearest endpoints of these two edges are joined by a segment containing at most s-1<=2 cube edges. Thus their physical endpoint-set Hamming distance is <=2, contradicting the different-direction dead-edge separation theorem. Therefore
  min(|k-l|,n-|k-l|)>=4
for every pair of dead positions k,l.
COROLLARIES. The dead positions form a 4-separated code on the cyclic n-position set, so their number is at most floor(n/4) (for n<8, at most one). This is strictly stronger than the matching-only bound ceil(n/2). When a hypothetical active NORI counterexample in dimensions <=10 has any dead edges, the separately proved mixed-dead-direction extraction theorem forces all dead edges to lie in ONE coordinate direction. Every full antipodal geodesic uses that direction exactly once; hence in a hypothetical counterexample on Q_5,...,Q_10 every full geodesic has AT MOST ONE dead physical edge.
The rule is an all-dimensional COLOR-INDEPENDENT packing fact once dead-edge rigidity and active antipodal reversal are in place. It does not imply the full one-switch conjecture, but it removes complex multi-dead configurations from each root/permutation chamber, narrowing the cyclic-seam and adjacent-swap descent analysis.

THEOREM (SHARP Q8 DEAD-HUB POLARITY BOOTSTRAP). In EVERY binary coloring of the physical ORDERED three-dimensional faces of Q8, with NO antipodal/reversal constraint assumed, if some physical cube edge e_i={z,z xor i} belongs to NO genuinely monochromatic directed four-edge geodesic, then Q8 has a FULL antipodal eight-edge geodesic with AT MOST ONE color change among its six ordered-three-face windows. Consequently any hypothetical active NORI Q8 counterexample is COMPLETELY DEAD-EDGE-FREE. This strengthens the earlier Q8 at-most-one-antipodal-dead-pair obstruction to NO dead edges.
PROOF. The exact dead-edge rigidity theorem assigns one bit t such that EVERY ordered three-face containing z and whose free triple omits i has color t (similarly at z xor i). Set D=[8] minus {i}, |D|=7. Argue by contradiction: suppose EVERY full eight-edge geodesic has at least two window-color changes.
STEP 1 (FORCED ONE-SHELL ANTIPOLARITY). Fix ANY r in D and ordered distinct (a,b,c) in D minus {r}. Let (u,v,w) be the other three directions of D, excluding {r,a,b,c}. Consider the full eight-coordinate order (u,v,w,r,a,b,c,i), starting from x=z xor {u,v,w}, so after the first three moves the path reaches z. Its FIRST FOUR ordered-three-face windows, (u,v,w),(v,w,r),(w,r,a),(r,a,b), ALL contain z, have no free direction i, and are therefore color t. Its FIFTH face window is (a,b,c), through the vertex z xor r; its SIXTH is (b,c,i), of arbitrary color. For the full word (t,t,t,t,X,Y) to have >=2 changes, it is NECESSARY that X=1-t and Y=t. Since r,a,b,c were arbitrary, this forces
  for EVERY r in D and ALL ordered distinct a,b,c in D minus {r}: c(F(z xor r;{a,b,c}),(a,b,c))=1-t.
STEP 2 (SECOND HUB MAKES A GOOD PATH). Choose distinct r,s in D. Choose any six directions q1,...,q6 giving an order of D minus {r}, with q4=s; write q5=a,q6=b. Put y=z xor r, and start a directed full eight-edge path at y xor {q1,q2,q3} using order (q1,q2,q3,s,a,b,r,i). Its first SIX edges are centered at y after three moves, and their FIRST FOUR ordered-three-face windows are all through y and omit r and i, so by the one-shell polarity from Step1 they have color 1-t. Its FIFTH ordered window has directions (a,b,r) and is a physical face through the vertex y xor s=z xor {r,s}. Because r is a FREE coordinate of this window, the same physical face contains z xor s. Its ordered free triple (a,b,r) excludes i and s, so Step1 with hub z xor s says its color is ALSO 1-t. The SIXTH, final window has arbitrary color. Therefore the full eight-edge antipodal geodesic has window word (1-t,1-t,1-t,1-t,1-t,Y), with at most ONE color change, contradiction. QED.
GEOMETRIC MECHANISM. A dead-edge hub yields a monochromatic star on all ordered faces avoiding its direction. Failure of one-switch closure forces the next outer coordinate shell to have COMPLEMENTARY uniform color on triples not containing the shell direction. This forced shell is itself rich enough to produce a new monochromatic six-edge hub geodesic whose first extension window is physically IDENTICAL to a face on a neighboring shell hub, contradicting the putative necessary color flip. The proof is fully face-geometric and does not use numerical enumeration or the active NORI parity condition.
SCOPE. It leaves arbitrary DEAD-FREE ordered-three-face colorings of Q8 unresolved by this argument. In dimensions larger than 8, six-window hub propagation leaves more than two uncontrolled tail windows and requires an additional memory-boundary forcing lemma.

The descent yields a terminal normal form and sharp constraints on its remaining caps. It does not by itself force zero or one switch in every dimension; the residual plateau requires an additional cross-root or cap comparison.

### Dead-hub facet lifting and live-edge completion constraints

# Dead-hub facet lifting and live-edge completion constraints

A monochromatic hub certificate occupying a bounded set of directions can be embedded in a larger cube facet. For each such lifting one must preserve actual exterior-coordinate bits and the order of the newly created windows at the facet boundary. The following results quantify the dimension-dependent strength of dead-edge hub lifting and show how live parallel-edge completion interacts with antipodal parity.

THEOREM (FACET-LOCAL VERSION OF Q8 POLARITY BOOTSTRAP). Let n>=8 and c be ANY binary coloring of physical ORDERED three-faces of Q_n. Suppose a physical edge e_i is DEAD, meaning no monochromatic directed four-edge cube geodesic traverses it. Then for EVERY physical 8-dimensional coordinate face H of Q_n that contains e_i, the restricted coloring on ordered physical three-faces of H admits a FULL eight-edge antipodal H-geodesic with AT MOST ONE ordered-window color change. Reason: a dead edge globally remains dead in the restricted 8-face, and the independent Q8 polarity-bootstrap theorem applies to every binary ordered face coloring, with no antipodal oddness required. Thus this is a UNIFORM RANK-EIGHT REACHABILITY SEED around EVERY dead edge, in arbitrary ambient dimensions.
COROLLARY (SHARPENED FULL GLOBAL SWITCH BOUND CONDITIONAL ON ONE DEAD EDGE). For every n>=8, an arbitrary binary ordered-three-face coloring having a dead edge admits a FULL n-edge antipodal Q_n geodesic with at most n-7 color changes. Proof: choose any H as above, its good eight-edge geodesic P has six ordered-three-face windows and <=1 change. Append the n-8 unused coordinate directions in any order. The full n-edge path has n-2 windows, thus n-8 additional window colors; each extension adds at most one change, yielding D<=1+(n-8)=n-7. In particular n=8 closes with <=1, n=9 yields <=2, n=10 <=3, and beyond n>=8 this improves the earlier single-dead-edge n-6 bound by one. The endpoint inside H is its H-antipode, so appending each unused direction produces a genuine full antipodal cube geodesic.
LIMITATION. An 8-dimensional face good path is not necessarily MONOCHROMATIC, and the additional coordinates can generate new switches. Exact extraction to one switch in unrestricted n>8 still requires compatible extensions or multi-face topological forcing. No claim is made that an arbitrary face avoiding a dead edge has the rank-eight guarantee.

THEOREM (FULLY REALIZABLE TOPOLOGICAL CONNECTIVITY NO-GO, ALL n>=9). For each n>=9 there exists an ACTIVE NORI binary coloring of PHYSICAL ordered three-dimensional faces of Q_n obeying c(bar F,rev pi)=1-c(F,pi) such that for a fixed physical cube direction i, the projected graph L_i of i-parallel edges traversed by some GENUINE monochromatic four-edge geodesic is DISCONNECTED. More precisely, L_i has a connected component which is exactly a projected TWO-DIMENSIONAL CUBE SQUARE: four i-parallel physical edges, each with exactly two live projected neighbors, all outside neighbors dead. It also has at least one distinct live projected edge outside that square, and its antipodal mirror contains another isolated live square. Thus antipodal symmetry, physical face consistency, and the actual monochromatic four-path certificates DO NOT force each coordinatewise live-position carrier to be connected. This is NOT a NORI grand counterexample.
EXPLICIT CONSTRUCTION. Number directions i=0, a=1,b=2, and put E={3,...,n-1}, of size r=n-3>=6. Project along i onto Q_(n-1). Let C be the 2-dimensional square of positions with E-bits all zero and arbitrary a,b bits, namely C={0,e_a,e_b,e_a+e_b}. Define the lower OUTER BOUNDARY B={v xor e_j:v in C,j in E}; this has 4r projected positions with exactly one E-bit1. Let bar B be its projected antipodal complement, having exactly r-1 E-bits1. Prescribe every i-parallel edge at positions in B to be DEAD with rigidity bit t=0, and every antipodal mate at positions in bar B to be DEAD with bit t=1. To realize this, at both physical endpoint hubs of EACH such edge prescribe EVERY physical ordered three-face color by the exact local dead-edge template: color t if i is absent or in the middle of its ordered free triple, and color 1-t if i occupies either end.
PRESCRIPTION CONSISTENCY. Within B all prescriptions have the SAME rigidity bit; within bar B they have complementary bit. Between B and bar B, projected E-coordinate Hamming distance is at least (r-1)-1=r-2>=4, so no physical ordered 3-face can contain hubs from BOTH groups: a 3-face changes at most3 projected coordinates if i is absent, and at most2 if i is free. Antipodal reversal interchanges B with bar B and complements all template colors (middle stays middle, end swaps with end, absent remains absent). Thus the prescribed partial colors are mutually consistent and active-NORI compatible. Extend to all remaining ordered three-face involution orbits arbitrarily, assigning each mate its complementary bit. Every B/bar B i-edge is genuinely DEAD, since the local color template makes every four-edge geodesic through that edge bichromatic.
FORCE THE CENTRAL SQUARE LIVE. The physical ordered 3-face whose free triple is (a,i,b) and whose fixed E-bits are ALL ZERO is untouched by the dead templates; assign it color1. (Its antipodal-reversed mate with free order (b,i,a) and all E-bits one automatically gets color0.) For EACH projected v in C, consider the genuine four-edge geodesic with direction order (a,i,b,3), rooted at the physical cube vertex having E-bits zero and projected a,b position v xor e_a (with i-bit0). Its first ordered three-face (a,i,b) is the newly assigned color1. Its second ordered three-face (i,b,3) includes the hub at projected v xor e_3 in B, so dead template t=0 forces color1 (i in FIRST position). Hence this honest directed four-step geodesic is monochromatic color1 and traverses the physical i-edge at v. ALL FOUR vertices v of C therefore lie in L_i. Every projected neighbor of C outside C is in B and DEAD, so C is a WHOLE CONNECTED COMPONENT of Q_(n-1)[L_i], a genuine live square. Its antipodal square bar C is likewise fully live by the active NORI involution, and separated from C since r>=6.
AN OUTSIDE LIVE EDGE (independent verification). Put w=e_3+e_4+e_5 in the projected cube (physical bits in directions 3,4,5). The physical ordered 3-face with free order (i,4,6) through the hub at w is untouched by the boundary templates: its projected E-bit weight ranges between2 and4 as the two free exterior directions4,6 vary, while B has weight1 and bar B has weight r-1>=5. Assign this face color0, with its antipodal-reversed mate complementary. The four-edge geodesic rooted at physical position w xor e_3, with direction word (3,i,4,6), traverses the i-edge at w: its first ordered 3-face (3,i,4) contains the low dead projected hub e_5∈B, forcing color0 since i is MIDDLE; its second ordered 3-face (i,4,6) is the explicitly assigned color0. Thus the path is genuinely monochromatic0, so w∈L_i, while w lies outside C and bar C. No conflicting prescription occurs. This makes the disconnection explicit even without appealing to antipodal symmetry.
CONSEQUENCES. The projected live-edge carrier L_i need not be connected, even though its graph has unconditional minimum degree >=2 (proved separately). Thus a fixed-root permutohedral or cubical fixed-point proof cannot assume coordinatewise four-window reachability sheets are connected purely from NORI oddness and local certificate coverage. One must use higher memory, a compatible long-path nerve, or a stronger relative connector theorem. The construction is a REAL VALID active NORI coloring, but its existence says nothing against the grand <=1-switch conjecture (it may have many good full geodesics).

THEOREM (EXACT TWO-COORDINATE TUCKER EXTRACTION FROM PHYSICAL NORI CERTIFICATES). For every active NORI coloring c of Q_n (n>=5) and every coordinate direction i, let L_i be the positions of i-parallel physical edges traversed by a genuinely monochromatic directed four-edge geodesic. Let X_i be the Freudenthal simplicial LIVE subcomplex of the antipodal projected three-skeleton ∂[0,1]^(n-1) built in theorem nori_dead_live_projected_three_skeleton_tucker_index_two_20261008. This is a FREE antipodal simplicial complex with w1(X_i/τ)^2 !=0.
For each projected live vertex v, choose one ACTUAL directed monochromatic four-edge path P_v that traverses the physical i-edge at v. Do so τ-EQUIVARIANTLY on antipodal v-pairs: choose an arbitrary P_v for one representative, and define P_(bar v)=ΘP_v, the physical antipodally complemented path with REVERSED direction order and complemented window color. Record its genuine color q(v)∈{0,1}, and traversal role r(v)∈{1,2,3,4} of coordinate i in its four-edge ordered word. The antipodal rule gives q(bar v)=1−q(v), r(bar v)=5−r(v).
Define a TWO-ABSOLUTE-VALUE signed Tucker label λ(v)∈{±1,±2} by λ(v)=(-1)^(q(v)) * h(r(v)), with h(r)=1 for r∈{1,4} (OUTER/EXTREME traversal) and h(r)=2 for r∈{2,3} (MIDDLE traversal, which certifies the physical middle square containing the i-edge). Then λ(bar v)=−λ(v).
THEOREM CONCLUSION. There are two DIFFERENT ACTUAL LIVE projected vertices v,w that lie in one common physical projected cube face of dimension≤3, and their selected real four-path witnesses P_v,P_w have OPPOSITE monochromatic colors q(v)!=q(w) but matching centrality h(r(v))=h(r(w)). In particular d_H(v,w)<=3. More precisely, either BOTH witnesses traverse their respective i-edges as a middle (second or third) edge and hence BOTH i-edges have genuine monochromatic CENTER-SQUARE certificates in opposite colors, or BOTH witness edges occur as outer (first or fourth) steps. The forced pair depends on the equivariant selection, but the existence holds for EVERY such choice.
PROOF. Suppose NO simplex edge of X_i joins complementary signed λ-labels. Send each vertex with label +j to e_j∈R² and each label −j to −e_j, and extend linearly over every Freudenthal simplex of X_i. Since no simplex contains ±e_j simultaneously, every simplex maps into a face of the crosspolytope boundary not containing zero; equivalently each coordinate has at most one appearing sign, so 0 is not in the affine convex hull. Normalizing gives an antipodally equivariant continuous map X_i→S¹. But such a map would annihilate the square of w1(X_i/τ), whereas the previously proved live-carrier theorem has w1² !=0. Contradiction. Therefore a complementary-label edge exists. Its endpoints are real live positions in one 3-face; equality of |λ| and opposition of signs give matching traversal class and opposite actual mono4 colors.
LIMITATION. The two true four-edge witnesses may have different ordered middle pairs and different starting roots; their physical i-edges merely lie within a common projected 3-face. An antipodally valid TuckER pair is not yet the SAME-root complementary reversed-terminal-tail witness required for NORI grand closure. The theorem replaces virtual sign-neutrality by a genuine bounded-distance, equal-memory-class, opposite-color certificate pair, which is a concrete target for a four-face local repair theorem.

Facet-level success is not synonymous with full-dimensional success. Where the local bounds leave more than one switch, exact exterior-bit and terminal-memory conditions remain an explicit obligation.

## Root hubs, midpoint witnesses and terminal caps

# Bichromatic root diamonds and certified seam repairs

Let c color actual ordered three-faces of Q_n. A monochromatic four-edge geodesic is witnessed by its two overlapping ordered three-face windows. A bichromatic hub is a cube vertex supporting such genuine connectors in both colors. Two questions then arise: which endpoint caps does a hub force, and when can two paths through the same hub be spliced without introducing additional changes?

## Same-root opposite-color diamonds

Suppose x and y are cube vertices at distance four and there are monochromatic geodesics P_0 and P_1 from x to y with direction orders (c,a,b,d) and (a,c,d,b), of colors 0 and 1 respectively. Let e be an unused coordinate. Appending e to either path produces a genuine five-edge geodesic, with two original windows of constant color and one new terminal window. Both new windows lie in the same actual three-face through y, with free set {b,d,e} but with distinct orders (b,d,e) and (d,b,e). Their colors are independent unless a physical reversal relation actually identifies their orbits. The diamond therefore provides two candidate continuations with explicit terminal-color tests, not an automatic common monochromatic extension.

Under additional global maximality assumptions, failures of both continuations force the corresponding ordered-cap colors to be opposite to their original path colors. Such identities can feed a root exchange, provided the newly exposed starting and terminal windows are checked in the same manner.

## Four-way splicing at a common physical midpoint

Let P and Q be full antipodal geodesics from the same root x, whose first ell used-coordinate sets agree, where 3<=ell<=n−3. Both paths reach the identical midpoint y after ell steps, and both suffixes traverse the complementary coordinate support. Hence any of the four choices of prefix from P or Q and suffix from P or Q yields a genuine full antipodal geodesic: no direction is repeated.

Write a chosen prefix A with last two directions (u,v) and a chosen suffix B with first two directions (w,t). The actual window-color word of AB consists, in order, of the interior three-windows of A, followed by

c(F_y({u,v,w});(u,v,w)),  c(F_y({v,w,t});(v,w,t)),

and then the interior windows of B. This follows by listing consecutive triples of the concatenated direction word; exactly two triples straddle the seam. The two displayed windows are physical faces at the common midpoint, so root identification is exact.

Thus selecting a prefix and suffix whose interior words each have the desired constant phase leaves exactly two independently checkable seam colors. A monochromatic hub through y may repair both when its certified edge geometry matches the ordered pairs. Merely knowing that P and Q cross at y, or have balancing topological labels, does not settle those seam colors.

## Closure obligation

The four-way splice lemma converts a topological or counting coincidence into a finite set of physical seam checks. The opposite-color diamond supplies locally rich candidates but can be blocked by ordered-cap colors on shared physical faces. A global connector theorem must force one successful choice across a compatible family of roots or cut positions. This is the precise interface between local bichromatic hub abundance and full one-switch antipodal extraction.

### Bichromatic root diamonds and mixed terminal cap obstruction

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

### Bichromatic six-move hubs and two-color connector density

# Bichromatic six-move hubs and two-color connector density

A vertex supporting monochromatic four-geodesics in both colors is a bichromatic hub. Its incoming and outgoing directions support many genuine six-edge paths that are at most one switch away from monochromaticity. Quantifying those paths reveals forced root packets and separators under the additional hypothesis that no physical edge is certified in both colors.

## The unrestricted NORI root-chart gap has TWO logically independent missing obligations

The proved nonlinear fault robustness theorem nori_quadratic_nonlinear_triple_fault_robust_antipodal_chart_closure_20261008 is substantial, but DOES NOT itself approach arbitrary NORI through chart connectivity alone. Its exact proof requires TWO separate parity-reference features, both unavailable for an arbitrary active ordered-three-face coloring:

**(I) PREFIX POLARIZATION / SUFFIX FORCING.** Fix an ordered list p of outside directions D=[n]\K and a root x where its D-prefix is monochromatic. To force the three exceptional terminal windows to ALTERNATE under hypothetical grand failure, the proof flips ONE K-coordinate s_1 which is free in each of the last three windows, hence does not change their actual physical ordered-face colors. What is ALSO necessary is that this same bit flip sends ALL preceding D-only window colors from q to 1−q, keeping the preceding block monochromatic. Full exterior parity supplies precisely this property: each early face has s_1 as an exterior coordinate, so toggling its root bit flips every early color. An arbitrary NORI coloring need not have this property. NORI oddness only relates (F,π) to (bar F,rev π), not two D-only faces differing in a SINGLE outside K-bit at the same orientation.

**(II) ANTIPODAL CHART CONNECTIVITY.** Even if a root-specific antipodally odd suffix bit t(S) is successfully manufactured, to contradict it one needs a chain of ACTUAL monochromatic-prefix reachability witnesses whose first exceptional physical ordered faces agree and whose roots connect S to bar S. The clean parity baseline gives the six-periodic root code S_{p_{j+3}}=1−S_{p_j}, whose middle-layer chart graph has this connectivity. For arbitrary c, the set of monochromatically reachable prefixes and their physical face incidence may be sparse, disconnected, or lack this root-coupled structure. Connectedness of the separate physical certified-four-square complex does NOT automatically imply connectivity of a terminal-memory-compatible root chart.

**THEOREM (safe abstract two-obligation NORI extraction).** Fix K of size3, D its complement. Suppose a collection \mathscr P of D-direction geodesic witnesses possesses all the following genuine properties:
(a) For every outside root S in a set G invariant under complementation, there is a selected D-order p and K-root assignment with a monochromatic D-prefix, and for EACH of the 6 orders of K the corresponding first three exceptional windows refer to the actual physical colored faces.
(b) Each selected D-order witness is **polarized**: there exist two K-root choices yielding identical actual exceptional three-window colors but opposite uniform monochromatic prefix bits. Consequently under no full good geodesic the last three exceptional windows have at least2 internal changes, hence alternate.
(c) The six-order/reversal physical-face comparisons align these alternating suffixes into one well-defined label t:G→F2, independent of selected p, with t(bar S)=1−t(S).
(d) The graph on G linking selected root witnesses with IDENTICAL actual first exceptional physical ordered faces has a component containing S and bar S.
Then the full NORI one-switch conclusion follows.

**Proof.** Under no full good path, (b) forces the alternating suffix for each selected witness by comparing opposite prefix colors against the SAME suffix. Conditions (c) and (d) make t locally constant along a certified chain from S to bar S, while antipodal oddness makes it complementary at the two endpoints. Contradiction. QED.

**CAUTION.** The theorem is a modular, CONDITIONAL extraction theorem. Conditions (b) and (c) are NOT inherent to arbitrary monochromatic-prefix reachability and must be genuinely proved from each new construction; condition (d) is a separate topological forcing obligation. Simply declaring an uncolored reachability set R(x), an antipodal involution, or a connected lower-dimensional certified square complex does NOT discharge either obligation. An alternative global strategy is to target the already proved EXACT color-free reversed-two-tail complementary-support intersection, which bypasses the need for these polarization hypotheses entirely and automatically splices a full one-switch path.

**Main direction after latest robust closure.** Seek a topological connector theorem on actual reversed-terminal-memory reachability basins that forces complementary supports, rather than extrapolating the reference-dependent parity-root synchronization to unrestricted face colors.

## Every bichromatic hub has a local common-edge or uniform-cap alternative

Let \(n\ge6\) and let \(c\) satisfy the active NORI physical ordered-three-face axiom \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). Let \(X_c\) be the genuine certified-middle-square complex of NORI. At a cube vertex \(z\), let \(K_z(i)\subseteq\{0,1\}\) be the set of colors \(q\) of actual centered monochromatic four-edge connectors whose middle-pair square contains the **incident physical cube edge** \(\{z,z\oplus e_i\}\). Every incident certified square carries the same certificate color at each of its four vertices; by the centered-link theorem all but at most one \(K_z(i)\) are nonempty.

Call \(z\) **bichromatic** if \(\bigcup_i K_z(i)=\{0,1\}\). Every valid active NORI coloring has at least one bichromatic \(z\), by the proved connected-certified-square topological overlap theorem.

**Theorem (local hub dichotomy, without any global shadow restriction).** For **every** bichromatic \(z\), one of the following alternatives holds.

**(I) A local color-overlap edge.** There exists a direction \(i\) such that \(K_z(i)=\{0,1\}\). This is an actual physical edge at \(z\), lying in two genuine centered monochromatic-connector squares of opposite colors.

**(II) A locally rigid two-color direction partition.** All nonempty \(K_z(i)\) are singleton sets. Put
\[
A_z=\{i:K_z(i)=\{0\}\},\quad B_z=\{i:K_z(i)=\{1\}\}.
\]
Then \(|A_z|,|B_z|\ge2\), \(|A_z|+|B_z|\ge n-1\), and for **every** actual ordered three-face through \(z\) with distinct ordered free directions \((u,v,w)\), when \(v\in A_z\cup B_z\) and one of \(u,w\) belongs to the opposite class,
\[
\boxed{c(F_z(\{u,v,w\}),(u,v,w))=\mathbf1_{\{v\in B_z\}}.}
\tag{1}
\]
In particular, for every mixed omission \(a\in A_z,\ b\in B_z\), every \(i\notin\{a,b\}\), and every choice of the omitted two starting bits above the projected \(U\)-root \(r=z|_U\), \(U=[n]\setminus\{a,b\}\), the actual cap labels are **uniform**:
\[
\boxed{c(F(x;\{a,b,i\}),(a,b,i))=1,\quad
c(F(x;\{a,b,i\}),(b,a,i))=0.}
\tag{2}
\]
Consequently, **a single monochromatic \(U\)-spanning geodesic from any of those four parallel-facet roots directly yields a full NORI geodesic with at most one color change**. Under hypothetical grand failure, all \(4|A_z||B_z|\) such root/bundle choices are free of any monochromatic \(U\)-spanning geodesic, with at least \(2(n-3)\) distinct forbidden mixed omission pairs.

**Proof.** If (I) is false, the sets \(A_z,B_z\) are disjoint. Each of the two certified monochromatic four-path colors at \(z\) certifies a physical square and hence at least two distinct incident coordinate directions; thus both classes have size at least two. At most one direction is isolated by the established \(n-1\) certified-degree theorem, giving \(|A_z|+|B_z|\ge n-1\). Every cross middle pair \(v\in A_z,w\in B_z\) is **uncertified at \(z\)**: any monochromatic middle-square certificate of color \(q\) would place the same bit in both already oppositely certified edge-label sets \(K_z(v)=\{0\}\) and \(K_z(w)=\{1\}\).

For a fixed ordered cross pair \((v,w)\), write \(I_t=c(F_z(\{t,v,w\}),(t,v,w))\), \(O_s=c(F_z(\{v,w,s\}),(v,w,s))\) for distinct outer \(t,s\notin\{v,w\}\). Since every centered four-path \((t,v,w,s)\), \(t\ne s\), is nonmonochromatic, \(I_t\ne O_s\). At least three outer coordinates exist since \(n\ge6\); comparing values using a common third outer direction forces every \(I_t\) to equal one bit \(K_{vw}\) and every \(O_s=1-K_{vw}\). Repeating this for the reverse cross orientation gives \(K_{wv}\). Shared physical ordered-face triples with two \(A_z\) and one \(B_z\), or vice versa, yield exactly the compatibility equations
\[
K_{wv'}=1-K_{vw}\quad(v,v'\in A_z,\ w\in B_z,\ v\ne v'),
\]
\[
K_{v w'}=1-K_{wv}\quad(w,w'\in B_z,\ v\in A_z,\ w\ne w').
\]
Since both classes have size at least two and at least one has at least three, elementary elimination of these equations gives a common bit \(K\) on all \(A\to B\) cross pairs and bit \(1-K\) on all \(B\to A\) cross pairs. Choose a genuine color-0 certified middle square at \(z\) with middle pair \(v,v'\in A_z\). Choose distinct outer \(w,w'\in B_z\). The ordered four-path \((w,v,v',w')\) has both window colors \(K\) by the cross-pair constraints, so it is a monochromatic certificate of color \(K\) on the SAME physical square that was already certified color 0. Since (I) is false, \(K=0\). The resulting incoming/outgoing cross-triple formulas yield (1), by whether the middle coordinate is in \(A_z\) or \(B_z\).

For \(a\in A_z,b\in B_z\), the ordered cap triples \((a,b,i)\), \((b,a,i)\) have their middle direction respectively in \(B_z\), \(A_z\), and an opposite-class adjacent direction. Thus their colors at \(z\) are 1 and 0. The physical face has both \(a,b\) free, so varying those two bits does not alter its identity, proving (2) simultaneously in all four parallel facets.

If \(P\) is a monochromatic full \(U\)-geodesic from one such facet root, color \(q=0\), prepend \((a,b)\) starting at the appropriately shifted full root. The new first cap has color 1 and the first original face color is 0; the one intermediate new window has arbitrary color, so the resulting full word has exactly one change. If \(q=1\), append \((b,a)\), whose final cap is \(1-c(F(x;\{a,b,j\}),(a,b,j))=0\) by the active antipodal-reversal law, and again there is exactly one change regardless of the intermediate color. Thus either monochromatic \(P\) forces grand closure.

Finally if \(|A_z|=p, |B_z|=q\), \(p,q\ge2\), \(p+q\ge n-1\), then \(pq\ge2(n-3)\). This counts distinct mixed omission pairs. \(\square\)

**Strength over earlier results.** Previously the mixed-direction selector theorem and uniform-cap blockade were stated inside global square-edge shadow alternative B, where *no* physical edge anywhere in the cube has both certification colors. The proofs actually use only **lack of a doubly certified incident edge at the chosen bichromatic center**. This local theorem therefore applies even in colorings where alternative A occurs elsewhere. It supplies a site-by-site topological obstruction to combine with genuine opposite-color edge overlaps, without an artificial global case split.

**Remaining closure obligation.** The theorem does not guarantee a monochromatic near-spanning \(U\)-geodesic for any prescribed projected root. To prove full NORI, one would need a fixed-point/connector principle forcing, for some bichromatic hub, either (I) an opposite-color common-edge configuration whose witnesses can be extended compatibly, or (II) one of the many forbidden near-spanning monochromatic cores. An opposite-color shared edge alone is also not yet a full-geodesic certificate. The new statement is exact and dimension independent, not grand closure.

## Topological global consequence: monochromatic six-geodesic hubs meet every certified antipodal path in the unique-color edge-shadow regime

Let n>=10 and let c be an ACTIVE NORI binary coloring of physical ordered three-faces. Assume the GLOBAL unique-color certified-square edge-shadow case B: no physical cube edge receives square certificates from monochromatic centered four-edge connectors of both colors. Let X_c be the genuine certified-center-square complex, let G_c=X_c^(1) be its spanning cube subgraph, and write M=E(Q_n)\E(G_c). By proved NORI theorems, M is an antipodally invariant matching, G_c is connected, and every vertex has certified-center degree at least n−1. Define the bichromatic hub set
\[
B=\{z: \text{genuine centered monochromatic four-edge connectors of BOTH colors exist at z}\},
\]
and the MONOCHROMATIC SIX-HUB set
\[
H_6=\{z: \text{there exists an ACTUAL monochromatic six-edge cube geodesic with ALL FOUR ordered-three-face windows physically containing z}\}.
\]

**THEOREM 1 (unavoidable monochromatic six-hub separator).** Under the stated assumptions,
\[
\boxed{B\subseteq H_6.}
\]
Moreover every G_c-graph path from any cube vertex x to its antipode bar x intersects H_6. In particular, for EVERY root x∈Q_n there exists a FULL antipodal n-edge cube geodesic from x to bar x (whose edges all belong to G_c) that passes through at least ONE vertex z∈H_6.

**Proof.** At each bichromatic hub z, the no-common-edge assumption splits the incident certified directions into two classes A,B, each of size at least2, of total size at least n−1. Since n>=10, the larger class has cardinality at least5. The proved five-majority odd-cycle theorem (Item nori_majority_five_bichromatic_hub_odd_cycle_forces_monochromatic_six_20261008) constructs a genuine monochromatic six-edge geodesic through z. Thus B⊆H_6.

The separate, unconditional bichromatic-hub antipodal separator theorem (Item nori_bichromatic_mono_four_hubs_hit_every_certified_antipodal_path_density_20261008) states that EVERY G_c-path from x to bar x meets B, since physical square certificates share a common monochromatic color across each G_c-edge, but the hub singleton color label flips under antipodality. Such a path consequently meets H_6.

Finally the general cube matching-avoidance theorem (Item nori_matching_avoidance_every_root_full_geodesic_20261008) says any cube matching that is NOT the entire set of parallel edges of one coordinate can be avoided by SOME full antipodal geodesic from ANY prescribed root x. Our matching M cannot be that entire parallel matching because G_c is CONNECTED and would otherwise split into opposite coordinate facets. Therefore from every x there is a full M-avoiding geodesic P(x), which is a G_c-path. It meets H_6. QED.

**THEOREM 2 (quantitative density of monochromatic six-hubs).** The same model satisfies
\[
\boxed{|H_6|\ge |B|\ge
\frac{2^n-2|M|}{n+1}.}
\]
Both hub sets are antipodally invariant. In the special case M=∅, at least a fraction 1/(n+1) of all Q_n vertices are centers of GENUINE monochromatic six-edge geodesics:
\[
|H_6|\ge 2^n/(n+1).
\]

**Proof.** Apply B⊆H_6 to the existing quantitative bichromatic-hub separator bound. Global antipodal reversal carries every monochromatic six-edge path through z to a complementary-color monochromatic six-edge path through bar z; hence H_6 is antipodally invariant. QED.

**Conceptual topological result.** This produces, in one structural branch of arbitrary ACTIVE NORI colorings, a physical Q_n antipodal hitting set of ACTUAL SIX-edge monochromatic paths. Its strength is global and root-mobile: the center of such a path is encountered by a fully spanning antipodal route from EVERY starting cube root, but the mono-six direction word may not match the route's entering/leaving used-direction support, and the route's unrelated local certificates need not share the mono-six color. The unproved GRAND-EXTRACTION step is to synchronize at least one of these mono-six hubs with a full legal root/terminal-memory geodesic so that its entire ordered-three-face word has <=1 switch. This theorem does not assert such synchronization.

Hub abundance is a robust local theorem. Extending those six-move witnesses to a full n-move geodesic without accumulating extra window defects is the outstanding global problem.

### Near-midpoint hub witnesses and concrete splice-failure tests

# Near-midpoint hub witnesses and concrete splice-failure tests

High-index permutation arguments force authentic endpoint-opposed geodesics and central physical-face interactions near the midpoint of the cube. The core question is whether such witnesses can be cut and reassembled along a common actual vertex without creating too many new window-color changes. The local connector calculations below keep all four possible splices, not just an abstract sign coincidence.

## A genuine two-seam splicing law at a common physical hub; locally rigid bichromatic hubs automatically repair both seams

Let n>=6, and let c be ANY binary coloring of physical ORDERED three-faces of Q_n. Let P and Q be two genuine full directed antipodal cube geodesics rooted at SAME physical vertex x, with direction words
\[
P=(a_1,\ldots,a_\ell,b_1,\ldots,b_{n-\ell}),\qquad
Q=(a'_1,\ldots,a'_\ell,b'_1,\ldots,b'_{n-\ell}),
\]
for some 3<=ell<=n-3, and suppose their first-ell used-direction sets coincide:
\[
\{a_1,\ldots,a_\ell\}=\{a'_1,\ldots,a'_\ell\}=S.
\]
Thus BOTH pass at time ell through the SAME physical cube vertex y=x⊕S. ALL FOUR paths obtained by choosing either prefix and either suffix are genuine full antipodal geodesics, because the first block uses S and second block uses its coordinate complement.

**THEOREM 1 (exact physical two-window splice).** Given any prefix A with last directions (u,v) and any suffix B with first directions (w,t), the ordered-three-face color word of their full splice A B is
\[
\boxed{\operatorname{Int}_3(A),\
c(F(y;\{u,v,w\}),(u,v,w)),\
c(F(y;\{v,w,t\}),(v,w,t)),\
\operatorname{Int}_3(B).}
\]
Here \operatorname{Int}_3(A) is the actual color word of the ell-2 ordered three-face windows entirely inside A, and \operatorname{Int}_3(B) is the actual color word of the n-ell-2 windows entirely inside B, preserving each branch's physical face identities. In particular BOTH NEW splice windows are actual ordered physical three-faces THROUGH THE SAME PHYSICAL INTERMEDIATE VERTEX y; they are not virtual/interpolated colors.

**Proof.** All windows wholly before/after the cut preserve precisely the same physical exterior bits, because both choices of prefix reach the same y. There are exactly two crossing windows of ordered directions (u,v,w) and (v,w,t). Their physical first vertices lie respectively at y⊕u⊕v and y⊕v, so each corresponding free-face contains y. This is the displayed formula. QED.

**THEOREM 2 (automatic seam compatibility at a locally rigid bichromatic hub).** Assume additionally that y is a bichromatic hub in the LOCAL UNIQUE-CERTIFIED-COLOR case of Item nori_every_bichromatic_hub_local_shared_edge_or_uniform_mixed_cap_dichotomy_20261008. Let A_y,B_y be its genuine certified incident direction color classes, with assigned bits h(i)∈{0,1}. Suppose the LAST prefix direction v belongs to A_y∪B_y, the FIRST suffix direction w belongs to A_y∪B_y, and their certified bits differ:
\[
h(v)\ne h(w).
\]
Then regardless of the neighboring directions u,t, the two actual crossing window colors are
\[
\boxed{c(F(y;\{u,v,w\}),(u,v,w))=h(v),\quad
c(F(y;\{v,w,t\}),(v,w,t))=h(w).}
\]
This follows DIRECTLY from the proved local mixed-middle selector at y: in each ordered triple, the MIDDLE direction has a neighboring free direction in the opposite certified color class.

**COROLLARY 3 (actual full one-switch extraction from compatible monochromatic branches).** Under Theorem2, suppose A is a genuinely MONOCHROMATIC ell-edge geodesic from x to y of ordered-window color h(v), and B is a genuinely MONOCHROMATIC (n−ell)-edge geodesic from y to bar x of ordered-window color h(w). Then their full concatenation P=A B is a full antipodal directed geodesic with ordered-face window-color word
\[
h(v)^{\ell-1}\ h(w)^{n-\ell-1},
\]
and hence has EXACTLY ONE change. It works regardless of the direction order in the rest of A or B.

**COROLLARY 4 (exact additive defect formula for nonmonochromatic branches).** Under Theorem2, suppose the LAST internal ordered window of A has color h(v), and the FIRST internal ordered window of B has color h(w), but their other windows may change. Let d_A,d_B be the number of changes in their respective internal window-color words. Then the full spliced word has
\[
\boxed{D(A B)=d_A+d_B+1.}
\]
Indeed the two new splice windows match their adjacent internal side colors and differ exactly once from one another. Thus local hub certification supplies a ZERO-EXCESS connector: there are NO uncontrolled seam changes. In particular, if d_A=d_B=0, grand closure is immediate.

**RELATION TO THE TOPOLOGICAL TUCKER PAIR.** Item nori_odd_dimension_permutohedral_tucker_common_vertex_opposite_mirror_switch_pair_20261008 proves unconditionally, in EVERY odd n>=7 and at EVERY root x, TWO actual endpoint-opposed full paths P,Q sharing some proper interior vertex y and carrying opposite mirrored switch labels. Theorem1 now turns this topologically forced common vertex into an ACTUAL two-seam geodesic rectangle, with both seam colors lying in physical faces through y. If y is a locally rigid bichromatic hub and the boundary directions of one of the four splice combinations cross the certified A_y/B_y cut with matching adjacent window colors, then Corollaries3-4 give exact switch-controlled extraction/defect bookkeeping. Such additional properties of y or the splice do not follow automatically from the Tucker pair theorem and remain the outstanding GLOBAL COMBINATORIAL task.

**Scope.** Theorem1 uses no NORI antipodal law; Theorem2 uses physical hub rigidity proved under ACTIVE NORI. The topological pairing and the one-switch extraction are both rigorous but their unconditional conjunction is NOT proved. No claim of unrestricted grand closure is made.

## Kneser forces a same-root, same-center, two-sided reversal square of genuine six-edge geodesics

Let n>=8 and let c be ANY binary coloring of actual physical ORDERED 3-faces of Q_n, not necessarily satisfying antipodal oddness. Fix ANY physical cube vertex z. For each ordered triple alpha=(a,b,c) of distinct direction names, define h_z(alpha) to be the physical color of the ordered 3-face through z with ordered free directions alpha.

**Theorem (unconditional centered six-edge two-sided reversal square).** There exist DISJOINT unordered direction triples A,B with ordered orientations alpha=(a1,a2,a3) on A and gamma=(b1,b2,b3) on B, and two bits q,r∈{0,1}, such that
\[
h_z(\alpha)=h_z(\operatorname{rev}\gamma)=q,\qquad
h_z(\operatorname{rev}\alpha)=h_z(\gamma)=r.
\tag{1}
\]
Consequently from the ONE SAME ROOT x=z XOR A to the ONE SAME ENDPOINT y=z XOR B there exist FOUR ACTUAL six-edge direction-distinct geodesics:
\[
P_{00}=(\alpha,\operatorname{rev}\gamma),\quad
P_{01}=(\alpha,\gamma),\quad
P_{10}=(\operatorname{rev}\alpha,\operatorname{rev}\gamma),\quad
P_{11}=(\operatorname{rev}\alpha,\gamma).
\tag{2}
\]
All four traverse the SAME physical hub z at their midpoint after three moves, and ALL FOUR physical ordered-three-face window faces of EVERY path contain z. Their initial/final ordered-window color pairs are the complete two-by-two table
\[
\begin{array}{c|cc}
 &\operatorname{rev}\gamma&\gamma\\
\hline
\alpha&(q,q)&(q,r)\\
\operatorname{rev}\alpha&(r,q)&(r,r)
\end{array}.
\tag{3}
\]
In particular the two diagonal paths P00 and P11 each have either ZERO or EXACTLY TWO ordered-window color changes (since their four-window color words begin and end with the same bit). The other two have opposite endpoint colors precisely when q≠r. NO conclusion is asserted about the two interior window bits or the existence of a monochromatic/one-switch SIX-edge path.

**Proof.** Associate to each unordered 3-set T the pair (h_z(alpha_T),h_z(rev alpha_T)), for an arbitrarily selected orientation alpha_T. Orientation reversal interchanges the two bits. Up to this interchange there are exactly THREE orbit types: 00,11,{01,10}. Thus the unordered 3-subsets of [n] are colored with THREE types. The classical Kneser chromatic theorem gives chi(KG(n,3))=n-4>3 for n>=8, so two DISJOINT triples A,B have the same orbit type. Reorient alpha and gamma so that the second triple signature is the SWAPPED signature of the first, yielding precisely the two equations (1). For n>=10 one may avoid the named Kneser input and instead use the elementary cyclic-interval disjoint-triple count already proved in Item nori_same_order_antipodal_root_pairs_endpoint_opposition_disjoint_triple_orbits_20261008.

Every word in (2) uses the same six distinct directions A union B, first the A directions then B, so from root x=z XOR A each reaches z after 3 moves and then ends at y=z XOR B. The four length-three free-coordinate windows begin at path positions1,2,3,4. In window1 the already fixed directions outside the first triple are still at their z-bits, because root differs from z only in the three FREE A bits. In windows2,3 the remaining untraversed A directions are still the only differing bits from z and are FREE in the window. After the third move the path is at z; window4 is the B-face through z. Hence ALL four physical face windows contain z. Their first and last ordered free triples are just the selected A and B orientations; (1) gives their color pairs (3). An even-parity number of changes follows for a four-bit word whose first/last bits agree, so the diagonal words have 0 or2 changes. \(\square\)

**Topology-first significance.** This creates at EVERY physical hub a literal four-vertex square in the space of genuine SAME-root/SAME-endpoint six-edge paths, indexed by two INDEPENDENT reversals of 3-direction prefix/suffix blocks. Unlike a fixed-root pair of unrelated endpoint-balanced full paths, these four certificates have a COMMON midpoint z and complete agreement of their used support. The input is a TOPLOGICAL Kneser coloring obstruction with only three signature orbits. Under active NORI oddness the four-path square also has the usual physically antipodal mate centered at bar z with complemented-reversed ordered windows.

The unresolved step is to transport this certified six-edge square through the other n−6 directions, using physical face incidence/root slides, so that an equivariant fixed-point collision produces a complete n-edge path with ≤1 change. The diagonal endpoint-equality condition alone is weaker than monochromaticity, and cannot be inflated to a global grand result without controlling the two middle seam windows and later exterior-bit changes.
## Elevation: why a fixed-hub six-square cannot be extended by preserving its two end faces

Assume n>6, and fix disjoint triple supports A,B with ordered first/last physical face windows BOTH passing through the SAME physical vertex z, as in the theorem. Let C=[n]\(A union B), nonempty.

**Exact no-lift corollary.** NO full n-edge geodesic can have those two fixed physical windows as its first and last ordered-three-face windows. More strongly, any geodesic containing them in the corresponding order has window-index separation EXACTLY 3, with NO coordinate outside A union B traversed between them. Indeed for every i outside A union B, their fixed exterior bits are both z_i. The exact physical two-window incidence theorem says their intermediate support is precisely the directions with DIFFERENT exterior bits, so it is empty. To extend the six-path into an n-path while keeping those end windows, any remaining directions must be traversed BEFORE the first or AFTER the last named window; either choice prevents those two windows from being the first/last of a FULL n-geodesic. Thus the Kneser six-square CANNOT be inflated into a full geodesic by inserting n−6 unused directions between its two 3-blocks without altering at least one endpoint physical face.

Likewise its full four-window path has no nontrivial root-translation symmetry preserving ALL its physical window faces: the intersection of its four free-coordinate triples is EMPTY. A root bit toggle in any direction changes the physical face of at least one of the four windows. This explains why genuinely mobile-root higher-dimensional cells must compare DIFFERENT physical faces and track the resulting color changes rather than freezing a common hub z.

The no-lift is a geometric compatibility obstruction, NOT a NORI counterexample. It pinpoints what an equivariant transport theorem has to accomplish: move and reassign physical face windows while maintaining enough certified reachability memory to preserve the one-change extraction.


## Exact moving-hub shift representation and its certified root squares

**Setting.** Let n>=5. For any binary coloring C of physical ordered three-faces of Q_n, define its hub table h_z(a,b,c)=C(F(z;{a,b,c}),(a,b,c)), where z is a cube vertex and a,b,c are distinct coordinate directions.

**Theorem 1 (complete hub coordinates).** The tables satisfy h_(z xor e_t)(a,b,c)=h_z(a,b,c) for t in {a,b,c}. Conversely any family with these invariances defines a unique physical ordered-three-face coloring. Its active NORI antipodal oddness is precisely h_(bar z)(c,b,a)=1-h_z(a,b,c).

Proof: toggling a free coordinate leaves its physical face unchanged, and any two points of a face differ only in free coordinates. The antipodal face contains bar z and reverses the ordered free tuple under the axiom.

**Theorem 2 (EXACT PATHWISE moving-hub identity).** For ANY full rooted geodesic (x,p), p=(p_1,...,p_n), let z_i=x xor e_(p_1) xor ... xor e_(p_i) and t_i=(p_i,p_(i+1),p_(i+2)) for i=1,...,n-2. If w_i denotes its ACTUAL physical ordered-three-face window color then
  w_i=h_(z_i)(t_i),
  h_(z_i)(t_(i+1))=h_(z_(i+1))(t_(i+1)),
and consequently each switch indicator is
  w_i xor w_(i+1)=h_(z_i)(p_i,p_(i+1),p_(i+2)) xor h_(z_i)(p_(i+1),p_(i+2),p_(i+3)),  i=1,...,n-3.
These are pointwise equations for EACH path, independent of any averaging or choice of a different witness.

Proof: the i-th physical window, with free directions t_i, contains both z_(i-1) and z_i, so its color is h_(z_i)(t_i). The hubs z_i,z_(i+1) differ in p_(i+1), which belongs to the free set of t_(i+1), so invariance gives the second identity.

**Exact admissible zigzag model.** Use states (z,t), z a cube vertex and t an injective ordered triple. Horizontal arrows at fixed z shift (a,b,c) to (b,c,d), d distinct; vertical arrows flip a coordinate in the fixed triple t, preserving h exactly. Each genuine full n-edge geodesic yields the zigzags
 (z_i,t_i) -> (z_i,t_(i+1)) -> (z_(i+1),t_(i+1))
for i=1,...,n-3, where the second arrow flips p_(i+1). Its switches are precisely its color-changing horizontal arrows. A valid zigzag must also come from one globally injective length-n direction word and coherent root x; arbitrary walks in this enlarged graph do not automatically encode cube geodesics. Grand closure is exactly existence of an admissible full zigzag with <=1 color-changing horizontal arrow.

**Theorem 3 (two certified commuting root directions).** The switch bit s_z(a,b,c,d):=h_z(a,b,c) xor h_z(b,c,d) is unchanged when z is toggled in coordinate b, c, or both. Thus each horizontal arrow has a geometrically certified square of four parallel horizontal comparisons over the 2-dimensional root face on {b,c}, with identical switch values. Toggling a changes the physical (b,c,d)-face while leaving the (a,b,c)-face fixed, and toggling d changes the physical (a,b,c)-face while leaving the (b,c,d)-face fixed; the geometry alone imposes no analogous invariance for a or d.

Proof: the two ordered triples share exactly their middle two directions {b,c}. Invariance of both face colors under toggling either shared coordinate proves the equalities. The remaining toggles change exactly one of the two actual physical faces; its color can be independently prescribed (with antipodal reversed mates fixed by the NORI axiom).

**Corollary (a rigorous limitation on automatic pentagon annuli).** A centered physical shift pentagon on five distinct coordinates p_0,...,p_4 uses ordered face triples t_i=(p_i,p_(i+1),p_(i+2)) modulo five. Their five free sets have EMPTY intersection. Therefore no nonzero coordinate toggle is guaranteed by the physical-face invariance to preserve every vertex color of the pentagon at once. Merely tensoring a centered pentagon with a fixed root-direction edge is not a universally certified product annulus; any successful antipodally transported good-window annulus must allow nonuniform root/order repair with literal shared path certificates. This is a limitation of the automatic face-preserving operation, not a theorem forbidding other annuli.

**Theorem 4 (exact full-switch mean equals same-hub graph cut energy).** Define
 A(C)=[2^n*(n)_4]^{-1} sum_{z in Q_n} sum_{(a,b,c,d) injective} 1{h_z(a,b,c)=h_z(b,c,d)},
where (n)_4=n(n-1)(n-2)(n-3).
For a uniform root X and uniform direction permutation P,
  E[D(X,P)]=(n-3)*(1-A(C)),
where D is the number of color changes among its n-2 physical window colors. Moreover A(C)>=1/5 for any binary physical ordered-three-face coloring, without NORI oddness.

Proof: for every fixed switch position i, (z_i,p_i,p_(i+1),p_(i+2),p_(i+3)) is uniform over all cube vertices and injective ordered quadruples: conditioned on P, the map X->z_i is a bijection. The pathwise identity makes the probability of an equality exactly A(C), independent of i. Summation gives the expectation. To prove the lower bound, at each fixed hub z form the directed shift graph G_n: vertices are injective ordered triples and arcs are injective ordered quadruples (a,b,c,d) from (a,b,c) to (b,c,d). Every cyclic ordered 5-tuple of distinct directions yields a directed odd pentagon, necessarily containing at least one equal-color arc. There are (n)_5/5 distinct directed pentagons and each arc belongs to n-4 of them. Hence at least (n)_4/5 arcs are equal-colored at each hub, so A(C)>=1/5. This recovers the team's universal E[D]<=4(n-3)/5 theorem by an exact moving-hub graph calculation.

**Research frontier.** The pointwise hub identities and the 2-direction commuting root squares are genuine, dimension-independent local chart transitions. They give a concrete means to seek coherent moving-hub higher cells, linking the physical pentagon parity cocycle and the exact same-root complementary reversed-two-tail extraction. The full proof still requires a global certificate-preserving selection/holonomy/descent that synchronizes horizontal equalities along ONE admissible n-coordinate zigzag. The mean and the local commuting squares alone do not provide that selection; unrestricted grand NORI closure remains open.

**Theorem 5 (a universal genuine ROOT-MOVING essential seven-cycle).** Fix ANY five distinct directions (a,b,c,d,e), ANY physical hub z and ANY physical ordered-three-face coloring in n>=5. In the actual good-window shift graph (hence inside W_good) there is the following SEVEN-VERTEX SIMPLE CYCLE. Write [T;y] for the actual ordered face with ordered free triple T passing through hub y:
 u_0=[(a,b,c);z],
 u_1=[(b,c,d);z],
 u_2=[(c,d,e);z xor b],
 u_3=[(d,e,a);z xor b xor d],
 u_4=[(e,a,b);z xor b],
 u_5=[(a,b,c);z xor e],
 v=[(b,c,e);z].
Then
  u_0 - u_1 - u_2 - u_3 - u_4 - u_5 - v - u_0
is a cycle of SEVEN DISTINCT actual ordered physical windows. EVERY edge is the pair of consecutive ordered windows of an actual directed four-edge cube geodesic and therefore is genuinely certified as a W_good edge for EVERY coloring. It contains BOTH ordered (a,b,c)-faces with exterior e-bit differing by one.

Proof (literal intermediate hubs). For the first five edges the common actual hubs are, in order:
 z, z xor b, z xor b xor d, z xor b, z xor b xor e.
The ordered triple pairs are respectively
 (abc,bcd), (bcd,cde), (cde,dea), (dea,eab), (eab,abc).
Every pair shares the last two directions of the first tuple with the first two of the second, and its two face objects really pass through the stated common hub. Invariance in the free directions verifies all displayed hub representatives agree. For the last two edges, [(a,b,c);z xor e] and [(b,c,e);z] both pass through z xor e on their respective physical faces (e is free for the latter), and [(b,c,e);z] and [(a,b,c);z] share hub z. Their order as undirected shift edges is legitimate. Every such pair has the explicit four-edge certificate with direction order of the corresponding shift, starting at hub XOR its first direction. All listed vertices are pairwise distinct: the only repeated ordered direction triple is (a,b,c), and those two ordered physical faces differ in exterior bit e. QED.

**Nontrivial integral-mod-two temporal homology.** Every edge in this literal seven-cycle has physical face-center L1-distance one, so the established intrinsic temporal cocycle beta(edge)=distance mod2 evaluates to 7=1 in F2. Since beta extends as a genuine 1-cocycle on all W_good simplices, this cycle C_7 is NOT a boundary of any 2-chain in W_good and is nonzero in H_1(W_good;F2). Likewise the same-color connector cocycle alpha=beta+delta(color) evaluates to 1. In active NORI, the cycle projects to a closed path in W_good/tau with beta_bar=1 and covering voltage w=0 (it already closes upstairs).

**Exact exterior sensitivity parity.** Let E_j be the equality indicator (1 for equal colors, 0 otherwise) on the seven consecutive edges. Telescoping the endpoint color differences around the FIVE-edge segment u_0 -> ... -> u_5 yields
 sum_{j=0}^{4} E_j = 1 + h_z(a,b,c) + h_(z xor e)(a,b,c)   (mod 2).
Along the TWO-edge bridge u_5 -> v -> u_0, one has
 E_5+E_6 = h_z(a,b,c)+h_(z xor e)(a,b,c) (mod 2).
The sum around all seven edges is therefore 1, as required. This makes a cross-root physical-face derivative visible through a genuine five-window transport, while its two-edge shortcut canonically closes an odd homology cycle. The seven-cycle itself is a graph 1-cycle and DOES NOT supply a certified two-dimensional annulus, a cup product, or a full n-geodesic.

**Suggested next implication to prove.** Search for actual W_good triangles allowing two such exterior-bit seven-cycles on distinct coordinates d,e to commute through good-window path homotopies. Any resulting certified annular transport around an antipodal root loop would activate the team's proved beta_bar cup w forcing criterion. The current theorem provides explicit, universally valid root-mobile one-dimensional cycles and common physical hubs for that search, but does not establish commuting homotopies or grand closure.


**Audit addendum (physical good-window quotient, 2026-10-09).** The "certified root squares" in Theorem 3 are squares ONLY in the redundant hub-coordinate PARAMETER graph. Toggling either shared free direction b or c fixes BOTH underlying ordered physical faces, so the four hub-chart comparisons all project to ONE and the SAME edge of the actual good-window complex W_good. Therefore these squares are DEGENERATE after physical-face identification and must NEVER be counted as nondegenerate 2-cells, an annulus, or evidence for a mixed cup product in W_good. The first genuine exterior-root transport (toggle a direction e outside {a,b,c,d}) is the six-window hexagon completely classified in proved Item nori_exterior_root_transport_hexagon_exact_good_triangles_rigidity_dichotomy_20261009. Its local triangles may fail simultaneously; when present they collapse across free chord edges and leave an induced S1. This addendum sharpens the precise scope of the earlier state-space observation while preserving its pointwise identities and averaging theorem.


The explicit bad rectangles show that a common midpoint and opposite central colors alone are not a closure certificate. The repair complex must also control physical seam windows and their root-bit dependence.

## Maximal good paths and snake exchanges

# Maximal geodesics, endpoint blockers, and snake exchanges

Let c be a binary coloring of physical ordered three-faces of Q_n satisfying c(bar F,rev pi)=1-c(F,pi). A direction-distinct k-edge path from x is a geodesic; its k-2 consecutive ordered-face colors are its window word. Call the path good when this word has at most one change. We establish the extremal consequences of a hypothetical failure of full antipodal good-path closure, then compare maximal monochromatic snakes.

## Longest good paths have two oppositely colored end walls

Assume no full good path exists. Let P=(p_1,...,p_k) from x to y maximize k among good paths over all cube roots and direction orders. We have k<n. For k>=4 write its window word q^s r^t, with positive s,t and q≠r, and put T=[n]\S, S={p_j}. Such a two-phase description is necessary: if P were monochromatic, appending any d in T would introduce one window and still produce a good path, contradicting maximality.

Set a=p_(k-1), b=p_k, alpha=p_1, beta=p_2. For every d in T,
c(F_y({a,b,d});(a,b,d))=q,
c(F_x({d,alpha,beta});(d,alpha,beta))=r.
Indeed the appended color must differ from the final r, while the prepended color must differ from the first q. Prepending uses starting root x xor d, so its remaining windows are literally the original faces of P. Thus extension at either end produces precisely two color changes, q^s r^t q or r q^s r^t. Antipodal reversal makes the corresponding incoming windows at bar y color r and those at bar x color q. This is a two-ended physical blocker theorem for all globally longest good paths.

## Monochromatic endpoint snakes

Independently let P=(u_1,...,u_(k-2),a,b) be a globally longest q-monochromatic path with k<n and used set S; write T=[n]\S and m=|T|. Every unused d has terminal cap c(F_y({a,b,d});(a,b,d))=1-q. Antipodal reversal supplies a q-monochromatic three-edge path (d,b,a) ending at bar y, with starting root h xor d, where h=bar y xor {a,b}. Consequently the m first-level roots form a physical cube star. For every pair d,e in T there are two actual four-edge paths (d,e,b,a) and (e,d,b,a) rooted at h xor {d,e}. Their last ordered three-face windows already have color q. Their respective first windows have colors c(F_h({b,d,e});(d,e,b)) and c(F_h({b,d,e});(e,d,b)). This gives an exact Johnson J(m,2) configuration of potential merging roots: the roots are indexed by unordered two-subsets, with distance two corresponding to Johnson adjacency. The first-window bits may be assigned independently in legal reversal-odd physical colorings, so the geometry alone forces no monochromatic merge.

For any A subseteq T, let r_A=h xor A. A q-monochromatic incoming path with direction order consisting of A followed by (b,a) witnesses that A is in the incoming snake family. The family contains every singleton and is accessible by deleting the first direction of a witness; it is not automatically a downward-closed family. Reversing antipodally identifies these witnesses with (1-q)-monochromatic paths from y beginning (a,b). The distinguished top root is r_T=x xor {a,b}. This is the only rank at which the root agrees with the translated original path in the standard complementary reversed-two-tail extraction.

## A conditional row-merging theorem

Suppose the q-monochromatic P above is globally longest of its color, k>=4, and |T|>=2. Put v=u_(k-2), w=u_(k-3), t=y xor {a,b}, and let alpha be the color of the genuine (w,v,b) seam after replacing the last pair (a,b) by b. For d in T let beta_d color the corresponding (v,b,d) seam. If alpha=beta_d=q, then for each e in T\{d} the path (u_1,...,u_(k-2),b,d,e) has all preceding windows q and final window gamma_de=c(F_t({b,d,e});(b,d,e)). Its length k+1 contradicts maximality if gamma_de=q; hence gamma_de=1-q. Antipodal reversal gives c(F_h({b,d,e});(e,d,b))=q. Together with the forced q-colored terminal (d,b,a) window, the actual four-edge path (e,d,b,a) from h xor {d,e} to bar y is monochromatic q. One admissible seam direction therefore certifies m-1 complete merge branches.

If instead alpha=q and every beta_d=1-q, consider the remaining seam (v,b,a). When it has color q, swapping the final two directions gives another q-monochromatic k-edge path with the same endpoints. When it has color 1-q, the shortened monochromatic prefix ending in b has a blocked terminal fan including a and all unused directions. This supplies a precise exchange alternative; maximality of the shortened prefix is an additional condition for iteration.

## Locality of adjacent direction exchanges

Swapping consecutive directions p_i,p_(i+1) preserves the root, endpoint and support. The prefix vertices coincide through step i-1 and from step i+1 onward, so every physical ordered three-face window beginning outside [i-2,i+1] stays identical. Thus only four consecutive window colors and their boundary comparisons require recertification. Conversely, there exist legal reversal-odd colorings in every n>=5 for which every insertion of a single missing direction into a specified near-spanning good word is bad. Any successful maximal-path argument must therefore prove progress using a family of genuine reroutings or a compatible complementary-support witness.

The open global step is a terminating exchange or equivariant incidence theorem for these physically rooted path families. The endpoint blocker laws, Johnson roots, and adjacent swaps provide exact inputs to such a theorem; none individually implies a full one-switch antipodal geodesic.

### Maximal geodesic blockers and snake exchanges

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
