# Sparse antipodally odd edge reachability: exact paired-coordinate counts and half-volume obstruction

# Sparse monochromatic reachability without large-volume guarantees

**Theorem (exact reachability count for an antipodally odd edge-colored family).** Let \(n=2m\) and partition the \(n\) directions into \(m\) ordered pairs \((a_t,b_t)\). Give each undirected edge in direction \(a_t\) the color of its fixed \(b_t\)-bit, and each edge in direction \(b_t\) the color of its fixed \(a_t\)-bit:
\[
c(\{z,z\oplus e_{a_t}\})=z_{b_t},\qquad
c(\{z,z\oplus e_{b_t}\})=z_{a_t}.
\]
This is a well-defined antipodally odd two-edge-coloring of \(Q_{2m}\): the partner bit remains fixed across its associated edge and toggles under antipodal complementation.

For root \(x\), let \(A,B,H\) be the numbers of coordinate pairs with starting bits \(00,11,\) and mixed \(01/10\), respectively; \(A+B+H=m\). Let \(R_i(x)\) be the vertices reachable from \(x\) by an edge-color-\(i\) monochromatic *geodesic*, including the zero-length path. Let \(R(x)=R_0(x)\cup R_1(x)\). Then
\[
|R_0(x)|=3^{A+H},\quad
|R_1(x)|=3^{B+H},\quad
|R_0(x)\cap R_1(x)|=2^H,
\]
and therefore
\[
\boxed{|R(x)|=3^{A+H}+3^{B+H}-2^H.}
\]
The maximum over roots is
\[
\boxed{\max_x |R(x)|=2\cdot3^m-2^m,}
\]
and the average over all \(2^{2m}\) roots is \(2(5/2)^m-(3/2)^m\).

For every \(m\ge5\), **no** starting vertex has a monochromatic reachability set comprising more than half the cube:
\[
|R(x)|\le2\cdot3^m-2^m<2^{2m-1}.
\]
Nevertheless, the coloring admits a full **monochromatic antipodal geodesic**.

**Proof.** A geodesic changes each coordinate at most once. In a starting \(00\) pair, an edge-color-0 geodesic may traverse neither coordinate or exactly one of the pair (three choices) but cannot traverse both, since the second move would see partner bit 1; edge-color-1 traversal permits only the empty support. For a starting \(11\) pair the roles of the colors reverse. In a mixed pair \(01/10\), each color separately permits exactly three supports: the empty support, one of the two singleton supports, and the two-coordinate support. The two color-specific local support sets intersect precisely in the empty and full-pair supports (two choices).

Coloring interactions between distinct pairs are independent: colors within a pair depend only on that pair's coordinates, so every selection of independently realizable per-pair support witnesses can be concatenated to a globally monochromatic geodesic of the same selected color. Counting the possible global supports, which correspond bijectively to endpoints, gives the two powers of 3; the intersection has one support choice in each homogeneous pair and two in each mixed pair, giving \(2^H\). Inclusion-exclusion yields the formula.

Converting one homogeneous pair to a mixed pair strictly increases the union size: for \(00\to\text{mixed}\), \(3^{A+H}\) stays fixed, \(3^{B+H}\) is tripled and \(2^H\) doubled, so the net increment is \(2\cdot3^{B+H}-2^H>0\); the \(11\to\text{mixed}\) case is symmetric. Thus the maximum occurs when \(A=B=0,H=m\), giving \(2\cdot3^m-2^m\). For a uniformly random root, pairs are independently \(00,11,01,10\) with probability \(1/4\) each. Taking expectations of \(3^{A+H}\), \(3^{B+H}\), and \(2^H\) gives the stated average by multiplying the respective per-pair expectations \(5/2,5/2,3/2\).

For \(m=5\), \(2\cdot3^5-2^5=454<512=2^{9}\). The ratio \((2\cdot3^m-2^m)/2^{2m-1}=4(3/4)^m-2(1/2)^m\) decreases with \(m\ge5\), proving the strict half-volume inequality for all later \(m\).

For the full antipodal geodesic, take a root whose bits in every pair are mixed. For each pair choose the order of its two moves so that both edges have a preselected common color 0 (or analogously color 1); this is possible because one order traverses both directions in color 0 and the other in color 1. Concatenate the resulting monochromatic two-move paths across all pairs. Each direction is used exactly once, yielding a full monochromatic antipodal geodesic. \(\square\)

**Verified checks.** A direct monotone-subset dynamic program enumerated *all roots* in \(n=2,4,6,8\), with no discrepancies between computed monochromatic reachable-endpoint counts and the formula. The independent \(Q_4\) square-face obstruction example in Item \`nori_edge_reachability_nerve_square_face_nonfilling_and_support_symmetries_20261008\` uses the same family.

**Implication for topological NORI strategy.** A proposed proof based solely on universal largeness \(|R(x)|>2^{n-1}\) (and therefore pigeonhole overlap with its antipode) cannot work. The goal must use geometry, support structure, local face incidence, or equivariant topology of the *actual certified reachability family*, rather than a large-volume bound. This theorem is about the simpler edge-colored proving ground; it is NOT by itself a proof or disproof of ordered-three-face NORI.

### Elevation pass I: antipodal invariance at vanishing density

For a root \(x\) with **all \(m\) coordinate pairs mixed** (one 0 and one 1 in each pair), the same family satisfies the stronger identity
\[
\overline{R(x)}=R(x),
\]
even though
\[
\frac{|R(x)|}{|Q_{2m}|}=\frac{2\cdot3^m-2^m}{4^m}\longrightarrow0
\]
exponentially. Indeed, within a mixed pair the color-0 supports are exactly \(\varnothing,\{b\},\{a,b\}\) after a suitable naming of the directions, whereas the color-1 supports are \(\varnothing,\{a\},\{a,b\}\). Complementation of that two-element coordinate support interchanges these lists. Since distinct pairs contribute independent choices, global support complementation interchanges the full color-0 and color-1 reachable families. Thus every endpoint \(x\oplus S\) monochromatically reachable from this particular root has its physical antipode \(x\oplus(V\setminus S)\) monochromatically reachable as well. This demonstrates a much sharper limitation on purely volumetric fixed-point methods: **complete antipodal closure of a reachable set can coexist with arbitrarily small density**. Its arrangement and certified support involution, not its size, contain the relevant obstruction.
