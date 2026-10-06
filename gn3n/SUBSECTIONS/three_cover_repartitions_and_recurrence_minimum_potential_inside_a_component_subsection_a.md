# three_cover_repartitions_and_recurrence_minimum_potential_inside_a_component_subsection_a

## Metadata

- ID: three_cover_repartitions_and_recurrence_minimum_potential_inside_a_component_subsection_a
- Parent Section: three_cover_repartitions_and_recurrence_minimum_potential_inside_a_component
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Fix a component \(\mathcal C\) of \(\mathcal R(H)\) containing a singleton lift, and choose \(C=P_1\mid P_2\mid P_3\in\mathcal C\) minimizing \(\Phi\).

**Lemma 2.** For \(i\ne j\), every two-cover \(R\mid S\) of
\[
H[V(P_i)\cup V(P_j)]
\]
satisfies
\[
\bigl||R|-|S|\bigr|
\ge
\bigl||P_i|-|P_j|\bigr|.
\]

**Proof.** The replacement \(P_i\mid P_j\mapsto R\mid S\) is an edge of \(\mathcal R(H)\). With fixed sum \(a+b\),
\[
a^2+b^2=\frac{(a+b)^2+(a-b)^2}{2},
\]
so a smaller size difference would decrease \(\Phi\), contrary to the choice of \(C\). \(\square\)

Thus every displayed pair is a minimum-imbalance two-cover of its union.

Among triples of positive integers with fixed sum, the minimum of the sum of squares occurs exactly when the largest and smallest entries differ by at most one. Therefore the absolute minimum size multisets are
\[
\{r,r,r\},\qquad
\{r+1,r,r\},\qquad
\{r+1,r+1,r\}.
\]
Strict decrease of \(\Phi\) must eventually stop, and it can stop at one of these profiles.

## Frontier

- Development version when composed: None
- Development version now: 1
