# Cyclic strengthenings and balanced-cut obstructions

**Summary:** A two-component spanning cycle is too strong; the exact cyclic invariant is whether two cut positions can cover all blue transitions.

## Statement

The tempting strengthening asking for a spanning cycle with at most two monochromatic transition components is false, even when a one-change spanning order and a two-cover exist. The correct cyclic reformulation uses a vertex cover of the blue-transition defect graph.

## Body

## Why the two-component cycle target fails

A natural first attempt at importing antipodal path ideas was to seek a spanning cycle whose cyclic transition-color word has at most two monochromatic components. This would be sufficient for a two-cover, but it is not necessary.

There is an infinite family of edge-orderable boundary tournaments \(H_s\) on \(4s\) vertices with
\[
\operatorname{pc}(H_s)=2,
\qquad
\min_C \rho_{H_s}(C)=4,
\]
where \(\rho_H(C)\) is the cyclic monochromatic-component count. The same \(H_s\) nevertheless admits a spanning linear order whose triple-status word changes exactly once.

The construction partitions the vertices into four equal classes \(A,B,C,D\) and orders ordinary edges by four levels: within-class; \(AB,CD\); \(AC,BD\); \(AD,BC\). Suitable within-level orders make two alternating level-three paths tight and give a two-cover.

## Balanced cuts force four components

In an edge-ordered model, a Hamilton cycle with at most two transition-color components has a unimodal cyclic sequence of edge ranks: from its unique minimum the ranks increase to the unique maximum and then decrease. Hence for every rank threshold, the cycle edges above that threshold form one cyclic interval.

Now let a Hamilton cycle meet a balanced partition \(U\mid W\). If all crossing edges form one cyclic interval, degree counting gives the same number of internal cycle edges on the two sides. But the complementary interval of internal edges, if nonempty, lies entirely in one side, a contradiction. Therefore every cycle edge must cross the partition.

Applying this first to \(A\cup B\mid C\cup D\) forces all edges to have level at least two. Applying it next to \(A\cup C\mid B\cup D\) forces all edges to have level three. The level-three graph is the disjoint union of the complete bipartite graphs on \(A,D\) and on \(B,C\), so it has no Hamilton cycle. Thus no spanning cycle has two transition-color components.

This obstruction is structural, not a small-order accident; it occurs for every \(s\ge1\).

## The exact cyclic defect-graph formulation

For an oriented Hamilton cycle \(Z=(v_1,\ldots,v_n,v_1)\), let \(e_i=\{v_i,v_{i+1}\}\). Define the blue-transition defect graph \(D_Z\) on the cycle-edge positions \(e_i\) by adding \(\{e_{i-1},e_i\}\) exactly when \((v_{i-1},v_i,v_{i+1})\) is non-tight.

Cutting a nonempty set \(S\) of cycle edges leaves \(|S|\) inherited path components. Every resulting component is tight exactly when \(S\) meets every edge of \(D_Z\), i.e. exactly when \(S\) is a vertex cover of \(D_Z\). Hence
\[
\operatorname{pc}(H)
=
\min_Z \max\{1,\tau(D_Z)\}.
\]
In particular,
\[
\operatorname{pc}(H)\le2
\iff
\text{some cyclic order }Z\text{ has }\tau(D_Z)\le2.
\]

This is the correct cyclic reformulation. It allows several separated blue runs provided two cut positions hit them all, which is exactly the information lost by counting monochromatic components alone.

## Metadata

- ID: cyclic_strengthenings_and_balanced_cut_obstructions
- Kind: section
- Version: 9
- Math version: 3
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 4: Why the two-component cycle target fails
- Subsection 2 — crystallized, version 4: Balanced cuts force four components
- Subsection 3 — HOT, version 3: The exact cyclic defect-graph formulation
