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

## Valid NORI coloring with NO monochromatic spanning geodesic in any of four parallel codimension-two facets

Fix n>=7, choose U⊆[n] of size m=n-2>=5, and let [n]\U={a,b}. Mark any two distinct coordinate directions u*,v* inside U, and call all other directions of U unmarked. For every ordered triple (i,j,k) of distinct directions FROM U define
\[
f(i,j,k)=
\begin{cases}
1,& j\text{ is unmarked and at least one of }i,k\text{ is marked},\\
0,&\text{otherwise}.
\end{cases}
\]
This f is reversal-even, f(k,j,i)=f(i,j,k). Define colors on ALL physical ordered three-faces whose free directions lie in U by
\[
c(F,(i,j,k))=f(i,j,k)\oplus t_a(F),
\]
where t_a(F) is the fixed exterior a-bit. Since a lies outside U, it is fixed on each such face. If \bar F is antipodal, t_a(\bar F)=1-t_a(F), and reversal-evenness gives
\[
c(\bar F,(k,j,i))=f(k,j,i)\oplus(1-t_a(F))=1-c(F,(i,j,k)).
\]
Thus this partial coloring respects the active NORI axiom. Extend arbitrarily, orbit by orbit, to all ordered faces with at least one free direction outside U; the involution (F,pi)↦(\bar F,rev pi) is free so this always yields a globally valid NORI coloring.

**THEOREM.** For this full valid coloring, NONE of the FOUR parallel U-facets contains a monochromatic complete U-geodesic, in EITHER traversal orientation or from ANY projected root. Consequently the color-free four-facet first–last direction graph H_U(r) of the canonical cap theorem is EMPTY for every r∈Q_U.

**Proof.** Fix a permutation p=(p1,...,pm) of U and any facet exterior bits. Its m-2 ordered-three-face window colors equal
\[
f(p_i,p_{i+1},p_{i+2})\oplus t_a,\qquad 1\le i\le m-2.
\]
The physical U-exterior bits do not appear in f, so the word is root-independent inside the facet up to the fixed global flip t_a.

We prove its f-word contains BOTH symbols 0 and1. If either marked coordinate appears in an internal position 2,...,m-1, the window centered there has f=0, since the middle direction is marked. If instead both marked positions are endpoints 1,m, the window (p2,p3,p4) consists entirely of unmarked directions for m>=5, so again f=0.

For f=1, it suffices to find two adjacent positions k,k+1, with one position marked and the other unmarked, such that the unmarked position is internal (2,...,m-1). Such a pair must exist: otherwise any marked-to-unmarked boundary could only have its unmarked position at one of the endpoints, forcing the entire interval of internal positions to be marked or all transitions to occur only at ends. The first is impossible since m-2>=3 but only two marked directions exist. The latter possibility would make the marked positions consist only of a subset of the two endpoints, with both marks at endpoints; then positions 1 and 2 form a boundary whose unmarked index 2 is internal, a contradiction. More directly, if the marks are adjacent at positions 1,2 or m-1,m, the boundary at positions 2,3 or m-2,m-1 works; in all other arrangements at least one marked coordinate has an internal unmarked neighbor. Choose the triple centered at this internal unmarked position and having the marked adjacent position as an endpoint; then f=1.

Hence the f-word contains 0 and1 for EVERY direction permutation, so no full U-geodesic is monochromatic. Complementing the word by t_a does not change this. There are no actual monochromatic U-spanning witnesses in any of four facets, and H_U(r) has no edges. QED.

**Important strategic guardrail.** A dimension-independent proof of grand NORI closure CANNOT begin by claiming that for every (or every prescribed) n-2 support U the four-facet memory graph H_U(r) is nonempty or nonbipartite. This fully legal coloring annihilates that graph for the selected U, while grand closure itself may hold elsewhere. Thus the cap-cycle extraction theorem, although correct, must be combined with a global support-selection argument or with shorter monochromatic reachability. The example is direction-only within U plus one exterior-bit affine twist, so it is not an exotic nonlinear obstruction.

Under hypothetical failure the cap conditions force a rigid bipartition on available near-spanning cores. A valid construction must still prove those cores exist in the required parallel facets.
