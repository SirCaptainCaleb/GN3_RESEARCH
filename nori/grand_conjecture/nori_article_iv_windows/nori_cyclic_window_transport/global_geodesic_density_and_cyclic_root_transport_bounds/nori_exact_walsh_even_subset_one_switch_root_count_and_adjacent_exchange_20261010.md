# Exact nonlinear Fourier count of good physical roots and local adjacent-transposition conservation equations

# Exact Walsh–Fourier identity for one-switch rooted geodesics, with local adjacent-order transport

Let n>=3. Fix ANY legal physical ordered-three-face NORI coloring c and ANY full direction order p=(p_1,...,p_n). For each cube starting vertex x write W_p(x)=(W_1(x),...,W_L(x)) for the genuine consecutive ordered three-face colors, where L=n−2. Let G_p be the number of starting cube vertices for which this word has at most one change.

For every S⊆[L], define the real multilinear-root correlation
  rho_p(S)=2^(−n) * sum_(x∈F_2^n) (−1)^(sum_(i∈S) W_i(x)).
For every EVEN-cardinality S, define the explicit integer coefficient
  a_L(S)=sum_(t=0)^(L−1) (−1)^|S∩{1,...,t}|.
In particular a_L(empty)=L. All quantities refer to actual physical face colors along genuine antipodal n-edge geodesics; no affine, fiber-flatness, or coordinate-only hypothesis is assumed.

**THEOREM (exact nonlinear one-switch Fourier certificate).**
  G_p = 8 * sum_(S⊆[L], |S| even) a_L(S)*rho_p(S)
      = 8 * [L+sum_(even S≠empty) a_L(S)*rho_p(S)].

Therefore this FIXED direction order has a good full rooted geodesic if and only if
  L+sum_(even S≠empty) a_L(S)*rho_p(S)>0.
If it has no good starting root, the following EXACT spectral obstruction equality holds:
  sum_(even S≠empty) a_L(S)*rho_p(S)=−L.
In particular the sufficient correlation bound
  sum_(even S≠empty) |a_L(S)|*|rho_p(S)| < L
forces a good full geodesic, even with arbitrarily nonlinear exterior-face dependence.

For a pair S={i,j}, 1<=i<j<=L, one has
  a_L({i,j})=L−2(j−i).
Thus pairwise root-color correlations enter the exact certificate with an explicit signed separation-distance kernel.

**Proof.** For an arbitrary binary word w=(w_1,...,w_L) define 1_good(w) as the indicator of at most one switch. Its Walsh coefficient at S is
   H(S)=sum_(w good) (−1)^(sum_(i∈S) w_i).
Good words occur in complementary pairs (w,1−w), so H(S)=0 when |S| is odd. For even S, enumerate 0^t 1^(L−t) and their complements for t=0,...,L, noting that the two constant words occur twice in this list. Then
  H(S)=2 sum_(t=0)^L (−1)^|S∩{t+1,...,L}| −2
      =2 sum_(t=0)^(L−1) (−1)^|S∩{1,...,t}|
      =2a_L(S).
The second equality uses |S| even and removes the duplicate constant terms. Walsh inversion gives
  1_good(w)=2^(−L) sum_S H(S)(−1)^(sum_(i∈S) w_i).
Average over all 2^n physical starting cube roots x. As n−L=2, multiply by 2^n to obtain G_p=2^(n−L+1) sum_even a_L(S)rho_p(S)=8 sum_even a_L(S)rho_p(S). This proves every assertion, including positivity equivalence since G_p is a nonnegative integer. For S={i,j}, the prefix parity is odd precisely when i<=t<j, giving a_L=L−2(j−i). QED.

**LOCAL SPECTRAL EXCHANGE LEMMA.** Suppose p' is obtained from p by swapping adjacent directions at positions j,j+1. Define the affected-window index set I=[j−2,j+1]∩[1,L]. For every root x,
  W_i(x,p')=W_i(x,p)   for i∉I,
with exactly the same physical three-face and same ordered free directions. Hence
  rho_(p')(S)=rho_p(S) whenever S∩I=empty.
If a hypothetical NORI counterexample makes both p and p' rootwise bad, subtracting their exact Fourier obstruction equalities gives the local identity
  sum_(even S:S∩I≠empty) a_L(S)*(rho_p(S)−rho_(p')(S))=0.
This applies to every adjacent permutation exchange and expresses a finite-range spectral conservation equation over the full permutation graph.

*Proof.* An adjacent swap changes the intermediate cube vertex inside the two-direction square. Before the swap the path prefixes agree, and after both directions have been traversed the prefixes agree again. An ordered-three-face window outside I has the same free ordered triple and same fixed exterior bits in the two paths. Products of its signs and their cube-root averages agree. All untouched terms cancel upon subtracting the two zero-count Fourier identities. QED.

**AFFINE SPECIALIZATION (links to seam Jacobians).** If the fixed-order color-word map is affine W_p(x)=A_px+d_p over F_2, then
 rho_p(S)=(-1)^(sum_(i∈S)d_(p,i)) when A_p^T 1_S=0, and rho_p(S)=0 otherwise.
Thus the exact universal Fourier identity becomes a finite signed sum over even words in the left kernel of A_p. The previously proved near-surjective seam-Jacobian criterion is a structured case of this general nonlinear certificate.

**Research direction.** The grand conjecture is equivalent to showing that for every legal c at least one direction order p has a strictly positive spectral sum. If none does, every permutation order satisfies an exact cancellation of its trivial contribution L by higher even correlations, and every adjacent swap satisfies the localized conservation equation above. A promising next step is to use actual physical-face overlap and antipodal reversal to show that this global system of exact cancellations cannot hold simultaneously. This avoids imposing any false independence or constant-exterior assumptions.
