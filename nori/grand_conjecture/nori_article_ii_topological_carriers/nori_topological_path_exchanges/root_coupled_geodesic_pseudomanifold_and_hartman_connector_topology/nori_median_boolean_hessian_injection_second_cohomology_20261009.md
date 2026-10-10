# Median cocycles: nonlinear Boolean functions inject into second geodesic cohomology

# Explicit nonlinear-Boolean second cohomology in the all-root cube-geodesic complex

Let n>=2 and K_n be the all-root geodesic simplicial pseudomanifold (its simplices are vertex subsets of full antipodal cube geodesics). For each 2-simplex {u,v,w}, exactly one vertex m is BETWEEN the other two in Hamming distance; call m its median. For any Boolean function f:{0,1}^n -> F_2 define a 2-cochain A_f by A_f({u,v,w})=f(m).

**THEOREM (injective nonlinear-functions-to-H^2 map).** Every A_f is a 2-cocycle, and [A_f]=0 in H^2(K_n;F_2) if and only if f is affine linear over F_2. Consequently

F_2^({0,1}^n) / Aff(n,2)  EMBEDS into H^2(K_n;F_2),
dim H^2(K_n;F_2) >= 2^n-n-1.

The classes of A_f for the Boolean monomials f(x)=product_(i in I) x_i with |I|>=2 are linearly independent; there are exactly 2^n-n-1 of them.

*Proof of cocycle condition.* Every 3-simplex is the vertex set of a Hamming-collinear ordered four-tuple v_0,v_1,v_2,v_3. Its four triangle faces, formed by deleting v_0,v_1,v_2,v_3, have medians v_2,v_2,v_1,v_1 respectively. Hence delta A_f = f(v_2)+f(v_2)+f(v_1)+f(v_1)=0.

*Proof that affine f yield coboundaries.* For constant f=1, A_f is the coboundary of the constant-one 1-cochain on every edge, as a triangle has three edges. For coordinate f(x)=x_i define the edge 1-cochain B_i({u,v})=u_i v_i (ordinary product of the endpoint bits). Along a Hamming-collinear triple (u,m,v), the sequence of i-th bits is one of 000,001,011,100,110,111. Directly in all six cases,
B_i({u,m})+B_i({m,v})+B_i({u,v})=m_i.
Thus A_(x_i)=delta B_i. Linearity establishes triviality for affine f.

*Proof of converse and explicit detecting cycles.* For every coordinate 2-face (square) with corners a,a+e_i,a+e_j,a+e_i+e_j, all four of its vertex triples are K_n 2-simplices, forming the boundary S^2 of a tetrahedron whose full four-vertex set is absent from K_n. On these four triangles the intrinsic median takes each corner exactly once. The evaluation of A_f on the mod-2 square sphere is exactly
f(a)+f(a+e_i)+f(a+e_j)+f(a+e_i+e_j),
the Boolean mixed second difference Delta_i Delta_j f(a).
If A_f is a coboundary, it evaluates zero on every 2-cycle, so every mixed square difference vanishes. Consequently the first difference Delta_i f(x)=f(x)+f(x+e_i) is invariant under all translations e_j for j≠i; it is also invariant under e_i, hence it is constant on the cube. Therefore f(x)=f(0)+sum_i f(e_i)+f(0) times x_i, an affine function. This proves exactly the claimed kernel and dimension lower bound.

**Finite low-dimensional check (evidence, not an all-n equality theorem).** Exact F_2 boundary-matrix reduction gives (n,dim H^2)=(2,1),(3,4),(4,11),(5,26), matching 2^n-n-1 in every tested case. It remains to prove whether the explicit nonlinear-function classes span ALL H^2(K_n;F_2) for arbitrary n.

**Meaning for grand NORI.** Even though K_n has trivial pi_1 (the preceding Item), it has at least exponentially many independent degree-2 cohomology classes from Boolean nonlinearities. Each has a concrete coordinate-square-sphere detector. This forbids assuming low-dimensional acyclicity of the complete physical root-geodesic carrier and suggests using second differences/curvature of physically rooted face labels as a topology-to-color interface. A cocycle evaluation yielding a physical one-switch geodesic is still required to close the grand conjecture.

**Independent n=6 extension.** Exact mod-2 reduction gave f_1=2016, f_2=19264, rank(partial_2)=1953 by simple connectivity, and rank(partial_3)=17254; hence dim H^2=19264−1953−17254=57=2^6−6−1. Moreover the 240 coordinate-square spheres, taken modulo third-boundaries, span exactly 57 independent classes. Therefore the explicit Boolean-median classes exhaust degree-two cohomology for every n=2,...,6 tested. The all-dimensional equality and square-sphere spanning remain unproved.
