# Affine change syndromes and exact root-count phenomena

# Affine change syndromes and exact root-count phenomena

Fix a coordinate order and vary the starting vertex in an affine coloring of physical ordered faces. The successive color changes are affine functions of the root bits; good paths correspond to syndrome vectors of Hamming weight at most one. This linear-algebraic translation gives exact fiber counts, quantitative generic success and sharp rank-deficient obstructions.



*Exact scoped proof in note* note_nori_carrier_requires_joint_actual_geodesic_witnesses.

## Random affine NORI: most colorings are full-rank at EVERY chosen permutation with a quantitative constant bound

Consider the affine-exterior ordered-three-face family
 c(F,(i,j,k))=h(i,j,k)+sum_(t notin{i,j,k}) a_(i,j,k),t z_t,
where all bits are mod2. Impose active NORI antipodal-reversal oddness by choosing the coefficient vector and intercept freely and uniformly for one ordered-triple in each reversal pair, and defining the reversed triple on the antipodal face by the complementary rule. In particular, for any FIXED full direction permutation pi, the exterior coefficient vectors L_1,...,L_(n−2) associated with its consecutive ordered triples are independent and uniformly random on the coordinate subspaces outside their respective free triples: none of these ordered triples is the reverse of another since pi uses distinct directions.

Let m=n−3 and form the affine full-geodesic change vector D_pi(x)=b+M x∈F2^m, where the slope of its jth row is L_j+L_(j+1). The random intercepts do not affect rank.

**Theorem (explicit rank failure probability).** For EVERY fixed direction order pi and all n>=4,
 P(rank M < m)
 <= 1/8 + (4n−14)/2^n.
In particular this bound is <=5/16 for all n>=4 (with its maximum at n=5), so
  P(rank M=n−3) >= 11/16
for every n>=4; the probability lower bound tends to 7/8 as n→∞.

Whenever rank M=n−3, for EVERY binary change pattern y∈F2^m exactly eight starting roots produce D_pi(x)=y. Hence at least 11/16 of the randomly sampled valid AFFINE NORI colorings have exactly eight fully monochromatic antipodal pi-geodesics for this SINGLE user-prescribed order and exactly 8(n−2) good <=1-switch pi-geodesics.

**Proof (first moment of the left kernel).** Write the (m+1)×n matrix L with rows L_1,...,L_(m+1), and the m×(m+1) successive-difference matrix ∂, so M=∂L. For any nonzero row vector t∈F2^m, put w=t∂∈F2^(m+1). The map t→w bijects F2^m with the EVEN-parity subspace of F2^(m+1), so w is nonzero of even Hamming weight at least two. The random row combination tM=wL is uniform on exactly the union of the EXTERIOR coordinate supports of windows j with w_j=1: for a coordinate i, it is the XOR of independent uniform coefficients from the selected rows whose free triples omit i, and random bits from different coordinates i are independent. If the intersection of the selected windows' free triple sets has size a, this union has size n−a, so
   P(tM=0)=2^(−(n−a)).
For two selected windows a distance1 apart, a=2; a distance2, a=1; distance>=3, a=0. For FOUR or more distinct selected windows, a=0 because any coordinate belongs to at most three consecutive length-three windows. There are exactly m weight-two supports at distance1 and m−1 at distance2; all remaining 2^m−1−(2m−1) nonzero even supports have exterior union size n.

Thus the EXPECTED number of nonzero vectors in ker(M^T) is exactly
 E(|ker(M^T)|−1)
  = m*2^(−(n−2)) + (m−1)*2^(−(n−1)) + (2^m−1−(2m−1))*2^(−n)
  = 1/8+(4n−14)/2^n.
If M is rank-deficient, its left kernel has at least one nonzero vector. Markov's inequality (or union bound) yields P(rank M<m) <= this expectation. The sequence is <=5/16 for n>=4, with equality of the BOUND at n=5 (directly check n=4 and n=5 and that (4n−14)/2^n decreases thereafter). QED.

**Scope.** This shows affine NORI counterexamples, if any, are not remotely generic: even a PRESCRIBED direction order has probability bounded far above one half of admitting a monochromatic full antipodal geodesic, uniformly in dimension, and tending to at least 7/8. This is a probability statement about a well-defined uniform ensemble of valid affine-exterior colorings, NOT proof that every coloring or every affine coloring has a good path. The full NORI grand conjecture is still open.

## Global sparse-slope stability around the full exterior-parity affine coloring

Let n>=4. Consider ANY binary coloring c of physical ordered three-faces of Q_n that is affine in the exterior cube bits, with arbitrary orientation-dependent intercepts. For each ordered triple \(\pi=(a,b,c)\) of distinct coordinates, write its exterior coefficient vector \(A_\pi=(a_{\pi,t})_{t\notin\operatorname{set}\pi}\). Let \(P_\pi\) be the full exterior-parity coefficient vector with ALL entries 1. Let
\[
\mathcal E=\{\pi:A_\pi\ne P_\pi\},\qquad M=|\mathcal E|\le n(n-1)(n-2).
\]
The intercept bits on all triples are unrestricted. Active NORI antipodal-reversal oddness may hold but is NOT REQUIRED for this result.

**Theorem (sparse affine perturbation closure).** There exists a full antipodal directed cube geodesic whose ordered-three-face window colors change at most
\[
\boxed{\left\lfloor\frac{M}{n(n-1)}\right\rfloor}
\]
times (with the trivial cap n-3 if desired). In particular:
- If M<n(n-1), there exists a FULL MONOCHROMATIC antipodal geodesic.
- If M<2n(n-1), there exists a full antipodal geodesic with AT MOST ONE window-color change, proving the active NORI conclusion for this affine class even without imposing its oddness axiom.

**Proof.** Choose a uniformly random permutation p=(p_1,...,p_n). A fixed ordered triple \pi appears as one of its n-2 consecutive three-direction windows with probability
\[
\frac{n-2}{n(n-1)(n-2)}=\frac1{n(n-1)}.
\]
Let K(p) count the windows whose ordered triples belong to \mathcal E. By linearity of expectation,
\[
\mathbb E K(p)=\frac{M}{n(n-1)}.
\]
Therefore SOME order p satisfies K(p)≤floor(M/[n(n-1)]).

For a fixed such p, write the n-2 ordered window colors as the affine vector C_p(x)=h_p+L_p x over F2, where x is the starting root. Let L_0 be the coefficient matrix for the parity-baseline coloring with slope 1 on every exterior coordinate (but the same arbitrary intercepts); L_p-L_0 has nonzero rows at no more than K(p) exceptional windows, so rank(L_p-L_0)≤K(p). Apply consecutive difference operator \partial to obtain the (n-3)×n change matrices M_p=\partial L_p and M_0=\partial L_0. The rows of M_0 are EXACTLY
\[
e_{p_i}+e_{p_{i+3}},\quad 1\le i\le n-3,
\]
because consecutive three-face exterior masks differ only in the exiting direction p_i and entering direction p_{i+3}. These rows form the edge-incidence vectors of three disjoint paths on the coordinate positions modulo 3 and are linearly independent; hence rank M_0=n-3.

By rank perturbation,
\[
\operatorname{rank}M_p\ge n-3-K(p).
\]
The affine syndrome theorem (also proven independently: for any affine map F2^n→F2^{n-3} with rank r, its affine image contains a vector of Hamming weight at most n-3-r) yields a root x for which the full p-geodesic has at most K(p) changes. Combined with the expectation bound, this proves the claimed floor(M/[n(n-1)]) bound and its two threshold corollaries. QED.

**Interpretation.** This is a structural all-dimension closure theorem: an affine NORI coloring may perturb an arbitrary set of up to roughly \(2n^2\) orientation-triple exterior slopes away from the uniform parity baseline and still MUST have a full one-switch antipodal geodesic. The proof has TWO independent ingredients: permutation averaging to avoid most exceptional ordered triples, and a full-rank three-residue incidence matrix on the remaining windows. It is a genuine subclass result, not a proof for arbitrary nonlinear or dense exceptional-slope NORI colorings.

These results solve broad affine and near-affine subclasses and quantify the exceptional linear ranks. They do not assert the unrestricted NORI theorem, where the exterior-bit dependence need not be affine.
