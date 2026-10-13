# Canonical resource recovery and the basis-polarity obstruction for partition matroid unification

- Stable ID: note_90fc247db08fb0d2da5cba30
- Author: independent research session
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: structural-obstruction, matroid, polarization, basis-graph
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7130_4
- Updated session: session_nori_r7130_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

## Intrinsic recovery and the location of polarization

Let \(M_{\rm cub}=\bigoplus_{i=1}^n U_{1,2}\), \(n\ge3\), and \(M_{\rm bd}=U_{2,n}\), \(n\ge5\). Write \(\Gamma(M)\) for the basis-exchange graph.

**Proposition 1 (canonical resource recovery).** The unlabelled graph \(\Gamma(M_{\rm cub})=Q_n\) canonically determines its \(n\) coordinate resource classes as the transitive closures of opposite-edge relations in graph four-cycles. The unlabelled graph \(\Gamma(M_{\rm bd})=J(n,2)\) canonically determines the original \(n\) resources as its maximal cliques of size at least four: precisely the stars
\[
S_a=\{\{a,b\}:b\ne a\},\qquad a\in[n].
\]
Every vertex of \(J(n,2)\) belongs to precisely two such cliques.

*Proof.* Opposite sides of every cubical square change the same coordinate. Holding one coordinate fixed while changing any others by squares shows that its full edge direction class is connected by opposite-edge moves; these are the complete classes. In \(J(n,2)\), a family of pairwise intersecting two-subsets either shares one common symbol or is contained in the three two-subsets of a three-element set. Hence maximal cliques with at least four vertices are precisely the \(S_a\), and a pair \(\{a,b\}\) belongs precisely to \(S_a,S_b\). \(\square\)

**Proposition 2 (sharp basis-level polarity obstruction).** For \(n\ge3\), the nonidentity central element of \(\operatorname{Aut}(M_{\rm cub})\cong C_2^n\rtimes S_n\) is simultaneous exchange of the two members of every parallel class; on bases it is the free antipodal involution. For \(n\ge5\), every \(\operatorname{Aut}(U_{2,n})\)-equivariant map
\[
f:\mathcal B(U_{2,n})\longrightarrow\mathcal B(U_{2,n})
\]
is the identity. In particular no nontrivial canonical basis involution exists for \(U_{2,n}\), even if one allows a general equivariant self-map rather than an automorphism.

*Proof.* The center of \(C_2^n\rtimes S_n\), for \(n\ge3\), consists of the identity and simultaneous translation by \((1,\dots,1)\): a central translation must be fixed under coordinate permutations, and no nontrivial coordinate permutation centralizes all individual bit flips. For \(U_{2,n}\), \(\operatorname{Aut}(U_{2,n})=S_n\). Let \(B=\{1,2\}\). Its stabilizer \(S_{\{1,2\}}\times S_{\{3,\dots,n\}}\) fixes only the two-subset \(B\) when \(n\ge5\). Equivariance forces \(f(B)\) to be fixed by this stabilizer, hence \(f(B)=B\). Transitivity of \(S_n\) on all bases forces \(f\) to be the identity everywhere. \(\square\)

**Proposition 3 (both unrestricted coloring algebras as graph orientations).** After choosing a representative \(0,1\) for each two-element parallel class of \(M_{\rm cub}\), NORI1 antipodally odd edge colorings of \(Q_n\) are in bijection with all orientations of the folded graph \(F_n=Q_n/\tau\). Explicitly, for a directed edge of the folded graph represented by \(x\to x\oplus e_i\), put
\[
o_c([x]\to[x\oplus e_i])=c(\{x,x\oplus e_i\})\oplus x_i.
\]
The value is independent of the chosen antipodal lift and satisfies \(o_c(\mathrm{reverse\ arc})=1\oplus o_c(\mathrm{arc})\). Conversely \(c(e)=o_c(\mathrm{arc})\oplus x_i\) recovers every antipodally odd coloring. Changing the \(0/1\) gauge of parallel classes reverses corresponding direction classes in this orientation dictionary.

Similarly, ordinary reversal-odd boundary 3-tournaments are in bijection with all orientations of \(J(n,2)=\Gamma(U_{2,n})\), by assigning the directed edge \(\{a,b\}\to\{b,c\}\) the bit \(b(a,b,c)\). The reverse directed edge is indexed by \((c,b,a)\), and every edge of \(J(n,2)\) has a unique middle symbol, proving the bijection.

Under these dictionaries the respective witness predicates are:
(i) a direction-rainbow length-\(n\) closed walk in \(F_n\), with lift \(x=x_0,x_1,\ldots,x_n=\tau x\), satisfying \(o_c([x_{j-1}]\to[x_j])\oplus x_{\pi_j}=\epsilon\) for every used coordinate \(\pi_j\);
(ii) a path of basis states \(\{v_1,v_2\},\{v_2,v_3\},\ldots\), arising from pairwise distinct original vertices, on whose directed steps the tournament orientation bits are all \(\epsilon\).
The first is a prescribed signed-orientation condition, the second an ordinary directed-path condition with a resource-simple language.

**Consequence.** A unification using a *canonical free involution on bases* excludes all \(U_{2,n}\) for \(n\ge5\). A common intrinsically polarized class must place the involution at the covering-flag, ordered-terminal, or exchange-transition level. Neither intrinsic recovery of resource classes nor unrestricted orientations by itself proves the sought path-existence statements. In particular, these propositions supply a necessary architectural restriction, rather than a new universal existence conjecture.

**Proposition 4 (neither full-witness family is a matroid basis system).** For every \(n\ge3\), the edge sets of all full antipodal geodesics of \(Q_n\) are not the bases of any matroid on \(E(Q_n)\). For every \(n\ge4\), the edge sets of all Hamiltonian paths of \(K_n\) are not the bases of any matroid on \(E(K_n)\). Consequently, the two witness classes cannot both be treated as bases of their respective single ordinary matroids on the natural path-transition resources; independent-set intersections or a path complex retain additional necessary structure.

*Proof.* For \(n=3\), the two cube geodesics
\[
P=(000,100,110,111),\qquad Q=(010,011,001,101)
\]
are antipodal geodesics with vertex-disjoint supports. For every \(n>3\), append coordinates \(4,\dots,n\), initially all zero, and after traversing the respective displayed three-step path flip the extra coordinates one by one; the resulting two full antipodal geodesics still have disjoint vertex supports, since their projections on the first three coordinates lie in the disjoint vertex sets of \(P,Q\). For any edge \(e\in E(P)\) and any \(f\in E(Q)\), the graph on the edges \((E(P)\setminus\{e\})\cup\{f\}\) is disconnected: the endpoints of \(f\) belong to none of the retained \(P\)-edges. Hence no replacement \(f\) satisfies the matroid basis-exchange axiom. The boundary statement follows from the separate basis-exchange counterexample for Hamiltonian paths in Article XI's Subsection "Three-matroid Hamiltonian galleries and bounded-cost block reversal": exchanging the edge \(01\) from \((0,1,2,3,\dots,n-1)\) toward \((0,2,1,3,\dots,n-1)\) cannot produce a Hamiltonian path with either available replacement \(02\) or \(13\). \(\square\)

The cube obstruction is intrinsically all-dimensional and uses the complete legal geodesic family, rather than a counterexample induced by coloring.

**Corollary 5 (intrinsic recovery of the common terminal-comparison theorem).** From the unlabelled basis graph \(\Gamma(M_{\rm cub})\), construct \(G_{\rm cub}=\Gamma(M_{\rm cub})\) and label edges by their recovered square-opposite direction classes. From the unlabelled basis graph \(\Gamma(U_{2,n})\), construct \(G_{\rm bd}\) with one vertex for each recovered large star clique \(S_a\) and one edge between \(S_a,S_b\) for their unique shared basis \(\{a,b\}\). Then \(G_{\rm bd}\cong K_n\), and its edges label themselves. Both canonical models thus yield *properly edge-labelled graphs with local tournaments*, the common class of Article VII's rainbow terminal-edge theorem:
\[
L_{\rm cub}-1\ge \frac{1+\sqrt{1+4n}}4,\qquad
L_{\rm bd}\ge 1+\sqrt{\frac{n-1}{2}}.
\]
In the cube, sort incident edges by their given two colors, breaking ties, to define local transitive comparison tournaments. The resulting admissible paths have distinct coordinate directions and weakly increasing color words, hence at most one switch. In the boundary model, the arbitrary reversal-odd triple values orient every local star tournament, and admissible paths are precisely monochromatic vertex-simple tight paths. The cited dimension-independent terminal-edge theorem proves both inequalities.

This is a common *existence proof mechanism*, with an intrinsic resource-graph extraction from each basis graph. Its cube conclusion is much weaker than NORI1: it makes no use of antipodal oddness and cannot by itself force a monochromatic full antipodal geodesic. Indeed, arbitrary (not reversal-odd) cube colorings constant by coordinate, with distinct colors on two coordinate classes, have no monochromatic full geodesic, while their locally ordered graph still satisfies the terminal theorem. Thus any proposed common strengthening that settles NORI1 needs a global antipodal/dual-path condition in addition to the local-comparison and independent-resource axioms.
