# Universal odd zero-free map bounds ordered-segment carrier index by n−1

# Explicit zero-free odd map on the FULL ordered-segment poset: exact index ceiling

Let n>=2. Define P_n to be the finite poset of all directed cube geodesic segments P=(v_0,...,v_k), 0<=k<=n, ordered by oriented contiguous-subsegment inclusion. Its involution is Theta(P)=(bar v_k,...,bar v_0). In NORI, every color-admissible one-switch segment subposet G_n(c) is Theta-invariant and included in P_n.

**Theorem (unconditional equivariant map to S^(n-1)).** There exists an EXPLICIT simplicial-PL Theta-odd map U:|P_n|->R^n that never vanishes, hence a Theta-equivariant map |P_n|->S^(n-1), and the same map restricts to every |G_n(c)|. In particular, the free Z2 cohomological index of ANY admissible ordered-segment complex is at most n-1. Therefore a proposed proof of NORI via forcing index >= n on THIS carrier is IMPOSSIBLE, regardless of the coloring.

**Construction.** At any nonfull segment P=(x,...,y) of rank k<n, put
U(P)=x+y-1, interpreted coordinatewise in R^n. Its i-th component is +1 if both endpoints have bit 1 at i, -1 if both have bit 0, and 0 if the segment traverses i. At any FULL antipodal segment P=(x,...,bar x) with distinct direction order p=(p_1,...,p_n), set
U(P)=(1-2x_(p1)) e_(p1) + (2x_(pn)-1)e_(pn).
Since n>=2, p1 and pn differ, so this vector is nonzero. Extend U affinely on every simplex of the order complex.

**Oddness.** If k<n, Theta(P) starts at bar y and ends at bar x, so U(Theta P)=(1-y)+(1-x)-1=-(x+y-1). If k=n, Theta(P) starts at x (since y=bar x) and its direction order is rev(p). Hence its first direction is pn and its last is p1. The prescribed vector becomes
(1-2x_(pn))e_(pn)+(2x_(p1)-1)e_(p1)=-U(P).
Thus the affine map is Theta-odd.

**No zero on any simplex.** A simplex is a chain P_0<...<P_m. If its maximal segment P_m has rank<n, choose any coordinate i not used by P_m. Every nested subsegment also avoids i and has both endpoint bits equal to the same b; hence every vertex of the simplex has U_i=2b-1, so each convex combination has that nonzero component.

If P_m is full, consider its largest proper subsegment P_(m-1), which is a contiguous portion of the full segment and therefore omits the FIRST direction p1 or the LAST direction pn (or both). If it omits p1, its entire vertex interval lies strictly after the first edge, so every nonfull subsegment P_j in the chain has both endpoint bits equal to 1-x_(p1) in coordinate p1. Thus U_(p1)(P_j)=1-2x_(p1). At the full vertex P_m our assigned U_(p1) is precisely the same sign. Therefore U_(p1) is constant nonzero throughout the simplex. If P_(m-1) instead omits pn, every lower segment lies before the last edge, with common pn-bit x_(pn), and U_(pn)(P_j)=2x_(pn)-1, agreeing with the prescribed component of the full vertex. Again U cannot vanish. In a singleton full-vertex simplex U(P_m) is nonzero directly. This handles all chains.

**Consequences.** Earlier NORI research correctly built a free ordered-segment involution and an equivariant map onto physical barycentric face data, but suggested trying to prove index(|G_n|)>=n. The universal zero-free map here refutes that SPECIFIC INDEX OBJECTIVE, without affecting the correctness of the geometrical carrier or the NORI grand conjecture. The stronger topological program must use relative endpoint conditions, a carrier WITHOUT an equivariant inclusion into P_n, or a coloring-dependent obstruction not reducible to absolute Z2-index. The preserved actual-geodesic face labels remain useful.

This theorem is independent of all coloring axioms. It is a sharp methodological no-go for the full ordered-segment carrier, not a counterexample to NORI.
