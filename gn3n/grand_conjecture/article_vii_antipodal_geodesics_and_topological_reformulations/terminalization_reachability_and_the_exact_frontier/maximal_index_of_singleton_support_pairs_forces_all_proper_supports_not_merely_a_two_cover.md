# Maximal index of singleton support pairs forces all proper supports, not merely a two-cover

## Composition

(none yet)

## Development

This is a structural audit of the universal index/coindex proposals in 241 and 243, not a small-order cutoff argument. The counterexample-specific conditional criteria remain logically sufficient; the universal versions ask for substantially more than the grand conjecture.

A GENERAL MISSING-POINT LEMMA.
Let X be a closed antipodally invariant proper subspace of a standard antipodal d-sphere, d>=1. Choose p outside X. Then -p is also outside X. Orthogonal projection to p-perp, followed by normalization, gives a continuous equivariant map
X -> S^(d-1).
Its only zeroes on S^d are p and -p, neither in X. Thus index(X)<=d-1. The same conclusion holds for a proper invariant subcomplex of any equivariantly homeomorphic sphere.

THE UNRESTRICTED SINGLETON PAIR POSSET IS A SPHERE, NOT JUST AN INDEX MODEL.
Let Qhat_n be the poset of ordered disjoint nonempty subsets (A,B), ordered componentwise by inclusion.
Consider
Z_n={x in R^n: sum x_i=0, ||x||_1=1}.
This is the boundary of the convex body {sum x_i=0, ||x||_1<=1}, in its (n-1)-dimensional span, hence a standard antipodal S^(n-2) after radial normalization.
For nonempty disjoint A,B, its sign cell is
C_(A,B)={x_i>=0 on A, x_i<=0 on B, x_i=0 elsewhere,
sum_(i in A) x_i=1/2, sum_(i in B)(-x_i)=1/2}.
This is the product (1/2 Delta_A) x (-1/2 Delta_B), of dimension |A|+|B|-2.
Cell-face inclusion is exactly componentwise support inclusion. Consequently Delta Qhat_n is the barycentric subdivision of Z_n, equivariantly homeomorphic to S^(n-2).

Let Khat(H) be the subcomplex on actual Hamiltonian support pairs, allowing singleton supports, as in 241. Then, for n>=3,
index Khat(H)=n-2
IF AND ONLY IF
every nonempty proper subset of V(H) is Hamiltonian.
The reverse implication makes Khat(H)=Delta Qhat_n.
For the forward implication, if a proper nonempty S is non-Hamiltonian, the vertex (S,V-S) of Qhat_n is absent from Khat(H). Thus Khat(H) is a proper invariant closed subcomplex of the sphere. The missing-point lemma gives index Khat(H)<=n-3. Equivalently no equivariant S^(n-2)->Khat(H) can exist.

This extends the earlier audit 245 to the singleton-allowed target and gives a conceptual projection proof rather than a finite cochain certificate. A tournament with a proper bad four-set and an actual two-cover, such as the explicit edge-ordered example in 245, already refutes the universal maximal-index/sphere-map statement for Khat.

THE FULL DOWNWARD-CLOSURE TARGET HAS THE SAME ISSUE.
E(H) is an invariant subcomplex of the n-crosspolytope boundary S^(n-1). If it is proper, the missing-point lemma gives index E(H)<=n-2. Therefore index E(H)=n-1 requires E(H) to be the ENTIRE crosspolytope boundary.
In particular, whenever H itself is non-Hamiltonian, the all-positive full-support facet is absent, so E(H) is proper. Explicitly, the two points +/- (1/n,...,1/n) are absent and the projection
x -> (x-mean(x)1)/||x-mean(x)1||_2
maps E(H) equivariantly to S^(n-2).
This conclusion does not depend on whether empty witnessing supports are permitted: absence of Hamiltonicity of H already excludes the two full monochromatic facets. If witnesses must both be nonempty, those full monochromatic facets are absent even for Hamiltonian H.

Thus a UNIVERSAL n-1 index theorem for E(H) is false. The n-1 criterion remains a valid conditional contradiction target under minimum-counterexample assumptions, but cannot be justified by a theorem valid for all boundary tournaments.

CORRECTION TO THE STRATEGIC READING OF 274.
The equivalence in 274 for minimum counterexamples is unchanged. Its phrase 'the stronger bound index E(H)>=n-1 is the genuine closure target' must be read as a counterexample-specific conditional theorem, not a universal index lower bound for arbitrary H. Maximal absolute index is much stronger than existence of a spanning cover.

The correct existential invariant is the presence of at least ONE full-support cell. Relative homology against the lower-dimensional skeleton detects this cell without demanding that every full-support partition be allowed. A relative or counterexample-specific construction must replace the invalid universal maximal-index claim. No such construction is proved by this audit alone.
