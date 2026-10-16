# Folded-cube orientation and paired-square reductions

- Stable ID: note_nori_folded_cube_semieulerian_alternating_girth_equivalence_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: balanced, folded-cube, orientation, odd-girth, closure-equivalence, hall-obstruction, paired-square
- Lifecycle: active
- Epistemic status: proved
- Current version: 8
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_4
- Updated session: session_nori_r9962_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For odd d=2m+1>=3 let G_d=Q_d/<tau> be the folded cube (antipodal quotient). Its vertex set consists of antipodal vertex pairs, and its edges are antipodal pairs of cube edges. Since d is odd, each vertex orbit has one even-parity representative. Each edge orbit has two representatives: one incident to the even representative of its first endpoint orbit, and the other incident to the even representative of its second endpoint orbit. Thus an orientation of G_d is equivalent to an antipodally odd coloring c of Q_d: direct the quotient edge away from the orbit whose even representative is incident to its color-zero edge.

**Theorem 1 (geodesics as almost-alternating odd-girth cycles).** The folded cube G_d has odd girth d. A color-zero full antipodal geodesic of c projects to a d-cycle C in G_d in which one vertex is a transit (one entering and one leaving cycle edge) and the other d-1 vertices alternate between cycle sources (two leaving) and cycle sinks (two entering). Conversely, every such oriented d-cycle lifts to a color-zero full antipodal geodesic. Hence c has a monochromatic full antipodal geodesic if and only if its associated orientation of G_d contains an almost-alternating shortest odd cycle.

*Proof.* An odd closed walk in the quotient lifts to a cube walk that starts at x and ends at bar x: its endpoints must lie in the same orbit, and odd parity precludes returning to x since d is odd. It therefore has length at least d. Projected full geodesics have length d and are simple quotient cycles, because a repeated orbit along a proper subpath would imply two cube vertices at distance 0 or d with fewer than d traversed edges. Thus the odd girth is d.

Choose a color-zero full geodesic starting at an even vertex. Along its projected cycle, the first edge is traversed with its quotient orientation, the second against it, the third with it, etc., and the last (dth) with it. Therefore the first and last edges form a transit at the starting quotient vertex; every other vertex is alternately a sink and a source. Starting from an odd cube vertex reverses all these traversal signs. Conversely, if an oriented d-cycle has this pattern, choose the even or odd cube lift of its transit vertex so that the first traversed edge is color zero. The prescribed alternating orientation signs imply every successive lifted edge is color zero, and the lifted d-cycle joins antipodes. Its directions occur once because its length equals the cube distance d. QED.

**Theorem 2 (counterexample-preserving nearly regular odd lift).** Suppose c is a vertex-balanced antipodally odd coloring of Q_(2m), with zero degree m everywhere. Adjoin a new direction b and take any antipodally odd binary function h on the original vertices (for instance h(x)=x_1), setting
\[
c'_i(x,t)=c_i(x)\ (i\le2m),\qquad c'_b(x,t)=h(x).
\tag{1}
\]
Then c' is antipodally odd on Q_(2m+1), its zero-degree at every vertex lies in {m,m+1}, and it contains a monochromatic full antipodal geodesic if and only if c does.

*Proof.* Antipodal oddness follows from c_i(bar x)=1-c_i(x) and h(bar x)=1-h(x), with h independent of the added bit. Each vertex has m old zero edges and another zero edge precisely when h(x)=0. A monochromatic full geodesic in c' projects, after deleting its unique b-edge, to a monochromatic full antipodal geodesic in c. Conversely, let a monochromatic full geodesic of c go from x to bar x with color t. If h(x)=t, place the new direction before the original geodesic; otherwise h(bar x)=t, so place it after. Either choice is a monochromatic full geodesic of c'. QED.

**Theorem 3 (unrestricted closure equivalence).** Unrestricted NORI1 is equivalent to the following oriented-graph conjecture:

For every odd d=2m+1>=3, every orientation of G_d with each vertex having outdegree m or m+1 contains an almost-alternating d-cycle (one transit vertex and alternating cycle sources/sinks at its other d-1 vertices).

*Proof.* For an odd coloring, its color-zero degree at the even representative of a quotient vertex equals the outdegree there, and the antipodal oddness makes the opposite degree d minus that count. Thus near-regular odd colorings correspond precisely to orientations with outdegrees m or m+1. Theorem 1 identifies the geodesic with the required cycle. If unrestricted NORI1 holds, the orientation statement follows. Conversely, if a counterexample exists, the established reduction produces a balanced counterexample of even dimension. Apply Theorem 2 to obtain a nearly regular odd counterexample; its quotient orientation violates the cycle statement by Theorem 1. QED.

**Explicit binary-circuit Cayley form.** On the even representatives, G_d is the Cayley graph of the even-parity vector space F2^(d-1), with d generators s_i=one+e_i (viewed in the even-parity subspace of F2^d). Their sum is zero, and every proper nonempty subset is linearly independent. Choosing any d-1 of them as a basis identifies G_d with Q_(d-1) plus the diagonal matching for the remaining generator. Every shortest odd cycle consists of the d generators in some order. The oriented-cycle statement can therefore be read as a balanced orientation of a binary circuit Cayley graph that admits an alternating generator-order cycle.

**Boundary of generalization.** Degree balance and equality of the odd girth with d do not suffice for arbitrary d-regular graphs. The triangular prism is 3-regular with odd girth 3. Orient each of its two triangle faces cyclically and orient each of the three matching edges arbitrarily. Every vertex then has indegree and outdegree 1 and 2, yet the only triangles are the two cyclically oriented faces, and neither has a source/sink/transit pattern. Thus a proof of Theorem 3 must use the folded-cube circuit incidence, not merely near-Eulerian vertex degrees and odd girth.

**Theorem 4 (nonnegative semidefinite trace and common-out-neighbor criterion).** Let D be the oriented adjacency matrix of G_d (D_(u,v)=1 when the quotient edge is directed u->v), let A_G=D+D^T, and put H=DD^T. For d=2m+1, the number C_alt of almost-alternating d-cycles is
\[
\boxed{C_{\rm alt}=\operatorname{tr}(H^mD)=\frac12\operatorname{tr}(H^mA_G).}
\tag{2}
\]
If R is the color-zero adjacency of the corresponding odd cube coloring, its number Z_0 of rooted oriented zero-colored antipodal full geodesics equals 2 C_alt. Thus unrestricted NORI1 is equivalent to the strict positivity of the nonnegative trace in (2) for all near-balanced orientations of all folded cubes in odd dimension.

*Proof.* A term of tr((DD^T)^m D) counts a closed walk of length 2m+1 whose successive traversals follow, oppose, follow, oppose, ..., follow the prescribed arc directions. Since the folded cube has odd girth d, every such walk is a simple d-cycle. Its start is the unique transit vertex, and its remaining vertices alternate sources and sinks. Conversely such a cycle has precisely one traversal starting from its transit vertex along its outgoing cycle edge, so the trace counts each once. Since H^m is symmetric, tr(H^mD)=tr(H^mD^T), establishing the second expression.

Index the cube's even vertices and odd vertices by the same antipodal quotient orbits; in this basis the red adjacency and antipodal permutation are
\[
R=\begin{pmatrix}0&D\\D^T&0\end{pmatrix},\qquad
P=\begin{pmatrix}0&I\\I&0\end{pmatrix}.
\]
Consequently tr(PR^d)=2tr((DD^T)^mD), proving the count identity. QED.

**Corollary (undirected two-step distance problem).** Form a graph C_D on V(G_d), joining two distinct vertices u,v when they share an out-neighbor in D, so H_(u,v)>0. Then an almost-alternating d-cycle exists if and only if some adjacent u,v in G_d can be joined by a path of length m in C_D. Any such length-m path consists of two-step moves in the binary-circuit generators, and uses each of the d-1 generators other than the closing edge precisely once.

*Proof.* Expanding (H^m)_(u,v) gives paths of m common-out-neighbor moves. Trace(H^mD) sums these entries over directed closing edges v->u. Positivity therefore means C_D has an m-step walk between G_d-neighbors. Such a walk produces an odd closed G_d-walk of length 2m+1=d and is consequently simple. Its generator sequence includes the closing generator once and every other generator once, by the binary-circuit relation. Distinctness of the original 2m generators also prevents repetitions or backtracking in the C_D path. QED.

The kernel H=DD^T is symmetric positive semidefinite and entrywise nonnegative. The unresolved positivity in (2) is therefore a question about a nonnegative Gram-kernel power meeting edges of the fixed folded cube graph. This form may support an isoperimetric, spectral or Hall-type forcing argument without choosing a starting cube root or a direction order.

**Correction: connected-component interpretation and a sharp distance parameter.** For the common-out-neighbor graph C_D, define
\[
\delta(D)=\min_{uv\in E(G_d)}\operatorname{dist}_{C_D}(u,v)\in\{m,m+1,\ldots\}\cup\{+\infty\}.
\tag{3}
\]
Let ell_0(c) be the least length of a zero-colored antipodal path in the corresponding odd-dimensional cube, or +infinity if none exists.

**Theorem 5.** The monochromatic detour identity is
\[
\boxed{\ell_0(c)=2\delta(D)+1.}
\tag{4}
\]
*Proof.* The block form of cube adjacency in Theorem 4 gives, for k>=0,
\[
\operatorname{tr}(PR^{2k+1})=2\operatorname{tr}((DD^T)^kD).
\]
Its left side counts zero-colored antipodal walks of length 2k+1. Every such walk contains a zero-colored antipodal simple path of no greater length, by deletion of closed subwalks. The right side is positive if and only if there is a directed folded-cube edge v->u with (H^k)_(u,v)>0. Since H_(v,v)=outdeg_D(v)>=m>=1, such an entry is positive if and only if u and v have distance at most k in the undirected support graph C_D (pad shorter walks by positive diagonal terms). The minimum feasible k is therefore delta(D), yielding the identity. Hamming distance in the cube gives ell_0(c)>=d=2m+1 and delta(D)>=m. QED.

**Lemma 6 (parity-component identification).** Components of C_D are in natural bijection with color-zero connected components of the original cube: each C_D component comprises the even-parity vertices of one color-zero connected component, indexed by antipodal quotient orbits. As the color-zero degree at every vertex is at least m>=1, each color-zero component meets both parity classes.

*Proof.* An edge uv in C_D is equivalent to a length-two zero-colored walk from even vertex u to even vertex v, through a shared odd red neighbor; conversely every two-step red path between even vertices gives such an edge. Any red walk between even vertices has even length and decomposes into two-step walks. QED.

**Essential limitation.** Even if a component of C_D contains two adjacent vertices of G_d, its distance between them may exceed m, so component connectivity does not establish NORI1. The Wu--Yang antipodal-path theorem already ensures delta(D) is finite for every legal odd coloring. Closure asks for the sharp upper bound delta(D)<=m, rather than merely finiteness. An admissible balanced Q5 orientation exhibits three C_D components (12,2,2 vertices): among the G5 edges whose endpoints lie in one C_D component, 12 have C_D-distance 2 and 8 have distance 3 (checked by enumerating paths). Thus larger distances occur even in successful colorings.

The previous corollary concerning a length-m C_D path remains valid. The stronger reading that success is equivalent to an edge anywhere inside a C_D component is withdrawn.

**Theorem 7 (exponentially many C_D components despite sharp closure).** For each r>=1 there is a nearly regular orientation D_r of the folded cube G_(4r+1), with all outdegrees 2r or 2r+1, whose common-out-neighbor graph C_(D_r) has precisely 3*2^(r-1) connected components while delta(D_r)=2r and hence the corresponding odd coloring has a monochromatic full geodesic.

*Proof.* Begin with the vertex-balanced antipodally odd Q4 coloring
\[
c_0=x_1,\quad c_1=x_0,\quad c_2=1-x_1,\quad c_3=1-x_0.
\tag{5}
\]
Its zero subgraph consists of a four-cycle on {3,7,11,15}, on which the first bit x_0 is uniformly 1, and a twelve-cycle containing vertices with x_0=0. It has a zero full antipodal geodesic, for example 1->9->8->10->14. Take r independent Cartesian copies on Q_(4r). Their zero subgraph is the Cartesian product of the factor zero subgraphs, hence consists of 2^r connected components, each a product of one of the two base cycles per block. All these old-direction edges retain their colors when adjoining a new bridge direction b with c_b(x,t)=x_0, reading bit zero of the first Q4 block. Thus the full Q_(4r+1) zero graph consists, over each product component K, of two layers K x {0,1}, joined by bridge edges precisely at the vertices of K with x_0=0.

For the 2^(r-1) product components with the first block's four-cycle, x_0=1 at every vertex, so their two layers remain separate, contributing 2*2^(r-1) zero components. For the other 2^(r-1) product components, at least one bridge edge joins their connected layers, contributing 2^(r-1) more. Total zero components are 3*2^(r-1). Lemma 6 identifies them with C_D components. All original zero degrees equal 2r and the bridge adds zero or one zero incident edge, so the folded orientation has the asserted outdegrees. The Cartesian product of the displayed base geodesics, with the bridge step inserted at an endpoint where its color is zero, provides a zero full antipodal geodesic of length 4r+1. Consequently delta(D_r)=2r by Theorem 5. QED.

**Theorem 8 (sublinear folded-distance excess suffices for all-dimensional closure).** Let delta(D) be as in Theorem 5. Unrestricted NORI1 is equivalent to the existence of a single uniform function epsilon(m)=o(m) such that every near-regular orientation of every G_(2m+1) satisfies
\[
\boxed{\delta(D)\le m+\epsilon(m).}
\tag{6}
\]

*Proof.* NORI1 implies delta(D)=m by Theorem 3, hence supplies epsilon=0. Conversely suppose a bad legal coloring exists. The established balanced counterexample-preserving reduction supplies a balanced bad coloring c on Q_(2q). Let ell be the minimum length of a zero-colored antipodal path in c; the Wu--Yang path theorem gives finiteness, and failure of a full geodesic forces ell>=2q+2. In the h-fold independent Cartesian product c^(box h), the shortest zero-colored antipodal path has length h ell: projection to each factor gives a zero antipodal walk of at least ell steps, while concatenating h shortest factor paths attains h ell. Add one bridge direction with any antipodally odd bit-reader as in Theorem 2. Projection of any zero antipodal walk from the enlarged cube to the old factors gives an antipodal zero walk of length at least h ell, and it must also use the bridge direction an odd positive number of times. Conversely a shortest factor-product zero path accepts a zero bridge step before or after its body, since the bridge reader reverses under antipodal complementation. Thus the shortest zero antipodal path in the enlarged Q_(2qh+1) has length h ell+1. By Theorem 5 the corresponding near-regular folded orientation satisfies
\[
\delta(D_h)=h\ell/2=qh+h(\ell-2q)/2\ge qh+h.
\]
Since its m parameter is qh, its distance excess is at least h=m/q, contradicting a uniform epsilon(m)=o(m) as h tends to infinity. QED.

This is the folded-graph counterpart of the previously published Cartesian amplification for monochromatic shortest-walk excess. It identifies an all-dimensional approximate-distance target; it is not by itself a proof that the target holds. Theorem 7 demonstrates why the number of C_D components cannot serve as a substitute for the minimum distance across G-edges.

## Paired-generator Hall obstruction to directed cycle covers

Let d=2m+1>=5 and let G_d be the folded cube on the even-weight subgroup V of F_2^d, with generators s_i=1+e_i. Its oriented adjacency matrix is D. A directed cycle cover is equivalent, by the bipartite matching criterion, to a perfect matching in the bipartite graph with adjacency D.

**Theorem 9 (near-balanced orientations can violate Hall in every odd dimension).** For every m>=2 there exists an orientation D of G_(2m+1) such that every vertex has outdegree m or m+1, but D has no directed cycle cover. More precisely, there are sets S,T with
\[
|S|=2^m,\quad |T|=2^m-1,\quad N_D^+(S)=T.
\tag{7}
\]

*Proof.* Partition [d]=I disjoint union J, where |I|=m+1 and |J|=m. Let S be the even vectors whose bits on J are all zero, and U the even vectors whose bits on J are all one. Then |S|=|U|=2^m. For i in I, an s_i-edge starting in S ends in U; for j in J, an s_j-edge starting in S ends outside S union U (because m>=2). Every t in U is adjacent, in each of the m+1 directions i in I, to a unique member of S.

Pair m generators i_1,...,i_m from I with the m generators j_1,...,j_m of J, leaving i_* in I unpaired. For each pair (i_k,j_k), the corresponding two-generator squares partition V. A square contains at most one member of S: its J-bit patterns are y, bar y, bar y+e_(j_k), y+e_(j_k), among which zero occurs at most once since m>=2. Orient every square as a directed 4-cycle, choosing its sense, whenever it meets S, so that the i_k-edge leaves S and the j_k-edge enters S. The orientations on squares disjoint from S are arbitrary. Every vertex then has one outgoing edge for each generator pair, hence m outgoing edges in total from those 2m generators. In particular every paired I-edge from S to U points outward, and every paired J-edge at S points inward. Every paired I-edge into U points toward U, and every paired J-edge at U points outward.

Choose t_0 in U and put w_k=t_0+s_(j_k) for k=1,...,m. Orient the unpaired generator-i_* matching outward from every s in S, and inward at each w_k. These requirements are consistent: the i_*-matching joins S to U; no w_k belongs to S union U; and w_j+w_k=e_(j_j)+e_(j_k) differs from s_(i_*) for j!=k (their Hamming weights are 2 and 2m). Orient all remaining matching edges arbitrarily.

The resulting orientation has outdegree m or m+1 everywhere. Every s in S has all m+1 I-edges outward and all m J-edges inward, so its outdegree is m+1. Every t in U has all m+1 I-edges inward and all m J-edges outward, so its outdegree is m. Each w_k has outdegree m by the choice of the unpaired matching.

Now reverse all m+1 edges t_0--(t_0+s_i), i in I, and all m edges t_0--w_k, k=1,...,m. Before reversal the former enter t_0 and the latter leave t_0. Its outdegree rises from m to m+1. Each of its m+1 neighbors in S loses one outgoing edge, changing from m+1 to m; each w_k gains one outgoing edge, changing from m to m+1. All other outdegrees are unchanged. After reversal every outgoing edge from S still uses a generator in I and ends in U other than t_0, while each t in U other than t_0 has incoming edges from S. Hence N_D^+(S)=U\{t_0}, proving (7).

Any directed cycle cover would give an injective successor assignment from S into N_D^+(S), contradicting (7). QED.

**Lemma 10 (uniform local common-out-neighbor branching).** For every near-balanced D on G_(2m+1), with m>=2, the undirected support graph C_D of H=DD^T satisfies
\[
\deg_{C_D}(u)\ge \frac{m(m-1)}2\qquad(u\in V).
\tag{8}
\]
Indeed, for each u, the weighted number of off-diagonal common-out-neighbor moves is
\[
\sum_{v\ne u}H_{uv}
=\sum_{w:u\to w}\bigl(\deg^-_D(w)-1\bigr)\ge m(m-1).
\]
Two distinct folded-cube vertices have at most two common neighbors: a two-generator sum s_i+s_j=e_i+e_j determines the unordered pair {i,j}, because the only dependence among the d generators uses all d of them. Therefore H_(u,v)<=2 for u!=v, giving (8). QED.

**Interpretation.** Every nearly balanced orientation has quadratic local branching in C_D, but a directed cycle cover need not exist. Theorem 9 disproves a general directed one-factor or doubly stochastic scaling route based solely on the orientation degrees and folded-cube incidence. It does not contradict the almost-alternating shortest-cycle assertion: the latter concerns a different kind of cycle.

**Independent audits.** The construction was generated in dimensions 5, 7, and 9, yielding Hall sets (|S|,|N^+(S)|)=(4,3),(8,7),(16,15). In each case all folded-cube edges were oriented once and all outdegrees were m or m+1. For d=5 the resulting orientation has 21 almost-alternating shortest odd cycles, counted independently by tr((DD^T)^2D), so the Hall obstruction occurs even in an orientation already possessing the required cycle.


**Theorem 11 (near-perfect directed Hall matching).** Let G be a directed graph on N vertices with all indegrees and outdegrees in {m,m+1}. Then the directed arc relation admits a matching covering at least N-floor(N/(2m+1)) vertices on both sides. Thus every near-balanced orientation of G_(2m+1) admits a permutation of its vertices respecting at least a fraction 1-1/(2m+1) of its directed arc assignments.

*Proof.* For any S subset V, write T=N^+(S), s=|S|, t=|T|, and k=s-t. Assume k>0. Counting all arcs leaving S yields ms <= (m+1)t=(m+1)(s-k), hence (m+1)k<=s. Write U=V\T and Z=V\S. All incoming arcs into U must start in Z, so m|U|<=(m+1)|Z|. Since |U|=N-s+k, obtain mk<=N-s. Adding gives (2m+1)k<=N. The deficiency version of Hall's matching theorem yields at most floor(N/(2m+1)) unmatched vertices. Extend that matching to a permutation arbitrarily on the remaining vertices. QED.

This improves the naive matching bound N/(m+1) to N/(2m+1), without using cubical structure. It complements the explicit Hall obstruction above: a full directed cycle cover can fail, but an arc-supported permutation with a vanishing fractional defect always exists. Such a permutation need not preserve geodesic direction labels or produce the required alternating shortest cycle; the result does not close NORI1.


Paired-square permutation reduction (proved). In the folded cube G_(2m+1), fix m direction pairs and a remaining direction z. Orient each paired-generator four-cycle cyclically. Each pair gives a permutation P_j of vertices consisting of four-cycles, with P_j^2 equal to translation by e_(a_j)+e_(b_j). Their squares commute, and their product is the generator-z translation. If M is the oriented z-matching, D=sum_j P_j+M and M+M^T=product_j P_j^2. All such orientations are near-balanced and have m directed cycle covers. This class is counterexample-universal: lift any hypothetical odd-coloring counterexample c on Q_m to its pointwise complementary paired lift on Q_(2m), then adjoin an odd bridge rule x_1. Geodesic failure persists by projection; complementary paired directions force every corresponding folded four-cycle to be cyclically oriented. Hence proving the almost-alternating girth-cycle theorem in this paired-square class would settle unrestricted NORI1. One cannot insist that the final trace arc lies in M: the legal odd coloring c_(a_j)=x_z, c_(b_j)=1-x_z, c_z=x_(b_1) has full monochromatic geodesics but requires z to appear in the middle position of every such geodesic. Therefore tr((DD^T)^m M)=0 while tr((DD^T)^m D)>0. The counterexample-universal target instead involves compatibility of the noncommuting permutation square roots P_j.
