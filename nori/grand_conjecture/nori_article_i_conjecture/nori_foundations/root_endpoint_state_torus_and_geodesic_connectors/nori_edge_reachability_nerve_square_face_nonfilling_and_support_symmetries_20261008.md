# Reachability nerve: universal square triangles but unfilled affine Q4 tetrahedron; root-support involutions

# The reachability nerve has universal triangle boundaries but not universal square filling

Let \(Q_n=\{0,1\}^n\) have any binary edge coloring. Define
\[
R(x)=\{z:\text{some monochromatic geodesic of either color joins }x\text{ to }z\},
\]
including \(z=x\). The **reachability nerve** \(N_R\) is the abstract simplicial complex on root vertices \(x\in Q_n\) in which a set of roots \(\sigma\) is a simplex exactly when \(\bigcap_{x\in\sigma}R(x)\ne\varnothing\).

**Lemma 1 (universal closed-star simplices).** For every root \(v\), the set consisting of \(v\) and its \(n\) cube neighbors is a simplex of \(N_R\), independently of coloring.

**Proof.** Every member of this set reaches \(v\) by a path of length at most one, vacuously monochromatic. \(\square\)

**Lemma 2 (all square triples, but potentially no square quadruple).** For each geometric two-coordinate square with four corners \(v_1,v_2,v_3,v_4\), any three of its corners have a common reachable vertex, hence span a two-simplex of \(N_R\). Their full four-point set need not be a simplex, even when the edge coloring is antipodally odd and affine in its exterior bits. Thus the induced nerve on the four corners may be exactly \(\partial\Delta^3\), a combinatorial two-sphere, rather than a filled tetrahedron.

**Proof of the universal assertion.** Any three vertices of a square comprise the center and the two leaves of a length-two path. The center belongs to the reachability sets of all three vertices, using only empty and one-edge paths.

**Explicit antipodally odd affine counterexample to full filling.** Take \(Q_4\), with coordinate indices \(0,1,2,3\). Give the edge of direction \(i\) through vertex \(x\) color
\[
c_0(x)=x_1,\qquad
c_1(x)=x_0,\qquad
c_2(x)=x_3,\qquad
c_3(x)=x_2.
\tag{1}
\]
Each color depends only on coordinates exterior to its edge, so it is well-defined and affine. Complementing all vertex bits toggles each edge color: \(c(\bar e)=1\oplus c(e)\).

Identify each cube vertex with the integer having bit \(i\) in coordinate \(i\). Consider the two-coordinate face with free coordinates \(0,2\) and fixed bits \(x_1=1,x_3=0\). Its four roots are
\[
F=\{2,3,6,7\}.
\]
At root \(3=(1,1,0,0)\), the direction-0 and direction-1 incident edges both have color 1, whereas the direction-2 and direction-3 edges both have color 0. Two different directions from the same pair \(\{0,1\}\) or \(\{2,3\}\) cannot be traversed with one color because flipping either coordinate switches the color of the other. Nor can a path use directions from *different* pairs monochromatically, since initially one pair has color 1 and the other color 0, and crossing one pair does not affect the other pair's edge colors. Consequently
\[
R(3)=\{1,2,3,7,11\}.
\tag{2}
\]

We now successively eliminate these possible common targets:
- Neither \(7\) nor \(11\) lies in \(R(2)\): reaching either from \(2\) requires exactly two directions, one from each of the two coordinate pairs, whose edge colors are 1 and 0 in either order. Thus \(R(2)\cap R(3)\subseteq\{1,2,3\}\).
- The vertex \(3\) does not belong to \(R(6)\): the required two directions are \(0,2\), whose colors from root \(6\) are respectively 1 and 0, independently of their order. Therefore \(R(2)\cap R(3)\cap R(6)\subseteq\{1,2\}\).
- Neither \(1\) nor \(2\) belongs to \(R(7)\): the coordinate differences from root \(7\) are respectively \(\{1,2\}\) and \(\{0,2\}\), with edge colors 1 and 0 in either order.

It follows that
\[
R(2)\cap R(3)\cap R(6)\cap R(7)=\varnothing.
\tag{3}
\]
The universal triple-intersection lemma still guarantees all four triangular faces, so the induced nerve on \(F\) is precisely the boundary of a tetrahedron. \(\square\)

**Lemma 3 (the correct antipodal involution preserves supports).** For an antipodally odd edge-colored cube, let
\[
\mathcal K=\{(x,S):x\oplus S\in R(x)\}\subseteq Q_n\times\{0,1\}^n,
\]
writing \(S\) for the support of the root-to-target difference. Then \(\mathcal K\) is invariant under the commuting involutions
\[
A(x,S)=(\bar x,S),\qquad E(x,S)=(x\oplus S,S).
\tag{4}
\]
Here \(A\) complements the entire monochromatic geodesic and flips its color, while \(E\) reverses the geodesic and preserves its color. In contrast, the support-complement transformation
\[
T(x,S)=(x,\bar S)
\tag{5}
\]
is **not** a guaranteed symmetry. The edge-colored grand conjecture is exactly \(\mathcal K\cap T(\mathcal K)\ne\varnothing\).

**Proof.** Antipodal complementation of a monochromatic geodesic \(x\leadsto x\oplus S\) gives a monochromatic geodesic \(\bar x\leadsto\bar x\oplus S\); reversing its direction gives \(x\oplus S\leadsto x\). These are precisely \(A\) and \(E\); XOR operations commute. The criterion \(\mathcal K\cap T(\mathcal K)\ne\varnothing\) says there is a root \(x\) having monochromatic geodesics to the two antipodal vertices \(x\oplus S\) and \(x\oplus\bar S\). This is the exact known extraction condition. In the example above, root 3 reaches only supports of size 0 or 1, so \((3,\{0\})\in\mathcal K\) while \((3,\{1,2,3\})\notin\mathcal K\): \(T\) is not a symmetry. \(\square\)

**Topological consequence and limitation.** The simplicial complex \(N_R\) automatically contains full simplices on the closed stars of Q_n and the complete triangular boundary of each square's four-corner tetrahedron. It does **not** automatically contain a tetrahedron for each cubical two-face, so a proposed cubical KKM/Sperner carrier based on facewise intersections requires an additional geometric or reachability argument. More fundamentally, the genuine antipodal symmetry of the root-support witness complex is \(A:(x,S)\mapsto(\bar x,S)\), whereas closure requires a collision under \(T:(x,S)\mapsto(x,\bar S)\). Standard Tucker/Borsuk-Ulam cannot be invoked by falsely identifying these two actions. An actual theorem must exploit the reachability-specific path incidence to couple them, or construct a different equivariant carrier with proved extraction.

This is a dimension-independent exact obstruction to an overly strong local nerve hypothesis. It neither proves nor refutes the grand conjecture.
