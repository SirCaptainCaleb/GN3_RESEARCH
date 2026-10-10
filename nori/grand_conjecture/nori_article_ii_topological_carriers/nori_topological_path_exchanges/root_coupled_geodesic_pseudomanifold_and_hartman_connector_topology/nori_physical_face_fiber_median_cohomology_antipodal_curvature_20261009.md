# Actual ordered-three-face exterior curvature gives reversal-paired cohomology classes

# Physical ordered-three-face color fibers as median 2-cohomology classes

Fix n>=5 and the all-root cube-geodesic complex K_n. For each ordered triple t=(a,b,c) of distinct coordinate directions and a valid NORI coloring, define the Boolean function f_t(z) to be the color of the physical ordered t-face whose exterior coordinates agree with z. The function f_t is invariant under flipping any of its three free coordinates.

The NORI antipodal-reversal condition is exactly
f_(reverse t)(bar z)=1+f_t(z), with arithmetic in F_2.

For every t, assign to a geodesic 2-simplex {u,m,v}, where m lies between u and v, the value A_t({u,m,v})=f_t(m).

**THEOREM (exterior curvature in honest all-root cohomology).**
(1) A_t is a 2-cocycle on K_n. Its class vanishes in H^2(K_n;F_2) if and only if f_t is affine in its n−3 exterior bits.
(2) Under the cube complement involution tau on K_n, tau^*[A_(reverse t)]=[A_t]. Thus each reversal pair of ordered direction triples defines a single naturally paired, equivariant class.
(3) For each reversal orbit {t,reverse t}, the class [A_t] ranges freely through a subspace of dimension
2^(n−3)−(n−3)−1 = 2^(n−3)−n+2
as the allowed color fiber varies. The face-fiber parameters can be assigned independently for all 3 binom(n,3) reversal orbits. Their images lie in the SAME H^2(K_n;F_2) and may be linearly dependent there; independence means arbitrary simultaneous realizability of the indexed assignments, with no universal cross-orbit relation forced by antipodal reversal.

*Proof.* The preceding median Boolean cocycle theorem proves (1): the 2-cocycle of an arbitrary cube Boolean f is exact precisely for affine f. Here f_t ignores the three coordinates in t, so affinity in n variables is equivalent to affinity in the n−3 exterior variables.

For (2), applying the involution to a simplex sends its median m to bar m. Thus
(tau^*A_(reverse t))({u,m,v})=f_(reverse t)(bar m)=1+f_t(m)=1+A_t({u,m,v}).
The constant-one 2-cochain is the coboundary of the constant-one 1-cochain, so the two cohomology classes agree.

For (3), there are 2^(n−3) Boolean functions on the exterior cube as an F_2 vector space, and its affine subspace has dimension n−2. By (1), the quotient injects into H^2(K_n;F_2) with the claimed dimension. One may prescribe f_t completely arbitrarily for one representative of each reversal orbit and then uniquely define its partner by f_(reverse t)(z)=1+f_t(bar z). These prescriptions satisfy the full NORI antipodal-reversal condition and impose no requirements between distinct ordered-triple reversal orbits. Thus all the indicated class parameters are freely realizable.

**Explicit physical detectors.** For exterior directions i,j outside t, evaluate A_t on the tetrahedral boundary S^2 formed by the four vertices of any physical i,j square. The evaluation is
f_t(z)+f_t(z+e_i)+f_t(z+e_j)+f_t(z+e_i+e_j),
the actual mixed exterior Boolean derivative. These local square evaluations completely detect whether the fiber class is zero.

**Strategic consequence.** This supplies a canonical color-dependent high-dimensional topological interface: each oriented three-face fiber contributes a genuinely geometric second-cohomology class and a complete table of physical exterior-square curvature. Oddness pairs the classes under reversal but allows arbitrary nonlinear complexity across triples. A grand-extraction argument must also exploit compatibility between consecutive ordered triple windows along genuine cube geodesics. In particular, nonzero exterior curvature alone is compatible with legal colorings and cannot serve as a universal contradiction.
