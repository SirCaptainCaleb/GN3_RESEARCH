# The root-endpoint state torus preserves geodesicity under extensions at both ends

This develops the user's proposed n root bits plus n current-position bits in the ordinary antipodally odd edge-colored cube. Let c be a binary coloring of undirected edges of Q_n, n>=2, satisfying c(bar e)=1-c(e). A monochromatic antipodal geodesic has n edges.

**State poset.** Use states (x,y) in {0,1}^n x {0,1}^n, recording the two endpoints of the currently constructed geodesic. Its used-coordinate set is S(x,y)={i:x_i!=y_i}, and rank is rho(x,y)=|S(x,y)|. For any unused direction i, there are two covers:
(x,y) -> (x XOR e_i,y), colored c({x,x XOR e_i});
(x,y) -> (x,y XOR e_i), colored c({y,y XOR e_i}).
All covers increase rank by one. Root extension is permitted only in an unused direction, just as current-end extension is.

**Exact geodesic extraction.** Every monochromatic directed chain starting at a diagonal state (z,z) constructs a monochromatic geodesic between its current endpoints. A root cover prepends the indicated edge, and a current-end cover appends it. Its direction is unused, so no coordinate repeats. The resulting path has length rho and is therefore geodesic. A chain reaching rank n produces a monochromatic antipodal geodesic. Conversely, any monochromatic geodesic between x and y is represented by a chain of current-end covers from (x,x) to (x,y). Consequently directed monochromatic reachability from the diagonal is exactly monochromatic geodesic reachability between the two endpoint labels, even when root moves are allowed.

**Geometry theorem.** The order complex of this state poset triangulates the n-torus
T_n=(boundary[0,1]^2)^n.
In particular, it is n-dimensional, although its vertices carry 2n bits. The cubical one-skeleton is Q_{2n}; the order-complex triangulation adds diagonals. Colored directed chains throughout this item use cover edges, rather than arbitrary diagonals of the triangulation.

Proof. For one coordinate the two unused states 00,11 are minimal, the two used states 01,10 are maximal, and every minimum is covered by every maximum. Its order complex is the four-edge square boundary S^1. The n-coordinate poset is the product of these one-coordinate posets. A comparable chain uses, in each factor, at most one source-to-sink edge; hence it belongs to a product of square-boundary edges and vertices. On each product cell, its chains give the standard monotone triangulation of that cell. These triangulations agree on common faces and cover the product of the n square boundaries. Thus the order complex is a triangulated n-torus. The rank extends affinely on these simplices.

A fixed root x gives an n-cube chart: y ranges freely and covers change y_i away from x_i. The torus adds root-extension cells to these charts, and those transitions have an exact geodesic meaning. Filling the entire geometric 2n-cube would add cells beyond this state complex.

**Symmetries.** Endpoint exchange sigma(x,y)=(y,x) preserves rank and cover colors. Simultaneous antipodality alpha(x,y)=(bar x,bar y) preserves rank and complements cover colors. The involutions commute. Their product tau(x,y)=(bar y,bar x) also preserves rank and complements cover colors. In the product-square geometry:
Fix(sigma)=D={(x,x)};
Fix(tau)=A={(x,bar x)}.
These statements hold on the full torus, since a square boundary meets its diagonal only at 00,11 and its antidiagonal only at 01,10. Alpha acts freely as a half-turn in each circle factor. The two different reflection fixed sets D and A are precisely the geodesic start and target states.

**Top-rank extension lemma.** Every monochromatic geodesic of length n-1 in an antipodally odd edge coloring extends, at one of its two endpoints, to a monochromatic antipodal geodesic.

Proof. Its endpoints x,y agree in exactly one unused coordinate i. The edges {x,x XOR e_i} and {y,y XOR e_i} are antipodal, since bar x=y XOR e_i and overline(x XOR e_i)=y. Their colors are opposite. One therefore has the color of the existing path, and extending at that endpoint uses the final unused direction. QED.

Thus forcing a monochromatic directed chain to rank n-1 already suffices.

**Reachability labels with exact recursion.** Let r_q(x,y) be 1 precisely when a monochromatic q-geodesic joins x to y. Then r_q(x,x)=1. For x!=y,
r_q(x,y)=OR over i in S(x,y) of
[c({x,x XOR e_i})=q AND r_q(x XOR e_i,y)]
OR
[c({y,y XOR e_i})=q AND r_q(x,y XOR e_i)].
The two alternatives remove an edge from the corresponding endpoint and decrease rank by one. Therefore this recursion has no cyclic dependency and is exact. Moreover
r_q(y,x)=r_q(x,y),
r_q(bar x,bar y)=r_{1-q}(x,y),
r_q(bar y,bar x)=r_{1-q}(x,y).
A hypothetical failure has reachability label (r_0,r_1)=(0,0) at every rank n-1 and rank n state. At D the label is (1,1). Every q-colored cover preserves q-reachability forward.

**Equivalent connector formulation at a common vertex.** For an actual cube vertex v, let R_q(v) be the set of roots x admitting a monochromatic q-geodesic x->v. A monochromatic antipodal geodesic exists if and only if R_0(v) intersects R_0(bar v) for some v. If x lies in this intersection, the coordinate sets used from x to v and from x to bar v are complementary and disjoint. Concatenating the two red paths at x gives a red antipodal geodesic v->bar v. Conversely, a red antipodal geodesic itself witnesses the intersection. Any blue antipodal geodesic has a red antipodal image, so red alone suffices.

More directly matching the user's two-root proposal, if roots x and bar x admit monochromatic geodesics to the same v, with either color on either branch, their two direction sets are complementary. Concatenation is an antipodal geodesic with at most one change. In an odd edge coloring that one-change geodesic rotates to a monochromatic one: if x->v has color q and v->bar x has color 1-q, append the antipodal image of x->v after bar x. The suffix v->bar x followed by that image is a monochromatic n-geodesic from v to bar v. If the two branches have the same color, the original concatenation is monochromatic.

**Precise topological obligation.** A connector theorem on this state complex must produce a directed monochromatic chain from D to rank n-1 (or A), or produce the exact complementary-root meeting just described. Once it does, geodesic extraction is automatic. The outstanding claim is the existence of that chain. Undirected connectivity in the state graph does not preserve the used-direction constraint; arbitrary barycentric label averages do not by themselves give a directed chain.

The geometry and the reachability recursion are established. A topological forcing theorem remains open. Symmetry and the labels at D and A alone cannot supply it: the continuous pair (1-rho/n,1-rho/n) has the same exchange symmetries and endpoint values (1,1) at D and (0,0) at A. The colored-cover propagation and edge-color consistency must enter any obstruction argument.

**NORI applicability.** This construction currently concerns one-coordinate windows, namely ordinary edge colors. For ordered-three-face NORI, a state must additionally retain the last two directions (and potentially the first two when extending at the root) so that extension determines the newly formed ordered-three-face window. No edge-case topological conclusion is being silently transferred to three-face colors.

**Additional verification.** The two-end recursion was compared with ordinary fixed-root monotone geodesic reachability for both colors in all 64 antipodally odd edge colorings of Q_3; every endpoint pair agreed.
