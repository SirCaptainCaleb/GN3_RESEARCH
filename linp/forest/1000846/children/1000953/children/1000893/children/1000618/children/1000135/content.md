# Rank-nullity forces a small zero-sum block in the joint set

## Statement

In the joint-residue setting, suppose XOR(A)=0 and the joint set J has k=ell-1 elements spanning rank at most d. If k>=d+2, then J has a proper zero-sum subset S with 3<=|S|<=floor(k/2). For PG(3,2), k=6 and d=4, so |S|=3 and its complement also has size 3 and sum zero; hence the six joints split into two projective lines. This numerical collapse is specific to the six-joint rank-four case.

## Body

Let M be the d-by-k binary matrix whose columns are the distinct nonzero vectors of J. Since XOR(J)=XOR(A)=0, the all-ones vector 1_J lies in ker M. Because
  dim ker M >= k-d >= 2,
there is another nonzero kernel vector c distinct from 1_J. Let S be its support. Then S is nonempty and proper and
  XOR(S)=0.
Since XOR(J)=0, the complement J\S also has XOR zero. Replace S by its complement if necessary so that
  |S|<=floor(k/2).

A zero-sum subset of distinct nonzero vectors cannot have size one, and cannot have size two because x+y=0 over F_2 implies x=y. Hence |S|>=3, proving
  3<=|S|<=floor(k/2).

For PG(3,2), a spanning P_7 would have k=6 joints in F_2^4. Thus k=d+2 and floor(k/2)=3, forcing |S|=3. Its complement also has size three and sum zero. Each zero-sum triple {a,b,c} of distinct nonzero binary vectors satisfies c=a+b and is exactly the set of nonzero vectors of a 2-dimensional subspace. The two triples are disjoint, so their 2-dimensional subspaces meet only in zero and hence are complementary in F_2^4. This recovers the two-line decomposition in the new P7 proof.

For k>6 the argument only produces a zero-sum block of some size between 3 and floor(k/2); it no longer forces the complement to be another triple. In particular the mechanism does not by itself propagate to higher projective dimensions.
