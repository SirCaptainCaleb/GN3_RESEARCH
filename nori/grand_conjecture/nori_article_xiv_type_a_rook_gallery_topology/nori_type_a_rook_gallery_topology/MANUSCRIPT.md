## Type-A rook galleries and antipodal chain topology

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
