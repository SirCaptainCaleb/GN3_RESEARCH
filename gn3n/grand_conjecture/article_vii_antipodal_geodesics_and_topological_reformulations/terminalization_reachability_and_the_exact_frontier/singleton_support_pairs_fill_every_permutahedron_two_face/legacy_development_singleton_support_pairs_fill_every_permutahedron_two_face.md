# Singleton support pairs fill every permutahedron two-face — preserved pre-item development

## Development

## Singleton supports make every permutahedron two-face loop fill

Work in the singleton-allowed Hamiltonian support-pair poset
\[
\widehat{\mathcal P}(H)
=
\{(A,B):A,B\neq\varnothing,\ A\cap B=\varnothing,\ H[A],H[B]\text{ Hamiltonian}\},
\]
ordered componentwise by inclusion.

For every chamber \(\pi\) of the permutahedron, let
\[
C(\pi)=(P_\pi,Q_\pi)
\]
be its canonical partial two-cover in the positive-deficiency state. For adjacent chambers \(\pi,\sigma\), use the common lower pair
\[
C(\pi,\sigma)=
(P_\pi\cap P_\sigma,\;Q_\pi\cap Q_\sigma),
\]
whose two supports are nonempty Hamiltonian, as established in [[singleton_allowed_support_pairs_match_the_antipodal_dimension_and_absorb_all_chamber_edges]].

Thus the boundary of every rank-two permutahedron face maps to an alternating loop of chamber vertices and adjacent-chamber lower vertices in
\[
\widehat K(H)=\Delta\widehat{\mathcal P}(H).
\]

### Theorem

Every such square or braid-hexagon loop is null-homotopic in \(\widehat K(H)\).

### Proof

Let \(F\) be a rank-two face. Its ordered-partition type is either

1. one non-singleton block \(W\) of order three (the braid hexagon), or
2. two non-singleton blocks \(W_1,W_2\), each of order two (the commuting square).

All other face blocks are singletons and stay in the same positions in every chamber.

Put
\[
A_F=\bigcap_{\pi\in F}P_\pi,
\qquad
B_F=\bigcap_{\pi\in F}Q_\pi.
\]

Whenever nonempty, \(A_F\) and \(B_F\) are Hamiltonian. Indeed each is a union of whole initial, respectively terminal, face blocks: a partial active block cannot survive intersection over all its internal permutations unless the whole block is retained. Hence a nonempty \(A_F\) is an inherited common prefix, and a nonempty \(B_F\) an inherited common suffix.

#### Case 1: both common sides are nonempty

Then
\[
Z=(A_F,B_F)\in\widehat{\mathcal P}(H)
\]
and \(Z\) is below every chamber vertex and every adjacent-chamber lower vertex on the loop. Therefore the whole loop lies in the upper interval of \(Z\), whose order complex is a cone with apex \(Z\). It fills.

#### Case 2: \(A_F=\varnothing\) and \(B_F\neq\varnothing\)

Because every \(P_\pi\) is a nonempty prefix, if the first face block were a singleton then that fixed first label would belong to every \(P_\pi\), contradicting \(A_F=\varnothing\). Hence the first face block is non-singleton. Call it \(W\). In a rank-two face,
\[
|W|\in\{2,3\}.
\]

Every chamber left support meets \(W\). The same is true for every adjacent-chamber lower left support: if two adjacent prefixes both extend beyond \(W\), they contain \(W\); if their boundary lies inside \(W\), the established edge-intersection theorem says their intersection is nonempty and there is no earlier block from which such an intersection could come.

Also
\[
W\cap B_F=\varnothing.
\]
For every \(w\in W\), some chamber places \(w\) first inside the first block; its nonempty prefix contains \(w\), so \(w\) cannot lie in every right support.

For every loop vertex \(S=(A,B)\), define
\[
r(S)=(A\cap W,\;B_F).
\]
The first component is a nonempty subset of a set of order at most three, hence Hamiltonian; the second is Hamiltonian; they are disjoint. Thus \(r(S)\in\widehat{\mathcal P}(H)\).

Moreover \(r\) is order-preserving on the loop poset and
\[
r(S)\le S.
\]
Hence the inclusion of the loop is homotopic, by the standard poset-order homotopy, to its image under \(r\).

But every image vertex satisfies
\[
r(S)\le (W,B_F)=:Z.
\]
Since \(W\) is Hamiltonian for \(|W|\le3\), \(Z\in\widehat{\mathcal P}(H)\), and the image loop lies in the cone below \(Z\). Therefore the original loop is null-homotopic.

The case \(A_F\neq\varnothing,\ B_F=\varnothing\) is symmetric, using the last non-singleton face block.

#### Case 3: both \(A_F\) and \(B_F\) are empty

A braid face has only one non-singleton block. If that block is not first, the fixed first singleton lies in every left support; if it is not last, the fixed last singleton lies in every right support. Except for the trivial ground sets where the theorem is immediate, one block cannot be both first and last. Thus a braid hexagon cannot occur in this case.

Hence \(F\) is a commuting square, and its two order-two blocks must be the first and last face blocks. Call them
\[
W_L,\qquad W_R.
\]
They are disjoint.

Every loop left support meets \(W_L\), and every loop right support meets \(W_R\), including the adjacent-chamber lower supports by the same edge-intersection argument as above.

Define
\[
r(A,B)=(A\cap W_L,\;B\cap W_R).
\]
Both components are nonempty subsets of two-sets, hence Hamiltonian, and \(r\) is order-preserving with \(r(S)\le S\).

Every image vertex is below
\[
Z=(W_L,W_R)\in\widehat{\mathcal P}(H),
\]
so the image lies in a cone and the square loop fills.

This proves the theorem. \(\square\)

### Consequence

The canonical chamber map
\[
\partial\operatorname{Perm}(V)\cong S^{n-2}
\longrightarrow
|\widehat K(H)|
\]
already extends equivariantly over the entire two-skeleton.

Thus the protected four-label \(C_4\) obstruction of the earlier terminal-carrier target is **not** an obstruction in the singleton-allowed support-pair target. It was created by retaining a more rigid carrier notion. The support-pair quotient absorbs all commuting-square and braid-hexagon coherence automatically.

The next closure question is therefore genuinely higher-dimensional: determine whether the same facewise intersection/retraction mechanism extends over every permutahedron face, or whether a first obstruction appears in dimension at least three. Any such obstruction must survive after arbitrary singleton support contraction, so it is strictly stronger than the old four-label loop residue.
