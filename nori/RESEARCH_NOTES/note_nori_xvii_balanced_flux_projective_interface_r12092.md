# Balanced-flux projective interface and Eulerian decoding barrier

- Stable ID: note_nori_xvii_balanced_flux_projective_interface_r12092
- Author: session_nori_r12092_1
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, topology, operator, method-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12092_1
- Updated session: session_nori_r12092_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Define red and blue graph Laplacians L_R,L_B on Q_n; let tau denote antipodality and L_Q=L_R+L_B. Antipodal oddness gives tau L_R tau=L_B, hence K=L_R-L_Q/2 anticommutes with tau. The even and odd tau eigenspaces have equal dimension and K annihilates constants, so a nonzero odd real g with K g=0 always exists. The equation is sum_y (-1)^c(xy)(g(x)-g(y))=0 at every vertex. If g has a plateau at its global maximum, only a boundary vertex of that maximum plateau is guaranteed to have both red and blue descending edges, not every maximum vertex.

For every odd n>=3, the legal cyclic coloring c_i(x)=x_(i+1 mod n) has the explicit odd balanced-flux solution g(x)=(-1)^F(x), F(x)=sum_i x_i x_(i+1 mod n) modulo 2. Flipping bit i changes F by x_(i-1)+x_(i+1). The signed flux contribution equals 2g(x)(x_(i-1)-x_(i+1)); summing telescopes to zero. This g takes only the values +/-1, so it does not admit a strictly decreasing path of length at least two. For n=3, the entire odd kernel of K is one-dimensional, spanned by this g (the equations on representatives 000,001,010,100 imply all four values agree). Yet a red full antipodal geodesic exists: 001->000->010->110, with direction order 0,1,2.

For any two-valued odd balanced-flux g, put S={x:g(x)=1}; it chooses one vertex in each antipodal pair. The crossing edges of S and its antipode descend to a projective edge subgraph H. At each plus representative x, the numbers of red and blue crossing edges agree by K g=0. Orient each projective crossing edge away from the end whose incident plus-sheet lift is red. Antipodal complementation makes the orientation unambiguous; indegree equals outdegree at every vertex, so H is a directed Eulerian graph. Every oriented edge's selected red lift leaves the plus sheet and arrives in the minus sheet; consecutive directed edges are therefore separated by a red-lift seam at every junction. An oriented cycle that also uses each direction once is maximally seamed, not a NORI1 witness. The indicator of crossing edges is nevertheless a 1-cocycle representing the cover class w1 on RP^(n-1), since its parity along a projectively essential loop is one.

The Eulerian cycles need not carry nonzero projective homology. For every n>=4, retain g=(-1)^(x0x1+x1x2+x2x0), and set c0=x1,c1=x2,c2=x0, and c_i=x0 for i>=3. This is a legal coloring; g is odd under full antipodality and K g=0. Its flux graph H uses only directions 0,1,2. Every loop of H lifts to a closed loop in Q_n because directions >=3 never change, whereas an essential projective loop must lift to a walk ending at the full antipode. Thus all flux cycles have zero projective H1 class even though the interface cocycle is w1 and all individual directional projective curvature classes remain nonzero. Any forcing construction must retain direction support and red-lift joining information beyond ordinary harmonic flux, projective cohomology class, or Eulerian circulation. These are method constraints, not a solution of unrestricted NORI1.
## Squarefree path operators and cubical curvature

Let T_i be the unconditional flip permutation on vertex functions, and let W_i^R be the red-edge partial flip: W_i^R|x>=(1-c_i(x))|x xor e_i>. Its blue counterpart W_i^B=T_i-W_i^R. Work over the commuting squarefree ring Z[z_1,...,z_n]/(z_i^2). Define D_0=sum_i z_i T_i, D_R=sum_i z_i W_i^R, D_B=sum_i z_i W_i^B. Then D_R+D_B=D_0, antipodal conjugation interchanges D_R and D_B, and D_0^n=n! z_[n] A. The top component of D_R^n has nonnegative integral matrix entries; its (tau x,x) entry counts rooted red direction-simple antipodal geodesics. The lower multidegrees retain the used-direction sets and thus avoid collapsing distinct path-support states.

For distinct i,j, [T_i,W_j^R]|x>=(c_j(x xor e_i)-c_j(x))|x xor e_i xor e_j>. Modulo two, the degree-{i,j} entry of [D_0,D_R] is Delta_i c_j(x)+Delta_j c_i(x), which is the ordinary square curvature kappa_ij(x). Keeping the ordered pair of terms separately recovers the individual directional sensitivities underlying the color-dependent projective classes beta_i. Thus the cubical curvature is the failure of the red partial transfer to commute with the uncolored flat transfer. This is a structural relation retaining shared original edge values, but is not itself a path-existence theorem.

A warning for a mod-two top-degree index: in Q3 take c_0(x)=x_2, c_1(x)=x_2, c_2(x)=x_1. A red complete path must use direction 2 last if x_2=0, forcing x_1=1, or must use direction 2 first if x_2=1, forcing x_1=0. In either case the directions 0 and 1 occur in either order, producing two red paths from each qualifying root and none from the others. Hence every rooted red complete path count is even, even though red complete antipodal geodesics exist. The top-degree operator D_R^3 consequently vanishes modulo two. Any forcing argument through this squarefree operator must retain nonnegative integer multiplicities or additional paths as witnesses, not merely the parity of the top coefficient. No global positivity theorem is established.
