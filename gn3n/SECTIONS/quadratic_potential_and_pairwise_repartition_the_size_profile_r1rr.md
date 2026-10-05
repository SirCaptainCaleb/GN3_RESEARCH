# The size profile \(\{r+1,r,r\}\)

## Composition

Let \(A\mid B\mid C\) have orders \(r+1,r,r\), and let \(x,y\) be the endpoints of \(A\).

Suppose first that \(x\) extends both \(B\) and \(C\). For a two-cover \(T\) of \(H-x\), use the partition
\[
(A-\{x\})\mid B\mid C.
\]
If \(T\) had only one edge joining different classes, its three blocks could be restored with \(x\) to produce a two-cover of \(H\). Hence there are at least two such edges. With exactly two, Section 3 gives either an inherited displayed edge whose endpoints lie in different paths of \(T\), or two blocks of one displayed support separated by a block of another.

Suppose instead that \(x\) extends \(B\) and \(y\) extends \(C\), while the opposite extensions are unavailable. If either Hamiltonian extension reverses the order of two core vertices, there is an order disagreement. Otherwise the extensions are obtained by inserting \(x\) and \(y\) into the displayed orders of \(B\) and \(C\).

Write \(A=(x,M,y)\), and let \(T\) be a two-cover of \(H-\{x,y\}\). If at least two edges of \(T\) join distinct sets among \(M,B,C\), Section 3 again gives the preceding alternatives. If there is only one, the three sets occur as whole blocks on two paths. The insertion positions of \(x\) into \(B\) and \(y\) into \(C\) must then be adjacent to the unique join between two blocks; otherwise both insertions can be made while leaving the join unchanged, giving a two-cover of \(H\). The triple needed to perform both insertions at the remaining join is therefore non-tight, and its boundary flip is tight.

Hence:

**Lemma 5.** At a minimum of \(\Phi\) with size multiset \(\{r+1,r,r\}\), one obtains an order disagreement, an edge joining distinct displayed supports in a comparison cover, an inherited displayed edge split between the two paths of a comparison cover, two blocks of one displayed support separated by another, or a reverse tight triple at a displayed join.

## Metadata

- ID: quadratic_potential_and_pairwise_repartition_the_size_profile_r1rr
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/quadratic_potential_and_pairwise_repartition_the_size_profile_r1rr_subsection_a.md) (`quadratic_potential_and_pairwise_repartition_the_size_profile_r1rr_subsection_a`; development v1; composition vNone; stale=False)
