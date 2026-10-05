# A path-forest consequence of threshold deletion

## Cold composition

The following elementary statement is useful whenever a threshold set \(D\) has already been shown to contain every edge not lying on a fixed maximum path.

## Lemma 4

Suppose \(D\subseteq V(H)\) has the property that every edge of \(H-D\) belongs to the edge set of a linear path \(P\). Then \(H-D\) is a disjoint union of linear paths and isolated vertices. In particular,
\[
\Delta(H-D)\le2
\]
and
\[
|E(H-D)|\le \frac{|V(H)\setminus D|}{2}. \tag{9}
\]

#### Proof
A subset of the edge set of a linear path has no intersections except between consecutive selected path edges. Its nonempty connected components are therefore linear paths.

If the nonempty components have \(t_1,\ldots,t_c\) edges, they use
\[
\sum_{i=1}^c(2t_i+1)=2|E(H-D)|+c
\]
vertices. Hence
\[
2|E(H-D)|+c\le |V(H)\setminus D|,
\]
which implies (9). ∎

If every vertex outside \(D\) has degree at least \(q+1\), Lemma 4 immediately implies that every such vertex lies in at least \(q-1\) edges meeting \(D\).

## Metadata

- ID: induction_on_the_complement_of_a_longest_path_a_path_forest_consequence_of_threshold_deletion
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/induction_on_the_complement_of_a_longest_path_a_path_forest_consequence_of_threshold_deletion_subsection_a.md) (\`induction_on_the_complement_of_a_longest_path_a_path_forest_consequence_of_threshold_deletion_subsection_a\`; development v1; composition v1; stale=False)
- [Subsection 2 — Lemma 4](../SUBSECTIONS/induction_on_the_complement_of_a_longest_path_a_path_forest_consequence_of_threshold_deletion_subsection_b.md) (\`induction_on_the_complement_of_a_longest_path_a_path_forest_consequence_of_threshold_deletion_subsection_b\`; development v1; composition vNone; stale=True)
