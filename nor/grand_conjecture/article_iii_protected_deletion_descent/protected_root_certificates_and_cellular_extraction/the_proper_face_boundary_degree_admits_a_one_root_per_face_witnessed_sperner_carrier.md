# The proper-face boundary degree admits a one-root-per-face witnessed Sperner carrier

## Composition

(none yet)

## Development

The proper-face boundary degree can be represented using ONE actual witnessed crossing root per face, rather than an average over all refinements.

Let F=B_1|...|B_s be a proper face of the centered permutahedron. Every block B_j is a proper coordinate subset of the minimum counterexample. Choose, for each block, a spanning order with no internal 10 descent (equivalently a one-change ternary word), and concatenate these block orders in the fixed face order.

The resulting full order refines F. Since the ambient instance is a counterexample, it has some actual 10 descent. No such descent can lie wholly inside one block, by construction. Hence at least one 10 descent crosses distinct blocks. Choose one such occurrence and denote its actual root by
r_F=e_a-e_b.
Thus the block-rank functional phi_F satisfies
phi_F(r_F)>0.

Do this independently for every proper face F.

Now barycentrically subdivide the boundary. Label the barycenter of each proper face F by r_F and extend affinely over every boundary flag simplex. Call the resulting PL map R:partial P->W.

Take a point in a boundary simplex with minimal supporting face-chain
F_0<...<F_k=G.
Its barycentric coefficient at the largest face G is positive. Every selected root r_{F_i} comes from an order refining F_i and hence also refines G. Therefore
phi_G(r_{F_i})>=0
for every i, while
phi_G(r_G)>0.
Consequently
phi_G(R(x))>0.
So R is zero-free on the entire boundary.

Moreover the same argument applies to the straight homotopy between R and the all-refinements boundary carrier H of root 139: on a minimal boundary flag, both G-labels are strictly phi_G-positive and all smaller-face labels are weakly nonnegative. Hence the homotopy never vanishes.

Therefore R/||R|| has the same nonzero boundary degree as H/||H||, namely the inward radial degree.

Now choose one genuine ambient actual 10 root r_0 and label the top-face barycenter by r_0. Cone the boundary map R to this apex. Nonzero boundary degree forces a zero in some cone simplex. Since neither the boundary nor apex is zero, the minimal zero support has the form
lambda_0 r_0 + lambda_1 r_{F_1}+...+lambda_k r_{F_k}=0
with all displayed coefficients positive and
F_1<...<F_k=G
a chain of proper faces.

Thus the topological extraction may be made entirely finite and witnessed:
- one chosen ambient root r_0;
- at most dim(P)=n-1 proper-face roots;
- every proper-face root comes from one explicit full coordinate order assembled from good orders on the blocks of that face;
- all proper-face roots refine the same largest proper face G.

As before, phi_G(r_0)<0 while every r_{F_i} is weakly forward in G and r_G is strictly forward. Flow decomposition yields a directed monotone path from the target of r_0 back to its source using a subset of these finitely many witnessed proper-face roots.

This replaces the averaged common-face path certificate by a nested-FLAG certificate with one concrete witness order per root. The remaining gluing problem is correspondingly discrete: compare root witnesses attached to successive faces in one refinement flag, rather than arbitrary refinements of a common face.
