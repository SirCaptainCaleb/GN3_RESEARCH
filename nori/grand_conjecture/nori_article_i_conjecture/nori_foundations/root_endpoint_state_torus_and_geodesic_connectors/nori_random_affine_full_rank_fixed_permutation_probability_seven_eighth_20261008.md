# Most affine NORI colorings have eight monochromatic roots on any fixed direction order

# Random affine NORI: most colorings are full-rank at EVERY chosen permutation with a quantitative constant bound

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
