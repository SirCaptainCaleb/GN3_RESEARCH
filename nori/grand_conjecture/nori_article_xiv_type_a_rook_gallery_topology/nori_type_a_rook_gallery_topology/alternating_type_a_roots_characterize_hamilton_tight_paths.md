# Alternating type-A roots characterize Hamilton tight paths

# Alternating type-A roots characterize Hamilton tight paths

## Ordered-pair geometry and an orientation-sensitive coloring

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

## A simple-root characterization of complete tight paths

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

## Coxeter chambers and the chain-level antipodal connection

A Hamilton ordering \((v_1,\ldots,v_n)\) determines the type-\(A_{n-1}\) Weyl chamber
\[
\{z\in W_V:z_{v_1}\ge z_{v_2}\ge\cdots\ge z_{v_n}\}.
\]
Its consecutive simple roots are the \(\alpha_i\) in the forward proof above. Thus the boundary problem is a colored *chamber-selection problem* in which successive alternating-sign simple roots satisfy (7) and their connecting rook arcs have at most one bit switch. The root-basis condition and nonrepetition of original symbols are built into the type-A chamber rather than asserted for an arbitrary auxiliary walk.

The link with Wu–Yang's chain-level Borsuk–Ulam proof of Norine's antipodal-coloring conjecture is structural: their rook labels lie in the same \(\Omega_V\), their involution interchanges the ordered-pair entries, and they send \((a,b)\) to the same root \(e_a-e_b\) in the sphere \(S(W_V)\). Their use of Freudenthal monotone galleries and chain-valued root cones supplies a relevant technique for topological selection. Their published conclusion, however, concerns a monochromatic antipodal path that need not be a geodesic. A failure of NORI1's monochromatic *geodesic* conclusion does not imply their off-diagonal component-pair rook labeling exists: a monochromatic non-geodesic path may still join antipodes. Furthermore a Wu–Yang rook gallery need not have Gram matrix (7), alternating rook moves, or a low-switch arc word.

This delineates the missing work. A common proof would have to construct from the original cube-edge coloring and from arbitrary reversal-odd boundary tournaments a *faithful* gallery carrier; establish an equivariant selection or chain obstruction on that carrier; and extract an entire gallery obeying its corresponding spanning-path conditions and at most one switch. The type-A criterion is intrinsic for boundary tournaments, but no claim is made that NORI1 itself has a matching type-A basis geometry. Neither a general Borsuk–Ulam zero nor unrestricted rook adjacency forces the Gram pattern (7).

**Source and relation.** Wu and Yang, *A Chain-Level Borsuk–Ulam Obstruction Proof of Norine's Antipodal-Coloring Conjecture*, arXiv:2607.19276 (2026), recorded in Toolkit entry \`literature_wu_yang_norine_chain_level_borsuk_ulam\`. Companion Article XIV research note: \`note_05a0824513a6316fac1be336\`. Earlier undirected ordered-pair reduction and its failure to preserve directed Hamilton witnesses: \`note_ordered_pair_antipodal_graph_bridge_and_decoding_obstruction_20261011\`.
