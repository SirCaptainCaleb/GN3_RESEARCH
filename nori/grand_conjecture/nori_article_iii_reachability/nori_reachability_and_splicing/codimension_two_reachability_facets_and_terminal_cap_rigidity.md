# Codimension-two reachability facets and terminal cap rigidity

# Codimension-two reachability facets and terminal cap rigidity

Consider path families occupying a codimension-two coordinate facet while two exterior directions remain available for completion. The terminal ordered-pair memory determines the colors of the first and last newly formed windows. This gives an exact cap-compatibility problem, together with missing-facet and isoperimetric restrictions if global closure is assumed to fail.

## Target-fiber carrier transport along a colored physical edge

In the ordinary edge-colored hypercube, write A_q(z)={r in Q_n : there exists a monochromatic q-geodesic from r to z}; by reversing the path, A_q(z) is also the q-geodesic reachability star rooted at z. For each physical target z, let K_q(z) be the union of all witnessed monochromatic q prefix-chain simplices on its affine root-target fiber F_z, identified with the r-cube and triangulated by relative support S=r XOR z.

**Theorem (two-sided facet nesting).** If i in [n], z'=z XOR e_i, and c({z,z'})=q, then
(1) A_q(z) intersect {r:r_i=z_i} subseteq A_q(z') intersect {r:r_i=z_i};
(2) A_q(z') intersect {r:r_i=z_i'} subseteq A_q(z) intersect {r:r_i=z_i'}.
Both inclusions hold with witness-compatible SIMPLEX carriers, not only pointwise reachable root labels: the identity correspondence on physical root vertices maps each q-monochromatic-prefix simplex on the specified facet of F_z to a simplex of K_q(z') in (1), and symmetrically from F_z' to F_z in (2).

Proof. For (1), any q-geodesic z->r with r_i=z_i never traverses i. Prefix it by the q-colored edge z'->z. Since i was unused in the old geodesic, the resulting path z'->z->r is a q-monochromatic geodesic (its length is d(z',r)=d(z,r)+1). On relative supports its nested prefix chain S_0 subset ... subset S_k, all avoiding i, becomes the actual prefix chain {i} subset {i} union S_0 subset ... subset {i} union S_k from root z', so the image of every old chain simplex is a witnessed face in K_q(z'). The root-label identity sends the Boolean corner (r,r XOR z) in F_z to (r,r XOR z') in F_z', and preserves inclusions as claimed. The reverse statement (2) is the same argument with z and z' interchanged.

**Interpretation as face-local monotonicity.** Across a physical q-colored target edge, the q-reachable-root region expands from target z into z' on the root facet r_i=z_i and expands from target z' into z on the opposite facet r_i=z_i'. Because every physical edge has one of the two colors, each neighboring pair of target fibers has a precisely specified two-sided carrier inclusion for that color. Antipodal oddness makes the analogous opposite-target edge colored 1-q. These constraints couple otherwise independent target fibers and are much stronger than requiring each reachability set to contain the target root and its one-step neighbors.

**Exact topological objective.** Establish an n-dimensional cubical KKM/Hex/Tucker intersection theorem for the families K_0(z),K_1(z) satisfying these facet transfers, full path-prefix coherence, and physical-edge antipodal color oddness. The required conclusion is a Boolean corner (r,r XOR z) in K_q(z) and its beta-antipode (bar r, bar r XOR z) in K_p(z) for some z and colors q,p. Such a collision is an actual monochromatic antipodal geodesic certificate. The carrier inclusions above are proved; a topological forcing theorem from them is still OPEN. The geometric crossings F_z intersect F_z' at fractional points and do not themselves count as collisions.

For ordered-three-face NORI, extending a path across the first two edges does not yet create a colored three-window; an analogous carrier theorem must be formulated on the exact two-ended finite-memory path-state lift, with two seam windows checked at final extraction.

## Codimension-four universal incoming reachability and density of monochromatic four-edge roots

Let c be ANY binary coloring of physical ordered three-faces in Q_n, n>=5, without requiring antipodal oddness. For r∈Q_n define
\[
I(r)=\{i\in[n]:\text{there exists a monochromatic four-edge geodesic }
(r\oplus e_i)\to r\to\cdots\},
\]
where its first step uses direction i and its next three steps are along distinct other coordinates. Let
\[
X=\{x\in Q_n:\text{some monochromatic four-edge geodesic starts at }x\}.
\]

**Theorem (at most four prohibited incoming directions per vertex).** For every vertex r,
\[
\boxed{|I(r)|\ge n-4.}
\]
Consequently,
\[
\boxed{|X|\ge 2^n\left(1-\frac4n\right).}
\]
More quantitatively, at least \((n-4)2^n\) directed cube edges \(x\to r\) can serve as the FIRST edge of some monochromatic four-edge geodesic.

**Proof.** If [n]\I(r) contained five distinct directions, take them as a cyclic 5-tuple. The universal odd-cyclic monochromatic seed theorem gives a four-edge monochromatic geodesic whose first edge arrives at r along one of those five directions. This would put that direction into I(r), contradiction. Hence at most four directions are excluded.

There are 2^n vertices r and at least n-4 good incoming directed edges into each, totaling at least (n-4)2^n such edges. Let B=Q_n\X be roots having NO monochromatic four-edge path. Every one of their n outgoing directed edges must be bad (cannot extend to a monochromatic length-four path), and these bad directed edges have distinct tails, so n|B| is at most the total number of bad directed edges, which is at most 4·2^n. Thus |B|≤4·2^n/n and the asserted root-density bound follows. QED.

**Antipodal-pair corollary.** For n>=9, |X|>2^{n-1}. Since the cube's antipodal involution partitions its 2^n vertices into 2^{n-1} pairs, at least one such pair is fully contained in X. More quantitatively the number of antipodal root pairs with BOTH roots in X is at least \(|X|-2^{n-1}\ge 2^{n-1}(1-8/n)\).

**Uniform k-face generalization.** Let k>=1 and m be the least odd integer >=k+1. For arbitrary binary ordered-k-face coloring of Q_n with n>=m, define I_k(r) as incoming directions of a monochromatic (k+1)-edge geodesic whose first step arrives at r. The same odd-cycle proof yields
\[
|I_k(r)|\ge n-m+1,\qquad
|X_{k+1}|\ge 2^n\left(1-\frac{m-1}{n}\right).
\]
The active k=3 case has m=5.

**Research link.** This imposes a strong necessary local reachability coverage on any hypothetical counterexample to full NORI: almost all roots (proportion at least 1-4/n) possess nontrivial monochromatic terminal-two-tail reachability labels of support rank 2. The next closure obligation is to use antipodal symmetry, root mobility, and the exact REVERSED-TWO-TAIL complementary-support equivalence to turn this abundant low-rank reachability into a complementary high-rank collision. The density bound by itself does not supply that collision.



See the linked research note for the precise four-facet obstruction.
