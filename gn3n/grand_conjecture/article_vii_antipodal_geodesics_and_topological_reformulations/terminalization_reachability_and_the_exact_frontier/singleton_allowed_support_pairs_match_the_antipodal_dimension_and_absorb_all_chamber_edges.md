# Singleton-allowed support pairs match the antipodal dimension and absorb all chamber edges

## Composition

(none yet)

## Development

## The singleton-allowed support-pair complex is the dimension-matched topological target

Let \(\widehat{\mathcal P}(H)\) be the poset of ordered pairs
\[
(A,B)
\]
of disjoint nonempty Hamiltonian supports of a boundary tournament \(H\), ordered componentwise by inclusion. Singleton supports are allowed. Let
\[
\widehat K(H)=\Delta\widehat{\mathcal P}(H),
\qquad
T(A,B)=(B,A).
\]
The involution is free on \(|\widehat K(H)|\).

### Exact rank identity without normalization

For every \(H\) on \(n\) vertices,
\[
\boxed{
\kappa_2(H)
=
n-\max_{(A,B)\in\widehat{\mathcal P}(H)}(|A|+|B|).
}
\]
Indeed the complement of any support pair is a deletion set leaving a two-cover, and conversely every deletion two-cover gives such a support pair, including covers with a singleton component.

Thus if \(H\) has no spanning two-cover,
\[
|A|+|B|\le n-1
\]
for every support pair. Since the minimum total support is \(2\), every strict chain has at most the ranks \(2,3,\ldots,n-1\), and therefore
\[
\boxed{\dim\widehat K(H)\le n-3.}
\]

Let \(\widehat Q_n\) be the same poset with no Hamiltonicity restriction. Its equivariant index and coindex are both \(n-2\). For the lower bound, take the sum-zero hyperplane
\[
W=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
Every nonzero \(x\in W\) has at least one positive and one negative coordinate. The coordinate-hyperplane cell structure on \(S(W)\cong S^{n-2}\) has signed support pair
\[
(A(x),B(x))=(\{i:x_i>0\},\{i:x_i<0\}),
\]
giving an equivariant face-poset map
\[
S^{n-2}\longrightarrow\Delta\widehat Q_n.
\]
For the upper bound, label a pair of total order \(s\) by the signed \((s-1)\)-st cross-polytope vertex, with sign determined by whether the least label of \(A\cup B\) lies in \(A\) or \(B\). Strict chains have distinct totals, so no simplex receives an opposite pair. This gives
\[
\Delta\widehat Q_n\longrightarrow S^{n-2}.
\]

Consequently, any equivariant continuous map
\[
S^{n-2}\longrightarrow|\widehat K(H)|
\]
already closes the grand theorem: if \(H\) were a counterexample, compose with a generic equivariant map from the \((n-3)\)-dimensional free complex \(\widehat K(H)\) to \(S^{n-3}\), contradicting Borsuk--Ulam.

This target is dimension-matched to the normalized side-balance sphere of Article VII. Requiring both supports to have order at least two lowers the target by two dimensions and obscures this match.

### Canonical chamber states

Assume now that \(H\) is a counterexample. Every spanning order \(\pi\) has positive exact deficiency. Write its canonical partial two-cover as
\[
P_\pi\mid X_\pi\mid Q_\pi
\]
from the exact inversion-window theorem. Define
\[
C(\pi)=\bigl(V(P_\pi),V(Q_\pi)\bigr)\in\widehat{\mathcal P}(H).
\]
Reversal swaps the pair:
\[
C(\pi^{\rm rev})=T C(\pi).
\]

### Adjacent chambers always have a common Hamiltonian lower pair

Let \(\pi,\sigma\) be adjacent chambers of the permutahedron, differing by a single adjacent transposition. Then
\[
A_{\pi\sigma}=V(P_\pi)\cap V(P_\sigma),
\qquad
B_{\pi\sigma}=V(Q_\pi)\cap V(Q_\sigma)
\]
are nonempty Hamiltonian supports.

Proof for the left side. \(P_\pi\) and \(P_\sigma\) are initial segments of two orders differing only by exchanging adjacent positions \(t,t+1\). The intersection of two such initial segments is always an initial segment of one of the two orders, except when both cuts lie exactly between the swapped labels; then it is the common initial segment ending immediately before the swapped pair. Thus the intersection inherits a tight displayed order. Since every canonical left path has order at least two, the intersection is nonempty; in the exceptional boundary case it may be a singleton, which is why singleton supports should be retained. The right side is the reversed-suffix analogue.

The two intersections are disjoint, since each is contained simultaneously in the left and right supports of either chamber. Hence
\[
C(\pi\sigma)=\bigl(A_{\pi\sigma},B_{\pi\sigma}\bigr)
\]
is a vertex of \(\widehat K(H)\) satisfying
\[
C(\pi\sigma)\le C(\pi),
\qquad
C(\pi\sigma)\le C(\sigma).
\]

Therefore the chamber assignment extends canonically over every permutahedron edge by
\[
C(\pi)\;-\;C(\pi\sigma)\;-\;C(\sigma).
\]
These edge paths are equivariant under reversal.

### Consequence for the Article VII architecture

At deletion distance one, a direct canonical side flip was previously exceptional because the role map could jump \(P\leftrightarrow Q\) across one adjacent swap. In \(\widehat K(H)\) it is not exceptional at all: the two rank-\((n-1)\) deletion-cover states are joined through their common lower support pair, obtained by dropping the transferred endpoint. More generally the same common-lower-pair construction works for every adjacent chamber, whether or not a direct side flip occurs.

Thus the first obstruction to an equivariant map
\[
\partial\mathrm{Perm}(V)\cong S^{n-2}\longrightarrow|\widehat K(H)|
\]
does not occur on the one-skeleton. It occurs first on the two-skeleton: one must fill the loops induced by square and hexagonal permutahedron faces. This places the later Article VII two-skeleton and four-label carrier results at a much earlier and more natural point in the proof.

The resulting closure program is precise:

1. chamber vertices map to canonical Hamiltonian support pairs;
2. all chamber edges extend by common lower pairs, as proved above;
3. prove that every induced two-face loop is null-homotopic in a natural support-pair carrier;
4. prove that the relevant carrier components have no higher homotopy, or otherwise supply higher fillings.

If steps 3--4 hold equivariantly, Borsuk--Ulam forces a rank-\(n\) support pair, i.e. a spanning two-cover.
