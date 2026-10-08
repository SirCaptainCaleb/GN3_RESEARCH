# Single target's antipodal link cannot force reachable collision: parity star

# Fixed-target local-index no-go: sparse reachable cones in an antipodally odd coloring

For every even n>=4 take the antipodally odd exterior-parity edge coloring c_i(v)=sum_(j neq i) v_j mod2. Fix physical target z=0^n. Every edge incident with z is color zero. After traversing the first edge to e_j, each unused-direction edge e_j->e_j XOR e_i (i neq j) has color one. Therefore every monochromatic geodesic starting at z has length at most one. In the affine root-target fiber F_z,
K_0(z) is exactly the n-legged star of simplex edges from the diagonal root corner (z,empty support) to the n neighboring root corners; K_1(z) contains only its apex. The union K(z) is the same star.

Under beta simultaneous root and support complement, beta K(z) is the opposite n-legged star at the antipodal corner of F_z. For n>=4 the two stars have no common Boolean vertices (one uses roots of Hamming weight 0 or1, the other roots of weight n or n-1). In their common simplicial triangulation they are disjoint subcomplexes.

Nevertheless the coloring has a monochromatic antipodal geodesic: choose an initial root with n/2 zero-bits and n/2 one-bits and traverse the directions in an alternating zero/one pattern. By the direct color formula c_(p_k)=P(x) XOR(k-1) XOR x_(p_k), all traversed edges then have equal color.

Thus the antipodal S^(n-1) link of a SINGLE fixed-target fiber and the fact that its reachable sets contain all n one-step rays cannot, by themselves, force antipodal reachable-root coincidence. A forcing proof must choose the target globally, couple several target fibers through the actual colored-edge facet transport, or use a different genuinely color-dependent boundary condition. This provides an explicit obstruction to applying a fixed-target Borsuk--Ulam theorem without verifying its hypotheses, not a counterexample to the global conjecture.
