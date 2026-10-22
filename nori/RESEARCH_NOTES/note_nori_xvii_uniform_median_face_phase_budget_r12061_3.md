# Uniform median-face phase budget and edge-poset convexity

- Stable ID: note_nori_xvii_uniform_median_face_phase_budget_r12061_3
- Author: unspecified; session provenance retained
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, topology, median, phase, rank-parity
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12061_3
- Updated session: session_nori_r12061_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_xvii_median_three_route_telescoping_r12024_2
- note:note_nori_median_arm_mobius_ladder_nerve_index_r12061_3

## Research note

# All-face phase budget and alternating chains in the cubical edge poset

Let c be an arbitrary antipodally odd binary coloring of Q_n, and let d>=3 be the global minimum of twisted cyclic color changes D(P) over full antipodal geodesics. Fix a minimizing geodesic with d nonempty monochromatic run-support blocks B_1,...,B_d. For any one of its 2d run-boundary vertices p, let A,B be the two incident blocks, sizes a,b, and let F_p be the cubical face fixing them at p, of dimension L=n-a-b.

UNIFORM BUDGET THEOREM. Every spanning geodesic Q of F_p rooted at p has at most eta=n-d-2 equal-color adjacent edge pairs. Indeed choose the spanning run-boundary triangle whose median-to-p arm equals F_p and whose other two arms use A and B. The three-route telescoping theorem requires the sum of the three arms' ordinary color changes to be >=d-1. The other arms can have at most a-1 and b-1 changes. Therefore s(Q)>=d+1-a-b; since Q has L-1 edge comparisons, its equal-color comparisons number at most (n-a-b-1)-(d+1-a-b)=n-d-2. This holds for EVERY run-boundary face, not just faces with singleton incident blocks.

RANK-PHASE CHART. If eta=0 and L>=3, every spanning path alternates. Swapping successive directions at positions >=2 preserves the first original edge, and swapping positions 1 and 2 preserves the third original edge; so all orders have the same first color a_p. Every face edge at rank r from p then has c(e)=a_p+(r-1) mod2.

TRANSVERSE ODD-DIMENSION CONTRADICTION. For an i-edge e, write h_i(e)=c(e)+sum_(j!=i)x_j mod2, where x is either endpoint (the summation omits i). For odd n, h_i(tau e)=h_i(e)+1. A rank-phase chart on F_p makes h_i constant on all its i-edges. If F_p,F_q have disjoint nonempty fixed-direction sets and a common free direction i, then F_p meets both F_q and tau F_q in i-edges. Constancy forces equal h_i values, while antipodality forces opposite values on F_q and tau F_q. Contradiction.

COROLLARY. If d is odd and d>=5, then n>=d+3. The budget gives n>=d+2. If n=d+2, then n is odd, eta=0, and every boundary face has dimension >=d-2>=3 because the d blocks have only two total extra directions. Pick two nonadjacent run boundaries on the d-cycle; their incident direction blocks are disjoint. The transverse contradiction applies. Thus every odd dimension n>=7 has minimum D at most n-4. The d=3,n=5 case is not decided by these two-face charts.

POSEТ MODEL FOR eta>=1. In an L-face rooted at p, represent an original edge by (S,i), where S is its set of already flipped free directions and i is the next direction. Define (S,i) < (T,j) iff S union {i} is a subset of T. Every chain of such edges lies in a common spanning geodesic, and conversely the edge sequence of every spanning geodesic is a maximal chain. Define the normalized phase theta_p(S,i)=c(S,i)+|S| mod2. Its changes along a spanning geodesic occur precisely where consecutive original edge colors agree. Thus the phase budget eta is equivalent to forbidding every strictly increasing edge-poset chain of length eta+2 with alternating phase labels. When eta=1, this is equivalent to BOTH phase classes being order-convex in the edge poset: if e<=f<=g and theta(e)=theta(g), then theta(f)=theta(e). This does not imply globally constant phases: a monotone threshold depending on one free direction may change once on any maximal chain.

OPEN. Prove an incompatibility among these order-convex phase charts over the full antipodal median-arm face cover, using original shared edges and the global-minimum constraints. Comparing just two faces is insufficient for a one-phase-change budget: the two relevant intersection patterns can be incomparable in the rooted edge poset.
