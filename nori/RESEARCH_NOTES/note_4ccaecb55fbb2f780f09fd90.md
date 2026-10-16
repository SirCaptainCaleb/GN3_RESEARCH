# Antipodally paired directed two-factorizations and reversible matching permutations

- Stable ID: note_4ccaecb55fbb2f780f09fd90
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: eulerian, one-factorization, directed-cycles, reversible-permutation
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10487_3
- Updated session: session_nori_r10487_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

### Antipodally paired directed 2-factorization

Let \(c\) be a perfectly balanced antipodally odd coloring on \(Q_N\) with \(N=2m\ge4\). The red edge graph \(R\) is \(m\)-regular and bipartite. By the bipartite one-factorization theorem, its edge set partitions into \(m\) perfect matchings,
\[
E(R)=M_1\sqcup\cdots\sqcup M_m.
\tag{EF1}
\]
Antipodal translation \(\tau(x)=\bar x\) maps the red edge graph bijectively to the blue edge graph. Therefore the blue edges split into perfect matchings \(\tau(M_j)\).

**Theorem.** For each \(j\), the spanning 2-regular subgraph
\[
F_j=M_j\cup\tau(M_j)
\]
is a union of alternating-color directed cycles under the canonical Eulerian orientation. Its directed cycles occur in distinct antipodal-reversal pairs. Moreover
\[
\boxed{E(Q_N)=F_1\sqcup\cdots\sqcup F_m.}
\tag{EF2}
\]
Thus every balanced legal coloring admits a decomposition into \(m\) antipodally invariant directed cycle covers, each with one incoming and one outgoing arc at every vertex.

*Proof.* Every vertex meets one red matching edge and one blue matching edge of \(F_j\). The canonical orientation points the red edge outward at even vertices and the blue edge inward there, reversing those roles at odd vertices. So each vertex has one incoming and one outgoing \(F_j\)-arc and each connected component is a directed cycle alternating colors. Antipodality maps \(F_j\) to itself, reverses every arc, and acts without fixed points on the geometric realization of the cube. A self-antipodal directed component would yield an orientation-reversing involution of its traversal circle with a fixed point; hence the directed cycles come in distinct antipodal pairs. The perfect matchings partition all red and blue edges, proving (EF2). \(\square\)

**Paired-lift specialization.** For the complementary paired lift \(C_i(x,y)=c_i(x)\), \(C_{m+i}(x,y)=1-c_i(x)\), the set of red edges in the two directions \(\{i,m+i\}\) is a perfect matching \(M_i\). Its blue antipodal mate is the set of blue edges in the same two directions, and \(M_i\cup\tau(M_i)\) partitions into directed four-cycles of those pair-faces. Thus (EF2) generalizes the edge-disjoint directed-square decomposition of the standard lift to arbitrary balanced colorings, with longer cycles replacing squares.

**Algebraic permutation form.** Treat each perfect matching \(M_j\) as a fixed-point-free involution \(r_j\) on cube vertices, taking each vertex to its red matching neighbor. Its blue matching involution is \(b_j=\tau r_j\tau\). On even-parity vertices, two successive directed steps of \(F_j\) act as
\[
T_j=b_jr_j=\tau r_j\tau r_j,\qquad
\tau T_j\tau=T_j^{-1}.
\tag{EF3}
\]
Thus the oriented 2-factors provide an ensemble of reversible permutations of the even-parity vertex set, whose cycles are the even-vertex halves of the directed alternating cycles. This is a potential entry point for permutation/rainbow-path methods; no direction-simple antipodal path is asserted.
