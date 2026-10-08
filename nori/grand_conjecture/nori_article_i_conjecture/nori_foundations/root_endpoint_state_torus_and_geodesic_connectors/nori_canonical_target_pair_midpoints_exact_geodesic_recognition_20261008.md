# Canonical target-pair midpoint belongs to reachability carrier iff actual monochromatic geodesic exists

# Canonical face centers recognize every monochromatically reachable target exactly

In the n-dimensional diagonal-fiber cross X_n, let z,z' be any two physical vertices, and D={i:z_i neq z'_i}. Their affine fibers F_z and F_z' intersect in the coordinate constraints r_i=s_i=1/2 for i in D and s_j=(r_j XOR z_j) in the continuous affine sense for j outside D. Define the CANONICAL midpoint point
m(z,z')=(r,s), where
r_i=(z_i+z'_i)/2 and s_i=1/2 for i in D;
r_j=z_j=z'_j and s_j=0 for j outside D.
It satisfies m(z,z')=m(z',z) and belongs to F_z intersect F_z'. In the coordinate chart F_z, this is exactly the center of the |D|-dimensional face with supports S subseteq D, incident with the empty-support apex.

**Theorem (exact partial-target midpoint test).** For any q in {0,1},
m(z,z') belongs to K_q(z) iff there exists a monochromatic q-GEODESIC z->z'.
Consequently m(z,z') in K_q(z) iff it belongs to K_q(z'), and both hold precisely when z,z' are joined by a q-monochromatic geodesic. Thus the colored edge carriers are just the distance-one instances of an exact midpoint-overlap principle at EVERY distance.

*Proof.* A q-monochromatic geodesic z->z' has support exactly D. Its full prefix simplex in F_z contains the empty vertex and the D vertex, so it contains their midpoint m(z,z'). Reversing the geodesic gives the same midpoint in K_q(z').
Conversely suppose m(z,z') lies in one witnessed prefix simplex of K_q(z), corresponding to a chain of actual supports S_0 subset ... subset S_k. Since each s_j=0 outside D, any vertex of this chain contributing with positive barycentric weight has no directions outside D. Since each s_i=1/2 inside D, no contributing supports can all omit any such i or all contain any such i. By nestedness, a positive-weight minimal contributing support must be empty (otherwise some coordinate remains one in the entire positive support), and the maximal positive-weight support must be D (otherwise some coordinate remains zero). The witnessed monochromatic path therefore contains empty and full D support along its own order, yielding a monochromatic geodesic z->z'. More formally, the faces of a Freudenthal chain intersect the relative cube center only if the chain includes both its minimum and maximum support. QED.

**Corollary (face-barycenter labels).** For fixed z, all candidate reachable vertices z' are represented by the 2^n barycenters m(z,z') of cube faces containing the root apex in F_z. The full antipodal conjecture asks whether the barycenter m(z,bar z)=o of the ENTIRE fiber appears in some K_q(z). If z,z' differ by k coordinates, q-reachability to z' is literally the inclusion of the associated k-face barycenter in the witnessed path complex. These barycenter labels avoid false intersections of convex averages: each particular canonical midpoint has an exact shortest-path extraction theorem.

**Root-color symmetry.** Under physical antipodality alpha(r,s)=(1-r,s), one has alpha(m(z,z'))=m(bar z,bar z'); oddness sends K_q(z) to K_(1-q)(bar z). Both the midpoint representation and its witness test are fully antipodally equivariant.

**Limit.** Other points of F_z intersect F_z' may lie in K_q(z) and K_r(z') without monochromatic shortest paths between z,z'. The theorem singles out canonical midpoint points as the faithful labels; a general topological intersection theorem must force one of these certified points, rather than an arbitrary geometric crossing. For full antipodal targets, F_z intersect F_bar z={o}, so every intersection is automatically canonical.
