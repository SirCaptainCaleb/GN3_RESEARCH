# endpoint_transport_and_small_support_gluing_compatible_one_vertex_extensions_subsection_a

## Metadata

- ID: endpoint_transport_and_small_support_gluing_compatible_one_vertex_extensions_subsection_a
- Parent Section: endpoint_transport_and_small_support_gluing_compatible_one_vertex_extensions
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

Let \(K\) be a vertex set and let \(x,y\notin K\). Suppose \(K\cup\{x\}\) and \(K\cup\{y\}\) have Hamilton paths that induce the same order
\[
C=(c_1,\ldots ,c_m)
\]
on \(K\). Each path is obtained by inserting its exceptional vertex into a gap of \(C\), allowing the two endpoint gaps.

**Lemma 4.**
1. If the insertion gaps are separated by at least one gap, inserting both vertices gives a Hamilton path on \(K\cup\{x,y\}\).
2. If the gaps are adjacent, the simultaneous order is Hamiltonian unless the unique triple containing \(x\), the intervening core vertex, and \(y\) is non-tight; in that case its boundary flip is tight.
3. If the gaps coincide at an internal edge \(uv\) of \(C\), then \(\{u,v,x,y\}\) is Hamiltonian.

**Proof.** In the first case no consecutive triple in the simultaneous order contains both \(x\) and \(y\); every triple is inherited from one of the two given Hamilton paths. In the adjacent case there is exactly one new triple, so boundary reversal gives the alternative. In the common internal gap, both
\[
(u,x,v),\qquad(u,y,v)
\]
are tight. Among the boundary pair on \(\{x,y,u\}\) or \(\{x,y,v\}\), the tight orientation extends one of these triples to a Hamilton path on the four vertices. \(\square\)

Thus, if neither a larger Hamiltonian support nor a reverse triple nor a Hamiltonian four-set occurs, two compatible extensions use the same endpoint gap.

Three extensions of one four-set cannot all remain featureless.

**Lemma 5.** Let \(C\) be a four-set and \(r_1,r_2,r_3\notin C\). If each \(C\cup\{r_i\}\) is Hamiltonian, then at least one of the following holds:
1. two chosen Hamilton paths have an order disagreement on \(C\);
2. \(C\cup\{r_i,r_j\}\) is Hamiltonian for some \(i\ne j\);
3. a Hamiltonian four-set lies in \(C\cup\{r_1,r_2,r_3\}\);
4. a tight triple through two roots reverses an edge of one chosen path.

**Proof.** If the induced orders on \(C\) disagree, (1) holds. Otherwise all roots are inserted into one common order on \(C\). Lemma 4 gives (2), (3), or (4) unless all three occupy one endpoint gap. In that remaining case assume they all precede \(c_1\). Failure of every pair union to be Hamiltonian forces
\[
(c_1,r_i,r_j)
\]
tight for every ordered pair \(i\ne j\). One of
\[
(r_1,r_2,r_3),\qquad(r_3,r_2,r_1)
\]
is tight, so one of
\[
(c_1,r_1,r_2,r_3),\qquad(c_1,r_3,r_2,r_1)
\]
is a Hamilton path. This gives (3). The common terminal gap is symmetric. \(\square\)
