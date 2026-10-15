# Braid fillings and commuting-square winding in second-switch topology

# Braid cancellation versus commuting-square winding

The second-switch labeling of the type-\(B_n\) Coxeter **chambers**, developed in the preceding subsection, preserves full dimension-simplicity. Under a hypothetical coloring with no monochromatic antipodal geodesic, each complete-geodesic color word has at least two switches, so we may label its chamber
\[
L(x,\pi)=(-1)^{w_1(x,\pi)}e_{s_2(x,\pi)}
\in\{\pm e_2,\ldots,\pm e_{n-1}\},
\tag{1}
\]
where \(s_2\) is the position of the second color change. Adjacent chambers never receive opposite labels. The target crosspolytope boundary is \(S^{n-3}\).

This subsection distinguishes **braid residues**, which always admit a canonical local filling, from **commuting-exchange residues**, which can have nonzero winding in the first dimension where winding is meaningful. It thereby identifies a missing cancellation that a Wu–Yang-style chain map must accommodate.

## A uniform braid-residue filling

Let \(s_1,s_2\) exchange dimensions in positions \(1,2\) and \(2,3\). Their rank-two parabolic residue is the hexagon consisting of all six orderings of the same first three dimensions, with one fixed root \(x\) and the same remaining dimension order.

**Theorem 1 (braid hexagons are nullhomotopic in a contractible carrier).** Suppose \(n\ge4\), and every chamber of a rank-two \(s_1,s_2\)-residue has a color word with at least two switches. Then the piecewise-linear signed-second-switch labeling on its six dual edges extends continuously to the dual two-cell, through a contractible subcomplex of the crosspolytope boundary.

*Proof.* Write the six color words as \(w^{(\pi)}\), indexed by the six permutations of the first three dimensions. Every such path ends its third step at the same cube vertex, then traverses the same remaining dimensions. Thus
\[
w^{(\pi)}_j=u_j\qquad(4\le j\le n)
\tag{2}
\]
for a suffix \(u=(u_4,\ldots,u_n)\) independent of \(\pi\).

If the second switch of \(w^{(\pi)}\) occurs at position \(r\ge3\), then the first \(r\) comparisons contain precisely two changes, so
\[
w^{(\pi)}_1=w^{(\pi)}_{r+1}=u_{r+1}.
\tag{3}
\]
Consequently **for each axis index \(r\ge3\), only one of the two opposite labels \(\pm e_r\) can occur on the hexagon**; its sign is prescribed by \(u_{r+1}\).

Let \(T\) be the set of labels \((-1)^{u_{r+1}}e_r\) with \(r\ge3\) that occur. If \(T\ne\varnothing\), all six labels belong to the simplicial subcomplex
\[
L=S^0_{\{\pm e_2\}}*\Delta(T)
\subseteq\partial\operatorname{Crosspolytope}_{n-2}.
\tag{4}
\]
Here the simplex \(\Delta(T)\) uses one signed vertex for each of the distinct axes \(r\ge3\), and the join is contractible because \(\Delta(T)\) is nonempty and contractible. The edge images also lie in \(L\), since adjacent labels are nonopposite. Hence their circular boundary map extends over a disk in \(L\).

If \(T=\varnothing\), every label is \(+e_2\) or \(-e_2\). Adjacent chambers cannot have opposite labels, so connectedness of the six-cycle forces one constant label on the residue; its boundary image is constant and extends. \(\square\)

The theorem holds at all dimensions and does not assume any restriction beyond the original shared-edge coloring and the availability of the second switch on the six constituent complete paths.

## A commuting exchange with nonzero local winding

**Theorem 2 (nontrivial square obstruction to the canonical one-skeleton map).** In \(Q_4\) there is a valid antipodally odd edge coloring for which the rank-two commuting residue \(\langle s_1,s_3\rangle\) at cube root \(0000\) consists of the four complete-geodesic orders
\[
1234,\quad2134,\quad2143,\quad1243
\tag{5}
\]
with respective words
\[
(1,0,0,1),\quad(0,1,0,1),\quad(0,1,1,0),\quad(1,0,1,0).
\tag{6}
\]
All four words have at least two switches. Their second-switch labels, listed around the square, are
\[
-e_3,\quad+e_2,\quad+e_3,\quad-e_2.
\tag{7}
\]
Consequently the map of the dual square boundary to \(S^1=\partial\operatorname{Crosspolytope}_2\), obtained by mapping each chamber to its label and every dual edge to the shorter crosspolytope edge, has winding number \(+1\). It cannot be extended to this dual two-cell with its prescribed boundary map.

*Proof.* The following eight undirected edges determine the required local coloring; dimension numbers start at \(1\), and the four-bit starting vertices list bits in dimension order:
\[
\begin{array}{c|c|c}
\text{starting vertex}&\text{edge dimension}&\text{color}\\\hline
0000&1&1\\
1000&2&0\\
1100&3&0\\
1110&4&1\\
0000&2&0\\
0100&1&1\\
1100&4&1\\
1101&3&0
\end{array}
\tag{8}
\]
These eight edges lie in distinct antipodal edge orbits. Assign complementary colors to their antipodal mates, and complete the other orbits arbitrarily. Reading the four orders (5) gives the words (6). The first and third words have their second switch at position \(3\), with first bits \(1\) and \(0\), respectively; the second and fourth words have their second switch at position \(2\), with first bits \(0\) and \(1\). This yields (7). Traversing their four crosspolytope edges follows the circle once. \(\square\)

**Scope.** Theorem 2 concerns the forced short-edge interpolation in the second-switch 1-skeleton map. It does **not** contradict NORI1, since the coloring can have favorable complete geodesics elsewhere. Nor does it preclude an altered chain map that sends the same dual edges to longer target chains, or uses additional source faces for cancellation. In higher dimensions, the displayed loop lies in a circle inside a higher-dimensional sphere and is nullhomotopic when the target has dimension at least two.

## Structural lesson for Wu–Yang's chain cancellation

Wu and Yang's Lemmas 5.1 and 5.4 control radial chains by rook-gallery rank and even multiplicity of dependent facets. For the rank-preserving second-switch construction:

* braid residues generated by \(s_1,s_2\) already admit contractible-carrier fillings, with the proof relying on equality of the suffix edges after three steps;
* commuting residues generated by \(s_1,s_3\) can carry a nontrivial boundary cycle for the canonical short-edge chain assignment, despite respecting shared cube edges and full rank;
* therefore a modified chain map cannot be justified solely by verifying braid relations or by a pairwise nonopposition lemma.

The next substantive proof obligation is a **coherent chain correction across commuting exchanges**, whose boundaries cancel over larger Coxeter cells or over a suitably chosen subdivision. This is a direct rank-simple analogue of the cubical face cancellation in Wu–Yang's construction, not a statement about a restricted family of colorings.
