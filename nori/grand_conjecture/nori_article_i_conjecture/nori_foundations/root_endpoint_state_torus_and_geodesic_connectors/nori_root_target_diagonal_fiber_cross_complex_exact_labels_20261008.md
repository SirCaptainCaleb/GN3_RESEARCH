# Root–target diagonal fibers: n-dimensional honest antipodal reachability labels

# Root-target diagonal-fiber complex: an n-dimensional honest common-target carrier

Work first in the ordinary antipodally odd EDGE-colored cube. Write the doubled root-progress cube as C=[0,1]^n_r x [0,1]^n_s, where Boolean vertices (r,s) mean a root r and the used-coordinate support S={i:s_i=1}. The physical target is z=r XOR s at Boolean vertices.

For each *actual target* z in {0,1}^n define the linear diagonal fiber
F_z={ (r,s) in C : s_i=r_i if z_i=0, and s_i=1-r_i if z_i=1, for every i}.
This is an n-cube affinely parameterized by r in [0,1]^n. Its Boolean corners are EXACTLY the 2^n pairs (r,S) satisfying r XOR S=z.

**Theorem 1 (faithful antipodal-label geometry).** Let beta(r,s)=(1-r,1-s), the simultaneous root-and-support complement. Each F_z is beta-invariant, with beta acting as the standard central reflection of its n-dimensional r-cube. At Boolean corners beta sends (r,S) to (bar r,[n]\S), which has the SAME physical target z. Therefore the existence of a monochromatic antipodal geodesic is equivalent to the existence of some target z and some pair of beta-antipodal Boolean corners of F_z, each labeled by an ACTUAL monochromatically reachable geodesic to z (colors may differ). This is an exact literal common-target coincidence in geometric dimension n.

Proof. The fiber equations are preserved under (r,s)->(1-r,1-s), and the Boolean XOR identity (bar r) XOR ([n]\S)=r XOR S proves target invariance. Monochromatic geodesics r->z and bar r->z concatenate (reversing one branch) to a full antipodal one-switch geodesic, whose one switch can be eliminated by oddness; the converse uses a monochromatic full antipodal geodesic and z equal to one endpoint.

**Theorem 2 (all targets form a common n-dimensional cross complex).** The union
X_n= union_(z in Q_n) F_z
is the product X_n = X_1^n, where
X_1= {(r,s) in [0,1]^2:s=r or s=1-r}
is a four-armed cross (two intersecting diagonals). For target vertices z,z', F_z intersect F_z' in an affine cube of dimension n-d_H(z,z'); coordinates on which z and z' disagree must have r_i=s_i=1/2. All 2^n fibers contain the unique common center o=(1/2,...,1/2;1/2,...,1/2). The complex X_n has dimension n, and beta is a cellular involution fixing only o.

**Theorem 3 (sharp link index at the common target center).** The link L of o in this cross product is the join of n discrete four-point spaces:
L = D_4 * ... * D_4 (n factors).
It is an (n-1)-dimensional simplicial complex with a free beta-action, and its cohomological Z_2-index is exactly n-1. Indeed, the link of any single fiber F_z at o is a beta-antipodal (n-1)-sphere, establishing index >= n-1. Conversely assign to each of the four signed coordinate rays the sign of its root displacement r_i-1/2, and extend on the join to obtain an everywhere nonzero beta-odd map L -> R^n (then normalize to S^(n-1)). Thus its index <= n-1.

**Exact reachability complexes on fibers.** For a physical vertex z and q in {0,1}, let K_q(z) be the union in F_z of all simplices corresponding to chains of prefixes of q-monochromatic geodesics beginning at z (use the standard monotone triangulation under support coordinates S=r XOR z). Then K_q(z) is a cone with apex the Boolean corner (r=z,S=empty): every witnessed prefix chain includes the apex, and all its faces are retained. Its Boolean vertices are precisely those roots r from which z is reachable by a q-monochromatic geodesic, by reversing the witnessed path. Let K(z)=K_0(z) union K_1(z). It is likewise contractible and contains all n one-coordinate edges out of the apex. No-good-connector means K(z) and beta K(z) have DISJOINT Boolean vertex sets for all z.

**Exact missing topological step.** The large free antipodal index of the link L does NOT automatically make K(z) meet beta K(z): two small opposing cones in an n-cube may be disjoint. A proof needs a coloring-sensitive KKM/Tucker/Hex boundary-carrier theorem coupling K(z) across neighboring target fibers z through the actual q-colored cube edges and their monotone directed transitions. In particular, intersections between distinct affine target fibers occur at fractional coordinates and are not certificates of a common reachable Boolean target. Only beta-opposite REACHABLE BOOLEAN vertices in one fixed F_z certify closure. The fiber construction supplies a faithful n-dimensional geometry for the user's original complementary-support/same-target labels, with no exponential-dimensional target simplex, but does not yet force the needed intersection.

For NORI ordered-three-face windows, this is the outer root/target support carrier; boundary memory and the exact two cross-seam windows must be added before claiming extraction.
