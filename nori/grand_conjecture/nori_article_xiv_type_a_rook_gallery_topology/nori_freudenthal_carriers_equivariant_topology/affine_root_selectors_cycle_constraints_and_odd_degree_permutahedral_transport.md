# Affine root selectors, cycle constraints, and odd-degree permutahedral transport

# Affine roots, cycle constraints, and odd-degree flag transport

Let \(\sigma\in S_n\) be a derangement and \(a_i\in\mathbb F_2\). Color cube edges by \(c(\{x,x\oplus e_i\})=x_{\sigma(i)}\oplus a_i\). This is independent of the chosen edge endpoint because \(\sigma(i)\ne i\), and it is antipodally odd.

**Theorem 1 (unique root selector and exchange).** Given a full dimension order \(\pi\) and a bit \(b\), there is a unique root \(x_\pi^{(b)}\) making every edge of the full geodesic along \(\pi\) have color \(b\):
\[
\boxed{(x_\pi^{(b)})_{\sigma(i)}
=b\oplus a_i\oplus[\sigma(i)\text{ precedes }i\text{ in }\pi].}
\tag{1}
\]
One has \(x_\pi^{(1)}=\bar x_\pi^{(0)}\) and \(x_{\pi^{rev}}^{(b)}=\bar x_\pi^{(b)}\). If \(\pi'\) swaps consecutive directions \(i,j\), the selected roots can differ only at bit \(j\) if \(\sigma(i)=j\), or bit \(i\) if \(\sigma(j)=i\). If \(\sigma\) has no two-cycle, their Hamming distance is at most one.

*Proof.* By the time the path uses direction \(i\), bit \(\sigma(i)\) has changed from its starting value if and only if \(\sigma(i)\) occurred earlier. Setting its resulting color equal to \(b\) yields (1), prescribing each starting bit once because \(\sigma\) is a permutation. Reversal negates each precedence indicator, and adjacent exchange changes only the relative order of the swapped symbols. \(\square\)

**Theorem 2 (feasible roots and counting).** A fixed root \(x\) admits a monochromatic full geodesic if and only if the binary sequence \((x_{\sigma(i)}\oplus a_i)_{i\in C}\) is nonconstant on every cycle \(C\) of \(\sigma\). Such a root admits geodesics of *both* colors. If the cycle lengths are \(\ell_1,\ldots,\ell_s\), the number of feasible roots is
\[
\boxed{\prod_{t=1}^s(2^{\ell_t}-2).}
\tag{2}
\]
Across all roots there are \(n!\) ordered monochromatic geodesics of either fixed color.

*Proof.* Equation (1) imposes ordering comparisons between \(i\) and \(\sigma(i)\). Within each permutation cycle, these comparisons form an orientation of its cyclic graph. They admit a total order if and only if there is no directed circuit, which occurs if and only if the comparison bits are not all equal. Changing the target color reverses every comparison, preserving the absence of directed circuits. The root-bit assignment to each cycle's comparison bits is bijective, and two constant patterns are excluded among its \(2^{\ell_t}\) patterns. The last assertion follows from uniqueness of the root for each \(\pi,b\). \(\square\)

For two three-cycles and zero offsets, 36 of the 64 roots support full monochromatic geodesics, and each such root has \(\binom63=20\) orders of each color. Nevertheless root \(0^6\) supports none, as in the locally obstructed two-block Grassmannian example of Article XV.

Now suppose \(\sigma\) is one \(n\)-cycle, \(n\ge3\), and all offsets vanish. Write \(x_\pi=x_\pi^{(0)}\). Let \(P_n\) be the centered permutahedron in \(W=\{z\in\mathbb R^n:\sum z_i=0\}\), with vertex \(u_\pi=\sum_j((n+1)/2-j)e_{\pi_j}\). Its boundary is \(S^{n-2}\), with central involution taking \(\pi\) to its reversed order.

**Theorem 3 (equivariant odd-degree root carrier).** The vertex labels \(u_\pi\mapsto x_\pi\) have a canonical antipodal piecewise-linear extension
\[
\boxed{F_\sigma:\partial P_n\longrightarrow
\partial[0,1]^n\setminus\{0^n,1^n\}.}
\tag{3}
\]
After equivariant retraction of its target onto \(S^{n-2}\), this is an antipodal sphere map of odd mod-two degree.

*Proof.* A nonempty proper subset \(S\subset[n]\) indexes a permutahedral facet whose vertex orders put all of \(S\) before its complement. A single \(n\)-cycle has no proper invariant nonempty subset, so some \(i\in S\) satisfies \(\sigma(i)\notin S\). In every refining order, \(i\) precedes \(\sigma(i)\). Equation (1) thus makes bit \(\sigma(i)\) of every corresponding root zero. Hence all root labels on that facet lie in one fixed face of the cube.

On the barycentric subdivision of \(\partial P_n\), send each face barycenter to the arithmetic mean of the root labels of its vertices, then extend affinely across the nested-face simplices. Every simplex lies in a permutahedral facet, where the same cube bit stays zero. This gives the cubical-boundary property.

No root label can be \(0^n\), since this would require \(i\) before \(\sigma(i)\) all around the directed cycle; no label can be \(1^n\) for the reverse reason. Convex combinations cannot equal either extreme cube corner unless every contributing label does. Thus the image avoids the two corners.

By Theorem 1, reversing an order complements its root; averaging over antipodally paired faces makes the map equivariant. Central radial projection identifies the cube boundary with \(S^{n-1}\), and removing the two opposite vertices permits an equivariant retraction to its equatorial \(S^{n-2}\). The resulting map is antipodal between two spheres of dimension \(n-2\). Its quotient preserves the degree-one class and its top cup power in \(H^*(\mathbb RP^{n-2};\mathbb F_2)\), proving odd degree. \(\square\)

**Theorem 4 (multi-cycle obstruction to the same face carrier).** If \(\sigma\) has at least two cycles, choose \(S\) to be a nonempty proper union of full cycles. The facet of orders putting \(S\) first has root labels whose average is the cube center \(\frac12\mathbf1\). Consequently the face-barycenter construction above does not land in the cube boundary.

*Proof.* Every pair \(i,\sigma(i)\) lies within one of the two ordered blocks. As the orders within these blocks range uniformly, either element precedes the other half the time. Formula (1) therefore gives mean root bit \(1/2\) for every bit. The facet barycenter is mapped to the cube center. \(\square\)

**Research interpretation.** An indecomposable cyclic dependency gives an antipodally equivariant, odd-degree, globally coherent selector of monochromatic roots on the type-A flag sphere, with local changes of at most one cube direction. The local Grassmannian obstruction at root zero is resolved in this family through root mobility, not by filling that obstructed top cell. The construction is not extended to arbitrary odd edge colorings and does not settle NORI1.

## The graphical-zonotope refinement: integral degree one and a sharp connectedness criterion

The antipodal root-carrier map above has a stronger realization through the graphical zonotope of the dependency cycle. The following general theorem applies to any simple graph \(G\) on the dimension set \([n]\), \(n\ge3\), and does not presume that its graphic matroid is connected.

For each edge \(\{i,j\}\), take \(i<j\), and write \(w_{ij}=e_i-e_j\in W=\{z\in\mathbb R^n:\sum z_i=0\}\). Let \(P_n\subset W\) be the centered permutahedron, or equivalently the graphical zonotope of \(K_n\):
\[
P_n=\sum_{\{i,j\}\in E(K_n)}[-w_{ij}/2,w_{ij}/2].
\tag{9}
\]
For an order \(\pi\), put \(\epsilon_{ij}(\pi)=1\) if \(i\) precedes \(j\), and \(-1\) otherwise. Its permutahedral vertex is
\[
u_\pi=\frac12\sum_{E(K_n)}\epsilon_{ij}(\pi)w_{ij}.
\]
For a graph \(G\), define the graphical-zonotope vertex label
\[
z_G(\pi)=\frac12\sum_{E(G)}\epsilon_{ij}(\pi)w_{ij},\qquad
Z_G=\sum_{E(G)}[-w_{ij}/2,w_{ij}/2].
\tag{10}
\]
The label depends only on the orientation of the edges of \(G\) induced by the total order.

**Theorem 5 (connected graphical-zonotope map has integral degree \(+1\)).** Let \(G\) be a connected graph on \([n]\). Map each nonempty face barycenter of \(\partial P_n\) to the arithmetic mean of the \(z_G(\pi)\) over its vertices, and interpolate affinely over the barycentric subdivision. The resulting map
\[
\boxed{\mathcal F_G:\partial P_n\longrightarrow\partial Z_G}
\tag{11}
\]
is continuous, commutes with central inversion, and, after identifying both polytope boundaries with the unit sphere of \(W\) by radial projection, has **integer Brouwer degree \(+1\)**.

*Proof.* For \(t\in[0,1]\), define
\[
Z_t=Z_G+t Z_{K_n\setminus G},\qquad
z_t(\pi)=z_G(\pi)+t z_{K_n\setminus G}(\pi).
\tag{12}
\]
When \(t=1\), \(Z_t=P_n\) and \(z_t(\pi)=u_\pi\). When \(t=0\), these are \(Z_G,z_G(\pi)\). Since \(G\) is connected, its edge-difference vectors span \(W\), so every \(Z_t\) is a centrally symmetric, full-dimensional convex body with the origin in its interior.

A facet \(F_S\) of \(P_n\) is indexed by a nonempty proper \(S\subset[n]\), and its vertices are the orders putting \(S\) before its complement. For every such order,
\[
\sum_{i\in S}z_t(\pi)_i
=\frac12\Bigl(|\partial_G S|+t|\partial_{K_n\setminus G}S|\Bigr),
\tag{13}
\]
the maximum of the same linear functional on \(Z_t\). Connectedness implies \(|\partial_G S|>0\). Therefore all vertex images of \(F_S\) belong to one exposed proper face of \(Z_t\). The barycentric interpolation maps every subdivision simplex in \(F_S\) into that face, giving a continuous map \(\mathcal F_t:\partial P_n\to\partial Z_t\) for all \(t\in[0,1]\). Every image avoids the origin.

At \(t=1\), every source face barycenter maps to the arithmetic mean of that same face's vertices, namely the chosen source barycenter. Thus \(\mathcal F_1\) is the identity on \(\partial P_n\). The normalized maps \(\mathcal F_t/\|\mathcal F_t\|\) form a continuous homotopy from the identity radial sphere map to the normalized map for \(G\). Its degree is therefore \(+1\). Reversing any order reverses every edge-orientation sign, making the construction antipodally equivariant. \(\square\)

**Theorem 6 (sharp necessity of graph connectedness).** If \(G\) is disconnected, the same prescribed face-barycenter formula sends the barycenter of some facet of \(\partial P_n\) to \(0\), so the associated normalized sphere map is undefined. Moreover \(Z_G\) lies in a proper linear subspace of \(W\).

*Proof.* Choose \(S\) to be a nonempty proper union of connected components of \(G\). Every edge of \(G\) lies entirely in \(S\) or its complement. On the facet \(F_S\), internal orders in each block vary independently and uniformly. For each edge \(\{i,j\}\) of \(G\), its two possible orientation signs occur with equal frequency, so the arithmetic average of \(z_G(\pi)\) on this facet is zero. Disconnectedness also means the edge-difference vectors span a subspace of dimension \(n-\#\mathrm{components}(G)<n-1\), so its zonotope has no interior in \(W\). \(\square\)

**Corollary 7 (degree-one strengthening of the cyclic affine root selector).** Suppose the dependency permutation \(\sigma\) is one \(n\)-cycle, \(n\ge3\), with zero offsets. Let \(x_\pi\) be the monochromatic color-zero root of Theorem 1. With the orientation of the cycle edges \(\{\sigma(i),i\}\) chosen consistently, the linear incidence transformation
\[
\boxed{\mathcal B(x)=
\sum_{i=1}^n(x_{\sigma(i)}-\tfrac12)(e_{\sigma(i)}-e_i)}
\tag{14}
\]
sends \(x_\pi\) to \(z_{C_n}(\pi)\). The permutahedron-boundary root-selector interpolation of Theorem 3, followed by \(\mathcal B\) and radial normalization, therefore has **integer degree \(+1\)**. In particular its formerly established odd mod-two degree is the reduction of a unit integral degree.

*Proof.* The root formula gives \(x_{\sigma(i)}=1\) if \(\sigma(i)\) precedes \(i\) and zero otherwise. The summand of (14) is then half of the directed edge vector pointing from the later to the earlier member of the pair, which is the corresponding summand in (10). Linearity of \(\mathcal B\) commutes with face averaging and interpolation. Theorem 5 with \(G=C_n\) therefore applies. \(\square\)

**Meaning and limitation.** The odd-degree root carrier is the \(t=0\) limit of a family of full-dimensional zonotopes, beginning at the original permutahedron. The construction is globally coherent across all Coxeter faces and has signed degree \(+1\), rather than merely nonzero parity. Graph connectedness is necessary and sufficient for this *particular* piecewise-linear carrier to avoid the origin. This provides a robust full-dimensional transport model, but does not prove that an arbitrary antipodally odd edge coloring admits analogous root labels, and does not prove NORI1.

## General affine root transport: exchange-influence graphs

Let \(M\in\mathbb F_2^{n\times n}\) be invertible with zero diagonal and \(M\mathbf1=\mathbf1\), and color \(i\)-direction edges by \(c_i(x)=a_i+(Mx)_i\). For a total dimension order \(\pi\), define \(t_i(\pi)=\sum_{j\text{ earlier than }i}M_{ij}\). Its unique color-zero root is
\[
\boxed{x_\pi=M^{-1}(a+t(\pi)),\qquad x_{\pi^{rev}}=\bar x_\pi.}
\tag{15}
\]
An adjacent exchange of \(i,j\) changes the root by
\[
\boxed{d_{ij}=M^{-1}(M_{ij}e_i+M_{ji}e_j).}
\tag{16}
\]
For each root bit \(k\), let \(G_k(M)\) be the graph on \([n]\) whose edges are those pairs \(\{i,j\}\) with \((d_{ij})_k=1\).

**Theorem 8 (finite facet-carrier criterion).** For a nonempty proper dimension subset \(S\), root bit \(k\) is constant over all orders listing \(S\) first if and only if *every edge of \(G_k(M)\) crosses the cut* \(S|S^c\). The standard arithmetic-mean barycentric extension of the root labels maps the whole permutahedron boundary into the boundary of the \(n\)-cube if and only if
\[
\boxed{\forall\varnothing\ne S\subsetneq[n],\ \exists k:
E(G_k(M))\subseteq\partial S.}
\tag{17}
\]
If no such \(k\) exists for a facet \(S\), the facet's barycenter is sent to the open cube interior.

*Proof.* Adjacent exchanges within \(S\) or within its complement generate all orders refining the facet indexed by \(S\). They change root bit \(k\) according to (16). Hence \(k\) stays constant throughout precisely when every root-changing exchange pair crosses the cut. A convex hull of cube vertices lies in the cubical boundary only when at least one bit is constant on all its vertices. If each bit varies, the arithmetic mean of its vertex labels has every entry strictly between zero and one, so lies in the open cube interior. This applies on each facet and proves (17). \(\square\)

**Theorem 9 (dense full-rank affine obstruction).** For every even \(n\ge4\), choose \(M=I+J\) and \(a=0\), where \(J\) is the all-ones matrix over \(\mathbb F_2\). Then \(M\) is invertible, has zero diagonal, and has all row sums odd. Its unique roots satisfy
\[
\boxed{(x_\pi)_i=(\operatorname{pos}_\pi(i)-1+n/2)\bmod2.}
\tag{18}
\]
Every such root has Hamming weight \(n/2\). For every facet \(S|S^c\) with \(2\le|S|\le n-2\), its uniform average root lies in the **open cube interior**; if both blocks have even cardinality, this average is the cube center \(\frac12\mathbf1\). Thus all those facets obstruct the standard convex root carrier despite the existence of one monochromatic root for every order.

*Proof.* Since \(n\) is even, \(J^2=nJ=0\) over \(\mathbb F_2\), so \(M^2=I\). We have \(t_i(\pi)=\operatorname{pos}_\pi(i)-1\bmod2\) and \(\sum_i t_i=n(n-1)/2=n/2\bmod2\), yielding (18). Among the \(n\) ranks, half give root bit one. On a two-block facet, each named direction can occupy any rank within its block. If each block contains at least two ranks, these sets contain both parities. Therefore every root bit varies over the refining orders, and its average lies strictly between zero and one. If both blocks have even size, both parities occur equally often within either block, giving mean \(1/2\) in every root bit. \(\square\)

**Interpretation.** The root vertices of this dense family lie in the hypersimplex \(\Delta(n,n/2)\), unlike the punctured-cube root carrier of a connected permutation cycle. For a single-cycle permutation matrix, each influence graph \(G_k(M)\) consists of one edge, so (17) reduces to connectedness of the dependency graph. For \(M=I+J\), each \(G_k(M)\) is the star at \(k\), and no cut with both sides of size at least two makes every edge of that star cross. Consequently invertibility of the affine interaction matrix does not justify the cyclic root-selector interpolation. This is a limitation of a prescribed facewise convex construction, not an obstruction to other color-sensitive root transport or to NORI1.## Functional-reader root census with branching

Fix \(n\ge2\), a function \(r:[n]\to[n]\) with \(r(i)\ne i\), and bits \(a_i\). The coloring \(c_i(x)=x_{r(i)}+a_i\) is antipodally odd. Let \(L_1,\ldots,L_s\ge2\) be the lengths of the directed cycles of \(i\mapsto r(i)\), permitting branches into these cycles.

**Theorem.** The number of roots \(x\in Q_n\) supporting a monochromatic-zero full antipodal geodesic is
\[
\boxed{|R_0|=2^n\prod_{j=1}^s(1-2^{1-L_j})\ge2^{\lceil n/2\rceil}.}
\tag{FR1}
\]
Every such root also supports a monochromatic-one antipodal geodesic. The lower bound is attained by disjoint directed two-cycles, plus an attached tree leaf in odd dimension. The coloring has at least \(2^{\lceil n/2\rceil-1}\) unoriented monochromatic-zero antipodal geodesics.

*Proof.* For an ordering \(\pi\) rooted at \(x\), its step \(i\) has color zero precisely when
\[
[\pi(r(i))<\pi(i)]=x_{r(i)}+a_i.
\]
These equalities orient the functional-graph edges as precedence constraints. A compatible total order exists if and only if their orientation is acyclic. Each component is unicyclic, possibly with a directed two-cycle represented by parallel constraints; attached trees cannot participate in a directed circuit. On a reader cycle of length \(L\), the comparison directions depend independently on its \(L\) root bits. Precisely two of the \(2^L\) patterns create a directed circuit: for \(L\ge3\), the two consistently directed cycle orientations; for \(L=2\), the two assignments requiring both incompatible precedence orders. The other patterns all extend to total orders. Cycle bit sets are disjoint, and tree root bits impose no restrictions, proving the root count.

Complementing \(x\) reverses every precedence edge, preserving acyclicity. A monochromatic-zero antipodal geodesic from \(x\) gives a monochromatic-one geodesic with the same start by antipodal complementation followed by path reversal. Each factor \(1-2^{1-L_j}\ge1/2\) and there are at most \(\lfloor n/2\rfloor\) cycles. The lower bound follows and is attained by two-cycles. Each unoriented monochromatic-zero geodesic has two starting vertices, yielding the stated path-count bound. \(\square\)

For permutation readers this extends the earlier cycle-product result of this Subsection. The contribution is that branching trees leave the root-success fraction unchanged. It combines with the quadratic Walsh minimizer classification to give exponentially many paired roots at every sharp spectral minimizer.

## Edge-orbit avoidance and restoration resilience for one-reader colorings

Continue with a legal coloring \(c_i(x)=x_{r(i)}+a_i\), where \(r(i)\ne i\), and let \(L=\{j:r^{-1}(j)=\varnothing\}\) be its set of unused reader bits (leaves of the functional graph).

**Theorem (no compulsory antipodal edge pair).** For \(n\ge4\) and every antipodal edge orbit \(q=\{e,\bar e\}\), there is a monochromatic-zero full antipodal geodesic avoiding both members of \(q\). Hence flipping any one antipodal edge pair preserves a monochromatic antipodal geodesic. When \(r\) is a permutation, the avoidance assertion already holds for \(n\ge3\).

*Proof.* Fix the direction \(i\) of \(q\). It suffices to exhibit two monochromatic-zero full geodesics using different direction-\(i\) edge orbits.

Suppose \(L\ne\varnothing\). If a leaf \(j\in L\) is distinct from \(i\), take any monochromatic-zero full path \(P\) rooted at \(x\), whose existence was proved above. Changing the initial bit \(x_j\), while keeping its direction order, leaves every traversed color unchanged: no direction reads bit \(j\). The two resulting paths use different direction-\(i\) edges, since their bit \(j\) values differ when that direction is traversed. Both edges have color zero and thus cannot belong to the same antipodal edge orbit.

It remains to consider \(L=\{i\}\). The colors of every other direction are independent of bit \(i\). Restrict to the \((n-1)\)-cube on directions other than \(i\), still a one-reader coloring. Its monochromatic-zero root set \(R'_0\) is antipodally invariant and has size at least \(2^{\lceil(n-1)/2\rceil}\) by the root census. Let \(j=r(i)\). Precisely half of \(R'_0\) has initial bit \(x_j=1+a_i\). For each of these roots take any monochromatic-zero full path in the smaller cube and append the direction-\(i\) edge. Its color is zero because bit \(j\) has been flipped, and its direction-\(i\) edge is located at the antipode of that smaller-cube root. When \(n\ge4\), there are at least two such roots; they yield different zero-colored direction-\(i\) edges, hence different orbits.

Finally suppose \(L=\varnothing\). Then \(r\) is a permutation without fixed points. For each direction order \(\pi\), the monochromatic-zero root is uniquely prescribed by
\[
x_{r(k)}=a_k+[\pi(r(k))<\pi(k)].
\]
Choose \(j\notin\{i,r(i)\}\), possible for \(n\ge3\), and put \(k=r^{-1}(j)\). The bit in position \(j\) of the direction-\(i\) edge traversed by this root/order pair is
\[
a_k+[\pi(j)<\pi(k)]+[\pi(j)<\pi(i)].
\]
The three symbols \(i,j,k\) are distinct. Choose orders with \(j\) preceding both \(i,k\), and with \(j\) strictly between them; the displayed bit changes. These orders therefore yield different zero-colored direction-\(i\) edge orbits. \(\square\)

**Theorem (leaf-translated Boolean path family).** Suppose \(\ell=|L|\ge1\). Every one-reader coloring has a family of \(2^\ell\) monochromatic-zero full geodesics, obtained from any one path by changing its initial bits in arbitrary subsets of \(L\), while keeping the direction order fixed. For a uniformly selected member of this family, the probability that its direction-\(i\) edge belongs to any prescribed antipodal edge orbit is at most
\[
\boxed{2^{-(\ell-\mathbf1_{i\in L})}\le2^{1-\ell}.}
\tag{AR1}
\]
Therefore any legal recoloring of fewer than \(2^{\ell-1}\) antipodal edge orbits preserves a monochromatic-zero full geodesic.

*Proof.* By the definition of \(L\), no direction color depends on a bit in \(L\). Each changed initial leaf bit therefore translates the entire path without changing its zero word. At its direction-\(i\) step, the edge position records all translated leaf bits except the bit \(i\) itself, if \(i\) is a leaf. Thus each prescribed zero-colored direction-\(i\) edge is encountered by at most a fraction \(2^{-(\ell-\mathbf1_{i\in L})}\) of the translated paths. Since the antipodal mate has color one, the same estimate holds for an antipodal edge orbit. For a set of \(k\) recolored orbits, the expected number hit by a random path in the family is at most \(k2^{1-\ell}\). If \(k<2^{\ell-1}\), this expectation is less than one, so some path avoids every changed orbit and survives monochromatically. \(\square\)

**Consequence for restoration and closure.** For \(n\ge4\), any coloring obtained by changing at most one antipodal edge pair of a one-reader legal coloring is good. More generally, the forbidden Hamming radius around a one-reader template with \(\ell\) unused reader bits is at least \(2^{\ell-1}-1\) orbits, and is at least one orbit regardless of \(\ell\). Thus the universal internal-pivot configuration forced by a hypothetical good-to-bad restoration transition cannot have a one-reader coloring on its good side. The statement is consistent with the sharp dimension-three limitation: one-reader colorings in dimension three can have a common edge orbit in all monochromatic-zero geodesics.

The same-degree path avoidance and leaf-family claims were checked against complete enumeration of one-reader legal colorings in dimensions two through five; the proofs apply at all dimensions.

## Partial reader paired roots and one unrestricted cube direction

For an arbitrary two-coloring \(g\) of \(Q_m\), let \(A_0(g)\) be the roots admitting full antipodal geodesics with words \(0^*1^*\), and let \(A_1(g)\) use words \(1^*0^*\). Define \(P(g)=A_0(g)\cap A_1(g)\). A *partial reader coloring* has, in every direction \(i\), either a constant edge-color function or one of the form \(a_i+x_{r(i)}\) with \(r(i)\ne i\).

**Lemma (leaf insertion).** If a new direction is appended to an arbitrary colored \(Q_d\), all previous direction colors are independent of its bit, and the new-direction color function is arbitrary, then
\[
\boxed{P(g)\times\mathbb F_2\subseteq P(g^+).}
\tag{PR1}
\]
*Proof.* At each root in \(P(g)\), choose paths with color words \(0^*1^*\) and \(1^*0^*\). Insert the new-direction step at the zero-to-one division in the first path and the one-to-zero division in the second. Either value of the inserted color preserves each respective monotone word. The remaining edge colors do not change after the insertion because they are independent of the new bit. Both constructions work from either new-bit starting value. \(\square\)

**Theorem (partial reader paired-root census).** Given a partial reader coloring \(g\) of \(Q_m\), draw a directed arc \(i\to r(i)\) for each nonconstant direction \(i\). Let its directed cycles have lengths \(L_1,\ldots,L_s\ge2\). Then
\[
\boxed{
|P(g)|\ge2^m\prod_{\nu=1}^s(1-2^{1-L_\nu})
\ge 2^{\lceil m/2\rceil}.}
\tag{PR2}
\]
*Proof.* Every weak component of this partial functional graph is either a directed cycle with trees feeding into it or a constant-direction sink with trees feeding into it. A reader cycle of length \(L\) is an antipodally odd one-reader coloring and has \(2^L-2\) roots supporting monochromatic full geodesics of both colors, by the root census proved above. A constant one-dimensional sink has both of its roots in \(P\), because every one-letter word qualifies for either monotone orientation. Attach the remaining tree vertices outward from the cycle or sink. Each new direction reads a previously present bit, while all earlier direction colors are independent of its own bit, so the leaf-insertion lemma doubles the paired-root count. Different weak components have disjoint dependencies, and the Cartesian factorization of paired roots multiplies their counts. This yields the product in (PR2). There are at most \(\lfloor m/2\rfloor\) directed cycles, and each cycle factor is at least \(1/2\); the second inequality follows. \(\square\)

**Theorem (NORI1 with one unrestricted direction).** Let \(c\) be a legal antipodally odd coloring of \(Q_n\), \(n\ge2\). Suppose some direction \(h\) has an arbitrary antipodally odd edge-color function, but for every other direction \(i\ne h\),
\[
\boxed{c_i(x)=a_i+x_{r(i)},\qquad r(i)\ne i,}
\tag{PR3}
\]
with \(r(i)=h\) permitted. Then \(c\) possesses a monochromatic antipodal full geodesic. If the reader cycles of the coloring induced on the lower \(h\)-facet have lengths \(L_1,\ldots,L_s\), the number of unoriented monochromatic-zero full geodesics satisfies
\[
\boxed{
F_n(c)\ge2^{n-2}\prod_{\nu=1}^s(1-2^{1-L_\nu})
\ge2^{\lceil(n-1)/2\rceil-1}.}
\tag{PR4}
\]

*Proof.* Fix the \(h\)-bit to zero and let \(g\) be the horizontal coloring of that facet. A direction \(i\) reading \(h\) becomes constant, while every other direction remains a one-bit reader. Thus \(g\) is a partial reader coloring, and (PR2) applies to its paired roots. For each antipodal pair \(\{y,\bar y\}\subseteq P(g)\), the two \(h\)-edges above \(y,\bar y\) have opposite colors, so one is zero. Both roots lie in \(A_0(g)\); the universal bridge-splice bijection consequently constructs a monochromatic-zero full geodesic crossing the chosen zero edge. Different selected antipodal root pairs give different crossing edges, hence distinct full geodesics. Therefore \(F_n(c)\ge|P(g)|/2\). Substitute (PR2) with \(m=n-1\). \(\square\)

**Necessary complexity of any counterexample.** Every hypothetical bad legal coloring must have at least two direction functions that are not signed one-bit readers. Equivalently, at least two directions have nonzero Fourier mass at odd degrees at least three: a Boolean antipodally odd function with only degree-one Fourier terms is a signed singleton character. This is a dimension-uniform support condition on the nonlinear part of an obstruction, complementary to the quadratic spectral separation theorem.

The statement permits the exceptional direction to depend in any way on all other cube bits. Neither connectivity nor bounded dimension is assumed for the remaining reader graph. The case of two or more arbitrary direction functions is not settled here.
