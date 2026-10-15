# Boolean reachability posets and complementary geodesic gluing

# Rooted Boolean reachability restores transitivity without repeated dimensions

Wu–Yang's successful antipodal-path argument (arXiv:2607.19276) uses ordinary monochromatic connected-component labels. Those labels forget dimension support. Unrooted monochromatic shortest-path reachability is not transitive, as shown by the earlier \(Q_3\) example in this Article. However, rooting the Boolean lattice and insisting that every step increase Hamming distance from the root restores transitivity and retains every dimension-simplicity constraint.

Let \(c:E(Q_n)\to\mathbb F_2\) satisfy \(c(\bar e)=1-c(e)\), with red \(0\) and blue \(1\). Fix a cube vertex \(x\), and identify each vertex with its flip set \(S\subseteq[n]\), meaning the vertex is \(x\oplus\mathbf1_S\).

For \(a\in\{0,1\}\), define a relation \(S\preceq_x^a T\) when \(S\subseteq T\) and there exists a color-\(a\) path from \(x\oplus\mathbf1_S\) to \(x\oplus\mathbf1_T\) that traverses only the dimensions in \(T\setminus S\), each once. Permit the length-zero path when \(S=T\).

**Theorem 1 (rooted geodesic orders and antipodal duality).** For each \(a\), the relation \(\preceq_x^a\) is a partial order on \(2^{[n]}\). It obeys
\[
\boxed{
S\preceq_x^0 T\quad\Longleftrightarrow\quad
T^c\preceq_x^1 S^c.
}
\tag{1}
\]
Thus Boolean complementation gives an order-reversing isomorphism between the rooted red and blue reachability posets. Every chain of comparable elements can be realized by concatenating monochromatic paths with disjoint dimension supports.

*Proof.* Reflexivity is allowed by zero-length paths; antisymmetry follows from subset containment. If \(S\preceq_x^a T\preceq_x^a U\), the two path segments respectively use only \(T\setminus S\) and \(U\setminus T\). These dimension sets are disjoint; concatenating yields a color-\(a\) geodesic from the vertex for \(S\) to the vertex for \(U\), proving transitivity and the rank-simplicity assertion.

For (1), apply the cube antipode to a red geodesic from \(x\oplus\mathbf1_S\) to \(x\oplus\mathbf1_T\). It becomes a blue geodesic from the vertex for \(S^c\) to the vertex for \(T^c\). Reverse the path, obtaining a blue geodesic from the vertex for \(T^c\) to the vertex for \(S^c\), using precisely \(T\setminus S=S^c\setminus T^c\). The converse follows by the same operation. \(\square\)

Put
\[
\mathcal R_x=\{S\subseteq[n]:\varnothing\preceq_x^0 S\},
\tag{2}
\]
the flip sets of vertices reachable by a red geodesic beginning at \(x\). This family is accessible: any nonempty member has a one-dimension deletion also in \(\mathcal R_x\), by removing the last step of a witnessing path. It need not be downward closed under arbitrary subset deletion.

**Theorem 2 (complementary reachability is equivalent to a one-switch geodesic).** For each fixed root \(x\), the following statements are equivalent:

(i) There exists a full antipodal geodesic beginning at \(x\) whose word is red followed by blue, with either monochromatic segment allowed to be empty.

(ii) The family \(\mathcal R_x\) contains two complementary subsets:
\[
\boxed{\mathcal R_x\cap\{S^c:S\in\mathcal R_x\}\ne\varnothing.}
\tag{3}
\]

*Proof.* A red-then-blue geodesic has a unique intermediate vertex \(x\oplus\mathbf1_S\) at its color boundary, with \(\varnothing\preceq_x^0 S\) and \(S\preceq_x^1[n]\). By (1), the latter relation is equivalent to \(\varnothing\preceq_x^0 S^c\). This proves (i) implies (ii). Conversely, if \(S,S^c\in\mathcal R_x\), take a red geodesic from \(x\) to the vertex for \(S\), and use (1) to obtain a blue geodesic from that vertex to \(\bar x\). Their support sets are respectively \(S\) and \(S^c\), so concatenation traverses all \(n\) dimensions once and changes color at most once. \(\square\)

**Corollary 3 (a complement-free reachability formulation of NORI1).** An antipodally odd cube-edge coloring has a monochromatic full antipodal geodesic from some root if and only if \(\mathcal R_x\) contains a complementary pair of subsets for some root \(x\).

*Proof.* If a complementary pair exists, Theorem 2 gives a one-switch full geodesic, and root-slide rotation at the change produces a monochromatic full geodesic. Conversely, a red monochromatic full geodesic beginning at \(x\) makes both \(\varnothing\) and \([n]\) members of \(\mathcal R_x\). If only a blue monochromatic full geodesic is initially given, reverse its antipodal translate to obtain a red monochromatic full geodesic beginning at the same root. \(\square\)

Under a hypothetical NORI1 counterexample, each \(\mathcal R_x\) is therefore complement-free and has size at most \(2^{n-1}\). This bound is a consequence of the stronger complement-free property, not a proposed route through average-size estimates.

**Proposition 4 (root-change inclusions).** If the cube edge \(\{x,x^i\}\) is red, where \(x^i=x\oplus e_i\), then for every \(S\subseteq[n]\setminus\{i\}\),
\[
S\in\mathcal R_x\quad\Longrightarrow\quad S\cup\{i\}\in\mathcal R_{x^i},
\]
\[
S\in\mathcal R_{x^i}\quad\Longrightarrow\quad S\cup\{i\}\in\mathcal R_x.
\tag{4}
\]
If the given edge is blue, the corresponding implications hold for the red families at the antipodal vertices \(\bar x,\overline{x^i}\).

*Proof.* A red path from \(x\) to the vertex for \(S\) avoids dimension \(i\). Prepend the red edge \(x^i\to x\); the result is a red geodesic from \(x^i\) using dimensions \(S\cup\{i\}\). This proves the first implication. Exchange the roots to prove the second. If the original edge is blue, its antipodal mate is red. \(\square\)

**Implication for Wu–Yang's chain map.** The replacement for ordinary red components need not be another equivalence relation. The rooted red reachability **orders** have associative dimension-simple path concatenation; the red and blue orders are antipodally dual by (1); and across each cube edge one of the paired red reachability families obeys the rank-preserving transport law (4). These are intrinsic local incidences of the unrestricted cube coloring, without any arbitrary choice of path galleries.

The outstanding theorem is to construct from the family \((\preceq_x^0,\preceq_x^1)_x\) an equivariant augmentation-preserving chain map to a target of sufficiently small dimension, or to derive the complementary-pair conclusion through a topological intersection principle. Ordinary rook labels use equality of component indices; the relations (4) provide support-preserving inclusions instead. No full chain map is established here.
