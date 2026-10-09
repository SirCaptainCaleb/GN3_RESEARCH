# Active NORI colorings as compatible antipodal coordinate-sector cuts; exact full-path cut energy

# Exact equivariant sector-cut atlas for physical monochromatic connectors and global switch defect

Let n>=5 and c be an ACTIVE NORI binary coloring of actual physical ordered three-faces, c(tau u)=c(u)+1 in F_2, where tau(F,(a,b,d))=(bar F,(d,b,a)). Let H be the actual physical ordered-window shift graph: vertices are physical ordered 3-face windows, and an undirected edge uv records two consecutive windows of a genuine four-edge geodesic. For each cube coordinate i let H_i be the sector subgraph induced by the actual windows containing i, retaining exactly those H-shift edges on which i belongs to the TWO overlapping middle directions of the underlying four-direction word. Earlier Item nori_certified_square_complex_connected_antipodal_one_class_20261008 proved H_i is connected.

**THEOREM 1 (exact phase-cut identity).** For a vertex u=(F,(a,b,d)) of H_i, define s_i(u)=1 iff i=b is in the MIDDLE position of the ordered free triple, and 0 iff i=a or i=d. Define the binary phase
 g_i(u)=c(u)+s_i(u).
Then:
(A) s_i(tau u)=s_i(u), g_i(tau u)=1+g_i(u).
(B) Every genuine sector shift uv in H_i changes s_i by one, so
 1{c(u)=c(v)} = g_i(u)+g_i(v) (in F_2).
Consequently the entire set of genuine monochromatic four-edge connector edges involving direction i is EXACTLY the graph edge boundary
 delta_{H_i} A_i,
where A_i={u in V(H_i):g_i(u)=0}. The two phase shores A_i and its complement are interchanged by tau, and every even-length sector path from u to tau u crosses the good connector cut an ODD number of times.

Proof. On a genuine four-direction shift (a,b,d,e), the sector coordinates are precisely i=b or i=d. If i=b, its position changes 2->1; if i=d, its position changes 3->2. Thus s_i differs on the adjacent actual windows. Substituting g_i=c+s_i gives g_i(u)+g_i(v)=c(u)+c(v)+1, which equals 1 exactly for same-color windows. Reversing an ordered triple fixes the predicate of the middle position; NORI oddness flips c, proving (A). As g_i labels the sides of A_i, the good-edge equality set is its exact edge cut. For a path from u to tau u, summing g_i differences telescopes to1, so the number of good cut crossings is odd. QED.

**THEOREM 2 (complete multi-coordinate compatibility; exact converse).** For every ordered physical window u=(F,(a,b,d)) the three sector phases satisfy
 g_a(u)=g_d(u)=c(u),   g_b(u)=1+c(u).
Thus on any shared vertex u of H_i and H_j, the transition law is
  g_i(u)+g_j(u) = s_i(u)+s_j(u).                 (GLUE)
Conversely, suppose that for each direction i a binary labeling g_i of ALL physical windows containing i is given, satisfying (i) g_i(tau u)=1+g_i(u), and (ii) GLUE on every shared window. Then c(u)=g_i(u)+s_i(u) is independent of which free direction i is chosen, defines a UNIQUE genuine active NORI coloring on ALL physical ordered faces, and its i-middle monochromatic connectors are precisely the edges crossing delta A_i. Therefore active NORI colorings are EXACTLY equivariantly antipodal families of binary sector shores satisfying the explicit physical window overlap equations GLUE. The sector shores cannot be varied independently.

Proof. The displayed phase identities follow by the definition of s. For the converse, GLUE makes g_i+s_i equal for all three free coordinates of each actual ordered-face window, hence defines one well-defined c(u). Since tau preserves each s_i and flips each g_i, c(tau u)=1+c(u). Its values belong to ACTUAL physical face windows (rather than different hub representatives), so face locality is automatic. The first theorem then recovers the exact sector cut sets. QED.

**THEOREM 3 (exact rooted full-geodesic cut energy).** Let P be ANY actual FULL n-edge geodesic from a physical root x with direction order p=(p1,...,pn). Let u_t be its actual ordered three-face window with tuple (p_t,p_(t+1),p_(t+2)), for t=1,...,n-2. On the t-th consecutive-window shift e_t=(u_t,u_(t+1)), both coordinates p_(t+1),p_(t+2) belong to the overlapping middle pair, and both belong to their H_i sectors. Then
  D(P) = sum_(t=1)^(n-3) 1{ g_(p_(t+1))(u_t)=g_(p_(t+1))(u_(t+1)) }
       = sum_(t=1)^(n-3) 1{ g_(p_(t+2))(u_t)=g_(p_(t+2))(u_(t+1)) },
where D(P) is the EXACT number of ordered-three-face window color switches of P (ordinary integer sum).
Thus active NORI grand closure is equivalent to a PHYSICAL FULL ROOTED direction-distinct window walk crossing its current sector cut on ALL BUT AT MOST ONE of its n-3 actual window-shift edges, with the sector on each shift selected from its pair of middle free directions. The root, physical faces and global direction order remain mandatory witness data. Arbitrary paths in H or across sector cuts cannot be substituted for a full cube geodesic.

Proof. By Theorem 1, for each actual shift and either middle coordinate i, g_i has equal endpoints iff its physical face colors differ. Sum this exact bitwise equivalence over the n-3 shifts. QED.

**THEOREM 4 (cohomological localization of the temporal and connector classes).** On each connected sector graph H_i, the intrinsic temporal 1-cocycle beta_H(e)=1 on every physical shift edge is the exact coboundary delta s_i. The same-color connector cochain alpha_H(e)=1{c(u)=c(v)} is the exact coboundary delta g_i. On quotient H_i/tau, however, alpha_bar represents precisely the NONZERO antipodal-cover class w_i, while beta_bar represents zero. To see this, choose one lift of each quotient vertex; the voltage t(e) is the tau-swap of its terminal chosen lift. Antivariance g_i(tau u)=g_i(u)+1 gives alpha_bar(e)= t(e)+delta(g_i on chosen lifts). Since s_i is tau-invariant, beta_bar=delta(s_i on chosen lifts), so [alpha_bar]=w_i and [beta_bar]=0. Connectivity of H_i makes its free quotient cover connected and hence w_i nonzero.

Globally H is covered by the sectors H_i: every shift belongs to exactly the two sectors indexed by its middle pair. On the full H, beta is NONEXACT, by the physical 5-window pentagon on which beta evaluates1. Therefore the global temporal obstruction is produced by JOINING DIFFERENT SECTOR CHARTS; within each individual H_i the same parity is a coboundary. This mathematically identifies the cross-chart gluing requirement that all one-sector cut-count arguments lose.

**Research consequence / exact gap.** The improved exponentially numerous good sector cut edges (Item nori_equivariant_window_shift_short_antipodal_path_many_middle_connectors_20261009) supply dense genuine interfaces between antipodally paired phases, and this Item shows how the interfaces overlap at each physical window. Grand closure requires finding ONE injective full geodesic meeting all but at most one of its successive rotating sector cuts. A nonzero first cover class or abundant sector cut crossings alone does not synchronize the cuts. The next forcing target is a higher-dimensional physical window/terminal-memory comparison of these sector shores whose nonzero obstruction compels the exact same-root complementary reversed-two-tail reachability pair.
