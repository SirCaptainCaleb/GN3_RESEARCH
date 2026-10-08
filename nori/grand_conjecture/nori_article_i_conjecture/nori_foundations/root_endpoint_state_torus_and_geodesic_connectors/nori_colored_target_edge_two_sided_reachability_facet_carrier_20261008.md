# Colored target-edge facet nesting of monochromatic reachability carriers

# Target-fiber carrier transport along a colored physical edge

In the ordinary edge-colored hypercube, write A_q(z)={r in Q_n : there exists a monochromatic q-geodesic from r to z}; by reversing the path, A_q(z) is also the q-geodesic reachability star rooted at z. For each physical target z, let K_q(z) be the union of all witnessed monochromatic q prefix-chain simplices on its affine root-target fiber F_z, identified with the r-cube and triangulated by relative support S=r XOR z.

**Theorem (two-sided facet nesting).** If i in [n], z'=z XOR e_i, and c({z,z'})=q, then
(1) A_q(z) intersect {r:r_i=z_i} subseteq A_q(z') intersect {r:r_i=z_i};
(2) A_q(z') intersect {r:r_i=z_i'} subseteq A_q(z) intersect {r:r_i=z_i'}.
Both inclusions hold with witness-compatible SIMPLEX carriers, not only pointwise reachable root labels: the identity correspondence on physical root vertices maps each q-monochromatic-prefix simplex on the specified facet of F_z to a simplex of K_q(z') in (1), and symmetrically from F_z' to F_z in (2).

Proof. For (1), any q-geodesic z->r with r_i=z_i never traverses i. Prefix it by the q-colored edge z'->z. Since i was unused in the old geodesic, the resulting path z'->z->r is a q-monochromatic geodesic (its length is d(z',r)=d(z,r)+1). On relative supports its nested prefix chain S_0 subset ... subset S_k, all avoiding i, becomes the actual prefix chain {i} subset {i} union S_0 subset ... subset {i} union S_k from root z', so the image of every old chain simplex is a witnessed face in K_q(z'). The root-label identity sends the Boolean corner (r,r XOR z) in F_z to (r,r XOR z') in F_z', and preserves inclusions as claimed. The reverse statement (2) is the same argument with z and z' interchanged.

**Interpretation as face-local monotonicity.** Across a physical q-colored target edge, the q-reachable-root region expands from target z into z' on the root facet r_i=z_i and expands from target z' into z on the opposite facet r_i=z_i'. Because every physical edge has one of the two colors, each neighboring pair of target fibers has a precisely specified two-sided carrier inclusion for that color. Antipodal oddness makes the analogous opposite-target edge colored 1-q. These constraints couple otherwise independent target fibers and are much stronger than requiring each reachability set to contain the target root and its one-step neighbors.

**Exact topological objective.** Establish an n-dimensional cubical KKM/Hex/Tucker intersection theorem for the families K_0(z),K_1(z) satisfying these facet transfers, full path-prefix coherence, and physical-edge antipodal color oddness. The required conclusion is a Boolean corner (r,r XOR z) in K_q(z) and its beta-antipode (bar r, bar r XOR z) in K_p(z) for some z and colors q,p. Such a collision is an actual monochromatic antipodal geodesic certificate. The carrier inclusions above are proved; a topological forcing theorem from them is still OPEN. The geometric crossings F_z intersect F_z' at fractional points and do not themselves count as collisions.

For ordered-three-face NORI, extending a path across the first two edges does not yet create a colored three-window; an analogous carrier theorem must be formulated on the exact two-ended finite-memory path-state lift, with two seam windows checked at final extraction.
