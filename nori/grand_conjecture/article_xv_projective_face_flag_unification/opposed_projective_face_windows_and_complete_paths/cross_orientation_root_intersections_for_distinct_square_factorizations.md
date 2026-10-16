# Cross-orientation root intersections for distinct square factorizations

### Cross-orientation intersection for crossed square factorizations

For a cube-edge coloring \(f\), let \(A_0(f)\) and \(A_1(f)\) be the roots admitting full dimension-simple geodesics with color words \(0^*1^*\) and \(1^*0^*\), respectively. Fix two perfect matchings \(M,N\) of the \(2r\) dimensions. Suppose \(f\) is a Cartesian product of arbitrary colored squares on the pairs in \(M\), and \(g\) is a product of arbitrary colored squares on the pairs in \(N\). Let \(c(M,N)\) be the number of connected components of the multigraph \(M\cup N\), which is a union of even cycles, allowing parallel-edge cycles of length two.

**Lemma 1 (binary cycle feasibility).** A cycle of \(m\ge2\) Boolean variables, with one constraint per consecutive pair forbidding at most one two-bit pattern, has at least two satisfying assignments.

*Proof.* Add an arbitrary forbidden pattern to every unconstrained pair. Delete the last constraint. Either initial bit can be extended greedily across the remaining path, because for each fixed earlier bit at least one choice of the next bit is permitted. The deleted constraint can reject at most one of the two constructed assignments, since they have different initial bits. Hence a satisfying assignment exists.

If there were only one solution, changing any single variable would have to violate an adjacent constraint. Each currently satisfied pair constraint can forbid changing at most one of its endpoints, because its forbidden two-bit pattern differs from the current pair in at least one bit. With \(m\) constraints guarding \(m\) variables, each constraint must guard one endpoint. Thus on every edge the forbidden pattern differs from the solution's pattern in one bit. Complementing all variables changes both bits on every edge and avoids all forbidden patterns, giving a second solution. QED.

**Theorem 2 (cross-matching feasible-root intersection).**
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{c(M,N)}.}
\tag{1}
\]
The bound is sharp for every pair \(M,N\).

*Proof.* By the two-cube favorability lemma, each of \(A_0\) and \(A_1\) excludes at most one of the four roots of a colored square. The Cartesian product property identifies common feasible roots with Boolean assignments satisfying one such forbidden-pattern constraint on each edge of \(M\cup N\). Apply Lemma 1 independently to its cycle components.

For sharpness, put on every square the two-cube coloring \(h\) with \(A_0(h)=Q_2\setminus\{00\}\), \(A_1(h)=Q_2\setminus\{11\}\). The \(M\)-constraints then say \(x_u+x_v\ge1\), while the \(N\)-constraints say \(x_u+x_v\le1\). On a component containing \(2s\) variables, summing the inequalities in either matching yields \(\sum x_i\ge s\) and \(\sum x_i\le s\). All inequalities are tight, so every pair of neighboring bits is complementary. Each even cycle permits just its two alternating assignments, attaining (1). QED.

**Corollary 3 (two common roots in unbounded dimension).** Take \(M=(1,2),(3,4),\ldots,(2r-1,2r)\) and \(N=(2,3),(4,5),\ldots,(2r,1)\). Their union is a single \(2r\)-cycle. The corresponding \(h\)-product colorings have \(|A_0(f)|=|A_1(g)|=3^r\), but their intersection consists of only the two alternating bit strings. For \(r\ge3\), both feasible sets are smaller than half the cube, yet the intersection remains nonempty through a structural, rather than cardinality, argument.

**Open sufficient strengthening of NORI1.** Ask whether arbitrary binary cube-edge colorings \(f,g\) satisfy \(A_0(f)\cap A_1(g)\ne\varnothing\). Choosing \(g=f\) would yield a paired root and hence NORI1 in one higher dimension. This proposed cross-favorability principle is stronger than NORI1 and may fail in general; Theorem 2 proves it only for independent Cartesian products of colored squares.


## Cross-orientation overlap for pseudoforest incidence graphs

The preceding crossed-perfect-matching theorem considers Cartesian products of colored squares. The correct ambient structure is the **factor-incidence multigraph** of any two Cartesian decompositions: vertices are factor blocks, one part for each coloring, and every cube direction is an edge joining the two factor blocks that contain it. A substantially wider all-dimensional overlap theorem holds whenever that multigraph is a pseudoforest.

Let \(B\) be a nonempty finite dimension set. Let \(g,h\) be arbitrary binary colorings of \(Q_B\) which each factor as Cartesian products of edge-colorings on disjoint nonempty direction blocks,
\[
g=\prod_{\alpha\in I}g_\alpha,\qquad h=\prod_{\beta\in J}h_\beta.
\]
Write \(\mathcal U=\{U_\alpha:\alpha\in I\}\) and \(\mathcal V=\{V_\beta:\beta\in J\}\) for their partitions of \(B\). Define the bipartite multigraph \(H(\mathcal U,\mathcal V)\) with one vertex for each \(U_\alpha,V_\beta\) and one edge labeled \(i\in B\) connecting its two containing blocks. Parallel edges are allowed. Assume each individual factor's oriented favorable-root set has density at least \(3/4\):
\[
|A_0(g_\alpha)|\ge 3\cdot 2^{|U_\alpha|-2},
\qquad
|A_1(h_\beta)|\ge 3\cdot 2^{|V_\beta|-2},
\tag{4}
\]
interpreted as an ordinary real inequality, so singleton factors (both roots favorable) qualify. The small-cube root-majority theorem supplies these bounds automatically for arbitrary factors of sizes one, two, or three.

**Lemma 4 (binary pseudoforest constraint extension).**
Let \(H\) be a finite multigraph, and give each vertex \(v\) a nonempty set \(L_v\subseteq\{0,1\}^{E(v)}\) of permitted assignments to its incident edges, with
\[
|L_v|\ge \tfrac34\,2^{\deg v}.
\]
If every connected component of \(H\) is a tree or contains precisely one cycle (counting a pair of parallel edges as a two-cycle), then the edge-variable constraint system has at least \(2^{c(H)}\) global satisfying assignments, where \(c(H)\) is the number of connected components.

*Proof.* Work componentwise. For any vertex \(v\) and prescribed bit on one incident edge, at least one choice for its other incident bits is permitted: the forbidden set has size at most \(2^{\deg v-2}\), smaller than the size \(2^{\deg v-1}\) of either one-bit slice. Thus, in a tree component, choose either value on any one edge, then extend its endpoint assignments and proceed away from that edge through the tree. Every prescribed entering-edge bit has a permitted continuation. Both initial values extend, so the component has at least two solutions.

For a unicyclic component, first consider the variables on the unique cycle. At any cycle vertex, fixing the two incident cycle-edge bits leaves \(2^{\deg v-2}\) choices of its other incident edges. Since the total forbidden set has at most this size, **at most one** of the four cycle-bit pairs can have no permitted continuation. Thus each cycle vertex forbids at most one of the four possible assignments to its two neighboring cycle edges. The binary cycle feasibility lemma from Theorem 2 proves that the resulting cycle constraints have at least two solutions, including for parallel-edge two-cycles. At each cycle vertex choose a permitted completion of its off-cycle edge bits; then extend outward along the attached trees, using the one-prescribed-bit extension property from the first paragraph. The choices of cycle solutions produce distinct complete assignments. Finally distinct components have disjoint edge-variable sets, so their solution counts multiply. \(\square\)

**Theorem 5 (cross-factorization intersection beyond matchings).**
Under (4), if the factor-incidence multigraph \(H(\mathcal U,\mathcal V)\) is a pseudoforest, then
\[
\boxed{|A_0(g)\cap A_1(h)|\ge 2^{c(H)}\ge2.}
\tag{5}
\]
In particular, this holds for any two Cartesian decompositions into arbitrarily colored \(Q_1,Q_2,Q_3\) factors whose incidence multigraph is a pseudoforest. The block pairings and block sizes may differ between the two colorings.

*Proof.* A Cartesian-product coloring has a favorable root precisely when each constituent factor has a favorable root for the same orientation: favorable factor paths concatenate in sorted order of their color blocks, and conversely deleting the other factor steps from a favorable full geodesic preserves monotonicity. Thus a common root is an assignment to the \(|B|\) direction bits satisfying, at every factor vertex of \(H\), the corresponding local allowable root pattern. Each vertex's allowed fraction is at least \(3/4\) by (4). The lemma supplies at least \(2^{c(H)}\) compatible assignments. \(\square\)

**Corollary 6 (pseudoforest terminal-fiber gluing).**
Split the directions of an arbitrary coloring \(F\) as \(A\sqcup B\), with all \(A\)-edge colors independent of the \(B\)-bits, inducing outer coloring \(f\). Suppose that for every outer vertex \(x\), the \(B\)-fiber coloring \(g_x\) factors into arbitrary colored blocks of sizes at most three, and for every pair \(x,y\) the incidence multigraph of their two factor partitions is a pseudoforest. Then
\[
\boxed{|P(F)|\ge2|P(f)|.}
\tag{6}
\]
More precisely, for each outer paired root \(z\), with two chosen favorable outer paths and respective switch-seam vertices \(v_z,w_z\),
\[
|P(F)|\ge\sum_{z\in P(f)}2^{c(H_{v_z,w_z})}.
\]
Here \(H_{v_z,w_z}\) is the incidence multigraph of the two fiber partitions. Every constructed witness remains a full dimension-simple geodesic.

*Proof.* By path reversal, \(A_1(g)=\overline{A_0(g)}\). Therefore Theorem 5 ensures at least \(2^{c(H)}\) fiber roots in \(A_0(g_{v_z})\cap\overline{A_0(g_{w_z})}\). Insert the two corresponding favorable fiber paths at the zero-to-one seams of the two outer paths starting at antipodal roots \(z,\bar z\), respectively. Each insertion preserves the monotone word and uses each \(B\)-direction once; the outer paths use each \(A\)-direction once. Distinct fiber roots yield distinct paired roots, giving the bounds. \(\square\)

**Closure perspective.** The earlier two-matching theorem corresponds to factor-incidence graphs of maximum degree two, hence disjoint paths and cycles. Theorem 5 permits arbitrary factor-vertex branching and all three-dimensional factors, as long as the incidence graph has at most one independent cycle per component. Thus the real obstruction to this local intersection *method* is a factor-incidence component of cyclomatic number at least two. That is not asserted to be an obstruction to the paired-root conjecture itself; additional coloring-specific structure may still force intersections in multicyclic components.


## Multicyclic cross-factor intersections: theta and cactus

Assume every factor vertex permits at least three quarters of the assignments to its incident binary edge variables. A vertex of degree one permits both bits, a vertex of degree two forbids at most one of four pairs, and a vertex of degree three forbids at most two of eight triples.

**Lemma (path reduction).** A chain of degree-two vertices, each forbidding at most one pair, induces a terminal two-bit relation forbidding at most one pair. This follows inductively: composing two binary relations that each omit at most one of four pairs still omits at most one, since blocking both possible values of the intermediate bit consumes the unique forbidden pair in each relation. A direct edge identifies its endpoint bit copies.

**Theorem (theta intersection).** Two trivalent vertices joined by three internally disjoint paths, with any number of degree-two internal vertices, have a compatible global assignment under the stated local constraint bound, including when some paths are direct parallel edges.

*Proof.* Contract the paths to their endpoint relations. Each indirect relation contains at least three pairs, so it has nonempty rows and columns and at most one row of size one. The allowed incident-bit triple sets U,V at the two trivalent vertices each have size at least six.

For zero direct paths, at least four start triples have at least four compatible end triples. U contains one such start, while V excludes at most two endings. For one direct path, write a_t,b_t for the forbidden counts in the two four-pattern slices of the junction sets having shared bit t. Some t has a_t+b_t at most two. If either slice is full, compatibility follows from nonempty rows and columns; otherwise both slices contain at least three patterns, and some permitted start has at least two permitted end options, meeting the other size-three slice. For two direct paths, each of the four shared two-bit values t induces sets X_t,Y_t of possible last bits. If no value t were compatible with the remaining indirect relation, then at each t either X_t or Y_t would be empty, or both would be singletons. This requires at least two excluded junction patterns per t, totaling eight, while only four exclusions are allowed. For three direct paths, U and V intersect in at least four triples. QED.

**Lemma (pendant-cycle extension).** For a cycle with one extra bridge bit at one trivalent attachment vertex, fixing that bridge bit leaves at least two admissible patterns for the two cycle edges at the attachment. The complementary degree-two path admits at least three endpoint pairs by path reduction. Their intersection is nonempty, so the cycle can be solved for either bridge-bit choice.

**Theorem (subcubic cactus intersection).** Every cactus multigraph of maximum degree three has a global solution to three-quarter-dense local binary edge constraints.

*Proof.* Root its bridge/cycle block tree. Terminal branches composed of trees extend from either choice of their entering edge bit because each local constraint admits a continuation after fixing one incoming bit. Terminal cycle blocks extend from either choice of their attachment bit by the pendant-cycle lemma, after treating attached tree branches. Remove terminal blocks inductively, retaining their ability to extend any parent-bridge bit. The remaining root vertex or cycle is solvable by direct local feasibility or the binary-cycle lemma. Restore removed blocks in reverse order. QED.

**Corollary (dimension-simple seam gluing).** If two conditional fiber colorings factor into blocks each with at least three quarters of roots favorable in the required orientation, their favorable-root sets intersect whenever every connected block-incidence component is a pseudoforest, a theta, or a subcubic cactus. Arbitrary colored factors of dimension one, two, or three satisfy the density requirement. Inserting two compatible fiber paths at the opposite outer switch seams preserves full dimension-simplicity and gives a paired root.

Cycles linked through bridge trees and the basic three-path multicyclic core therefore cannot obstruct this cross-factor intersection method. The remaining unresolved structure involves more highly connected multicyclic factor-incidence blocks, or individual factors with smaller favorable-root density.


## Unrestricted crossing of all one-, two-, and three-dimensional Cartesian factors

The preceding pseudoforest, theta, and cactus theorems controlled the topology of the block-incidence graph. A stronger *linear matroid selection* argument removes **every incidence restriction** for arbitrary factors of sizes one, two, and three. It also identifies a sufficient local condition for larger factors.

Let \(B\) be a finite dimension set, \(m=|B|\), and let \(g,h\) be arbitrary binary cube-edge colorings each expressible as a Cartesian product of factor colorings across a partition of \(B\). The two partitions may overlap in any fashion. For an orientation \(\sigma=0,1\), denote by \(A_\sigma(g)\) the roots of a full dimension-simple geodesic whose color word has form \(0^*1^*\) when \(\sigma=0\), or \(1^*0^*\) when \(\sigma=1\). Empty color blocks are permitted.

A factor with variable set \(U\) and allowed root set \(A\subseteq\mathbb F_2^U\) has the **two-dimensional safe-check property** if it admits a two-dimensional binary linear subspace \(L\subseteq\mathbb F_2^U\) such that for every nonzero \(v\in L\), some affine parity equation
\[
\boxed{v\cdot x=b_v}
\tag{10}
\]
has its full solution hyperplane inside \(A\). The value \(b_v\) may depend on \(v\).

**Lemma 16 (affine-span criterion for safe checks).** Let \(F=\mathbb F_2^U\setminus A\) be the unfavorable root set, with \(s=|U|\ge2\). If the affine span of \(F\) has dimension at most \(s-2\), then \(A\) has the two-dimensional safe-check property. In particular, every subset of \(\mathbb F_2^2\) omitting at most one point and every subset of \(\mathbb F_2^3\) omitting at most two points has this property.

*Proof.* If \(F\) is nonempty, fix \(p\in F\) and let \(D=\operatorname{span}\{x+p:x\in F\}\). Its dimension is the affine dimension of \(F\), at most \(s-2\). Choose a two-dimensional subspace \(L\subseteq D^\perp\). For any nonzero \(v\in L\), the scalar \(v\cdot x\) equals \(v\cdot p\) on every forbidden root. The opposite parity equation \(v\cdot x=1+v\cdot p\) therefore excludes all of \(F\). If \(F\) is empty, choose any two-dimensional \(L\); both right-hand sides yield allowed hyperplanes. The final assertions use the respective bounds on the cardinality of \(F\). \(\square\)

**Lemma 17 (two-fold support and independent parity selectors).** Let \(U_1,\ldots,U_k\) be two-dimensional linear subspaces of \(\mathbb F_2^m\), each supported on a subset \(B_i\subseteq[m]\), such that each ground-set position occurs in at most two of the subsets \(B_i\). Then there exist linearly independent nonzero representatives \(u_i\in U_i\) for all \(i=1,\ldots,k\).

*Proof.* Use Rado's independent-transversal theorem for a family of subsets of a representable matroid: it suffices to prove
\[
\dim\left(\sum_{i\in S}U_i\right)\ge|S|
\quad\text{for every }S\subseteq[k].
\tag{11}
\]
Fix \(S\), put \(W=\sum_{i\in S}U_i\), and write \(r=\dim W\). Choose an information set \(J\subseteq[m]\) of size \(r\) on which the projection \(W\to\mathbb F_2^J\) is injective; such a set exists by selecting pivot columns in a basis matrix of \(W\). Its restriction to each \(U_i\subseteq W\) is also injective. Since \(\dim U_i=2\), at least two positions of \(J\) must belong to \(B_i\). Each position of \(J\) belongs to at most two \(B_i\), so double counting gives
\[
2|S|\le\sum_{i\in S}|J\cap B_i|\le2|J|=2r.
\]
This proves (11) and hence the independent-representative assertion. \(\square\)

**Theorem 18 (universal cross-factor favorable-root intersection).** Suppose each non-singleton factor of \(g\) or \(h\), in its respective required orientation, has the two-dimensional safe-check property, while singleton factors permit both possible roots. Let \(k\) be the total number of non-singleton factors across the two decompositions. Then
\[
\boxed{|A_0(g)\cap A_1(h)|\ge 2^{m-k}\ge1.}
\tag{12}
\]
In particular, this conclusion holds for **every pair of Cartesian products of arbitrary colored \(Q_1,Q_2,Q_3\) factors**, with absolutely no restriction on their two partitions or their factor-incidence multigraph.

*Proof.* For each non-singleton factor choose a two-dimensional safe-check subspace as above, embedded by zeros in the \(m\)-bit ground space. Each ground dimension belongs to precisely one factor of \(g\) and one factor of \(h\), so it belongs to at most two such subspace supports. Apply Lemma 17 to choose a linearly independent safe-check vector \(u_v\) for every non-singleton factor \(v\). Choose the corresponding right-hand side \(b_v\) from its safe-check property. The affine linear system
\[
u_v\cdot x=b_v\qquad\text{for all chosen factors }v
\tag{13}
\]
has \(k\) independent equations in \(m\) binary variables, and therefore admits \(2^{m-k}\) solutions. Each solution satisfies every factor's safe equation and hence every local favorable-root requirement. For singleton factors both bits are always favorable. Finally favorable-root sets of Cartesian-product colorings are Cartesian products of the local favorable-root sets: necessity follows by deleting steps in other blocks from a monotone full path, and sufficiency by taking full monotone factor paths and interleaving all their zero prefixes before all their one suffixes. Thus all solutions of (13) belong to \(A_0(g)\cap A_1(h)\). The small-cube majority results give at most one unfavorable root in \(Q_2\) and at most two in \(Q_3\), so Lemma 16 applies to every possible factor of those sizes. \(\square\)

**Corollary 19 (unrestricted terminal-fiber gluing for variable small-block partitions).** Let the dimensions of an arbitrary coloring \(F\) split into outer directions \(A\) and fiber directions \(B\), with all outer-edge colors independent of fiber bits, inducing coloring \(f\). Suppose that for every outer vertex \(x\), its fiber coloring \(g_x\) is an arbitrary Cartesian product of colored factors of sizes at most three. The factorization and block partition may vary freely with \(x\). For any \(z\in P(f)\), choose full favorable outer paths from \(z\) and \(\bar z\) and let \(k_z\) be the total number of nonsingleton factors across the two fiber colorings encountered at their respective seam vertices. Then
\[
\boxed{
|P(F)|\ge\sum_{z\in P(f)}2^{|B|-k_z}\ge|P(f)|.
}
\tag{14}
\]
Thus no least-dimensional paired-root counterexample can have a terminal fiber block whose conditional colorings all factor into blocks of size at most three, **even when their block decompositions overlap arbitrarily**. The full paths produced by insertion are dimension-simple.

*Proof.* By full-path reversal, \(A_1(g_{w_z})=\overline{A_0(g_{w_z})}\). Apply Theorem 18 to \(g_{v_z},g_{w_z}\) to obtain at least \(2^{|B|-k_z}\) fiber roots in the required opposite-orientation intersection. At the two switch seams insert full favorable fiber geodesics starting respectively from such a root and from its antipode. The resulting full paths have both monotone color orientations and traverse every dimension once. Summing distinct paired starting roots gives (14). \(\square\)

**Path to closure.** The obstruction has moved away from the *geometry of overlapping small factors* altogether. Linear-matroid selection solves all such overlaps, even where their factor-incidence graph has arbitrarily high cycle rank. What remains are conditional fiber colorings with **indecomposable blocks of dimension at least four**, or larger blocks whose unfavorable-root affine span has codimension below two. The natural next task is to seek a safe-check substitute with higher-dimensional coefficient modules or supported path chains on those irreducible blocks, preserving the two-fold overlap rank argument where possible.


## General rank-overlap principle and failure of safe hyperplanes in higher ranks

**Theorem (linear safe-check selection at matching overlap multiplicity).** Let local permitted-pattern sets A_v depend on bit sets B_v among m global binary variables. Suppose each bit occurs in at most t of the sets B_v. Suppose for every factor v there is a binary linear space L_v of dimension at least t, supported on B_v, whose every nonzero vector u admits a right-hand side b_u such that the full affine solution hyperplane u·x=b_u lies in A_v. Then all local constraints have a common solution; indeed they contain an affine solution space of at least 2^(m-k) points, where k is the number of factors.

*Proof.* For any subset S of factors let W be the sum of their L_v, with rank r. Choose r pivot positions on which projection of W is injective. For every v in S the projection of L_v is injective, so those pivot positions contain at least t elements of B_v. Every pivot position belongs to at most t factor supports. Double counting gives t|S|<=tr, hence rank(W)>=|S|. Rado's linear independent-transversal theorem selects one independent vector u_v from each L_v. Give every selected vector its safe right-hand side; all k affine equations are independent, and their 2^(m-k) common solutions satisfy every factor. QED.

**Corollary (unfavorable affine-span criterion).** The theorem applies whenever each nonempty forbidden pattern set F_v has affine span dimension at most |B_v|-t. Pick one excluded pattern p. The subspace orthogonal to all differences q-p with q in F_v then has dimension at least t; for every nonzero vector in it, the affine equation whose bit value is opposite to its value at p avoids every excluded pattern. Empty forbidden sets impose no restriction.

**Proposition (an all-dimensional barrier to linear safe checks).** For every even d=2r>=4, set the color on an edge in direction i to the parity of all vertex bits other than bit i. The set of roots supporting full 0*1* paths has Hamming weights r or r+(-1)^r, as proved by the rooted parity-reader count in Article XIV. Thus all middle-layer roots of weight r are paired with their antipodes. Yet the favorable-root set contains no affine hyperplane. Its complement contains the zero vector and all d unit vectors because weights zero and one are excluded when r>=2. Those d+1 excluded patterns affinely span the full d-dimensional binary cube; they cannot all lie on one affine hyperplane. Hence no affine hyperplane can avoid them.

**Closure target.** Two-fold factor overlap is solved when every block possesses two independent safe-check directions; arbitrary colored Q2 and Q3 factors satisfy this. For larger indecomposable blocks, favorable paths may exist abundantly despite there being no safe affine parity equation. A full proof of NORI1 therefore needs a richer supported intersection object, or a higher-codimension substitute for safe parity hyperplanes.

## Three-family overlap obstruction on four bits

**Proposition.** Let g1,g2,g3 be Cartesian products of colored Q2 factors on four dimensions, using the three matchings M1={(0,1),(2,3)}, M2={(0,2),(1,3)}, M3={(0,3),(1,2)}. Choose the colored-square favorable-root exclusions on these six pairs as (0,1):00, (0,2):00, (0,3):10, (1,2):11, (1,3):01, (2,3):01. Every prescribed excluded pattern is realizable by a colored Q2 factor through translation of the sharp three-favorable-root example.

Then A0(g1) intersect A0(g2) intersect A0(g3) is empty, although the intersection of any two of these favorable-root sets is nonempty by the crossed-square matching theorem.

*Proof.* Avoiding patterns 00 on pairs (0,1) and (0,2) says x0 OR x1 and x0 OR x2. Avoiding pattern 11 on pair (1,2) says NOT x1 OR NOT x2. These three constraints imply x0=1, since x0=0 forces x1=x2=1. Avoiding pattern 10 on (0,3) then forces x3=1. Avoiding patterns 01 on (1,3) and (2,3) forces x1=x2=1, contradicting the forbidden 11 pattern. No common root exists. All two-family intersections exist by the preceding general matroid theorem. QED.

The result shows the two-fold-support parameter in the safe-check matroid theorem cannot be replaced by three-family Helly without stronger local safety rank. It does not produce a counterexample to the paired-root theorem, which involves two orientations of one coloring.


## Sharp three-quarter threshold for local cubic root constraints

**Theorem (density threshold for bipartite cubic factor incidence).** In any bipartite multigraph with binary variables on edges and permitted local patterns on each vertex star, if all degree-three vertices permit at least six of eight bit triples, all degree-two vertices at least three of four pairs, and all degree-one vertices both bits, then there is a satisfying global assignment. However, replacing six of eight by five of eight at degree-three vertices is not sufficient, even for the simple bipartite graph \(K_{3,3}\).

*Sufficiency.* At each degree-two or degree-three vertex the forbidden patterns have affine dimension at most the star degree minus two, yielding a two-dimensional subspace of safe parity-check vectors. Every original edge variable lies in at most two vertex stars. The independent-transversal theorem established earlier therefore chooses one linearly independent safe parity-check equation per nonsingleton vertex. Their full-rank affine system has a solution, which meets all the local restrictions.

*Sharpness.* Put nine binary variables \(x_{ij}\) on \(K_{3,3}\), for \(i,j\in\{0,1,2\}\). At its row vertices prescribe
\[
\begin{array}{ll}
R_0:&\neg x_{01}\ \lor\ (\neg x_{00}\land x_{02}),\\
R_1:&\neg x_{12}\ \lor\ (x_{10}\land\neg x_{11}),\\
R_2:&x_{22}\ \lor\ (x_{20}\land x_{21}),
\end{array}
\]
and at the three column vertices prescribe
\[
\begin{array}{ll}
C_0:&x_{00}\ \lor\ (\neg x_{10}\land x_{20}),\\
C_1:&x_{01}\ \lor\ (x_{11}\land\neg x_{21}),\\
C_2:&x_{12}\ \lor\ (\neg x_{02}\land\neg x_{22}).
\end{array}
\]
Every rule accepts five of the eight assignments to its own three variables: it is one Boolean input condition OR a conjunction of two independently varying input conditions.

Suppose a global assignment satisfied the rules. If \(x_{12}=0\), then \(C_2\) gives \(x_{02}=x_{22}=0\); \(R_2\) gives \(x_{20}=x_{21}=1\); \(C_1\) gives \(x_{01}=1\); and \(R_0\) requires \(x_{02}=1\), contradiction. If \(x_{12}=1\), then \(R_1\) gives \(x_{10}=1,x_{11}=0\); \(C_0\) gives \(x_{00}=1\); \(R_0\) gives \(x_{01}=0\); and \(C_1\) requires \(x_{11}=1\), contradiction. Hence the six five-eighths-dense constraints have no joint solution. \(\square\)

**Research consequence.** Merely knowing that local favorable-root sets have strict majority is not enough to glue two arbitrarily crossing factor partitions. The three-quarter lower bound guaranteed for every colored \(Q_3\) factor is sharp as a general cardinality hypothesis on cubic vertex constraints. These abstract five-eighths permitted sets need not be realizable as favorable-root sets of cube-edge colorings, so this does not challenge NORI1 or the preceding small-factor gluing theorem. It rules out the proposed density-only extension and directs attention to stronger algebraic invariants of large root sets.



## One exceptional safe-parity factor: an integral-rank strengthening

The two-fold-support matroid argument tolerates one factor whose family of safe parity-check vectors has rank **one** instead of two. No increase in the rank of the remaining factors is required. The reason is the integral rounding in the information-set double count.

**Lemma 25 (nonuniform rank-overlap bound).** Let \(L_1,\ldots,L_k\subseteq\mathbb F_2^m\) be linear spaces supported respectively on \(B_1,\ldots,B_k\subseteq[m]\). Suppose each bit position occurs in at most \(t\) of the supports \(B_i\). Then for every \(S\subseteq[k]\),
\[
\boxed{
\dim\left(\sum_{i\in S}L_i\right)
\ge \left\lceil\frac{\sum_{i\in S}\dim L_i}{t}\right\rceil.
}
\tag{21}
\]

*Proof.* Put \(W=\sum_{i\in S}L_i\), \(r=\dim W\), and select \(r\) pivot positions \(J\subseteq[m]\) such that projection onto \(J\) is injective on \(W\). Its restriction to each \(L_i\) is injective, so \(|J\cap B_i|\ge\dim L_i\). Counting incidences and using the support multiplicity bound gives
\[
\sum_{i\in S}\dim L_i
\le\sum_{i\in S}|J\cap B_i|
\le t|J|=tr.
\]
Take ceilings. \(\square\)

**Theorem 26 (one rank-one exception in two-fold fiber gluing).** Consider two arbitrary Cartesian decompositions of the same binary root variables, with a local allowed set at each factor. At every factor except possibly one, assume the two-dimensional safe-check property of Theorem 18; at the exceptional factor assume only that its permitted set contains some full affine parity hyperplane. Singleton factors permit both roots. Then the two products of allowed local sets have a common root.

More precisely, if \(m\) is the number of shared bit variables and \(k\) is the number of factors imposing a nontrivial permitted-root restriction, there are at least
\[
\boxed{2^{m-k}}
\tag{22}
\]
common roots.

*Proof.* Represent each local safe-check family by a linear subspace \(L_v\) of coefficient vectors, supported on its factor directions. All but one have dimension at least two. The exceptional factor has a nonzero safe coefficient vector, spanning a one-dimensional space. Since each dimension belongs to one factor from each Cartesian decomposition, every bit lies in at most two supports.

Fix any nonempty subfamily \(S\) of size \(s\). If it omits the exceptional factor, the sum of the safe-check ranks is at least \(2s\); if it includes the exception, the sum is at least \(2s-1\). Lemma 25 with \(t=2\) gives
\[
\dim\left(\sum_{v\in S}L_v\right)
\ge\left\lceil\frac{2s-1}{2}\right\rceil=s
\]
in either case. This is the Hall--Rado rank condition. Select linearly independent nonzero safe-check vectors, one per nontrivial factor, and give each its favorable parity right-hand side. The resulting \(k\) affine equations are consistent and admit \(2^{m-k}\) solutions. Every solution belongs to every local permitted-root set by the definition of a safe check. \(\square\)

**Corollary 27 (an exceptional conditional fiber block).** The paired-root seam-lifting theorem remains valid when, at its two conditional fiber states, every local Cartesian factor has a two-dimensional safe-check coefficient space except for one factor across the two decompositions, which may have only a single safe parity hyperplane. In particular, one exceptional factor of any dimension is allowed, provided its feasible-root set contains an affine hyperplane and all other factors meet the two-dimensional condition. The two fiber decompositions may overlap arbitrarily; all constructed full paths remain dimension-simple.

This is a strict enlargement of the previous equal-rank assumption. It does **not** handle a parity-reader factor having no favorable affine hyperplane, nor two unrelated rank-one factors. Those remain potential requirements for a nonlinear or higher-chain proof.



## Absorbing arbitrary irreducible factors by safe-rank surplus

The independent-transversal method can also accommodate local factors with **no safe affine hyperplane whatsoever**, provided other factors have enough rank surplus to absorb their shared variables. This is relevant to parity-reader-type favorable-root sets and is not a statement about local density alone.

Let the ground binary variable set \(B\) be partitioned in two ways, \(\mathcal U\) and \(\mathcal V\), and impose one permitted-pattern set \(A_D\subseteq\mathbb F_2^D\) for each block \(D\) of either partition. Call a coefficient vector \(u\in\mathbb F_2^D\) *safe* if one of the two affine equations \(u\cdot x=b\) has its entire solution hyperplane inside \(A_D\); a *safe-check space* is a linear subspace all of whose nonzero vectors are safe.

Select any collection \(\mathcal E\subseteq\mathcal U\) of **exceptional blocks on one side**, and put \(W=\bigcup_{D\in\mathcal E}D\). The sets in \(\mathcal E\) are disjoint. Assume their allowed sets are nonempty but make **no** affine-safe-check assumption about them.

**Theorem 28 (arbitrary-factor absorption from neighboring rank surplus).** Suppose every other nontrivial factor block \(D\notin\mathcal E\) admits a safe-check space \(L_D\) satisfying
\[
\boxed{\dim L_D\ge2+|D\cap W|.}
\tag{23}
\]
Singleton factors may instead be completely unrestricted, permitting both root bits. Let \(k\) be the number of nonexceptional factors to which a safe-check equation is applied. Then all local constraints have at least
\[
\boxed{
\left(\prod_{D\in\mathcal E}|A_D|\right)\,
2^{\,|B\setminus W|-k}
}
\tag{24}
\]
joint solutions. In particular, any finite family of large irreducible factors can be absorbed without any safe affine hyperplane of their own, if they lie in one partition and their neighbors carry the stated rank surplus.

*Proof.* Choose permitted assignments independently on every exceptional block \(D\in\mathcal E\). Together they fix the bits in \(W\), and there are \(\prod_{D\in\mathcal E}|A_D|\) choices.

For each remaining factor \(D\), restrict its coefficient space to vectors with zero entries on \(D\cap W\):
\[
L_D'=\{u\in L_D:u|_{D\cap W}=0\}.
\]
Restriction to \(D\cap W\) has rank at most \(|D\cap W|\), so
\[
\dim L_D'\ge\dim L_D-|D\cap W|\ge2.
\]
Every vector in \(L_D'\) involves only unfixed variables and retains its original safe right-hand side, which still guarantees the full local permitted-pattern condition regardless of the fixed bits. Each unfixed bit belongs to at most two remaining factor blocks, one from each partition. Apply the two-fold-support linear independent-transversal theorem to the spaces \(L_D'\) on \(B\setminus W\). Select \(k\) independent safe parity equations; their solution set has \(2^{|B\setminus W|-k}\) points. Each such assignment, combined with the arbitrarily selected permitted exceptional roots, satisfies all local restrictions. The solution sets for distinct exceptional choices are disjoint, establishing (24). \(\square\)

**Corollary 29 (one parity-reader-type conditional factor can be glued).** Suppose two conditional terminal-fiber colorings factor across possibly unrelated direction partitions. One of them may include an arbitrary indecomposable factor \(D_*\), whose favorable-root set is merely assumed nonempty, even if it has no safe affine hyperplane. Assume every other nonsingleton factor \(D\) has a safe-check space of dimension at least \(2+|D\cap D_*|\). Then the two required favorable-root sets intersect, and a paired outer root lifts through the fiber by the usual dimension-simple seam insertion.

For example, if each factor in the opposite partition shares **at most one bit** with \(D_*\) and has at most one forbidden root among its patterns, a factor of size four offers safe-check rank three and can absorb the shared bit. All other colored \(Q_2\) or \(Q_3\) factors offer rank two. This gives a family of intersections in which the exceptional factor may have any dimension and arbitrary nonlinear internal dependencies.

**Scope.** The theorem is conditional on a permitted root in each exceptional factor; it does not establish nonemptiness for an arbitrary cube coloring. It gives an all-dimensional gluing mechanism for locally irreducible factors supported by sufficiently flexible neighbors. When exceptional factors occur on both sides, or neighboring safe-check ranks have insufficient surplus, the method does not guarantee consistency. These cases remain candidates for supported-path or equivariant-index arguments.



## Hall-deficiency localization of failed root intersections

The rank-overlap inequality also gives an obstruction certificate for any two factorized permitted-root families that do **not** intersect. This is a necessary condition for failure, not a sufficient condition for failure.

**Theorem 30 (a two-unit local deficit is necessary for incompatibility).** Let \(\mathcal U,\mathcal V\) be any two partitions of the same binary dimension set \(B\), and let \(A_D\) be a permitted-root subset on each factor \(D\). For every factor choose any safe-check linear space \(L_D\) (possibly zero-dimensional), embedded in \(\mathbb F_2^B\). If
\[
\boxed{\bigcap_{D\in\mathcal U\cup\mathcal V}\{x:x|_D\in A_D\}
=\varnothing,}
\]
then there exists a nonempty factor subfamily \(S\) for which
\[
\boxed{
\dim\left(\sum_{D\in S}L_D\right)<|S|,
\qquad
\sum_{D\in S}(2-\dim L_D)\ge2.
}
\tag{25}
\]
Equivalently, if every nonempty subfamily has total safe-check rank at least \(2|S|-1\), then all local root constraints have a common assignment.

*Proof.* Suppose all subfamilies met the Hall--Rado rank condition \(\dim\sum_{D\in S}L_D\ge|S|\). Rado's independent-transversal theorem would select one nonzero safe-check vector per factor, the chosen vectors being linearly independent. Giving each vector its permitted parity right-hand side would yield a consistent affine system all of whose solutions lie in the local permitted sets. This contradicts the assumed empty intersection. Thus some subfamily \(S\) has sum rank at most \(|S|-1\).

Every ground-set bit belongs to at most two factor supports, one in each partition. The nonuniform information-set inequality from Lemma 25 gives
\[
\frac12\sum_{D\in S}\dim L_D
\le\dim\left(\sum_{D\in S}L_D\right)
\le |S|-1.
\]
Rearranging proves (25). The contrapositive gives the equivalent compatibility assertion. \(\square\)

**Corollary 31 (where a paired-root gluing obstruction must concentrate).** If a pair of conditional terminal-fiber colorings has disjoint required monotone-root sets, then *any chosen family* of local safe-check spaces must have a subfamily with at least two units of deficiency relative to rank two per factor. Thus a single rank-one factor among rank-two factors cannot prevent root overlap, agreeing with Theorem 26. A no-safe-hyperplane factor can supply two deficiency units by itself; Theorem 28 explains a separate mechanism by which sufficient neighboring rank surplus can nevertheless absorb such a factor.

**Closure use.** This converts failure of affine-safe-check gluing into a rank-deficient *subcollection* of interacting factors. A future supported-chain or Smith-index proof need not repair all factor overlaps uniformly: it may instead localize its obstruction to one Hall-deficient cluster, where two or more effective safe-check degrees are missing. However, the existence of such a cluster does not imply a counterexample to the underlying paired-root conjecture; larger-root-set compatibility may survive despite the failure of all selected parity checks.


## One-forbidden-root gluing on unrestricted factor-incidence graphs

Let H be a finite loopless multigraph without isolated vertices, with one binary variable x_e on each edge. At each vertex v impose a constraint L_v on its incident variables that forbids at most one binary assignment. Assume every degree-one vertex is unconstrained.

**Theorem (two assignments per connected component).** There exist at least 2^{c(H)} simultaneous satisfying edge assignments, where c(H) is the number of connected components. The lower bound is attained for suitable forbidden patterns on cycles.

*Proof.* It suffices to treat connected H. Orient its edges so every constrained vertex has an incoming edge. When H has a cycle, orient a cycle cyclically, orient spanning trees away from that cycle, and orient the remaining edges arbitrarily. When H is a tree, orient away from a leaf, which is unconstrained. For each directed edge u->v, choose its variable to disagree with the forbidden pattern at v on that edge, if one is present. Thus all constrained vertices are satisfied.

Suppose the satisfying assignment x is unique. Flipping any one edge e must violate a constraint at an endpoint of e. A constrained vertex can witness such a violation for at most one incident edge: its forbidden assignment differs from x on at least one bit, and if changing one bit makes it forbidden, that bit is uniquely determined. Thus |E(H)| is at most the number k of constrained vertices. In a tree, k<=|V(H)|-2<|E(H)|. Otherwise, |E(H)|>=|V(H)|>=k. Equality throughout forces a connected unicyclic graph, every vertex constrained and therefore of degree at least two. Hence H is a cycle (including a two-cycle with parallel edges). At every vertex the forbidden word differs from x in one of its two incident bits. The bitwise complement of x differs from that forbidden word in the other bit and hence also satisfies every constraint, contradicting uniqueness. There are at least two solutions for connected H, and components multiply. QED.

**Corollary (cross-factor root gluing without restrictions on overlap cycles).** Let f,g be arbitrary binary edge colorings of Q_B, each with an independent Cartesian factorization into nonempty dimension blocks, with possibly different partitions U,V. Suppose each f-factor excludes at most one root from A_0 and each g-factor excludes at most one root from A_1, where A_0 consists of roots of nondecreasing full color words and A_1 of roots of nonincreasing full color words. Let H be the bipartite multigraph whose vertices are the factors and whose dimension-labeled edges indicate membership in one factor of each partition. Then
\[
|A_0(f)\cap A_1(g)|\ge 2^{c(H)}.
\]

*Proof.* The favorable-root set of a Cartesian product is the Cartesian product of the factor favorable-root sets: concatenate the zero-colored and one-colored portions of factor paths in the required order; deleting other factors' steps gives necessity. A common root is consequently a binary labeling of H's edges satisfying the factor constraints. A one-dimensional factor admits both roots under either orientation, so leaves are unconstrained. Apply the theorem. QED.

This removes the pseudoforest assumption from the earlier factor-overlap theorem when each factor has at most one forbidden root. It is consistent with the higher-rank safe-check theorems below, and is a conditional cross-root theorem rather than unrestricted NORI1.
