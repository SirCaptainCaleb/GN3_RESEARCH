# endpoint_transport_and_small_support_gluing_endpoint_positions_of_a_transferred_vertex_subsection_a

## Metadata

- ID: endpoint_transport_and_small_support_gluing_endpoint_positions_of_a_transferred_vertex_subsection_a
- Parent Section: endpoint_transport_and_small_support_gluing_endpoint_positions_of_a_transferred_vertex
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Suppose \(X,Y,D,\{x\}\) partition \(V(H)\) and both
\[
(X\cup\{x\})\mid Y\mid D
\quad\text{and}\quad
X\mid(Y\cup\{x\})\mid D
\]
are three-covers.

**Lemma 3.** If \(x\) is the final vertex of a Hamilton path on \(X\cup\{x\}\) and the initial vertex of a Hamilton path on \(Y\cup\{x\}\), then a displayed end-edge reversal occurs. The same holds with initial and final interchanged.

**Proof.** Start with the Hamilton path on \(X\cup\{x\}\) ending at \(x\), and greedily append the vertices following \(x\) in the Hamilton path on \(Y\cup\{x\}\). If the whole path is absorbed, its union with \(D\) is a two-cover. Otherwise Lemma 1 gives a displayed end-edge reversal. \(\square\)

Consequently, if no two-cover, strict decrease, or displayed end-edge reversal occurs, then either
- \(x\) is internal in every Hamiltonian order of one augmented support; or
- whenever \(x\) is an endpoint in either augmented support, it is always on the same side in both.

The second possibility is governed by insertion positions.
