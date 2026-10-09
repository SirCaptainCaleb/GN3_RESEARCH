# Edge-conjecture counterexamples lift to all higher dimensions; proving even dimensions suffices

THEOREM (upward propagation of original odd edge-color counterexamples). Let c be ANY antipodally odd binary coloring of the UNDIRECTED physical edges of Q_n, n>=1, i.e. c(bar e)=1-c(e). Add a coordinate t to form Q_(n+1). Define physical edge colors
 c'_i(x,t)=c_i(x) for 1<=i<=n,
 c'_(n+1)(x,t)=x_1.
These are well-defined as undirected edge colors: c'_i independent of x_i, and vertical c'_(n+1) independent of t. Also antipodally odd under (x,t)->(bar x,1-t): the first n edge colors complement by the original law, while x_1 maps to 1-x_1.

If a genuine FULL (n+1)-edge antipodal geodesic of Q_(n+1) is MONOCHROMATIC under c', then OMITTING its unique t-direction edge and projecting every cube vertex onto the first n coordinates yields a genuine FULL n-edge antipodal geodesic of Q_n with the SAME physical edge color on every remaining edge, because c'_i(x,t)=c_i(x) independent of t. Therefore
  MONOCHROMATIC Q_(n+1) closure for all colorings IMPLIES MONOCHROMATIC Q_n closure for all colorings.
Equivalently, every counterexample in Q_n extends to a counterexample in Q_(n+1). Iterating yields counterexamples in ALL larger dimensions if any exists. In particular, proving the original odd-edge conjecture in EVERY EVEN dimension suffices to solve it in ALL dimensions: for n odd invoke the statement at n+1, an even dimension.

The same projection is non-increasing in color-switch count, so the same monotone dimension lifting applies to any proposed upper bound r on the number of switches along full antipodal geodesics.

This exact zero-memory face-projection is SPECIAL to physical edge colors, whose color of an existing direction is unaffected by inserting a new coordinate edge. It must not be applied to active NORI ORDERED THREE-FACE windows without separately controlling new triple windows and their seam colors; known doubling seam obstruction prevents that naive transfer.

STRATEGIC CONSEQUENCE. The newly proved odd-dimensional projection coloring nori_k1_odd_dimension_middle_belt_cannot_contain_monochrom_full_projection_permutation_20261009 refutes any universal odd-dimensional two-middle-layer normal form. But the even-dimensional central THREE-layer carrier remains a potentially sufficient reduction, and an all-even-dimension proof would solve the original edge-color conjecture completely via this theorem.
