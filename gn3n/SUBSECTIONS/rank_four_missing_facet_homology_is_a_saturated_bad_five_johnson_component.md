# Rank-four missing-facet homology is a saturated bad-five Johnson component

## Metadata

- ID: rank_four_missing_facet_homology_is_a_saturated_bad_five_johnson_component
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 251
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Rank-four missing-facet homology is a saturated bad-five Johnson component

Let \(W\) be a finite vertex set. Define \(X_5(W)\) to be the simplicial complex consisting of

- every subset of \(W\) of order at most four, and
- the \(4\)-simplex on every Hamiltonian five-set of \(H[W]\).

Equivalently, the only missing \(4\)-simplices are the non-Hamiltonian five-sets.

Work over \(\mathbb F_2\), and let
\[
\mathcal B_5(W)=\{B\subseteq W:|B|=5,\ H[B]\text{ non-Hamiltonian}\}.
\]

### Exact presentation of the first missing-facet homology

\[
H_3(X_5(W);\mathbb F_2)
\]
has one generator \(e_B\) for every
\[
B\in\mathcal B_5(W),
\]
and, for every six-set \(U\subseteq W\), the single relation
\[
\sum_{\substack{B\subset U\\|B|=5\\B\in\mathcal B_5(W)}}e_B=0.
\]

Proof. Compare \(X_5(W)\) with the full simplex \(\Delta(W)\). In the relative chain complex
\[
C_*(\Delta(W),X_5(W)),
\]
all groups through degree three vanish. Relative \(4\)-chains have the bad five-sets as basis, and their relative boundaries vanish because every four-set is already a simplex of \(X_5(W)\). Relative \(5\)-chains have the six-sets as basis, and the relative boundary of a six-set is exactly the sum of its bad five-facets. Since \(\Delta(W)\) is contractible, the long exact sequence identifies
\[
H_3(X_5(W))\cong H_4(\Delta(W),X_5(W)),
\]
giving the presentation. \(\square\)

### Boundary tournaments make every relation binary

The audited small-set theorem says that every six-set contains at least four Hamiltonian five-subsets. A six-set has six five-subsets, so it contains at most two bad five-sets.

Therefore every relation above has one of the forms
\[
0,\qquad e_B=0,\qquad e_B=e_C.
\]

Define the bad-five Johnson graph \(J^{\rm bad}_5(W)\):

- vertices are the bad five-sets;
- \(B,C\) are adjacent exactly when
  \[
  |B\cap C|=4,
  \]
  equivalently \(B\cup C\) is a six-set.

Then each connected component contributes at most one generator to \(H_3(X_5(W))\).

A component survives exactly when no generator in it is killed by a singleton relation. Equivalently:

> for every bad five-set \(B\) in the component and every exterior label \(x\in W-B\), the six-set \(B+x\) contains exactly one second bad five-set.

Since there are at most two bad five-facets in \(B+x\), that second bad set is unique. It has the form
\[
B-\{y\}+\{x\}
\]
for a uniquely determined \(y\in B\).

Thus a surviving component carries a deterministic exchange map
\[
(B,x)\longmapsto y,
\qquad
B-\{y\}+\{x\}\in\mathcal B_5(W).
\]

### Rank-four interpretation

This is the exact analogue one dimension higher of the bad-four Johnson presentation for \(H_2(X_4)\).

Consequently the first possible missing-facet \(3\)-homology at rank four is not an arbitrary family of non-Hamiltonian five-sets. It is a **saturated connected Johnson component** in which every attempt to adjoin an exterior label forces one unique exchange to another bad five-set.

Every vertex of such a component is edge-orderable, because every non-Hamiltonian five-vertex boundary tournament is edge-orderable. Hence a surviving rank-four obstruction is a family of edge-ordered bad \(K_5\)'s equipped with a deterministic one-label exchange dynamics.

This is scale-independent. The next closure target is to show that boundary-tournament edge-order structure forbids such a saturated bad-five component in the relative carrier arising from a minimum counterexample, or that mixed larger Hamiltonian supports fill its unique homology class.

## Frontier

- Development version when composed: None
- Development version now: 1
