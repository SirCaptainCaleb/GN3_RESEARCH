# From transport to an end-edge reversal

## Body

The lower states in Lemma 4 have path orders \(4,3,m\), with the same long path retained. Repartitioning the four- and three-vertex sides may strictly decrease the quadratic potential
\[
\Phi(P_1\mid P_2\mid P_3)=|P_1|^2+|P_2|^2+|P_3|^2.
\]
If two adjacent lower states admit the same strict decrease, a state of smaller \(\Phi\) lies in the same component of the pairwise-repartition graph.

Assume no such synchronized decrease is available. Fix the transported vertex \(z\) and one seven-vertex set \(W\). Let \(\Omega\) be the graph in the proof of Lemma 4. We have \(\deg_\Omega(z)\ge4\). If the degree is larger, two adjacent choices give synchronized descent. If the degree is four, let \(u,v\) be the two nonneighbors of \(z\). Then
\[
F=W-\{z,u\}
\]
is a non-Hamiltonian five-set with at least four Hamiltonian vertex deletions.

Choose Hamilton paths on these four deletions. If all common vertices had the same relative order in every pair, the orders would combine to a Hamilton path of \(F\). Hence two have an order disagreement. A minimal such pair contains either a common edge traversed in opposite directions or a tight triple reversing an edge of one of the paths. A tight-cycle-only alternative is impossible inside a non-Hamiltonian edge-orderable five-set. In the common-edge case, one adjacent triple of the other Hamilton path reverses that edge. Therefore:

**Lemma 5.** If synchronized strict decrease is unavailable, a three-cover in the same component contains a Hamiltonian four-path \(K\) and a tight triple on the surrounding five vertices that reverses an edge of \(K\).

If the reversed edge is an end edge of \(K\), nothing further is needed. If it is the internal edge, the four vertices of \(K\) together with the reversing triple contain either a Hamiltonian four-set or an edge-orderable matching-block \(K_4\). In the Hamiltonian case the complement has path-cover number two. In the matching-block case, adjoining an endpoint of the long path produces a Hamiltonian support of order four or five containing that endpoint; its complement again has path-cover number two.

Hence:

**Proposition 6.** The fixed-deletion transport produces one of:
1. a strict decrease of \(\Phi\) inside the same component of the pairwise-repartition graph;
2. a reversal of an end edge of a displayed Hamiltonian four-path;
3. a Hamiltonian support of order four or five containing a displayed endpoint of the complementary path, with two-coverable complement.

## Metadata

- ID: defect_lines_and_spanning_order_compression_from_transport_to_an_end_edge_reversal
- Kind: line
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Chunk 1 — HOT, version 1: (untitled)
