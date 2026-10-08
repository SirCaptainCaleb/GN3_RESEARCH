# Hamiltonian support pairs and Smith chains give a direct closure target — preserved pre-item development

## Development

## Audit status: the universal lifting proposal is refuted

The conditional closure criterion, source-index calculation, and Smith-chain implication below remain valid. The proposed universal map Delta Q_n -> K(H), and the assertion that every H admits Smith chains through degree n-4, are false. An explicit edge-ordered six-vertex tournament already has a two-cover but admits no length-two Smith chains; see [[audit_universal_support_pair_smith_lifting_is_refuted_by_an_explicit_cochain]]. Any surviving application must construct chains using additional counterexample-specific hypotheses. Full support rank is not maximal equivariant index.

## Support pairs, equivariant rank, and a direct closure target

### Diagnosis of the earlier proof steps

The extreme-root map records positions of defects; positive balance yields a circulation among positional roots. It does not yield a spanning pair of paths. Order-agreement arguments then attempt to lift positional information back to paths, and local surgery repeatedly returns Hamiltonian supports without retaining a spanning conversion.

A different candidate target retains actual Hamiltonicity but forgets chosen path orders: the order complex of disjoint Hamiltonian support pairs. Order disagreement is not an obstruction in this target. A vertex records existence of two Hamilton orders, not a compatible choice of those orders across other vertices.

This is a proposed route, not a proof that the target always has the requisite equivariant topology.

### Definition and normalization

For n>=5 let P(H) consist of ordered pairs (A,B) of disjoint subsets of V(H), each of cardinality at least two, such that H[A] and H[B] are Hamiltonian. Order pairs by componentwise inclusion. Let K(H)=Delta P(H), its order complex. The involution T(A,B)=(B,A) is free on its geometric realization: ranks are distinct in a chain and T preserves ranks, so no simplex is setwise invariant.

For n>=4, H has a two-cover if and only if P(H) contains a pair with A union B=V(H). To normalize a singleton side, move an endpoint of the other path to the singleton; the resulting two-vertex path is vacuously tight and the remaining contiguous path has at least two vertices. A Hamilton path can instead be split into blocks of orders two and n-2.

Hamiltonian support families need not be downward closed. P(H) is an ordinary poset, not the face poset of a purported simplicial complex of all Hamiltonian subsets. Its simplices are chains of separately certified Hamiltonian sets. No hereditary Hamiltonicity is assumed.

### Rank obstruction

If H has no two-cover, every pair has 4<=|A|+|B|<=n-1. A strict inclusion increases this total, so dim K(H)<=n-5.

There is also an explicit equivariant map K(H)->S^(n-5). Fix a total order on V(H), assign rank r=|A|+|B|-3 in {1,...,n-4}, and sign + if the least vertex of A union B is in A, minus otherwise. Send (A,B) to the signed r-th vertex of the crosspolytope. Ranks in a chain are distinct, so its labels contain no opposite pair. Extend simplicially. Swapping A,B negates every label.

Consequently an equivariant map S^(n-4)->K(H) would force a spanning two-cover, by Borsuk--Ulam. The conversion is immediate from rank; it requires no endpoint matching or bounded-support handoff.

### An orientation-independent source of the correct dimension

Let Q_n be the same support-pair poset without Hamiltonicity restrictions. Its equivariant index and coindex are both n-4.

Proof of the lower bound. Choose distinct reals t_1<...<t_n and let
L={x in R^n: sum x_i=sum t_i x_i=sum t_i^2 x_i=0}.
The three constraints are independent, so its unit sphere has dimension n-4.

Every nonzero x in L has at least two positive and at least two negative coordinates. If i were its unique positive coordinate, dividing the negative coefficients by x_i would express both t_i and t_i^2 as their convex averages. The resulting variance sum w_j(t_j-t_i)^2 would be zero, impossible for distinct t_j. Apply the same argument to -x.

The coordinate-hyperplane arrangement decomposes S(L) into antipodal spherical polyhedral cells. Each cell has constant positive support A and negative support B, both of order at least two. Faces have smaller supports, so their face poset maps equivariantly and monotonically to Q_n. Its barycentric subdivision gives S^(n-4)->Delta Q_n.

For the upper bound, the rank-label map above, now allowing total n and ranks 1,...,n-3, gives Delta Q_n->S^(n-4). This establishes both index bounds without any condition on H.

One concrete sufficient transport theorem is therefore an equivariant map Delta Q_n->K(H). This assertion is now refuted as a universal theorem; see the audit above. The source construction alone supplies no Hamiltonicity.

### A weaker algebraic target: Smith chains

Geometric carrier extension may be stronger than needed. Work over F_2. Write N=1+T on simplicial chains of K(H), with the usual augmentation on zero-chains.

Theorem. Suppose there are chains c_i in C_i(K(H);F_2), 0<=i<=d=n-4, satisfying
aug(c_0)=1,
boundary(c_i)=N c_(i-1) for 1<=i<=d.
Then H has a two-cover.

Proof. If H had no two-cover, dim K(H)<=d-1, hence c_d=0 and N c_(d-1)=0. On each free simplex orbit, ker N=im N. Therefore c_(d-1)=N b_(d-1). Descending inductively through the boundary equations yields
c_j=boundary(b_(j+1))+N b_j
for j=d-2,...,0. Augmenting the last equation gives aug(c_0)=0, contradiction. The d=1 case is the same argument with c_1=0. Thus a spanning support pair exists.

These are Smith-chain identities, not merely a circulation of defect-root labels. They give an explicit algebraic closure certificate without asserting contractibility of every carrier or compatibility of path orders.

### Where later local results can move earlier

Hamiltonian four/five-support results provide vertices of P(H), not closure. A useful strengthening would show that these vertices and mixed support pairs fill a specified chain boundary. Four-of-six and prescribed-deletion variants naturally supply incidence information for such fillings. Seed-preserving enlargement supplies comparable vertices, but must not be assumed to give an equivariant contraction.

The relevant next obligation is to construct the Smith chains, or a map from the source sphere, permitting vertices to move between A and B. The accompanying frozen-support obstruction proves that carriers confined to the original two sides can already fail on a fixed local configuration.

This route removes the automatic one-sided facets through the source's two-sign requirement, rather than excluding facets ad hoc. It preserves dissimilar support states instead of first asking their path orders to agree. The universal transport theorem and universal Smith-chain existence are refuted; a counterexample-specific construction remains an open possibility.
