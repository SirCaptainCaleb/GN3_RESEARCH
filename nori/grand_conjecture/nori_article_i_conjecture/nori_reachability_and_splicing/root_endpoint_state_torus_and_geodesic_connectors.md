# Root-endpoint state torus and geodesic connectors

# Root-endpoint state torus and geodesic connectors

Root and endpoint are independent state variables. A two-ended geodesic may extend on its initial or terminal side without repeating a cube coordinate, provided the current support and the two-window terminal memory are retained. The root-endpoint torus is the simplest geometric carrier for these extensions, but its antipodal index remains small. The following proofs establish the exact extension geometry and identify the earliest loss of physical compatibility under naïve reachability coincidence.

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

## Antipodal endpoint links are high-index spheres with canonical monochromatic entrance sectors

Continue the rooted two-end state torus T_n=(S^1)^n of ordered pairs (u,v) in Q_n^2, with rank d_H(u,v), endpoint exchange sigma(u,v)=(v,u), simultaneous antipodality alpha(u,v)=(bar u,bar v), and tau=alpha sigma. Each coordinate circle is the square 00--01--11--10--00, with angles 0,pi/2,pi,3pi/2.

**Theorem 1 (local antipodal link).** For n>=2, every top-rank state a_x=(x,bar x) is an isolated fixed point of tau, and a sufficiently small link L_x around a_x is an (n-1)-sphere on which tau acts as ordinary antipodality. Its natural crosspolytope cell decomposition has 2n signed vertices (two inward rank-decreasing choices for each coordinate), and its 2^n orthant facets are indexed by all possible common connector vertices z in Q_n. Opposite orthants correspond to z and bar z.

*Proof.* In angular coordinates, tau(theta)=pi-theta coordinatewise. At a_x each theta_i is pi/2 or 3pi/2. In a sufficiently small local chart delta around a_x, tau(delta)=-delta. A small Euclidean ball is tau-invariant, and its boundary is the stated antipodal sphere. The 2n inward directions are the two arcs in each coordinate circle from a_x toward the two diagonal states 00 and 11. Choosing one arc per coordinate gives precisely a product n-cube from the diagonal state (z,z) to a_x, with z_i the chosen diagonal bit. The sector's directed chains are geodesics built by extending either endpoint at each unused direction. Tau sends the diagonal root (z,z) to (bar z,bar z), proving the opposite-sector claim.

**Theorem 2 (canonical entrance-sector selectors).** Let c be an antipodally odd coloring of the undirected edges of Q_n. Write c_i(x)=c({x,x XOR e_i}), and define a cube vertex z_q(x), q in {0,1}, by
(z_q(x))_i = x_i XOR 1 XOR c_i(x) XOR q.
For each antipodal endpoint state a_x=(x,bar x), the q-colored incoming cover edges at a_x select exactly one of the two inward signs in each coordinate. These n signs together specify the unique orthant sector whose *all n immediate final edges into a_x* have color q, and its diagonal root is z_q(x). Moreover
z_1(x)=bar z_0(x),
z_q(bar x)=z_q(x).

*Proof.* The two inward covers in coordinate i add either the edge incident with x of color c_i(x) or its antipodal edge incident with bar x of color 1-c_i(x). The first cover belongs to the sector with diagonal coordinate z_i=bar x_i; the second to z_i=x_i. Thus the sector whose incoming cover has color q has z_i=bar x_i when c_i(x)=q and z_i=x_i when c_i(x)!=q, exactly z_i=x_i XOR 1 XOR c_i(x) XOR q. Each coordinate's two incoming colors are complementary, so the sector is unique. The first displayed relation is immediate, and the second follows from c_i(bar x)=1-c_i(x).

**Precise topological opportunity and extraction warning.** The simultaneous-antipodality action alpha on the entire T_n has equivariant cohomological index only one, but the tau action on each punctured neighborhood of a target a_x has link S^(n-1) with full local antipodal index n-1. The selected z_0(x) and z_1(x) are complementary labels encoding the last-edge color data, precisely matching the proposed antipodal-coordinate labels. Nevertheless color agreement of all n last edges does **not** imply a monochromatic directed chain from the corresponding diagonal root to a_x: interior covers can obstruct, and a successful chain could also enter through a sector whose other last edges have different colors. A Hartman/Tucker/Sperner argument would have to label each local sector by jointly realizable *directed reachability* and prove the required boundary/incidence relations; the local high index and final-edge selectors alone do not settle the edge conjecture or ordered-three-face NORI.

## Three-unused-direction flap dichotomy in ordered-three-face NORI

Fix n>=6, a color-q geodesic P of length m=n-3 from x to y, with direction sequence p=(p_1,...,p_m), and the three unused coordinates W={a,b,c}. Thus the ordered-three-face word inside P consists of m-2>=1 copies of q. For any ordering t=(a,b,c) of W, consider two *full antipodal* geodesics:
H_front: starting at x XOR W, flip a,b,c to reach x, then follow P to y;
H_back: follow P from x to y, then flip c,b,a to finish at y XOR W=bar x.

Let u=c(F_x,(a,b,c)), the color of the ordered missing-coordinate face at x (its exterior coordinates equal x outside W). Since F_y=bar F_x and antipodal reversal reverses coordinate order, the last ordered face of H_back has color 1-u.

Introduce the exact four bridge colors
A(b,c)=color of the (b,c,p_1) window in H_front,
B(c)=color of the (c,p_1,p_2) window in H_front,
C(c)=color of the (p_{m-1},p_m,c) window in H_back,
D(c,b)=color of the (p_m,c,b) window in H_back.
(The displayed dependencies on b,c are justified because ordered-three-face colors ignore the three free coordinate bits, so the removed first missing coordinate does not affect A/B, and the terminal unflipped missing coordinate does not affect C/D.)

The two full color words are EXACTLY
H_front: (u,A(b,c),B(c),q,...,q),
H_back: (q,...,q,C(c),D(c,b),1-u).

**Theorem (forced anti-switch flaps).** If the NORI grand conjecture fails for this coloring, then for EVERY length-(n-3) monochromatic q-geodesic P and EVERY ordering (a,b,c) of the three unused coordinates the following holds:
- if u=q, then (C(c),D(c,b))=(1-q,q), and at least one of A(b,c),B(c) differs from q;
- if u=1-q, then (A(b,c),B(c))=(q,1-q), and at least one of C(c),D(c,b) differs from q.

*Proof.* If u=q, H_back begins with q and ends with 1-q. The complete four-block word q,C,D,1-q has at most one color change precisely when (C,D) is qq, q(1-q), or (1-q)(1-q). Under counterexample all such completions fail, so the sole remaining pair is ((1-q),q). The matching-front outer color and the P interior color are both q; it fails only if at least one of A,B differs from q. If u=1-q, the same argument with the two completions interchanged gives (A,B)=(q,1-q) and a defect in at least one of C,D. All four bridge windows are actual ordered-three-faces, and the only oddness relation used is c(bar F,rev pi)=1-c(F,pi). QED.

**General-dimension consequence.** Any proposed NORI counterexample must exhibit an explicitly prescribed *alternating two-seam obstruction* on one of two opposite three-direction flap completions of every nearly spanning monochromatic core. This is a direct face-local analogue of the one-edge antipodal extension mechanism, now with two unavoidable seam windows. It is not yet a closure theorem: the color on the missing ordered three-face can vary with all six permutations, and the four bridge families do not contradict each other without additional overlapping-core or path-exchange relations.

**Research target.** Derive an exchange or carrier theorem that forces, for at least one such core, one permutation of W whose forced-flap pattern is impossible. Unlike a Q_7 subclass enumeration, this obstruction and its color transport hold for every dimension n>=6.

These results give exact local and conditional constructions. No conclusion here asserts unrestricted high-dimensional grand closure.
