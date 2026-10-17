## Coxeter Galleries and Flag Geometry

### Introduction — problems, geometry, and research objectives

#### Purpose and mathematical status

This article investigates a geometric route toward **one common path-selection principle** for two problems: the NORI1 antipodally odd coloring problem on cube edges, and the one-switch Hamilton tight-path problem for ordinary reversal-odd boundary 3-tournaments. It develops the *type-\(A\) root system*, alternating rook galleries, Freudenthal/Coxeter chambers, and equivariant chain methods as possible ingredients of such a principle. The distinctive feature of this direction is that it arises from an existing chain-level Borsuk–Ulam proof rather than from axioms designed solely to contain the two graph families.

**Current status.** The ordered-pair encoding of boundary tournaments, its type-\(A\) root embedding, and the Gram-matrix criterion for Hamilton tight paths are proved. The corresponding universal topological selector is **not proved**. Nor is there yet a faithful reduction sending every NORI1 coloring to the same type-\(A\) gallery-existence problem. All subsequent research should distinguish these theorems from the proposed common mechanism.

The article is meant to be readable independently. The surrounding NORI papers and the Toolkit are optional sources for additional proofs, obstructions, and literature; the essential definitions, full-strength targets, and decoding requirements appear below.

#### The two original path problems

##### NORI1: antipodally odd coloring of cube edges

Let \(Q_n\) have vertex set \(\mathbb F_2^n\), with an undirected edge between \(x\) and \(x\oplus e_i\) for each \(i\in[n]\). Write \(\bar x=x\oplus\mathbf1\) for the antipode, and \(\bar e\) for the image of an undirected edge under vertex complementation. An arbitrary binary edge coloring
\[
c:E(Q_n)\longrightarrow\mathbb F_2
\]
belongs to **NORI1** when
\[
c(\bar e)=1-c(e).
\tag{I.1}
\]
There is no linearity, independence, direction-invariance, or root restriction in the definition.

A full antipodal geodesic is
\[
P(x,\pi):x,\;x\oplus e_{\pi_1},\;
x\oplus e_{\pi_1}\oplus e_{\pi_2},\ldots,\bar x,
\tag{I.2}
\]
where the **root** \(x\) and the permutation \(\pi\in S_n\) are freely chosen. It traverses each cube dimension once. The open NORI1 conjecture asks for one such geodesic with every edge of the same binary color. This is stronger than merely finding an arbitrary monochromatic path between antipodal vertices.

For a binary word \(w=(w_1,\ldots,w_m)\), write
\[
\operatorname{sw}(w)=
\sum_{i=1}^{m-1}\mathbf1_{\{w_i\ne w_{i+1}\}}.
\tag{I.3}
\]
The NORI1 monochromatic conclusion is equivalent to requiring some *full* antipodal geodesic with at most one switch. Indeed, root-slide rotation after the first \(j\) dimensions changes its edge word to
\[
(w_{j+1},\ldots,w_n,\,1-w_1,\ldots,1-w_j).
\tag{I.4}
\]
Cutting after the unique switch in a one-switch word makes all the rotated edge colors equal. This already established lemma is detailed in Article IX; its formula is included here to state the common target without losing NORI1.

**Root selection is essential:** the existence of a favorable permutation at a prescribed cube root, or a favorable root for a prescribed permutation, is not guaranteed. Both variables must be allowed to move together.

##### Boundary 3-tournaments: a vertex-simple spanning tight path

Let \(V\) be an arbitrary \(n\)-element set, \(n\ge3\). An **ordinary reversal-odd boundary 3-tournament** is an arbitrary function
\[
b:\{(a,h,c)\in V^3:a,h,c\text{ pairwise distinct}\}
\longrightarrow\mathbb F_2
\]
satisfying only
\[
b(c,h,a)=1-b(a,h,c).
\tag{I.5}
\]
Different reversal orbits of triples are independently colored. No global ordering of undirected edges or other representability is assumed.

A Hamilton tight path is an ordering \(v_1,\ldots,v_n\) in which every element of \(V\) occurs once. Its consecutive overlapping ordered-triple word is
\[
b(v_1,v_2,v_3),\;
b(v_2,v_3,v_4),\ldots,
b(v_{n-2},v_{n-1},v_n).
\tag{I.6}
\]
The full-strength boundary conjecture asks for a Hamilton ordering with **at most one binary switch** in (I.6). A long nonspanning monochromatic tight path is insufficient, as is an undirected path in an auxiliary state graph that revisits original vertices. This problem does not have an additional freely chosen cube root; its varying parameter is the Hamilton ordering itself.

#### The type-A sphere and the faithful tournament representation

Put
\[
\Omega_V=\{(a,h)\in V^2:a\ne h\},\qquad
W_V=\{z\in\mathbb R^V:\sum_{v\in V}z_v=0\}.
\tag{I.7}
\]
A **rook arc** changes one entry of an ordered pair while keeping the other fixed. The entry-swap involution
\[
\tau(a,h)=(h,a)
\]
acts as an antipode under the type-\(A_{n-1}\) root embedding
\[
\rho(a,h)=e_a-e_h\in W_V,
\qquad
\rho(\tau q)=-\rho(q).
\tag{I.8}
\]
The normalized roots lie on the sphere \(S(W_V)\cong S^{n-2}\).

The boundary bit \(b(a,h,c)\) labels the two oriented rook arcs
\[
(a,h)\to(c,h),\qquad (h,a)\to(h,c).
\tag{I.9}
\]
Call this directed-arc labeling \(\beta\). Reversal of a *directed arc* changes its bit; entry-swap of both endpoint pairs preserves it:
\[
\beta(u\to v)=1-\beta(v\to u),
\qquad
\beta(\tau u\to\tau v)=\beta(u\to v).
\tag{I.10}
\]
Every binary labeling satisfying (I.10) is obtained from a unique boundary tournament. **Do not confuse** (I.10) with oddness of an undirected edge coloring under \(\tau\). The vertex involution is antipodal in the root embedding; the tournament-bit reversal is expressed using the direction of the rook arc. This distinction is vital to valid transfer arguments.

The Hamilton ordering \(v_1,\ldots,v_n\) produces the alternating rook gallery
\[
q_i=
\begin{cases}
(v_i,v_{i+1}),&i\text{ odd},\\
(v_{i+1},v_i),&i\text{ even},
\end{cases}
\qquad i=1,\ldots,n-1.
\tag{I.11}
\]
The changed pair entry alternates at every move, and
\[
\beta(q_i\to q_{i+1})=
b(v_i,v_{i+1},v_{i+2}).
\tag{I.12}
\]
Hence this encoding preserves both the **underlying ordered path** and its entire switch word.

There is also a geometric decoding certificate. Set \(r_i=\rho(q_i)\). The roots associated with a Hamilton ordering satisfy
\[
\boxed{\langle r_i,r_j\rangle=
2\delta_{ij}+\mathbf1_{\{|i-j|=1\}}.}
\tag{I.13}
\]
Conversely any \(n-1\) type-\(A\) roots with this Gram matrix reconstruct an alternating rook gallery of a Hamilton ordering, up to global entry swap and reversal of the vertex ordering. The matrix is the standard type-\(A_{n-1}\) Cartan matrix conjugated by alternating signs; it has determinant \(n\). In particular the roots form a basis of \(W_V\), and the required nonrepetition of original symbols is encoded directly by this root geometry. The next Subsection proves the equivalence, including the coherent rook-arc coloring.

Thus the complete boundary conjecture can be restated without weakening it:

> Every labeling \(\beta\) of rook arcs satisfying (I.10) admits a sequence of \(n-1\) type-\(A\) roots satisfying (I.13), whose successive rook-arc bits switch at most once.

This is a faithful **equivalent formulation**, not a theorem asserting such a sequence exists.

#### Connection with Freudenthal triangulation and Wu–Yang

A full monotone cube geodesic is a maximal saturated chain of the Boolean lattice \(2^{[n]}\), hence a top simplex of the Freudenthal triangulation of \([0,1]^n\). Complementing cube vertices and reversing a saturated chain induces a natural antipodal action on its windows and chamber orders. Independently, the orderings \(v_1,\ldots,v_n\) parameterize the chambers of the type-\(A_{n-1}\) Coxeter arrangement in \(W_V\).

Hehui Wu and Ningyuan Yang, *A Chain-Level Borsuk–Ulam Obstruction Proof of Norine's Antipodal-Coloring Conjecture* (2026), https://arxiv.org/abs/2607.19276, prove that every antipodally odd two-coloring of cube edges has a monochromatic **path**, not necessarily a geodesic, connecting some vertex to its antipode. Their proof assumes such paths do not exist, associates to each cube vertex \(x\) the ordered pair of red connected-component indices
\[
(p(x),p(\bar x)),
\tag{I.14}
\]
and uses the same entry-swap involution on ordered pairs. Every cube edge gives a rook move in this pair-label space. Mapping a pair \((a,h)\) to \(e_a-e_h\) and applying Freudenthal subdivision, subdivision-invariant root-cone chains, and a chain-level Borsuk–Ulam obstruction yields the contradiction.

**Why this connection matters.** The alphabet \(\Omega_V\), its type-\(A\) roots, and its antipodal involution are already native to a successful topological proof concerning cube antipodality. Boundary tournaments naturally produce paths in that same root alphabet, but with additional alternation, basis, and switch constraints. This suggests a possible common *chain-level selection or obstruction mechanism* rather than a combination of unrelated structural axioms.

**Why Wu–Yang does not settle either remaining target.** Negating the NORI1 *geodesic* claim does not prohibit monochromatic antipodal paths with detours, so the component-pair construction (I.14) need not exist. A Freudenthal rook gallery in their argument also need not alternate its changing pair entry, span \(W_V\), or have at most one switch. A Borsuk–Ulam zero or a chain obstruction must therefore be accompanied by a valid **full-path decoding theorem**. The two problems cannot be unified merely because they involve the same sphere or involution.

#### Research agenda and proof obligations

The guiding question is whether one can obtain a common, intrinsic **equivariant selection theorem for coherent complete paths**, strong enough to specialize to both models without adding class-specific escape clauses.

A proposed solution must meet the following tests.

1. **Common topological carrier.** Construct a space of compatible partial-path certificates from the coloring and the original path incidence, not a space whose simplices are only pairwise plausible. Prove an equivariant covering, connectivity, index, chain, or intersection condition that holds in both surviving classes.
2. **NORI1 extraction, including roots.** The selected object must reconstruct a full \(n\)-edge antipodal cube geodesic with at most one edge-bit switch, letting its starting vertex and dimension order vary jointly. A root-fixed theorem is not sufficient; root rotation then supplies the monochromatic conclusion.
3. **Boundary extraction, including all vertices.** The selected object must reconstruct one forward/coherent Hamilton tight path on all \(n\) original symbols with at most one triple-bit switch. In the rook model, this means alternation and the type-\(A\) Gram condition (I.13), not mere undirected monochromatic connectivity.
4. **Oddness and orientation.** Track the involution of *vertices* separately from reversal of directed arcs or geodesic chains. Preserve the two independently imposed coloring constraints in any simultaneous-labeling construction. Avoid assuming that the involution preserves an additional ordinary edge coloring.
5. **Obstruction tests.** Check every candidate selector against the established failure of fixed-root and fixed-order methods, incompatible path fragments, and stronger coloring classes known to require many switches. Record scope-limited failures as research notes instead of silently strengthening hypotheses.

The immediate research opportunity is to examine whether the root-pair/type-\(A\) chain-map architecture can be adapted to **legally realizable full-geodesic certificates**, while using the Gram geometry above to certify the boundary output. The next Subsection supplies the basic root geometry and faithful decoding theorem. The NORI Toolkit entry \`literature_wu_yang_norine_chain_level_borsuk_ulam\` summarizes the paper's proof architecture. Article IX records the separate cyclic-variation and root-selection results; Article XIV does not require reading it to understand the present definitions and goals.

**Boundary of what is proved:** the geometric identifications and encoding equivalences here are established mathematics; the common root-sensitive topological selection theorem and both full-strength conjectural existence statements remain open.

### Alternating type-A roots characterize Hamilton tight paths

#### Ordered-pair geometry and an orientation-sensitive coloring

Let \(V\) be an \(n\)-element set, \(n\ge3\), and put
\[
\Omega_V=\{(a,b):a,b\in V,\ a\ne b\},\qquad
W_V=\{z\in\mathbb R^V:\sum_{v\in V}z_v=0\}.
\]
The involution \(\tau(a,b)=(b,a)\) becomes the antipodal map under
\[
\rho(a,b)=e_a-e_b\in W_V,\qquad \rho(\tau q)=-\rho(q).
\tag{1}
\]
The unit vectors \(\rho(q)/\sqrt2\) lie on \(S(W_V)\cong S^{n-2}\). An *oriented rook arc* is an ordered pair of states differing in one entry, either \((a,h)\to(c,h)\) or \((h,a)\to(h,c)\), with distinct \(a,h,c\).

**Proposition 1 (tournament–arc equivalence).** Boundary 3-tournaments
\[
b(a,h,c)\in\mathbb F_2,\qquad b(c,h,a)=1-b(a,h,c)
\tag{2}
\]
are in bijection with binary labels \(\beta\) on oriented rook arcs that satisfy
\[
\beta(v,u)=1-\beta(u,v),\qquad
\beta(\tau u,\tau v)=\beta(u,v).
\tag{3}
\]
The correspondence is
\[
\beta((a,h),(c,h))
=\beta((h,a),(h,c))=b(a,h,c).
\tag{4}
\]

*Proof.* Every oriented rook arc has one of the two forms in (4). Reversing either arc exchanges \(a,c\), so (2) gives the first equality in (3). Applying \(\tau\) interchanges its row and column representations, giving the second. Conversely a row arc determines every ordered triple and (3) recovers the reversal condition; thus the assignment is bijective. \(\square\)

**Warning about involutions.** The type-A *vertex* involution is odd in (1), while the directed-arc coloring is invariant under its induced \(\tau\)-action and odd under arc reversal. In particular (3) is not the condition \(\beta(\tau e)=1-\beta(e)\) on undirected edges. The two operations must not be conflated.

#### A simple-root characterization of complete tight paths

For any ordered vertex word \(v_1,\ldots,v_n\) with distinct consecutive triples, associate the ordered-pair states
\[
q_i=
\begin{cases}
(v_i,v_{i+1})& i\text{ odd},\\
(v_{i+1},v_i)&i\text{ even},
\end{cases}
\quad 1\le i\le n-1.
\tag{5}
\]
Adjacent \(q_i\)'s differ in the first entry at odd \(i\) and the second at even \(i\), so \(q_1\to\cdots\to q_{n-1}\) is an alternating rook gallery. Its \(\beta\)-word is the original sequence of consecutive triple bits:
\[
\beta(q_i,q_{i+1})=b(v_i,v_{i+1},v_{i+2}),\quad 1\le i\le n-2.
\tag{6}
\]

**Theorem 2 (type-A Gram criterion).** A sequence \(q_1,\ldots,q_{n-1}\in\Omega_V\) is an alternating rook encoding of a Hamilton ordering of all \(n\) symbols, in one of the two globally \(\tau\)-related orientations, if and only if its type-A roots \(r_i=\rho(q_i)\) have Gram matrix
\[
\boxed{
\langle r_i,r_j\rangle=
\begin{cases}
2&i=j,\\
1&|i-j|=1,\\
0&|i-j|\ge2.
\end{cases}}
\tag{7}
\]
Equivalently, writing \(C_{A_{n-1}}\) for the type-A Cartan matrix and \(D=\operatorname{diag}(1,-1,1,-1,\ldots)\), the Gram matrix is \(DC_{A_{n-1}}D=2I+A(P_{n-1})\).

*Proof (forward).* For the associated Hamilton order, let \(\alpha_i=e_{v_i}-e_{v_{i+1}}\) be the consecutive simple roots of the Weyl chamber indexed by \((v_1,\ldots,v_n)\). Equation (5) gives \(r_i=(-1)^{i-1}\alpha_i\). The simple-root inner products are \(2\) on the diagonal, \(-1\) for consecutive positions, and zero otherwise. Alternating the signs yields (7).

*Proof (reverse).* Each \(r_i=e_{a_i}-e_{b_i}\) determines the undirected symbol pair \(E_i=\{a_i,b_i\}\). For distinct type-A roots, inner product \(1\) means that the two symbol pairs share one symbol, appearing with the same sign; inner product \(0\) means disjoint symbol pairs. Thus (7) says that consecutive \(E_i\)'s share one symbol and nonconsecutive \(E_i\)'s are disjoint. Consequently their union is a path of \(n-1\) distinct edges on \(n\) distinct symbols, giving a Hamilton ordering \(v_1,\ldots,v_n\), unique up to reversal of its vertex word. The positive inner products at consecutive positions further force the shared symbol to appear with the same sign in both roots. Along the path, the shared signs alternate, because the two endpoints of the middle root have opposite signs. The entire root sequence is therefore (5), or its global image under \(\tau\), for the reconstructed ordering. \(\square\)

**Corollary 3 (basis and switch decoding).** Every root sequence with Gram matrix (7) is automatically a basis of \(W_V\), since its Gram determinant is \(n\): the determinant of the leading \(j\times j\) tridiagonal block satisfies \(\Delta_j=2\Delta_{j-1}-\Delta_{j-2}\), with \(\Delta_0=1,\Delta_1=2\), hence \(\Delta_j=j+1\). The boundary one-switch Hamilton problem is therefore equivalent to finding \(n-1\) type-A roots obeying (7), with a rook-arc labeling \(\beta\) of form (3), whose \(n-2\) successive arc bits switch at most once. This is an equivalent *path characterization*, not an existence theorem.

Under full reversal of the vertex word, the rook state sequence becomes \(\operatorname{rev}(q)\) when \(n\) is odd, and \(\tau(\operatorname{rev}(q))\) when \(n\) is even. By (3), in both cases the directed-arc bit word is complemented and reversed, as it should be for a boundary tournament.

#### Coxeter chambers and the chain-level antipodal connection

A Hamilton ordering \((v_1,\ldots,v_n)\) determines the type-\(A_{n-1}\) Weyl chamber
\[
\{z\in W_V:z_{v_1}\ge z_{v_2}\ge\cdots\ge z_{v_n}\}.
\]
Its consecutive simple roots are the \(\alpha_i\) in the forward proof above. Thus the boundary problem is a colored *chamber-selection problem* in which successive alternating-sign simple roots satisfy (7) and their connecting rook arcs have at most one bit switch. The root-basis condition and nonrepetition of original symbols are built into the type-A chamber rather than asserted for an arbitrary auxiliary walk.

The link with Wu–Yang's chain-level Borsuk–Ulam proof of Norine's antipodal-coloring conjecture is structural: their rook labels lie in the same \(\Omega_V\), their involution interchanges the ordered-pair entries, and they send \((a,b)\) to the same root \(e_a-e_b\) in the sphere \(S(W_V)\). Their use of Freudenthal monotone galleries and chain-valued root cones supplies a relevant technique for topological selection. Their published conclusion, however, concerns a monochromatic antipodal path that need not be a geodesic. A failure of NORI1's monochromatic *geodesic* conclusion does not imply their off-diagonal component-pair rook labeling exists: a monochromatic non-geodesic path may still join antipodes. Furthermore a Wu–Yang rook gallery need not have Gram matrix (7), alternating rook moves, or a low-switch arc word.

This delineates the missing work. A common proof would have to construct from the original cube-edge coloring and from arbitrary reversal-odd boundary tournaments a *faithful* gallery carrier; establish an equivariant selection or chain obstruction on that carrier; and extract an entire gallery obeying its corresponding spanning-path conditions and at most one switch. The type-A criterion is intrinsic for boundary tournaments, but no claim is made that NORI1 itself has a matching type-A basis geometry. Neither a general Borsuk–Ulam zero nor unrestricted rook adjacency forces the Gram pattern (7).

**Source and relation.** Wu and Yang, *A Chain-Level Borsuk–Ulam Obstruction Proof of Norine's Antipodal-Coloring Conjecture*, arXiv:2607.19276 (2026), recorded in Toolkit entry \`literature_wu_yang_norine_chain_level_borsuk_ulam\`. Companion Article XIV research note: \`note_05a0824513a6316fac1be336\`. Earlier undirected ordered-pair reduction and its failure to preserve directed Hamilton witnesses: \`note_ordered_pair_antipodal_graph_bridge_and_decoding_obstruction_20261011\`.

### Cyclic type-A root fans and the two path involutions

#### Complete fans of Hamilton cuts

Let \(V\) have \(n\ge3\) symbols and let \(W=\{z\in\mathbb R^V:\sum_vz_v=0\}\). For a linear ordering \(\pi=(v_1,\ldots,v_n)\), put
\[
K(\pi)=\operatorname{cone}(e_{v_1}-e_{v_2},\ldots,e_{v_{n-1}}-e_{v_n})\subset W.
\tag{1}
\]
This positive simple-root cone is distinct from the dual Weyl chamber described by inequalities \(z_{v_1}\ge\cdots\ge z_{v_n}\). If \(\pi^{\rm rev}\) is the reversed ordering, then
\[
K(\pi^{\rm rev})=-K(\pi).
\tag{2}
\]

**Theorem 1 (cyclic simplex fan).** Fix an oriented cyclic ordering \(C=(v_1,\ldots,v_n)\), indexed modulo \(n\), and set
\[
\gamma_i=e_{v_i}-e_{v_{i+1}},\qquad K_i=\operatorname{cone}\{\gamma_j:j\ne i\}.
\tag{3}
\]
The \(n\) cones \(K_i\) are the maximal cones of a complete simplicial fan in \(W\), satisfying
\[
K_i\cap K_k=\operatorname{cone}\{\gamma_j:j\notin\{i,k\}\}\quad(i\ne k).
\tag{4}
\]
Their unit-sphere intersections constitute a simplicial decomposition of \(S^{n-2}\) combinatorially isomorphic to the boundary of an \((n-1)\)-simplex. The maximal cone \(K_i\) equals \(K(\pi_i)\), where the Hamilton ordering \(\pi_i=(v_{i+1},\ldots,v_n,v_1,\ldots,v_i)\) is obtained by cutting \(C\) after \(v_i\). In particular every maximal cone is a certificate for a spanning ordering and its type-A root basis.

*Proof.* The vectors \(\gamma_i\) are the signed incidence vectors of the edges of a cycle. Every \(n-1\) are independent, they span \(W\), and their relation space is generated by \(\sum_i\gamma_i=0\). Thus each \(z\in W\) has a representation \(z=\sum_i t_i\gamma_i\), with the coefficient vector unique modulo adding a constant to every entry. Subtracting \(\min_i t_i\) makes all coefficients nonnegative and at least one coefficient zero. It follows that \(z\in K_i\) if and only if \(t_i\) is a minimum. The simultaneous-minimum condition for \(i,k\) gives (4), and the analogous condition for arbitrary sets of indices identifies all intersections as faces. Since every proper subset of the rays is independent, the resulting fan is simplicial. Its faces are the cones generated by proper subsets of \(\{\gamma_1,\ldots,\gamma_n\}\), which form the boundary face poset of a simplex. Deleting \(\gamma_i\) leaves the consecutive roots of \(\pi_i\), proving the last claim. \(\square\)

**Corollary 2 (multiplicity and mod-two cancellation).** Let \(z\in W\) satisfy \(\sum_{v\in A}z_v\ne0\) for each nonempty proper \(A\subset V\). Among all \(n!\) linear orderings \(\pi\), precisely \((n-1)!\) have \(z\in K(\pi)\): one from each oriented cyclic ordering. Consequently the unweighted sum of all \(n!\) spherical root cones, interpreted as top-dimensional chains on any common triangulation, vanishes over \(\mathbb F_2\) for \(n\ge3\). Each individual cyclic fan, on the other hand, represents the mod-two fundamental class of the sphere.

*Proof.* The coefficients in Theorem 1 obey \(z_{v_i}=t_i-t_{i-1}\). Any difference \(t_i-t_k\) equals a sum of \(z\)-entries along a proper nonempty consecutive arc of \(C\). The stated hypothesis makes the \(t_i\) pairwise distinct. One index minimizes them, so one cone from each cyclic fan contains \(z\). There are \((n-1)!\) oriented cyclic orderings on \(V\). Each fan contributes the sphere's fundamental chain on a common subdivision, while \((n-1)!\) is even for \(n\ge3\). Their unweighted sum therefore cancels over \(\mathbb F_2\). \(\square\)

Reversal of \(C\) negates and permutes its \(\gamma_i\), taking the cyclic fan to its antipodal fan. Thus cyclic classes of Hamilton orderings support complete, antipodally paired sphere carriers in which every maximal cell has a spanning-path decoding. The cancellation identifies a limitation of unweighted mod-two chamber chains: a nonzero global chain obstruction must involve additional coloring or incidence data.

#### A common reversal involution with different root transport

Identify \(V=[n]\) with the dimensions of \(Q_n\). A *cube geodesic flag* is \((x,\pi)\), where \(x\in\mathbb F_2^n\) is the freely chosen initial vertex and \(\pi\) is the dimension order of a full antipodal geodesic \(P(x,\pi)\). A *boundary tight-path flag* is a Hamilton vertex order \(\pi\). Both project to \(K(\pi)\). Each cone carries \(2^n\) cubical flags, one for each root, and one boundary flag.

**Proposition 3 (common antipodal reversal; distinct cyclic monodromy).** Let \(c\) be any NORI1 edge coloring, and let \(b\) be any reversal-odd boundary 3-tournament. Write \(w_c(x,\pi)\) for the \(n\)-edge color word of \(P(x,\pi)\) and \(w_b(\pi)\) for the \((n-2)\)-triple color word of the boundary Hamilton path. Then
\[
w_c(x,\pi^{\rm rev})=\mathbf1-\operatorname{rev}w_c(x,\pi),\qquad
w_b(\pi^{\rm rev})=\mathbf1-\operatorname{rev}w_b(\pi).
\tag{5}
\]
Both flag reversals cover the antipodal cone map (2), and both retain the full-length path interpretation. Fix a cyclic ordering \(C=(v_1,\ldots,v_n)\) and its cuts \(\pi_i\) from Theorem 1. The root-slide transport on cubical flags is
\[
T:(x,\pi_i)\longmapsto(x\oplus e_{v_{i+1}},\pi_{i+1}),
\tag{6}
\]
with indices modulo \(n\). It satisfies
\[
T^n(x,\pi_i)=(\bar x,\pi_i),\qquad
T^{2n}(x,\pi_i)=(x,\pi_i).
\tag{7}
\]
Over any oriented cyclic fan there are \(2^{n-1}\) root-slide orbits, each of length \(2n\). By comparison, the cyclic-cut transport on boundary tight-path flags returns to its starting flag after \(n\) cuts. Hence the two path systems share the antipodal simple-root-cone base and the color-word reversal law, with complementary-root and identity monodromy around a cyclic ordering, respectively.

*Proof.* Reversing the cube dimension order while retaining \(x\) reverses the antipodal image of the original geodesic. Its edges are antipodal to the original edges in reverse sequence. NORI1 oddness proves the first part of (5). Reversing a boundary vertex ordering reverses and complements each of its consecutive triple bits, proving the second part. Equation (2) gives the geometric action. Taking the first step of a cube geodesic and moving that dimension to the end gives (6). After \(n\) such steps every dimension has been flipped once, proving (7). The cut index first returns after \(n\) steps, when the root has changed to its distinct antipode, so the orbit length is \(2n\). There are \(n2^n\) flags over a fixed cyclic rotation class; division by \(2n\) gives \(2^{n-1}\) orbits. For boundary orders, cyclically moving the first vertex to the end returns to the same word after \(n\) steps. \(\square\)

The shared root-cone carrier preserves unrestricted NORI1 root choice and vertex-simple boundary Hamilton orderings. Selecting an individual maximal cone still requires proving a one-switch color condition; for NORI1 it additionally requires selecting a compatible cube-root flag over that cone. No universal selector is asserted here.

### Zigzag comparison complexes and the antipodal sphere of Hamilton galleries

Let \(V\) have \(n\ge3\) elements and let \(W=\{z\in\mathbb R^V:\sum_{v\in V}z_v=0\}\). For a permutation \(\pi=(v_1,\ldots,v_n)\) and \(\sigma\in\{-1,1\}\), define
\[
r_i(\pi,\sigma)=\sigma(-1)^{i-1}(e_{v_i}-e_{v_{i+1}}),\qquad 1\le i<n,
\]
and its **dual zigzag cone**
\[
C_{\pi,\sigma}=\{z\in W:\langle z,r_i(\pi,\sigma)\rangle\ge0
\text{ for every }1\le i<n\}.
\tag{1}
\]
The ordered roots have Gram matrix \(2I+A(P_{n-1})\). Thus each \((\pi,\sigma)\) encodes a Hamilton alternating rook gallery, with \(\sigma=-1\) corresponding to entry-swap of every rook state. The inequalities in (1) orient every edge \(v_iv_{i+1}\) of the Hamilton path from the endpoint with the larger required value of \(z\) toward the smaller one; denote the resulting alternately oriented Hamilton path by \(D_{\pi,\sigma}\). In particular, an arc \(u\to v\) means \(z_u\ge z_v\).

**Theorem 1 (Hamilton gallery nerve).** The spherical sets
\[
S_{\pi,\sigma}=C_{\pi,\sigma}\cap S(W)
\]
form a finite antipodally invariant cover of \(S(W)\cong S^{n-2}\). Their nerve \(\mathcal N_n\), with vertices \((\pi,\sigma)\), has the following combinatorial characterization:
\[
\boxed{\quad
F\in\mathcal N_n
\iff
\bigcup_{(\pi,\sigma)\in F}D_{\pi,\sigma}
\text{ is not strongly connected}.
\quad}
\tag{2}
\]
Every nonempty finite intersection of sets \(S_{\pi,\sigma}\) is contractible. The involution
\[
(\pi,\sigma)\longmapsto(\pi,-\sigma)
\tag{3}
\]
acts freely on \(\mathcal N_n\), and its geometric realization is \(\mathbb Z_2\)-equivariantly homotopy equivalent to \(S^{n-2}\) with its antipodal action.

*Proof.* Every \(z\in W\) admits a permutation satisfying
\[
z_{v_1}\ge z_{v_2}\le z_{v_3}\ge z_{v_4}\le\cdots:
\]
successively choose the largest remaining entry, the smallest remaining entry, and so on. Such a \(z\) lies in \(C_{\pi,+1}\), proving the covering assertion. Equation (1) gives \(C_{\pi,-1}=-C_{\pi,+1}\), hence antipodal invariance.

For a nonempty family \(F\), let \(D_F=\bigcup_{(\pi,\sigma)\in F}D_{\pi,\sigma}\). If \(D_F\) is strongly connected, the inequalities \(z_u\ge z_v\) along every directed path force all entries of any \(z\in\bigcap_F C_{\pi,\sigma}\) to agree. Since \(z\in W\), their common value is zero. Thus the spherical intersection is empty. Conversely, if \(D_F\) has at least two strongly connected components, its condensation is a directed acyclic graph. Assign strictly decreasing real values along a topological ordering of its components, then subtract their weighted mean over \(V\). The resulting nonzero vector lies in \(W\) and satisfies every inequality represented by \(D_F\). Normalizing it gives a point of the spherical intersection. This proves (2).

Each cone \(C_{\pi,\sigma}\) is pointed: if \(z\) and \(-z\) both belong to it, all consecutive entries of \(z\) are equal along the Hamilton path, so \(z=0\). Every intersection of these cones is convex and lies in one pointed cone. A nonempty intersection with \(S(W)\) is therefore contractible: fix a point \(z_0\) in it and contract \(z\) toward \(z_0\) along the normalized straight-line interpolation. The denominator stays positive because a pointed cone contains no pair of opposite nonzero vectors. These spherical polyhedra admit a common triangulation, so the finite good-cover nerve lemma identifies \(|\mathcal N_n|\) with \(S(W)\) up to homotopy. This identification is equivariant by the antipodally paired cones and the equivariant nerve lemma.

Finally \(C_{\pi,+1}\cap C_{\pi,-1}=\{0\}\). Hence no nerve simplex contains both \((\pi,+1)\) and \((\pi,-1)\). Every simplex fixed setwise by (3) would contain such a pair, so the simplicial involution has no fixed simplex. \(\square\)

The characterization (2) realizes the antipodal sphere as a simplicial complex defined entirely in terms of compatible collections of **complete Hamilton paths**. In particular the nonrepetition condition is retained at each vertex of the nerve; compatibility of several vertices is decided by strong connectivity of their combined comparison digraph. The nerve construction is independent of a boundary-tournament coloring. Under the rook entry-swap involution, the directed-arc labels \(\beta\) are preserved, so \((\pi,+1)\) and \((\pi,-1)\) carry the same triple-bit word. Consequently antipodality of this carrier alone imposes no oddness relation on those words; any color-sensitive obstruction must also use directed-arc reversal or additional incidence data.

The use of **dual** cones in Theorem 1 is necessary for its covering assertion. Positive hulls of the alternating root bases do not enjoy the analogous property.

**Proposition 2 (open holes in the positive-root cone family).** For \(n\ge4\), let
\[
P_{\pi,\sigma}=\left\{\sum_{i=1}^{n-1}t_i r_i(\pi,\sigma):t_i\ge0\right\}.
\]
Then \(\bigcup_{\pi,\sigma}P_{\pi,\sigma}\) misses a nonempty open subset of \(W\), and hence misses a nonempty open subset of \(S(W)\).

*Proof.* Given \(z\in W\) and \(\pi=(v_1,\ldots,v_n)\), write \(A_i=\sum_{j=1}^i z_{v_j}\). Since the \(r_i(\pi,\sigma)\) form a basis of \(W\), its expansion coefficients are
\[
t_i=\sigma(-1)^{i-1}A_i.
\tag{4}
\]
Thus membership in \(P_{\pi,\sigma}\) requires its successive partial sums \(A_i\) to alternate weakly in sign.

Choose distinct symbols \(a,b\in V\) and set
\[
z_a=1,\qquad z_b=-\tfrac12,\qquad
z_v=-\frac1{2(n-2)}\quad(v\notin\{a,b\}).
\tag{5}
\]
These entries sum to zero. If \(A_1>0\), then \(v_1=a\), and \(A_2>0\) for every choice of \(v_2\), so the signs cannot alternate. If \(A_1<0\), obtaining \(A_2\ge0\) requires \(v_2=a\). When \(v_1=b\), this gives \(A_2=1/2\), and any third entry leaves \(A_3>0\). When \(v_1\notin\{a,b\}\), this gives \(A_2=1-1/[2(n-2)]\), and again any third entry leaves \(A_3>0\). Because \(n\ge4\), three partial sums are present; neither possible alternating sign pattern occurs. Every exclusion is strict, so the same conclusion holds in an open neighborhood of \(z\). \(\square\)

Theorem 1 supplies an intrinsic antipodal topological carrier for the Hamilton-gallery geometry. Proposition 2 separates this carrier from the positive-root-cone geometry used in chain-level rook-label arguments. Neither result establishes that a given reversal-odd boundary labeling admits a gallery with at most one color switch; that requires a theorem involving the labeling as well as the carrier.

Let \(V\) be a set of \(n\ge3\) symbols and
\[
W=\{z\in\mathbb R^V:\sum_{v\in V}z_v=0\},\qquad
u_a^{\,h}=e_a-e_h\quad(a\ne h).
\]
For each \(h\in V\), the \(n-1\) vectors \(u_a^{\,h}\), \(a\ne h\), form a basis of \(W\). Write \(\operatorname{Alt}^2(W)\) for the space of alternating real bilinear forms on \(W\). The two-valued sign convention below is \(s(a,h,c)=(-1)^{b(a,h,c)}\).

**Theorem 1 (faithful center-indexed two-form representation).** Assignment
\[
\boxed{\quad
\omega_h(u_a^{\,h},u_c^{\,h})=(-1)^{b(a,h,c)}
\quad(a,c\ne h,\ a\ne c)
\quad}                                                   \tag{1}
\]
is a bijection between ordinary reversal-odd boundary 3-tournaments \(b\) on \(V\) and families \((\omega_h)_{h\in V}\) of alternating bilinear forms on \(W\) whose values in (1) belong to \(\{-1,1\}\). The forms at distinct centers \(h\) may be prescribed independently.

Moreover, if \(q_1,\ldots,q_{n-1}\) is the alternating rook encoding of a Hamilton ordering \(v_1,\ldots,v_n\), and \(r_i=e_{(q_i)_1}-e_{(q_i)_2}\), then
\[
\boxed{\quad
(-1)^{b(v_i,v_{i+1},v_{i+2})}
=\omega_{v_{i+1}}(r_i,r_{i+1})
\qquad(1\le i\le n-2).
\quad}                                                   \tag{2}
\]
Thus the boundary one-switch Hamilton problem is equivalent to finding an ordered root basis \(r_1,\ldots,r_{n-1}\) with Gram matrix \(2I+A(P_{n-1})\) for which the sequence of signs in (2) changes at most once.

*Proof.* For fixed \(h\), specifying the values of an alternating form on the ordered pairs of distinct basis vectors \(u_a^{\,h}\) determines that form uniquely. The condition \(b(c,h,a)=1-b(a,h,c)\) says
\[
(-1)^{b(c,h,a)}=-(-1)^{b(a,h,c)},
\]
precisely the alternating condition. Conversely, prescribing arbitrary values \(+1\) or \(-1\) for the \(\binom{n-1}{2}\) unordered pairs of basis vectors produces a unique \(\omega_h\) and the corresponding \(b\) at center \(h\). Different centers involve disjoint reversal orbits of ordered triples; there are therefore
\[
n\binom{n-1}{2}=3\binom n3
\]
independent bits, as required.

For the rook gallery, put \(h=v_{i+1}\). If \(i\) is odd, then
\[
(r_i,r_{i+1})=(u_{v_i}^{\,h},u_{v_{i+2}}^{\,h});
\]
if \(i\) is even, both roots are the negatives of these two vectors. Bilinearity makes simultaneous negation invisible, proving (2). This also proves that the formula respects entry swap \(\tau\) of rook states, while alternation changes its sign upon reversing a directed rook arc. The Gram characterization of Hamilton rook galleries supplies the final equivalence. \(\square\)

The use of one form per center is intrinsic to the full tournament class. Replacing the family by one alternating form on \(W\) introduces an additional constraint.

**Proposition 2 (cyclic restriction of a global two-form).** Let \(\omega\in\operatorname{Alt}^2(W)\), and put
\[
B_\omega(a,h,c)=\omega(e_a-e_h,e_c-e_h).
\]
Then \(B_\omega\) is alternating under every permutation of its three distinct arguments. In particular,
\[
B_\omega(a,h,c)=B_\omega(h,c,a)=B_\omega(c,a,h).
\tag{3}
\]
Consequently, any boundary 3-tournament obtained by taking the signs of \(B_\omega(a,h,c)\), assuming these values are nonzero, is invariant under cyclic rotation of its ordered triples. For \(n\ge3\), the cyclically invariant tournaments form a fraction
\[
2^{-2\binom n3}                                          \tag{4}
\]
of all reversal-odd boundary 3-tournaments.

*Proof.* Extend \(\omega\) to the formal basis vectors \(e_v\) by restricting their arguments to \(W\), and write \(\Omega_{ac}=\omega(e_a-e_o,e_c-e_o)\) for an arbitrary reference symbol \(o\). The expansion
\[
B_\omega(a,h,c)=\Omega_{ac}+\Omega_{ha}+\Omega_{ch}
\tag{5}
\]
is independent of the reference \(o\). Its cyclic invariance and change of sign under exchange of two arguments are immediate. A reversal-odd boundary 3-tournament has three independent reversal-orbit bits on each unordered three-element set; cyclic invariance identifies those three bits. Hence there are \(2^{3\binom n3}\) unrestricted tournaments and \(2^{\binom n3}\) cyclically invariant ones, giving (4). \(\square\)

The restriction can be sharpened for **real-valued** arc data, independently of a sign threshold.

**Proposition 3 (cocycle criterion for a global two-form).** Suppose \(B(a,h,c)\in\mathbb R\) is defined on ordered distinct triples. There exists \(\omega\in\operatorname{Alt}^2(W)\) such that
\[
B(a,h,c)=\omega(e_a-e_h,e_c-e_h)
\tag{6}
\]
for every ordered triple if and only if \(B\) is alternating under all permutations and satisfies
\[
B(b,c,d)-B(a,c,d)+B(a,b,d)-B(a,b,c)=0                    \tag{7}
\]
for all distinct \(a,b,c,d\). When \(n=3\), condition (7) is vacuous.

*Proof.* Equation (5) writes \(B\) as the negative of the simplicial coboundary of the alternating edge values \(\Omega_{ab}\). Alternation and (7) follow by cancellation. Conversely, fix \(o\in V\), and prescribe alternating edge values by
\[
\Omega_{oa}=0,\qquad
\Omega_{ac}=-B(o,a,c)\quad(a,c\ne o).
\]
These values define an alternating form on \(W\) through the basis \(\{e_a-e_o:a\ne o\}\). If \(a,h,c\ne o\), (7) on \(o,a,h,c\) gives
\[
B(a,h,c)
=B(o,h,c)-B(o,a,c)+B(o,a,h)
=\Omega_{ac}+\Omega_{ha}+\Omega_{ch}.
\]
The same identity is immediate when one of \(a,h,c\) equals \(o\), using alternation. Equation (6) follows. \(\square\)

Propositions 2–3 locate the limitation of a single exterior two-form: it enforces cyclic symmetry, and its real values also satisfy tetrahedral identities. The full boundary class instead corresponds to the independent center-indexed forms of Theorem 1. The antipodal root map acts by \(r\mapsto-r\), and each alternating form satisfies \(\omega_h(-r,-s)=\omega_h(r,s)\). Consequently the induced rook-arc labels are invariant under simultaneous antipodal entry swap and reversed upon reversal of the directed arc, matching the required two distinct symmetries.

This representation retains every Hamilton gallery and every tournament coloring, and it supplies a finite-dimensional algebraic formulation for a potential chain-level selector. No existence theorem for a one-switch Hamilton gallery follows from bilinearity alone: the forms \(\omega_h\) are independent, while the sought roots must jointly satisfy the Gram condition.

### Signed type-B chambers as paired-symbol type-A Hamilton orders

Let \(Q_n\) have vertices \(x\in\mathbb F_2^n\). A full antipodal geodesic is determined by its root \(x\) and dimension permutation \(\pi=(i_1,\ldots,i_n)\). Define its signed word
\[
w(x,\pi)=(w_1,\ldots,w_n),\qquad w_j=(-1)^{x_{i_j}}i_j.
\tag{1}
\]
These words, containing one of \(\{+i,-i\}\) for each \(i\), are the chambers of the type-\(B_n\) reflection arrangement. In particular the free choice of cube root is encoded by the signs of a Coxeter chamber.

**Theorem 1 (paired-symbol type-A realization).** Let
\[
U=\{+1,-1,\ldots,+n,-n\},\qquad
L=\{z\in\mathbb R^U:z_{-i}=-z_{+i}\text{ for each }i\}.
\]
Then \(L\) is an \(n\)-dimensional subspace of \(W_U=\{z:\sum_{u\in U}z_u=0\}\). The restriction to \(L\) of the type-\(A_{2n-1}\) braid arrangement \(z_u=z_v\) is the type-\(B_n\) arrangement
\[
t_i=0,\qquad t_i=t_j,\qquad t_i=-t_j\quad (i\ne j),
\tag{2}
\]
where \(t_i=z_{+i}\). Moreover,
\[
\boxed{
(x,\pi)\longmapsto H(x,\pi)=(w_1,\ldots,w_n,-w_n,\ldots,-w_1)
}
\tag{3}
\]
is a bijection between full cube geodesics with specified roots and Hamilton orders of \(U\) satisfying \(H_{2n+1-j}=-H_j\) for every \(j\). Each of these orders has a type-A simple-root basis of \(W_U\); its Weyl chamber intersects \(L\) in a full-dimensional type-B chamber.

*Proof.* The equations defining \(L\) imply \(\sum_{u\in U}z_u=0\). Intersecting \(z_{+i}=z_{-i}\), \(z_{+i}=z_{+j}\), and \(z_{+i}=z_{-j}\) with \(L\) yields respectively \(t_i=0\), \(t_i=t_j\), and \(t_i=-t_j\). These exhaust the braid hyperplanes after restriction.

Given a signed word \(w\), choose a point of \(L\) with
\[
z_{w_1}>z_{w_2}>\cdots>z_{w_n}>0,\qquad z_{-w_j}=-z_{w_j}.
\tag{4}
\]
Such points exist by assigning decreasing positive magnitudes. The complete ordering of its \(2n\) entries is then
\[
z_{w_1}>\cdots>z_{w_n}>z_{-w_n}>\cdots>z_{-w_1},
\]
so (3) determines a type-A Weyl chamber whose intersection with \(L\) has nonempty interior. Conversely, an order satisfying the displayed symmetry consists of \(n\) signed entries followed by their negatives in reverse order. Its first half uses one member of every signed pair, and recovers \(x\) and \(\pi\) uniquely from (1). The \(2n-1\) consecutive roots \(e_{H_j}-e_{H_{j+1}}\) form a type-A simple-root basis, proving the claim. \(\square\)

Under cube complementation the signed word becomes \(-w\), while
\[
H(\bar x,\pi)=\operatorname{rev}H(x,\pi).
\tag{5}
\]
Thus vertex antipodality in the cube is represented by reversal of a paired-symbol Hamilton order.

**Theorem 2 (Coxeter rotation and color transport).** Define the operations on signed words
\[
T(w_1,\ldots,w_n)=(w_2,\ldots,w_n,-w_1),\qquad
R(w_1,\ldots,w_n)=(-w_n,\ldots,-w_1).
\tag{6}
\]
The map \(T\) is right multiplication by the signed cycle \((2,3,\ldots,n,-1)\), a Coxeter element of \(B_n\), and
\[
T^nw=-w,\quad T^{2n}w=w,\quad R^2w=w,\quad RTR=T^{-1}.
\tag{7}
\]
Let \(c\) be any binary undirected-edge coloring satisfying \(c(\bar e)=1-c(e)\), and let \(C(w)=(C_1(w),\ldots,C_n(w))\) be the edge-color word of the geodesic corresponding to \(w\). Then
\[
\begin{aligned}
C(Tw)&=(C_2(w),\ldots,C_n(w),1-C_1(w)),\\
C(-w)&=\mathbf1-C(w),\\
C(Rw)&=\operatorname{rev}C(w).
\end{aligned}
\tag{8}
\]

*Proof.* Right multiplication by the signed permutation sending \(j\) to \(j+1\) for \(j<n\) and \(n\) to \(-1\) has the action \(T\). It is a product of the adjacent-transposition simple reflections and a sign-changing simple reflection of \(B_n\). The algebraic identities (7) follow by substitution.

If \(w=w(x,\pi)\), then \(Tw\) represents the geodesic rooted at \(x\oplus e_{i_1}\) with dimension order \((i_2,\ldots,i_n,i_1)\). Its first \(n-1\) edges are the final \(n-1\) edges of the original geodesic, and its last edge is the antipodal image of the original first edge. This proves the first equality of (8). The signed word \(-w\) represents \((\bar x,\pi)\), giving the second equality by antipodal oddness. The word \(Rw\) represents \((\bar x,\operatorname{rev}\pi)\), which follows the original geodesic backward, giving the third. \(\square\)

Theorems 1–2 retain unrestricted NORI1 root choice while placing all its complete paths inside type-A Hamilton-order geometry. The type-B chamber sphere \(S(L)\cong S^{n-1}\) is an antipodal subsphere of the type-\(A_{2n-1}\) sphere \(S(W_U)\cong S^{2n-2}\). Thus root variation is an intrinsic sign dimension of the chamber representation, and root sliding is the signed Coxeter rotation (6).

This is a faithful embedding of the path geometry. To transfer the path-existence conjecture from ordinary boundary 3-tournaments one would additionally need a valid correspondence between the cube-edge word and a reversal-odd labeling of consecutive triples on the paired-symbol alphabet, or a selection theorem that applies to both label types. The chamber embedding by itself makes no such correspondence.

### Coxeter chambers and reconstruction from local color-word identities

Let \(V=[n]\), \(n\ge3\). The open chambers of the type-\(A_{n-1}\) arrangement in \(W=\{z\in\mathbb R^n:\sum_i z_i=0\}\) are
\[
A(\pi)=\{z:z_{\pi_1}<\cdots<z_{\pi_n}\}\quad(\pi\in S_n).
\]
These chambers parameterize Hamilton vertex orderings, triangulate \(S^{n-2}\), and obey \(-A(\pi)=A(\pi^{\mathrm{rev}})\).

The open chambers of the type-\(B_n\) arrangement \(z_i=0,\ z_i=\pm z_j\) are
\[
B(x,\pi)=\{z:0<|z_{\pi_1}|<\cdots<|z_{\pi_n}|,
\ \operatorname{sgn}(z_i)=(-1)^{x_i}\},
\quad x\in\mathbb F_2^n,\ \pi\in S_n.
\]
They parameterize all rooted antipodal cube geodesics \(P(x,\pi)\), triangulate \(S^{n-1}\), and obey \(-B(x,\pi)=B(\bar x,\pi)\). Thus the cube's freely chosen root is the sign part of a signed permutation. Each chamber in either model certifies a full path: distinct cube dimensions in type \(B\), and distinct original vertices in type \(A\).

Write \(s_i\pi\) for exchanging entries at positions \(i,i+1\), and \(R\pi=(\pi_2,\ldots,\pi_n,\pi_1)\).

**Theorem 1 (NORI1 word reconstruction).** A family of binary words \(w(x,\pi)=(w_1,\ldots,w_n)\), indexed by \(x\in\mathbb F_2^n,\pi\in S_n\), is induced by a unique antipodally odd coloring of the undirected cube edges if and only if it satisfies
\[
w_j(x,s_i\pi)=w_j(x,\pi)\quad(j\notin\{i,i+1\}),\tag{C1}
\]
\[
w(x\oplus e_{\pi_1},R\pi)
=(w_2(x,\pi),\ldots,w_n(x,\pi),1-w_1(x,\pi)),\tag{C2}
\]
and
\[
w(x,\pi^{\mathrm{rev}})
=\mathbf1-\operatorname{rev}(w(x,\pi)).\tag{C3}
\]

*Proof.* Given an undirected antipodally odd edge coloring, swapping neighboring dimensions changes only the two edges traversed within their square. Rotating the first dimension to the end after traversing it preserves the remaining \(n-1\) edges and appends the antipodal image of the first edge. Reversing the dimension order while retaining the root gives the antipodal image of the reversed path. These observations yield (C1)–(C3).

Conversely, for \(i\in[n]\) and \(y\in\mathbb F_2^n\), set
\[
a_i(y)=w_1(y,\pi)\quad\text{where }\pi_1=i.\tag{1}
\]
Adjacent swaps among positions \(2,\ldots,n\) connect all such orders and preserve their first word entry by (C1); hence \(a_i\) is well defined. Applying (C2) successively \(j-1\) times moves the \(j\)-th letter to the first position without crossing the final complemented seam. Thus
\[
w_j(x,\pi)=a_{\pi_j}\!\left(x\oplus\sum_{k<j}e_{\pi_k}\right).\tag{2}
\]
Applying (C2) \(n\) times returns to the original permutation at the complementary root and complements all word entries, proving
\[
a_i(\bar y)=1-a_i(y).\tag{3}
\]
Take an order \(\pi\) with \(\pi_n=i\). Its reversal begins with \(i\). Equations (C3) and (2) give
\[
a_i(y)=1-a_i(\bar y\oplus e_i)=a_i(y\oplus e_i),\tag{4}
\]
where (3) gives the final equality. Therefore \(a_i(y)\) is independent of which endpoint of \(\{y,y\oplus e_i\}\) is selected. Define the color of that edge to be \(a_i(y)\). Equation (3) gives antipodal oddness, (2) reconstructs every word, and (1) proves uniqueness. \(\square\)

**Theorem 2 (boundary-tournament word reconstruction).** A family \(u:S_n\to\mathbb F_2^{n-2}\) is induced by a unique ordinary reversal-odd boundary 3-tournament through
\[
u_j(\pi)=b(\pi_j,\pi_{j+1},\pi_{j+2})\tag{5}
\]
if and only if
\[
u_j(s_i\pi)=u_j(\pi)
\quad\text{whenever }\{j,j+1,j+2\}\cap\{i,i+1\}=\varnothing,\tag{T1}
\]
\[
u_j(R\pi)=u_{j+1}(\pi)\quad(1\le j\le n-3),\tag{T2}
\]
and
\[
u(\pi^{\mathrm{rev}})=\mathbf1-\operatorname{rev}(u(\pi)).\tag{T3}
\]

*Proof.* A tournament \(b\) makes (T1) immediate, since the selected ordered triple remains unchanged. Cyclic transport preserves overlapping triples and proves (T2), while reversal oddness proves (T3).

Conversely, for pairwise distinct \(a,h,c\), set \(b(a,h,c)=u_1(\pi)\) for any permutation beginning with \((a,h,c)\). All such permutations are connected by adjacent swaps in positions \(4,\ldots,n\); these preserve \(u_1\) by (T1). This defines \(b\) independently of the unspecified suffix. Iterating (T2) brings the triple at positions \(j,j+1,j+2\) to the beginning while retaining its bit; hence (5) holds. If \(\pi\) begins with \((a,h,c)\), then \(\pi^{\mathrm{rev}}\) ends in \((c,h,a)\). Using (T3) and (5),
\[
b(c,h,a)=u_{n-2}(\pi^{\mathrm{rev}})
=1-u_1(\pi)=1-b(a,h,c).
\]
Thus \(b\) is reversal odd, and its uniqueness follows from its defining first-window values. \(\square\)

**Scope of the reconstruction.** The three axioms in each theorem impose the shared-incidence compatibility of the underlying coloring, in addition to antipodal word symmetry. The hypotheses of Theorem 1 preserve every possible NORI1 root and place no restrictions on the independent antipodal edge orbits. The hypotheses of Theorem 2 preserve all ordinary boundary-tournament reversal orbits and every Hamilton ordering. All maximal certificates are full rank: the cube's move vectors are distinct standard basis vectors, while the consecutive type-\(A\) incidence roots of a Hamilton ordering form a basis of \(W\).

These two sets of intrinsic axioms provide a verifiable starting point for a common color-sensitive selection theorem. The missing assertion is an equivariant or homological principle that, using such incidence-compatible exchange data, selects a maximal certificate whose word has at most one switch.

### Alternating-word obstructions on type-A and type-B chambers

Put \(\epsilon(\pi)=\operatorname{inv}(\pi)\bmod2\) and \(\operatorname{rot}(\pi)=(\pi_2,\ldots,\pi_n,\pi_1)\). Then
\[
\epsilon(\operatorname{rot}\pi)=\epsilon(\pi)+n-1,\qquad
\epsilon(\pi^{\rm rev})=\epsilon(\pi)+\binom n2\pmod2.
\tag{1}
\]

**Theorem 1 (type-B example).** For \(n\ge7\), \(n\equiv3\pmod4\), prescribe the following word on every root-and-order flag \((x,\pi)\) of an antipodal cube geodesic:
\[
w_j(x,\pi)=j-1+|x|+\epsilon(\pi)\pmod2,\qquad1\le j\le n.
\tag{2}
\]
Each word alternates, so has \(n-1\) switches. Nevertheless, the family obeys
\[
w(x\oplus e_{\pi_1},\operatorname{rot}\pi)
=(w_2,\ldots,w_n,1-w_1),\quad
w(x,\pi^{\rm rev})=\mathbf1-\operatorname{rev}w(x,\pi).
\tag{3}
\]
Every represented geodesic is dimension-simple. The family cannot arise from an undirected cube-edge coloring because it violates (C1), the adjacent-exchange incidence identity.

*Proof.* Rotation of an odd-length permutation preserves its parity, whereas changing the initial root by one dimension flips \(|x|\bmod2\). The new word therefore has letters \(w'_j=j+|x|+\epsilon(\pi)\); they equal \(w_{j+1}\) for \(j<n\) and \(1-w_1\) for \(j=n\). Reversal of the permutation flips parity because \(\binom n2\) is odd. For odd \(n\), reversal preserves the alternating position word, so complementing it gives the stated reversal relation. Finally, any adjacent permutation swap flips \(\epsilon(\pi)\), complementing even the unaffected edge positions, contrary to (C1). \(\square\)

**Theorem 2 (type-A example).** For \(n\ge8\), \(n\equiv0\pmod4\), prescribe on every Hamilton vertex-order flag \(\pi\)
\[
u_j(\pi)=j-1+\epsilon(\pi)\pmod2,\qquad1\le j\le n-2.
\tag{4}
\]
Each word alternates, hence has \(n-3\) switches. Nevertheless,
\[
u_j(\operatorname{rot}\pi)=u_{j+1}(\pi)\ (1\le j\le n-3),
\quad u(\pi^{\rm rev})=\mathbf1-\operatorname{rev}u(\pi).
\tag{5}
\]
The family cannot arise from an ordinary reversal-odd boundary 3-tournament because it violates (T1), the adjacent-exchange shared-triple identity.

*Proof.* Rotation of an even-length permutation changes its parity, giving the cyclic overlap relation in (5). Reversal preserves parity for \(n\equiv0\pmod4\); the alternating word of even length has complementary reversal, yielding the second relation. An adjacent swap complements all word letters, including windows that do not touch the swapped positions, contrary to (T1). \(\square\)

**Corollary.** Full matroid rank, antipodally symmetric type-A or type-B chamber spheres, reversal of color words, and their respective cyclic shift laws do not together force one-switch maximal paths. Counterexamples exist in arbitrarily high dimensions in *both* classes of flag spaces, although neither example descends to a coloring of the shared local incidences. Every proposed unification must include this descent compatibility and employ it in the existence argument.

The formulas were independently checked for thousands of random type-B flags with \(n=7\) and for all \(8!\) type-A flags with \(n=8\).

### A single Coxeter-coset formulation of the two one-switch conjectures

This formulation uses only classical Coxeter groups, parabolic stabilizers of local path incidences, and a Coxeter element. It preserves unrestricted root selection in NORI1 and Hamilton vertex-simplicity in boundary tournaments; it does not postulate an auxiliary graph of galleries.

#### General coset-word problem

Let \(G\) be a finite group, \(K\le G\), \(t\in G\), and \(\rho\in N_G(K)\setminus K\) with \(\rho^2\in K\). A **reversal-odd coset coloring** is any function \(f:G\to\mathbb F_2\) satisfying
\[
f(gk)=f(g)\quad(k\in K),\qquad
f(g\rho)=1-f(g)\quad(g\in G).
\tag{1}
\]
The first equation means that \(f\) is a coloring of local incidences \(G/K\); the second pairs those incidences under the fixed-point-free involution \(gK\mapsto g\rho K\). Fix a length \(m\ge2\). For a complete flag \(g\in G\), define its Coxeter-orbit window word
\[
\mathsf w_g=(f(g),f(gt),\ldots,f(gt^{m-1})).
\tag{2}
\]
The proposed **parabolic-coset one-switch conclusion** is
\[
\boxed{\text{Some }g\in G\text{ has }\operatorname{sw}(\mathsf w_g)\le1.}
\tag{3}
\]
The following two canonical Coxeter instances recover the open conjectures without changing their mathematical strength.

#### Type \(A_{n-1}\): boundary 3-tournaments

For \(n\ge3\), take \(G=S_n\), acting on \([n]\), and let
\[
K_A=\{\sigma\in S_n:\sigma(1)=1,\ \sigma(2)=2,\ \sigma(3)=3\}
=\langle(4\,5),(5\,6),\ldots,(n-1\,n)\rangle.
\]
Let \(t_A=(1\,2\,\cdots\,n)\) (a Coxeter element), \(\rho_A=(1\,3)\), and \(m_A=n-2\). The subgroup \(K_A\) is standard parabolic, and \(\rho_A\) commutes with it. A right coset \(gK_A\) is determined by the ordered triple \((g(1),g(2),g(3))\). The involution \(gK_A\mapsto g\rho_AK_A\) reverses its outside entries.

**Theorem 1.** Assigning \(b(a,h,c)=f(g)\) when \(g(1)=a,g(2)=h,g(3)=c\) gives a bijection between functions satisfying (1) for \((G,K_A,\rho_A)\) and ordinary reversal-odd boundary 3-tournaments. For the complete flag \(g\), equation (2) is
\[
\mathsf w_g=(b(g(1),g(2),g(3)),\ b(g(2),g(3),g(4)),\ldots,
b(g(n-2),g(n-1),g(n))).
\tag{4}
\]
Consequently (3) is equivalent to the boundary one-switch Hamilton tight-path conjecture.

*Proof.* Right \(K_A\)-invariance says that the bit depends only on the first three entries; right \(\rho_A\)-oddness says that interchanging the first and third entry complements it. Since \(t_A^{j-1}\) sends positions \((1,2,3)\) to \((j,j+1,j+2)\) for \(1\le j\le n-2\), the word formula follows. Every \(g\) is a permutation of all \(n\) vertices, so the corresponding path is Hamilton. \(\square\)

#### Type \(B_n\): NORI1

For \(n\ge2\), let \(G=B_n=\mathbb F_2^n\rtimes S_n\), acting on cube vertices by
\[
(a,\sigma)\cdot x=a\oplus\sigma x,\qquad
(a,\sigma)(b,\tau)=(a\oplus\sigma b,\sigma\tau).
\tag{5}
\]
Let \(E_0=\{0,e_1\}\) be the initial undirected cube edge and set
\[
K_B=\operatorname{Stab}_{B_n}(E_0)
=\{(a,\sigma):a\in\{0,e_1\},\ \sigma(1)=1\}.
\tag{6}
\]
This is the standard parabolic subgroup generated by sign-flip \(s_0\) in the first dimension and adjacent swaps \(s_2,\ldots,s_{n-1}\) among the remaining dimensions. Put
\[
t_B=(e_1,(1\,2\,\cdots\,n)),\quad
\rho_B=z=(\mathbf1,\mathrm{id})=t_B^n,\quad m_B=n.
\tag{7}
\]
Here \(t_B\) is a Coxeter element of order \(2n\), and \(z\) is its central antipodal half-turn. The right cosets \(G/K_B\) correspond to undirected cube edges \(gE_0\), with \(g\rho_BK_B\) representing their antipodal mates.

**Theorem 2.** Functions satisfying (1) for \((G,K_B,\rho_B)\) are in bijection with unrestricted antipodally odd colorings of undirected edges of \(Q_n\). If \(g=(x,\sigma)\), equation (2) is the edge-color word along the full antipodal geodesic beginning at \(x\) and using dimensions
\[
\sigma(1),\ \sigma(2),\ldots,\sigma(n)
\tag{8}
\]
in that order. Consequently (3) is equivalent to the NORI1 one-switch formulation, and hence to its monochromatic full-geodesic formulation by root-slide rotation.

*Proof.* A cube-edge coloring is the same as a right-\(K_B\)-invariant function of \(g\), because \(K_B\) stabilizes \(E_0\); the central element \(z\) sends each edge to its antipodal image, yielding (1). Let \(\eta=(1\,2\,\cdots\,n)\). The power \(t_B^{j-1}\) has translation component \(e_1+\cdots+e_{j-1}\), and its permutation component sends \(1\) to \(j\). Thus \(g t_B^{j-1}E_0\) is the \(\sigma(j)\)-edge beginning at
\[
x\oplus e_{\sigma(1)}\oplus\cdots\oplus e_{\sigma(j-1)}.
\]
These are precisely the successive edges of (8). Every \(g\in B_n\) gives a freely chosen root and an independent permutation of all dimensions, establishing the bijection and the claim. \(\square\)

#### Unified conjecture and the proof obligation

**Conjecture (classical Coxeter parabolic-coset one-switch principle).** For each of the canonical type-A and type-B tuples \((G,K,t,\rho,m)\) above, every right-\(K\)-invariant, right-\(\rho\)-odd binary function \(f\) has a Coxeter-orbit segment \(\mathsf w_g\) with at most one switch.

Theorems 1 and 2 prove that this is a single algebraic statement recovering both original conjectures. They do not prove its existence assertion. The specific parabolic stabilizers and Coxeter-element windows are essential; the unrestricted statement for all finite groups and all subgroups is false.

**Proposition 3 (a failed extension within type B).** Replace \(K_B\) by \(K_{\rm vertex}=\{(0,\sigma):\sigma\in S_n\}\), the stabilizer of the cube vertex \(0\), retaining \(t_B,z\) and \(m=n\). For every odd \(n\ge5\), the right-\(K_{\rm vertex}\)-invariant function
\[
f((x,\sigma))=|x|\pmod2
\]
is \(z\)-odd and has \(n-1\) switches on every Coxeter-orbit word. Thus (3) fails for this alternative parabolic subgroup.

*Proof.* Vertex cosets are identified by \(x\). Since \(n\) is odd, parity changes when all \(n\) bits are complemented, so the coloring is \(z\)-odd. Each multiplication by \(t_B\) changes the flag root by one previously unused dimension, flipping vertex parity. Therefore all consecutive window entries differ. \(\square\)

#### Coxeter-cycle reformulation of the outstanding proof

For type B, \(t_B^n=z\), and hence the length-\(2n\) cyclic sequence \(f(gt_B^j)\) is antiperiodic at separation \(n\). Its \(n\) cyclic change indicators have odd sum \(D_B(g)\). A complete one-switch segment exists in the \(t_B\)-orbit of \(g\) if and only if \(D_B(g)=1\); then moving the root to the unique cyclic change yields a monochromatic full geodesic. Therefore NORI1 asks whether every admissible \(f\) has some Coxeter cycle with \(D_B=1\).

For type A, \(t_A^n=1\). Its circular word has even total change count \(D_A(g)\); cutting to the \(n-2\) tournament triple windows removes three consecutive change indicators. The circular-switch criterion already established in Article IX gives
\[
\min_{\ell}\operatorname{sw}(\mathsf w_{g t_A^\ell})
=D_A(g)-\max_{\ell}(d_\ell+d_{\ell+1}+d_{\ell+2}).
\tag{9}
\]
Thus the boundary conjecture asks whether some Coxeter cycle has \(D_A\le2\), or \(D_A=4\) with three consecutive changes. These are two forms of a common Coxeter-cycle minimization problem under right-parabolic incidence descent.

The remaining mathematical challenge is to use right-\(K\)-invariance to couple different Coxeter cycles and force one of these low-variation configurations. Pure cyclic parity cannot suffice: deleting the parabolic invariance admits the alternating-word constructions proved in the preceding subsection.

### Orientation gauges and a common involutive directed-arc symmetry

Let \(G\) be a finite simple graph with a fixed-point-free vertex involution \(\tau\). For a directed arc \(a=(u,v)\), write \(a^{-1}=(v,u)\). Assume that no undirected edge is fixed setwise by \(\tau\), and choose an orientation \(o\) of every edge such that \(\tau\) reverses these choices. Put \(\theta(a)=0\) if \(a\) agrees with \(o\), and \(\theta(a)=1\) otherwise. Then
\[
\theta(a^{-1})=1-\theta(a),\qquad
\theta(\tau a)=1-\theta(a).
\tag{1}
\]

**Theorem (orientation-gauge equivalence).** The formula
\[
\boxed{\beta(a)=c(\{u,v\})+\theta(a)\pmod2}
\tag{2}
\]
is a bijection from antipodally odd undirected-edge colorings \(c\), meaning \(c(\tau e)=1-c(e)\), to binary directed-arc labels satisfying
\[
\boxed{
\beta(a^{-1})=1-\beta(a),\qquad \beta(\tau a)=\beta(a).
}
\tag{3}
\]

*Proof.* Both identities follow by substituting (1) into (2). Conversely, given (3), define \(c(\{u,v\})=\beta(a)+\theta(a)\) for either directed orientation of the edge. Changing the orientation complements both summands, leaving their sum unchanged. Applying \(\tau\) preserves \(\beta\) and complements \(\theta\), so \(c(\tau e)=1-c(e)\). The two constructions are inverse. \(\square\)

**Cube specialization.** Take \(G=Q_n\) with \(\tau x=\bar x\), \(n\ge2\). Orient each dimension-\(i\) edge from its endpoint with \(x_i=0\) to its endpoint with \(x_i=1\). The orientation is reversed by \(\tau\), and \(\theta(x,x\oplus e_i)=x_i\). Consequently
\[
\boxed{
\beta(x,x\oplus e_i)
=c(\{x,x\oplus e_i\})+x_i\pmod2
}
\tag{4}
\]
gives a faithful representation of every unrestricted NORI1 coloring by the labels (3).

**Boundary-tournament specialization.** Let \(\Omega_V=\{(a,h):a\ne h\}\) be the rook states with involution \(\tau(a,h)=(h,a)\). For distinct \(a,h,c\), define
\[
\beta((a,h),(c,h))
=\beta((h,a),(h,c))
=b(a,h,c).
\tag{5}
\]
A reversal-odd boundary tournament, characterized by \(b(c,h,a)=1-b(a,h,c)\), yields the same directed-arc relations (3). Every such tournament arises this way, with independent choices at distinct middle vertices.

Equations (3) are thus a common intrinsic coloring symmetry for both full classes. Their *observable* path words retain an essential distinction: the cube geodesic reads \(\beta(a)+\theta(a)\), whereas a boundary Hamilton rook gallery reads \(\beta(a)\). The former path traverses each dimension once; the latter requires an alternating rook sequence whose type-A roots form a basis. The shared symmetry by itself does not imply a one-switch complete path, and the cubical orientation correction must be retained.

### Linear-threshold one-switch theorem in both Coxeter models

We use the Coxeter parabolic-coset representation from the preceding subsection. Its two local-incidence spaces admit equivariant vector labels in the reflection representations, negated by their coset reversal involutions. A linear threshold of these vectors consequently defines a reversal-odd coloring. The theorem below produces a complete low-switch path in both types.

#### The common threshold construction

Let \(G\) be either \(S_n\) (type \(A_{n-1}\)) or \(\mathbb F_2^n\rtimes S_n\) (type \(B_n\)), with \(K,\rho,t,m\) as in the preceding subsection. Let \(V\) be the real reflection representation, and choose the following \(K\)-fixed vector:
\[
q_A=e_1-e_3\in W=\{z\in\mathbb R^n:\sum_i z_i=0\},\qquad
q_B=\sum_{i=2}^n e_i\in\mathbb R^n.
\tag{1}
\]
In both cases \(\rho q=-q\). Hence
\[
R(gK)=gq
\tag{2}
\]
is a well-defined \(G\)-equivariant local-incidence vector satisfying \(R(g\rho K)=-R(gK)\). For any \(\theta\in V\) such that \(\langle\theta,gq\rangle\ne0\) for every \(g\in G\), put
\[
f_\theta(gK)=
\begin{cases}0,&\langle\theta,gq\rangle>0,\\1,&\langle\theta,gq\rangle<0.\end{cases}
\tag{3}
\]
It follows at once that this is an admissible reversal-odd coset coloring.

**Theorem 1 (constructive linear-threshold closure).** For either of the canonical type-A or type-B coset systems, every coloring of the form (3) has a complete Coxeter-orbit word with at most one switch. For type A, a suitable Hamilton ordering yields zero switches. For type B, a suitable cube root yields at most one switch for **every** dimension ordering; a root-slide rotation then produces a monochromatic full antipodal geodesic.

*Proof, type A.* Here \(gq_A=e_{g(1)}-e_{g(3)}\), so for the ordered triple \((a,h,c)\),
\[
b_\theta(a,h,c)=\mathbf1_{\{\theta_a-\theta_c<0\}}.
\]
The genericity assumption makes all \(\theta_a\) distinct. Take \(\pi\) listing the vertices in decreasing order of \(\theta\). Each triple \((\pi_j,\pi_{j+1},\pi_{j+2})\) satisfies \(\theta_{\pi_j}>\theta_{\pi_{j+2}}\); all its bits are zero. This is a Hamilton tight path and proves the claim.

*Proof, type B.* The signed-permutation action on \(\mathbb R^n\) is
\[
(a,\sigma)\cdot v=\operatorname{diag}((-1)^{a_1},\ldots,(-1)^{a_n})P_\sigma v.
\]
For an undirected cube edge \(E_i(y)=\{y,y\oplus e_i\}\), equation (2) becomes
\[
R(E_i(y))=\sum_{k\ne i}(-1)^{y_k}e_k,
\qquad
f_\theta(E_i(y))
=\mathbf1_{\{\sum_{k\ne i}(-1)^{y_k}\theta_k<0\}}.
\tag{4}
\]
The expression is independent of the endpoint chosen because its \(i\)-th term is absent. Complementing all cube bits negates the expression, so (4) is antipodally odd.

Choose a root \(x\in\mathbb F_2^n\) with \((-1)^{x_i}\theta_i=|\theta_i|\) for every \(i\); choose any dimension order \(\pi\). Immediately before the \(j\)-th step, dimensions \(\pi_1,\ldots,\pi_{j-1}\) have been flipped once, and all others have their starting signs. Thus the threshold quantity for the \(j\)-th traversed edge is
\[
M_j=\sum_{k>j}|\theta_{\pi_k}|-\sum_{k<j}|\theta_{\pi_k}|.
\tag{5}
\]
For adjacent positions,
\[
M_j-M_{j+1}=|\theta_{\pi_j}|+|\theta_{\pi_{j+1}}|\ge0.
\tag{6}
\]
All \(M_j\) are nonzero by genericity. Therefore the binary sign sequence \(\mathbf1_{\{M_j<0\}}\) is nondecreasing, and so has at most one switch. Every dimension occurs once, so the resulting path is a full antipodal geodesic. Root-slide rotation across its sole switch, when present, produces a monochromatic geodesic by the previously established NORI1 cyclic-rotation lemma. \(\square\)

#### A monotone multi-threshold extension

**Corollary 2 (shared-chamber monotone aggregation).** Let \(f_{\theta^{(1)}},\ldots,f_{\theta^{(r)}}\) be threshold colorings in the same Coxeter model, and let
\[
\Phi:\{0,1\}^{r}\longrightarrow\{0,1\}
\]
be monotone in every argument and self-dual, meaning \(\Phi(\mathbf1-a)=1-\Phi(a)\). Define \(f=\Phi(f_{\theta^{(1)}},\ldots,f_{\theta^{(r)}})\) pointwise on local incidences.

In type A, if the weight vectors \(\theta^{(1)},\ldots,\theta^{(r)}\) induce one common strict ordering of the \(n\) vertices, then \(f\) has a monochromatic Hamilton tight path. In type B, if those weight vectors have a common entrywise sign pattern, then \(f\) has a one-switch full antipodal geodesic, and hence a monochromatic one.

*Proof.* Self-duality gives the required reversal oddness. In type A choose the common decreasing order: every constituent color word is constant zero, so the aggregate word is constant. In type B choose a root aligning the common sign pattern. For any dimension order, formula (6) applies to each constituent weight vector, making each constituent bit sequence nondecreasing. Monotonicity of \(\Phi\) makes their pointwise aggregate nondecreasing. The same root-slide completion applies. \(\square\)

For example, \(\Phi\) may be strict majority on an odd number of threshold colorings. The theorem establishes a common geometric subclass of the two open problems, including nonlinear combinations of compatible halfspaces. It does not establish one-switch existence for arbitrary reversal-odd coset colorings. The main unresolved issue is how to replace a globally consistent threshold vector by a topological obstruction when the coloring lacks a shared linear ordering or common sign pattern.

### Parabolic character obstruction and the first Coxeter one-switch theorem

Let \(G\) be a finite group, \(K\le G\), and \(t\in G\), and let \(f:G\to\mathbb F_2\) be right-\(K\)-invariant. Its orbit word of length \(m\) is \((f(g),f(gt),\ldots,f(gt^{m-1}))\).

**Lemma 1 (the alternating-character obstruction).** Assume \(G=\langle K,t\rangle\) and that there is no homomorphism \(\chi:G\to\mathbb F_2\) with \(\chi(K)=0\) and \(\chi(t)=1\). Then
\[
\boxed{\text{Some }g\in G\text{ satisfies }f(g)=f(gt).}
\tag{1}
\]
In particular, for \(m=3\), some orbit word has at most one switch, regardless of any antipodal constraint on \(f\).

*Proof.* Suppose \(f(gt)=1-f(g)\) for every \(g\). Right-\(K\)-invariance says \(f(gk)=f(g)\) for \(k\in K\). In a word in the generators \(K\cup\{t,t^{-1}\}\), multiplication on the right by \(t\) or \(t^{-1}\) complements \(f\), while multiplication by an element of \(K\) leaves it unchanged. Since \(G=\langle K,t\rangle\), the function \(\chi(g)=f(g)+f(1)\) counts the parity of occurrences of \(t^{\pm1}\) in any such word. It follows that \(\chi(gh)=\chi(g)+\chi(h)\), \(\chi(K)=0\), and \(\chi(t)=1\), a contradiction. Hence (1). A three-letter binary word without two switches has at most one switch; if every three-letter word had two switches, its first two letters would disagree for every \(g\), contradicting (1). \(\square\)

The relevant canonical Coxeter-coset instances are as follows.

**Theorem 2 (common parabolic character vanishing).** In the type-\(A_{n-1}\) instance
\[
G=S_n,\quad K=\{\sigma:\sigma(1)=1,\ \sigma(2)=2,\ \sigma(3)=3\},\quad t=(1\,2\,\cdots\,n),
\tag{2}
\]
the hypotheses of Lemma 1 hold for \(n\ge5\). In the type-\(B_n\) instance
\[
G=\mathbb F_2^n\rtimes S_n,\quad
K=\{(a,\sigma):a\in\{0,e_1\},\ \sigma(1)=1\},\quad
t=(e_1,(1\,2\,\cdots\,n)),
\tag{3}
\]
they hold for \(n\ge3\).

*Proof.* In (2), \(K\) contains the transposition \((4\,5)\); conjugating it by powers of the \(n\)-cycle \(t\) supplies the adjacent transpositions and hence generates \(S_n\). Thus \(G=\langle K,t\rangle\). Every homomorphism \(S_n\to\mathbb F_2\) is a multiple of permutation parity. Because \((4\,5)\in K\), a character vanishing on \(K\) is trivial.

In (3), the projection of \(\langle K,t\rangle\) to \(S_n\) contains the point stabilizer \(S_{\{2,\ldots,n\}}\) and an \(n\)-cycle, hence is all of \(S_n\). The subgroup contains the elementary sign flip \((e_1,\mathrm{id})\in K\); conjugating this flip by lifts of permutations moves it to every dimension. Thus it contains all translations and therefore equals \(\mathbb F_2^n\rtimes S_n\). A homomorphism from \(B_n\) to \(\mathbb F_2\) has the form
\[
\chi(a,\sigma)=A\sum_i a_i+B\,\operatorname{sgn}(\sigma)
\quad(A,B\in\mathbb F_2):
\tag{4}
\]
its restriction to the normal group \(\mathbb F_2^n\) is linear and invariant under permutations, while its restriction to \(S_n\) is a parity character. The subgroup \(K\) contains both \((e_1,\mathrm{id})\) and \((0,(2\,3))\) when \(n\ge3\). Consequently \(\chi(K)=0\) forces \(A=B=0\). \(\square\)

**Corollary 3 (a common proof in the first three-slot ranks).** The classical Coxeter parabolic-coset one-switch conjecture holds for type \(A_4\), namely ordinary reversal-odd boundary 3-tournaments on five vertices, and for type \(B_3\), namely antipodally odd cube-edge colorings of \(Q_3\). In both cases the proposed word has length three and some complete flag has at most one switch.

*Proof.* Apply Lemma 1 and Theorem 2 with \(m=n-2=3\) in (2), or \(m=n=3\) in (3). The coset-word reconstructions identify the resulting words respectively with the triple bits of a Hamilton ordering on all five vertices and the edge bits of a full three-dimension antipodal geodesic. In type \(B_3\), rotating at its possible unique switch yields a monochromatic full geodesic. \(\square\)

The same character argument proves the weaker conclusion (1) at every rank. It rules out a global alternating two-color character on the Coxeter-element arrows while respecting local-incidence descent. For orbit words of length at least four, the presence of one equal neighboring pair does not bound the total number of switches. A full-rank one-switch proof therefore needs a stronger use of the parabolic coset identifications.

#### A rooted tight-path lemma and mixed Hamming products

Let \(V\) have \(m\) vertices. A binary ordered-triple coloring is a function \(b(a,h,c)\in\mathbb F_2\) on pairwise distinct vertices; for the first theorem no reversal condition is imposed. A Hamilton tight path \(v_1,\ldots,v_m\) has triple word
\[
(b(v_1,v_2,v_3),\ldots,b(v_{m-2},v_{m-1},v_m)).
\]
The switch count is the number of unequal consecutive bits.

**Theorem 1 (rooted five-vertex lemma).** For \(3\le m\le5\), every ordered-triple coloring has a Hamilton tight path beginning at any specified vertex and whose triple word switches at most once. For \(m=5\), the theorem requires no reversal oddness.

*Proof.* The cases \(m\le4\) are immediate since the triple word has at most two entries. Let \(m=5\), and fix the first vertex \(a\). Suppose, toward contradiction, that every ordering \(a,p,q,r,s\) of the vertices has at least two switches. Its three-bit triple word must then alternate. In particular,
\[
b(a,p,q)\ne b(p,q,r),\qquad
b(p,q,r)\ne b(q,r,s).                                   \tag{1}
\]
Put \(U=V\setminus\{a\}\). For distinct \(p,q\in U\), let \(r,s\) be the remaining two members of \(U\). Comparing (1) for the orders \((a,p,q,r,s)\) and \((a,p,q,s,r)\), whose first triple is unchanged, shows
\[
b(p,q,r)=b(p,q,s).
\]
Define \(t(p,q)\) to be this common value. The second inequality of (1) becomes
\[
t(p,q)\ne t(q,r)\qquad(p,q,r\in U\ \text{distinct}).      \tag{2}
\]
For three distinct vertices \(p,q,r\in U\), apply (2) successively to \((p,q,r)\), \((q,r,p)\), and \((r,p,q)\). This asks three binary values \(t(p,q),t(q,r),t(r,p)\) to alternate around a cycle of odd length, a contradiction. \(\square\)

We next state a mixed-path model. Write \(H_{m,d}=K_m\square Q_d\), with vertices \((a,z)\), \(a\in V\), \(z\in\mathbb F_2^d\). Assume \(d\ge2\). For each \(a\), color the undirected edges of the \(Q_d\)-fiber by \(c_a\), subject to
\[
c_a(\bar e)=1-c_a(e).                                    \tag{3}
\]
For each \(z\), color the ordered triples in the \(K_m\)-fiber by \(b_z\), subject to
\[
b_z(c,h,a)=1-b_z(a,h,c),\qquad b_{\bar z}=b_z.             \tag{4}
\]
A **complete factor-block path** is a path traversing every binary dimension once and traversing a Hamilton ordering of the \(K_m\)-factor as one contiguous block. Its color word consists of one bit per binary edge and one bit per consecutive triple in the complete-graph block, taken in traversal order. Both the binary directions and the \(K_m\) vertices are used without repetition. Define the proposed **one-factor Hamming conjecture** to assert that every labeling (3)–(4) admits such a complete path whose combined word switches at most once.

At \(m=1\), the conjecture is the one-switch formulation of NORI1. At \(d=0\), omit the cube coloring and use a single reversal-odd \(K_m\)-coloring; the conjecture is the boundary one-switch Hamiltonian problem. These are limiting cases of the same complete-path model. The general conjecture remains open.

**Lemma 2 (two-dimensional cube).** Every antipodally odd edge coloring of \(Q_2\) has a monochromatic antipodal geodesic. Its antipodal translate is monochromatic in the opposite color.

*Proof.* Label the four consecutive edges of the square by \(\alpha,\beta,1-\alpha,1-\beta\), using antipodal oddness. If \(\alpha=\beta\), the first consecutive pair is monochromatic; otherwise \(\beta=1-\alpha\), and the second consecutive pair is monochromatic. Either pair forms an antipodal geodesic. Antipodal translation complements its two colors. \(\square\)

**Theorem 3 (mixed case).** For \(m\le5\) and \(d=2\), the one-factor Hamming conjecture holds. Indeed, the conclusion holds if each \(b_z\) is an arbitrary ordered-triple coloring satisfying only \(b_{\bar z}=b_z\), with no reversal oddness required.

*Proof.* Fix \(a\in V\). By Lemma 2, there is a monochromatic full cube geodesic in its \(Q_2\)-fiber, ending at some \(z\), and its antipodal translate is another such geodesic of the complementary color ending at \(\bar z\). By Theorem 1 (or the immediate shorter-word cases), \(b_z\) has a Hamilton ordering starting at \(a\) whose triple word has at most one switch. Since \(b_{\bar z}=b_z\), the same Hamilton ordering is available in both antipodal complete-graph fibers. If the triple word is nonempty, choose the cube geodesic whose color equals its first triple bit. Concatenate this cube geodesic with the Hamilton ordering in the corresponding terminal complete-graph fiber. There is no switch at their word boundary, and the Hamilton triple word contributes at most one switch. For \(m\le2\), the triple word is empty, so either cube geodesic suffices. The concatenated path uses each binary dimension once and each complete-graph vertex once. \(\square\)

**Corollary 4 (conditional higher-dimensional extension).** Suppose the NORI1 monochromatic full-geodesic conjecture holds for dimension \(d\ge2\). Then the one-factor Hamming conjecture holds on \(K_m\square Q_d\) for every \(m\le5\).

*Proof.* The NORI1 hypothesis supplies the monochromatic full geodesic in the fiber at a fixed \(a\). Its antipodal translate supplies the complementary color and ends at the antipode of the first terminal vertex. Apply the rooted theorem and the common-fiber identity \(b_{\bar z}=b_z\) as in Theorem 3. \(\square\)

The rooted lemma gives a nontrivial mixed existence theorem, while the general conjecture remains an open strengthening of both motivating conjectures. A complete proof for larger \(m\) would require selecting compatible binary and complete-graph portions; Theorem 1 supplies this compatibility for \(m\le5\).

#### Gluing through common admissible starting vertices

For each \(z\in\mathbb F_2^d\), define
\[
S_z=\{a\in V:\ \text{some Hamilton ordering of }V\text{ beginning at }a
\text{ has at most one switch under }b_z\}.
\tag{5}
\]
The identity \(b_{\bar z}=b_z\) gives \(S_{\bar z}=S_z\).

**Theorem 5 (root-intersection gluing).** Suppose the NORI1 monochromatic full-geodesic conclusion holds in dimension \(d\), and the complete-graph fiber colorings satisfy (4). If
\[
\bigcap_{[z]\in\mathbb F_2^d/\langle z\mapsto\bar z\rangle}S_{[z]}\ne\varnothing,
\tag{6}
\]
then a complete factor-block path with at most one switch exists in \(K_m\square Q_d\), regardless of the antipodally odd cube-fiber edge colorings.

*Proof.* Select \(a\) in the intersection. Apply NORI1 in the cube fiber at \(a\) to obtain a monochromatic full cube geodesic \(P\), with color \(\varepsilon\), whose endpoint is \(z\). The antipodal translate \(\bar P\) is monochromatic with color \(1-\varepsilon\) and ends at \(\bar z\). By (6), some Hamilton ordering of \(V\) begins at \(a\) and has a triple word with at most one switch in \(b_z\). Since \(b_{\bar z}=b_z\), the same ordering has the same triple word at \(\bar z\). Choose \(P\) or \(\bar P\) according to whether its color equals the first triple bit; this gives a concatenation with no switch at the block boundary. The complete-graph triple word contributes at most one switch. The resulting path uses every cube dimension once and every complete-graph symbol once, proving the claim. If the triple word is empty, either cube geodesic works. \(\square\)

**Corollary 6 (common-order and majority conditions).** Under the NORI1 hypothesis of Theorem 5, each of the following implies its conclusion:

1. All \(b_z\) admit a single Hamilton ordering whose triple word has at most one switch in every fiber (the color words may differ).
2. Every \(b_z\) is obtained from one reversal-odd tournament \(b\) by complementing all its triple bits, with the complement choice constant on antipodal vertex pairs, and \(b\) has a one-switch Hamilton ordering.
3. If \(d=2\), the two sets \(S_{00}=S_{11}\) and \(S_{01}=S_{10}\) have nonempty intersection; in particular this holds whenever both contain more than \(m/2\) vertices.

*Proof.* In the first two cases the initial vertex of a common favorable ordering belongs to every \(S_z\). In the third, (6) is the pairwise intersection condition, and two subsets of an \(m\)-element set each of size exceeding \(m/2\) must intersect. Apply Theorem 5. \(\square\)

This isolates the remaining difficulty of the mixed conjecture: choosing cube-root and Hamilton starting vertex simultaneously when favorable rooted sets of the complete-graph fibers do not share a vertex. The explicit seven-vertex rooted counterexample in research note \`note_a9777ec5fa11e3d5fe120599\` shows that an individual \(S_z\) can be proper even for reversal-odd boundary tournaments. That example has \(|S_z|=6\) of seven vertices. Therefore, when \(d=2\), pairing that example with any second tournament possessing a one-switch Hamilton path automatically satisfies the intersection condition: reversing a one-switch Hamilton path gives a second favorable starting vertex, so the second rooted set has size at least two, and it must meet the six-element set.


### Full-rank monochromatic paths beyond threshold colorings

We establish constructive closure for reversal-odd boundary colorings obtained from an arbitrary tournament and for two affine classes of unrestricted antipodally odd cube-edge colorings. All paths in the proofs use each original vertex or each cube dimension once.

#### Interleaving tournament Hamilton paths

**Theorem 1 (outer-pair tournament theorem).** Let \(T(a,c)\in\mathbb F_2\) satisfy \(T(c,a)=1-T(a,c)\) for all distinct \(a,c\in V\). Put
\[
b(a,h,c)=T(a,c)
\]
for pairwise distinct triples on \(V\), where \(|V|=n\ge3\). Then the boundary tournament \(b\) has a monochromatic Hamilton tight path, even if \(T\) is cyclic.

*Proof.* Split \(V=A\sqcup B\) with \(|A|=\lceil n/2\rceil\) and \(|B|=\lfloor n/2\rfloor\). Declare \(a\to c\) if \(T(a,c)=0\). Each induced tournament has a directed Hamilton path. For completeness, insert a new vertex \(v\) into a previously constructed directed path: place it first if it beats the first vertex, last if the last beats it, and otherwise at a place between consecutive vertices \(a_i,a_{i+1}\) with \(a_i\to v\to a_{i+1}\). This proves the tournament Hamilton-path lemma inductively. Let the resulting paths be \(a_1\to\cdots\to a_{|A|}\) and \(b_1\to\cdots\to b_{|B|}\), and interleave the two lists as \(a_1,b_1,a_2,b_2,\ldots\). Every consecutive ordered triple has two outer vertices that are consecutive along one of the directed Hamilton paths, so its bit is zero. The interleaving includes every vertex once. \(\square\)

**Corollary 2 (higher windows).** For \(k\ge1,n\ge k+1\), color ordered \((k+1)\)-tuples of distinct vertices by \(T(v_0,v_k)\), with \(T\) an arbitrary tournament. Then there is a Hamilton ordering of all \(n\) vertices whose consecutive \((k+1)\)-window bits are monochromatic.

*Proof.* Split vertices into \(k\) classes occupying positions congruent modulo \(k\) in the desired ordering. Choose a directed Hamilton path on every class, and interleave the paths in their corresponding residue positions. The first and last vertices of each consecutive \((k+1)\)-window are successive vertices of one class's directed path, giving bit zero. \(\square\)

#### Affine cube-edge colorings

An affine coloring of the undirected direction-\(i\) edges has the form
\[
c_i(y)=\alpha_i+\sum_j A_{ij}y_j\pmod2,
\tag{1}
\]
where \(A_{ii}=0\) ensures endpoint invariance and \(A\mathbf1=\mathbf1\) ensures antipodal oddness.

**Theorem 3 (invertible dependency matrix).** If \(A\) is invertible over \(\mathbb F_2\), each dimension order \(\pi\) has precisely two starting roots giving monochromatic full antipodal geodesics: one root gives all zeros, and its antipode gives all ones. There are therefore \(2n!\) monochromatic rooted-and-ordered complete geodesics.

*Proof.* Before traversing direction \(\pi_i\), the path from \(x\) has flipped the preceding dimensions \(\pi_1,\ldots,\pi_{i-1}\). Its edge color is
\[
w_i=\alpha_{\pi_i}+(Ax)_{\pi_i}+
\sum_{k<i}A_{\pi_i,\pi_k}\pmod2.
\tag{2}
\]
The equations \(w_i=0\) for all \(i\) form the nonsingular system \(Ax=\alpha+r(\pi)\), where \(r(\pi)_{\pi_i}=\sum_{k<i}A_{\pi_i,\pi_k}\). It has one root solution. Since \(A\mathbf1=\mathbf1\), adding \(\mathbf1\) to the root complements every path bit, giving the unique all-one root. Every order uses every direction once, and there are \(n!\) orders. \(\square\)

**Theorem 4 (one dependency per dimension, allowing singular matrices).** Let \(p:[n]\to[n]\) satisfy \(p(i)\ne i\) and choose arbitrary bits \(\alpha_i\). Every coloring
\[
c_i(y)=y_{p(i)}+\alpha_i\pmod2
\tag{3}
\]
has a monochromatic full antipodal geodesic, whether or not \(p\) is injective.

*Proof.* For a root \(x\), the direction-\(i\) step of a full dimension ordering has bit zero if and only if
\[
\mathbf1_{\{p(i)\ \text{precedes }i\}}=x_{p(i)}+\alpha_i.
\tag{4}
\]
Give each edge \(\{p(i),i\}\) of a multigraph the direction \(p(i)\to i\) when the right side is one, and \(i\to p(i)\) otherwise. A topological ordering of this directed multigraph satisfies all equations (4).

Because each vertex chooses one parent \(p(i)\), the undirected dependency multigraph is a pseudoforest: every component consists of one cycle (including a pair of parallel edges when a cycle has two vertices) with attached trees. Fix an arbitrary linear ordering of the vertices on each cycle. Every cycle vertex \(v\) is the parent of one other cycle vertex \(i\), so the choice of \(x_v\) controls the direction of its corresponding cycle edge. Set \(x_v\) so each cycle edge points forward in the chosen linear ordering. Choose the remaining root bits arbitrarily. The resulting directed multigraph has no directed cycle: the edges in its only undirected cycle are aligned with an acyclic order, while the attached trees contain no cycles. Choose a topological ordering of its vertices and use it as the cube dimension order. Equation (4) makes every traversed cube edge color zero. Antipodal translation gives a full geodesic of color one. \(\square\)

These results prove the monochromatic full-path conclusion for nonlinear outer-pair tournament colorings and for two affine cube families. They supply additional tests for a proposed common selection theorem on locally consistent Coxeter coset words; unrestricted one-switch existence remains open.

#### Cokernel root-slide transport and affine corank-two closure

Retain the affine antipodally odd cube-edge coloring
\[
f_i(x)=\alpha_i+(Ax)_i,\qquad A_{ii}=0,\quad A\mathbf1=\mathbf1
\]
over \(\mathbb F_2\). The matrix need not be symmetric or have an acyclic dependency graph. Let \(V=\mathbb F_2^n/\operatorname{im}A\), \(k=\dim V=n-\operatorname{rank}A\), and \(v_i=[e_i]\in V\). The \(v_i\) span \(V\), and
\[
\sum_i v_i=[\mathbf1]=[A\mathbf1]=0. \tag{CR1}
\]
For a permutation \(\pi=(\pi_1,\ldots,\pi_n)\) put
\[
(r_\pi)_{\pi_t}=\sum_{s<t}A_{\pi_t,\pi_s},
\qquad \sigma(\pi)=[\alpha+r_\pi]\in V. \tag{CR2}
\]

**Lemma 5 (monochromatic solvability and cyclic transport).** A full all-zero geodesic with dimension order \(\pi\) exists if and only if \(\sigma(\pi)=0\). Every successful order admits \(2^k\) all-zero starting roots; their antipodes give \(2^k\) all-one starting roots. For cyclic rotation \(\rho\pi=(\pi_2,\ldots,\pi_n,\pi_1)\),
\[
\boxed{\sigma(\rho\pi)=\sigma(\pi)+v_{\pi_1}.} \tag{CR3}
\]
Consequently the obstructions of the \(n\) cyclic rotations are
\[
\sigma(\pi)+\sum_{s=1}^t v_{\pi_s},\qquad 0\le t<n. \tag{CR4}
\]

*Proof.* The color on the \(t\)-th step from starting root \(x\) is \(\alpha_{\pi_t}+(Ax)_{\pi_t}+(r_\pi)_{\pi_t}\). Thus all colors vanish precisely when \(Ax=\alpha+r_\pi\), solvable if and only if its quotient class vanishes. The solution fiber has cardinality \(|\ker A|=2^k\). Since \(A\mathbf1=\mathbf1\), translating the root antipodally changes every color from zero to one.

Let \(i=\pi_1\). Under cyclic rotation, every other predecessor sum changes by \(A_{ji}\), while the predecessor sum in row \(i\) changes from zero to \(\sum_{j\ne i}A_{ij}=1\). Therefore \(r_{\rho\pi}+r_\pi=Ae_i+e_i\). Project into \(V\) to obtain (CR3) and iterate. \(\square\)

**Corollary 6 (quotient prefix-cover criterion).** If some order satisfies
\[
\left\{\sum_{s=1}^t v_{\pi_s}:0\le t<n\right\}=V, \tag{CR5}
\]
then for every constant vector \(\alpha\), one of its cyclic rotations supplies a monochromatic full antipodal geodesic.

*Proof.* Equation (CR4) translates all of \(V\) and therefore contains zero. Apply Lemma 5. \(\square\)

**Theorem 7 (all-dimensional affine corank-two closure).** Every affine antipodally odd cube-edge coloring as above satisfies
\[
\boxed{\operatorname{rank}_{\mathbb F_2}A\ge n-2
\ \Longrightarrow\
\text{a monochromatic dimension-simple full antipodal geodesic exists}.} \tag{CR6}
\]

*Proof.* Put \(k=\dim V\le2\). For \(k=0\), every \(\sigma(\pi)\) vanishes. For \(k=1\), some \(v_i\ne0\), because the classes span \(V\). Beginning an order with \(i\) makes the two prefix sums \(0,v_i\) exhaust \(V\), proving the result by Corollary 6.

Suppose \(k=2\). If two distinct directions \(i,\ell\) have equal nonzero classes \(v_i=v_\ell=a\), choose \(j\) with \(v_j=b\) independent of \(a\) and begin an ordering with \(i,j,\ell\). The first four prefix sums \(0,a,a+b,b\) exhaust \(V\), again giving (CR5).

It remains to consider the case in which every nonzero quotient class occurs at most once among the \(v_i\). As these classes span \(V\) and sum to zero by (CR1), three distinguished directions \(i,j,\ell\) have
\[
v_i=a,\qquad v_j=b,\qquad v_\ell=a+b,
\]
where \(a,b\) are independent, and all remaining \(v_h=0\).

Assume contrariwise that every dimension ordering \(\pi\) has nonzero syndrome \(\sigma(\pi)\). Choose an order \(\pi=(i,j,\ldots)\). Its first three rotation syndromes are \(\sigma(\pi),\,\sigma(\pi)+a,\,\sigma(\pi)+a+b\). All must be nonzero. As \(V=\{0,a,b,a+b\}\), this forces \(\sigma(\pi)=b\). Swapping the first two directions gives \(\pi'=(j,i,\ldots)\), for which the same reasoning forces \(\sigma(\pi')=a\).

An adjacent swap changes only the two predecessor entries involved:
\[
r_{\pi'}+r_\pi=A_{ij}e_i+A_{ji}e_j,
\]
hence
\[
a+b=\sigma(\pi')+\sigma(\pi)=A_{ij}a+A_{ji}b.
\]
Independence yields \(A_{ij}=A_{ji}=1\). Since any two of the three distinct nonzero vectors of \(V\) are independent, the same argument applied to the other two pairs forces all six off-diagonal entries in the distinguished \(3\times3\) submatrix to equal one. In particular, \(A_{ji}=A_{\ell i}=1\).

But the \(i\)-th column lies in \(\operatorname{im}A\), so
\[
0=[Ae_i]=\sum_h A_{hi}v_h=v_j+v_\ell=b+(a+b)=a,
\]
a contradiction. Here \(A_{ii}=0\), and every unlisted \(v_h\) vanishes. Therefore some \(\sigma(\pi)=0\), and Lemma 5 supplies a monochromatic full antipodal geodesic. \(\square\)

**Proof-closure perspective.** The quotient root-slide identity (CR3) translates monochromatic existence into locating the zero syndrome in a permutation gallery. The prefix-cover criterion gives an order-independent sufficient condition, while the exceptional corank-two proof extracts additional compatibility from adjacent-order exchanges. In higher corank the identity
\[
\sigma(\pi')+\sigma(\pi)=A_{ij}v_i+A_{ji}v_j
\]
for exchanging adjacent directions is a candidate global invariant. Establishing that these relations force zero for arbitrary affine \(A\) with \(A\mathbf1=\mathbf1\) would close the antipodally odd affine class, which is strictly narrower than unrestricted NORI1. The present theorem makes no assertion about arbitrary nonlinear edge colorings or arbitrary reversal-odd boundary 3-tournaments.


#### Weighted-inversion curvature normal form

Retain \(V,v_i,r_\pi,\sigma(\pi)\) from the preceding results. For distinct direction indices \(i,j\), define the symmetric quotient-valued pair weight
\[
K_{ij}:=A_{ij}v_i+A_{ji}v_j=K_{ji}\in V. \tag{CR7}
\]
For permutations \(\pi,\tau\), let \(I(\pi,\tau)\) comprise the unordered direction pairs whose relative order differs between \(\pi\) and \(\tau\).

**Proposition 8 (inversion formula and star-curvature identity).** For every antipodally odd affine cube-edge coloring,
\[
\boxed{\sigma(\pi)+\sigma(\tau)
=\sum_{\{i,j\}\in I(\pi,\tau)}K_{ij}.} \tag{CR8}
\]
Moreover,
\[
\boxed{\sum_{j\ne i}K_{ij}=v_i\qquad(i\in[n]).} \tag{CR9}
\]
Consequently the affine span of the attainable syndrome set \(\{\sigma(\pi):\pi\in\mathfrak S_n\}\) is the whole quotient \(V\), for *every* matrix rank. The set contains at least \(k+1\) values, where \(k=\dim V\), and no proper affine hyperplane contains it.

*Proof.* The \(i\)-th entry of \(r_\pi+r_\tau\) is the sum of \(A_{ij}\) over the indices \(j\) whose relative precedence changes. Hence
\[
r_\pi+r_\tau
=\sum_{\{i,j\}\in I(\pi,\tau)}
(A_{ij}e_i+A_{ji}e_j).
\]
Projecting to \(V\) gives (CR8). Summing the pair weights incident to \(i\) gives
\[
\sum_{j\ne i}K_{ij}
=\Bigl(\sum_{j\ne i}A_{ij}\Bigr)v_i
 +\sum_{j\ne i}A_{ji}v_j
=v_i+[Ae_i]=v_i,
\]
using \(A_{ii}=0\), \(A\mathbf1=\mathbf1\), and \([Ae_i]=0\). This proves (CR9).

Every pair \(i,j\) can be made adjacent in some permutation and then interchanged. By (CR8), the two resulting syndrome values differ by \(K_{ij}\). Thus the linear span of all differences of attained values contains each \(K_{ij}\), hence by (CR9) every \(v_i\). The \(v_i\) span \(V\), so the attained values affinely span \(V\). A spanning set in a \(k\)-dimensional affine space has at least \(k+1\) elements. \(\square\)

**Reduction to a global saturation lemma (open).** For any reference order \(\pi_0\), the statement that *every* choice of offset \(\alpha\) has a monochromatic full geodesic is equivalent to the weighted inversion map
\[
\pi\longmapsto\sum_{\{i,j\}\in I(\pi,\pi_0)}K_{ij} \tag{CR10}
\]
being surjective onto \(V\). Indeed (CR8) expresses the attainable syndromes as a translate of this image, and varying \(\alpha\) varies the translating coset arbitrarily. Proposition 8 proves that the image affinely spans \(V\); Theorem 7 proves surjectivity when \(\dim V\le2\). General surjectivity remains conjectural.

The needed further ingredient is therefore a global saturation principle for the permutation inversion weights, using both their pairwise form (CR7) and their star relations (CR9). This formulation preserves full dimension-simple paths and avoids reasoning through successively larger cube orders.


#### Quotient induction and the one-hole obstruction

The preceding affine results remain valid if the quotient \(V\) is replaced by *any* vector space equipped with a surjective linear map \(p:\mathbb F_2^n\to V\) satisfying \(pA=0\). In this generality let \(v_i=p(e_i)\) and \(\sigma_p(\pi)=p(\alpha+r_\pi)\). The cyclic-rotation and adjacent-interchange formulas, the star-curvature identity, and the corank-at-most-two surjectivity proof require only
\[
A_{ii}=0,\quad A\mathbf1=\mathbf1,\quad pA=0,\quad
\operatorname{span}\{v_i\}=V.
\]
In particular, any further linear quotient of \(V\) is again admissible.

**Proposition 9 (missing-syndrome descent).** Let \(S_p=\{\sigma_p(\pi):\pi\in\mathfrak S_n\}\subseteq V\). If \(S_p\) omits two distinct elements \(a,b\), then the induced syndrome set in the quotient \(V/\langle a+b\rangle\) also omits a point.

*Proof.* The two-element coset \(a+\langle a+b\rangle=\{a,b\}\) is disjoint from \(S_p\). Its image is therefore absent from the projection of \(S_p\). The quotient map composed with \(p\) still annihilates \(A\) and is surjective, so it gives admissible lower-dimensional data. \(\square\)

**Corollary 10 (one-hole reduction for universal affine closure).** Suppose that syndrome surjectivity is established for all admissible quotients of dimension strictly less than \(k\), where \(k\ge3\). For any admissible \(k\)-dimensional quotient, either its syndrome image is all of \(V\), or it is \(V\setminus\{a\}\) for a single element \(a\). In particular any minimal-dimensional failure of universal surjectivity has precisely one missing syndrome.

*Proof.* If two values were missing, Proposition 9 would exhibit a nonsurjective quotient of dimension \(k-1\), contrary to the hypothesis. \(\square\)

**Proof-closure target.** A general theorem excluding the *punctured full image* \(V\setminus\{a\}\), among admissible weighted-inversion maps, would imply universal affine syndrome surjectivity by induction from the corank-two theorem. The extra fact that every nonzero quotient syndrome would have to be attained in a minimal obstruction is available for exploiting rank-two exchanges, cyclic root slides, or parity counts. This is a conditional reduction; it does not establish the exclusion itself.

The reduction uses affine invariance and full direction permutations throughout. It makes no claim that nonlinear cube-edge colorings, or boundary-tournament colorings, admit analogous linear quotient syndromes.


#### Cyclic Fourier discrepancy and high-distance affine closure

Continue with an antipodally odd affine coloring \(f_i(x)=\alpha_i+(Ax)_i\), where \(A_{ii}=0\) and \(A\mathbf1=\mathbf1\). Write \(V=\mathbb F_2^n/\operatorname{im}A\), \(k=\dim V\), and \(\sigma(\pi)=[\alpha+r_\pi]\). Let \(\mu\) be the probability distribution of \(\sigma(\pi)\) when \(\pi\) is uniformly sampled from all \(n!\) direction orders.

The dual space of \(V\) is \(W=\ker A^{\mathsf T}\). For \(z\in W\), let \(\widehat\mu(z)=\mathbb E_\pi(-1)^{z\cdot\sigma(\pi)}\), and write \(w(z)=|\operatorname{supp}z|\). Every \(z\in W\) has even weight since
\[
z\cdot\mathbf1=z^{\mathsf T}A\mathbf1=0. \tag{FD1}
\]

**Theorem 11 (cyclic Fourier discrepancy).** For every nonzero \(z\in W\), with positive even weight \(w=w(z)\),
\[
\boxed{|\widehat\mu(z)|
\le \sqrt{\frac{n-w}{n(w+1)}}.} \tag{FD2}
\]
The bound is uniform in the offset \(\alpha\) and the matrix entries of \(A\), subject to the stated antipodal and undirected-edge hypotheses.

*Proof.* Let \(\rho\) cyclically rotate a direction order. The root-slide identity (CR3) gives, for \(0\le t<n\),
\[
(-1)^{z\cdot\sigma(\rho^t\pi)}
=(-1)^{z\cdot\sigma(\pi)}
 (-1)^{\sum_{s=1}^t z_{\pi_s}}.
\]
Define \(S_z(\pi)=\sum_{t=0}^{n-1}(-1)^{\sum_{s=1}^t z_{\pi_s}}\). Uniform permutation sampling is invariant under each cyclic rotation, so
\[
|\widehat\mu(z)|
\le\frac1n\mathbb E_\pi |S_z(\pi)|
\le\frac1n\sqrt{\mathbb E_\pi S_z(\pi)^2}. \tag{FD3}
\]

We compute its second moment. Read the cyclic sequence \(z_{\pi_1},\ldots,z_{\pi_n}\), which has precisely \(w=2h\) entries equal to one. Its cyclic gaps between successive ones have positive lengths
\(\ell_1,\ldots,\ell_{2h}\) summing to \(n\). Since the number of ones is even, rotating the sequence changes \(S_z\) only by a global sign. Choosing one of the marked positions as a distinguished cyclic origin leaves \(S_z^2\) unchanged and makes the gap vector uniform among positive compositions of \(n\) into \(2h\) parts.

Put \(N=n-2h\), \(a_j=\ell_j-1\), and \(U=a_1+a_3+\cdots+a_{2h-1}\). Then \(a_j\ge0\), \(\sum a_j=N\), and the alternating-sign sum equals \(S_z=\pm(2U-N)\). Stars-and-bars gives
\[
\Pr(U=u)=
\frac{\binom{u+h-1}{h-1}
      \binom{N-u+h-1}{h-1}}
     {\binom{N+2h-1}{2h-1}}.
\]
This beta-binomial distribution has \(\mathbb E U=N/2\) and
\[
\operatorname{Var}(U)=\frac{N(N+2h)}{4(2h+1)}
=\frac{n(n-w)}{4(w+1)}.
\]
Thus
\[
\mathbb E_\pi S_z(\pi)^2
=4\operatorname{Var}(U)
=\frac{n(n-w)}{w+1}.
\]
Substitution into (FD3) proves (FD2). \(\square\)

**Corollary 12 (uniform favorable-order and path counts).** Put
\[
D(W)=\sum_{z\in W\setminus\{0\}}
 \sqrt{\frac{n-w(z)}{n(w(z)+1)}}. \tag{FD4}
\]
For every syndrome target \(v\in V\),
\[
\boxed{
\mu(v)\ge2^{-k}\bigl(1-D(W)\bigr).
} \tag{FD5}
\]
If \(D(W)<1\), every syndrome occurs, and therefore every affine offset \(\alpha\) has a monochromatic full antipodal geodesic. There are at least
\[
\boxed{n!\bigl(1-D(W)\bigr)} \tag{FD6}
\]
rooted, direction-ordered all-zero full geodesics, counted with their starting roots. The same lower bound holds for all-one rooted full geodesics.

*Proof.* Fourier inversion on \(V\) gives
\[
\mu(v)=2^{-k}\left(
1+\sum_{z\in W\setminus\{0\}}
 (-1)^{z\cdot v}\widehat\mu(z)\right).
\]
Use Theorem 11 term by term. For a successful order \(\pi\), the linear system \(Ax=\alpha+r_\pi\) has \(2^k\) solutions, all giving all-zero full paths. Hence the total all-zero rooted-path count is \(2^k n!\mu(0)\), bounded below by (FD6). Antipodal translation exchanges the zero and one colors. \(\square\)

**Corollary 13 (dual-distance sufficient condition).** Let \(d=\min_{z\in W\setminus\{0\}}w(z)\), with \(k\ge1\). If
\[
\boxed{(2^k-1)\sqrt{\frac{n-d}{n(d+1)}}<1,} \tag{FD7}
\]
then the affine coloring has a monochromatic full antipodal geodesic. In particular \(d\ge(2^k-1)^2\) suffices.

*Proof.* The function \(w\mapsto(n-w)/(n(w+1))\) is decreasing. Consequently (FD4) is bounded by the left side of (FD7). For the final sufficient inequality, \((n-d)/n<1\) and \(d+1>(2^k-1)^2\) establish the strict inequality. Apply Corollary 12. \(\square\)

**Closure significance and limitation.** The bound controls the distribution of *full dimension-order monochromatic solvability* by the weight distribution of the left-kernel code, rather than the cube's dimension or a feedback-graph size. It is especially effective when the cokernel is small and all nonzero codewords have large Hamming support. In contrast, short even kernel relations permit large Fourier biases, and the estimate alone cannot exclude a one-hole obstruction for arbitrary matrices. The general affine saturation lemma remains open.


#### An abstract one-hole obstruction to star identities alone

The full-affine spanning statement (CR9) leaves open a potential surjectivity argument using only symmetric pair weights and their star sums. Such an argument is impossible without further structural hypotheses.

**Proposition 14 (star-compliant, one-hole weighted inversion map).** Take \(V=\mathbb F_2^3\), four ordered labels \(0,1,2,3\), and symmetric pair weights encoded as binary integers
\[
(K_{01},K_{02},K_{03},K_{12},K_{13},K_{23})
=(0,1,2,3,4,4). \tag{OH1}
\]
Define \(v_i=\sum_{j\ne i}K_{ij}\). Then
\[
(v_0,v_1,v_2,v_3)=(3,7,6,2), \qquad
\operatorname{span}\{v_0,v_1,v_2,v_3\}=V, \tag{OH2}
\]
and \(\sum_i v_i=0\), but the weighted inversion sums over all 24 permutations take precisely seven values:
\[
\boxed{
\left\{\sum_{\substack{i<j\\\pi^{-1}(i)>\pi^{-1}(j)}}K_{ij}:
\pi\in\mathfrak S_4\right\}
=V\setminus\{5\}.} \tag{OH3}
\]
Thus star-curvature constraints and affine spanning are insufficient to eliminate the one-hole obstruction.

*Proof.* The star sums are computed directly from (OH1); for instance \(v_0=0+1+2=3\) and \(v_1=0+3+4=7\). The three values \(3,7,6\) are linearly independent over \(\mathbb F_2\), so the span is \(V\). To verify (OH3), the multiplicities of inversion sums \(0,1,\ldots,7\), in increasing binary-integer order, are
\[
\boxed{(6,2,4,4,4,0,2,2),} \tag{OH4}
\]
obtained by grouping the 24 permutations according to their inversion sets. These multiplicities sum to 24 and show that 5 alone is absent. \(\square\)

**Important limitation of the example.** The weights (OH1) are not of the matrix-compatible form \(K_{ij}=A_{ij}v_i+A_{ji}v_j\) for a zero-diagonal row-odd matrix with \(v_i=[e_i]\) in its cokernel. Indeed \(K_{13}=4\) is not in
\[
\operatorname{span}\{v_1,v_3\}
=\operatorname{span}\{7,2\}=\{0,7,2,5\}.
\]
Thus this proposition does not contradict affine corank-two closure or the proposed general affine theorem. It identifies the pairwise support identity, together with \(pA=0\) and \(A\mathbf1=\mathbf1\), as indispensable input for any general one-hole exclusion proof. The example is a finite refutation of an auxiliary overstrong lemma, not a counterexample to NORI1.


#### Nonlinear triangular Boolean profiles

#### Nonlinear triangular Boolean profiles force monochromatic full cube geodesics

Let \(n\ge2\) and \(c=(c_i)_{i=1}^n\) be the binary direction rules of an undirected-edge coloring of \(Q_n\): \(c_i(x+e_i)=c_i(x)\). Antipodal oddness, when required, is \(c_i(x+\mathbf1)=1+c_i(x)\), with addition in \(\mathbb F_2\). For each permutation \(\pi\), define the full-geodesic color profile \(\Phi_\pi(x)\in\mathbb F_2^n\) with its entries indexed by direction labels, so
\[
[\Phi_\pi(x)]_i=c_i(x+q_i(\pi)),\qquad
q_i(\pi)=\sum_{\pi^{-1}(j)<\pi^{-1}(i)}e_j.
\tag{TN1}
\]

**Theorem 1 (triangular nonlinear profile bijection).** Suppose there is an invertible binary matrix \(L\in\mathrm{GL}_n(\mathbb F_2)\) and Boolean functions \(h_i:\mathbb F_2^{i-1}\to\mathbb F_2\) such that, writing \(y=Lx\),
\[
\boxed{c_i(x)=y_i+h_i(y_1,\ldots,y_{i-1})\qquad (1\le i\le n).}
\tag{TN2}
\]
Then for *every* direction permutation \(\pi\), the map \(\Phi_\pi:Q_n\to Q_n\) is bijective. In particular, for every prescribed color word \(w\in Q_n\), each order \(\pi\) admits one and only one initial vertex with profile \(w\). If the coloring is antipodally odd, every order admits a monochromatic red and a monochromatic blue full antipodal geodesic, on antipodal initial vertices. There are \(n!\) oriented red full geodesics and \(n!/2\) unoriented red full geodesics.

*Proof.* Write \(y=Lx\), and put \(v_i=Lq_i(\pi)\), a vector depending on the chosen order but not on \(x\). Then
\[
[\Phi_\pi(x)]_i=y_i+(v_i)_i+
h_i(y_1+(v_i)_1,\ldots,y_{i-1}+(v_i)_{i-1}).
\tag{TN3}
\]
For prescribed profile \(w\), solve (TN3) in the order \(i=1,\ldots,n\): the first equation determines \(y_1\), the second determines \(y_2\), and so on. Each equation contains its newly introduced unknown \(y_i\) with coefficient one and depends otherwise only on already determined bits. Thus there is one solution \(y\), and \(L^{-1}y\) gives one initial vertex \(x\). This works for every \(\pi,w\). Antipodal oddness implies \(\Phi_\pi(x+\mathbf1)=\Phi_\pi(x)+\mathbf1\), so the red and blue roots are antipodal. For each of \(n!\) direction orders there is one oriented red geodesic; reversing its direction gives the opposite orientation of the same red path, proving the unoriented count. \(\square\)

**Equivalent derivative certificate.** Define \(f(y)=c(L^{-1}y)\) and Boolean differences \(\partial_j f_i(y)=f_i(y)+f_i(y+e_j)\). Condition (TN2) is equivalent to
\[
\boxed{\partial_i f_i\equiv1,\qquad \partial_j f_i\equiv0\quad(j>i).}
\tag{TN4}
\]
The first condition integrates to \(f_i=y_i+h_i(y_{<i})\), and the second makes \(h_i\) independent of every later variable. Therefore (TN4) is an order-independent, verifiable Boolean-Jacobian certificate for one-root solvability of every complete color profile.

**Example with unbounded nonlinear directions.** Index directions and vertex bits by \(0,\ldots,n-1\), and take \(n\ge5\). Define the antipodally even, degree-two Boolean function
\[
H(x_1,x_2,x_3)=(x_1+x_2)(x_2+x_3),
\]
and let
\[
\boxed{c_i(x)=x_{(i+1)\bmod n}+[i\ge4]H(x_1,x_2,x_3)\quad(0\le i<n).}
\tag{TN5}
\]
Every rule ignores its own vertex bit: for \(i\le3\) the nonlinear term is absent, and for \(i\ge4\) the term depends only on \(x_1,x_2,x_3\). The cyclic reader index \((i+1)\bmod n\) never equals \(i\). Since \(H(x+\mathbf1)=H(x)\), every rule changes color under antipodality. Thus the coloring is legal and antipodally odd.

Let \(L\) be the cyclic permutation matrix \(y_i=x_{(i+1)\bmod n}\). For \(i\le3\) we have \(c_i=y_i\); for \(i\ge4\),
\[
c_i=y_i+(y_0+y_1)(y_1+y_2),
\]
which is triangular in the \(y\)-variables. Therefore Theorem 1 applies. There are \(n-4\) nonlinear rules, all of algebraic degree two, for arbitrarily large \(n\). Independent enumeration for \(n=5\) and \(n=7\) verified edge consistency, antipodal oddness, and bijectivity of the color-profile map for all \(5!=120\) and \(7!=5040\) direction orders, respectively.

*Placement and scope.* The invertible affine dependency-matrix theorem is the case \(h_i\) affine, after a suitable invertible linear transformation. The present theorem permits arbitrary nonlinear triangular transformations, with unboundedly many nonlinear direction rules. It forces NORI1 on this family by substitution, without using root-density bounds or cooperation between paths. It does not imply that every legal odd coloring possesses a triangular presentation.

##### Order-wise bijectivity beyond first-level Fourier rank

**Corollary (profile bijections with singular linear Fourier matrix).** For every \(n\ge6\), define
\[
c_i(x)=x_{i+1}\quad(0\le i<n-1),\qquad
c_{n-1}(x)=x_0+H(x_1,x_2,x_3,x_4),
\tag{TN6}
\]
where
\[
H=\operatorname{Maj}(x_1+x_2,\ x_1+x_3,\ x_1+x_4)
\]
and \(\operatorname{Maj}(a,b,d)=ab+ad+bd\) is the three-input majority function over \(\mathbb F_2\). Because each difference \(x_1+x_j\) is invariant under complementing every vertex bit, \(H\) is antipodally even. Every rule ignores its own direction bit, so (TN6) is a legal antipodally odd coloring. With \(L\) the cyclic permutation \(y_i=x_{(i+1)\bmod n}\), the only nonlinear term is in the final output, and it depends on \(y_0,y_1,y_2,y_3\); Theorem 1 therefore makes \(\Phi_\pi\) bijective for every \(\pi\).

Let \(s_i(x)=(-1)^{c_i(x)}\), and let \(M_{ij}=\mathbb E_x s_i(x)(-1)^{x_j}\) be the matrix of first-level Walsh coefficients. The three differences \((x_1+x_2,x_1+x_3,x_1+x_4)\) are uniformly distributed on \(\mathbb F_2^3\), so their majority is a fair bit and \(\mathbb E(-1)^H=0\). Also \(H\) ignores \(x_0\). Consequently
\[
M_{n-1,0}=\mathbb E(-1)^H=0,\qquad
M_{n-1,j}=\mathbb E(-1)^{x_0+H+x_j}=0
\quad(j\ne0),
\tag{TN7}
\]
as the independent fair bit \(x_0\) forces cancellation. Thus the full \(n\)-entry last row of the first-level Fourier matrix is zero, even though all \(n!\) geodesic profile maps are bijections. For \(n=6\), enumeration verified the Walsh cancellation and all 720 color-profile bijections.

This example shows that full-color-profile solvability can be an entirely nonlinear triangular phenomenon not visible to first-order Walsh rank. It is not a counterexample to NORI1.

#### Acyclic-orientation model for affine geodesic profiles

#### Acyclic-orientation model for affine geodesic profiles

Let \(c_i(x)=\alpha_i+(Ax)_i\) be an affine binary edge coloring of \(Q_n\), with \(A\in M_n(\mathbb F_2)\), \(A_{ii}=0\), \(A\mathbf1=\mathbf1\). Thus the coloring is invariant on each undirected direction edge and is antipodally odd. Put
\[
V=\mathbb F_2^n/\operatorname{im}A,\qquad v_i=[e_i]\in V,\qquad
\gamma_{ij}=A_{ij}v_i+A_{ji}v_j\in V\quad(i\ne j).
\tag{FO1}
\]
Let \(H_A\) be the undirected graph on \([n]\) with edges \(ij\) for which \(\gamma_{ij}\ne0\). For a direction order \(\pi\), define \((r_\pi)_i=\sum_{j\text{ before }i}A_{ij}\), so that the direction-indexed color profile from root \(x\) is
\[
w(x,\pi)=\alpha+Ax+r_\pi.
\tag{FO2}
\]

**Theorem 1 (acyclic-orientation cokernel model).** Fix a reference total order \(\pi_0\) and orient every edge of \(H_A\) from earlier to later under \(\pi_0\). If \(O\) is any acyclic orientation of \(H_A\), let \(I(O)\) be its set of edges oriented opposite to this reference orientation. Then the attainable color-profile set is
\[
\boxed{\mathcal W(c)=
\bigcup_{O\text{ acyclic}}
\left(\alpha+r_{\pi_0}
+\sum_{ij\in I(O)}(A_{ij}e_i+A_{ji}e_j)
+\operatorname{im}A\right).}
\tag{FO3}
\]
In particular its number of profiles depends on \(A\), not on the affine constant \(\alpha\). The unrestricted affine profile-surjectivity question is equivalent to whether the images in \(V\) of the inversion-label sums of acyclic orientations of \(H_A\) exhaust \(V\).

*Proof.* Moving adjacent directions \(i,j\) past one another changes \(r_\pi\) by \(A_{ij}e_i+A_{ji}e_j\). For arbitrary orders \(\pi,\pi_0\), one can sort \(\pi\) into \(\pi_0\) by swapping each reversed pair once (a reduced word for their relative permutation). Thus \([r_\pi]+[r_{\pi_0}]\) is the sum of \(\gamma_{ij}\) over the pairs whose relative order differs. The pairs outside \(H_A\) contribute zero modulo \(\operatorname{im}A\). Restricting a total order to edges of \(H_A\) always gives an acyclic orientation; conversely every acyclic orientation of a finite graph has a total-order extension. Therefore the image of all \(r_\pi\) modulo \(\operatorname{im}A\) is precisely the finite set in (FO3). Equation (FO2) gives the asserted union of cosets. \(\square\)

**Lemma 2 (automatic span of all exchange labels).** Without any acyclicity hypothesis,
\[
\boxed{\sum_{j\ne i}\gamma_{ij}=v_i,\qquad
\operatorname{span}_{\mathbb F_2}\{\gamma_{ij}:ij\in E(H_A)\}=V.}
\tag{FO4}
\]
*Proof.* Since \(\sum_{j\ne i}A_{ij}=1\) and \(\sum_{j\ne i}A_{ji}v_j=[Ae_i]=0\), the first identity follows. The vectors \(v_i\) span \(V\), hence so do the exchange labels. \(\square\)

**Theorem 3 (forest criterion and polynomial-time construction).** If \(H_A\) is a forest, then
\[
\boxed{\mathcal W(c)=\mathbb F_2^n}
\tag{FO5}
\]
for every affine constant \(\alpha\). Given any desired profile \(w\), a full antipodal geodesic with profile \(w\) can be constructed by Gaussian elimination and topological sorting in polynomial time.

*Proof.* A forest has no directed cycles under any orientation, so every subset \(T\subseteq E(H_A)\) can be realized as the reversed-edge set \(I(O)\) of some acyclic orientation \(O\). Thus (FO3) realizes every subset sum of \(\gamma_{ij}\). By (FO4) those sums cover \(V\), giving (FO5). Constructively, solve in \(V\) for coefficients \(t_{ij}\) such that \(\sum t_{ij}\gamma_{ij}=[w+\alpha+r_{\pi_0}]\). Reverse the reference orientation on the selected forest edges and topologically sort the resulting directed forest, obtaining an order \(\pi\). Equations (FO3)-(FO4) then ensure \(w+\alpha+r_\pi\in\operatorname{im}A\), so solve \(Ax=w+\alpha+r_\pi\) by Gaussian elimination. Equation (FO2) proves that the resulting geodesic has profile \(w\). \(\square\)

**Corollary 4 (odd-degree forest dependency graphs).** If \(T\) is any forest in which every vertex has odd degree, let \(A\) be its binary adjacency matrix. The legal antipodally odd coloring
\[
c_i(x)=\alpha_i+\sum_{j:\{i,j\}\in E(T)}x_j
\]
has complete direction-indexed color-profile support, for every \(\alpha\). Indeed \(A_{ii}=0\), \(A\mathbf1=\mathbf1\), and \(\gamma_{ij}=0\) outside \(E(T)\); hence \(H_A\subseteq T\).

**Corollary 5 (simultaneously unbounded cokernel and nonunary dependence).** For any odd \(h\ge3\), let \(T_h\) have vertices consisting of a hub \(o\), branch vertices \(b_1,\ldots,b_h\), and two private leaves \(a_j,d_j\) for each branch. Its edges are \(ob_j,b_ja_j,b_jd_j\). Then \(n=3h+1\), every vertex has odd degree, the binary adjacency matrix \(A_h\) has rank \(2h\), and its cokernel has dimension \(h+1\). The hub and all \(h\) branch vertices have at least three readers, so the number of nonunary direction rules is \(h+1\). By Corollary 4 every direction-indexed profile occurs, even though both the cokernel dimension and number of nonunary rows diverge with \(n\).

*Rank proof.* Each leaf column is \(e_{b_j}\), so the leaf columns span the \(h\)-dimensional branch subspace. The column of branch vertex \(b_j\) is \(e_o+e_{a_j}+e_{d_j}\). These \(h\) columns are independent modulo the branch subspace, because their disjoint private-leaf supports are nonzero. The hub column is \(\sum_{j=1}^h e_{b_j}\) and is already in the branch subspace. Hence \(\operatorname{rank}A_h=2h\). The number of branch readers is three; the hub degree \(h\) is odd, so all row sums equal one. \(\square\)

**Audit.** A Gaussian-elimination and topological-sort implementation constructed geodesics with prescribed independently randomized color profiles in the \(T_h\) families for \(h=3,5,7,9\) (dimensions \(10,16,22,28\)); 200 target profiles were tested per instance. The computed ranks were \(6,10,14,18\), respectively, agreeing with \(2h\). Separately, all 32,768 legal affine five-direction dependency matrices were checked for full profile support, as were 10,000 sampled legal affine six-direction matrices. These finite checks support, but do not establish, surjectivity for arbitrary affine matrices; only the forest theorem and its corollaries are proved.

*Scope.* The acyclic-orientation description (FO3) is valid for all legal affine colorings, not just forests. In general a cyclic exchange-support graph need not admit arbitrary choices of inverted edges; the full affine profile-surjectivity conjecture remains open beyond established classes. The forest theorem does not assert the unrestricted nonlinear NORI1 conjecture.

#### Universal local cycle transparency and one-cycle affine profiles

#### Universal local cycle transparency and one-cycle affine profile surjectivity

Let \(c_i(x)=\alpha_i+(Ax)_i\) be an affine antipodally odd edge coloring of \(Q_n\), where \(A_{ii}=0\) and \(A\mathbf1=\mathbf1\). Put \(V=\mathbb F_2^n/\operatorname{im}A\), \(v_i=[e_i]\in V\), and \(\gamma_{ij}=A_{ij}v_i+A_{ji}v_j\in V\). Let \(H_A\) be the undirected graph with edges \(ij\) precisely when \(\gamma_{ij}\ne0\). Every orientation of \(H_A\) induced by a total order is acyclic, and every acyclic orientation arises from some total order. Fixing a reference orientation, its reversed-edge sum determines the class of the color-profile offset modulo \(\operatorname{im}A\).

**Lemma 1 (universal vertex-star identity).** For every direction \(i\),
\[
\boxed{v_i=\sum_{j\ne i}\gamma_{ij}.}\tag{CL1}
\]
*Proof.* The first contribution is \((\sum_{j\ne i}A_{ij})v_i=v_i\), because row \(i\) has odd sum. The second is \([\sum_j A_{ji}e_j]=[Ae_i]=0\). \(\square\)

**Theorem 2 (local cycle transparency in arbitrary affine exchange graphs).** Let \(C\) be any simple undirected cycle of length \(\ell\ge3\) in \(H_A\), and let \(W_C\subseteq V\) be the span of all exchange labels from edges not belonging to \(C\). In the quotient \(\widetilde V=V/W_C\), there exists a nonempty proper subset \(D\subsetneq E(C)\) satisfying
\[
\boxed{\sum_{e\in D}\widetilde\gamma_e=0.}\tag{CL2}
\]
Consequently, every attainable class in \(\widetilde V\) of an orientation of \(C\) is also attained by an orientation in which \(C\) is not directed. This conclusion imposes no assumptions on other cycles elsewhere in \(H_A\).

*Proof.* All directions outside \(C\) have \(\widetilde v_j=0\), by the vertex-star identity: every edge incident to such \(j\) lies outside \(C\). For a vertex \(i\) on \(C\), denote its two incident cycle labels by \(\gamma_{i-}\), \(\gamma_{i+}\), giving \(\widetilde v_i=\widetilde\gamma_{i-}+\widetilde\gamma_{i+}\). Fix an edge \(e=ij\) on the cycle, with predecessor edge \(e_-\) at \(i\) and successor edge \(e_+\) at \(j\), following an arbitrary cyclic order. Put \(a=A_{ij}\), \(b=A_{ji}\), with \((a,b)\ne(0,0)\) because \(\gamma_e\ne0\). The definition of \(\gamma_e\) gives
\[
(1+a+b)\widetilde\gamma_e+
a\widetilde\gamma_{e_-}+
b\widetilde\gamma_{e_+}=0.
\tag{CL3}
\]
If \((a,b)=(1,0)\), the predecessor label vanishes; if \((a,b)=(0,1)\), the successor label vanishes. If both equal one, the sum of the predecessor, central, and successor labels vanishes. For \(\ell\ge4\), these are nonempty proper edge subsets, proving (CL2).

It remains to treat a triangle on which every cycle edge has \(a=b=1\). At each of its three vertices, the two internal readers give even parity. Since every row of \(A\) has odd sum, each triangle vertex \(i\) has some reader \(j\) outside the triangle with \(A_{ij}=1\). In \(\widetilde V\), both \(\widetilde v_j=0\) and \(\widetilde\gamma_{ij}=0\), whether \(ij\) lies outside \(C\) as an edge of \(H_A\) or has label zero. The equation \(\widetilde\gamma_{ij}=A_{ij}\widetilde v_i+A_{ji}\widetilde v_j\) therefore yields \(\widetilde v_i=0\). Thus all triangle labels \(\widetilde\gamma_{ij}\) vanish, and any singleton triangle edge establishes (CL2). If at least one triangle edge is asymmetric, the first two cases of (CL3) already apply.

The two directed orientations of \(C\) differ by reversing every cycle edge. Let \(D\) be the proper nonempty zero-sum subset supplied above. Reversing the edges in \(D\) changes no class in \(\widetilde V\), and sends either directed orientation to a nondirected orientation. \(\square\)

**Theorem 3 (one-cycle affine closure with constructive witnesses).** If \(H_A\) contains at most one undirected cycle in total, then every direction-indexed full-geodesic color profile is realized:
\[
\boxed{\mathcal W(c)=\mathbb F_2^n.}\tag{CL4}
\]
For a prescribed profile, a starting root and direction order can be constructed in polynomial time by binary Gaussian elimination, cycle repair, and a topological sort.

*Proof.* If \(H_A\) is a forest, this is the previously proved forest theorem. Otherwise let \(C\) be its unique cycle and put \(W=W_C\). The noncycle edges induce a forest. For a desired target offset class \(t\in V\), first choose a subset of cycle-edge reversals whose labels have image \(t+W\) in \(V/W\). This is possible because all exchange labels together span \(V\). If these reversals make the cycle directed, change them on a nonempty proper subset from Theorem 2; the quotient class is unchanged, but the cycle becomes nondirected. The remaining difference in \(V\) lies in \(W\), so choose orientations of noncycle edges to match it, using their spanning definition. Regardless of those tree-edge orientations, the full orientation of \(H_A\) remains acyclic because its only possible undirected cycle is not directed. Topologically sort to obtain a total direction order \(\pi\), then solve \(Ax=w+\alpha+r_\pi\). The prescribed profile follows. All operations are polynomial-time linear algebra or graph algorithms. \(\square\)

**Nonforest example.** In dimension five, take the binary row masks
\[
(A_0,A_1,A_2,A_3,A_4)=(2,13,2,7,8),
\]
meaning
\[
c_0=x_1+\alpha_0,\quad c_1=x_0+x_2+x_3+\alpha_1,\quad
c_2=x_1+\alpha_2,\quad c_3=x_0+x_1+x_2+\alpha_3,\quad
c_4=x_3+\alpha_4.
\]
Every row has odd weight and zero diagonal. The cokernel has dimension two, with representatives \(v=(1,2,3,2,2)\) in a fixed two-bit basis. Its nonzero exchange-label graph has edges \(01,03,12,23,34\), containing the four-cycle \(0-1-2-3-0\) and a pendant edge \(34\). Independent dynamic programming confirms all four cokernel classes occur. Theorem 3 proves this directly and for all affine constants.

**Scope and methodological caution.** The cycle-transparency theorem holds for *every* legal affine matrix and identifies a universal forced relation near each cycle. The full-surjectivity corollary requires at most one cycle. For graphs with multiple interacting cycles, repairing one directed cycle may change other cycles, so Theorem 2 must not be interpreted as a global acyclic-orientation selection theorem. Neither result proves unrestricted affine or nonlinear NORI1.

#### Odd paired-block nonlinear profile universality

### Odd paired-block profile universality with nonlinear later-bit gates

All sums are in F2. For a subset S of direction labels, write p_S(x)=sum_(i in S)x_i. A full-geodesic profile records the edge colors indexed by direction.

Lemma 1 (odd bipartite four-run ordering). Let U,V be disjoint nonempty direction sets of odd sizes, and define the cube-edge colors c_i(x)=beta_i+p_V(x) for i in U, c_j(x)=beta_j+p_U(x) for j in V, where beta_i are arbitrary constants. Fix any starting root x. A profile w is attained by some full direction order from x if and only if
sum_(i in U union V)(w_i+beta_i)=1+p_U(x)+p_V(x). (L1)
Consequently the rootwise profile image contains 2^(|U|+|V|-1) words and each prescribed word is attained from 2^(|U|+|V|-1) roots.

Proof. The vertex function Q(x)=p_U(x)p_V(x) has derivative Q(x)+Q(x+e_i) equal to the partner-block parity for any i. Along a full geodesic, the sum of these derivatives telescopes to Q(x)+Q(bar x)=1+p_U(x)+p_V(x), since both block sizes are odd. This proves necessity. For sufficiency, put z_i=w_i+beta_i+p_V(x) on U and z_i=w_i+beta_i+p_U(x) on V; (L1) makes the total number of ones in z odd. Write U0,U1,V0,V1 for the four lists partitioned by z value, and a=|U1|, b=|V1|. When a is odd and b even, take the direction order U0,V0,U1,V1. The number of preceding V-moves has parity zero on U0 and one on U1 because |V0| is odd; the number of preceding U-moves is even on V0 because |U0| is even, and odd on V1 because |U| is odd. This realizes z, hence w. When a is even and b odd, use V0,U0,V1,U1, with the symmetric verification. For any prescribed w, condition (L1) is one nonzero root-bit parity equation, giving the root count. QED.

Theorem 2 (arbitrary nonlinear one-way gates). Partition all n dimensions into r ordered pairs of odd-sized nonempty blocks (U_t,V_t), 1<=t<=r. Set L_t=union_(s>t)(U_s union V_s). For every individual direction i in U_t union V_t choose alpha_i in F2 and an arbitrary Boolean function f_i on the L_t bits satisfying f_i(bar z)=f_i(z). Define c_i(x)=alpha_i+p_(V_t)(x)+f_i(x_(L_t)) for i in U_t, and c_i(x)=alpha_i+p_(U_t)(x)+f_i(x_(L_t)) for i in V_t. Then c is a legal antipodally odd edge coloring, and every binary direction-indexed profile is attained by a full antipodal geodesic. All witnesses can use orders that traverse the block pairs in sequence, with at most four runs inside each pair.

More strongly, for any fixed starting vertex x, the profiles attained by these pair-consecutive direction orders are precisely the solutions w to the r parity equations
sum_(i in U_t union V_t)(w_i+alpha_i+f_i(x_(L_t)))=1+p_(U_t)(x)+p_(V_t)(x), 1<=t<=r. (L2)
They form an affine subspace of codimension r and size 2^(n-r). For each prescribed w, the number of roots satisfying (L2) is 2^(n-r), and all such roots admit a pair-consecutive geodesic with profile w.

Proof. An old-direction rule is unchanged on its undirected edge because it reads only its opposite block and later blocks. Under global antipodal translation the parity of its opposite odd block flips and the even gate f_i does not, establishing legality. During traversal of the t-th pair, later bits remain fixed and earlier bits do not occur in that pair's rules. The frozen pair coloring therefore has the form of Lemma 1, with constants beta_i=alpha_i+f_i(x_(L_t)). Lemma 1 establishes (L2), including the sufficiency by four-run order for each pair. The r conditions involve disjoint target-bit sets and hence have rank r for fixed x. To prescribe w and choose a starting root, process pairs from r backwards to 1. Once the later root bits are chosen, the t-th equation requires only one parity on the current pair's root bits and permits 2^(|U_t|+|V_t|-1) assignments. Their product is 2^(n-r). For every resulting root, concatenate the four-run direction orders supplied by Lemma 1. QED.

The gates may have unbounded Boolean degree and vary independently with i. For instance, if there are r>=3 pairs, take f_i(x)=product_(s>t)(x_(u_s)+x_(v_s)) for all i in U_t with t<=r-2, where u_s in U_s and v_s in V_s are fixed representatives. Each factor is antipodally even; the earliest gate has degree r-1. Taking |U_t|=|V_t|=3 gives 3(r-2) nonlinear rows of degree at least two.

Theorem 3 (affine odd-clone lift with matched invertible core). Let m be even and B in GL_m(F2) satisfy B_aa=0, B*1=1, and B_(2t-1,2t)=B_(2t,2t-1)=1 for each matching pair. Partition [n] into odd-sized nonempty blocks D_1,...,D_m. For i in D_a set
c_i(x)=alpha_i+sum_(b=1)^m B_ab p_(D_b)(x). (L3)
Then c is legal and antipodally odd, its affine reader matrix has rank m, and every full direction-indexed color profile occurs.

Proof. Let p_b be the initial parity of D_b. When the pair (D_(2t-1),D_(2t)) is traversed after all earlier pairs, the frozen part of the color in D_a equals alpha_i+(Bp)_a+sum_(b<2t-1)B_ab, and every preceding direction of its matched block toggles that color once. For any prescribed profile, Lemma 1 allows choosing arbitrary effective phases for each matched pair subject only to one selectable odd parity condition; choose them to support a four-run order. This determines the desired vector q=Bp, because the earlier-completed-block correction is known for every a. Invert B to obtain p, select root bits with those block parities, and concatenate the matched-pair four-run orders. The reader matrix is the composition of the surjective block-parity map, invertible B, and injective block-repetition map, proving rank m. QED.

Corollary. For any odd p,q>=1, the complete bipartite reader graph K_(p,q) gives a legal affine coloring of rank 2 and corank p+q-2 whose exchange graph has (p-1)(q-1) independent cycles; its complete profile support follows from Theorem 3. For any even m, B=I+J (J the all-one matrix) satisfies B^2=I and has reciprocal pairs; all complete multipartite reader graphs with m odd-sized classes therefore satisfy the same full-profile conclusion with rank m, regardless of their many interacting cycles.

Independent tests used randomly generated antipodally even truth-table gates separately for every direction in Q_10, Q_12 and Q_14, constructing 1,000 prescribed profiles per instance and checking legality. The affine matched-core construction was checked on 250-300 prescribed targets in dimensions 6, 10 and 16. These are finite audits of the dimension-uniform proofs. The result covers unrestricted nonlinear complexity inside one-way gated paired-block systems but does not establish NORI1 for arbitrary legal colorings.

#### Cyclic paired-gate feedback and Boolean fixed-point obstructions

#### Cyclic paired-gate feedback encodes Boolean fixed points

Let \(r\ge1\), with \(2r\) directions named \(a_t,b_t\) for \(1\le t\le r\). Write \(u_t=x_{a_t}\), \(v_t=x_{b_t}\), and \(p_t=u_t+v_t\), with arithmetic in \(\mathbb F_2\). Choose arbitrary Boolean functions \(f_t:\mathbb F_2^{r-1}\to\mathbb F_2\), each acting on the list of parities \(p_s\), \(s\ne t\), and define
\[
\boxed{c_{a_t}(x)=v_t+f_t(p_{-t}),\qquad c_{b_t}(x)=u_t.}\tag{FB1}
\]
Every direction rule is constant along its own undirected edge. Antipodal translation changes \(u_t,v_t\) individually but preserves every parity \(p_s\), so (FB1) is a legal antipodally odd coloring in every dimension \(2r\).

Let a *pair-consecutive* direction order be one in which the two directions \(a_t,b_t\) of each pair are adjacent, while the \(r\) pairs may be permuted and oriented internally. For a target direction-indexed profile \(w\), define \(b_t=1+w_{a_t}+w_{b_t}\) and the Boolean map \(T_f(p)=(p_t+f_t(p_{-t}))_{t=1}^r\).

**Theorem 1 (feedback-profile fiber formula).** The number of rooted oriented full antipodal geodesics of (FB1) with profile \(w\) and a pair-consecutive order is
\[
\boxed{N_w^{\mathrm{pc}}=2^r\,r!\,|\{p\in\mathbb F_2^r:T_f(p)=b\}|.}\tag{FB2}
\]
In particular, a red pair-consecutive full geodesic exists if and only if \(T_f(p)=\mathbf1\) is solvable.

*Proof.* When the two directions of pair \(t\) are consecutive, every other pair is either entirely untouched or entirely traversed. Thus its parity \(p_s\) has its starting value during the two steps of pair \(t\). If \(a_t\) is followed by \(b_t\), the corresponding profile bits are \(w_{a_t}=v_t+f_t(p_{-t})\), \(w_{b_t}=u_t+1\). If \(b_t\) is followed by \(a_t\), they are \(w_{b_t}=u_t\), \(w_{a_t}=v_t+1+f_t(p_{-t})\). In both orders,
\[
w_{a_t}+w_{b_t}=1+p_t+f_t(p_{-t}).\tag{FB3}
\]
Conversely, if (FB3) matches the target pair-bit sum, then for a fixed root precisely one of the two internal orders yields the two individually prescribed colors: switching the internal order complements both profile bits. For each admissible parity vector \(p\) there are \(2^r\) starting roots realizing it, each pair has one forced internal order, and the \(r\) pairs can be permuted in \(r!\) ways without changing their parity inputs. This proves (FB2). \(\square\)

**Theorem 2 (arbitrary Boolean fixed-point realization).** Let \(F:\mathbb F_2^r\to\mathbb F_2^r\) be an arbitrary Boolean map, represented by a Boolean circuit. Construct a legal odd coloring of \(Q_{4r}\) with \(2r\) named pairs, \(P_i=(a_i,b_i)\) and \(Q_i=(c_i,d_i)\). Define the pair parities \(p_i=x_{a_i}+x_{b_i}\), \(q_i=x_{c_i}+x_{d_i}\), and direction-color rules
\[
\begin{array}{ll}
c_{a_i}=x_{b_i}+q_i, & c_{b_i}=x_{a_i},\\
c_{c_i}=x_{d_i}+F_i(p), & c_{d_i}=x_{c_i}.
\end{array}\tag{FB4}
\]
All gates read only other pairs' parities, so this belongs to the cyclic paired-gate family (FB1). The rooted oriented red full-geodesic count among orders keeping every \(P_i\) and \(Q_i\) consecutive is
\[
\boxed{2^{2r}(2r)!\,|\operatorname{Fix}(F)|.}\tag{FB5}
\]
In particular, such a red geodesic exists if and only if \(F\) has a fixed point.

*Proof.* Applying (FB3) with target profile zero to the \(P_i\) pair yields \(p_i+q_i=1\); applying it to \(Q_i\) yields \(q_i+F_i(p)=1\). Eliminating \(q\) gives \(F_i(p)=p_i\) for all \(i\). Each fixed point \(p\) determines \(q=\mathbf1+p\); the \(2r\) pair parities admit \(2^{2r}\) starting roots, each has a unique red orientation within each pair, and all \((2r)!\) orders of the pairs succeed. \(\square\)

**Corollary 3 (SAT universality of static pair schedules).** For a Boolean formula \(\psi(z_1,\ldots,z_r)\), set \(F_1(z)=z_1+1+\psi(z)\) and \(F_i(z)=z_i\) for \(i>1\). Then \(\operatorname{Fix}(F)=\{z:\psi(z)=1\}\), so the legal odd edge-coloring in (FB4) has a red pair-consecutive full geodesic if and only if \(\psi\) is satisfiable. With Boolean-circuit encodings of the color rules, existence of a red pair-consecutive antipodal geodesic is NP-complete even for the family (FB4), and counting such rooted ordered red geodesics determines the number of satisfying assignments after division by \(2^{2r}(2r)!\). This is a restricted scheduling problem; it does not claim NP-hardness or failure of unrestricted monochromatic geodesic existence.

**Four-dimensional obstruction repaired by interleaving.** Let \(r=2\), \(f_1(p_2)=p_2\), and \(f_2(p_1)=p_1+1\). Then the pair-consecutive all-red conditions are \(p_1+p_2=1\) and \(p_1+p_2=0\), so no such path exists. Nevertheless, from root \((u_1,v_1,u_2,v_2)=(0,0,0,0)\), the order
\[
\boxed{b_1,\ b_2,\ a_1,\ a_2}\tag{FB6}
\]
has four red edges and terminates at the antipode. The second pair's parity is temporarily toggled when the first \(a\)-direction is evaluated; this defeats the inconsistent static parity constraints.

**Finite feedback audit, not a universal theorem.** For \(r=3\), all \(16^3=4096\) choices of the functions \(f_t:\mathbb F_2^2\to\mathbb F_2\) were enumerated. Each corresponding legal odd \(Q_6\) coloring attained all 64 direction-indexed profiles using direction orders with at most two simultaneously open pairs (a pair is open after its first and before its second step). In 816 instances pair-consecutive orders already attained all profiles; in the other 3280 some profile required interleaving. Random samples for \(r=4\) likewise had width-two profile witnesses. These finite observations do not establish a dimension-uniform width-two theorem.

The reduction identifies a limitation of any argument that assumes the parity equations of cyclically dependent interfaces can always be solved simultaneously: such equations represent arbitrary Boolean fixed-point problems. Allowing interleaving introduces intermediate-state changes absent from those static equations. The existence of full monochromatic geodesics without pair-consecutive restriction remains a separate question.

#### Three-phase parity reset eliminates arbitrary nonlinear feedback

#### Three-phase reset theorem: arbitrary cyclic pair-feedback gates are profile-universal

Let \(r\ge1\) and index \(2r\) cube directions by \(a_i,b_i\) (\(i\in[r]\)). Write \(u_i=x_{a_i}\), \(v_i=x_{b_i}\) and \(p_i=u_i+v_i\). For every \(i\), let \(f_i:\mathbb F_2^{[r]\setminus\{i\}}\to\mathbb F_2\) be an unrestricted Boolean function (there is no acyclicity, locality, degree, or rank hypothesis), and define
\[
\boxed{c_{a_i}(x)=v_i+f_i(p_{-i}),\qquad c_{b_i}(x)=u_i.}\tag{TR1}
\]
Every rule ignores its own direction bit. Global antipodal translation complements \(u_i,v_i\), but preserves each \(p_j\), so the coloring is legal and antipodally odd.

**Theorem 1 (unrestricted feedback profile universality).** For every coloring (TR1), every prescribed direction-indexed binary profile \(w\in\mathbb F_2^{2r}\) occurs on a full antipodal geodesic. In symbols,
\[
\boxed{\mathcal W(c)=\mathbb F_2^{2r}.}\tag{TR2}
\]
More strongly, fix any order \(\sigma\in S_r\) of the \(a_i\)-directions. There is a constructive full geodesic with profile \(w\), using the following three-phase form: an initial group of selected \(b\)-directions, then the \(a\)-directions in order \(\sigma\), then the remaining \(b\)-directions. Its initial vertex and the membership of the two \(b\)-groups are obtained with precisely \(r\) evaluations of the Boolean gates.

*Proof.* For \(i\ne j\) define \(k_{ij}=[a_j\text{ precedes }a_i\text{ in }\sigma]\), and regard \(k_{i,-i}\in\mathbb F_2^{r-1}\) as a fixed input for the \(i\)-th gate. For the desired profile \(w\), set
\[
\boxed{p_i=1+w_{a_i}+w_{b_i}+f_i(k_{i,-i}),}\tag{TR3}
\]
\[
\boxed{u_i=w_{b_i}+1+p_i,\qquad v_i=u_i+p_i.}\tag{TR4}
\]
Start at the vertex with the indicated \(u_i,v_i\). First traverse every direction \(b_i\) for which \(p_i=1\), in arbitrary order. Second traverse all \(a_i\) in order \(\sigma\). Third traverse all \(b_i\) with \(p_i=0\), in arbitrary order.

After phase one, \(v_i\) has become \(u_i\) for every \(i\), since the initial \(b_i\)-bit differs from \(u_i\) by \(p_i\) and \(b_i\) is flipped once precisely when \(p_i=1\). Thus every pair parity is zero before phase two. During phase two, just before \(a_i\), the current pair-parity vector outside \(i\) is precisely \(k_{i,-i}\), independently of the starting vertex. Furthermore \(v_i=u_i\) before \(a_i\), so
\[
c_{a_i}=u_i+f_i(k_{i,-i})=w_{a_i}
\]
by (TR3)-(TR4). For the direction \(b_i\), if \(p_i=1\), it was traversed in phase one and its color was \(u_i=w_{b_i}\). If \(p_i=0\), it is traversed in phase three, after \(a_i\) has flipped \(u_i\), so its color is \(u_i+1=w_{b_i}\). Every direction is used once. Therefore the path is a full antipodal geodesic and has all prescribed colors. \(\square\)

**Corollary 2 (many constructive witnesses and oracle complexity).** For every target \(w\), each one of the \(r!\) orders \(\sigma\) gives a rooted, ordered full geodesic of profile \(w\), with different orders on the \(a_i\). Consequently
\[
\boxed{G_c(w)\ge r!\qquad\text{for all }w.}\tag{TR5}
\]
For a fixed \(\sigma\), only the \(r\) Boolean values \(f_i(k_{i,-i})\) are queried. The root and path are constructed with \(O(r^2)\) elementary operations, apart from those queries, regardless of the functions' Boolean degree or circuit complexity. For fixed \(\sigma\) and \(w\), the root and partition of \(b\)-steps in this particular three-phase scheme are uniquely determined by (TR3)-(TR4).

**Corollary 3 (static SAT-hardness versus unrestricted constructive solvability).** The earlier fixed-point encoding remains valid: restricting (TR1) to pair-consecutive orders makes existence of a red full geodesic equivalent to a Boolean fixed-point equation and is NP-complete under circuit input. Removing that restriction yields the explicit algorithm of Theorem 1. Thus the SAT obstruction is solely an artifact of forbidding dynamic interleaving; arbitrary Boolean feedback does not obstruct full profiles in this entire family. The theorem supersedes the previous uncertainty about unrestricted profile attainment for (TR1); whether two simultaneously open pairs always suffice is a separate bounded-width scheduling question and is not needed for NORI1 closure within this family.

**Gauge-reset interpretation.** Phase one moves the root onto the diagonal subcube \(\{x_{a_i}=x_{b_i}\ \forall i\}\); phase two evaluates all nonlinear feedback gates on a completely predetermined chain of pair-parity states \(0,e_{\sigma_1},e_{\sigma_1}+e_{\sigma_2},\ldots\); phase three completes the antipodal traversal. This temporary reset breaks every apparent feedback cycle without solving any fixed-point equation.

**Independent audit.** Implemented the construction with independently sampled unrestricted Boolean truth tables for each gate, random profiles and random \(\sigma\). Verified legality by symbolic inspection and directly simulated 300 target profiles per sample in dimensions \(4,6,8,10,16,24\), all successful. These finite tests supplement the dimension-uniform proof.

*Scope.* The theorem covers cyclic dependence of arbitrary complexity through other pairs' XOR parities, with the private \(b_i\)-directions serving as resettable auxiliary bits. It does not establish a comparable reset mechanism for an arbitrary legal odd coloring of \(Q_n\); in particular a counterexample-preserving paired lift need not possess these programmable scratch-bit rules.

### Coxeter-window switch moments and a boundary spectral polynomial

We work with the Coxeter-coset representations of Article XIV. A general averaging identity permits direct comparison of the canonical type-A and type-B models without losing full-path admissibility.

**Lemma 1 (uniform Coxeter-window moment).** Let \(G\) be a finite group, \(t\in G\), \(q:G\to\{-1,1\}\), and \(m\ge2\). For each \(g\in G\), let \(\mathsf w_g=(q(g),q(gt),\ldots,q(gt^{m-1}))\), with a switch whenever consecutive signs differ. Then
\[
\boxed{\quad
\mathbb E_{g\in G}\operatorname{sw}(\mathsf w_g)
=\frac{m-1}{2}\left(
1-\mathbb E_{g\in G}q(g)q(gt)
\right).
\quad}
\tag{1}
\]

*Proof.* The switch indicator between consecutive signs \(u,v\in\{-1,1\}\) is \((1-uv)/2\). For each fixed window position \(j\), uniformity of \(g\) makes \(gt^j\) uniform in \(G\), giving the same correlation \(\mathbb E_g q(g)q(gt)\). Summing over \(m-1\) comparisons proves (1). \(\square\)

#### A cubical sum-of-squares identity

For any binary undirected-edge coloring of \(Q_n\), define
\[
s_i(x)=(-1)^{c(\{x,x\oplus e_i\})},
\qquad
M(x)=\sum_{i=1}^n s_i(x).
\tag{2}
\]
In particular, \(s_i(x\oplus e_i)=s_i(x)\).

**Theorem 2 (cubical switch moment).** If \(x\) is a uniform cube root and \(\pi\) a uniform permutation of all dimensions, the full antipodal geodesic \(P(x,\pi)\) satisfies
\[
\boxed{\quad
\mathbb E_{x,\pi}\operatorname{sw}(P(x,\pi))
=\frac n2-\frac1{2n\,2^n}\sum_{x\in Q_n} M(x)^2
\le\frac n2.
\quad}
\tag{3}
\]
For odd \(n\), the right-hand side is at most \(n/2-1/(2n)\). Consequently every cube-edge coloring admits a full antipodal geodesic with at most \(\lfloor n/2\rfloor\) switches. For antipodally odd colorings, the parity reduction of Article IX permits the smallest switch count to be chosen even.

*Proof.* At each of the \(n-1\) comparisons of successive edges, their dimensions are a uniformly selected ordered pair \(i\ne j\), and the tail \(y\) of the first edge is uniform over \(Q_n\). The edge signs are \(s_i(y)\) and \(s_j(y\oplus e_i)\). By translation invariance of uniform \(y\) and \(s_i(y\oplus e_i)=s_i(y)\),
\[
\mathbb E_y[s_i(y)s_j(y\oplus e_i)]
=\mathbb E_y[s_i(y)s_j(y)].
\]
Averaging over \(i\ne j\) yields
\[
\mathbb E\operatorname{sw}
=\frac{n-1}{2}
-\frac1{2n}\mathbb E_y\sum_{i\ne j}s_i(y)s_j(y).
\]
Since \(\sum_{i\ne j}s_i s_j=M(y)^2-n\), (3) follows. For odd \(n\), the sum of \(n\) signs is odd, hence \(M(y)^2\ge1\). Integer rounding and the earlier antipodal rotation lemma give the consequences. \(\square\)

This nonnegative quadratic defect is available even without antipodal oddness; its positivity comes from undirected-edge incidence compatibility.

#### The boundary-tournament transition operator

Let \(n\ge4\). On ordered distinct triples define a real field \(s(a,b,c)\) satisfying
\[
s(c,b,a)=-s(a,b,c).
\tag{4}
\]
The sign field of any ordinary reversal-odd boundary tournament belongs to this space and takes values in \(\{-1,1\}\). Let \(H_n\) be the real vector space of such fields, represented by the independent entries \(s(a,b,c)\) with \(a<c\) and their standard Euclidean inner product. Define
\[
\boxed{\quad
(A_n s)(a,b,c)
=\sum_{d\notin\{a,b,c\}}
\bigl[s(b,c,d)-s(b,a,d)\bigr].
\quad}
\tag{5}
\]
The right-hand side is odd under interchange of \(a,c\), so \(A_n\) maps \(H_n\) to itself.

**Lemma 3 (boundary correlation).** The operator \(A_n\) is self-adjoint, and for any binary boundary tournament with sign field \(s\),
\[
\boxed{\quad
\mathbb E_{\pi\in S_n}\operatorname{sw}
=\frac{n-3}{2}
\left(1-\frac{\langle s,A_n s\rangle}
{2(n-3)\langle s,s\rangle}\right).
\quad}
\tag{6}
\]

*Proof.* Put \(F(s,t)=\sum_{a,b,c,d\ {\rm distinct}}s(a,b,c)t(b,c,d)\). Under reversal of the ordered quadruple, both fields acquire a minus sign, so \(F(s,t)=F(t,s)\). The skew relation (4), followed by the exchange \(a\leftrightarrow c\), gives \(\langle s,A_n t\rangle=F(s,t)\) in the independent-entry inner product. This proves self-adjointness. For sign fields, \(\langle s,s\rangle=n(n-1)(n-2)/2\). Every consecutive pair of triple bits in a uniform Hamilton order is distributed as a uniform ordered quadruple of distinct vertices. Hence its sign correlation equals \(F(s,s)/[n(n-1)(n-2)(n-3)]\). Substitute in Lemma 1 with \(m=n-2\) to obtain (6). \(\square\)

**Theorem 4 (boundary spectral polynomial; finite-algebra certificate).** For every \(n\ge4\), the symmetric operator (5) satisfies
\[
\boxed{\quad
A_n(A_n+2I)(A_n-I)
\bigl(A_n^2-(n-2)^2 I\bigr)=0.
\quad}
\tag{7}
\]
Thus every eigenvalue belongs to \(\{-(n-2),-2,0,1,n-2\}\), and in particular
\[
\boxed{\quad
\mathbb E_{\pi\in S_n}\operatorname{sw}
\le \frac{3n-8}{4}.
\quad}
\tag{8}
\]
For \(n=5\), inequality (8) gives a Hamilton tight path with at most one switch.

*Computer-assisted proof of (7), with a finite interpolation justification.* The coefficients of \(A_n\), between two ordered-triple basis vectors, depend only on the equality pattern among their symbols. The entries of \(A_n^k\) count signed \(k\)-step transitions, where each step introduces at most one new symbol. After fixing the input and output triples (together involving at most six symbols), classify the intermediate symbols by equality pattern. A pattern involving \(r\) additional distinct symbols contributes a multiple of the falling factorial \((n-h)_r\), where \(h\le6\) is the number of fixed symbols, and \(r\le k\). Consequently each matrix entry of \(A_n^k\), for every fixed input-output equality pattern and \(n\ge6\), is a polynomial in \(n\) of degree at most \(k\). Expanding the left-hand side of (7), including its coefficients polynomial in \(n\), gives degree at most five. Every possible equality pattern among two triples occurs already for \(n=6\). It therefore suffices to verify the integer matrix identity for the six values \(n=6,\ldots,11\). The remaining \(n=4,5\) are checked directly.

Here is a standalone Python 3 / SciPy verification of these finitely many integer equalities. Each matrix entry is an integer, so no floating-point eigensolver or tolerance is involved.

\`\`\`python
from itertools import permutations
import numpy as np
from scipy.sparse import coo_matrix, identity

for n in range(4, 12):
    reps = [(a,b,c) for a,b,c in permutations(range(n),3) if a<c]
    loc = {t:(i,1) for i,t in enumerate(reps)}
    for i,(a,b,c) in enumerate(reps):
        loc[c,b,a] = (i,-1)

    rows, cols, vals = [], [], []
    for i,(a,b,c) in enumerate(reps):
        for d in range(n):
            if d in (a,b,c):
                continue
            j,sgn = loc[b,c,d]
            rows.append(i); cols.append(j); vals.append(sgn)
            j,sgn = loc[b,a,d]
            rows.append(i); cols.append(j); vals.append(-sgn)

    A = coo_matrix(
        (np.array(vals, dtype=np.int64), (rows,cols)),
        shape=(len(reps),len(reps))
    ).tocsr()
    A.sum_duplicates()
    I = identity(len(reps), dtype=np.int64, format="csr")
    P = A @ (A+2*I) @ (A-I) @ (A-(n-2)*I) @ (A+(n-2)*I)
    P.eliminate_zeros()
    assert (A-A.T).nnz == 0
    assert P.nnz == 0
\`\`\`

The polynomial interpolation argument promotes this finite verification to all \(n\ge4\). Since \(A_n\) is real symmetric, (7) bounds its smallest eigenvalue below by \(-(n-2)\). Inserting this in (6) yields
\[
\frac{n-3}{2}\left(1+\frac{n-2}{2(n-3)}\right)
=\frac{3n-8}{4},
\]
proving (8). The number of switches is integral, and \((3\cdot5-8)/4=7/4<2\), giving the stated five-vertex consequence. \(\square\)

#### Implication for the unified conjecture

The cubical and boundary coset models now share Lemma 1, a spectral quadratic formulation of their complete-path switch counts. Local incidence descent gives the positive sum-of-squares formula (3) in type B. In type A, the corresponding compressed Coxeter transition has the five-root polynomial (7), proved by the finite-algebra certificate above. Both guarantee complete paths with bounded switches in every dimension, while neither alone forces the desired universal one-switch conclusion in large rank. A full proof needs either higher moments or structural concentration beyond the first Coxeter correlation.

### Root selection: six-vertex rooted closure and seven-vertex obstruction

Let \(b(a,h,c)\in\mathbb F_2\) be an arbitrary coloring of pairwise distinct ordered triples satisfying \(b(c,h,a)=1-b(a,h,c)\). A Hamilton tight path rooted at \(a\) is a permutation of all original vertices beginning with \(a\).

**Theorem 1 (computer-assisted six-vertex closure).** On six vertices, every such coloring has a Hamilton tight path starting at any prescribed vertex whose four triple bits have at most one switch.

*Finite exhaustive proof.* Relabel the root as \(0\). There are 60 reversal pairs of triples, represented by tuples \((a,h,c)\) with \(a<c\). There are \(5!=120\) Hamilton orderings beginning at \(0\). To deny the conclusion, every one of their four-bit words must avoid the eight words with at most one switch. Each forbidden favorable word gives a clause requiring one of its four entries to differ from the specified entry. This yields 960 clauses on 60 Boolean variables. Global complementation preserves the hypotheses and switch counts, so fix \(b(0,1,2)=0\).

Here is a standalone exhaustive Boolean verifier. It uses unit propagation followed by complete binary branching. Every branch is considered.

\`\`\`python
from itertools import permutations, product
V = range(6)
reps = sorted(t for t in permutations(V,3) if t[0]<t[2])
idx = {t:i for i,t in enumerate(reps)}
clauses = []
for tail in permutations(range(1,6)):
    p = (0,)+tail
    triples = [p[j:j+3] for j in range(4)]
    for w in product((0,1),repeat=4):
        if sum(w[j]!=w[j+1] for j in range(3))>1:
            continue
        C = []
        for t,v in zip(triples,w):
            flip = t[0]>t[2]
            rep = t[::-1] if flip else t
            C.append((idx[rep],1-(v^flip)))
        clauses.append(C)
calls = 0
def sat(a):
    global calls
    calls += 1
    while True:
        changed = False
        for C in clauses:
            if any(a[i]==v for i,v in C): continue
            free = [(i,v) for i,v in C if a[i]<0]
            if not free: return False
            if len(free)==1:
                i,v = free[0]
                a[i] = v
                changed = True
        if not changed: break
    weights = [0.0]*len(a)
    for C in clauses:
        if any(a[i]==v for i,v in C): continue
        free = [i for i,_ in C if a[i]<0]
        for i in free: weights[i] += 1/(len(free)**2)
    if max(weights)==0: return True
    i = weights.index(max(weights))
    for v in (0,1):
        b = a.copy()
        b[i] = v
        if sat(b): return True
    return False
a = [-1]*len(reps)
a[idx[(0,1,2)]] = 0
assert len(reps)==60 and len(clauses)==960
assert not sat(a)
print("UNSAT",calls)  # UNSAT 8085
\`\`\`

The verifier explores 8085 recursive nodes and establishes infeasibility. An independently coded binary integer feasibility model with XOR constraints also reports infeasibility. Thus no counterexample exists for root \(0\), and relabeling proves the theorem for any root. \(\square\)

**Corollary.** In every reversal-odd boundary tournament on at least six vertices, each specified root begins some vertex-simple six-vertex tight path with at most one switch. Choose any six vertices containing the root and restrict the coloring.

**Theorem 2 (seven-vertex rooted obstruction).** There is a reversal-odd boundary 3-tournament on \(V=\{0,\ldots,6\}\) such that every Hamilton ordering beginning at \(0\) has at least two switches, although some Hamilton ordering has zero switches.

*Explicit construction and proof.* List lexicographically all 105 triples \((a,h,c)\) of distinct vertices with \(a<c\), indexed \(j=0,\ldots,104\). Set
\[
H=\mathtt{0x18651ceb71780f8fd20583f5729}.
\]
For the \(j\)-th listed triple, set \(b(a,h,c)\) to bit \(j\) of \(H\), counting from the least significant bit; set \(b(c,h,a)=1-b(a,h,c)\). The following independent short verifier checks every rooted and unrestricted Hamilton ordering:

\`\`\`python
from itertools import permutations
V = range(7)
rep = sorted((a,h,c) for a,h,c in permutations(V,3)
             if a<c)
index = {t:i for i,t in enumerate(rep)}
H = int("18651ceb71780f8fd20583f5729",16)
def bit(a,h,c):
    if a<c: return (H>>index[(a,h,c)])&1
    return 1-bit(c,h,a)
def switches(p):
    w = [bit(*p[i:i+3]) for i in range(5)]
    return sum(x!=y for x,y in zip(w,w[1:]))
assert len(rep)==105
assert min(switches((0,)+p)
           for p in permutations(range(1,7)))==2
assert min(switches(p) for p in permutations(V))==0
\`\`\`

Indeed, \((1,2,4,0,6,5,3)\) is a monochromatic Hamilton ordering with word \((0,0,0,0,0)\). The rooted ordering \((0,1,2,3,5,4,6)\) has word \((1,0,1,1,1)\), attaining the rooted minimum of two changes. \(\square\)

**Consequence for the unified conjecture.** The starting vertex of the boundary Hamilton path must be free to vary. This parallels the rooted-geodesic obstruction in NORI1, even though the two root parameters arise from different combinatorial data. The computer-assisted six-vertex theorem is suitable for replacement by an analytic proof, while the seven-vertex obstruction is specified by a reproducible finite certificate.

### The six-vertex boundary one-switch theorem from Coxeter spectra

We prove the ordinary reversal-odd boundary 3-tournament conjecture on six vertices, using the self-adjoint transition operator from the preceding subsection. The proof retains all six original vertices in the Hamilton witness and imposes no global order or representability condition on the tournament.

**Theorem 1 (six-vertex boundary closure).** Let \(V\) have six vertices and let \(b(a,h,c)\in\mathbb F_2\) be defined for all ordered distinct triples, subject only to
\[
b(c,h,a)=1-b(a,h,c).
\]
There exists a permutation \((v_1,\ldots,v_6)\) of \(V\) such that
\[
\boxed{\quad
\operatorname{sw}\bigl(
b(v_1,v_2,v_3),b(v_2,v_3,v_4),
b(v_3,v_4,v_5),b(v_4,v_5,v_6)
\bigr)\le1.
\quad}
\tag{1}
\]

*Proof.* Let \(s(a,h,c)=(-1)^{b(a,h,c)}\), so \(s(c,h,a)=-s(a,h,c)\). Fix a uniformly random permutation \(\pi=(v_1,\ldots,v_6)\) and put \(q_i=s(v_i,v_{i+1},v_{i+2})\) for \(i=1,2,3,4\). A four-bit word has at most one switch precisely when a majority of its three adjacent comparisons have equal signs. The elementary identity for \(q_i\in\{-1,1\}\) is
\[
\boxed{\quad
\mathbf1_{\{\operatorname{sw}(q_1,q_2,q_3,q_4)\le1\}}
=\frac12+\frac14(q_1q_2+q_2q_3+q_3q_4-q_1q_4).
\quad}
\tag{2}
\]
Uniformity under cyclic relabeling makes the three adjacent correlations equal:
\[
C_1=\mathbb E_\pi q_1q_2
=\mathbb E_\pi q_2q_3
=\mathbb E_\pi q_3q_4.
\]
Moreover
\[
\mathbb E_\pi q_1q_4
=\mathbb E_\pi s(v_1,v_2,v_3)s(v_4,v_5,v_6)=0,
\tag{3}
\]
since exchanging \(v_1,v_3\) changes the sign of the first factor and leaves the second unchanged. Averaging (2) therefore yields
\[
\Pr_\pi(\operatorname{sw}\le1)=\frac12+\frac34 C_1.
\tag{4}
\]

Let \(H_6\) be the 60-dimensional space of real fields \(s(a,b,c)=-s(c,b,a)\), with the independent-entry inner product, and define
\[
(A_6s)(a,b,c)
=\sum_{d\notin\{a,b,c\}}
\bigl[s(b,c,d)-s(b,a,d)\bigr].
\tag{5}
\]
The preceding spectral subsection proves that \(A_6\) is symmetric and satisfies the polynomial
\[
A_6(A_6+2I)(A_6-I)(A_6^2-16I)=0.
\tag{6}
\]
Its smallest eigenvalue is therefore at least \(-4\). The correlation identity from that subsection reads
\[
C_1=\frac{\langle s,A_6s\rangle}{6\langle s,s\rangle}
\ge-\frac23.
\tag{7}
\]
Consequently (4) is nonnegative. To obtain a successful Hamilton path we prove that equality in (7) is impossible for a sign field.

**Lemma 2 (negative extremal eigenspace).** The \(-4\)-eigenspace of \(A_6\) consists precisely of fields of the form
\[
s(a,b,c)=M_{ab}-M_{bc},
\tag{8}
\]
where \(M\) is a real symmetric \(6\times6\) matrix with zero diagonal and zero row sums. Its dimension is nine.

*Proof.* Let \(M\) be as stated. The field (8) is odd under interchange of its outer arguments. Since
\[
s(b,c,d)-s(b,a,d)
=M_{bc}-M_{ab}+M_{ad}-M_{cd},
\]
the zero row sums give
\[
\sum_{d\notin\{a,b,c\}}(M_{ad}-M_{cd})
=-M_{ab}+M_{bc}.
\]
There are three permitted values of \(d\), so (5) yields
\[
(A_6s)(a,b,c)=-3s(a,b,c)-s(a,b,c)=-4s(a,b,c).
\tag{9}
\]
The space of symmetric zero-diagonal matrices has 15 entries. Its six row-sum constraints are independent over \(\mathbb R\): any linear dependence would give scalars \(\lambda_a\) with \(\lambda_a+\lambda_b=0\) for all \(a\ne b\), forcing every \(\lambda_a=0\). Hence this space has dimension \(15-6=9\). The map \(M\mapsto s\) is injective: if every difference \(M_{ab}-M_{bc}\) vanishes, each row has constant off-diagonal entries, symmetry makes all those constants equal, and zero row sums make them zero.

It remains to show that the \(-4\)-eigenspace has dimension nine. In the independent-triple basis the integer matrix (5) has size 60, and direct finite walk enumeration gives
\[
\operatorname{tr}(I,A_6,A_6^2,A_6^3,A_6^4)
=(60,0,360,0,5040).
\tag{10}
\]
These five integer identities can be checked using the matrix construction in the preceding subsection, or by the following standalone checker:

\`\`\`python
from itertools import permutations
import numpy as np
from scipy.sparse import coo_matrix

n = 6
R = [(a,b,c) for a,b,c in permutations(range(n),3) if a<c]
index = {t:(i,1) for i,t in enumerate(R)}
index.update({t[::-1]:(i,-1) for i,t in enumerate(R)})
rows, cols, vals = [], [], []
for i,(a,b,c) in enumerate(R):
    for d in range(n):
        if d in (a,b,c):
            continue
        for t,sgn in (((b,c,d),1),((b,a,d),-1)):
            j,orient = index[t]
            rows.append(i); cols.append(j); vals.append(sgn*orient)
A = coo_matrix(
    (np.array(vals,dtype=np.int64),(rows,cols)),
    shape=(len(R),len(R))
).tocsr()
B = A.copy()
traces = [len(R)]
for k in range(1,5):
    traces.append(int(B.diagonal().sum()))
    B = B @ A
assert traces == [60,0,360,0,5040]
\`\`\`

By (6) and symmetry, the eigenvalues belong to \(\{-4,-2,0,1,4\}\). Let their multiplicities be \(m_\lambda\). Equation (10) gives the five linear equations
\[
\sum_\lambda m_\lambda\lambda^k
=(60,0,360,0,5040)_k,\qquad 0\le k\le4.
\]
The coefficient matrix is Vandermonde with distinct values \(-4,-2,0,1,4\), so the solution is unique:
\[
(m_{-4},m_{-2},m_0,m_1,m_4)=(9,10,15,16,10).
\]
Thus the nine-dimensional family (8) fills the entire \(-4\)-eigenspace. \(\square\)

Returning to Theorem 1, equality in (7) would force the sign vector \(s\) into the \(-4\)-eigenspace. By Lemma 2, there would be a symmetric matrix \(M\) with
\[
|M_{ab}-M_{bc}|=1
\qquad\text{for every three distinct }a,b,c.
\tag{11}
\]
Fix any middle vertex \(b\), and choose three distinct neighbors \(a,c,d\). Equation (11) would make the three real numbers \(M_{ab},M_{cb},M_{db}\) pairwise separated by absolute difference one. Three points on the real line cannot have all three pairwise distances equal to one. This contradiction proves
\[
C_1>-\frac23.
\]
Equation (4) then gives \(\Pr_\pi(\operatorname{sw}\le1)>0\). Therefore at least one permutation of all six vertices satisfies (1). \(\square\)

**Scope and significance.** The theorem proves the original six-vertex boundary conclusion for every reversal-odd coloring of ordered distinct triples. It does not require a prescribed initial vertex: a separate seven-vertex research note demonstrates that a fixed-root strengthening can fail. The proof is common to the Coxeter framework at the level of its local-incidence transition operator and positive-probability extraction, although the vanishing three-step correlation and extremal eigenspace analysis are specific to the type-A six-vertex instance. Larger dimensions remain open.

### Complementary-rank geodesic counting and parity blindness

Let \(D=[n]\), \(n\ge2\), and let \(c\) be an arbitrary binary coloring of **undirected** cube edges satisfying \(c(\bar e)=1-c(e)\). For \(x\in\mathbb F_2^n\), \(S\subseteq D\), and \(t\in\mathbb F_2\), let \(A_t(x,S)\) be the number of monochromatic color-\(t\) geodesics starting at \(x\), using precisely the dimensions in \(S\) (each once) and ending at \(x\oplus\mathbf1_S\). Put \(A_t(x,\varnothing)=1\). Paths are counted as ordered dimension sequences.

The recursion is
\[
A_t(x,S)=\sum_{i\in S}\mathbf1_{\{c(\{x,x\oplus e_i\})=t\}}\,
 A_t(x\oplus e_i,S\setminus\{i\})\quad(S\ne\varnothing).
\tag{1}
\]
Reversing a path and then applying the cube antipode gives a color-complementing bijection, and hence
\[
\boxed{A_t(x,S)=A_{1-t}(x\oplus\mathbf1_{D\setminus S},S).}
\tag{2}
\]
In particular \(A_0(x,D)=A_1(x,D)\) at **every** prescribed root.

**Theorem 1 (complementary-rank convolution identity).** For every root \(x\), color \(t\), and rank \(0\le k\le n\),
\[
\boxed{\quad
\sum_{\substack{S\subseteq D\\|S|=k}}
 A_t(x,S)\,A_{1-t}(x,D\setminus S)
 =
 A_t(x,D).
\quad}
\tag{3}
\]
Consequently the sum is independent of \(k\), and the path-existence statement \(A_t(x,D)>0\) is equivalent to the existence of complementary subsets \(S,D\setminus S\) for which both factors in some summand are positive.

*Proof.* Given a color-\(t\) full geodesic \(P\) from \(x\) to \(\bar x\), cut it after the \(k\)-th move. Let \(S\) be the set of dimensions used by its prefix. This prefix is a color-\(t\) geodesic counted by \(A_t(x,S)\). Its suffix, running from \(x\oplus\mathbf1_S\) to \(\bar x\), is color \(t\) with dimension set \(D\setminus S\). Reverse the suffix and take its antipodal image: the result is a color-\((1-t)\) geodesic from \(x\) to \(x\oplus\mathbf1_{D\setminus S}\), counted by \(A_{1-t}(x,D\setminus S)\). Conversely, any such pair of partial geodesics gives a full color-\(t\) geodesic by antipodally reversing the second one and appending it to the first. The dimension sets of the two parts are disjoint, so the concatenation uses every dimension once. These constructions are inverse at the prescribed cut rank \(k\). Thus (3) counts full color-\(t\) geodesics, each once. \(\square\)

**Corollary 2 (layer-by-layer separation under a hypothetical NORI1 counterexample).** If there is no monochromatic full antipodal geodesic at any root, then for every \(x,t,S\),
\[
\boxed{A_t(x,S)\,A_{1-t}(x,D\setminus S)=0.}
\tag{4}
\]
Conversely, (4) for all roots implies the absence of such a geodesic. Thus the proposed dimension-sensitive analogue of Wu–Yang's disjoint component-pair labeling is a **sequence of complementary-support separations at every Boolean rank**, not one equivalence-class partition. Moreover the local update (1) is a rank-increasing implication rather than equality along monochromatic edges. This is where the component-based rook-labeling reduction cannot simply be copied.

**Theorem 3 (parity blindness of the simple arm pairing).** In the square-zero polynomial algebra
\[
\mathcal A=\mathbb Z[z_1,\ldots,z_n]/(z_1^2,\ldots,z_n^2),
\qquad
P_t^x(\mathbf z)=\sum_{S\subseteq D}A_t(x,S)\prod_{i\in S}z_i,
\tag{5}
\]
the top-degree coefficient satisfies
\[
\boxed{[z_D]P_t^xP_{1-t}^x=(n+1)A_t(x,D).}
\tag{6}
\]
When \(n\) is odd, this coefficient vanishes modulo two for every coloring, even when monochromatic full geodesics exist. More strongly, for **every even** \(n=2m\ge4\), there exists an antipodally odd coloring with monochromatic full geodesics but
\[
A_0(x,D)\equiv A_1(x,D)\equiv0\pmod2
\quad\text{for every root }x;
\tag{7}
\]
in particular all complementary-rank coefficients in (3) also vanish modulo two for all roots and all ranks.

*Proof.* The square-zero relations imply that the coefficient of \(z_D\) in a product comes only from disjoint dimension sets whose union is \(D\). Summing (3) over all ranks gives (6). Odd \(n\) makes \(n+1\) even.

For the even-dimensional example, define the color of a dimension-\(i\) undirected edge with endpoint \(y\) by
\[
c_i(y)=\sum_{j\ne i}y_j\pmod2.
\tag{8}
\]
This is independent of the choice of endpoint because it ignores bit \(i\). Since \(n-1\) is odd, complementing every bit flips the color. Along a full geodesic with root \(x\) and dimension order \(\pi\), the \(k\)-th edge color is
\[
w_k=|x|+x_{\pi_k}+(k-1)\pmod2.
\tag{9}
\]
Thus \(w_k=w_{k+1}\) if and only if \(x_{\pi_k}\ne x_{\pi_{k+1}}\). A monochromatic full geodesic exists from \(x\) if and only if the root bits \(x_{\pi_1},\ldots,x_{\pi_n}\) alternate. For \(n=2m\), this is possible if and only if \(|x|=m\). At such a root, there are \(2(m!)^2\) alternating permutations: two alternating binary patterns, with \(m!\) assignments of dimensions of each bit. The color-complementing reversal-antipode bijection (2) at \(S=D\) splits them evenly between the two colors, giving
\[
\boxed{A_0(x,D)=A_1(x,D)=(m!)^2\ \text{when }|x|=m,}
\tag{10}
\]
and both counts zero at every other root. Since \(m\ge2\), all counts in (10) are even, proving (7). Equation (3) then yields the asserted parity vanishing at every individual rank. \(\square\)

**Implication for adapting Wu–Yang (arXiv:2607.19276, Sections 2 and 5).** The source Freudenthal simplices already describe dimension-simple monotone paths. Wu–Yang's proof obtains its ordinary rook labeling by passing through unrestricted connected components, which forgets whether the connecting monochromatic paths reuse dimensions. Equations (1)–(4) offer a rank-sensitive replacement for the component separation, and (3) supplies a cut-compatible counting law. However, the counterexample (8)–(10) shows that reducing these nonnegative integer path counts modulo two can annihilate every full-geodesic witness at every root. Therefore a modified chain argument cannot use just the mod-two scalar coefficient of the symmetric two-arm enumerator as its existence detector. It must retain dimension-set supports, asymmetric path order data, or finer geometric information before taking a mod-two obstruction.

**Relation to companion work.** The common-terminal two-arm polynomial for boundary tournaments in Article XI also has a symmetric-arm characteristic-two cancellation. Here the rank-resolved convolution (3) and the even-dimensional family (8) are specific to antipodally odd *edge* colorings and use their reversal-plus-antipode bijection. This makes the obstruction to direct binary counting visible on both sides of the intended unification. Neither theorem proves the NORI1 existence conjecture; it identifies a faithful dimension-simple calculation and a limitation of its parity compression.

#### Signed path-orbit incidence and incompatible monochromatic geodesics

Let \(c\) range over legal antipodally odd binary edge colorings of \(Q_n\). Choose one reference edge in each of the \(m=n2^{n-2}\) antipodal orbits of undirected edges, so each coloring is specified by independent binary bits \(z_o\). A full antipodal geodesic \(P\) uses one orbit per direction. Its direction-\(i\) edge in orbit \(o\) has color \(z_o\oplus s_{P,o}\), where \(s_{P,o}\) records which member of that orbit occurs.

For any finite nonempty family \(\mathcal P\) of full geodesics, construct a signed bipartite incidence graph \(B(\mathcal P)\) with left vertices the paths \(P\), right vertices the edge orbits \(o\) they use, and edge label \(s_{P,o}\). Write \(v\) for its number of orbit vertices and \(k\) for its number of connected components.

**Theorem (signed-incidence realization and probability).** The paths in \(\mathcal P\) can all be monochromatic (not necessarily in the same color) in a legal coloring if and only if the binary sum of incidence labels is zero around every cycle of \(B(\mathcal P)\). Moreover,
\[
\boxed{
\mathbb P_c[\text{all }P\in\mathcal P\text{ monochromatic}]
=\begin{cases}
2^{k-v},&\text{all incidence cycles have even label sum},\\
0,&\text{otherwise}.
\end{cases}}\tag{SI1}
\]
In the positive case the satisfying colorings form an affine subspace of \(\mathbb F_2^m\) of dimension \(m-v+k\).

*Proof.* Introduce an unknown color \(t_P\) for each selected path. Its monochromaticity is equivalent to
\[
z_o\oplus t_P=s_{P,o}\quad\text{for every incidence }P-o.
\]
Summing these equations around an incidence cycle yields the stated necessary condition. Conversely, in each connected component of the incidence graph choose one variable freely, then propagate the equations along a spanning tree. The equations on remaining edges hold precisely when all fundamental cycles have even label sum. Thus one binary degree of freedom survives per connected component, and the \(m-v\) unused orbit-color bits are unconstrained. There are \(2^{m-v+k}\) satisfying colorings among the \(2^m\) legal colorings, proving (SI1). \(\square\)

**Corollary (two-path overlap law).** Let two full geodesics \(P,Q\) have \(t\) shared antipodal edge-orbits. If \(t\le1\), their monochromaticity events are independent, with joint probability \(2^{2-2n}\). If \(t\ge2\), write \(d_o=s_{P,o}\oplus s_{Q,o}\) at each common orbit. If the \(d_o\) disagree then the joint probability is zero; if they agree then it equals \(2^{t+1-2n}\). Hence sharing at least two orbits creates either positive correlation or incompatibility. This follows directly by applying (SI1) to the union of two star incidence graphs.

**Theorem (frustrated triple of full geodesics in every dimension).** For any \(n\ge3\), put \(E=(3,4,\ldots,n-1)\) and consider the three full geodesics from the zero vertex with direction orders
\[
\boxed{P=(0,1,2,E),\qquad Q=(0,2,E,1),\qquad R=(1,0,2,E).}\tag{SI2}
\]
Any two of these can be monochromatic simultaneously in some legal coloring, but no legal coloring can make all three monochromatic.

*Proof.* Paths \(P,Q\) use the same first edge, forcing equal monochromatic colors if both succeed. Paths \(P,R\) reach \(e_0\oplus e_1\) after their first two moves, and share the remaining edges (directions \(2,E\)), also forcing equal colors. The final direction-one edge of \(Q\), from \(\mathbf1\oplus e_1\) to \(\mathbf1\), is antipodal to the first edge of \(R\), from \(0\) to \(e_1\). It forces opposite colors. These three requirements contradict one another.

For pairwise realizability, \(P,Q\) have just one common edge orbit (their first edge), and \(Q,R\) have just one (the opposite end edges). Their respective incidence graphs have no cycles. Paths \(P,R\) share all the same edges from direction two onward, and have no further common edge orbit; every resulting incidence cycle has even label sum. Hence each pair is individually realizable by the preceding theorem. \(\square\)

The pairwise probabilities in (SI2) are
\[
\boxed{
\mathbb P(M_PM_Q=1)=2^{2-2n},\quad
\mathbb P(M_PM_R=1)=2^{-n-1},\quad
\mathbb P(M_QM_R=1)=2^{2-2n},\quad
\mathbb P(M_PM_QM_R=1)=0.}\tag{SI3}
\]
The orbit incidence counts were independently verified by a signed disjoint-set algorithm for every \(3\le n\le10\).

This supplies a dimension-uniform signed-graphic description of joint full-geodesic events and a minimal three-path failure of pairwise compatibility. It does not prove unrestricted NORI1, which asks for at least one monochromatic path in each legal coloring.


### Coxeter flag parity and curvature reconstruction

This section links the all-rank Coxeter chain homotopies of Article XIV, Subsections 34–35, to the complete color information recoverable from square curvature. The theorem applies to every unrestricted antipodally odd coloring, for all \(n\ge3\).

Let \(c\) be a binary undirected-edge coloring of \(Q_n\) with \(c(\tau e)=1+c(e)\), and let \(\kappa=\delta c\) be its square-curvature cochain. A rooted dimension-simple complete geodesic flag is \(g=(x;d_0,\ldots,d_{n-1})\). Define its **flag parity**
\[
\boxed{p_c(g)=\sum_{e\in P(g)}c(e)\pmod2.}
\tag{1}
\]
The generator \(s_0\) flips the initial root in direction \(d_0\) while fixing the ordered dimensions, and \(s_i\) (\(1\le i<n\)) swaps \(d_{i-1},d_i\) while preserving the root.

**Theorem 1 (curvature transport at every Coxeter generator).** Let \(F_i(g)\) be the square used in exchanging the adjacent dimensions \(d_{i-1},d_i\), located after crossing the preceding \(i-1\) dimensions. Then
\[
\boxed{p_c(gs_i)+p_c(g)=\kappa(F_i(g)),\qquad 1\le i<n.}
\tag{2}
\]
For the root flip, let
\[
S_j(g)=F_{\{d_0,d_j\}}
\left(x\oplus\bigoplus_{r=1}^{j-1}e_{d_r}\right),
\qquad 1\le j<n.
\tag{3}
\]
These \(n-1\) squares form a strip between the two geodesics after their common initial undirected edge. Then
\[
\boxed{p_c(gs_0)+p_c(g)=1+\sum_{j=1}^{n-1}\kappa(S_j(g)).}
\tag{4}
\]

*Proof.* Interchanging adjacent dimensions replaces the two-edge route through a square by its alternative. Therefore the mod-two sum of the two complete geodesic edge chains is the boundary of that square, proving (2) by Stokes. For (4), the geodesics \(P(g)\) and \(P(gs_0)\) share and cancel their first undirected edge. Their suffixes are parallel paths in the two opposite \(d_0\)-faces. The sum of the strip boundaries equals
\[
\partial\Bigl(\sum_{j=1}^{n-1}S_j(g)\Bigr)
=P(g)+P(gs_0)+e_0+\tau e_0,
\]
where \(e_0\) is the shared initial undirected edge. Evaluating \(c\), the last pair contributes one by antipodal oddness, giving (4). \(\square\)

**Theorem 2 (all-flag parity reconstruction up to one global phase).** Suppose two legal colorings \(c,c'\) have the same square-curvature cochain. Then a single bit \(\epsilon\in\mathbb F_2\), independent of root and dimension order, satisfies
\[
\boxed{p_{c'}(g)=p_c(g)+\epsilon
\quad\text{for every full geodesic flag }g.}
\tag{5}
\]
Both values of \(\epsilon\) occur among legal colorings with that same curvature.

*Proof.* By (2) and (4), the difference \(p_{c'}(g)+p_c(g)\) is constant across every type-B Coxeter generator edge. These generators connect all rooted dimension orders, so the difference is constant. To obtain the opposite phase, add the invariant closed one-cochain \(d^{(a)}\) which is one on all edges of any fixed dimension \(a\), and zero on the other dimensions. This addition preserves antipodal oddness and curvature while flipping the parity of every complete geodesic, because every such geodesic uses \(a\) once. \(\square\)

**Corollary 3 (root-slide monodromy).** For the canonical root-slide rotation
\[
T(x;d_0,\ldots,d_{n-1})
=(x\oplus e_{d_0};d_1,\ldots,d_{n-1},d_0),
\tag{6}
\]
the color word transforms as
\((w_1,\ldots,w_n)\mapsto(w_2,\ldots,w_n,1-w_1)\). Consequently
\[
\boxed{p_c(Tg)=p_c(g)+1,\qquad
p_c(\tau g)=p_c(g)+n\pmod2.}
\tag{7}
\]
In particular \(T^n g=\tau g\) accumulates \(n\) parity flips, agreeing with antipodal complementation of all edge colors.

**Corollary 4 (parity-complete, switch-incomplete information).** The square curvature determines the **entire parity profile across all complete geodesics**, modulo one global binary phase. Yet Subsection 31 proves that every one of the \(2^n\) possible color words can appear on an individually prescribed complete geodesic while curvature is held fixed. Therefore curvature recovers global *word parity differences*, not switch counts or switch positions. The latter require finer color-sensitive incidence data.

**Relevance to the Wu–Yang adaptation.** Equations (2)–(4) supply the generator-level color-parity transport law compatible with the full-rank dimension-simple Coxeter chain geometry, without introducing any auxiliary class of graphs. The higher chain homotopies of Subsection 35 handle the uncolored braid and commuting polygons. The remaining proof problem is to retain ordered red/blue run structure under these homotopies and force cancellation of the primary high-rank second-switch obstruction under a hypothetical NORI1 counterexample. Neither theorem here asserts a monochromatic full-geodesic existence conclusion.

### Relative cycle-extension theorem for projected geodesic colorings

This establishes the full system of **linear compatibility constraints** on any collection of observed cube edges when the square curvature of an unrestricted antipodally odd coloring is fixed. It shows precisely why a single complete dimension-simple geodesic has arbitrary color-word freedom, while overlapping complete paths have constraints from their shared projective incidence cycles.

Fix \(n\ge3\), and write \(Y=\partial[0,1]^n/\tau\cong\mathbb{RP}^{n-1}\), with quotient edge graph \(G=Y^{(1)}\). It has \(V=2^{n-1}\) vertices. Fix a realizable projective square-curvature cocycle \(\eta\) and a legal reference edge coloring \(c_*\) with that curvature. Every other legal coloring with the same curvature is
\[
c_*+\pi^*d,\qquad d\in Z^1(Y;\mathbb F_2).
\tag{1}
\]
The vector space \(Z^1(Y)\) has dimension \(V\): the quotient one-skeleton is connected, so \(\dim B^1(Y)=V-1\), while \(H^1(Y;\mathbb F_2)\cong\mathbb F_2\).

Let \(H\subseteq G\) be an arbitrary edge subgraph. Prescribe a modification \(v\in C^1(H;\mathbb F_2)\) of the coloring of its quotient edges, relative to \(c_*\). Write
\[
\phi_H:H_1(H;\mathbb F_2)\to H_1(Y;\mathbb F_2)\cong\mathbb F_2
\tag{2}
\]
for the inclusion-induced homomorphism. Put \(\epsilon_H=\operatorname{rank}\phi_H\in\{0,1\}\), \(v_H=|V(H)|\), and \(c_H=\text{number of connected components of }H\).

**Theorem 1 (relative cycle-extension criterion).** The prescribed modification \(v\) extends to a legal coloring of the entire cube with the same curvature \(\eta\) **if and only if**
\[
\boxed{\langle v,z\rangle=0
\quad\text{for every }z\in\ker\phi_H.}
\tag{3}
\]
Whenever an extension exists, the number of legal extensions is
\[
\boxed{2^{\,2^{n-1}-v_H+c_H-\epsilon_H}.}
\tag{4}
\]
In particular, no compatibility equations beyond the nullhomologous cycles of the selected edge subgraph are imposed by holding the entire square curvature fixed.

*Proof.* If \(v\) extends, then by (1) it is the restriction of a closed quotient cochain \(d\). A cocycle vanishes on every cycle representing zero homology in \(Y\), proving necessity.

Conversely, let \(u_1\in Z^1(Y)\) represent the nonzero class in \(H^1(Y)\). If \(\phi_H=0\), equation (3) says \(v\) vanishes on every cycle of \(H\), so it is a graph coboundary \(\delta h_H\). If \(\phi_H\ne0\), choose a cycle \(z_0\) with \(\phi_H(z_0)=1\), and put \(\lambda=\langle v,z_0\rangle\). Any cycle \(z\) with \(\phi_H(z)=0\) has evaluation zero by (3). If \(\phi_H(z)=1\), then \(z+z_0\in\ker\phi_H\), so \(\langle v,z\rangle=\lambda\). Thus in either case
\[
v+\lambda u_1|_H
\]
has zero evaluation on every graph cycle and equals \(\delta h_H\) for some vertex function \(h_H\) on \(H\). Extend \(h_H\) arbitrarily to all quotient vertices, define \(d=\delta h+\lambda u_1\), and use (1). This gives an extension.

For counting, restrictions of vertex gauges to \(H\) form its graph coboundary space of dimension \(v_H-c_H\). The class \(u_1\) adds one independent direction precisely if \(\phi_H\ne0\). Hence the image of the restriction map \(Z^1(Y)\to C^1(H)\) has dimension \(v_H-c_H+\epsilon_H\), and its kernel has dimension \(2^{n-1}-v_H+c_H-\epsilon_H\). Each attainable assignment has the number of preimages in (4). \(\square\)

**Corollary 2 (forest freedom).** If \(H\) contains no graph cycles, then every assignment \(v\) to its edges extends, at any fixed realizable curvature. More generally, a projectively nontrivial cycle contributes a freely selectable common phase, whereas a cycle representing zero projective homology imposes one linear compatibility relation (possibly dependent on other such relations).

**Corollary 3 (one complete geodesic).** The projection of a full antipodal dimension-simple geodesic is a simple \(n\)-cycle in \(G\) representing the nonzero class of \(H_1(Y)\). Thus \(v_H=n\), \(c_H=1\), \(\epsilon_H=1\), and the kernel of (2) is zero. All \(2^n\) possible complete edge-color words are feasible at fixed curvature, each in
\[
\boxed{2^{\,2^{n-1}-n}}
\tag{5}
\]
legal colorings, recovering the uniform one-path theorem of Subsection 31.

**Corollary 4 (arbitrary overlapping galleries).** Let \(H\) be the union of the projections of any family of complete dimension-simple antipodal geodesics, identifying their shared quotient edges. A simultaneous prescription of their edge colors is feasible at fixed projective curvature if and only if its differences from a reference coloring vanish on all cycles in \(H\) bounding two-chains in \(Y\). These are all the imposed linear conditions.

**Proof-search relevance.** This is an intrinsic classification of how the original unrestricted cube-edge coloring couples distinct complete geodesics. Square curvature places no restriction on a single chosen full color word, but it enforces compatibility across overlapping paths through their nullhomologous incidence cycles. The theorem therefore identifies a natural color-sensitive ingredient for the higher Coxeter homotopies of Subsections 34–35. It is not itself a proof of the existence of a monochromatic full geodesic; a successful Wu–Yang adaptation must use these path-to-path constraints to control the second-switch obstruction, rather than replacing the coloring by its curvature alone.

### Affine dependence labels and carriers at every word position

A binary word has at most one switch precisely when its signs can be separated by an affine function of position. The complementary case has an explicit positive affine dependence. This supplies a color-sensitive replacement for the signed-second-switch label, with a contractible carrier at every fixed word position.

Let \(s=(s_1,\ldots,s_m)\in\{-1,1\}^m\), \(m\ge3\), and put
\[
L_m=\{z\in\mathbb R^m:\ \sum_i z_i=0,\ \sum_i i z_i=0\}.
\tag{1}
\]
For \(i<j<k\) with \(s_i=s_k=-s_j\), define
\[
r_{ijk}(s)=s_i\bigl((k-j)e_i-(k-i)e_j+(j-i)e_k\bigr),
\]
and set
\[
\boxed{z(s)=\sum_{\substack{i<j<k\\s_i=s_k=-s_j}}r_{ijk}(s).}
\tag{2}
\]

**Theorem 1 (positive affine dependence).** The following are equivalent:

(i) \(s\) has at least two switches.

(ii) There is \(z\in L_m\) such that \(s_i z_i>0\) for every \(i\).

When these conditions hold, (2) is such a vector. Moreover
\[
\boxed{z(-s)=-z(s),\qquad
z(\operatorname{rev}s)=\operatorname{rev}z(s).}
\tag{3}
\]

*Proof.* Each summand in (2) has both sums in (1) equal to zero. Its nonzero entries have the signs of \(s\). If the word has at least three runs, each position belongs to an alternating triple: for a position in an interior run, choose one position in each adjacent run; for a position in the first or last run, choose positions in the next or previous two runs. Thus each entry of (2) receives a contribution with its required sign, and none with the opposite sign. This proves (i) implies (ii).

If the word has at most one switch, an affine function \(f(t)\) has sign \(s_i\) at every integer position \(i\): choose its zero strictly between the two runs, or take a constant function for a constant word. If (ii) held, then
\[
0=\sum_i f(i)z_i>0,
\]
where the equality follows from (1). This proves the converse. Negation gives the first identity in (3). Reversal bijects the triples and exchanges their first and last coefficients, proving the second. \(\square\)

The labels
\[
\ell(s)=z(s)/\|z(s)\|\in S(L_m)\cong S^{m-3}
\tag{4}
\]
therefore retain a nonzero signed entry at every position. The sphere is fixed independently of the source flags.

**Theorem 2 (carriers for partial sign constraints).** Let \(\mathcal S\) be a nonempty family of words, each with at least two switches. Suppose a nonempty set \(A\subseteq[m]\) of positions has fixed signs \(\sigma_i\) throughout \(\mathcal S\). Then
\[
\boxed{C(A,\sigma)=
S(L_m)\cap\{z:\sigma_i z_i\ge0\text{ for all }i\in A\}}
\tag{5}
\]
is nonempty and contractible, and contains all labels (4) of the family. Adding fixed sign constraints shrinks the carrier. Complementing all signs negates it.

*Proof.* Choose any \(s\in\mathcal S\) and put \(v=\ell(s)\). Every constrained entry of \(v\) has strict prescribed sign. Hence \(-v\) does not belong to (5). For \(q\in C(A,\sigma)\), normalized linear interpolation
\[
(q,t)\longmapsto
\frac{(1-t)q+tv}{\|(1-t)q+tv\|}
\]
never vanishes: vanishing would require \(q=-v\). The interpolation remains in the convex sign cone before normalization, giving a contraction. The remaining assertions follow from the defining inequalities. \(\square\)

#### Application to full cube geodesics

Let \(n\ge4\), let \(c(\bar e)=1-c(e)\), and provisionally suppose no monochromatic full antipodal geodesic exists. Every full rooted geodesic has at least two switches: a one-switch edge word becomes monochromatic after sliding its root across the change. Let \(X\cong S^{n-1}\) be the dual type-B Coxeter cellulation. Its vertices are the full rooted geodesics \(g=(x,\pi)\), and central antipodality sends \(g\) to \(\bar g=(\bar x,\pi)\).

For each vertex put
\[
\ell(g)=\ell\bigl((-1)^{w_1(g)},\ldots,(-1)^{w_n(g)}\bigr)
\in S(L_n).
\tag{6}
\]
This label is odd by (3). Let \(X_{\mathrm{pos}}\) be the union of closed dual cells on which at least one edge-color position is constant over all chamber vertices.

**Theorem 3 (extension using every constant position).** \(X_{\mathrm{pos}}\) is an antipodally invariant subcomplex containing the full dual one-skeleton. The labels (6) extend to an odd continuous map
\[
\boxed{F_{\mathrm{pos}}:X_{\mathrm{pos}}\to S^{n-3}}
\tag{7}
\]
using nested contractible carriers.

*Proof.* Constancy is inherited by cell faces, and antipodality complements each fixed sign. For a cell \(D\), use (5) with all its constant positions. Theorem 2 gives nonempty contractible carriers, nested under cell inclusion and negated by antipodality.

Every dual edge has a constant position. Flipping the initial-root bit in the first traversed dimension leaves the first undirected edge unchanged. Swapping adjacent dimensions beyond the first two leaves the first edge unchanged. Swapping the first two dimensions leaves the common suffix from position three onward unchanged. Thus every edge belongs to \(X_{\mathrm{pos}}\).

The prescribed vertex labels lie in their carriers. Extend over cell boundaries inductively inside these carriers, choosing one cell of each free antipodal pair and defining its partner by negation. Nestedness gives compatibility. \(\square\)

The previous signed-second-switch construction supplied position carriers for positions \(1,3,\ldots,n\). Formula (2) supplies them for **all** positions, including position two.

**Corollary 4 (complete positional variation in an obstruction cell).** There is an odd extension over
\[
X_{\mathrm{pos}}\cup X^{(n-3)}.
\]
For every such extension, its mod-two degree obstruction on the \((n-2)\)-cells represents
\[
\boxed{u^{n-2}\ne0\in H^{n-2}(\mathbb RP^{n-1};\mathbb F_2).}
\tag{8}
\]
Consequently some unfilled \((n-2)\)-cell has both colors represented at **every one of the \(n\) word positions**.

*Proof.* The sphere \(S^{n-3}\) is \((n-4)\)-connected, so the map extends equivariantly over the remaining cells through dimension \(n-3\). It is a section of the sphere bundle of \((n-2)\gamma\) on the antipodal quotient, where \(\gamma\) is the covering line bundle. The primary degree obstruction reduces modulo two to
\[
w_{n-2}((n-2)\gamma)=u^{n-2}.
\]
This class is nonzero in \(\mathbb RP^{n-1}\). Every position-constant cell has already been filled, so a degree-contributing cell has no constant position. \(\square\)

#### Higher switch thresholds

The dependence criterion extends to every number of switches. For \(1\le r<m\), define
\[
L_{m,r}=\{z:\sum_i i^q z_i=0,\ 0\le q<r\}.
\]
A sign word has at least \(r\) switches if and only if \(L_{m,r}\) contains a vector with strict sign \(s_i\) in every entry. Indeed, \(r+1\) alternating positions support a signed Vandermonde dependence: on positions \(i_0<\cdots<i_r\), its aligned entries are
\[
\frac{s_{i_j}}{\prod_{\ell\ne j}|i_j-i_\ell|}.
\]
The moment identities follow by comparing the degree-\(r\) coefficients in Lagrange interpolation of polynomials of degree below \(r\). Summing these aligned dependences over all alternating \((r+1)\)-subsequences gives strict prescribed signs everywhere; every position lies in such a subsequence because the word has at least \(r+1\) runs. Conversely, a word with fewer than \(r\) switches is separated by a polynomial of degree below \(r\), contradicting the moment identities. The fixed-position carrier proof then applies in \(S(L_{m,r})\cong S^{m-r-1}\).

The unrestricted NORI1 application uses \(r=2\). The remaining task is to control cells with simultaneous variation at every position. The construction supplies a global color-sensitive labeling and stronger valid fillings; it does not yet annihilate the nonzero obstruction (8).


### Affine dependence labels on Hamilton middle vertices

A boundary-tournament word transforms under reversal by complemented reversal. A word alone may consequently be fixed by opposition. Placing an affine-dependence certificate on the middle vertices of its Hamilton path converts this symmetry into a free antipodal action on one global type-A target. Shared triple incidences then provide compatible carriers.

Let \(V\) have \(n\ge7\) vertices, and let \(b(a,h,c)\in\mathbb F_2\) satisfy only
\[
b(c,h,a)=1-b(a,h,c).
\]
Suppose provisionally that every Hamilton ordering has at least two switches. Write \(m=n-2\). For a Hamilton ordering \(\pi=(v_1,\ldots,v_n)\), put
\[
s_j(\pi)=(-1)^{b(v_j,v_{j+1},v_{j+2})},\qquad 1\le j\le m.
\]
Use the affine-dependence vector
\[
z(s)=\sum_{\substack{i<j<k\\s_i=s_k=-s_j}}
s_i\bigl((k-j)e_i-(k-i)e_j+(j-i)e_k\bigr).
\tag{1}
\]
As proved in the preceding subsection, \(z(s)\ne0\), every entry has strict sign \(s_j\), both \(\sum_jz_j\) and \(\sum_jjz_j\) vanish, and
\[
z(-\operatorname{rev}s)=-\operatorname{rev}z(s).
\tag{2}
\]

Let
\[
W=\{q\in\mathbb R^V:\sum_{v\in V}q_v=0\},\qquad
Z=\{q\in S(W):q\text{ has at least two zero entries}\}.
\tag{3}
\]
Define the flag label
\[
\boxed{\ell(\pi)=
\frac{\sum_{j=1}^{m}z_j(s(\pi))e_{v_{j+1}}}
{\|z(s(\pi))\|}\in Z.}
\tag{4}
\]

**Theorem 1 (faithful odd flag labeling).** The label (4) is defined on every complete Hamilton ordering and satisfies
\[
\boxed{\ell(\pi^{\mathrm{rev}})=-\ell(\pi).}
\tag{5}
\]
Its two zero entries are the first and last vertices of the ordering. Each middle vertex has strict sign equal to the sign of its triple color.

*Proof.* The distinct middle vertices receive nonzero coefficients, and the sum of those coefficients is zero. This proves membership in \(S(W)\), with zeros at the endpoints. Reversal sends the sign word to \(-\operatorname{rev}s\) and reverses the list of middle vertices. Equation (2) therefore negates the vector in (4), proving (5). \(\square\)

The moving placement on middle vertices is part of the original Hamilton ordering. No additional root or restriction on the boundary tournament is introduced.

**Theorem 2 (the global sparse target).** \(Z\) is an antipodally invariant finite cell complex of dimension \(n-4\), and is \((n-5)\)-connected. It admits an odd continuous map to \(S^{n-4}\).

*Proof.* The type-A root polytope is
\[
R=\operatorname{conv}\{e_u-e_v:u\ne v\}\subset W.
\]
Its boundary is given by \(\sum_{q_v>0}q_v=1\). For disjoint nonempty \(A,B\subseteq V\), the face with positive support in \(A\) and negative support in \(B\) is
\[
\Delta_A\times\Delta_B
\]
of dimension \(|A|+|B|-2\). Radial projection identifies the part with at least two zero entries with the \((n-4)\)-skeleton of \(\partial R\cong S^{n-2}\). This proves the dimension assertion. Attaching the remaining cells cannot change homotopy groups through degree \(n-5\); those groups vanish in the sphere. Hence \(Z\) is \((n-5)\)-connected.

Antipodality exchanges the faces indexed by \((A,B)\) and \((B,A)\). On the barycentric subdivision, choose a sign for one face in each antipodal pair and assign opposite signs to its partner. Label a face of dimension \(r\) by its chosen sign times \(e_{r+1}\). Face-chain dimensions strictly increase, so this extends simplicially to the boundary of the \((n-3)\)-crosspolytope, giving the asserted odd map. \(\square\)

#### Carriers from invariant middle-vertex colors

Let \(X\cong S^{n-2}\) be the dual type-A Coxeter cellulation of the simplex flag sphere. Its vertices are Hamilton orders, and its edges exchange adjacent entries. Opposition is reversal of the order.

For a closed dual cell \(D\), let \(A_D\) and \(C_D\) be the sets of vertices that occur first and last, respectively, in its flags. They are disjoint: a proper parabolic residue permutes entries within consecutive position blocks, and its first and last blocks differ. Let
\[
B_D=V\setminus(A_D\cup C_D).
\]
For \(h\in B_D\), its triple color is the color of the unique consecutive triple centered at \(h\) in a given flag. Let \(H_D\subseteq B_D\) consist of those vertices for which this color is constant throughout \(D\), and denote their signs by \(\sigma_h(D)\).

Define
\[
\boxed{
\mathcal C_D=
\bigcup_{\substack{a\in A_D\\c\in C_D}}
\{q\in S(W):q_a=q_c=0,\ 
\sigma_h(D)q_h\ge0\text{ for every }h\in H_D\}.
}
\tag{6}
\]
Every label of \(D\) belongs to this subset of \(Z\). If \(D'\) is a face of \(D\), its endpoint sets shrink, its invariant middle-vertex set grows, and the inherited signs agree. Hence
\[
\mathcal C_{D'}\subseteq\mathcal C_D.
\tag{7}
\]
Opposition negates these carriers.

**Theorem 3 (contractible carriers and the complete one-skeleton).** Carrier (6) is contractible whenever \(H_D\) contains vertices of both colors. It is also contractible for every dual edge. Consequently (4) extends equivariantly over the subcomplex consisting of all dual edges and all closed dual cells with invariant middle vertices of both colors.

*Proof.* Suppose \(h,k\in H_D\) have opposite signs. The vector
\[
v=\sigma_h(D)(e_h-e_k)/\sqrt2
\]
belongs to every piece of the union (6). It satisfies the sign inequalities, with positive prescribed sign at \(h\), and vanishes at every candidate endpoint. Thus \(-v\) is excluded from the carrier. Normalized linear interpolation to \(v\) contracts each piece and, using the same \(v\) for all pieces, the whole union.

Now let \(D\) be an edge. Exchanging adjacent positions affects at most four consecutive triple windows. Since \(m=n-2\ge5\), at least one triple is unchanged, and its middle vertex belongs to \(H_D\). If both colors occur in \(H_D\), the preceding contraction applies.

Otherwise all \(\sigma_h(D)\) equal a sign \(\sigma\). We claim \(B_D\setminus H_D\ne\varnothing\). For an interior exchange, the endpoints stay fixed, so \(B_D\) is the set of all middle vertices. If every such vertex had the same invariant color, both words would be constant. For an exchange involving an endpoint, \(B_D\) comprises all middle vertices except the first or last one, respectively. If all of them had the same invariant color, each complete word would have at most one switch. Both alternatives contradict the hypothesis. This proves the claim.

Choose \(h\in H_D\) and \(k\in B_D\setminus H_D\). The vector \(v=\sigma(e_h-e_k)/\sqrt2\) again belongs to every piece of (6); all other constrained entries are zero. Its negative violates the constraint at \(h\). The same interpolation contracts the carrier.

Having invariant vertices of both colors is inherited by cell faces. Together with the whole one-skeleton, these cells therefore form an opposition-invariant subcomplex. Equations (7) and (5) give a nested equivariant acyclic carrier. Extend the prescribed vertex labels inductively over cells inside their contractible carriers, using antipodal cell pairs. \(\square\)

The edge argument uses the unchanged **ordered triple**, rather than word symmetry alone. It applies to every unrestricted reversal-odd boundary tournament.

**Corollary 4 (a boundary primary obstruction).** The map extends equivariantly over the union of that subcomplex with \(X^{(n-4)}\). After composition with the odd map \(Z\to S^{n-4}\) from Theorem 2, its degree obstruction on the \((n-3)\)-cells represents
\[
\boxed{u^{n-3}\ne0
\in H^{n-3}(\mathbb RP^{n-2};\mathbb F_2).}
\tag{8}
\]
Some degree-contributing cell therefore has no pair of invariant middle vertices with opposite colors.

*Proof.* Connectivity of \(Z\) permits filling every remaining cell through dimension \(n-4\), while retaining the existing carrier map. Composition gives an odd map to \(S^{n-4}\) on this domain. Its primary mod-two obstruction is the top Stiefel-Whitney class of \((n-3)\gamma\), namely \(u^{n-3}\). The quotient of the type-A opposition sphere is \(\mathbb RP^{n-2}\), where this class is nonzero. Every cell with opposite-colored invariant middle vertices is already filled, proving the localization. \(\square\)

**Relation to the cube construction.** Both constructions begin with the same positive affine dependence of a complete color word with at least two switches. Cube antipodality negates its fixed position vector. Boundary reversal negates the vector after placement on the ordering's middle vertices. Both give a fixed free target with dimension below the corresponding complete-path sphere and compatible color-sensitive fillings on source cells. They retain dimension-simple cube geodesics and vertex-simple Hamilton paths in the source.

The remaining obligations are the unfilled primary cells: full positional variation for the cube construction, and the absence of two opposite-colored invariant centers for the boundary construction. The results establish labels and coherent portions of the chain maps for both unrestricted models; neither gives the final cancellation of the primary obstruction.


### Fundamental-circuit intervals and reversal of matroid flat flags

Let \(M\) be a loopless rank-\(n\) matroid with basis \(B\). For \(e\in B\), set \(D_B(e)=\{e\}\); for \(e\notin B\), take \(D_B(e)\) to be the basis elements in the unique circuit of \(B\cup\{e\}\). These sets are nonempty by looplessness. For any ordering \(\pi\) of \(B\), let \(a_\pi(e)\) and \(b_\pi(e)\) be the minimum and maximum positions of the members of \(D_B(e)\), and let \(w_\pi(e)=b_\pi(e)-a_\pi(e)\).

**Theorem (two-end reversal and exchange).** The matroid-Sperner labeling induced by the nested flats \(F_j^\pi=\operatorname{cl}_M\{\pi_1,\ldots,\pi_j\}\) satisfies
\[
\boxed{\ell_\pi(e)=b_\pi(e),\quad
\ell_{\pi^{\rm rev}}(e)=n+1-a_\pi(e),\quad
\ell_\pi(e)+\ell_{\pi^{\rm rev}}(e)=n+1+w_\pi(e).}
\]
For adjacent Coxeter exchange \(\pi'=\pi s_j\),
\[
\boxed{|w_{\pi'}(e)-w_\pi(e)|\le1.}
\]
Under reversal, the support interval \([a_\pi(e),b_\pi(e)]\) becomes \([n+1-b_\pi(e),n+1-a_\pi(e)]\). Scalar reversal complementarity \(\ell_{\pi^{\rm rev}}(e)=n+1-\ell_\pi(e)\) holds precisely when \(D_B(e)\) is a singleton.

*Proof.* For \(A\subseteq B\), one has \(e\in\operatorname{cl}_M(A)\) if and only if \(D_B(e)\subseteq A\), by uniqueness of the fundamental circuit (and independence when \(e\in B\)). Thus \(e\) first enters the nested flat chain at its last support position \(b_\pi(e)\). Reversing the basis order sends each position \(j\) to \(n+1-j\), proving both label identities and interval reflection. An adjacent exchange either swaps two support members, swaps two nonsupport members, or moves a single support member by one position. In the first two cases the interval is unchanged. In the third, at most one interval extreme moves when the support contains at least two elements; if the support is singleton both extremes move together. Hence its width changes by at most one. The width is zero if and only if its support has one member. \(\square\)

**Partition-matroid specialization and NORI caveat.** In the signed-dimension partition matroid \(\bigoplus_i U_{1,2}\), every element has singleton fundamental support, so the scalar Sperner label obeys simple reversal complementarity. In a general matroid, circuits supported on multiple basis elements create the positive reversal defect \(w_\pi(e)\). Complete Boolean-flat flags are indexed by permutations: basis relabeling acts on the left, while flag reversal acts on the right by the longest permutation \(w_0\); they commute. The latter reverses flat ranks and is not a rank-preserving basis permutation. Thus the 2015 matroid-Sperner theorem supplies a useful ordered-flat-chain mechanism but not automatically the antipodal oddness or the compatible monochromatic path data required by the preceding Bockstein chain-transfer criterion.
