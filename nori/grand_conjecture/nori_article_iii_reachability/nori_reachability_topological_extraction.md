# Topological reachability spaces and extraction

# Topological reachability spaces and extraction

This section separates exact discrete geodesic extraction from the topology of its continuous carriers. The underlying objects are initially antipodally odd physical edge colorings, with c(bar e)=1-c(e). The ordered-three-face problem requires additional ordered terminal-memory data because joining two monochromatic branches creates two new three-face windows.

## The doubled root–endpoint cube

For x,y in Q_n, put S(x,y)={i:x_i≠y_i} and rank rho(x,y)=|S(x,y)|. A state (x,y) represents the endpoints of a path using precisely S. For any i outside S one may replace (x,y) by (x xor e_i,y) or by (x,y xor e_i). The respective covers prepend or append the corresponding genuine edge, and raise the rank by one. If a chain begins at (z,z) and all covers have color q, it constructs a monochromatic q-geodesic: each coordinate is used once. Conversely any monochromatic geodesic is encoded by appending its edges. A chain to rank n yields an antipodal geodesic.

For each coordinate, the four endpoint-bit states form a height-one poset whose order complex is the square boundary S^1. Their product has an order-complex triangulation of (S^1)^n, the n-torus. Thus the 2n endpoint bits give an n-dimensional topological carrier with exact cover-chain path meaning. Its topology alone has limited antipodal index, so a forcing argument must use the colored reachable part and its actual incidence data.

## The root–support reachability recursion

For q∈{0,1}, define E_q(x,S) to mean that some q-monochromatic geodesic begins at x and uses exactly S, ending at x xor 1_S; include S=empty. For nonempty S,

E_q(x,S) iff there exists a∈S such that c({x,x xor e_a})=q and E_q(x xor e_a,S\{a}).

This follows by deleting the first edge, and the converse follows by prepending it. Reversal gives E_q(x,S)=E_q(x xor 1_S,S). Antipodal reversal gives E_q(bar x,S)=E_(1-q)(x,S). Root movement can also prepend an unused q-edge while retaining the terminal vertex. These are genuine geometrical covers, rather than formal implications among labels.

Let E=E_0∪E_1. Define sigma(x,S)=(x,[n]\S). There is a one-switch antipodal edge-geodesic iff E meets sigma(E). Indeed a collision yields monochromatic branches from x to x xor 1_S and from x to x xor 1_([n]\S), with disjoint direction supports. Reverse the first branch and concatenate at x to obtain an antipodal geodesic with at most one color change. Antipodally odd edge colors also permit the standard rotation argument to turn this existential one-switch witness into a monochromatic antipodal witness. Equivalently there exists x whose color-free monochromatic reachable set R(x) contains both z and bar z. The same condition may be written as a common endpoint reachable monochromatically from x and bar x.

## Honest Freudenthal carriers and midpoint extraction

Fix x. A monochromatic geodesic with nested prefix supports S_0⊂...⊂S_k determines a simplex of the usual cubical triangulation of the support cube. Let K_q(x) be the union of simplices witnessed by actual q-monochromatic geodesics from x. The face center associated with D={i:x_i≠y_i} lies in K_q(x) precisely when some q-monochromatic geodesic joins x to y.

For the forward implication, the simplex of the witness contains the empty and D prefix vertices, hence their midpoint. Conversely, if the center of the D-face lies in one witnessed chain simplex, all coordinates outside D vanish and all coordinates in D equal 1/2. Nestedness forces the extremal supports represented by positive barycentric coefficients to be empty and D: otherwise some D-coordinate stays 0 or stays 1, or some outside coordinate remains positive. Thus the same witness path reaches D. This midpoint criterion faithfully encodes target reachability without creating paths from merely convex combinations of unrelated witnesses.

The candidate global argument seeks a topologically forced intersection between antipodally related honest carriers or labels. A zero of a continuous extension in the ambient 2n-cube need not belong to a discrete witnessed simplex, so an additional boundary or incidence theorem is indispensable.

## Terminal profiles and equivariant nerves in NORI

For active ordered-three-face colorings, fix an ordered terminal pair J=(a,b) and let D_J=[n]\{a,b}. Denote by R_J(x) the supports U⊂D_J of q-monochromatic physical geodesics from x ending in ordered directions (a,b), with color q existentially quantified. The reversed-tail splice theorem requires complementary supports U and D_J\U at the *same root*, with terminal orders J and rev J.

Form signed profiles L_x of true pairs (J,U) and their formal reversed-complement profiles tau L_x. The nerve of these signed sets has all positive vertices spanning one simplex and all negative vertices spanning another: every three-edge path has just one ordered-face window and hence supplies a monochromatic singleton-support label from every root. A mixed edge between (x,+) and (y,-) witnesses compatible labels at potentially different roots. When x=y it supplies the desired reversed-tail splice. When x≠y, antipodal symmetry supplies the mirrored mixed edge; along with the two universal same-shore edges these give a genuine equivariant four-cycle, whose two same-root mixed diagonals are precisely the missing grand-closure certificates. Therefore the nerve's nontrivial low-dimensional topology can survive under hypothetical grand failure.

This distinguishes the two forcing tasks. In the edge case, an antipodal collision in one uncolored R(x) is the exact extraction condition. In NORI, a collision must additionally preserve the physical terminal orders and same-root complementary supports. The present reachability carriers and signed-root nerves provide exact encodings and identifiable boundary configurations; a global coincidence theorem enforcing that strengthened compatibility remains open.
