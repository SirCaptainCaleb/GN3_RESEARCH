# Corrected two-bit carrier lift multiplies longest additive paths by four up to O(1)

## Statement

Let B be any finite nonzero domain in an elementary abelian 2-group, let L=L(H(B))>=1, and let A=((B union {0}) x F_2^2)\{0}. Then L(H(A))>=4L-1. If L is even, the stronger bound L(H(A))>=4L+3 holds. Moreover |A|=4|B|+3 and |E(H(A))|=16|E(H(B))|+6|B|+1. Consequently repeated exact two-bit carrier lifts cannot asymptotically improve the normalized density/path-length ratio of a construction family.

## Body

Take a longest linear path of length L in H(B), and let C subset B be its support, so |C|=2L+1.

If L is even, apply the corrected even fourfold-lift lemma to the spanning P_L in H(C). This gives a P_{4L+3} in
  ((C union {0}) x F_2^2)\{0},
an induced subdomain of A. Hence L(H(A))>=4L+3.

If L is odd, delete one endpoint edge from the longest path. The remaining path has even length L-1 and support C' of size 2L-1. Applying the corrected even fourfold-lift lemma gives a path of length
  4(L-1)+3=4L-1
inside A.

Thus universally L(H(A))>=4L-1, with the stronger 4L+3 bound when L is even. This parity is forced by the PG(3,2) exception: for L=1 the stronger bound would incorrectly give 7.

For the size and edge count, perform the one-bit carrier lift twice. If a domain D has v vertices and m additive triples, its one-bit full preimage D^+ has 2v+1 vertices. It has v vertical triples and four lifted triples above each old additive triple, hence e(D^+)=v+4m. Applying this again gives
  |A|=4v+3,
  e(A)=16m+6v+1.

Therefore, for any family with L_i->infinity, a fixed number of exact two-bit carrier lifts multiplies vertex count and edge density by four per lift up to additive O(1), while longest-path length is multiplied by at least four up to additive O(1). Hence the limsup of |E|/(|V|(L+1)) cannot increase under such lifts.

This repairs the parity error in math_version 1; the universal asymptotic fence survives.