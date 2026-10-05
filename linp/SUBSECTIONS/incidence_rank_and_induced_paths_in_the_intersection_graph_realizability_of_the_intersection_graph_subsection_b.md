# Lemma 2

## Metadata

- ID: incidence_rank_and_induced_paths_in_the_intersection_graph_realizability_of_the_intersection_graph_subsection_b
- Parent Section: incidence_rank_and_induced_paths_in_the_intersection_graph_realizability_of_the_intersection_graph
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

The indexed clique family \(\{C_x:x\in V(H)\}\) has the following properties.

1. Every vertex of \(F\) belongs to exactly three cliques.
2. Every edge of \(F\) belongs to exactly one clique.

Conversely, any graph equipped with an indexed family of cliques satisfying these two properties is the intersection graph of a linear \(3\)-graph.

#### Proof
A hyperedge has exactly three vertices, so its corresponding vertex of \(F\) belongs to exactly the three cliques indexed by those vertices. If two hyperedges intersect, linearity gives a unique common vertex, so the corresponding graph edge lies in exactly one \(C_x\).

Conversely, suppose a graph \(F\) has cliques \(C_x\) satisfying the two conditions. For a graph vertex \(q\), define
\[
E_q=\{x:q\in C_x\}.
\]
The first condition gives \(|E_q|=3\). If \(q,q'\) are adjacent, the graph edge \(qq'\) lies in a unique \(C_x\), so
\[
E_q\cap E_{q'}=\{x\}.
\]
If \(q,q'\) are nonadjacent, they lie together in no \(C_x\), so \(E_q\cap E_{q'}=\varnothing\). Thus the triples \(E_q\) form a linear \(3\)-graph whose intersection graph is \(F\). ∎

Any proof of (1) may therefore use the three-clique realization furnished by Lemma 2. A theorem for arbitrary induced-path-free graphs is unnecessarily general.
