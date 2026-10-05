# Balanced cuts force four components

## Metadata

- ID: cyclic_strengthenings_and_balanced_cut_obstructions_subsection_b
- Parent Section: cyclic_strengthenings_and_balanced_cut_obstructions
- Position: 2
- Row version: 4
- Development version: 4
- Composition version: 1
- Composition stale: False

## Cold composition

In an edge-ordered model, a Hamilton cycle with at most two transition-color components has a unimodal cyclic sequence of edge ranks: from its unique minimum the ranks increase to the unique maximum and then decrease. Hence for every rank threshold, the cycle edges above that threshold form one cyclic interval.

Now let a Hamilton cycle meet a balanced partition \(U\mid W\). If all crossing edges form one cyclic interval, degree counting gives the same number of internal cycle edges on the two sides. But the complementary interval of internal edges, if nonempty, lies entirely in one side, a contradiction. Therefore every cycle edge must cross the partition.

Applying this first to \(A\cup B\mid C\cup D\) forces all edges to have level at least two. Applying it next to \(A\cup C\mid B\cup D\) forces all edges to have level three. The level-three graph is the disjoint union of the complete bipartite graphs on \(A,D\) and on \(B,C\), so it has no Hamilton cycle. Thus no spanning cycle has two transition-color components.

This obstruction is structural, not a small-order accident; it occurs for every \(s\ge1\).

## Development

In an edge-ordered model, a Hamilton cycle with at most two transition-color components has a unimodal cyclic sequence of edge ranks: from its unique minimum the ranks increase to the unique maximum and then decrease. Hence for every rank threshold, the cycle edges above that threshold form one cyclic interval.

Now let a Hamilton cycle meet a balanced partition \(U\mid W\). If all crossing edges form one cyclic interval, degree counting gives the same number of internal cycle edges on the two sides. But the complementary interval of internal edges, if nonempty, lies entirely in one side, a contradiction. Therefore every cycle edge must cross the partition.

Applying this first to \(A\cup B\mid C\cup D\) forces all edges to have level at least two. Applying it next to \(A\cup C\mid B\cup D\) forces all edges to have level three. The level-three graph is the disjoint union of the complete bipartite graphs on \(A,D\) and on \(B,C\), so it has no Hamilton cycle. Thus no spanning cycle has two transition-color components.

This obstruction is structural, not a small-order accident; it occurs for every \(s\ge1\).
