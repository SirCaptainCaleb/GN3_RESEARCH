# Every density-beating induced Boolean counterexample contains a non-Hamiltonian exact one-bit core

## Statement

Let A subset F_2^d\{0}, |A|=n=2ell+1+t, and suppose H(A) is P_ell-free while |E(H(A))|/n>(ell-1)/3. Then A contains an induced subdomain A0 of odd size n-k with k<=t such that A0 is an exact full one-bit Boolean lift of a quotient domain B, and H(A0) has no spanning linear path. Consequently the entire density-beating induced x+y construction problem reduces, without any defect-absorption loss, to classifying non-Hamiltonian exact one-bit lifts.

## Body

Apply the almost-period lemma 1e6e60eb6c56. There is x in A for which the translation boundary
  k=b_S(x)
of S=A union {0} satisfies k<=t and k==t mod 2. Delete from S the unique S-point in each of the k crossing x-pairs. The resulting S0 satisfies S0+x=S0, contains 0 and x, and has
  |S0|=n+1-k.
Put A0=S0\{0}. Then
  |A0|=n-k=2ell+1+(t-k),
which is odd because t-k is even.

Since S0 is invariant under the order-two subgroup <x>, quotient by <x>. For T=S0/<x> and B=T\{0}, after choosing fiber coordinates one has exactly
  A0=((B union {0}) x F_2)\{(0,0)}.
Thus A0 is an exact full one-bit Boolean carrier lift of B.

Suppose H(A0) had a spanning linear path. Its length would be
  (|A0|-1)/2
  = (n-k-1)/2
  = ell + (t-k)/2
  >= ell.
Because H(A0) is an induced subhypergraph of H(A), the first ell edges of that spanning path would give P_ell in H(A), contradicting the hypothesis.

Therefore H(A0) is non-Hamiltonian.

No estimate on the number of edges surviving the deletion is required. In particular, the <=t defects supplied by 1e6e60eb6c56 need not be absorbed back into a carrier path: Hamiltonicity of the exact core alone already contradicts P_ell-freeness.

Combining with the compatible two-rail criterion 47949910006a, every density-beating induced Boolean counterexample must produce a quotient B whose one-bit lift is non-Hamiltonian, hence B admits no pair of spanning paths with a common endpoint satisfying the even-subhypergraph parity condition (and in particular no such pair with independent combined incidence rows).
