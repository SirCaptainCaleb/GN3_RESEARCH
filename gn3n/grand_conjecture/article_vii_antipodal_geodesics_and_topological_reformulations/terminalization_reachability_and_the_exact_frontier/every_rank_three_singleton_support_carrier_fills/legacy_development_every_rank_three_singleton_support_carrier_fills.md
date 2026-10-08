# Every rank-three singleton-support carrier fills — preserved pre-item development

## Every rank-three singleton-support carrier fills

Continue from [[rank_three_support_pair_carriers_reduce_to_one_extreme_non_hamiltonian_four_block]].

All rank-three faces except one exceptional form already have contractible natural carriers. It remains to treat the case in which the unique non-singleton face block is the first block
\[
W,\qquad |W|=4,
\]
with \(H[W]\) non-Hamiltonian, while a nonempty common right support
\[
B_F
\]
survives. The final-block case is symmetric.

Choose
\[
b\in B_F.
\]

### 1. The boundary really sees only proper subsets of \(W\)

For every chamber \(\pi\) of the face, the canonical left support \(P_\pi\) meets \(W\) but cannot contain all of \(W\).

Indeed \(W\) is the first face block. If \(P_\pi\) contained all four vertices of \(W\), then the first four vertices of the displayed Hamilton order on \(P_\pi\) would be exactly the chosen order of \(W\), and their consecutive triples would make \(H[W]\) Hamiltonian, contradiction.

Hence
\[
\varnothing\neq P_\pi\cap W\subsetneq W.
\]
The same is true for the common-lower states used on chamber edges and rank-two boundary faces. Therefore the exceptional boundary carrier retracts onto the support-pair copy
\[
\{(S,\{b\}):\varnothing\neq S\subsetneq W\}.
\]
Every nonempty proper subset of \(W\) has order at most three and is Hamiltonian. Its order complex is the barycentric subdivision of
\[
\partial\Delta(W)\cong S^2.
\]

Thus the only possible rank-three obstruction is precisely this four-block \(S^2\).

### 2. A fifth vertex fills the sphere whether its five-set is good or bad

Assume \(|V(H)|\ge6\), and choose
\[
z\in V(H)-(W\cup\{b\}).
\]

There are two cases.

#### Case A: \(W+z\) is Hamiltonian

Then
\[
(W\cup\{z\},\{b\})\in\widehat{\mathcal P}(H)
\]
lies above every boundary state \((S,\{b\})\), \(S\subsetneq W\). Hence it cones the \(S^2\).

#### Case B: \(W+z\) is non-Hamiltonian

The audited five-set theorem says that a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. Since \(W\) itself is already non-Hamiltonian, it is the unique bad four-subset of \(W+z\).

Consequently, for every \(w\in W\),
\[
R_w=(W-\{w\})\cup\{z\}
\]
is Hamiltonian.

Therefore
\[
(R_w,\{b\})\in\widehat{\mathcal P}(H)
\qquad(w\in W).
\]
The union of their lower intervals contains exactly the barycentric support-pair model of
\[
z*\partial\Delta(W).
\]
Indeed the four maximal left supports \(R_w\) are the four tetrahedra
\[
\{z\}\cup(W-\{w\})
\]
of the cone on the tetrahedral boundary. Their common base is the family of all nonempty proper subsets of \(W\).

Since
\[
z*\partial\Delta(W)\cong B^3,
\]
these four mixed Hamiltonian supports fill the boundary sphere.

Thus a bad fifth vertex fills the obstruction by four mixed supports, while a good fifth vertex fills it by one cone apex.

### 3. The order-five ground case is already impossible

If \(|V(H)|=5\), choose any three vertices for one support and the remaining two for the other. Every three-set and every two-set is Hamiltonian, so \(H\) already has a spanning two-cover.

Hence a counterexample has enough room to choose the required \(z\).

### Conclusion

Every rank-three face of the permutahedron has a fillable carrier in the singleton-allowed support-pair target.

The key point is the dual use of the five-set theorem:
\[
\boxed{
W+z\text{ Hamiltonian }\Rightarrow\text{ cone};
\qquad
W+z\text{ non-Hamiltonian }\Rightarrow
\text{ all four replacement }K_4\text{s are Hamiltonian }\Rightarrow\text{ ball}.
}
\]

So the matching-block extension desert found earlier is **not** a genuine rank-three topological obstruction. Its bad extensions supply exactly the mixed supports needed to fill the sphere.

This is the first place where a later local theorem genuinely obsoletes an earlier frontier rather than merely refining it.

The next possible obstruction is rank four, where an extreme active block may have order five. There the analogous boundary is an \(S^3\), and the six-set theorem guarantees at least four Hamiltonian five-deletions but not automatically all five replacement facets.
