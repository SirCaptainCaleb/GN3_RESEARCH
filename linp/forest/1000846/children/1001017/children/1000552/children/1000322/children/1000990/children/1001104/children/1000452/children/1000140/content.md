# Steiner deficiency two forces pair-universal vertices

## Statement

In an exact-density P_ell-free equality obstruction with n=6d+3 (Steiner deficiency s=2), the leave graph has even degrees and average degree 2 but cannot be 2-regular. Hence it has a degree-zero vertex, corresponding to a pair-universal vertex of H of degree 3d+1. If ell=0 mod3, the leave spike Delta>=6 forces at least two such pair-universal vertices; in residues 1 and 2 at least one is forced.

## Body


Let H be an exact-density P_ell-free linear triple system with
  |E(H)|=d|V(H)|,  d=floor(2ell/3),
and suppose its Steiner deficiency is
  s=n-(6d+1)=2.

Then n=6d+3 is odd, so by parity every leave degree is even. The leave U has average degree 2.

If U were 2-regular, then for every vertex
  d_H(v)=(n-1-2)/2=3d,
so H would be 3d-regular. The certified endpoint-potential floor would give a path of length
  ceil((3d+1)/2)>=ell,
contradiction. Therefore U is not regular.

Since all leave degrees are nonnegative even integers with average 2, nonregularity implies that some vertex has leave degree 0: if every leave degree were at least 2, the average 2 would force all degrees exactly 2.

A leave-isolated vertex a is pair-universal in H: every pair {a,x}, x!=a, is covered by a unique hyperedge. Equivalently
  d_H(a)=(n-1)/2=3d+1,
and the hyperedges through a induce a perfect matching on V(H) minus {a}.

More can be said by residue.

For ell≡0 mod3, 885251f8bcbc forces Delta(U)>=s+4=6. Relative to average 2, a degree-6 vertex contributes excess at least 4. Since the only degrees below 2 are zeros, and each zero contributes deficit 2, at least two leave-isolated vertices are necessary.

For ell≡1 mod3, parity plus nonregularity forces Delta(U)>=4 and at least one leave-isolated vertex.

For ell≡2 mod3, 885251f8bcbc gives Delta(U)>=s+2=4, again forcing at least one leave-isolated vertex.

Thus every s=2 equality obstruction has at least one pair-universal vertex, and residue 0 has at least two.
