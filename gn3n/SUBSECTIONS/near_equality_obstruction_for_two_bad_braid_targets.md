# Near-equality obstruction for two bad braid targets

## Metadata

- ID: near_equality_obstruction_for_two_bad_braid_targets
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 19
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## Near-equality form of a two-bad-target obstruction

Continue with the exchange matrix of [[dense_exchange_matrix_for_the_maximal_braid]]. Suppose two moving pairs, say \(P_1,P_2\), give non-Hamiltonian targets
\[
C\cup P_1,\qquad C\cup P_2.
\]

Let \(D_0\subseteq B\times C\) be the cells for which the complementary side \(B_{x,y}\) is non-Hamiltonian. For \(i=1,2\), let \(D_i\) be the cells for which the swap fails to repair target \(P_i\):
\[
C_{x,y}\cup P_i\quad\text{is non-Hamiltonian}.
\]

The exchange-matrix lemma gives
\[
|D_0|\le6,
\]
with at most two cells of \(D_0\) in each column, and
\[
|D_i|\le5,
\]
with at most one cell of \(D_i\) in each row.

Assume there is no swap that simultaneously preserves the Hamiltonian side and repairs both bad targets. Then every side-preserving cell belongs to \(D_1\cup D_2\):
\[
(B\times C)\setminus D_0\subseteq D_1\cup D_2.
\]
Since the left side has at least nine cells,
\[
9\le |D_1\cup D_2|\le10.
\]

This forces the following near-equality structure.

1. Each \(D_i\) has order at least four. Thus each bad target has a unique possible failed repair in at least four of the five rows.
2. The two target-failure sets satisfy
\[
|D_1\cap D_2|\le1.
\]
Indeed,
\[
|D_1\cap D_2|
=|D_1|+|D_2|-|D_1\cup D_2|
\le10-9=1.
\]
3. The side-preserving set has order nine or ten. Hence the side-failure set has order six or five.
4. Because every column contains at least three side-preserving cells, its column-degree sequence is necessarily
\[
(3,3,3)
\]
when there are nine side-preserving cells, or
\[
(4,3,3)
\]
up to permutation when there are ten. Equivalently, the side-failure column degrees are respectively
\[
(2,2,2)
\quad\text{or}\quad
(1,2,2).
\]
5. Since \(D_1,D_2\) each have row degree at most one, their union has row degree at most two. In the nine-cell case its row degrees must be a permutation of
\[
(2,2,2,2,1),
\]
and in the ten-cell case all five row degrees equal two.

Thus failure of a one-swap reduction from two bad braid targets is not a diffuse phenomenon. It forces two almost-everywhere-defined row functions
\[
f_i:B\dashrightarrow C
\]
whose graphs are \(D_i\), with at most one common graph point, while the Hamiltonian-side failures are essentially the complement of the union of those two graphs.

This is the exact equality regime that still needs local orientation analysis. Any strict improvement in one of the four-of-six inequalities already produces a side-preserving swap repairing both bad targets and reduces the braid from two bad targets to at most one.
