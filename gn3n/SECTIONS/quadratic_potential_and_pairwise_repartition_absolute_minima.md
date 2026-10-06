# Absolute minima

## Composition

**Lemma 3.** Among triples of positive integers with fixed sum \(n\), the minimum of \(a^2+b^2+c^2\) is attained exactly when the largest and smallest entries differ by at most one.

**Proof.** If \(a\ge b+2\), replacing \((a,b)\) by \((a-1,b+1)\) changes the sum of squares by
\[
-2(a-b)+2<0.
\]
Repeated balancing terminates exactly when no two entries differ by at least \(2\). \(\square\)

The possible size multisets at an absolute minimum are
\[
\{r,r,r\},\qquad \{r+1,r,r\},\qquad \{r+1,r+1,r\}.
\]
No strict decrease of \(\Phi\) is possible from these sizes while three nonempty paths remain.

## Small-component consequences

Two elementary balancing facts substantially narrow the possible minimum states. By [[toolkit_minimal_three_covers_have_no_components_of_order_one_or_two]], every component of a minimum-(\Phi\) three-cover has order at least three.

There is a further restriction at order three. Let \(T\mid C\) be two displayed components with \(|T|=3\) and \(|C|=s\). If \(s\ge6\), then [[three_vertex_component_long_neighbor_rotation01]] gives a strict pairwise decrease of \(\Phi\), contradicting minimality. Hence a three-vertex component can occur at a minimum only when each of the other two components has order at most five. In particular, for \(|V(H)|\ge14\), every component of a minimum-(\Phi\) three-cover has order at least four.

At the boundary value \(s=5\), the same lemma gives an explicit equal-(\Phi\) rotation
\[
3\mid5\longleftrightarrow5\mid3
\]
whenever the direct endpoint enlargement to a Hamiltonian four-set is unavailable. Thus the smallest surviving component is accompanied by a concrete neutral recurrence, not an unstructured exceptional case.

## Metadata

- ID: quadratic_potential_and_pairwise_repartition_absolute_minima
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False
- Subsections existing when composed: 2
- Subsections now: 2

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/quadratic_potential_and_pairwise_repartition_absolute_minima_subsection_a.md) (`quadratic_potential_and_pairwise_repartition_absolute_minima_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Small-component consequences](../SUBSECTIONS/quadratic_potential_and_pairwise_repartition_absolute_minima_subsection_b.md) (`quadratic_potential_and_pairwise_repartition_absolute_minima_subsection_b`; development v1; composition vNone; stale=False)
