# Honest reachable-target geometry equals the monochromatic flag subcomplex of barycentric Qn

# The honest root-target reachability complex folds into the ordinary barycentric subdivision of Q_n

Assume n>=2 and let X_n be the root-progress diagonal cross: X_n={(r,s) in [0,1]^(2n) : for each i, s_i=r_i or s_i=1-r_i}. Its target fiber F_z is the n-cube given by s_i=r_i for z_i=0 and s_i=1-r_i for z_i=1. Let K_q(z) be the union of all witnessed monochromatic q-geodesic prefix-chain Freudenthal simplices starting at z within F_z, and K=union_(z,q)K_q(z).

**Theorem 1 (canonical folded physical cube).** Define
B_n={(r,s) in X_n : s_i=min(r_i,1-r_i) for all i}.
Projection (r,s)->r identifies B_n PL-homeomorphically with the ORDINARY physical n-cube [0,1]^n, and it intertwines alpha(r,s)=(1-r,s) with physical antipodality r->1-r. For each z in Q_n,
C_z=F_z intersect B_n
is the closed corner orthant of physical cube, defined by 0<=r_i<=1/2 if z_i=0 and 1/2<=r_i<=1 if z_i=1. The C_z partition B_n into 2^n small subcubes.

**Theorem 2 (precise barycentric-subdivision identity).** For a cube face H(z,S) spanned by a corner z and a free direction set S, its physical barycenter b_H has coordinates r_i=1/2 for i in S and r_j=z_j for j outside S. Its unique point in B_n is exactly the canonical partial-target midpoint m(z,z XOR S) from the target-fiber construction. This point is independent of the choice of corner of H.

The full barycentric subdivision sd(Q_n) consists of simplices indexed by nested flags of faces
{z}=H_0 subset H_1 subset ... subset H_k,
where a maximal flag has dimension k=n and corresponds to a root corner z and an order of all n directions.
Define A subset sd(Q_n) as the union of all barycentric flag simplices whose direction order gives a MONOCHROMATIC EDGE-GEODESIC PREFIX from that root z, taking both colors. Then
A = K intersect B_n,
with both sides identified under the PL projection to the physical cube.

Proof. A q-monochromatic path starting from z in directions p_1,...,p_k gives the standard Freudenthal simplex in F_z on relative support vertices empty, {p_1},...,{p_1,...,p_k}. In r-coordinates this simplex is cut out by the homogeneous inequalities 1>=t_(p1)>=...>=t_(pk)>=0 and t_j=0 on unused coordinates, where t_i=|r_i-z_i|. Intersecting the corner orthant C_z is the same as intersecting each t_i<=1/2, giving exactly the 1/2 homothetic copy of that Freudenthal simplex at z. Its vertices occur at the physical barycenters of H(z,empty),H(z,{p_1}),...,H(z,{p_1,...,p_k}). Thus K_q(z) intersect C_z is exactly the union of all such witnessed monochromatic flag simplices. Every K_q(z) lies in F_z, and F_z intersect B_n=C_z; taking the union over z,q proves the identity.

**Theorem 3 (central filling and thin boundary alternative).** The barycenter b_(Q_n) of the whole physical cube is in A iff some monochromatic antipodal geodesic exists. Indeed it is precisely the common center o, and belongs to one witnessed flag simplex exactly when the flag reaches the full cube. If no monochromatic antipodal geodesic exists, the standard antipodal extension lemma excludes any monochromatic geodesic of length n-1. Consequently A is a centrally antipodal, finite simplicial subcomplex of sd(boundary Q_n), of dimension at most n-2, containing the entire subdivided physical 1-skeleton.

**Research payoff.** This replaces the doubled 2n-bit coordinates and cross-fiber bookkeeping by an honest centrally symmetric subcomplex of the barycentric subdivision of the ORIGINAL Q_n. A proved topological forcing theorem would say: for every antipodally odd edge coloring, its monochromatic geodesic-prefix FLAG subcomplex contains the barycenter of Q_n. Equivalently, no antipodally symmetric edge-coloring can produce an (n-2)-dimensional subcomplex A of sd(boundary Q_n) with precisely these rooted monochromatic flag-admissibility rules. This is an exact topological restatement with literal geodesic certificates at all face barycenters; no abstract label coincidence or fractional false intersection is involved. A general Sperner/Tucker/Hex forcing argument for these flag rules is still OPEN.

**Scope.** This is the ordinary antipodally odd EDGE-colored proving ground. For ordered-three-face NORI, path admissibility must be defined using the actual three-face color word and at-most-one-change acceptance (or its finite two-ended memory), with further seam compatibility before applying common-target extraction.
